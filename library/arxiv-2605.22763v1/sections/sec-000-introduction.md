---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing mathematics research with AI-driven formal proof search"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
doc_brief: "Advancing mathematics research with AI-driven formal proof search — 14 sections: Introduction; AlphaProof Nexus; Systematic Evaluation on Open Prob"
---
Large language models (LLMs) have recently shown remarkable promise in solving complex
mathematics problems [21, 65], butunreliabilityremains a primary barrier to their integra-
tion into mathematics research. Because LLM-generated natural language proofs can contain
subtle logical errors, or “hallucinations,” they require expensive expert review. Mistakes in
unreviewed intermediate steps can cascade through a proof, limiting the complexity of tasks
that can be delegated to AI.
Recent efforts [29, 1] mitigate these issues by using AI to generate proofs in formal
languages like Lean [43], in which a compiler automatically verifies every logical step. So
far, successes of this paradigm have been concentrated in competition mathematics and
the human-aided formalization of natural language arguments [28]. In this paper, we
demonstrate its broader potential through a large-scale evaluation on open research-level
problems.
Tothisend,wedevelopedaframework,AlphaProofNexus,forLLM-aidedproofgeneration
and used it to build a basic agent in which a set of subagents independently searches for
proofs with feedback from the Lean compiler. We also developed a “full-featured” agent
in which subagents are coordinated using an evolutionary algorithm [46] and can use
AlphaProof [29], a system for olympiad-level Lean theorem-proving based on reinforcement
learning, as a focused proof tool.
Our full-featured agent autonomously solved 9 Erdős problems out of 353 attempted,
including two questions that had been open for 56 years [54, 7, 17], at the inference cost
1†Equal contributions. The first three authors are in random order. Correspondence topushmeet@google.
comandswarat@google.com.
©2026 Google DeepMind. All rights reserved
arXiv:2605.22763v1  [cs.AI]  21 May 2026
Advancing Mathematics Research with AI-Driven Formal Proof Search
of a few hundred dollars per problem. It also proved 44/492 open conjectures from the
Online Encyclopedia of Integer Sequences (OEIS), resolved a 15-year-old open question on
Hilbert functions in algebraic geometry, improved an open bound in convex optimization by
discovering a novel algorithmic parameter schedule, identified several misformalizations in
the literature, helped resolve an open problem from Ben Green’s well-known list [27], and is
aiding ongoing research efforts on quantum optics and graph theory.
Tounderstandtheimpactoftheagentdesignontheseresults,wedidapost-hocanalysisof
the performance of the full-featured and basic agents, as well as two agents with intermediate
capabilities, on the 9 Erdős problems solved by the full-featured agent. Remarkably, the basic
agent solved all 9 problems, though at a higher cost on the harder problems.
Overall, our results demonstrate the utility of LLM-powered formal proof search as a tool
for mathematics research, and point to an ongoing shift from specialized trained systems
toward simple agentic loops as LLMs become more capable. All Lean proofs and select
natural-language proofs are available inhttps://www.github.com/google-deepmind/
alphaproof-nexus-results.
