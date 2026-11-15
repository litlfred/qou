/-
# The L/R bit is a choice of root, and `|q| > 1` is one way of making it

Bean `qou-wkcd` (epic `qou-qs0e`, blocks `qou-hlx7`). Follows
`OneSidedWeakVertex.lean` (#7844): the one-sided flavour vertex is `W_L = q⁻¹ J` or
`W_R = q J` with `J = P₊ − P₋`, and the bar involution `q ↔ q⁻¹, s ↔ s⁻¹` swaps them.
This file asks what, if anything, the regime `|q| > 1` adds.

## The letter does not know its parameter

`IsLetter q s` is `s² = h s + 1` with `h = q − q⁻¹`, and `h` is unchanged by
`q ↦ −q⁻¹`. So a letter fixes only `h`: the two roots `{q, −q⁻¹}` of `t² − h t − 1`
are its eigenvalues, and "the parameter" is a LABEL of one of them.

* `isLetter_neg_inv`: `IsLetter q s ↔ IsLetter (−q⁻¹) s`.
* `Pp_neg_inv`, `Pm_neg_inv`, `grading_neg_inv`: relabelling the root swaps the two
  eigenlines and sends `J ↦ −J`.
* `oneSidedL_neg_inv`: **relabelling the root turns `W_L` into `W_R`**, with the letter
  unchanged. `skein_neg_inv`: it turns the skein weighting `q s − q⁻¹ s⁻¹` into minus
  the mirror weighting `q⁻¹ s − q s⁻¹`. So "which crossing carries `q`", "which root is
  called `q`", and "L vs R" are one bit (and, by #7844's `oneSidedL_flip`, so is bar).

## Two intrinsic selectors on an ordered field, and how they differ

Over an ordered field with `h ≠ 0` the two roots have opposite signs and moduli on
opposite sides of `1`, so the letter (through `h` alone) determines two lines:

* `signLine`: the line of the POSITIVE eigenvalue. Label-independent
  (`signLine_neg_inv`), and **flavour-invariant**: the inverse letter `s⁻¹` has the
  same positive line (`signLine_flip`).
* `modLine`: the line of the eigenvalue of modulus `> 1`. Label-independent
  (`modLine_neg_inv`), and **flavour-covariant**: for `s⁻¹` it is the other line
  (`modLine_flip`).
* `modLine_eq_signLine_iff`: on a letter with positive parameter `q`, the two agree iff
  `1 < q`, i.e. iff `h > 0` (`h_pos_iff`).

So the regime does not create a selector the sign rule lacks. It makes the modulus rule
agree with the sign rule (the owner's D-H1 = A labelling, `+q` line) on the letters with
`h > 0`, and disagree on their inverses. Under the #7836 reading "flavour = letter
orientation", the modulus rule would put `u_L` and `d_L` on different lines
(`modLine_flip` with `signLine_flip`). Scope (b) **conditional on that reading**: the
invariant is that inversion inverts moduli and preserves signs.

## The classical point collapses the bit

`oneSidedL_eq_oneSidedR_iff`: `W_L = W_R` iff `h = 0` (i.e. `q² = 1`). At `q = 1` there
is one vertex, not two.

## Archimedean: a long positive braid projects onto the dominant line

`pow_eq`: `s^N = q^N P₊ + (−q⁻¹)^N P₋` (generic). Over `ℝ`, with `1 < |q|`,
`q^{−N} s^N → P₊` (`tendsto_normalised_pow`). This is a derived, non-conventional
selection, but it is relative to the letter `s`: the same limit for `s⁻¹` gives `P₋`.

Base ring (§7c): §§1–2 generic `[Field K] [Ring A] [Algebra K A]`; §3 needs an ORDER
(`[LinearOrder K] [IsStrictOrderedRing K]`); §5 is the archimedean limit over `ℝ`.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [kazhdan-lusztig1979] https://doi.org/10.1007/BF01390031
-/
import QOU.QuarkState.OneSidedWeakVertex
import Mathlib.Analysis.SpecificLimits.Basic

namespace QOU.QuarkState.WeakChiralityRootLabel

open QOU.QuarkState.Helicity QOU.QuarkState.OneSidedWeakVertex

/-! ## 1. The parameter is a label of one root -/

section Label

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]
variable {q : K} {s : A}

theorem h_neg_inv (q : K) : (-q⁻¹) - (-q⁻¹)⁻¹ = q - q⁻¹ := by
  rw [inv_neg, inv_inv]; ring

theorem bracket_neg_inv (q : K) : (-q⁻¹) + (-q⁻¹)⁻¹ = -(q + q⁻¹) := by
  rw [inv_neg, inv_inv]; ring

/-- **A letter does not know its parameter**: `q` and `−q⁻¹` give the same relation. -/
theorem isLetter_neg_inv : IsLetter q s ↔ IsLetter (-q⁻¹) s := by
  unfold IsLetter; rw [h_neg_inv]

theorem flip_neg_inv : flip (-q⁻¹) s = flip q s := by
  unfold Helicity.flip; rw [h_neg_inv]

/-- Relabelling the root swaps the lines: `P₊(−q⁻¹) = P₋(q)`. -/
theorem Pp_neg_inv : Pp (-q⁻¹) s = Pm q s := by
  unfold Pp Pm
  rw [bracket_neg_inv, inv_neg, inv_inv, neg_smul, ← smul_neg]
  congr 1
  rw [neg_add, neg_neg, neg_smul, add_comm]
  abel

/-- `P₋(−q⁻¹) = P₊(q)`. -/
theorem Pm_neg_inv : Pm (-q⁻¹) s = Pp q s := by
  unfold Pp Pm
  rw [bracket_neg_inv, inv_neg, neg_smul, ← smul_neg]
  congr 1
  rw [neg_sub, neg_smul, sub_neg_eq_add]

/-- Relabelling the root sends `J ↦ −J`. -/
theorem grading_neg_inv : grading (-q⁻¹) s = -grading q s := by
  unfold grading; rw [Pp_neg_inv, Pm_neg_inv, neg_sub]

/-- **Relabelling the root turns the L-only vertex into the R-only vertex**, with the
same letter `s`. -/
theorem oneSidedL_neg_inv (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedL (-q⁻¹) s = oneSidedR q s := by
  have hq' : (-q⁻¹ : K) ≠ 0 := neg_ne_zero.mpr (inv_ne_zero hq)
  have hq2' : (-q⁻¹) + (-q⁻¹)⁻¹ ≠ 0 := by rw [bracket_neg_inv]; exact neg_ne_zero.mpr hq2
  rw [oneSidedL_eq hq' hq2' (isLetter_neg_inv.mp hs), grading_neg_inv, inv_neg, inv_inv,
    oneSidedR_eq hq hq2 hs, neg_smul, smul_neg, neg_neg]

/-- **The skein weighting under relabelling**: `q s − q⁻¹ s⁻¹` becomes minus the mirror
weighting `q⁻¹ s − q s⁻¹`. "Which crossing carries `q`" is "which root is called `q`". -/
theorem skein_neg_inv :
    (-q⁻¹) • s - (-q⁻¹)⁻¹ • flip (-q⁻¹) s = -(q⁻¹ • s - q • flip q s) := by
  rw [flip_neg_inv, inv_neg, inv_inv, neg_smul, neg_smul, neg_sub]
  abel

end Label

/-! ## 2. At `h = 0` the two vertices coincide -/

section Collapse

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] [Nontrivial A]
variable {q : K} {s : A}

/-- **`W_L = W_R` iff `h = 0`**: the L/R distinction of the one-sided vertex exists
exactly off the classical points `q² = 1`. -/
theorem oneSidedL_eq_oneSidedR_iff (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedL q s = oneSidedR q s ↔ q - q⁻¹ = 0 := by
  rw [oneSidedL_eq hq hq2 hs, oneSidedR_eq hq hq2 hs]
  constructor
  · intro h
    have h1 : (q - q⁻¹) • grading q s = 0 := by rw [sub_smul, h, sub_self]
    have h2 : (q - q⁻¹) • (1 : A) = 0 := by
      rw [← grading_sq hq hq2 hs, ← smul_mul_assoc, h1, zero_mul]
    by_contra hne
    exact one_ne_zero ((smul_eq_zero.mp h2).resolve_left hne)
  · intro h
    rw [show q = q⁻¹ from sub_eq_zero.mp h, inv_inv]

end Collapse

/-! ## 3. Two intrinsic line selectors on an ordered field -/

section Ordered

variable {K A : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
  [Ring A] [Algebra K A]
variable {q : K} {s : A}

/-- On a positive parameter, `h > 0` iff `q > 1`. -/
theorem h_pos_iff (hq : 0 < q) : 0 < q - q⁻¹ ↔ 1 < q := by
  rw [sub_pos]
  constructor
  · intro h
    by_contra hle
    push_neg at hle
    have : 1 ≤ q⁻¹ := one_le_inv₀ hq |>.mpr hle
    linarith
  · intro h
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ h
    linarith

/-- The line of the POSITIVE eigenvalue. -/
noncomputable def signLine (q : K) (s : A) : A := if 0 < q then Pp q s else Pm q s

/-- The line of the eigenvalue of modulus `> 1`. -/
noncomputable def modLine (q : K) (s : A) : A := if 1 < |q| then Pp q s else Pm q s

theorem signLine_of_pos (hq : 0 < q) : signLine q s = Pp q s := if_pos hq

theorem modLine_of_one_lt (h : 1 < |q|) : modLine q s = Pp q s := if_pos h

/-- **The sign selector is a function of the letter** (independent of the root label). -/
theorem signLine_neg_inv (hq : q ≠ 0) : signLine (-q⁻¹) s = signLine q s := by
  unfold signLine
  rcases lt_or_gt_of_ne hq with h | h
  · have : 0 < -q⁻¹ := neg_pos.mpr (inv_lt_zero.mpr h)
    rw [if_pos this, if_neg (not_lt.mpr h.le), Pp_neg_inv]
  · have : ¬ 0 < -q⁻¹ := not_lt.mpr (neg_nonpos.mpr (inv_pos.mpr h).le)
    rw [if_neg this, if_pos h, Pm_neg_inv]

/-- **The modulus selector is a function of the letter**, off `|q| = 1`. -/
theorem modLine_neg_inv (hq : q ≠ 0) (h1 : |q| ≠ 1) : modLine (-q⁻¹) s = modLine q s := by
  unfold modLine
  have habs : |(-q⁻¹)| = |q|⁻¹ := by rw [abs_neg, abs_inv]
  have hpos : 0 < |q| := abs_pos.mpr hq
  rcases lt_or_gt_of_ne h1 with h | h
  · have : 1 < |(-q⁻¹)| := by rw [habs]; exact one_lt_inv₀ hpos |>.mpr h
    rw [if_pos this, if_neg (not_lt.mpr h.le), Pp_neg_inv]
  · have : ¬ 1 < |(-q⁻¹)| := by
      rw [habs]; exact not_lt.mpr (inv_lt_one_of_one_lt₀ h).le
    rw [if_neg this, if_pos h, Pm_neg_inv]

/-- **The sign selector is flavour-invariant**: the inverse letter `s⁻¹` (a letter at
`q⁻¹`) has the same positive line. -/
theorem signLine_flip (hq : 0 < q) : signLine q⁻¹ (flip q s) = signLine q s := by
  rw [signLine_of_pos (inv_pos.mpr hq), signLine_of_pos hq, flip_Pp]

/-- **The modulus selector is flavour-covariant**: for `s⁻¹` it is the other line. -/
theorem modLine_flip (h : 1 < |q|) : modLine q⁻¹ (flip q s) = Pm q s := by
  have hq : q ≠ 0 := by rintro rfl; simp at h
  unfold modLine
  have : ¬ 1 < |q⁻¹| := by
    rw [abs_inv]; exact not_lt.mpr (inv_lt_one_of_one_lt₀ h).le
  rw [if_neg this, flip_Pm]

/-- **The two selectors agree on a letter with positive parameter iff `q > 1`**
(given the lines are distinct). -/
theorem modLine_eq_signLine_iff (hq : 0 < q) (hne : Pp q s ≠ Pm q s) :
    modLine q s = signLine q s ↔ 1 < q := by
  rw [signLine_of_pos hq]
  unfold modLine
  rw [abs_of_pos hq]
  by_cases h : 1 < q
  · simp [h]
  · simp only [h, if_false, iff_false]
    exact fun e => hne e.symm

end Ordered

/-! ## 4. Powers of a letter -/

section Powers

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]
variable {q : K} {s : A}

/-- `s^N = q^N P₊ + (−q⁻¹)^N P₋`. -/
theorem pow_eq (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) (N : ℕ) :
    s ^ N = q ^ N • Pp q s + (-q⁻¹) ^ N • Pm q s := by
  induction N with
  | zero => simp [Pp_add_Pm hq2]
  | succ n ih =>
    rw [pow_succ', ih, mul_add, mul_smul_comm, mul_smul_comm, eigen_plus hq hs,
      eigen_minus hq hs, smul_smul, smul_smul, pow_succ', pow_succ']

/-- `q^{−N} s^N = P₊ + (−q⁻²)^N P₋`. -/
theorem normalised_pow_eq (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) (N : ℕ) :
    (q ^ N)⁻¹ • s ^ N = Pp q s + (-(q ^ 2)⁻¹) ^ N • Pm q s := by
  rw [pow_eq hq hq2 hs, smul_add, smul_smul, smul_smul, inv_mul_cancel₀ (pow_ne_zero _ hq),
    one_smul]
  congr 2
  rw [← inv_pow, ← mul_pow]
  congr 1
  field_simp

end Powers

/-! ## 5. Archimedean: the dominant line is the limit of long positive braids -/

section Limit

open Filter Topology

variable {A : Type*} [Ring A] [Algebra ℝ A] [TopologicalSpace A] [IsTopologicalAddGroup A]
  [ContinuousSMul ℝ A]
variable {q : ℝ} {s : A}

theorem ratio_tendsto (h : 1 < |q|) :
    Tendsto (fun N : ℕ => (-(q ^ 2)⁻¹) ^ N) atTop (𝓝 0) := by
  apply tendsto_pow_atTop_nhds_zero_of_abs_lt_one
  rw [abs_neg, abs_inv, abs_pow]
  have : 1 < |q| ^ 2 := one_lt_pow₀ h two_ne_zero
  exact inv_lt_one_of_one_lt₀ this

/-- **For `|q| > 1`, `q^{−N} s^N → P₊`**: the long positive braid projects onto the
`q`-line, which is the dominant (modulus `> 1`) line. -/
theorem tendsto_normalised_pow (h : 1 < |q|) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    Tendsto (fun N : ℕ => (q ^ N)⁻¹ • s ^ N) atTop (𝓝 (Pp q s)) := by
  have hq : q ≠ 0 := by rintro rfl; simp at h
  have e : (fun N : ℕ => (q ^ N)⁻¹ • s ^ N)
      = fun N : ℕ => Pp q s + (-(q ^ 2)⁻¹) ^ N • Pm q s := by
    funext N; exact normalised_pow_eq hq hq2 hs N
  rw [e]
  have := ((ratio_tendsto h).smul_const (Pm q s)).const_add (Pp q s)
  simpa using this

end Limit

end QOU.QuarkState.WeakChiralityRootLabel
