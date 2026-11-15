---
# qou-078y
title: 'RESEARCH: is there a crossing-additive energy derived from the framed Markov trace?'
status: todo
type: task
tags:
    - mass-energy
    - research
created_at: 2026-11-15T20:26:03Z
updated_at: 2026-11-15T20:32:23Z
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

## Owner lead (2026-11-15): crossing energy ~ computational cost
Owner: "crossing energy - related to computational cost". Starting points in the corpus:
- UGB `GrobnerShirshov/HeckeGS.lean`: `heckeCost_well_defined`, `threading_cost_unique`
  (cost of reducing a braid word to Hecke normal form; both conditional on the
  confluence hypotheses, now including `hlc`).
- `information-theory/photon-threading-mass.md` + `lean/QOU/Information/photon_threading_mass.lean`
  and `lean/QOU/PhotonThreading.lean` (threading cost and mass).
- `information-theory/planck-scale-computation.md`, `computational-spacetime-observer.md`.
- `mass-theory/graded-hecke-energy-truncation-bound.md`.
Question to settle: is E_cross (or a weighted crossing count) the reduction cost of the
Gröbner–Shirshov rewriting, and does the framed-trace energy 𝔈 = m·c_q² bound or equal
a cost functional? Each Hecke rewrite σ² → (q−q⁻¹)σ + 1 is one crossing step, which is the
natural link.

## Related claim found 2026-11-15: prop:photon-threading-mass
`prop:photon-threading-mass` states 𝔪 = (q−1)² Σ_{Hecke steps} |c_w|·|q−q⁻¹|, i.e. 𝔈 equals
the photon threading cost. With the mass of `def:mass-identity` the trivial braid refutes it
as stated: threading through no crossings takes 0 Hecke steps, while 𝔪 ≠ 0. Not changed
yet (owner decision). Its Lean is a context class (`PhotonThreadingMassContext`).
This is the cleanest form of the owner's "crossing energy ~ computational cost" lead:
the cost side is well defined (confluent GS reduction), the open part is its relation to 𝔈.
