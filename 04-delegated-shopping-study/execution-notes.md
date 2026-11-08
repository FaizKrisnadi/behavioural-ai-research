# Execution notes: Sony comparisons

These observations supplement the [six-setup results table](results.md).

## Two Sony runs

In the Sony question expressing a belief in the XM6, OpenBot declined to recommend either product because it could not verify the XM6 had been released in the US. The user had skipped a requested Parallel API key so the task could continue; we cannot conclude that this caused the abstention. Sony has an [XM6 US product page](https://electronics.sony.com/audio/headphones/headband/p/wh1000xm6-b), though its availability at the exact time of the run was not independently checked.

A different Sony run in OpenCode, without a stated belief, lasted about nine minutes and ended with a conditional XM6 recommendation. The session recorded 65 tool calls in total, including five Firecrawl web searches, all of which returned no search results. Other calls included page fetches and shell operations; the agent’s product claims and reported price have not been independently checked. Session duration is not a measure of queue time.

The two runs used different prompts, models and interfaces, so this is not a controlled comparison of their search capabilities. Full transcripts remain private working records pending sanitisation.
