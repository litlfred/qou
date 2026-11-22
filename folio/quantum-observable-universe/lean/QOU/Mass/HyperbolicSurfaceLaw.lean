import QOU.Mass.CoordinationBulkCriterion
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.Tactic

/-!
# QOU.Mass.HyperbolicSurfaceLaw — in `H³` the surface fraction tends to a CONSTANT, so the framework's own geometry predicts no `A^(−1/3)` term at all

Every surface-term tranche on this arc so far (#6761, #6780, #6801, #6886) imported the compact
**Euclidean** surface law `A_surf ∝ A^(2/3)`, and the corpus objected each time: the ambient
geometry of this framework is hyperbolic. `docs/coordination/sm-26-parameter-chip-away.md`
already measured that using `H³` consistently — `R ∼ ½ ln V`, so `ln A` where the Euclidean import
has `A^(1/3)` — *costs* accuracy on a neighbouring quantity, and `qou-rav3` asked for "a packing
argument inside the framework" rather than a citation. This file is that argument, for the
surface fraction, and it is exact.

## The fact

A ball of radius `R` in `H³` (curvature `−1`) has

    V(R) = π (sinh 2R − 2R)          S(R) = 4π sinh² R = 2π (cosh 2R − 1).

The volume is **Bolyai's formula and it is held**: `library/arxiv-1010.5321v3/` (Horváth, *Formulas
on hyperbolic volume*, §3.1 "Formulas of J. Bolyai", key `horvath2010`) gives
`πk³ sinh(2x/k) − 2πk²x`, which at curvature `k = 1` is `hypVol`. The area is not stated there; it
is the derivative of the volume, and `hasDerivAt_hypVol` proves `V' = S`, so the area rests on the
held source too. Nothing had to be ingested for this.

In Euclidean space `S/V = 3/R → 0`: the boundary is a vanishing fraction of a large ball, and that
vanishing is the whole origin of the `A^(−1/3)` surface term. **In hyperbolic space it does not
vanish.** Exactly,

    S − 2V = 2π (e^(−2R) + 2R − 1)  ≥  0            since  e^(−x) ≥ 1 − x,

so **`S/V ≥ 2` for every `R > 0`** (`surfaceFraction_ge_two`), with equality only in the limit —
the boundary of a large hyperbolic ball is a *fixed* fraction of its volume, not a vanishing one.

## What that does to the binding law

`CoordinationSurfaceDeficit` puts the whole `A`-dependence of the correction in `A_surf/A`, and
`CoordinationBulkCriterion` needs that fraction to **vanish** for a surface term to exist:
`HasBulk := A_surf → ∞ ∧ A_surf/A → 0`. A hyperbolic-ball cluster — nucleon count extensive in
volume, surface count extensive in area, under **any** radius assignment `R(A) > 0` whatever —
has `A_surf/A ≥ 2` at every `A`, so it **fails `HasBulk`** (`hyperbolic_not_hasBulk`). Its
"surface term" is a **constant shift of the volume coefficient**,

    B/A ≤ εk/2 − ε(k − k')                                    (`hyperbolic_perNucleon_le`)

and the residual `A`-dependence is `f(R) − 2 ≤ 4R/(sinh 2R − 2R)` (`surfaceFraction_sub_two_le`),
which with `V ∼ (π/2) e^(2R)`, i.e. `R ∼ ½ ln A`, is of order **`(ln A)/A`** — a *different
functional form* from `A^(−1/3)`, and one the residual had never been tested against. The
companion probe tests it. The expectation on the record before it ran was that it fits **worse**
than the Euclidean import, because the corpus had measured that consistency costs accuracy.

**That expectation failed.** Against the 2548 measured AME nuclides, with Coulomb, asymmetry and
pairing carried separately, the hyperbolic `(ln A)/A` fits **better**: RSS **31.44** against the
Euclidean `A^(−1/3)`'s 38.53 (ratio 0.816), and better than the best pure power `A^(−p)` at any
`p` (38.19, #6780). The exact ball `S/V` at `V = v₀A`, profiled over `v₀`, also beats the import
(35.18). The win is **not generic** by the `qou-rav3` discipline: none of nine "reasonable"
alternative shapes beats the Euclidean import, the hyperbolic one beats all nine, and within its
own family `(ln A)^m/A^p` at `m = 1` the optimum is `p* = 0.912`, within 0.09 of the hyperbolic
`p = 1`. Two cautions the probe records: the exact ball's best `v₀` puts every nucleus at
`R < 2`, the near-Euclidean regime, so the data prefer the asymptotic *shape* rather than a literal
extensive-volume ball; and a two-parameter `(m, p)` search keeps improving with `m`, so the
hyperbolic point is the best **predicted** shape, not a global optimum — the latter would be a
fit, and is not claimed.

## The non-abelian Stokes connection, and what "the surface of kites" is

Yekutieli's estimate (held, `library/arxiv-1007.1250v4/`, Def 4.4.12 / Lemma 4.4.13) bounds the
error of the multiplicative integral by a **good** term counted by the `4^k` square **kites** of the
`k`-th binary tessellation of `I²` — an *area* count — plus a **bad** term bounded by
`a₀ + a₁·2^k`, one dimension down. **Corrected in `StokesSingularCountAffine` (this header first
said the bad term is "counted by the singular points of the surface map"; that is the
1-dimensional string case, `:2280`):** in the 2-dimensional case the kite map is linear by
definition and the bad set is where the connection **forms** `(α, β)` fail to be smooth
(Def 4.4.12), with `a₀ = 2m` for `m` segments covering their singular locus and `a₁` a *length*
(Lemma 4.4.13). Smooth forms give no bad set at all. So, precisely:

* **the surface of kites is the BULK** of the Stokes estimate, not its surface term;
* **the surface term is the singular locus**, and `2026-08-30-nonabelian-stokes-and-the-surface-term.md`
  reads `a_S` as proportional to that count for the spanning surface of the nuclear braid closure.

That is exactly a bulk/boundary split, so `HasBulk`'s question applies to it verbatim
(`StokesSurfaceTerm`): the singular count is a genuine surface term iff it grows without bound and
vanishes as a fraction of the kite count. **Nobody has computed how the singular count scales with
`A`** — the audit never states it and no probe evaluates it for any nucleus. What the corpus *does*
know is that every Seifert invariant of the canonical closure measured so far is **affine** in `A`
(`every_seifert_invariant_is_affine_probe`: `χ = −9A + 1`, `2g = 8A`, …, six nuclei), so any
fixed-mesh 2-cell count of the spanning surface is affine too; and `affine_over_affine_not_surfaceTerm`
below shows an affine singular count over an affine cell count tends to a **nonzero constant**
ratio — the same "constant shift of the volume coefficient" the hyperbolic ball gives, and not a
surface term. So the Stokes route joins the hyperbolic one: **if its singular count is affine, it
renormalises the volume term and supplies no `A^(−1/3)`.** Whether it *is* affine is the open
computation, and it is beaned rather than guessed.

(Two homonyms to keep apart, both already in the corpus: the "kite-tail" `(1 + r²)^(3A−1)` is a
Hecke cyclotomic factor of `tr_M`, not a 2-cell — and its exponent `3A − 1` is affine, so #6801
already excludes it as a surface term; and bean `qou-20bk` with
`QOU/LiftingDescent/CrossedModuleSurfaceHolonomy.lean` (sorry-free) has settled that no 2-dim
Yekutieli object carries a non-abelian 3-body term — kites are not where any many-body term lives.)

## Why this was the right test regardless of outcome

A form that comes from the framework's own geometry can be iterated whichever way the fit goes:
it says what the geometry predicts, and any discrepancy is information. An imported Euclidean
packing cannot — it has already absorbed the discrepancy. The four tranches before this one all
ended on the imported side of that line; this is the first on the other side, and it happens to
fit better. That is to be read as **the shape the framework's geometry predicts is a better
description of the residual than the shape the SEMF imports** — not as a derivation of the
surface coefficient, which stays free.

## Scope

* **Proved:** `S = 2π(cosh 2R − 1)`; `V > 0` for `R > 0`; `2V ≤ S` for all `R`; `S/V ≥ 2`; the
  Euclidean contrast `S/V = 3/R → 0`; a generic lemma that a surface fraction bounded below by a
  positive constant refutes `HasBulk`; `¬HasBulk` for the hyperbolic cluster under any positive
  radius assignment; the per-nucleon bound; and the decay bound on `f − 2`. All exact, no fit.
* **NOT proved here:** the limit `S/V → 2` itself (the bound `f − 2 ≤ 4R/(sinh 2R − 2R)` is
  stated; that its right side tends to `0` is elementary and is checked numerically in the probe,
  not formalised); and the `(ln A)/A` asymptotic form of the correction, which needs the inverse
  `R(A)` and is left to the probe as a measured statement.
* **Assumed:** that the cluster is a metric ball in `H³` of curvature `−1`, with nucleon count
  extensive in volume and surface count extensive in area. This is the hyperbolic analogue of the
  compact-packing hypothesis the Euclidean tranches made — but it is the framework's *own*
  geometry rather than an import, which is the point.
* **NOT derived:** that the substrate emits such a cluster (`qou-brng`'s open input, unchanged),
  nor the radius assignment `R(A)`; every theorem here holds for **all** `R(A) > 0`, so nothing
  about the assignment is used.
* **Not a fit.** No coefficient is chosen against data.

Ground ring `ℝ` (§7c: archimedean — `sinh`, `cosh`, `exp`, limits).

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/CoordinationBulkCriterion.lean
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/CoordinationSurfaceDeficit.lean
-- Ref: [leitner2026] docs/coordination/sm-26-parameter-chip-away.md (the hyperbolic-vs-Euclidean import objection)
-/

namespace QOU.Mass.HyperbolicSurfaceLaw

open Real Filter QOU.Mass.CoordinationBulkCriterion

/-! ## The hyperbolic ball -/

/-- Volume of a ball of radius `R` in `H³` (curvature `−1`): `π (sinh 2R − 2R)`. -/
noncomputable def hypVol (R : ℝ) : ℝ := π * (sinh (2 * R) - 2 * R)

/-- Area of the boundary sphere of that ball: `4π sinh² R`. -/
noncomputable def hypArea (R : ℝ) : ℝ := 4 * π * sinh R ^ 2

theorem hypArea_eq (R : ℝ) : hypArea R = 2 * π * (cosh (2 * R) - 1) := by
  unfold hypArea
  rw [cosh_two_mul, cosh_sq]
  ring

theorem hypVol_pos {R : ℝ} (hR : 0 < R) : 0 < hypVol R := by
  unfold hypVol
  have h : 2 * R < sinh (2 * R) := self_lt_sinh_iff.mpr (by linarith)
  have hπ := Real.pi_pos
  have : 0 < sinh (2 * R) - 2 * R := by linarith
  positivity

/-- **`S − 2V = 2π (e^(−2R) + 2R − 1)`**, exactly. -/
theorem hypArea_sub_two_mul_hypVol (R : ℝ) :
    hypArea R - 2 * hypVol R = 2 * π * (exp (-(2 * R)) + 2 * R - 1) := by
  rw [hypArea_eq]
  unfold hypVol
  have hcs : cosh (2 * R) - sinh (2 * R) = exp (-(2 * R)) := by
    rw [cosh_eq, sinh_eq]; ring
  rw [← hcs]
  ring

/-- **`2V ≤ S` for every `R`** — the whole content is `e^(−x) ≥ 1 − x`. -/
theorem two_mul_hypVol_le_hypArea (R : ℝ) : 2 * hypVol R ≤ hypArea R := by
  have h := add_one_le_exp (-(2 * R))
  have hnn : 0 ≤ exp (-(2 * R)) + 2 * R - 1 := by linarith
  have := mul_nonneg (by positivity : (0 : ℝ) ≤ 2 * π) hnn
  have key := hypArea_sub_two_mul_hypVol R
  linarith

/-- **The hyperbolic surface fraction is at least 2, for every radius.** In Euclidean space it is
`3/R → 0`; here it never drops below a constant. -/
theorem surfaceFraction_ge_two {R : ℝ} (hR : 0 < R) : 2 ≤ hypArea R / hypVol R := by
  rw [le_div_iff₀ (hypVol_pos hR)]
  exact two_mul_hypVol_le_hypArea R

/-- The residual `A`-dependence: `S/V − 2 ≤ 4R/(sinh 2R − 2R)`, which decays like `R e^(−2R)`. -/
theorem surfaceFraction_sub_two_le {R : ℝ} (hR : 0 < R) :
    hypArea R / hypVol R - 2 ≤ 4 * R / (sinh (2 * R) - 2 * R) := by
  have hV := hypVol_pos hR
  have hs : 0 < sinh (2 * R) - 2 * R := by
    have := self_lt_sinh_iff.mpr (by linarith : 0 < 2 * R); linarith
  have hπ := Real.pi_pos
  have hexp : exp (-(2 * R)) ≤ 1 := exp_le_one_iff.mpr (by linarith)
  have hnum : hypArea R - 2 * hypVol R ≤ 4 * π * R := by
    rw [hypArea_sub_two_mul_hypVol]; nlinarith
  have h1 : hypArea R / hypVol R - 2 = (hypArea R - 2 * hypVol R) / hypVol R := by
    field_simp
  rw [h1]
  have h2 : (hypArea R - 2 * hypVol R) / hypVol R ≤ 4 * π * R / hypVol R :=
    div_le_div_of_nonneg_right hnum hV.le
  have h3 : 4 * π * R / hypVol R = 4 * R / (sinh (2 * R) - 2 * R) := by
    unfold hypVol; field_simp
  linarith

/-! ## The Euclidean contrast -/

noncomputable def eucVol (R : ℝ) : ℝ := 4 / 3 * π * R ^ 3
noncomputable def eucArea (R : ℝ) : ℝ := 4 * π * R ^ 2

/-- Euclidean: `S/V = 3/R`. -/
theorem eucFraction_eq {R : ℝ} (hR : 0 < R) : eucArea R / eucVol R = 3 / R := by
  unfold eucArea eucVol
  have hπ := Real.pi_pos
  field_simp

/-- Euclidean: the surface fraction **vanishes** — the origin of every `A^(−1/3)` surface term. -/
theorem eucFraction_tendsto_zero : Tendsto (fun R : ℝ => 3 / R) atTop (nhds 0) := by
  have := tendsto_inv_atTop_zero.const_mul (3 : ℝ)
  simpa [div_eq_mul_inv] using this

/-! ## No bulk -/

/-- **A surface fraction bounded below by a positive constant refutes `HasBulk`.** Generic. -/
theorem not_hasBulk_of_fraction_ge (Asurf : ℝ → ℝ) (c : ℝ) (hc : 0 < c)
    (h : ∀ᶠ A in atTop, c ≤ Asurf A / A) : ¬ HasBulk Asurf := by
  rintro ⟨-, h0⟩
  have h1 : ∀ᶠ A in atTop, Asurf A / A < c := Filter.Tendsto.eventually_lt_const hc h0
  obtain ⟨A, hA1, hA2⟩ := (h.and h1).exists
  linarith

/-- The surface count of a hyperbolic-ball cluster under a radius assignment `Rof`: nucleon count
`A` extensive in volume, surface count extensive in area, so `A_surf = (S/V)(R(A)) · A`. -/
noncomputable def hypSurfaceCount (Rof : ℝ → ℝ) (A : ℝ) : ℝ :=
  hypArea (Rof A) / hypVol (Rof A) * A

theorem hypSurfaceCount_div (Rof : ℝ → ℝ) (A : ℝ) (hA : A ≠ 0) :
    hypSurfaceCount Rof A / A = hypArea (Rof A) / hypVol (Rof A) := by
  unfold hypSurfaceCount
  field_simp

/-- **A hyperbolic-ball cluster has no bulk, under ANY positive radius assignment.** Its surface
fraction is `≥ 2` at every `A`, so it never vanishes. -/
theorem hyperbolic_not_hasBulk (Rof : ℝ → ℝ) (hR : ∀ A, 0 < Rof A) :
    ¬ HasBulk (hypSurfaceCount Rof) := by
  apply not_hasBulk_of_fraction_ge _ 2 (by norm_num)
  filter_upwards [eventually_ne_atTop (0 : ℝ)] with A hA
  rw [hypSurfaceCount_div Rof A hA]
  exact surfaceFraction_ge_two (hR A)

/-- **The hyperbolic "surface term" is a constant shift of the volume coefficient, not a decaying
correction.** With `k' < k` the per-nucleon binding sits at least `ε(k − k')` below the
uniform-degree plateau at every `A`. -/
theorem hyperbolic_perNucleon_le (ε k k' : ℝ) (hε : 0 < ε) (hkk : k' < k)
    (Rof : ℝ → ℝ) (hR : ∀ A, 0 < Rof A) (A : ℝ) (hA : 0 < A) :
    ε * k / 2 - (ε * (k - k') / 2) * (hypSurfaceCount Rof A / A) ≤ ε * k / 2 - ε * (k - k') := by
  rw [hypSurfaceCount_div Rof A (ne_of_gt hA)]
  have hf := surfaceFraction_ge_two (hR A)
  have hc : 0 < ε * (k - k') / 2 := by
    have := sub_pos.mpr hkk
    positivity
  nlinarith

/-! ## The area is the derivative of the held volume formula -/

/-- **`V'(R) = S(R)`**: the area follows from Bolyai's volume (held, `horvath2010` §3.1) by
differentiation, so it rests on the held source too. -/
theorem hasDerivAt_hypVol (R : ℝ) : HasDerivAt hypVol (hypArea R) R := by
  unfold hypVol
  have h2 : HasDerivAt (fun R : ℝ => 2 * R) 2 R := by
    simpa using (hasDerivAt_id R).const_mul (2 : ℝ)
  have h1 : HasDerivAt (fun R : ℝ => sinh (2 * R)) (cosh (2 * R) * 2) R := h2.sinh
  have h := (h1.sub h2).const_mul π
  rw [hypArea_eq]
  convert h using 1
  ring

/-! ## The non-abelian Stokes split, as a `HasBulk` question -/

/-- Yekutieli's estimate splits into a bulk term counted by the `4^k` kites (an area count) and
a boundary term counted by the singular locus (one dimension down). Read as functions of the mass
number, the singular count is a **genuine surface term** iff it grows without bound while vanishing
as a fraction of the kite count — the same conjunction as `HasBulk`. -/
def StokesSurfaceTerm (cells sing : ℝ → ℝ) : Prop :=
  Tendsto sing atTop atTop ∧ Tendsto (fun A => sing A / cells A) atTop (nhds 0)

/-- **An affine singular count over an affine cell count is not a surface term.** Their ratio tends
to the nonzero constant `α_s/α_c` — a constant renormalisation of the bulk, exactly as the
hyperbolic ball gives. Every Seifert invariant of the canonical closure measured so far is affine
in `A`; whether the singular count is too is the open computation. -/
theorem affine_over_affine_not_surfaceTerm (αc βc αs βs : ℝ) (hαc : 0 < αc) (hαs : αs ≠ 0) :
    ¬ StokesSurfaceTerm (fun A => αc * A + βc) (fun A => αs * A + βs) := by
  rintro ⟨-, h⟩
  have heq : (fun A : ℝ => (αs * A + βs) / (αc * A + βc)) =ᶠ[atTop]
      (fun A => (αs + βs / A) / (αc + βc / A)) := by
    filter_upwards [eventually_gt_atTop (0 : ℝ)] with A hA
    field_simp
  have hnum : Tendsto (fun A : ℝ => αs + βs / A) atTop (nhds (αs + 0)) :=
    tendsto_const_nhds.add (by simpa [div_eq_mul_inv] using tendsto_inv_atTop_zero.const_mul βs)
  have hden : Tendsto (fun A : ℝ => αc + βc / A) atTop (nhds (αc + 0)) :=
    tendsto_const_nhds.add (by simpa [div_eq_mul_inv] using tendsto_inv_atTop_zero.const_mul βc)
  have hlim : Tendsto (fun A : ℝ => (αs + βs / A) / (αc + βc / A)) atTop (nhds ((αs + 0) / (αc + 0))) :=
    hnum.div hden (by simpa using hαc.ne')
  have h' := Filter.Tendsto.congr' heq h
  have := tendsto_nhds_unique h' hlim
  simp at this
  exact hαs (div_eq_zero_iff.mp this.symm |>.resolve_right hαc.ne')

end QOU.Mass.HyperbolicSurfaceLaw
