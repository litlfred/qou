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
updated_at: 2026-11-28T00:00:00Z
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

## 2026-11-27 — off-vacuum row S_{1,j} from braiding (PR #9822)

`HeckeTemperleyLieb/TLHopfLinkRow.lean`, sorry-free: `hopf_trace` evaluates the Hopf link of one strand with `p_n` for any Markov tower, `δ^{n+2}τ_{n+1}((p_n⊗1)·hopfW) = [n+2](A^{2(n+2)}+A^{−2(n+2)}) = [2(n+2)]`, by recursion through the Wenzl identity. `hopf_row_eq_sMatrix` identifies this with `sMatrix ζ k 1 (n+1)` at ζ = ω². With #9817 it is unconditional. Still open: rows S_{b,j} with b ≥ 2 (these need the cabled projector p_{b−1} on the encircling bundle), the ribbon twist on p_n via interior curls, and full modularity. The bean stays open.

## 2026-11-27 — meridian closure (PR #9843), rows S_{b,j} stage 1

`HeckeTemperleyLieb/TLMeridianClosure.lean` (sorry-free): cap sandwich closure without a conditional
expectation; `jw_cap_hopf` (one closed loop around p_n = q^{n+2}+q^{-(n+2)} · p_n);
`trace_loop` (Markov meridian removal for a loop passing c strands). Still open for all rows:
cup slide `e·ι(loop_c)·loop_{c+1} = e`, naturality of the cabled loop with the cable projector,
Chebyshev recursion, root-of-unity identification. Bean stays open.

## 2026-11-28 — every row S_{b,j} from braiding (PR #9863)
`TLCableLoop.lean` (sorry-free): `cable_trace` gives δ^{n+m+2}·τ((p_n ⊗ p_m)·C_{m+1}) = [(n+2)(m+2)] for any Markov trace with δε = 1; `cable_row_eq_sMatrix` identifies it with sMatrix entry S_{n+1,m+1} at a primitive 2(k+2)-th root of unity, for all n+1, m+1 ≤ k. Route: cup slide, cable naturality, Chebyshev recursion rec_H / rec_R, closed form via lam_mul_qint. Still open for modularity in this bean: nondegeneracy of the braided category (S invertible is on main as sMatrix_mul_self), ribbon/twist identification, and the categorical (not trace-level) statement.

## 2026-11-28 — S and T from braiding are modular (PR #9886)
`TLBraidedModular.lean` (sorry-free): `braidS_eq_sMatrix` (whole matrix of Hopf-link traces on the vacuum and p_0..p_{k−1} equals S), `braidS_det_ne_zero`, `braidS_mul_self`, `ribbon_jw` (twist from full twist + framing curls), `braid_modular_relation` ((ST)³ = p₊S²). PR #9863 merged (64ba31d7f4). Still open, so the bean stays open: that the vacuum and p_0..p_{k−1} are exactly the simples of the semisimplified quotient category (categorical, not trace-level, modularity).

## 2026-11-28: semisimplified quotient (PR #9890)
TLSemisimpleQuotient.lean, sorry-free. p_n is a primitive idempotent and is negligible iff τ(p_n)=0. At a primitive 2(k+2)-th root: p_0…p_{k−1} survive, the trace form is nondegenerate below k+1 strands, and p_k ≠ 0 is negligible at every level. The rows of the braid-derived S are pairwise distinct, so the k+1 objects are pairwise non-isomorphic.
STILL OPEN: completeness, i.e. every simple of the quotient is one of these. Needs rectangular TL hom spaces Hom(m,n). Bean stays open.

## 2026-11-28: cup-cap corner and completeness below k+1 strands (PR #9897)
TLCupCapCorner.lean, sorry-free. capEmb : TL_{n+1} ≅ E·TL_{n+3}·E (onto via Jones' lemma, injective on nondegenerate levels). Objects are idempotents and isomorphism is Murray–von Neumann equivalence. simple_mvn_std: every simple idempotent of TL_{N+1} is equivalent to p_N, the vacuum, or a cup of a standard object, whenever p_m exists and the form is nondegenerate for m ≤ N. At a root of unity this covers N+1 ≤ k.
STILL OPEN: (1) k+1 or more strands, i.e. completeness in the quotient by negligibles; (2) rectangular Hom(m,n) as a category. Bean stays open.

## 2026-11-28 — completeness on every number of strands (PR #9902)

`TLNegligibleQuotient.lean`: in the quotient by negligibles, every simple idempotent on any number of strands is equivalent to the vacuum or some p_m (m < k) with cups, and none of these vanishes (`simple_mvn_stdLt_root`). Sorry-free. Still open: rectangular Hom(m,n) as a category; braiding/modular data on the quotient category itself (not just its objects).

## 2026-11-28 — rectangular Hom and quotient modular data (PRs #9903 merged, #9907)

- `TLRectangularHom.lean` (#9903, merged 1c32f0025e): Hom(a,b) = [b]·Q_N·[a] with [a] = nested cup-cap idempotent; a CategoryTheory.Category on labels a ≤ N; adding two strands is a full and faithful functor, so Hom(a,b) does not depend on N.
- `TLQuotientModularData.lean` (#9907): trace on the quotient is nondegenerate; crossings descend (invertible, braid relations); twist on p_n; `modular_data_quotient` = complete simples list + S = [(i+1)(j+1)] + det S ≠ 0.
- Still open: monoidal structure on the quotient category (tensor across strand counts) and a Mathlib BraidedCategory / ribbon instance; the N → ∞ colimit as one category.

## 2026-11-28 01:20Z — tensor product on the quotient (PR #9914)
TLQuotientTensor.lean, sorry-free. Proved: the Markov trace is mirror invariant (left Markov property derived from the right one); negligible morphisms form a tensor ideal; tensQ : Q n × Q m → Q (n+m+1), which is bilinear, multiplicative and unital, satisfies τ(x⊗y)=τxτy, and is associative up to strand reindexing. Still open: a Mathlib MonoidalCategory on the glued category (sibling thread "Glue all strand levels into one category"), and the braided/ribbon instance (sibling thread "Build the Mathlib braided ribbon instance"). The bean stays open.

## 2026-11-28 — tensor of corners (PR #9931)

`TLTensorCorner.lean`: `mvn_tens_P`, `P_a^{a+2i} ⊗ P_c^{c+2j}` ≅ (MvN) `P_{a+c+1}^{a+c+1+2(i+j)}` up to
recast. Sorry-free. Next: MonoidalCategory on the glued category `GObj` (#9929), formal unit.
Still open: monoidal structure, coherence (pentagon with the chosen movers), braided/ribbon (sibling
thread, #9923), modularity.

## 2026-11-28 — slide words done (PR #9941)
`TLSlideIso.lean`: slide words U, V with U·V = tensor corner, V·U = standard corner; compatible with two more strands on either factor (second factor exactly, first factor by slide_conj_succ). Sorry-free. Next: glued tensor of morphisms, unit object (needs zero-through-strand objects), MonoidalCategory.
