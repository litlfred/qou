---
# qou-w6x3
title: 'Option 2 of qou-hxz4: re-embed the binding producer''s word on 3A strands — does it restore level-locality?'
status: completed
type: task
priority: normal
created_at: 2026-09-12T07:09:28Z
updated_at: 2026-09-12T07:39:26Z
---

## ANSWERED 2026-09-12 (branch claude/binding-word-3a-reembedding-2026-09-12, PR #7202)

**NO for A >= 3, YES for A = 2 — and the obstruction is NOT the one #7173
named.** #7173 diagnosed the binding words' non-locality as the fixed-H_k
embedding (generator index cycling `g mod (k-1)`). Measured, that is not what
decides option 2. The decider is the **coupling graph**, which re-embedding
does not touch.

Probe `computations/probes/binding_word_3A_reembedding_probe.py` (18/18, 47 s,
mpmath 70 dps, proton pin as string, no float64). Lean
`QOU/Hecke/ContiguousCouplingGraph.lean` (7 decls, sorry-free, `#print axioms`
= exactly [propext, Classical.choice, Quot.sound]). Audit
`docs/audits/2026-09-12-binding-word-3A-reembedding.md`.

**The structures, instrumented from the producers.** `_step_chain_generic`
appends one inter-nucleon letter PER PREVIOUS NUCLEON, so `C(A,2)` in total —
the **complete graph K_A**. `atom_braid_word_3A` bonds only consecutive
nucleons at gen `3k+2` — `A-1`, the **path P_A**. Measured A=2..6: 1/3/6/10/15
against 1/2/3/4/5.

**Contiguity gives the path and nothing else.** Exhaustive over all `A!` block
orderings, A=2..7: the coupling graph is always `P_A`; `K_A` reachable iff
`A <= 2`. Proved general-A as `complete_coupling_forces_A_le_two` — a generator
crosses two ADJACENT strands and blocks are three wide, so a coupling from
nucleon `i` lands in `i+1` and nowhere further.

**Dropping contiguity does not rescue it.** `K_A` is layout-realisable iff
`A <= 6` (exhaustive DFS; A=7 impossible, and the counting bound
`C(A,2) <= 3A-1` excludes EVERY `A >= 7` — 3A strands have only 3A-1
adjacencies; proved as `pair_count_exceeds_adjacency_budget`). But exhaustively
over every K_A-realising layout, the max number of CONTIGUOUS nucleon triples
is 2/3 at A=3 and **0** at A=4 and A=5 (234 / 5736 / 64986 layouts). From 4He
up, not one nucleon keeps its three strands together, so every intra crossing
would need conjugating too.

**The conjugated-bond escape destroys the win.** 3 segments, largest holding
`3A-3` of `3A-1` generators (all but two), against the mass word's `2A-1`
segments of largest size 2. Order-free floor `3A-5`: the conjugating walk
BRACKETS its crossing, so gens `[2, 3A-4]` share a segment wherever the rest of
the letters go. Measured price at A=3, same H_9, same 30 partitions: mass word
**0.349 s**, conjugated binding word **41.311 s** — **118x**.

**A = 2 works completely.** The deuteron's single pair IS the one adjacency, so
no conjugation: level-local with EVERY segment holding one generator (finer
than the mass word's, because the binding intra chain is grouped where
atom_braid_word_3A's is alternating). Path sum **7.8x faster** than on the
fixed-H_k word.

**AND THE VALUE MOVES — this is the load-bearing part.** At A=2 both embeddings
live in the SAME H_6 with the SAME 23 letters and the same (c,d) offsets,
differing ONLY in generator assignment. chi^lambda differs on **9 of the 11
partitions of 6**, max relative 1.43; lambda=[5,1] goes -0.827 -> +3.216, a
SIGN CHANGE. The two 1-dim irreps are blind to the embedding
(chi^(6) = prod(q+d) exactly), so the whole move sits in dim >= 2.
Cross-checked against an independent dense Young-seminormal matrix product at
< 1e-45 on both words, every partition.

**Corpus defect found and fixed.** `hecke_core_legacy.py:1040-1042` asserted
*"The character chi_lambda(sigma_k) is independent of k (class function), so any
embedding of crossings into sigma_1, sigma_2, ... yields the same trace."* The
premise is true and the conclusion is false — chi is a class function on the
GROUP, not a function of the multiset of letters. Corrected in place with the
measurement. NOTE the neighbouring claim at :1004 (`_step_chain_22`, lambda =
(2,2) only) is TRUE, for a stronger reason than it gives: rho(sigma_1) and
rho(sigma_3) are the SAME MATRIX in (2,2), both diag(q, -q^-1), so they
substitute inside any word. Equal characters of single generators would not have
sufficed. An earlier draft of the audit conflated the two sites; corrected.

**Also recorded as NOT established:** an attempted direct counterexample in H_4
(chi^(3,1)(s1 s2) vs chi^(3,1)(s3 s2)) is not one — those are equal by the w_0
conjugation `s_i -> s_{n-i}` that qou-hxz4 already recorded as a genuine trace
identity, and the residual seen was ~1e-70, the floor of the arithmetic. The
refutation rests on the A=2 H_6 measurement alone, where the moves are O(1).

**Nothing wired, no recorded number moves, no route adopted.** The A=2
comparison is reported, not acted on: choosing an embedding by the number it
produces is selection against the target.

**Residual owner decision** (framed, not enacted) — see qou-8274.
