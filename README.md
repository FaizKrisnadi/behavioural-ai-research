# Behavioural AI Research

What happens when we rely on AI to interpret evidence or help us make a decision? This repository brings together work from my master's thesis and two experiments that grew out of that question.

In my thesis, I used AI-assisted coding to study how Indonesian elites discuss Chinese development finance and foreign investment. Comparing model labels raised a practical question: different systems can classify the same article differently, even when they use the same codebook.

That led me to test another source of variation: **does the opinion a user gives an AI affect its answer?** I started with simple claims about development data, then moved to agents researching products and making recommendations.

## Projects

### [1. Comparing labels in my master's thesis](01-thesis-model-comparison/README.md)

A recorded summary compares how ChatGPT, Claude and Gemini labelled a sample of 100 articles. This folder includes that summary and a later tool for comparing labels. The original article-level labels and model-calling code are not included, so the tool does not reproduce the thesis results.

### [2. Does a user's opinion change an AI's verdict?](02-chatbot-opinion-experiment/README.md)

I gave six AI systems four claims with supporting evidence. For each claim, I asked once saying I thought it was correct and once saying I thought it was incorrect. Their final verdicts stayed the same across the paired requests, although one answer initially gave the wrong verdict before correcting itself. The questions were simple and each version was tested once.

### [3. A first test with AI agents](03-agent-opinion-pilot/README.md)

Before testing open-ended decisions, I asked four agent setups two straightforward product questions. All 23 recorded first attempts got the specific comparisons right; one unanswered attempt was later retried. The pilot tested the procedure, not whether agents are generally free from bias.

### [4. Can an AI agent check your assumptions before making a decision?](04-delegated-shopping-study/README.md)

Six agent setups compared products for a shopper. Each decision had three versions: one with no stated belief and two with opposing factual beliefs. In one comparison, an agent recommended the product the user mentioned while correcting the user's claim about it. The result shows why the explanation matters as much as the final choice. The study is exploratory: timing, available information and agent settings varied, and some runs failed or were repeated.

## Code and records

Each project page explains what is available and how to inspect it. The first two projects include Python scripts; their analyses use recorded information and do not make model calls. The shopping study includes the prompts, a recommendation table and selected product links. Its full transcripts are not yet public, and the recommendation classifications still need further checking.

AI tools assisted with the research and preparation of this repository. The records and limitations are described in each project.
