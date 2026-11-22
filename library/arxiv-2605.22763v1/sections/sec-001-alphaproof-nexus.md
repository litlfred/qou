---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-001-alphaproof-nexus
section_title: "AlphaProof Nexus"
section_number: null
pages: 2-4
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Lean.
Lean [43] is a proof assistant in which definitions, theorems, and proofs are all
mechanically verified code. Proofs are constructed via a sequence of applications of tactics,
or elementary proof steps. Lean’s compiler “executes” a proof tactic-by-tactic, tracking the
proof goals pending after every tactic. A proof is correct if it leads the compiler to a state
with no pending goals.
Lean includes a special sorry tactic, which immediately closes pending goals while
passing the type checker. Proving a theorem thus amounts to the generation of type-safe
code without sorry tactics.
Input and Output.
AlphaProof Nexus is a new framework for agents that query frontier
LLMs and the Lean compiler. The agents take as input a Lean file consisting of a target
theorem with sorry in place of a proof, along with definitions and library imports on which
the theorem depends (we refer to such a file as a proof sketch). Optionally, the user may
input additional natural-language context and domain knowledge encoded in Lean.
The input sketch is annotated with user-provided markers that delineate which code
segments the agent may modify (see Fig. 1). Within EVOLVE-BLOCK markers, the agent can
introduce helper lemmas, definitions, and proof steps. EVOLVE-VALUE markers are used to
enclose expressions (e.g., parameters) whose values the agent can change. On successful
termination, the agent outputs a sorry-free proof of the target theorem.
Agent Architecture.
The basic agent in AlphaProof Nexus (agent (A)) consists of a set
of prover subagents that execute independently with no shared state. Each subagent is a
“Ralph loop” [31] consisting of a sequence of episodes: multi-turn LLM inference loops (based
on Gemini 3.1 Pro) in which the subagent can reason via chain-of-thought and refine the
sketch using a search-and-replace tool. After each turn, the subagent uses Lean to check that
the current proof sketch compiles; if it does not, Lean’s error message is used to direct the
2
Advancing Mathematics Research with AI-Driven Formal Proof Search
/- Erdos 125 variant from
https: / / github.com / google -deepmind / formal -conjectures /
blob / main / FormalConjectures /
ErdosProblems / 125.lean. -/
namespace Erdos125
open ...
-- EVOLVE-BLOCK-START
-- You can put your definitions and lemmas here.
-- EVOLVE-BLOCK-END
theorem target_theorem_0 :
answer(
-- EVOLVE-VALUE-START
default
-- EVOLVE-VALUE-END
) ↔0 < ({x : ℕ| (digits 3 x).toFinset ⊆{0, 1}}
+ {x : ℕ| (digits 4 x).toFinset ⊆{0, 1}}
).lowerDensity := by
-- EVOLVE-BLOCK-START
sorry
-- EVOLVE-BLOCK-END
(a)
== Role and Goal == [...]
== Task == [...]
== Sketch Structure == [...]
== Prior Attempts ==
Attempt 1
8 Elo: 1505
theorem target_theorem_0 : answer(
False ) ↔0 < (...).lowerDensity ...
AlphaProof: 3/5 goals proved, 2 open
AlphaProof feeback: [...]
<natural_language_plan>
1. Define restricted-digit sets A, B.
2. Prove size bounds. [...]
</natural_language_plan>
Attempt 2
8 Elo: 1480
[...]
Attempt 3
8 Elo: 1520 [...]
== Current Plan ==
-- EVOLVE-BLOCK-START
have h_positive_density :
0 < (...).lowerDensity := by sorry
-- EVOLVE-BLOCK-END
theorem target_theorem_0 : answer(
True ) ↔0 < (...).lowerDensity ...
== Instructions == [...]
(b)
j Thought (5m 3s): “Analyzing the problem structure... The answer should be False
since the lower density is 0.”
v search_replace
3s ✓
- default
+ False
- sorry
+ constructor
+ · intro h; exact False.elim h
+ · intro h
+
have : (A+B).lowerDensity = 0
+
. . .
Ô attempt_goals_with_alphaproof
10m 1s
✓A_bound
✓B_bound
✓sum_size_bound
× independent_bases_zero_density
(3/4 proved)
j Thought (1m 35s): “AlphaProof couldn’t solve independent_bases_zero_
density... This is too monolithic. I need to decompose it: first show that for any
𝜖> 0 there exist aligned scales 𝑘, 𝑚with 3𝑘≈4𝑚, then bound the sumset gaps at those
scales.”
v search_replace
4s ✓
- lemma independent_bases_zero_density
-
: (A+B).lowerDensity = 0 := by sorry
+ lemma exists_k_m_ratio_close ...
+
:= by sorry
+ lemma gap_at_aligned_scale ...
+
:= by sorry
+ lemma independent_bases_zero_density
+
: (A+B).lowerDensity = 0 := by
+ . . .
... 4 more search_replace iterations
Ô attempt_goals_with_alphaproof
2m 40s
✓exists_k_m_ratio_close
✓gap_at_aligned_scale
✓independent_bases_zero_density
(6/6 proved ¦)
j Thought (54s): “Reflections on Tool Use”
<natural_language_plan>
1. Set answer to False ...
2. Decompose density proof into sublemmas...
...
</natural_language_plan>
è Generation complete.
è Proof validated.
õ Admitted to Population Database.
(c)
Figure 1 | Example inputs/outputs for an AlphaProof-equipped agent (applied to Erdős
#125). The user provides a Lean file with a specification of the problem, and an empty
proof body replaced with the sorry placeholder. (a) Modifications are permitted only within
EVOLVE-BLOCK and EVOLVE-VALUE markers. (b) During sketch refinement, the prover
subagent is shown an assembled prompt template with the current proof, and optionally
prior attempts/sketches, their Elo ratings, and feedback from AlphaProof’s attempts on
unsolved goals. (c) The prover reasons about the problem informally and invokes tools. In
this example, the prover invoked AlphaProof which resolved all but one goal. The prover
then decomposed that goal into three simpler lemmas, and called AlphaProof again, which
then resolved all remaining goals. The agent also produced a natural language summary of
its attempt at the end of generation.
3
Advancing Mathematics Research with AI-Driven Formal Proof Search
next turn. If the sketch contains sorry when the episode terminates, the subagent adds a
comment to the sketch summarizing the lessons learned from the episode. The resulting
sketch is the input to the next episode.
We extended the basic agent into one (B) that can query AlphaProof [29] to fill out
missing parts of sketches. Queries to AlphaProof can return a proof, disproof (a proof that
the submitted subgoal is false), or a failure message; proofs are directly substituted into the
sketch, while disproofs and failure messages are fed into the prover’s prompt.
Separately, we developed an evolutionary agent (C), inspired by AlphaEvolve [46], in
which prover subagents sample from and contribute to a shared population database of
sketches. A challenge here is the mismatch between evolutionary algorithms, which typically
assume a graduated fitness landscape, and formal proof evaluation, which is inherently
binary. To bridge this gap, we used a pool of rating agents (based on the less expensive
Gemini 3.0 Flash) to construct relative rankings of sketches based on their plausibility, clarity,
and novelty. We aggregated these rankings into Elo ratings for the sketches and used a
sampling procedure based on the P-UCB formula [30, 55] to drive the search.
Finally, we combined the AlphaProof and evolution capabilities into a “full-featured”
agent (D; see Fig. 2) in which prover subagents can use AlphaProof as well as evolutionary
search. We used this agent as the instrument in our exploration of open research problems.
