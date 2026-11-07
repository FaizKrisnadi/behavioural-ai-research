# Do shopping agents follow a user's opinion?

This exploratory study asks whether a user's initial factual belief changes what an AI agent recommends when asked to compare products. Four agent setups—AutoClaw, OpenBot Chief of Staff, Codex and Muse—received five shopping comparisons, each in three versions: no stated belief, a belief favouring the first product, and a belief favouring the second. A new chat or task was intended for each run.

The [recommendation table](results.md) records the observed answers and failures. Most recommendations did not change across the three versions. One Muse Dyson comparison changed with the stated opinion; the agent also corrected the user's factual claim in one version, so the recommendation alone does not establish bias. Codex showed other changes, including two different answers to the same charger prompt. Two OpenBot runs ended with content refusals and no final recommendation.

These are early observations, not conclusive findings. Each version was tested once per setup apart from retries and a duplicate; timing, prices, search results, settings and persistent memory may differ. Four manually entered Muse prompts have not been verified in full in the captured view. Search traces and factual claims have not been fully audited. The neutral prompt also omits the belief sentence entirely. The draft protocol was not externally preregistered.

The [prompt design](prompts.md), [draft protocol](protocol.md) and [case files](cases/) show what was planned. Some runs were entered manually after execution problems; original failed and mismatched attempts were retained in the working records. Full transcripts are not part of this public release yet. No purchases were made.
