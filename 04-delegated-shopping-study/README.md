# Does an AI shopping agent take your word for it?

A shopping request can contain two different things: what the user wants, and what the user believes to be true. I wanted to see how AI agents handle both when those beliefs may be wrong.

I gave four agent setups five real-product comparisons. For each comparison, I used three versions of the request: one without a stated belief, one favouring the first product on a factual measure and one favouring the second. The budget and shopping priorities stayed the same. The agents were asked to research and recommend, not purchase.

The answers suggest why the distinction matters. In one Dyson comparison, Muse recommended the product the user believed was stronger—but explicitly corrected that belief and gave price as a reason for its choice. Its recommendation differed under the opposite belief, but the two answers also reported different prices. We cannot tell from these runs what caused the change.

[Read the research note](research-note.md) · [Compare the recommendations](results.md) · [See the prompts](prompts.md)

## What is here

- The [research note](research-note.md) explains the question, what happened and what a follow-up would need to check.
- The [recommendation table](results.md) shows the responses by agent, product pair and prompt version, including two failures and a duplicate.
- The [prompt design](prompts.md), [historical draft protocol](protocol.md) and [case files](cases/) document the planned design and background evidence.

## Agent setups

| Setup | Model recorded |
| --- | --- |
| OpenBot | Inception Mercury 3, medium setting |
| Codex | GPT-6.1 Terra, as recorded in session context |
| AutoClaw | `zai_auto` in response traces; exact underlying model version not established |
| Muse | Underlying model version not established |

These are agent configurations, with their own tools and instructions. They are not a controlled comparison of models alone.

## How to read the results

This is an exploratory exercise, not a measure of how often agents are biased. Each version was run once per setup apart from retries and a duplicate. Runs occurred at different times; prices, search results, settings and persistent memory could also differ. Four manually submitted Muse prompts have not been verified in full in the captured view. Product claims and search traces have not been fully audited.

Some runs were entered manually after execution problems. Failed and mismatched attempts were retained in the working records, but full transcripts are not included in this public release. The protocol is a historical draft, not an external preregistration. No products were purchased.
