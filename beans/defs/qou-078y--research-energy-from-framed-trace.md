---
# qou-078y
title: 'RESEARCH: is there a crossing-additive energy derived from the framed Markov trace?'
status: todo
type: task
tags:
    - mass-energy
    - research
created_at: 2026-11-15T20:26:03Z
updated_at: 2026-11-15T20:26:03Z
parent: qou-6qbv
---

Owner request 2026-11-15 (thread "Make the Lean foundations real").

## Background
`thm:mass-energy-equivalence` claimed E_cross = m·c_q², where E_cross is the
per-crossing sum (q per positive crossing, −q⁻¹ per negative one, `def:crossing-energy`)
and m is the framing-corrected Markov trace of `def:mass-identity`,
(1+q²)ⁿ q^(−n−2w) ∫_A ρ(β). That statement is false: on the trivial braid E_cross = 0
while m = (1+q²)ⁿ q^(−n) ≠ 0. On σ₁ ∈ B₂, E_cross = q but m·c_q² = (1+q²)/(q(q−1)²).
Owner ruling: the energy is now *defined* as 𝔈 = m·c_q² (no subscript); crossing
energy keeps its subscript and is unchanged.

The old proof sketch's Step 1 (ribbon trace = per-crossing sum) is false:
Tr((K⊗K)Ř) = q(q²+1), Tr((K⊗K)Ř²) = (q²+1)(q⁴+1)/q²
(/mnt/project-files/qou-derivation-chain/bridge-b/h1_hierarchy_origin.md §2).

## Question (open; outcome unknown)
Is there an energy functional that is (a) additive over crossings, like E_cross, and
(b) derived from the framed trace rather than chosen? Candidate: log of the framed
trace. Its framing factor contributes −2w·log q, which is crossing-additive (w = writhe);
the remaining log ∫_A ρ(β) is not additive in general.

## Suggested first steps
1. Formalize-first: state the relation of log(framed trace) to w and to E_cross over a
   generic ring where possible; find the invariant that would forbid or allow additivity.
2. Check small braids exactly (symbolic ℚ(q), no float): trivial, σ₁^k in B₂, the trefoil.
3. Report a scope-(a) negative if no additive part beyond the writhe term exists.

Anti-fit: no choice of word, branch, or truncation against measured masses.
