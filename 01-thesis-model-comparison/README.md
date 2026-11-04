# Comparing AI labels in my master's thesis

My thesis examined how Indonesian elites describe Chinese development finance and foreign direct investment. One component used AI-assisted analysis of news articles. For a 100-article validation sample, the existing thesis repository records how often labels from ChatGPT, Claude and Gemini agreed on each article's frame and stance.

## What is included

- `data/reported_validation_summary.csv` is a copy of the summary already included in the thesis repository. It records the previously reported results; it is not the underlying 100-article data. Source: [master-thesis repository](https://github.com/FaizKrisnadi/master-thesis), `data/diagnostics/validation_summary.csv`.
- `compare_labels.py` is a **new companion tool**, written after the thesis, for comparing labels from the same articles. It was not used to produce the thesis results and does not itself reproduce them.
- `tests/test_compare_labels.py` checks the tool using invented examples, clearly separate from the study.

The original model-specific labels are not included here. The existing repository states that the exact production prompt and the original code that coordinated the model calls are missing. Accordingly, this package does not recreate those calls or independently verify the reported numbers. It makes no model calls and requires no API key. The full news articles and interview materials are not included.

## What the recorded summary says

The existing summary reports 100 items for each comparison. For example, it records agreement of 72% for stance and 81% for frame between ChatGPT and Claude; it also reports Cohen's kappa. The summary is a record of reported findings, not proof that the labels or calculations have been reproduced here. Details: [measurement note in the thesis repository](https://github.com/FaizKrisnadi/master-thesis/blob/main/docs/llm_measurement_note.md).

## Run the new tool on labels you are authorised to use

Requires Python 3.9 or newer; no additional packages. Prepare a UTF-8 CSV with exactly one row per article and model. Required column names are `article_id`, `model`, `frame`, and `stance`; additional columns are ignored. Use consistent model names, article IDs and category spellings. A blank frame or stance is treated as missing. Provide labels only, without article text or private information.

```text
article_id,model,frame,stance
item_001,model_a,frame_x,positive
item_001,model_b,frame_y,positive
```

These two rows illustrate the format and are invented, not thesis observations. Then run:

```bash
python3 compare_labels.py path/to/labels.csv > agreement.csv
```

For each model pair and each outcome, the script uses articles with a non-blank label for both models. `paired_articles` is that number; `agreement` is the proportion with identical labels; `cohen_kappa` adjusts observed agreement for agreement expected from the two sets of labels. Kappa is blank when it cannot be calculated, such as when both models assign the same single category to every shared article. No shared non-blank labels yields `paired_articles=0` and blank statistics. Labels are compared exactly after stripping surrounding whitespace, so harmonise inconsistent coding schemes before interpreting results. Duplicate article/model rows are rejected.

To run the checks:

```bash
python3 -m unittest discover -s tests -v
```

The checks use synthetic labels only. The work was prepared with AI assistance and should be reviewed by the researcher before sharing or drawing conclusions.
