---
doc_id: arxiv-2605.22763v1
doc_title: "2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof Search George Tsoukalas1† , Anton Kovsharov1† , Sergey Shirobokov1† , Anja Surina1, Moritz Firsching1, Gergely"
section_id: sec-002-systematic-evaluation-on-open-problems
section_title: "Systematic Evaluation on Open Problems"
section_number: null
pages: 4-6
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
doc_brief: "2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof Search George Tsoukalas1† , Anton Kovsharov1† , Sergey Shirobokov1† , Anja Surina1, Moritz Firsching1, Gergely — 14 sections: Intro"
---
Erdős Problems.Bloom maintains an online catalog [8] of over 1200 open problems posed
by Paul Erdős and his collaborators. The open-source Formal Conjectures repository [23]
contains Lean formalizations of a subset of these problems. We ran Agent (D) on all these
formal statements (353 at the time of the run), terminating the search if no proof was found
within 3000 episodes. The agent solved 9/353 problems (Table 1 and supplementary text);
after each solve, experts on our team validated that the Lean statement faithfully captured
the original conjecture. We have publicly shared the proofs, and our results have been logged
on Terence Tao’s wiki on AI contributions to Erdős problems [59].
Several proofs require sophisticated constructions and the synthesis of distinct mathe-
matical arguments. For example, problem #12(i), posed by Erdős and Sárközy in 1970
[18], asks if there is an infinite set𝐴 that satisfies a restrictive divisibility constraint – no
element may divide the sum of two larger elements – and which satisfies the density con-
dition lim inf𝑁→∞
|𝐴∩[1,𝑁]|√
𝑁 > 0; this problem had received attention in multiple prior works
[17, 54, 7]. Our agent constructed𝐴 as an infinite union of disjoint “blocks”𝐵𝑖⊆[𝑃 𝑖, 1.1𝑃𝑖]
for a suitably rapidly growing sequence(𝑃𝑖). To satisfy the local divisibility conditions, the
proof integrates the Chinese Remainder Theorem with the properties of sets that avoid
length-3 arithmetic progressions.
Problem #125 concerns the sumset𝐴+𝐵 , where𝐴 is the set of non-negative integers
whose base-3 representation uses only the digits 0 and 1, and𝐵 is the analogous set in base
4. The question of whether the lower density of(𝐴+𝐵) is positive was open since 1996
[12]. Our agent resolved the conjecture by synthesizing an inductive thinning argument that
exploits the Diophantine proximity of the two multiplicatively independent bases (3𝑚≈ 4𝑘).
4
Advancing Mathematics Research with AI-Driven Formal Proof Search
Lean Problem 
Formalization 
Mathematician
Natural 
Language 
Context
Domain 
Knowledge & 
Proof Libraries
Prover Subagent
LLM (+ AlphaProof)
Proof Validator
Population Database
ELO Scores
Rater Subagent
LLM Critic +
Tournaments
Sketches Goal Proofs
Formal Proof
AlphaProof Nexus
(2)
(3)
(4)(5)(1)
Figure2|Designofthefull-featuredAlphaProofNexusagent.Themathematicianprovides
as input a Lean theorem withsorry for a proof, and optionally, natural language context
and additional domain knowledge encoded in Lean. The agent architecture consists of a
basic generation-validation pipeline and an optional evolutionary framework. An LLM-based
prover subagent attempts to solve the problem by refining proof sketches(2). The subagent
may optionally call AlphaProof as a tool; each invocation of AlphaProof on a goal returns
whether a proof or disproof was found, or whether it was unsuccessful in resolving the goal.
The sketch produced in the end is checked by a validator to ensure the problem statement
was not changed unsafely and the proof compiles. If all goals are successfully proved, the
agent outputs the final Lean proof. This basic pipeline can be extended with an evolutionary
population database and rating mechanism. In this configuration, validated sketches are
admitted into the Population Database(3). Simultaneously, rater subagents sample previous
attempts(4), which are then ranked by an LLM critic in matches. The match results are
admitted back into the database(5)to update the Elo scores of the sketches. These scores
are then used by the evolutionary algorithm to sample prior sketches from the database,
constructing an overall prompt – which includes any optional inputs from the mathematician
– to condition new episodes(1).
5
Advancing Mathematics Research with AI-Driven Formal Proof Search
The agent also served as a tool for detecting and fixing misformalizations. For example,
in Erdős problems #125 and #741(i), the interpretation of “density” in the original informal
statements was amended to “lower density” and “upper density” respectively, after our
full-featured agent found proofs using density as “natural density.” Following the correction
of the ambiguity, the agent was still able to resolve the questions.
Failure Analysis.We analyzed the highest-scoring sketches (measured by Elo) across a
random sample of problems on which our agent failed. First, the agent frequently offloaded
a problem’s core difficulty into a singlesorry within a helper lemma that reiterated the
target statement in a slightly different form. Explicitly prompting against this behavior
failed to prevent it. Second, for several problems, the top sketches relied on lemmas marked
with sorry that the agent claimed were established results in the mathematical literature.
Upon manual inspection, these lemmas proved to be hallucinations. These failure modes
underscore the value of end-to-end formal verification.
OEIS.We also applied the agent to systematically explore open problems in the OEIS [56],
a massive repository of integer sequences and their known and open properties. We used
Gemini to autoformalize 492 open questions from the OEIS and applied the agent to the
resulting Lean statements. As a guard against misformalization, the agent was required to
prove “test lemmas” verifying the first few terms of each sequence against its formal definition
before attempting the target conjectures. The agent found proofs for 44 conjectures that a
manual review found to be correctly formalized and previously unproven. Two of the proofs
appear in the supplementary material.
