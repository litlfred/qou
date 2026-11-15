import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import QOU.Mass.ColorSpectralCubicGeometry
import QOU.Mass.DilationBranchLocusRigidity

/-!
# QOU.Mass.PalindromicInvolutionLift — the one base symmetry that DOES lift to `Σ`

The colour spectral curve `Σ : P(X,z) = 0`, `P(X,z) = X³ + (z+1)X² + (z²+z+1)X +
(z³+z²+z+1)`, is a 3-sheeted cover of the `z`-line branching over the zeros of the
sextic `D(z) = 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16`
(`ColorSpectralCubicGeometry.color_cubic_discriminant`).

Wall W1 (`qou-d8de`) wants a q-difference prolongation `D_q` built from `Σ`. Four
tranches have narrowed it:

* **#6695** — no rational q-connection on the `z`-line has the sheets as flat sections.
* **#6738** — the same survives passage to the ramified local chart `z = z_c + t²`.
* **#6769** — `DilationBranchLocusRigidity`: no dilation `z ↦ l·z` with `l ≠ 1`
  preserves the branch locus, hence none lifts to `Σ`.
* **#7114** — `FibreMonodromyOrderTwo`: the local fibre monodromy is a transposition, so
  route 2's eigenvalue is `-1`, where the C1 carrier's own hypothesis is false.

#7114 named the gap this file fills, verbatim: *"#6769 closed dilations `z ↦ λz`; the
palindromic symmetry `z ↦ 1/z` is not of that form and is not covered by it."*

## What this file establishes

**(1) The involution lifts — a POSITIVE result** (`colorCubic_inv_lift`). The exact
identity

  `z³ · P(X/z, 1/z) = P(X, z)`   for every `z ≠ 0`

says the map `ι̃ : (X, z) ↦ (X/z, 1/z)` carries `Σ` to itself, covering the base
involution `ι : z ↦ 1/z`. `ι̃ ∘ ι̃ = id` (`invLift_involutive`). So `Σ` carries a
nontrivial automorphism — the first the corpus records. `ι` itself is not new: the
palindromy of `D` is already used at the *coefficient* level, in the `w = z + 1/z`
reduction of `D` to the reciprocal cubic `16w³+24w²−13w+2` that indexes the three Galois
orbits (`docs/audits/2026-05-19-delta-lambda-exploration-findings.md` §H3). What is new
is that it lifts to the curve.

**(2) It is the only inversion that does** (`inversion_rigid`). If `z ↦ l/z` preserves
the branch locus then `l = 1`. Two coefficients do all the work, exactly as in
`DilationBranchLocusRigidity`: the `z⁶` coefficient forces `c = 1`, and the `z⁵`
coefficient then forces `l = 1`.

**(3) So neither survivor can be the q-shift.** Paired with #6769, the monomial maps
`z ↦ l·z` and `z ↦ l/z` preserving the branch locus are exactly `id` and `ι`, both of
order at most `2`. A shift by the substrate modulus has infinite order —
`dilation_gt_one_not_involutive` is the algebraic core: for real `l > 1`, `l·(l·z) = z`
fails at every `z ≠ 0`.

**(4) The fixed-point data** (`fibre_at_neg_one_factors` and friends). `ι̃` fixes all
three points over `z = 1` and exactly the point `X = 0` over `z = -1`; both fibres are
unramified (`branchSextic 1 = 200`, `branchSextic (-1) = 4`), and `ι` swaps the fibres
over `0` and `∞`, so there are exactly **four** fixed points. `Σ` has genus `1` (#7114),
so Riemann–Hurwitz gives `2·1 − 2 = 2(2g' − 2) + 4`, i.e. `g' = 0`: `ι̃` is the
**elliptic involution** and `Σ/ι̃ ≅ P¹`. That step is arithmetic on the counts this file
proves, and is carried in the companion audit rather than here.

## What is NOT formalised, and what is NOT excluded

**Not formalised (prose only, as in #6769 and #7114):** the covering-space step —
an automorphism of `Σ` covering a base automorphism permutes the branch locus, so
"`σ` lifts" implies "`D ∘ σ` is a constant multiple of `D`". Mathlib carries no
branched-cover machinery in usable form. What is formalised is the algebra it rests on.

**Not formalised:** that the *full* Möbius stabiliser of a squarefree sextic's root set
is finite. The elementary reason — a Möbius map is determined by three points, so the
stabiliser of six distinct points embeds in `S₆` — is stated in the audit and measured
exactly in the companion probe, which finds `Stab(B) = {id, ι} ≅ ℤ/2`. This file proves
only the monomial case.

> **Currency note (2026-09-12) — the mathematics of both paragraphs above is now
> formalised; only their packaging is not.** The audit for this file said the Möbius
> half "would need Möbius machinery Mathlib does not carry in usable form". It does
> not: cleared of its denominator the fixed-point condition is the quadratic
> `c·w² + (d−a)·w − b = 0`, so three distinct fixed points force the identity.
> `QOU.Mass.MoebiusThreePointRigidity` proves that (`moebius_id_of_three_fixed`) and
> the sharper determinacy statement that *is* the embedding
> (`moebius_proportional_of_three_agree`: two data agreeing at three distinct points
> are proportional). Independently,
> `QOU.Mass.BranchLocusFiniteOrder.exists_pow_eq_one_of_stabilizes` proves the orbit
> bound for a scaling by pigeonhole, with `not_stabilizes_of_one_lt_complex` ruling
> out every real `l > 1` — which is the substrate case, since `B ⊂ ℂ`.
>
> Still genuinely open: assembling `Stab(B)` as a subgroup of `PGL₂` and the
> injection as a group homomorphism into `S₆` (bookkeeping over Mathlib's
> `Matrix.GeneralLinearGroup`), and the **covering-space step** of the preceding
> paragraph, which is the one irreducibly geometric link and stays prose.

**Not excluded:** a q-difference structure not arising from a base automorphism at all
(route 3, Ramis–Sauloy–Zhang / Sauloy — now supplied with a genus *and* an involution);
anything built from the monodromy representation rather than an automorphism.
`D_q` is **not constructed** here. No fit, nothing wired.

Ground ring: `[Field K]` for the lift (it divides), `[CharZero K]` for the rigidity
(it inverts `16` and `24`). Nothing archimedean appears except in the explicitly
real-valued `dilation_gt_one_not_involutive`, which is about an ordering.

-- Ref: [leitner2026] docs/audits/2026-09-07-w1-route2-fibre-monodromy-is-order-two.md (W1 routes 1-2)
-/

namespace QOU.Mass.PalindromicInvolutionLift

open Polynomial

variable {K : Type*}

/-! ### The colour spectral cubic as a scalar function -/

section CommRing

variable [CommRing K]

/-- The **colour spectral cubic** `P(X, z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`,
whose vanishing locus is `Σ`. Its coefficients are the truncated geometric sums
`a_k = 1 + z + ⋯ + z^(3−k)`, which is exactly why the palindromic involution lifts. -/
def colorCubic (X z : K) : K :=
  X ^ 3 + (z + 1) * X ^ 2 + (z ^ 2 + z + 1) * X + (z ^ 3 + z ^ 2 + z + 1)

/-- The coefficient closed form, made explicit: `a_k = ∑_{i≤3−k} z^i`. -/
theorem colorCubic_coeff_form (X z : K) :
    colorCubic X z
      = (1 : K) * X ^ 3 + (1 + z) * X ^ 2 + (1 + z + z ^ 2) * X + (1 + z + z ^ 2 + z ^ 3) := by
  unfold colorCubic; ring

/-- The fibre over `z = 0`: `P(X, 0) = (X+1)(X²+1)`, three distinct sheets. -/
theorem fibre_at_zero_factors (X : K) : colorCubic X 0 = (X + 1) * (X ^ 2 + 1) := by
  unfold colorCubic; ring

/-- The fibre over `z = -1`: `P(X, -1) = X(X²+1)`. Since `ι̃` acts there by `X ↦ -X`,
its unique fixed point over `z = -1` is `X = 0`. -/
theorem fibre_at_neg_one_factors (X : K) : colorCubic X (-1) = X * (X ^ 2 + 1) := by
  unfold colorCubic; ring

/-- `(0, -1)` really is a point of `Σ`: the fixed point over `z = -1` exists. -/
theorem origin_mem_sigma_at_neg_one : colorCubic (0 : K) (-1) = 0 := by
  unfold colorCubic; ring

/-- The fibre over `z = 1` is `X³ + 2X² + 3X + 4`. `ι̃` acts there by `X ↦ X/1 = X`, so
all three of its points are fixed. -/
theorem fibre_at_one (X : K) : colorCubic X 1 = X ^ 3 + 2 * X ^ 2 + 3 * X + 4 := by
  unfold colorCubic; ring

/-- Both fixed fibres are **unramified**: `D(1) = 200 ≠ 0` in characteristic zero. -/
theorem branchSextic_at_one :
    ColorSpectralCubicGeometry.branchSextic (1 : K) = 200 := by
  unfold ColorSpectralCubicGeometry.branchSextic; ring

/-- `D(-1) = 4 ≠ 0` in characteristic zero: the fibre over `z = -1` is unramified too. -/
theorem branchSextic_at_neg_one :
    ColorSpectralCubicGeometry.branchSextic (-1 : K) = 4 := by
  unfold ColorSpectralCubicGeometry.branchSextic; ring

end CommRing

/-! ### Part 1 — the palindromic involution lifts to `Σ` -/

section Lift

variable [Field K]

/-- **The lift identity.** `z³ · P(X/z, 1/z) = P(X, z)` for every `z ≠ 0`.

This is the palindromy of the *cubic's* coefficient list — `a_k(1/z) = z^{k−3} a_k(z)` —
rather than of the branch sextic, and it is what makes the base involution lift. -/
theorem colorCubic_inv_lift (X z : K) (hz : z ≠ 0) :
    z ^ 3 * colorCubic (X / z) z⁻¹ = colorCubic X z := by
  unfold colorCubic
  field_simp
  ring

/-- **`ι̃` maps `Σ` to `Σ`.** If `(X, z)` is a point of the curve with `z ≠ 0`, so is
`(X/z, 1/z)`. -/
theorem mem_sigma_of_mem_sigma (X z : K) (hz : z ≠ 0) (h : colorCubic X z = 0) :
    colorCubic (X / z) z⁻¹ = 0 := by
  have h3 : (z : K) ^ 3 ≠ 0 := pow_ne_zero 3 hz
  have := colorCubic_inv_lift X z hz
  rw [h] at this
  exact (mul_eq_zero.mp this).resolve_left h3

/-- **`ι̃` is an involution.** Applying `(X, z) ↦ (X/z, 1/z)` twice returns `(X, z)`. -/
theorem invLift_involutive (X z : K) (hz : z ≠ 0) :
    (X / z) / z⁻¹ = X ∧ (z⁻¹)⁻¹ = z := by
  refine ⟨?_, inv_inv z⟩
  field_simp

/-- The base involution is **not** the identity: `ι` genuinely has order `2`.

Characteristic zero is not decoration here — the statement is **false** in characteristic
`2`, where `𝔽₂`'s only unit is `1` and `1⁻¹ = 1`, so `ι` *is* the identity on `𝔽₂ˣ`. The
witness `z = 2` works exactly because `2⁻¹ = 2` would force `1 = 4`. -/
theorem base_involution_ne_id [CharZero K] : ∃ z : K, z ≠ 0 ∧ z⁻¹ ≠ z := by
  have h2 : (2 : K) ≠ 0 := by norm_num
  refine ⟨2, h2, ?_⟩
  intro h
  have hmul : (2 : K) * 2⁻¹ = 2 * 2 := by rw [h]
  rw [mul_inv_cancel₀ h2] at hmul
  norm_num at hmul

end Lift

/-! ### Part 2 — `z ↦ 1/z` is the ONLY inversion preserving the branch locus -/

section Rigidity

open QOU.Mass.DilationBranchLocusRigidity

variable [CommRing K]

/-- The polynomial `z ↦ z⁶ · D(l/z)`, coefficients read off. `D` has degree `6`, so
clearing the denominator gives a polynomial again — with the coefficient list reversed
and `l`-weighted. -/
noncomputable def invSexticPoly (l : K) : K[X] :=
  C (16 * l ^ 6) + C (24 * l ^ 5) * X + C (35 * l ^ 4) * X ^ 2 + C (50 * l ^ 3) * X ^ 3
    + C (35 * l ^ 2) * X ^ 4 + C (24 * l) * X ^ 5 + C 16 * X ^ 6

end Rigidity

section RigidityField

open QOU.Mass.DilationBranchLocusRigidity

variable [Field K]

/-- `invSexticPoly l` really does evaluate to `z⁶ · D(l/z)`, so the hypothesis of
`inversion_rigid` below is the honest "`z ↦ l/z` sends `D` to a multiple of itself". -/
theorem eval_invSexticPoly_eq (l z : K) (hz : z ≠ 0) :
    (invSexticPoly l : K[X]).eval z
      = z ^ 6 * ColorSpectralCubicGeometry.branchSextic (l / z) := by
  unfold invSexticPoly ColorSpectralCubicGeometry.branchSextic
  simp only [eval_add, eval_mul, eval_pow, eval_C, eval_X]
  field_simp

variable [CharZero K]

/-- **Inversion rigidity of the branch locus.** If `z ↦ l/z` sends the branch sextic to a
constant multiple of itself, then `l = 1` and the constant is `1` — i.e. the only
inversion preserving the branch locus is the palindromic `ι : z ↦ 1/z` itself.

The `z⁶` coefficient gives `16 = c·16`, hence `c = 1`; the `z⁵` coefficient then gives
`24·l = 24`, hence `l = 1`. Characteristic zero is used only to invert those two
integers — the same two that carry `DilationBranchLocusRigidity.dilation_scaling_rigid`,
one coefficient-index apart. -/
theorem inversion_rigid (l c : K)
    (h : (invSexticPoly l : K[X]) = C c * branchSexticPoly) :
    l = 1 ∧ c = 1 := by
  rw [C_mul_branchSexticPoly] at h
  have h6 := congrArg (fun p : K[X] => p.coeff 6) h
  have h5 := congrArg (fun p : K[X] => p.coeff 5) h
  unfold invSexticPoly at h6 h5
  simp only [coeff_add, coeff_C_mul_X_pow, coeff_C_mul_X, coeff_C] at h6 h5
  norm_num at h6 h5
  -- `h6` is the `z⁶` coefficient `16 = c·16`; `h5` is the `z⁵` coefficient `24·l = c·24`.
  refine ⟨?_, h6⟩
  linear_combination (1 / 24 : K) * h5 + h6

/-- **No inversion other than `ι` preserves the branch locus.** Contrapositive form. -/
theorem no_inversion_of_ne_one (l c : K) (hl : l ≠ 1) :
    (invSexticPoly l : K[X]) ≠ C c * branchSexticPoly :=
  fun h => hl (inversion_rigid l c h).1

end RigidityField

/-! ### Part 3 — neither survivor can be the substrate q-shift -/

/-- **A dilation by a factor `> 1` is not an involution.** Combined with
`DilationBranchLocusRigidity.dilation_scaling_rigid` and `inversion_rigid` above, the
monomial maps preserving the branch locus are exactly `id` and `ι`, both of order at most
`2`; a substrate shift `z ↦ l·z` with `l = q₀² > 1` squares to `z ↦ l²·z`, which moves
every nonzero point. So no monomial base automorphism supplies the W1 q-shift.

Stated for any real `l > 1` so that no numerical value enters the Lean, exactly as in
`DilationBranchLocusRigidity.no_scaling_of_one_lt`. -/
theorem dilation_gt_one_not_involutive (l z : ℝ) (hl : 1 < l) (hz : z ≠ 0) :
    l * (l * z) ≠ z := by
  intro h
  have hfac : (l * l - 1) * z = 0 := by linear_combination h
  rcases mul_eq_zero.mp hfac with hl1 | hz0
  · nlinarith
  · exact hz hz0

/-- The same statement for the shift the W1 route actually asks for, `l = q²` with
`q > 1`: the substrate shift is not of order `2`, at any nonzero point. -/
theorem qsquare_shift_not_involutive (q z : ℝ) (hq : 1 < q) (hz : z ≠ 0) :
    q ^ 2 * (q ^ 2 * z) ≠ z := by
  refine dilation_gt_one_not_involutive (q ^ 2) z ?_ hz
  nlinarith

end QOU.Mass.PalindromicInvolutionLift
