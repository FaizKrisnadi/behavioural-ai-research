# Research handoff

This repository brings together a thesis model comparison and three related experiments. The current project is [the shopping-agent study](04-delegated-shopping-study/README.md): six agent setups were asked five product-comparison questions in three versions. The goal is to examine how a user's factual belief relates to an agent's evidence and recommendation, as a starting point for research on reliable AI-assisted decisions.

## Where to start

1. Read the [research note](04-delegated-shopping-study/research-note.md) for the question, design, observations and limits.
2. Read the [recommendation table](04-delegated-shopping-study/results.md), then the [execution notes](04-delegated-shopping-study/execution-notes.md). The table covers all six setups, including failed runs and a duplicate.
3. The [case files](04-delegated-shopping-study/cases/) and [prompt design](04-delegated-shopping-study/prompts.md) document the questions. [Muse product links](04-delegated-shopping-study/muse-product-links.md) lists the product cards visible in its 15 chats.

## Evidence and limits

The public repository does not contain the full transcripts or tool histories. The recommendation table is provisional: not every classification, product claim or source has been independently checked. The four longest manual Muse prompts were checked visually, not compared byte-for-byte. Product cards do not establish what the agent searched in the background. A duplicate Codex attempt and the OpenBot failures are part of the record; do not silently discard them or select an answer based on the desired result.

A local backup of collected answers and available application records exists on Faiz's computer under `Documents/Behavioural AI Lab backups/study-2026-11-08`. It contains private session and account identifiers and is not automatically available to an agent on another device. It should be reviewed and sanitised before any public release. Background browser activity and some unavailable tool payloads may not be recoverable from the exports.

## What to do next

- Check each recommendation and the treatment of the user's factual belief against its original answer; distinguish corrections, agreement, abstention and conditional recommendations.
- Review original search traces where available, check key factual claims and report uncertainty; never infer a search solely from a citation or product card.
- Preserve and explain retries, duplicate attempts, failures, prior context, differing execution times and model/tool settings. Define any selection rule before comparing outcomes.
- If the goal is stronger evidence, design repeated runs of identical prompts and a separate study using real urban data. Neither a stable rate of bias nor an urban result has been established by the present study.

Faiz prefers simple English, connected prose and clear evidence. Present this as an exploratory research project, not a benchmark or a proof that an agent is trustworthy. Do not make purchases, publish private records, or contact anyone without appropriate authorization.
