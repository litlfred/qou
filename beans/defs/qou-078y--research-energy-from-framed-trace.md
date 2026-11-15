---
# qou-078y
title: 'RESEARCH: is there a crossing-additive energy derived from the framed Markov trace?'
status: in-progress
type: task
tags:
    - mass-energy
    - research
created_at: 2026-11-15T20:26:03Z
updated_at: 2026-11-15T21:10:00Z
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

## Result 2026-11-15 (thread "Find a trace-derived crossing energy")
Pre-registered checks C1-C4 all held (exact Q(q), sympy; files in project folder qou-crossing-energy/).
- C1 (structural, scope b, invariant = abelianisation of B_n is Z): a letter-additive function invariant
  under free cancellation and the braid relation is c*w. E_cross(sigma sigma^-1) = q - q^-1 != 0, so
  E_cross is not a braid function. In E_cross = w cosh(lambda) + l sinh(lambda) (prop:crossing-energy-decomposition)
  only the w part can come from any trace; l sinh(lambda) is word length (gate count) times sinh(lambda),
  i.e. computational cost, vanishing at q = 1. The trace-fixed writhe coefficient is -2 ln q in log m, not cosh(lambda).
- C2: m = [2]^n q^(-2w) tr_D; q^(2k) m(sigma^k) = [3] q^k + (-q^-1)^k (k <= 8): log m not additive.
- C3/C4: tr is linear in the GS normal-form coefficients, so m <= [2]^n q^(-2w) M_n(q) heckeCost(beta),
  equality on the identity (cost 1, mass [2]^n). M_n = 1 only below q*_n = 1.4656, 1.2414, 1.1712, 1.1344
  (n = 2..5), argmax the transposition (1 n): z_D((q^4+1)/(q^2+1))^(n-2); q*_n -> 1.
- Lean defects in HeckeGS.lean section 5 (not fixed): embedNegativeGen inverse is wrong (should be sigma - h),
  braidToAlg never reduces to normal form, and -0 = +0 in augmentedBraidElement.
- Info reading: m(unlink_n) = (2 cosh lambda)^n = partition function of n two-state systems (2^n at q=1).
Owner choice 2026-11-15: record (this note) + Lean the exclusion (PR) + then the info-theory route.
