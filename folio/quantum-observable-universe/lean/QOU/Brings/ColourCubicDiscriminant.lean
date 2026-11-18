/-
# The colour-tube cubic's discriminant locus: exact reduction to a trinomial

The colour-tube cubic on Bring's surface (`docs/picard-lefschetz-plan.md`) has
discriminant proportional to the sextic

    Δ(z) ∝ 16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16 .

Its roots are the **Bring-side "divergent points"** — the saddles whose
Picard–Lefschetz thimbles the resurgence arc integrates over.

🛑 **PARTIAL DUPLICATE — read this before using anything below.**
`QOU.Brings.ColourCubicBranchLocus` (sorry-free, 2026-09-03, bean `qou-qx7j`)
**already proves** the self-reciprocality (`disc_inv_mul`,
`branchLocus_inv_mem`), the reduction to `16w³+24w²−13w+2`
(`w_cubic_of_palindromic`), the IVT bracket for the real root
(`w_real_root_mem_Ioo`), and the unit-circle fact (`normSq_root_eq_one`).
I did not find it: my corpus-grep filtered audit *filenames* on
`alien|resurg|borel|stokes|gevrey|divergen`, and that audit is called
`enclosed-pole-set-E-is-not-identifiable`. Recorded rather than quietly
deleted, because the miss is the reusable part.

**What is genuinely new here is the last three theorems only** — the depression
`w = t − 1/2`, the scaling `t = (5/4)u` to the trinomial normal form
`u³ − u + 2/5`, and the composite chain constant. `palindromic_reduction`,
`colourSextic_eq_cube_mul_reduced` and `normSq_eq_one_of_abs_le_two` below are
restatements of the existing results over a generic `[Field R] [CharZero R]`
rather than `ℂ`; they are kept only because the new theorems are stated in that
generality and would otherwise not compose.

Nothing here is numerical: every statement is an identity over a
characteristic-zero field, or an exact consequence of `|w| ≤ 2` over `ℝ`/`ℂ`.

The chain, each step an identity proved below:

    sextic  --(w = z + 1/z)-->  16w³ + 24w² − 13w + 2
            --(w = t − 1/2)-->  32t³ − 50t + 25
            --(t = (5/4)u)-->   u³ − u + 2/5

so the saddle points are the roots of a **trinomial in Bring–Jerrard normal
form**, `u³ − u + 2/5`, whose discriminant is `−8/25 = −2³/5²`. The value
`−80000 = −2⁷·5⁴` is the discriminant of the reduced cubic `16w³ + 24w² − 13w + 2`
(as `ColourCubicBranchLocus` states), not of the sextic (bean `qou-ozyt`).
The sextic's own discriminant is `−5120000000000 = −2¹⁹·5¹⁰`, proved as
`QOU.Brings.colourSextic_discr` in `QOU.Brings.ColourCubicDiscriminantValues`
(Sylvester-formula discriminant on leading-first coefficient vectors; that file
also proves `reducedCubic_discr = −80000` and `saddleTrinomial_discr = −8/25`).

The last theorem explains, as algebra rather than observation, *why* one
conjugate pair of roots lies exactly on the unit circle: the trinomial's real
root gives `|w| < 2`, and for **any** real `w` with `|w| ≤ 2` the two `z` with
`z + 1/z = w` have `|z| = 1` exactly.
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

namespace QOU.Brings

/-- The palindromic sextic carrying the colour-tube cubic's discriminant locus. -/
noncomputable def colourSextic {R : Type*} [CommRing R] (z : R) : R :=
  16 * z ^ 6 + 24 * z ^ 5 + 35 * z ^ 4 + 50 * z ^ 3 + 35 * z ^ 2 + 24 * z + 16

/-- The cubic obtained from the palindromic reduction `w = z + 1/z`. -/
noncomputable def reducedCubic {R : Type*} [CommRing R] (w : R) : R :=
  16 * w ^ 3 + 24 * w ^ 2 - 13 * w + 2

/-- The trinomial normal form of the reduction. -/
noncomputable def saddleTrinomial {R : Type*} [Field R] [CharZero R] (u : R) : R :=
  u ^ 3 - u + 2 / 5

/-- **Step 1 — the palindromic reduction.** Writing the sextic in terms of the
symmetric combinations of `z` and `1/z` collapses it to `reducedCubic`. This is
the identity that makes the reduction legitimate. -/
theorem palindromic_reduction {R : Type*} [CommRing R] (w : R) :
    16 * (w ^ 3 - 3 * w) + 24 * (w ^ 2 - 2) + 35 * w + 50 = reducedCubic w := by
  unfold reducedCubic; ring

/-- **The reduction is exact on the sextic itself.** For `z ≠ 0`, the sextic
equals `z³` times the reduced cubic evaluated at `w = z + z⁻¹`. This is the
statement that the roots of the sextic are exactly the `z` whose `z + 1/z`
solves the cubic — the content of the palindromic reduction, not merely a
formal rearrangement. -/
theorem colourSextic_eq_cube_mul_reduced {R : Type*} [Field R] [CharZero R]
    (z : R) (hz : z ≠ 0) :
    colourSextic z = z ^ 3 * reducedCubic (z + z⁻¹) := by
  unfold colourSextic reducedCubic
  field_simp
  ring

/-- **Step 2 — depressing the cubic** by `w = t − 1/2` clears the quadratic term
and, after scaling by 2, gives integer coefficients `32t³ − 50t + 25`. -/
theorem depressed_cubic {R : Type*} [Field R] [CharZero R] (t : R) :
    2 * reducedCubic (t - 1 / 2) = 32 * t ^ 3 - 50 * t + 25 := by
  unfold reducedCubic
  have h2 : (2 : R) ≠ 0 := two_ne_zero
  field_simp
  ring

/-- **Step 3 — the trinomial normal form.** Scaling `t = (5/4)u` sends the
depressed cubic to `u³ − u + 2/5`: a trinomial whose linear coefficient is
exactly `−1`, with `2/5` the only remaining datum. -/
theorem trinomial_normal_form {R : Type*} [Field R] [CharZero R] (u : R) :
    (2 / 125) * (32 * ((5 / 4) * u) ^ 3 - 50 * ((5 / 4) * u) + 25) = saddleTrinomial u := by
  unfold saddleTrinomial
  have h125 : (125 : R) ≠ 0 := by norm_num
  have h4 : (4 : R) ≠ 0 := by norm_num
  have h5 : (5 : R) ≠ 0 := by norm_num
  field_simp
  ring

/-- **The full chain in one statement.** For `z ≠ 0`, the sextic vanishes iff the
trinomial vanishes at the corresponding `u`. Stated as the identity that carries
it, so the composite is checked rather than asserted. -/
theorem colourSextic_eq_trinomial_chain {R : Type*} [Field R] [CharZero R] (z u : R)
    (hz : z ≠ 0) (hu : z + z⁻¹ = (5 / 4) * u - 1 / 2) :
    colourSextic z = z ^ 3 * ((125 / 4) * saddleTrinomial u) := by
  rw [colourSextic_eq_cube_mul_reduced z hz, hu]
  unfold reducedCubic saddleTrinomial
  have h125 : (125 : R) ≠ 0 := by norm_num
  have h4 : (4 : R) ≠ 0 := by norm_num
  field_simp
  ring

/-- **Why a conjugate pair sits exactly on the unit circle.**

For a real `w` with `|w| ≤ 2`, the two solutions of `z + 1/z = w` are
`(w ± i√(4−w²))/2`, and each has modulus exactly `1`. The unit-circle pair of
the colour sextic is therefore *forced* — it is not a numerical coincidence —
because the trinomial's real root gives `w = (5/4)u − 1/2` with `|w| < 2`.

Proved via `Complex.normSq`, so the conclusion is an exact equality of reals. -/
theorem normSq_eq_one_of_abs_le_two (w : ℝ) (hw : |w| ≤ 2) :
    Complex.normSq (⟨w / 2, Real.sqrt (4 - w ^ 2) / 2⟩ : ℂ) = 1 := by
  have h4 : (0 : ℝ) ≤ 4 - w ^ 2 := by
    nlinarith [abs_le.mp hw |>.1, abs_le.mp hw |>.2]
  have hsq : Real.sqrt (4 - w ^ 2) ^ 2 = 4 - w ^ 2 := Real.sq_sqrt h4
  simp only [Complex.normSq_mk]
  nlinarith [hsq]

/-- The same fact as a norm: the root lies on the unit circle. -/
theorem norm_eq_one_of_abs_le_two (w : ℝ) (hw : |w| ≤ 2) :
    ‖(⟨w / 2, Real.sqrt (4 - w ^ 2) / 2⟩ : ℂ)‖ = 1 := by
  have h := normSq_eq_one_of_abs_le_two w hw
  have : ‖(⟨w / 2, Real.sqrt (4 - w ^ 2) / 2⟩ : ℂ)‖ ^ 2 = 1 := by
    rw [← Complex.normSq_eq_norm_sq] at *; exact h
  nlinarith [norm_nonneg (⟨w / 2, Real.sqrt (4 - w ^ 2) / 2⟩ : ℂ), this]

/-- **Palindromic self-reciprocality of the colour sextic** over an arbitrary field:
    for `z ≠ 0`, `colourSextic z = z^6 · colourSextic z⁻¹` (`bean qou-ok7t`). -/
theorem colourSextic_recip_identity {R : Type*} [Field R] (z : R) (hz : z ≠ 0) :
    colourSextic z = z ^ 6 * colourSextic z⁻¹ := by
  unfold colourSextic
  field_simp
  ring

/-- **The conjugate solution `(w − i√(4−w²))/2` also has unit norm-squared** for
    every real `w` with `|w| ≤ 2` (`bean qou-ok7t`). -/
theorem normSq_conj_eq_one_of_abs_le_two (w : ℝ) (hw : |w| ≤ 2) :
    Complex.normSq (⟨w / 2, -(Real.sqrt (4 - w ^ 2) / 2)⟩ : ℂ) = 1 := by
  have h4 : (0 : ℝ) ≤ 4 - w ^ 2 := by
    nlinarith [abs_le.mp hw |>.1, abs_le.mp hw |>.2]
  have hsq : Real.sqrt (4 - w ^ 2) ^ 2 = 4 - w ^ 2 := Real.sq_sqrt h4
  simp only [Complex.normSq_mk]
  nlinarith [hsq]

end QOU.Brings
