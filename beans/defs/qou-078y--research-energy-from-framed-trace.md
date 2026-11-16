---
# qou-078y
title: 'RESEARCH: is there a crossing-additive energy derived from the framed Markov trace?'
status: in-progress
type: task
tags:
    - mass-energy
    - research
created_at: 2026-11-15T20:26:03Z
updated_at: 2026-11-16T09:50:00Z
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

## Update 2026-11-15 (Lean + info route)
- PR #8005 (issue #8004): exclusion theorem (additive braid-invariant ⇒ c·writhe) sorry-free; HeckeGS σ⁻¹ and photon σ₀⁻¹ fixed; reduced cost + |τ| ≤ M·cost bound with Mₙ(q) as hypothesis.
- Info route (project file qou-crossing-energy/result-info.md): 𝔪(q=1) = 2^{components} on all 11 test braids (proof sketch: tr = z^{n−cyc} at q=1, z=1/2). 𝔪 is not a positive state sum (trefoil, Borromean). 𝔈 = 𝔪c_q² is linear in 𝔪, so not Landauer-derivable; Landauer gives T·ln 𝔪.
- Still open: Lean the q=1 counting theorem; owner call on vertex-algebra-relations axiom tr(σ)=tr(σ⁻¹).

## 2026-11-15: QUO-3a withdrawn; c₁ is the determinant character

- Owner chose options 1 and 3. Option 1 pushed to PR #8005 (e38b10f9f): `axiom first_chern_vanishes` removed; proved `trace_sub_trace_inv` (τ(x) − τ(x⁻¹) = h·τ(1)) and `trace_ne_trace_inv`; .md QUO-3a withdrawn, wr(a) = abelianisation writhe, relations 26 → 25.
- Option 3 (pre-registered, project file qou-crossing-energy/result-c1.md): the c₁ candidate is the determinant character. det ρ_λ(σ) = ±q^{c₁}, c₁(V_λ) = χ^λ(transposition); log_q|det ρ(β)| = c₁·w(β). det(Ad) = 1 and c₁(regular) = 0 for every λ, n = 2..5, exact. So the true "c₁(Ad A) = 0" holds identically and constrains nothing.
- Open: whether the crossing-energy writhe coefficient is a y_λ-weighted sum of c₁(V_λ). Not tested.

## 2026-11-15: option 1 Lean landed; option 3 energy link tested (scope-a negative)

- PR #8005: `QOU/Braiding/DeterminantChern.lean` — `det_evalWord` (det ρ(β) = det ρ(σ)^writhe), `det_kronecker_inv_transpose` (det of Ad = 1). Sorry-free.
- Pre-registered H1: crossing-energy writhe coefficient a = [2]/2 vs Σ_λ y_λ c₁(V_λ). FAIL as predicted: H1 = (q⁴+1)/(q²+1)² = 1 − 2/[2]² for n = 2..5 (n-independent, measured not proved). Equals the corpus constant α (augmentation/z_D Q_β ratio) as a rational function; identity of objects not established. Project file qou-crossing-energy/result-c1-energy.md.

## 2026-11-15: both observations proved (owner "1 and 2")

- `markov_average_c1` (PR #8005): Σ y_λ c₁(V_λ) = (2z − h)/[2] for every n, from tr(1)=1, tr(σ)=z only; `eigen_trace_split`: χ_λ(σ) = f h/2 + c₁[2]/2 (the crossing-energy split with ℓ↔f, w↔c₁).
- `trace_deltaS`: tr_z(Δ_S) = −(h/2)(2z − h), so the z_D/augmentation Q_β ratio α is the same (2z − h)/[2]. Δ_S = −(h/4)Σ(σᵢ+σᵢ⁻¹). Told the Q_β thread; no durable Q_β edit made.

## 2026-11-15: sign structure (continue, option 1)

- χ_λ(σ^ε) = ε·f·h/2 + c₁·[2]/2 but E(σ^ε) = ε·[2]/2 + h/2: in a trace the sign rides on the dimension term, in E on the writhe term; related by q ↦ iq. E uses the two eigenvalues of σ (symmetric channel for +, antisymmetric for −), not those of σ⁻¹. No new Lean (all one-line ring facts). PR #8005 ready; merge blocked by auto mode pending owner wording.

## 2026-11-15: options 2 and 3 of "continue"

- 3: Markov measure μ_λ = y_λ f^λ at z_D equals f^λ[n−2k+1]/[2]^n on two-row λ (exact, n = 2..6): the quantum-dimension share of spin sector k in (C²)^⊗n; denominator [2]^n = 𝔪(unlink). Sector entropy grows ~ (1/2) ln n vs ln 𝔪 = n ln[2]. Not an energy. Project file result-entropy.md.
- 2: Lean HeckeEigenSplit (PR #8005): det/trace of any Hecke generator matrix from its two eigenvalue multiplicities; c₁ = (2tr − dim h)/[2]. The q=1 identification with χ^λ(s) still cites Tits deformation.


2026-11-15: PR #8005 rebase-merged into main at 395ca05e9; issue #8004 closed.


2026-11-16: info-theory line Leaned. Issue #8112, draft PR #8113 (classical trace z^(n-cyc) at z_D(1)=1/2 gives 2^c; two-row Ocneanu weight at z_D = [n-2k+1]/[2]^n, Markov measure = spin-sector split, reading depends on G3.4; not_landauer remark).

## 2026-11-16: three-directions round + p/n mirror (handover record)

- Merged #8113 (issue #8112): 𝔪(1) = 2^c via tr(w) = z^{n−cyc} (`MarkovTraceClassicalLimit.lean`); spin-sector Markov measure at z_D, W_(n−k,k) = [n−2k+1]/[2]ⁿ (`SchurWeyl/SpinSectorMeasure.lean`, depends on G3.4 + Ocneanu uniqueness, stated in docstring); non-Landauer remark.
- Merged #8115 (issue #8114): equality lemmas for the Hecke cost bound (`UGB/.../HeckeReducedCost.lean`).
- Pre-registered directions (project file qou-crossing-energy/result-three-directions.md):
  - Tightness: M = 1 only at w = 1 below the thresholds; M > 1 from n = 7 at q₀. So 𝔈 is never an exact operation count (scope a).
  - Positivity of 𝔪: n = 2 rule proved; n = 3 sector condition sufficient, not necessary. n ≥ 3 characterisation OPEN.
  - Dead-block entropy ΔH is sublinear and does NOT track binding (scope a).
- p/n mirror via γγ walk (result-pn-mirror-gg-walk.md): the #8108 p and n words are a partial mirror. γγ core bar-even; quark blocks mirror exactly in χ₃, differ by −h/2 in the bar-odd part of χ₂₁. Sent to the weak-vertex and audit threads.

### Still open
1. Test #8111's F₃ condition against bar. Bar is semilinear (q ↦ q⁻¹): build a linear version first (bar ∘ coefficient involution).
2. Optional Lean: n = 2 positivity criterion; sector formula 𝔪(β) = q^{−2w} Σ [n−2k+1] χ_k; mirror = bar, 𝔪(β̄)(q) = 𝔪(β)(q⁻¹); long-transposition trace tr T_(1n) = z_D·r^{n−2}.
3. Characterise positivity for n ≥ 3.
4. Check max |tr T_w| at n = 6.

## 2026-11-16: F₃ (#8111) vs bar — done, pre-registered, all checks pass
Project file qou-crossing-energy/probes/f3-bar/ (preregistration, probe, output, result). Linear bar
X ↦ S^⊗3 X(q⁻¹) S^⊗3 is the mirror σᵢ ↦ σᵢ⁻¹ composed with u↔d (S⊗S Ř(q⁻¹) S⊗S = Ř⁻¹). It does not fix F₃ but
keeps every signed word (340, length ≤ 4) in the F₃ commutant, fixes the pivot, swaps p/n spaces:
Tr_p(β̄)(q) = Tr_n(β)(q⁻¹) = Tr_p(β)(q⁻¹); T_p/T_n = q² on mirrors. Verdict scope (a): bar adds no u↔d
breaker; the γγ-walk p/n χ₂₁ difference is element choice (qou-99qc). Lean candidate `mirror_trace_bar` not written (awaits owner).
