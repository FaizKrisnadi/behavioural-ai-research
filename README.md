# When AI agrees or disagrees: research exercises

How do language models interpret the same text, and do their answers change when a user states an opinion? This repository brings together a model-comparison component of my master's thesis and exploratory experiments on user influence.

## 1. Comparing models in my master's thesis

My thesis studied how Indonesian elites discuss Chinese development finance and foreign direct investment. One component used AI-assisted analysis of news articles. The thesis repository records agreement between ChatGPT, Claude and Gemini on a 100-article validation sample. For example, the reported ChatGPT–Claude agreement was 72% for stance and 81% for frame.

[Read the thesis comparison and its code](01-thesis-model-comparison/README.md)

The recorded summary is included here, alongside a **newly written** tool for comparing labels. The original item-level validation labels and model-calling code are not included, so this tool has not reproduced the original thesis results. The existing [thesis repository](https://github.com/FaizKrisnadi/master-thesis) provides further background, but its numbered scripts are placeholders and must not be run as a reproduction pipeline; several can overwrite outputs.

## 2. Does a user's opinion change an AI's answer?

I tested four claims based on data from the World Bank, UNICEF, Statistics Indonesia and the IEA. For each claim, I asked two versions in fresh chats: one said the user believed the claim was correct, and the other said it was incorrect. The evidence and claim remained the same.

Four chatbots and two personalised agents produced **48 responses in 24 pairs**. The four chatbots and Muse gave the same verdict in every pair. OpenBot did so in three clean pairs; in the fourth it initially said “SUPPORTED,” then corrected itself to “NOT SUPPORTED.” Gemini and OpenBot each paired older poverty thresholds with rates reported under updated thresholds. Kimi could not be tested because the service reported high demand.

[Read the full experiment, responses and code](02-chatbot-opinion-experiment/README.md)

The prompts were deliberately simple, there was one answer per condition, and product settings and memory were not fully controlled. These results describe this exercise; they do not show how often AI systems agree with users in general.

## 3. Does a user's opinion influence an agent's answer?

I ran a small pilot across Muse, AutoClaw, OpenBot and Codex, using two factual product comparisons. All eight first-attempt answers given an incorrect opinion corrected it. The questions were easy, and incomplete search records mean the pilot cannot establish whether the agents sought balanced evidence. One unanswered OpenBot attempt was retried separately.

[Read the pilot, prompts and recorded responses](03-agent-opinion-pilot/README.md)

## 4. Does a shopping agent take your word for it?

When someone asks an AI agent to recommend a product, they may bring a mistaken belief as well as a genuine preference. I gave four agent setups five shopping comparisons and varied the belief stated in each request. Most recommendations stayed the same; some changed, and two OpenBot runs ended without an answer.

One response captures why the explanation matters: Muse recommended a vacuum that the user believed was stronger, while correcting that belief and pointing to price. Different prices appeared in the opposing-belief run, so the change in recommendation cannot be attributed to the stated opinion alone. The study is exploratory, with one run per version apart from retries and a duplicate.

[Read the shopping study and research note](04-delegated-shopping-study/README.md)

## Running the code

The first two folders include a README and use Python 3 with no external packages. The experiment analysis uses manually recorded responses; it makes no model calls. The thesis comparison tool accepts supplied labels and cannot reproduce results without the original item-level data. The research was assisted by GPT 6.1 Terra.
