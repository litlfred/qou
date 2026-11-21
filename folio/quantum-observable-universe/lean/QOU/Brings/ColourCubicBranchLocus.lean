import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic
import QOU.Brings.RamificationParityMonodromy

/-!
# QOU.Brings.ColourCubicBranchLocus — the branch locus is bar-symmetric, and no residue survives

Two exact facts about the colour cubic

  `f(X, z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`

whose branch locus is the zero set of

  `Δ(z) = −(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16)`

(`bring_cubic_monodromy_probe.py` A1: degree 6, `gcd(Δ, Δ′) = 1`, so six
distinct simple branch points). Both facts bear on the **enclosed pole set `E`**
that `prop:sw-period-residue-sum` leaves open — see bean `qou-qx7j`.

## 1. The locus is invariant under the bar involution `z ↦ 1/z`

`Δ`'s coefficient list `[16, 24, 35, 50, 35, 24, 16]` is **palindromic**. Hence
`z⁶ Δ(1/z) = Δ(z)`, so the branch locus is closed under `z ↦ 1/z`
(`branchLocus_inv_mem`). That is the Hecke bar-involution acting on the pole
locus — the corpus had the polynomial written out exactly and had not noticed
that it is self-reciprocal.

Consequences, all exact:

* The substitution `w = z + 1/z` sends `Δ/z³` to the cubic
  `16w³ + 24w² − 13w + 2` (`w_cubic_of_palindromic`, verified by `field_simp; ring`).
* That cubic has discriminant `−80000 < 0`, so exactly one real root and one
  conjugate pair; and `C(−2) = −4 < 0 < 23 = C(−1)` puts the real root in
  `(−2, −1) ⊂ (−2, 2)` (`w_real_root_mem_Ioo`, integer evaluations only).
* A **real** `w` with `w² < 4` gives roots of `z² − wz + 1` of modulus exactly
  one (`normSq_root_eq_one`). So **two branch points lie exactly on the unit
  circle**, and they are the bar-*fixed* ones.
* The remaining four form a single bar-orbit `{a, ā, 1/a, 1/ā}` — two strictly
  inside, two strictly outside.

**The unit circle is therefore not an admissible contour**: it passes through
two branch points. That rules out the one candidate the corpus's own `∮_{S_c}`
notation suggests.

## 2. No residue survives, at any branch point, at any jet level

At a simple (square-root) branch point put `z = z_k + t²`, so `t` is a local
coordinate on the curve and `d/dz = (1/(2t)) d/dt`. On a Laurent term
`a_j t^j` that operator acts by `a_j t^j ↦ (j/2) a_j t^{j−2}`, so after `n`
applications

  `a_j t^j ↦ a_j · 2^{−n} · (∏_{i<n} (j − 2i)) · t^{j−2n}`.

Since `λ_SW^(n) = X^(n) dz = X^(n) · 2t dt`, the residue is `2 ·` the
coefficient of `t^{−2}` in `X^(n)`, which can only come from `j = 2n − 2`. But
that chain product **contains a zero factor** at `i = n − 1`
(`chain_factor_eq_zero`): the term has become a *constant* after `n − 1`
applications, and the `n`-th differentiates it away.

So every residue vanishes identically — **for every branch point and every
`n ≥ 1`, independent of the Puiseux coefficients**. Hence every subset `E`
gives period zero, and `E` is not identifiable because there is nothing to
enclose.

**This is a third route to a conclusion the corpus already holds.**
`prop:sw-classical-jet-exactness` gets `period = 0` from *global* exactness
(`λ_SW^(n) = d(X^(n−1))`) and scopes it as a scope-(b) exclusion of the
classical-jet reading; `QOU.Brings.period_eq_zero_of_total_residue_vanishes`
gets it from the ambient compact surface. This one is **local and per-point**:
it needs neither a global primitive nor the surface, only the parity of
`(1/2t) d/dt`. The q-difference prolongation is untouched by all three.

Ground ring: `ℤ` for the chain product (a parity fact), `ℂ`/`ℝ` for the
modulus computations, which are genuinely archimedean (§7c).

## References

- [leitner2026] §5-brings-surface/sw-period-residue-sum
- [leitner2026] §5-brings-surface/sw-classical-jet-exactness

LaTeX label: `prop:colour-cubic-branch-locus-reciprocal`
-/

namespace QOU.Brings.ColourCubicBranchLocus

open Finset

/-! ## 1. Bar-symmetry of the branch locus -/

/-- The colour cubic's discriminant, up to the overall sign that does not affect
its zero set: `Δ₆(z) = 16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16`. The
coefficient list is palindromic, which is the whole content of this section. -/
noncomputable def disc (z : ℂ) : ℂ :=
  16 * z ^ 6 + 24 * z ^ 5 + 35 * z ^ 4 + 50 * z ^ 3 + 35 * z ^ 2 + 24 * z + 16

/-- **Self-reciprocity.** `z⁶ · Δ(1/z) = Δ(z)` for `z ≠ 0` — the algebraic form
of "the coefficient list reads the same backwards". -/
theorem disc_inv_mul (z : ℂ) (hz : z ≠ 0) : z ^ 6 * disc z⁻¹ = disc z := by
  unfold disc
  field_simp
  ring

/-- **The branch locus is closed under the bar involution `z ↦ 1/z`.**

This is the Hecke bar-involution `q ↦ q⁻¹` acting on the pole locus of
`λ_SW^(n)`. It constrains any admissible enclosed set `E`: bar carries poles
inside the unit circle to poles outside it. -/
theorem branchLocus_inv_mem {z : ℂ} (hz : z ≠ 0) (h : disc z = 0) : disc z⁻¹ = 0 := by
  have h6 : z ^ 6 ≠ 0 := pow_ne_zero _ hz
  have := disc_inv_mul z hz
  rw [h] at this
  exact (mul_eq_zero.mp this).resolve_left h6

/-- The `w = z + 1/z` reduction of the palindromic sextic: `Δ(z)/z³` equals
`16w³ + 24w² − 13w + 2` at `w = z + z⁻¹`. Verified as an identity in `z`. -/
theorem w_cubic_of_palindromic (z : ℂ) (hz : z ≠ 0) :
    16 * (z + z⁻¹) ^ 3 + 24 * (z + z⁻¹) ^ 2 - 13 * (z + z⁻¹) + 2
      = disc z / z ^ 3 := by
  unfold disc
  field_simp
  ring

/-- The reduced cubic, over `ℝ`, whose roots are the `w`-values of the branch points. -/
noncomputable def wCubic (w : ℝ) : ℝ := 16 * w ^ 3 + 24 * w ^ 2 - 13 * w + 2

/-- **The real root lies in `(−2, −1)`** — hence in `(−2, 2)`, which is what puts
its two branch points exactly on the unit circle. Proved from two integer
evaluations, `wCubic (−2) = −4 < 0` and `wCubic (−1) = 23 > 0`, by the
intermediate value theorem. No numerics. -/
theorem wCubic_neg_two : wCubic (-2) = -4 := by unfold wCubic; norm_num

theorem wCubic_neg_one : wCubic (-1) = 23 := by unfold wCubic; norm_num

theorem w_real_root_mem_Ioo : ∃ w ∈ Set.Ioo (-2 : ℝ) (-1), wCubic w = 0 := by
  have hcont : ContinuousOn wCubic (Set.Icc (-2 : ℝ) (-1)) := by
    unfold wCubic; fun_prop
  have h := intermediate_value_Ioo (by norm_num : (-2 : ℝ) ≤ -1) hcont
  have hmem : (0 : ℝ) ∈ Set.Ioo (wCubic (-2)) (wCubic (-1)) := by
    rw [wCubic_neg_two, wCubic_neg_one]; constructor <;> norm_num
  obtain ⟨w, hw, hw0⟩ := h hmem
  exact ⟨w, hw, hw0⟩

/-- **A real `w` with `w² < 4` gives branch points of modulus exactly one.**

The roots of `z² − wz + 1` are `(w ± i√(4−w²))/2`, whose squared modulus is
`(w² + (4−w²))/4 = 1`. So the bar-fixed branch points sit *on* the unit
circle — and the unit circle is therefore **not** an admissible contour. -/
theorem normSq_root_eq_one (w : ℝ) (hw : w ^ 2 < 4) :
    Complex.normSq ((w / 2 : ℝ) + (Real.sqrt (4 - w ^ 2) / 2 : ℝ) * Complex.I) = 1 := by
  have h4 : (0 : ℝ) ≤ 4 - w ^ 2 := by linarith
  have hsq : Real.sqrt (4 - w ^ 2) ^ 2 = 4 - w ^ 2 := Real.sq_sqrt h4
  rw [Complex.normSq_add_mul_I]
  field_simp
  nlinarith [hsq]

/-- The root really is a root of `z² − wz + 1`, so the modulus computation above
is about the branch points and not about an unrelated complex number. -/
theorem is_root_of_w (w : ℝ) (hw : w ^ 2 < 4) :
    ((w / 2 : ℝ) + (Real.sqrt (4 - w ^ 2) / 2 : ℝ) * Complex.I) ^ 2
      - (w : ℂ) * ((w / 2 : ℝ) + (Real.sqrt (4 - w ^ 2) / 2 : ℝ) * Complex.I) + 1 = 0 := by
  have h4 : (0 : ℝ) ≤ 4 - w ^ 2 := by linarith
  -- `simp` normalises `w ^ 2` to `w * w` inside the radicand, so supply the
  -- hypothesis in exactly that shape as well.
  have h4' : (0 : ℝ) ≤ 4 - w * w := by nlinarith
  have hsq' : Real.sqrt (4 - w * w) * Real.sqrt (4 - w * w) = 4 - w * w :=
    Real.mul_self_sqrt h4'
  apply Complex.ext <;>
    simp [Complex.add_re, Complex.add_im, Complex.mul_re, Complex.mul_im, pow_two,
      Complex.I_re, Complex.I_im] <;>
    nlinarith [hsq']

/-! ## 2. No residue survives — stated in the corpus's own local model

`QOU.Brings.RamificationParityMonodromy` already carries exactly the setting
this needs: at a simple ramification point `z = z_c + t²` it models a local
Laurent expansion by its coefficient function `f : ℤ → R` and defines the
classical prolongation as

  `ddz f = fun e => ((e + 2 : ℤ) : R) • f (e + 2)`,

the coefficient form of `d/dz = (1/(2t)) d/dt` with its exponent shift of
exactly `−2`. That file uses the shift's **evenness** (to show `ddz` commutes
with the covering monodromy `t ↦ −t`). What follows uses the **multiplier**
instead, and it is the one exponent where that multiplier vanishes.

Nothing here rebuilds `ddz`; the results below are about the corpus's operator.

§7c: this half is pure algebra over a generic `[CommRing R]` — no ordering, no
`ℝ`. Only §1's modulus computations are archimedean. -/

variable {R : Type*} [CommRing R]

open QOU.Brings.RamificationParityMonodromy in
/-- **The residue slot is annihilated by a single application of `d/dz`.**

`(ddz f)(−2) = ((−2) + 2) • f 0 = 0 • f 0 = 0`, for **every** `f`. The `t^{−2}`
coefficient of a `z`-derivative is always zero, because the only input that could
reach it is the *constant* term `f 0`, and differentiating a constant kills it.

Since `λ_SW^(n) = X^(n) dz = X^(n) · 2t dt`, the residue at a simple branch point
is (up to the nonzero factor `2`) exactly this coefficient. So **every residue of
`λ_SW^(n)` vanishes, at every branch point, for every `n ≥ 1`, whatever the
Puiseux data** — the conclusion needs no global primitive and no compact surface,
only the multiplier `e + 2` at `e = −2`. -/
theorem ddz_residue_slot_eq_zero (f : ℤ → R) : ddz f (-2) = 0 := by
  simp [ddz, shift2]

open QOU.Brings.RamificationParityMonodromy in
/-- Iterating changes nothing: the outermost application is already evaluated at
`e = −2`, so the whole jet tower has vanishing residue. -/
theorem ddz_iterate_residue_slot_eq_zero (f : ℤ → R) (n : ℕ) :
    ddz (ddz^[n] f) (-2) = 0 :=
  ddz_residue_slot_eq_zero _

/-- **The same fact as a chain product, for the general-`n` bookkeeping.**
`n` applications of `(1/(2t)) d/dt` multiply the term `a_j t^j` by
`∏_{i<n} (j − 2i)`; at the critical `j = 2n − 2` (writing `n = m+1`) the factor
at `i = m` is zero. Kept because the probe reports this product across `n`. -/
theorem chain_factor_eq_zero (m : ℕ) :
    ∏ i ∈ range (m + 1), (2 * (m : ℤ) - 2 * (i : ℤ)) = 0 := by
  refine Finset.prod_eq_zero (Finset.self_mem_range_succ m) ?_
  ring

/-- **Hence no enclosed set `E` can produce a nonzero period.** A sum of zeros
over any finite index set is zero, so the choice of `E` is immaterial: the
question "which branch points does the contour enclose" has no content under
the classical-jet prolongation `λ_SW^(n) = X^(n) dz`. -/
theorem period_eq_zero_of_all_residues_vanish
    {ι : Type*} (E : Finset ι) (res : ι → ℤ) (h : ∀ p ∈ E, res p = 0) :
    ∑ p ∈ E, res p = 0 :=
  Finset.sum_eq_zero h

/-- **Non-vanishing of the colour-cubic discriminant at the bar-fixed real points `z = ±1` (`qou-l155`):**
`disc 1 = 200` and `disc (-1) = 4`, so neither `z = 1` nor `z = -1` lies in the branch locus,
and `wCubic 0 = 2`, `wCubic 1 = 29`. -/
theorem disc_at_pm_one_and_wCubic_vals :
    disc 1 = 200 ∧ disc (-1) = 4 ∧ wCubic 0 = 2 ∧ wCubic 1 = 29 := by
  unfold disc wCubic
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num⟩

open QOU.Brings.RamificationParityMonodromy in
/-- **Linearity of residue-slot annihilation under `ddz` (`qou-l155`):**
Any `R`-linear combination of local Puiseux series has vanishing `t⁻²` residue slot after `ddz`. -/
theorem ddz_linear_comb_residue_slot_eq_zero (a b : R) (f g : ℤ → R) :
    ddz (fun e => a * f e + b * g e) (-2) = 0 :=
  ddz_residue_slot_eq_zero _

end QOU.Brings.ColourCubicBranchLocus
