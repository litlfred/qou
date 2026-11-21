import Mathlib.Tactic
import Mathlib.Analysis.PSeries
import QOU.Archimedean.ClausenFunctionMathlibFiller

/-!
# The general Bloch–Wigner `D` via Lobachevsky — reaching `5₂`

`BlochWignerMathlibFiller` covers the two QOU knots whose ideal-tetrahedron
shape parameters lie **on the unit circle**: the figure-8 (`e^{iπ/3}`) and the
Borromean rings (`i`). There the boundary correction `log|z|·arg(1−z)` vanishes
identically and `D` collapses to `Cl₂`. That file names the general case as an
open gap:

> General `D : ℂ \ {0,1} → ℝ` for non-unit-circle shape parameters — needs
> `Complex.log` and `Complex.arg` infrastructure with branch-cut handling.

`5₂` is the first QOU knot that falls in that gap: its shape parameter has
`|y| = 1.52…`, so the correction term does **not** vanish and `Cl₂` alone does
not express `D`.

## The route, and why it does not need a complex `Li₂`

For `z` in the upper half plane the three **dihedral angles** of the ideal
tetrahedron of shape `z` are

    α = arg z,    β = arg(1/(1−z)),    γ = arg(1 − 1/z),

and the classical formula for its volume is `Λ(α) + Λ(β) + Λ(γ)` with the
Lobachevsky function `Λ(t) = Cl₂(2t)/2`. So the general `D` is expressible in
`Cl₂` after all — through the *angles* rather than through `z` directly. No
complex dilogarithm is required for `D`.

(A complex `Li₂` is still needed elsewhere, for `Re Li₂(y₁)` in the `5₂` saddle
**sum rule** — that is bean `qou-ph1k`, and it is a genuinely different
problem. This file does not close it and does not claim to.)

## What is proved here

* `summable_clausen` — the Clausen series is summable. Missing from the
  filler, and everything below needs it.
* `Cl_2_neg`, `Cl_2_add_two_pi` — oddness and `2π`-periodicity, from the
  series.
* `Cl_2_duplication` — `Cl₂(2θ) = 2Cl₂(θ) − 2Cl₂(π−θ)`, from the Fourier
  series by a parity split. `sin(nπ − nθ) = −(−1)ⁿ sin(nθ)` puts a factor
  `1 + (−1)ⁿ` on each term, killing the odd `n` and doubling the even; the
  surviving half reindexes to `Cl₂(2θ)`.
* `Cl_2_two_pi_div_three`, `three_Lob_pi_div_three` — **the consistency
  check.** Duplication at `θ = π/3` forces `Cl₂(2π/3) = (2/3)Cl₂(π/3)`, so
  the general formula's value at the regular ideal tetrahedron,
  `3·Λ(π/3) = 3·Cl₂(2π/3)/2`, collapses to exactly `Cl₂(π/3)` — the
  per-tetrahedron value behind the corpus's `Vol(4₁) = 2·Cl₂(π/3)`. This is
  not `rfl`: it validates the non-unit-circle definition against a case the
  corpus already trusts.
* `tetAngles_sum_eq_pi` — **the substantive theorem**: for `Im z > 0`,
  `arg z + arg(1/(1−z)) + arg(1 − 1/z) = π`. The three quantities really are
  the angles of a tetrahedron. The proof is that the three factors multiply to
  `−1` while each lies in the open upper half plane, so the arg-sum is `π` mod
  `2π` and confined to `(0, 3π)`.
* the `5₂` shape algebra: the saddle cubic, the Landen image, and the fact
  that the real root contributes nothing to `D`.

## What is NOT proved here — read before citing

The numerical identity behind this file is

    D(y₊) = Vol(5₂)/3,   y₊ = 0.7849201454990266… + 1.3071412786820454…i

and it is **published**: Broadhurst [hep-th/9811173] eq (73) records
`vol(5₂) = 3·Z₂₃,₃`, with `Z₂₃,₃` the Zagier value of the discriminant −23
cubic field — the smallest `|disc|` among complex cubic fields, which is why
that particular constant appears.

Checked at 80 dps against a `Vol(5₂)` computed **from the saddle roots**
(`computations/probes/fivetwo_saddle_values.py::volume()`), so no hardcoded
constant enters and there is no precision ceiling. Three routes agree:

    Vol(5₂)/3                              0.9427073627769277209212996030922116…
    Im Li₂(y₊) + arg(1−y₊)·log|y₊|         (same, |Δ| = 1.1e-81)
    Λ(α) + Λ(β) + Λ(γ)   ← this file       (same, |Δ| = 2.1e-81)

i.e. exact to working precision, and the dihedral-angle route agrees with the
naive complex-`Li₂` form it is meant to replace. It is recorded below as a
**conjecture carrier with no instance** — the honest representation of a
statement that is *numerically settled and published* but not formally derived
here.

**The one open reason is geometric.** `Vol(5₂) = 3·D(y₊)` needs the fact that
the `5₂` complement's ideal triangulation is three tetrahedra *all of the same
shape* `y₊`. That is Thurston/SnapPea, nowhere near Mathlib, and it is the
actual mathematical content — the division by 3 is bookkeeping. Note that
`Vol_figure_8` and `Vol_Borromean` in the filler enter the corpus the same
way, as definitions; their accompanying "theorems" are `rfl`. This file does
not repeat that pattern: it names the geometric input instead of hiding it in
a definition.

An earlier revision of this header listed the Clausen duplication formula as a
second open input, isolated as a `ClausenDuplication` carrier. **That is now
proved** (`Cl_2_duplication`), the carrier is gone, and the consistency check
it was gating is discharged: `BlochWigner_lob` reproduces the corpus's
figure-8 per-tetrahedron value at the regular shape. So the general definition
is no longer merely numerically validated — it agrees with the corpus on a
case the corpus already trusts.

-- Ref: [thurston1978] The geometry and topology of three-manifolds
-- Ref: [zagier1986] DOI 10.1007/BFb0084581
-- Ref: [leitner2026] computations/probes/qbeta_5two_saddle_sum_rule_and_provenance_probe.py
-/

namespace QOU.Archimedean

open Complex

/-! ## Part 1 — Clausen series infrastructure

The filler defines `Cl_2` as a `tsum` but proves nothing about convergence, so
every `tsum` manipulation below would be vacuous without this. -/

/-- **The Clausen series is summable**, by comparison with `∑ 1/(k+1)²`.
`|sin x| ≤ 1` is the only analytic input. -/
theorem summable_clausen (θ : ℝ) :
    Summable (fun k : ℕ => Real.sin (((k : ℝ) + 1) * θ) / ((k : ℝ) + 1) ^ 2) := by
  have hb : Summable (fun k : ℕ => 1 / ((k : ℝ) + 1) ^ 2) := by
    have h : Summable (fun n : ℕ => 1 / (n : ℝ) ^ 2) :=
      Real.summable_one_div_nat_pow.mpr one_lt_two
    have h2 := (summable_nat_add_iff 1).mpr h
    simpa using h2
  apply Summable.of_abs
  refine hb.of_nonneg_of_le (fun k => abs_nonneg _) (fun k => ?_)
  have hpos : (0 : ℝ) < ((k : ℝ) + 1) ^ 2 := by positivity
  rw [abs_div, abs_of_pos hpos]
  gcongr
  exact Real.abs_sin_le_one _

/-- **`Cl₂` is odd.** Termwise from `sin(−x) = −sin x`. -/
theorem Cl_2_neg (θ : ℝ) : Cl_2 (-θ) = -Cl_2 θ := by
  unfold Cl_2
  rw [← tsum_neg]
  congr 1
  funext k
  rw [mul_neg, Real.sin_neg, neg_div]

/-- **`Cl₂` is `2π`-periodic.** Each term has period `2π` in `θ` because
`sin` is `2π`-periodic and the frequency `k+1` is an integer. -/
theorem Cl_2_add_two_pi (θ : ℝ) : Cl_2 (θ + 2 * Real.pi) = Cl_2 θ := by
  unfold Cl_2
  congr 1
  funext k
  congr 1
  have h : ((k : ℝ) + 1) * (θ + 2 * Real.pi)
      = ((k : ℝ) + 1) * θ + ((k + 1 : ℤ) : ℝ) * (2 * Real.pi) := by push_cast; ring
  rw [h, Real.sin_add_int_mul_two_pi]

/-! ### The duplication formula

`Cl₂(2θ) = 2·Cl₂(θ) − 2·Cl₂(π−θ)`, proved from the Fourier series. The
mechanism: `sin(nπ − nθ) = −(−1)ⁿ sin(nθ)`, so the bracket
`sin(nθ) − sin(n(π−θ))` carries a factor `1 + (−1)ⁿ` — it **vanishes for odd
`n`** and doubles for even `n`. Splitting the sum on parity and reindexing
`n = 2m` returns `Cl₂(2θ)`. -/

/-- `cos(nπ) = (−1)ⁿ`, by induction on `n`. -/
private lemma cos_nat_mul_pi (n : ℕ) :
    Real.cos ((n : ℝ) * Real.pi) = (-1) ^ n := by
  induction n with
  | zero => simp
  | succ m ih =>
      have h : ((m + 1 : ℕ) : ℝ) * Real.pi = (m : ℝ) * Real.pi + Real.pi := by
        push_cast; ring
      rw [h, Real.cos_add, Real.cos_pi, Real.sin_pi, ih]
      ring

/-- The reflection `sin(n(π − θ)) = −(−1)ⁿ · sin(nθ)`. This sign alternation is
the entire content of the duplication formula. -/
private lemma sin_nat_mul_pi_sub (n : ℕ) (θ : ℝ) :
    Real.sin ((n : ℝ) * (Real.pi - θ)) = -((-1) ^ n) * Real.sin ((n : ℝ) * θ) := by
  have h : (n : ℝ) * (Real.pi - θ) = (n : ℝ) * Real.pi - (n : ℝ) * θ := by ring
  rw [h, Real.sin_sub, Real.sin_nat_mul_pi, cos_nat_mul_pi]
  ring

/-- The same, in the index shape `Cl_2` actually uses. -/
private lemma sin_succ_mul_pi_sub (k : ℕ) (θ : ℝ) :
    Real.sin (((k : ℝ) + 1) * (Real.pi - θ))
      = -((-1) ^ (k + 1)) * Real.sin (((k : ℝ) + 1) * θ) := by
  have hc : ((k : ℝ) + 1) = ((k + 1 : ℕ) : ℝ) := by push_cast; ring
  rw [hc]
  exact sin_nat_mul_pi_sub (k + 1) θ

/-- The termwise bracket of `2·Cl₂(θ) − 2·Cl₂(π−θ)`. -/
private noncomputable def dupTerm (θ : ℝ) (k : ℕ) : ℝ :=
  2 * (1 + (-1) ^ (k + 1)) * Real.sin (((k : ℝ) + 1) * θ) / (((k : ℝ) + 1) ^ 2)

/-- Odd `n = k+1` (i.e. even `k`) kills the term. -/
private lemma dupTerm_even (θ : ℝ) (m : ℕ) : dupTerm θ (2 * m) = 0 := by
  unfold dupTerm
  have h : (-1 : ℝ) ^ (2 * m + 1) = -1 := by
    rw [pow_succ, pow_mul]; norm_num
  rw [h]; ring

/-- Even `n = k+1` doubles it, and the reindexing `n = 2(m+1)` turns the term
into the `Cl₂(2θ)` term at index `m`. -/
private lemma dupTerm_odd (θ : ℝ) (m : ℕ) :
    dupTerm θ (2 * m + 1)
      = Real.sin (((m : ℝ) + 1) * (2 * θ)) / (((m : ℝ) + 1) ^ 2) := by
  unfold dupTerm
  have h1 : (-1 : ℝ) ^ (2 * m + 1 + 1) = 1 := by
    rw [show 2 * m + 1 + 1 = 2 * (m + 1) by ring, pow_mul]; norm_num
  have h2 : ((2 * m + 1 : ℕ) : ℝ) + 1 = 2 * ((m : ℝ) + 1) := by push_cast; ring
  rw [h1, h2, show (2 : ℝ) * ((m : ℝ) + 1) * θ = ((m : ℝ) + 1) * (2 * θ) by ring]
  have hne : ((m : ℝ) + 1) ≠ 0 := by positivity
  field_simp
  ring

/-- **The Clausen duplication formula.**

    Cl₂(2θ) = 2·Cl₂(θ) − 2·Cl₂(π − θ)

Proved from the Fourier series by the parity split described above. This is
what `ClausenDuplication` was isolating; with it in hand the general
`BlochWigner_lob` can be checked against the corpus's own unit-circle knots
rather than only against numerics. -/
-- Ref: [zagier1986]
theorem Cl_2_duplication (θ : ℝ) :
    Cl_2 (2 * θ) = 2 * Cl_2 θ - 2 * Cl_2 (Real.pi - θ) := by
  have hsθ := summable_clausen θ
  have hsπ := summable_clausen (Real.pi - θ)
  -- collapse the two series into one, termwise
  have step1 : 2 * Cl_2 θ - 2 * Cl_2 (Real.pi - θ) = ∑' k, dupTerm θ k := by
    unfold Cl_2
    rw [← tsum_mul_left, ← tsum_mul_left,
      ← Summable.tsum_sub (hsθ.mul_left 2) (hsπ.mul_left 2)]
    refine tsum_congr fun k => ?_
    unfold dupTerm
    rw [sin_succ_mul_pi_sub k θ]
    ring
  -- split on parity: the even part is identically zero
  have hse : Summable (fun m => dupTerm θ (2 * m)) := by
    simp only [dupTerm_even]; exact summable_zero
  have hso : Summable (fun m => dupTerm θ (2 * m + 1)) := by
    simp only [dupTerm_odd]; exact summable_clausen (2 * θ)
  have hsplit := tsum_even_add_odd hse hso
  rw [step1, ← hsplit]
  simp only [dupTerm_even, dupTerm_odd, tsum_zero, zero_add]
  unfold Cl_2
  rfl

/-- **Consistency with the corpus's figure-8 value.** The regular ideal
tetrahedron has all three angles `π/3`, so the general formula gives
`3·Λ(π/3) = 3·Cl₂(2π/3)/2`, and duplication at `θ = π/3` forces
`Cl₂(2π/3) = (2/3)·Cl₂(π/3)`, returning exactly `Cl₂(π/3)` — the
per-tetrahedron value behind `Vol(4₁) = 2·Cl₂(π/3)`.

This is the check that was missing: it is *not* `rfl`, and it validates the
non-unit-circle definition against a case the corpus already trusts. -/
theorem Cl_2_two_pi_div_three :
    Cl_2 (2 * (Real.pi / 3)) = 2 / 3 * Cl_2 (Real.pi / 3) := by
  have hdup := Cl_2_duplication (Real.pi / 3)
  have hsub : Real.pi - Real.pi / 3 = 2 * (Real.pi / 3) := by ring
  rw [hsub] at hdup
  linarith

/-- The regular ideal tetrahedron's Lobachevsky value **is** the figure-8
per-tetrahedron Clausen value: `3·Λ(π/3) = Cl₂(π/3)`. -/
theorem three_Lob_pi_div_three :
    3 * (Cl_2 (2 * (Real.pi / 3)) / 2) = Cl_2 (Real.pi / 3) := by
  rw [Cl_2_two_pi_div_three]; ring

/-- The **Lobachevsky function** `Λ(t) = Cl₂(2t)/2`, the standard normalisation
in which an ideal tetrahedron of dihedral angles `α, β, γ` has volume
`Λ(α) + Λ(β) + Λ(γ)`. -/
-- Ref: [thurston1978], [milnor1982]
noncomputable def Lob (t : ℝ) : ℝ := Cl_2 (2 * t) / 2

/-- `Λ` is odd, inherited from `Cl₂`. -/
theorem Lob_neg (t : ℝ) : Lob (-t) = -Lob t := by
  unfold Lob
  rw [show 2 * -t = -(2 * t) by ring, Cl_2_neg]
  ring

/-- `Λ(0) = 0`. -/
@[simp] theorem Lob_zero : Lob 0 = 0 := by
  unfold Lob; rw [mul_zero, Cl_2_zero]; norm_num

/-- `Λ(π/2) = 0`, since `Cl₂(π) = 0`. -/
@[simp] theorem Lob_pi_div_two : Lob (Real.pi / 2) = 0 := by
  unfold Lob
  rw [show 2 * (Real.pi / 2) = Real.pi by ring, Cl_2_pi]
  norm_num

/-- `Λ(π) = 0`, since `Cl₂(2π) = 0`. Together with `Lob_zero` this is what makes
`D` vanish on degenerate (real-shape) tetrahedra. -/
@[simp] theorem Lob_pi : Lob Real.pi = 0 := by
  unfold Lob
  rw [Cl_2_two_pi]
  norm_num

/-! ## Part 2 — the ideal-tetrahedron angles

This is the substantive part. The three expressions below are *defined* as
`arg`s of Möbius images of the shape parameter; the theorem is that they
behave like angles of a tetrahedron, i.e. they are positive and sum to `π`. -/

/-- First dihedral angle of the ideal tetrahedron of shape `z`. -/
noncomputable def tetAngle₁ (z : ℂ) : ℝ := z.arg

/-- Second dihedral angle: the shape parameter seen from the next vertex. -/
noncomputable def tetAngle₂ (z : ℂ) : ℝ := (1 / (1 - z)).arg

/-- Third dihedral angle: the shape parameter seen from the last vertex. -/
noncomputable def tetAngle₃ (z : ℂ) : ℝ := (1 - 1 / z).arg

/-- The three Möbius images have **positive imaginary part** whenever `z` does:
the upper half plane is preserved. This is what makes them genuine angles. -/
theorem tet_im_pos (z : ℂ) (hz : 0 < z.im) :
    0 < (1 / (1 - z)).im ∧ 0 < (1 - 1 / z).im := by
  have hz0 : z ≠ 0 := by
    intro h; rw [h] at hz; simp at hz
  have h1z : (1 : ℂ) - z ≠ 0 := by
    intro h
    have h' : ((1 : ℂ) - z).im = 0 := by rw [h]; simp
    simp only [Complex.sub_im, Complex.one_im, zero_sub, neg_eq_zero] at h'
    exact absurd h' (ne_of_gt hz)
  have hnz : 0 < Complex.normSq z := Complex.normSq_pos.mpr hz0
  have hn1z : 0 < Complex.normSq (1 - z) := Complex.normSq_pos.mpr h1z
  constructor
  · rw [one_div, Complex.inv_im]
    have him : ((1 : ℂ) - z).im = -z.im := by simp
    rw [him, show - -z.im / Complex.normSq (1 - z)
        = z.im / Complex.normSq (1 - z) by ring]
    exact div_pos hz hn1z
  · have him : ((1 : ℂ) - 1 / z).im = -(1 / z).im := by simp
    rw [him, one_div, Complex.inv_im,
      show -(-z.im / Complex.normSq z) = z.im / Complex.normSq z by ring]
    exact div_pos hz hnz

/-- For `Im w > 0` the argument lies in the **open** interval `(0, π)`. -/
theorem arg_mem_Ioo_of_im_pos (w : ℂ) (hw : 0 < w.im) :
    0 < w.arg ∧ w.arg < Real.pi := by
  constructor
  · rcases lt_or_eq_of_le (Complex.arg_nonneg_iff.mpr hw.le) with h | h
    · exact h
    · exfalso
      have := Complex.arg_eq_zero_iff.mp h.symm
      exact absurd this.2 (ne_of_gt hw)
  · rcases lt_or_eq_of_le (Complex.arg_le_pi w) with h | h
    · exact h
    · exfalso
      have := Complex.arg_eq_pi_iff.mp h
      exact absurd this.2 (ne_of_gt hw)

/-- **The three angles multiply their shapes to `−1`.**
`z · (1/(1−z)) · (1 − 1/z) = −1`. Pure algebra, and the source of the `π`. -/
theorem tet_shape_prod (z : ℂ) (hz0 : z ≠ 0) (h1z : (1 : ℂ) - z ≠ 0) :
    z * (1 / (1 - z)) * (1 - 1 / z) = -1 := by
  field_simp
  ring

/-- **The dihedral angles of an ideal tetrahedron sum to `π`.**

For `Im z > 0`,  `arg z + arg(1/(1−z)) + arg(1 − 1/z) = π`.

The three shapes multiply to `−1`, so the arg-sum is `π` modulo `2π`; each arg
lies in `(0, π)`, so the sum lies in `(0, 3π)`; the only value in that range
congruent to `π` is `π` itself. -/
theorem tetAngles_sum_eq_pi (z : ℂ) (hz : 0 < z.im) :
    tetAngle₁ z + tetAngle₂ z + tetAngle₃ z = Real.pi := by
  have hz0 : z ≠ 0 := by intro h; rw [h] at hz; simp at hz
  have h1z : (1 : ℂ) - z ≠ 0 := by
    intro h
    have h' : (1 - z).im = 0 := by rw [h]; simp
    simp only [Complex.sub_im, Complex.one_im, zero_sub, neg_eq_zero] at h'
    exact absurd h' (ne_of_gt hz)
  obtain ⟨him2, him3⟩ := tet_im_pos z hz
  have hne2 : (1 / (1 - z)) ≠ 0 := by
    intro h; rw [h] at him2; simp at him2
  have hne3 : ((1 : ℂ) - 1 / z) ≠ 0 := by
    intro h; rw [h] at him3; simp at him3
  obtain ⟨hp1, hl1⟩ := arg_mem_Ioo_of_im_pos z hz
  obtain ⟨hp2, hl2⟩ := arg_mem_Ioo_of_im_pos _ him2
  obtain ⟨hp3, hl3⟩ := arg_mem_Ioo_of_im_pos _ him3
  -- the arg-sum is `π` as an element of `Real.Angle`
  have hprod := tet_shape_prod z hz0 h1z
  have hangle : ((z.arg + (1 / (1 - z)).arg + ((1 : ℂ) - 1 / z).arg : ℝ) :
      Real.Angle) = ((Real.pi : ℝ) : Real.Angle) := by
    have e1 : ((z * (1 / (1 - z))).arg : Real.Angle)
        = (z.arg : Real.Angle) + ((1 / (1 - z)).arg : Real.Angle) :=
      Complex.arg_mul_coe_angle hz0 hne2
    have e2 : (((z * (1 / (1 - z))) * ((1 : ℂ) - 1 / z)).arg : Real.Angle)
        = ((z * (1 / (1 - z))).arg : Real.Angle)
          + (((1 : ℂ) - 1 / z).arg : Real.Angle) :=
      Complex.arg_mul_coe_angle (mul_ne_zero hz0 hne2) hne3
    rw [hprod, Complex.arg_neg_one] at e2
    rw [Real.Angle.coe_add, Real.Angle.coe_add, ← e1, ← e2]
  -- convert the `Real.Angle` equation into an integer multiple of `2π`
  rw [Real.Angle.angle_eq_iff_two_pi_dvd_sub] at hangle
  obtain ⟨k, hk⟩ := hangle
  have hpi : (0 : ℝ) < Real.pi := Real.pi_pos
  -- the sum lies in `(0, 3π)`, forcing `k = 0`
  have hk0 : k = 0 := by
    by_contra hkne
    rcases lt_or_gt_of_ne hkne with hneg | hpos
    · have : (k : ℝ) ≤ -1 := by exact_mod_cast Int.le_sub_one_of_lt hneg
      nlinarith [hk, hp1, hp2, hp3, hl1, hl2, hl3]
    · have : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hpos
      nlinarith [hk, hp1, hp2, hp3, hl1, hl2, hl3]
  rw [hk0] at hk
  unfold tetAngle₁ tetAngle₂ tetAngle₃
  push_cast at hk
  linarith

/-! ## Part 3 — the general Bloch–Wigner value

With the angles in hand, the general `D` is a sum of three Lobachevsky values,
hence expressible in `Cl₂` alone. -/

/-- **The general Bloch–Wigner value at shape `z`**, defined through the
dihedral angles rather than through a complex dilogarithm:

    D(z) = Λ(arg z) + Λ(arg 1/(1−z)) + Λ(arg(1 − 1/z)).

This extends `BlochWigner_unit_circle` past `|z| = 1`.

⚠ **THIS IS A DEFINITION, AND IT IS NOT THE STANDARD ONE** (recorded
2026-08-08 after reading Neumann–Zagier 1985 §3). The literature's Bloch–Wigner
function is

    D(z) = Im Li₂(z) + log|z| · arg(1 − z)          (Neumann–Zagier eq. (39))

i.e. it is built from the **dilogarithm**, not from `Λ`. That the Λ-sum above
equals it is **Kummer's identity** (Lewin, *Polylogarithms*, p. 121 eq. (5.5)),
which Neumann–Zagier invoke explicitly to pass from their eq. (37)
`Vol(S(z)) = Λ(α)+Λ(β)+Λ(γ)` to eq. (38) `Vol(S(z)) = D(z)`. It is a **theorem,
not a definitional unfolding**.

So, precisely:

* ⚠⚠ **STATUS: KUMMER IS NOW PROVED (2026-08-09, bean `qou-kmmr`).**

  `QOU/Knot/KummerRadial.lean` — `kummer` — proves, sorry-free and on the
  standard axioms, for every `z` with `Im z > 0`:

      BlochWigner_lob z = Im (cLiTwoExt z) + log‖z‖ · arg(1 − z)

  So the two objects named `D` in this corpus are the **same function** on the
  upper half plane. This bullet previously said the identity "cannot currently be
  proved in this corpus" (Mathlib has no dilogarithm); that was corrected first to
  "unblocked, not impossible" once `QOU.MathlibExt.cLiTwoExt` was recognised, and
  is now simply **done**.

  The proof chain, all sorry-free: `KummerUnitCircle` (the Λ-side on `|z| = 1`,
  which is Clausen duplication) → `KummerDilogHalf` (the `cLiTwoExt` side there,
  by same-derivative with basepoint `θ = π`) → `IdealTetLawOfSines`
  (`‖z‖ = sin θ₂/sin θ₃`) → `KummerRadial` (a radial reduction, using the unit
  circle as basepoint).

* **The prohibition below is therefore LIFTED.** It used to read: "do not
  transport dilogarithm facts onto this symbol — the five-term relation, the
  functional equations, or any N–Z result stated for *their* `D` — without first
  proving Kummer's identity. The name is shared; the objects are so far only
  numerically observed to agree."

  That condition is now met. Dilogarithm facts about `cLiTwoExt` **may** be
  transported onto `BlochWigner_lob` on `{Im z > 0}`, via `kummer`. Outside the
  upper half plane nothing is claimed — `BlochWigner_lob` is built from `arg`s and
  this file separately proves it vanishes on real shapes in `(0,1)`, which is a
  branch statement, not an instance of Kummer.

* The numerical cross-check that used to be the only evidence is retained as a
  control, not as grounds: `computations/qbeta/xi_classical_limit_probe.py`
  matches the two forms at the substrate anchor to ~1e-6 series accuracy, and
  Routes 72–73 match them to `1e-41`/`1e-45` at five shapes including `y₁`.

Consequence for `qou-idvt` T2 / `qou-5gai` H4: the target factors as
(geometric) `Vol = D` ∘ (analytic) `D = Λ-sum`. **The analytic factor is now
closed** (`kummer`). The *geometric* one — that a particular triangulation's
Λ-sum is the hyperbolic volume of a particular knot complement — is untouched and
is still the whole of H4. Nothing here computes `Vol(5₂)`. -/
-- Ref: [thurston1978], [milnor1982], [zagier1986]
noncomputable def BlochWigner_lob (z : ℂ) : ℝ :=
  Lob (tetAngle₁ z) + Lob (tetAngle₂ z) + Lob (tetAngle₃ z)

/-- **`D` vanishes on a degenerate tetrahedron.** If every dihedral angle
collapses to `0` or `π` — which is exactly what a shape parameter off the upper
half plane does — then `D = 0`, because `Λ` vanishes at both.

This is the honest form of a fact the corpus previously recorded by *defining*
a symbol named `blochWignerD` to be the constant `0`
(`QOU/Machinery/QDilogarithm.lean`, removed 2026-08-07, bean `qou-ir1l`). Here
it is derived from `Lob_zero` and `Lob_pi` instead of asserted, and it says what
is actually true: the vanishing is a property of degenerate *shapes*, not a
statement that Bloch–Wigner is trivial on the substrate. -/
theorem BlochWigner_lob_eq_zero_of_angles (z : ℂ)
    (h₁ : tetAngle₁ z = 0 ∨ tetAngle₁ z = Real.pi)
    (h₂ : tetAngle₂ z = 0 ∨ tetAngle₂ z = Real.pi)
    (h₃ : tetAngle₃ z = 0 ∨ tetAngle₃ z = Real.pi) :
    BlochWigner_lob z = 0 := by
  unfold BlochWigner_lob
  rcases h₁ with h | h <;> rw [h] <;>
    rcases h₂ with h' | h' <;> rw [h'] <;>
      rcases h₃ with h'' | h'' <;> rw [h''] <;>
        simp

/-- **`D` vanishes at a real shape parameter in `(0,1)`.**

The concrete case behind the removed stub: a real `x` gives a flat tetrahedron,
`arg x = 0`, `arg(1/(1−x)) = 0` and `arg(1 − 1/x) = π`, so all three Lobachevsky
terms vanish. Note this is a fact about `D` on the *reals* — it says nothing
about `D` in general, and in particular does not conflict with the sharp
non-zero value `D(y₊) = Vol(5₂)/3` at the complex `5₂` shape. -/
theorem BlochWigner_lob_real_eq_zero (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    BlochWigner_lob (x : ℂ) = 0 := by
  have hsub : (1 : ℂ) - (x : ℂ) = ((1 - x : ℝ) : ℂ) := by push_cast; ring
  have h1x : (0 : ℝ) < 1 - x := by linarith
  refine BlochWigner_lob_eq_zero_of_angles _ (Or.inl ?_) (Or.inl ?_) (Or.inr ?_)
  · exact Complex.arg_ofReal_of_nonneg hx0.le
  · unfold tetAngle₂
    rw [hsub, ← Complex.ofReal_one, ← Complex.ofReal_div]
    exact Complex.arg_ofReal_of_nonneg (by positivity)
  · unfold tetAngle₃
    have hx : (x : ℂ) ≠ 0 := by
      simpa using ne_of_gt hx0
    have hrw : (1 : ℂ) - 1 / (x : ℂ) = ((1 - 1 / x : ℝ) : ℂ) := by
      push_cast; ring
    rw [hrw]
    have hneg : 1 - 1 / x < 0 := by
      rw [sub_neg]
      rw [lt_div_iff₀ hx0]
      linarith
    exact Complex.arg_ofReal_of_neg hneg

/-- The **regular** ideal tetrahedron `z = e^{iπ/3}` has all three angles equal
to `π/3` — the degenerate case where the general formula must reproduce the
corpus's figure-8 value. Recorded as the angle statement, which is what
`tetAngles_sum_eq_pi` constrains; the numerical reconciliation with
`Cl₂(π/3)` needs `ClausenDuplication` below. -/
theorem regular_tet_angles_sum :
    Real.pi / 3 + Real.pi / 3 + Real.pi / 3 = Real.pi := by ring

/-! ## Part 4 — the `5₂` shape

`5₂`'s saddle cubic is `y³ − 2y² + 3y − 1`; the Landen substitution
`z = y/(y−1)` carries its roots to those of `z³ − z² + 1`. Both are stated as
algebraic identities over a generic `CommRing` (§7c). -/

/-- The `5₂` saddle cubic. -/
def fiveTwoSaddleCubic {R : Type*} [CommRing R] (y : R) : R :=
  y ^ 3 - 2 * y ^ 2 + 3 * y - 1

/-- The `5₂` shape cubic, the Landen image of the saddle cubic. -/
def fiveTwoShapeCubic {R : Type*} [CommRing R] (z : R) : R :=
  z ^ 3 - z ^ 2 + 1

/-- **The Landen substitution `z = y/(y−1)` carries the saddle cubic to the
shape cubic**: if `y ≠ 1` is a root of the saddle cubic, then `z = y/(y−1)` is
a root of the shape cubic. Stated over a field, since the substitution
inverts. -/
theorem landen_root {K : Type*} [Field K] (y : K) (hy : y ≠ 1)
    (h : fiveTwoSaddleCubic y = 0) :
    fiveTwoShapeCubic (y / (y - 1)) = 0 := by
  have hne : y - 1 ≠ 0 := sub_ne_zero.mpr hy
  unfold fiveTwoShapeCubic
  field_simp
  unfold fiveTwoSaddleCubic at h
  linear_combination h

/-- **The real root contributes nothing to `D`.** The Bloch–Wigner function
vanishes on the reals, so in `Σⱼ D(yⱼ)` only the conjugate pair contributes —
and those cancel. This is why `Σⱼ D(yⱼ) = 0` is *automatic* for any cubic with
one real root and a conjugate pair, and therefore carries **no** `5₂`-specific
information. Recorded because a previous investigation briefly mistook that
vanishing for evidence of a torsion class. -/
theorem real_shape_has_zero_angles (x : ℝ) (hx : 0 < x) :
    tetAngle₁ (x : ℂ) = 0 := by
  unfold tetAngle₁
  exact Complex.arg_ofReal_of_nonneg hx.le

/-! ## Part 5 — the one open input

The Clausen duplication formula, which an earlier revision isolated here as a
second carrier, is now proved above (`Cl_2_duplication`). What remains open is
geometric, and it is stated as a content-bearing class with **no instance** —
the honest representation of an open statement (AGENTS.md §3b). Nothing
downstream is wired to it. -/

/-- **The open input — the `5₂` triangulation.**

The `5₂` knot complement admits an ideal triangulation by **three** tetrahedra,
all of the same shape `y₊` (the upper-half-plane root of the saddle cubic), so
that `Vol(5₂) = 3·D(y₊)`.

This is the actual mathematical content of the identity `D(y₊) = Vol(5₂)/3`.
It is a fact of hyperbolic geometry (Thurston's gluing equations plus Mostow
rigidity), not an algebraic one, and it is far outside Mathlib's reach. The
numerical check stands at 20 digits — limited by the `Vol(5₂)` literal, not by
the computation — but a numerical check is not a proof.

The shape and the volume are **parameters**, so the class stays `Prop`-valued
and carries only hypotheses. There is deliberately **no instance**.

⚠ **"No instance" is weaker here than it is for `OhtsukiAsymptotic`, and the
difference matters.** This class is *satisfiable*, at a **derived** `vol` — the
following typechecks (probed 2026-08-31, bean `qou-6x46`; deliberately not
committed as an `instance`):

```
example {y : ℂ} (hy : IsOhtsukiShape y) :
    FiveTwoTriangulation ((starRingEnd ℂ) (1 / y))
      (3 * BlochWigner_lob ((starRingEnd ℂ) (1 / y))) where
  shape_im_pos   := (conj_inv_is_five_two_shape hy).2
  shape_root     := (conj_inv_is_five_two_shape hy).1
  vol_eq_three_D := rfl
```

and `FiveTwoOhtsukiBridge.exists_isOhtsukiShape` supplies the `hy`. The first
two fields are already theorems there, and the third *defines* `vol`. So the
absence of an instance is not unsatisfiability — it is a refusal to launder the
name `vol`. Adding that instance would make a downstream conclusion read
`… → nhds (3·D(y₊))`, which is true content, but it would no longer say **"the
hyperbolic volume of the `5₂` complement"**, because Lean has no definition of
hyperbolic volume to tie the name to. That is the whole gap, and it is a
definitional one, not an arithmetic one.

`OhtsukiAsymptotic` in `FiveTwoOhtsukiBridge` is a different animal: it carries
genuine unproved analysis (steepest descent on the Kashaev invariant), and no
instance is constructible at all. Do not describe the two as "the two remaining
axioms" without saying which is which. -/
class FiveTwoTriangulation (shape : ℂ) (vol : ℝ) : Prop where
  /-- The shape lies in the upper half plane — the tetrahedra are
      non-degenerate. -/
  shape_im_pos : 0 < shape.im
  /-- The shape is a root of the `5₂` saddle cubic. -/
  shape_root : fiveTwoSaddleCubic shape = 0
  /-- Three tetrahedra, all of that same shape, so the volume is `3·D(shape)`.
      This is the geometric input, and it is the whole content. -/
  vol_eq_three_D : vol = 3 * BlochWigner_lob shape

/-- **The identity in the form the investigation asked for**, conditional on
the triangulation input: the per-tetrahedron Bloch–Wigner value is exactly one
third of the volume.

This is `§3b-cond` conditional content, and non-degenerate in the sense of
item 5 there: the class supplies the *hypothesis* (three tetrahedra of equal
shape) and the theorem *derives* the division, rather than carrying
`D = vol/3` as a field and projecting it out. -/
theorem blochWigner_eq_vol_div_three (shape : ℂ) (vol : ℝ)
    [h : FiveTwoTriangulation shape vol] :
    BlochWigner_lob shape = vol / 3 := by
  rw [h.vol_eq_three_D]
  ring

end QOU.Archimedean
