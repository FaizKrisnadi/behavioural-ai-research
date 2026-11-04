#!/usr/bin/env python3
"""Compare pairs of models' categorical labels on matching articles.

This is a new, independent analysis tool; it was not the code used in the
thesis. It reads previously supplied labels and never calls a language model.
"""

import argparse
import csv
import itertools
import sys
from collections import Counter
from pathlib import Path

FIELDS = ("article_id", "model", "frame", "stance")


def read_labels(path):
    """Index rows by (article, model); preserve the source labels verbatim."""
    labels = {}
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not set(FIELDS).issubset(reader.fieldnames):
            raise ValueError(f"CSV must have columns: {', '.join(FIELDS)}")
        for line, row in enumerate(reader, start=2):
            article = row["article_id"].strip()
            model = row["model"].strip()
            if not article or not model:
                raise ValueError(f"Line {line}: article_id and model are required")
            key = (article, model)
            if key in labels:
                raise ValueError(f"Line {line}: duplicate article/model {key}")
            labels[key] = {field: (row[field] or "").strip() for field in ("frame", "stance")}
    if not labels:
        raise ValueError("CSV contains no observations")
    return labels


def compare(labels):
    """Return pairwise-complete agreement; blank labels are missing, not a class."""
    models = sorted({model for _, model in labels})
    if len(models) < 2:
        raise ValueError("At least two models are required")
    results = []
    for model_a, model_b in itertools.combinations(models, 2):
        articles_a = {article for article, model in labels if model == model_a}
        articles_b = {article for article, model in labels if model == model_b}
        shared = articles_a & articles_b
        for outcome in ("frame", "stance"):
            paired = [(labels[(a, model_a)][outcome], labels[(a, model_b)][outcome])
                      for a in sorted(shared)
                      if labels[(a, model_a)][outcome] and labels[(a, model_b)][outcome]]
            n = len(paired)
            if not n:
                results.append((model_a, model_b, outcome, 0, None, None))
                continue
            observed = sum(a == b for a, b in paired) / n
            left, right = Counter(a for a, _ in paired), Counter(b for _, b in paired)
            chance = sum(left[c] * right[c] for c in left.keys() | right.keys()) / (n * n)
            kappa = None if abs(1 - chance) < 1e-12 else (observed - chance) / (1 - chance)
            results.append((model_a, model_b, outcome, n, observed, kappa))
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("labels", type=Path, help="CSV of one row per article and model")
    args = parser.parse_args(argv)
    try:
        results = compare(read_labels(args.labels))
    except (OSError, ValueError, csv.Error) as exc:
        parser.exit(2, f"Error: {exc}\n")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(["model_a", "model_b", "outcome", "paired_articles", "agreement", "cohen_kappa"])
    for a, b, outcome, n, agreement, kappa in results:
        writer.writerow([a, b, outcome, n,
                         "" if agreement is None else f"{agreement:.6f}",
                         "" if kappa is None else f"{kappa:.6f}"])


if __name__ == "__main__":
    main()
