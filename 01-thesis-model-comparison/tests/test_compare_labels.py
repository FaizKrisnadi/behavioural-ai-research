"""Checks on invented labels; these are not thesis data."""
import csv
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "compare_labels.py"


class ComparisonTests(unittest.TestCase):
    def run_csv(self, contents):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "labels.csv"
            path.write_text(contents, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                  text=True, capture_output=True, check=False)

    def test_disagreement_kappa_and_missing_values(self):
        # Four shared articles: 75% frame agreement, with 3/1 and 2/2
        # marginal frequencies, gives expected agreement .5 and kappa .5.
        # One stance label is missing and should be excluded only for stance.
        result = self.run_csv("article_id,model,frame,stance\n"
                              "1,A,x,p\n1,B,x,p\n2,A,x,p\n2,B,x,p\n"
                              "3,A,x,q\n3,B,y,\n4,A,y,q\n4,B,y,q\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = list(csv.DictReader(io.StringIO(result.stdout)))
        self.assertEqual(rows[0]["paired_articles"], "4")
        self.assertEqual(rows[0]["agreement"], "0.750000")
        self.assertEqual(rows[0]["cohen_kappa"], "0.500000")
        self.assertEqual(rows[1]["paired_articles"], "3")
        self.assertEqual(rows[1]["agreement"], "1.000000")

    def test_duplicate_keys_rejected(self):
        result = self.run_csv("article_id,model,frame,stance\n1,A,x,p\n1,A,y,q\n1,B,x,p\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate", result.stderr)

    def test_constant_categories_have_undefined_kappa(self):
        result = self.run_csv("article_id,model,frame,stance\n1,A,x,p\n1,B,x,p\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(csv.DictReader(io.StringIO(result.stdout)))[0]["cohen_kappa"], "")

if __name__ == "__main__":
    unittest.main()
