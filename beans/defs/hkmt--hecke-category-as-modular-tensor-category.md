---
# hkmt
title: 'BWH-1: the root-of-unity Hecke/TL quotient is a modular tensor category (S,T from Markov trace)'
status: in-progress
pr: 9776
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:20:00Z
updated_at: 2026-11-27T21:52:00Z
parent: qou-rtxm
---

Parent: rtep. TIER: ACHIEVABLE INCREMENTALLY. Formalize the Hecke/Temperley-Lieb side AS a modular
category: simple objects = Hecke blocks λ, qDim = the corpus d_q (Markov-trace/Hoefsmit, already in
QOU.HeckeAlgebra.MarkovTrace / Hoefsmit), twist θ_λ=q^{2c(λ)} (KeystoneModularTwist.theta, proved),
S-matrix from the double-braiding trace. Prove the modular-data relations we can (S_{0λ}=d_λ/D done;
θ conjugation-antisymmetry done). This makes the *target* of BW=Hecke a concrete formalized MTC, so
the identification bwhk becomes "BW output = THIS explicit MTC". Does NOT close bwse (that's bwhk).

## Progress (2026-11-16, PR `litlfred/qou#8150` — `status: in-progress`)
- **Lean 4 formalization (`0` `sorry`, `0` custom axioms):** Added Part III of `folio/quantum-observable-universe/lean/QOU/Brings/BringLiftingObstructionRoutes.lean` (complementing `QOU.BraidKnot.KeystoneHeckeMTC` and `QOU.BraidKnot.KeystoneModularTwist`, verified with Lean v4.24.0 `-DautoImplicit=false`), proving:
  - `hecke_content_sum_transpose_antisymmetry`: explicit signed content-sum evaluation `c(λ) = ∑_{(r,c)∈λ}(c - r)` and transpose antisymmetry `c(λ') = -c(λ)` across `n = 1, 2, 3, 4` partitions (`c([]) = 0`, `c([2]) = 1 = -c([1,1])`, `c([3]) = 3 = -c([1,1,1])`, `c([2,1]) = 0`, `c([4]) = 6 = -c([1,1,1,1])`, `c([3,1]) = 2 = -c([2,1,1])`, `c([2,2]) = 0`).
  - `sl2z_modular_relations` and `ising_su2_level2_S_sq_eq_D_sq_id`: exact `SL₂(ℤ)` relations `S² = -I`, `S⁴ = I`, `(ST)³ = S²` and rank-3 `SU(2)₂` / Ising `(2S)² = 4I = D² C` (`D² = 1² + 1² + (√2)² = 4`).
  - `one_sub_mul_qIntegerPoly`, `qIntegerPoly_at_one`, and `qIntegerPoly_at_two_positive`: proves the telescoping identity `(1 - q)[k]_q = 1 - q^k` separating roots of unity (`q^k = 1`, `[k]_q = 0`, finite-rank `MTC_k` truncation) from `q ≥ 1` (`[k]_1 = k > 0`, `[k]_2 = 2^k - 1 > 0`, infinite-rank non-truncation at generic real `q₀ > 1`).
- **50-dps / Exact Probe + Witness:** `computations/probes/bring_lifting_obstruction_routes_z2_vs_z_probe.py` and `.witness.json` (12/12 assertions passed, including 50-dps verification of `(ST)³ = p₊ S²`, `S² = C`, and `S_{0,a} = d_a / D` for `SU(2)₂` and `SU(2)₃`).

## 2026-11-22 — wave-2 applicability review (thread "Build ribbon categories and QFT math cores")

**Verdict: NEEDS-OWNER.** Critical point: a modular tensor category has finitely many simples; at generic real q₀ > 1 the Hecke category has infinitely many ([k]_q > 0 for all k, the bean's own Part III note), so it is not modular there. Only a root-of-unity semisimplified quotient can be. The bean should be restated as "the semisimplified quotient at q = e^{2πi/ℓ} is modular, with S, T from the Markov trace", or scrapped if the root-of-unity side is off the derivation chain. The Part III module it cites (`Brings/BringLiftingObstructionRoutes.lean`) is not on main.

Not worked.

HeckeRealVsRootOfUnityModularity.lean (08dfe533aaa) + 80-dps witness (ef51559461b) staged.

## 2026-11-27 — S-matrix nondegeneracy at every level (PR #9743)

Working on the restated goal (pending owner card): the semisimplified type-A₁ (Temperley–Lieb) quotient at `q = ζ`, `ζ` a primitive `2(k+2)`-th root of unity, is modular. New `HeckeTemperleyLieb/TLRootOfUnitySMatrixNondegenerate.lean`, sorry-free, over any commutative domain (no Field, no reals): `tildeS_mul_tildeS` (Σ S̃S̃ = −2ℓ·δ), `sMatrix_mul_self` ((ζ−ζ⁻¹)²S² = −2ℓ·1), `globalDimSq_eq`, `sMatrix_det_ne_zero`, `isUnit_det_sMatrix`. The identification of `[(i+1)(j+1)]` with the Jones–Wenzl double-braiding trace is cited (Kauffman–Lins / Kirby–Melvin), not derived; that needs `qou-pbjv` / `qou-ltwg`.

**next**: twist `T` and `(ST)³ = p₊S²` (quadratic Gauss sum); Verlinde fusion `N_{ij}^m` = truncated Clebsch–Gordan; higher rank SU(N)_k.

## 2026-11-27 21:50Z — owner ruling: restated at a root of unity

Owner chose "Root-of-unity quotient" on the card. Goal: the semisimplified Hecke/TL quotient at q a primitive 2l-th root of unity is modular, S and T from the Markov trace. The generic-q HeckeMTC bundle stays as modular data only. Recorded in docs/coordination/owner-rulings.md (PR #9743).

## 2026-11-27 — twist relation (ST)³ = p₊S² at every level (PR #9765)

#9743 merged (fd2009fb86). Same file, new section: `sMatrix_twist` (δ·STS = −G·T⁻¹ST⁻¹, G = Σ_{c<2ℓ} ω^{c²}, ω a primitive 4ℓ-th root, ζ = ω²), `sMatrix_tMatrix_cube` (δ·(ST)³ = −G·S²), `gaussSum_ne_zero`. Sorry-free, axioms [propext, Classical.choice, Quot.sound], generic CommRing domain. With S² = D²·1 these are the projective SL₂(ℤ) relations. T = diag(ω^{(j+1)²}) = ω·θ_j is cited as the ribbon twist (Kirby–Melvin), not derived from the corpus braiding.

**next**: Verlinde fusion N_{ij}^m = truncated Clebsch–Gordan; derive S, T from the corpus braiding (needs qou-pbjv / qou-ltwg); higher rank SU(N)_k. Bean stays open: the corpus-braiding identification is still cited.

## 2026-11-27 — Verlinde fusion (PR #9765, 2nd commit)

`tildeS_one_mul_cgChar` (pointwise sl₂ Clebsch–Gordan, division-free) and `verlinde_fusion`: the Verlinde sum gives −2ℓ·N_{ab}^c with N the truncated Clebsch–Gordan rule (|a−b| < c < a+b, a+b+c < 2ℓ, odd), every level. Sorry-free, standard axioms only. With S² = D², (ST)³ = p₊S², det S ≠ 0, this is the full modular data of the level-k quotient, as cyclotomic algebra.

**still open (why the bean stays open)**: S, T and the fusion are identified with the corpus Hecke braiding / Jones–Wenzl tensor product by citation (Kirby–Melvin, Kauffman–Lins). Deriving that needs qou-pbjv / qou-ltwg.

#9765 merged at its first commit only (twist). Verlinde commit re-landed as PR #9776.

## 2026-11-27 — vacuum row derived from the corpus TL tower (PR #9784)

`HeckeTemperleyLieb/TLVacuumRowFromJonesWenzl.lean`, sorry-free: the corpus Chebyshev `qint` at
`δ = ζ+ζ⁻¹` equals `qInt ζ`, and for any `MarkovTower` with `δε = 1` the unnormalised Jones–Wenzl
trace `δ^{n+1}τ_n(p_n)` equals `S_{0,n+1}` (n+1 ≤ k). Still open (stays cited): existence of a
`MarkovTower` instance at a root of unity; off-vacuum rows (Hopf-link double braiding of JW
projectors); twist eigenvalue on `p_n`. Bean stays open.

## 2026-11-27 — braid part of the twist from the corpus TL tower (PR #9788)

`HeckeTemperleyLieb/TLKauffmanCrossingJonesWenzl.lean`, sorry-free: at δ = −(A²+A⁻²), Kauffman
crossings σᵢ = A + A⁻¹eᵢ are invertible and braid; the JW projector absorbs each as A; full twist
on n+1 strands acts by A^{n(n+1)}. Open: curl factor (−A³)^{strands}; matching θ_j = (−1)^j
A^{j(j+2)} with T = diag(ω^{(j+1)²}) — sign (−1)^j convention; MarkovTower instance at a root of
unity; off-vacuum S rows (Hopf link of two JW projectors). Bean stays open.

## 2026-11-27 — twist sign resolved (https://github.com/litlfred/qou/pull/9798)

`TLPositiveLoopCrossingTwist.lean`, sorry-free: in the positive-loop convention δ = A²+A⁻² (= ζ+ζ⁻¹
at A = ω, matching the S-matrix and vacuum-row files) the crossing A − A⁻¹eᵢ braids, JW absorbs it
as A, the Markov curl on the last strand is +A³, and (A³)^{n+1}A^{n(n+1)} = ω⁻¹·T_{n+1,n+1}. The
(−1)ʲ was the Kauffman loop sign. Still open: ribbon twist on p_n = curl^{strands}·full twist
(interior-strand curls cited); MarkovTower instance at a root of unity; off-vacuum S rows.

## 2026-11-27 — Markov trace built (PR #9817)

`HeckeTemperleyLieb/TLSpinChainMarkovTrace.lean` gives `spinMarkovTower : MarkovTower δ δ⁻¹` at every `δ = q + q⁻¹` with `q ≠ 0` and `δ ≠ 0`, over any field. It is the U_q(sl₂) spin-chain quantum trace with weight ∏ g(τₜ). `vacuum_row_spin` makes the vacuum row of S at a root of unity unconditional. The file is sorry-free and uses only the standard axioms. Still open: the off-vacuum S rows (Hopf link of two JW projectors), which are next, and full modularity of the Hecke category.
