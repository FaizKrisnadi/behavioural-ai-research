# Revision protocol — does a stated factual belief change what a delegated agent finds, presents, and recommends?

**Historical draft:** This document records the design before execution. The study has since been run with deviations and manual handoffs; see [results](results.md). This draft is not a preregistration or a record of exactly what happened.

Version R1 (draft for review — nothing has been run).

## Question

When a person delegates a shopping decision and states an initial
**factual belief** about one of the options, does that change what the
agent finds, presents, and recommends? The main observed outcome is the
**recommendation** (first product / second product / no clear single
recommendation), compared across belief conditions. Evidence handling
(quality and coverage of what is cited), unsupported claims, and — only
where traces are demonstrably complete — search activity are coded
separately.

## What is varied, and what is not

- **Varied:** one sentence stating a factual belief about the same
  criterion, in identical frames for the two products ("I believe the
  {product} {criterion claim}."), with no figures, no source hints, and
  no hint of which belief the evidence supports. Conditions per case:
  `neutral`, `belief_first`, `belief_second`.
- **Constant:** the decision context, the budget, the criteria sentence
  (a legitimate preference/constraint), the "US-market versions" line,
  the request to research and recommend (or decline), cite sources, and
  not purchase.
- The evidence pack (`cases/R*.md`) records, per case, whether the
  criterion evidence supports the first belief, the second, or is
  genuinely mixed (R4 and R5 are mixed by design and never get an
  invented winner). This is researcher-side only.

## Setups

Muse (Meta), AutoClaw (Z.ai), OpenBot (open-source), Codex (OpenAI) — as
installed on this Mac, compared as setups (memory, delegation, browsing,
costs: see `../04-agent-opinion-study/setups.md`, still accurate).
Model/mode/effort recorded per run where shown; settings fixed across the
study; forced changes logged.

## Sessions, memory, carryover

- Fresh chat/task/thread per run; **account memory is never cleared or
  altered** (rule from the pilot, kept).
- Memory settings state recorded at wave start and end per setup.
- Waves are **repeated measures within the same accounts**, not
  independent replicates. Any response that references a prior
  conversation is flagged (`references_prior_conversation`).
- Because memory cannot be ruled out, all analysis contrasts conditions
  *within* the same setup; cross-setup comparisons are descriptive only.

## Randomization and order

- Fixed seeded run order per wave (`tools/make_run_sheet.py`; Wave 1
  seed 20261109, Wave 2 seed 20261110 — generated only after the cases
  are approved). Hard constraint: no two adjacent runs share a case;
  soft constraint: same-condition adjacency minimized and the achieved
  count reported.
- Out-of-order execution is allowed only when a platform is down, and
  the deviation is noted. Nothing is re-run to get a nicer answer.

## Repeats

- **Wave 1:** every cell once (setups × cases × 3 conditions).
- **Wave 2:** full repeat on a different day (fresh order). Together
  they give two observations per cell — enough to see whether an
  interesting pattern repeats, not enough for prevalence claims.
- **Wave 3 (adaptive, small):** only cells whose waves disagree on the
  recommendation; reported but never used to "resolve" an outcome.
- Failed attempts are kept forever; retries are separate rows
  (pilot rule, kept).

## Capture per run

1. Exact prompt (in the run sheet row) and the **complete, unedited raw
   answer**, verbatim, in `responses/{run_id}.md` with start/end times
   and status.
2. Visible search/tool activity — screenshots or copied panel text into
   `responses/traces/{run_id}/`, taken while visible.
3. Local logs where they exist (Codex `~/.codex/sessions/` JSONL copied
   per run; AutoClaw / OpenBot app-data logs as located in the
   feasibility batch; Muse: "server-side, not capturable").
4. Model/mode/effort shown; delegation events; usage counters where
   exposed.
5. Every cited URL re-fetched independently after the run
   (supports / contradicts / unreachable), recorded per run.

## Gates before any study run

1. Cases verified and reviewed by Faiz.
2. Independent methodological review of the cases and prompts
   (leading-instruction and confound check) — memo in `review/`;
   blockers fixed.
3. **Feasibility batch** (already authorized separately): one neutral
   run per setup on the throwaway case **T02**, with full capture. This
   is not part of the study data. Outcomes excluded from all analyses.
4. Run sheets generated and checked.

## Analysis framing (prespecified, deliberately modest)

- **Primary contrast: `belief_first` vs `belief_second`** — the two
  matched belief sentences (same frame, same criterion). The belief
  sentence introduces the criterion into the prompt, so `neutral` is
  reported as a **descriptive reference**, not a clean no-opinion
  baseline for criterion salience. Outcome: recommendation shifts toward
  the believed product, per case × setup, described plainly with the raw
  responses attached.
- Secondary, descriptive: evidence presentation (coverage/quality
  codes), unsupported claims, belief handling, visible search activity
  (full traces only), substitution flags.
- **Belief × criteria alignment, prespecified per case** (this is the
  design's structure, not a flaw): R1 — conflict (stated criteria favor
  FIRST; criterion evidence favors SECOND); R2 — cleaning favors FIRST,
  price favors SECOND; R3 — both stated criteria favor SECOND, so
  belief_first conflicts on both; R4 — criterion genuinely mixed;
  R5 — mixed with a FIRST-side lean on most published US rate
  combinations (the LG leads on electricity, IMEF, Most-Efficient and
  verified price; the Samsung's only utility lead is 51 gal/yr of
  water), stated plainly in the pack. Replacement note: the R1 and R5
  pairs were replaced on 8 November 2026 for purchasability (superseded
  files preserved in `cases/history/`); the alignment structure above
  is unchanged.
- The honest unit is the case × setup cell observed twice. No power
  claims, no percentages from tiny cells, no "N runs" as an independent
  sample. Scope and cost are proposal estimates only; the feasibility
  batch supplies observed per-run timings and usage instead of guesses.
- Wave 3 is capped at **8 runs** (chosen by primary-outcome disagreement
  across waves, one per cell at most); its runs are reported but never
  used to "resolve" an outcome.
- An observed shift is reported as a belief-conditional output
  difference. This design cannot establish cognitive confirmation bias
  (`outcomes.md`, interpretation limits).
