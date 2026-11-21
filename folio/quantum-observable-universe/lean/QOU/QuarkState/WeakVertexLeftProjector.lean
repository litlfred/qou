/-
# D-H3: the weak vertex insertion is proportional to the left projector

Bean `qou-hlx7` (epic `qou-qs0e`). Owner decision D-H3 (2026-11-15, relayed by the
coordinator): record *"the weak vertex is proportional to the left projector"* as an open
conjecture, AND try to derive it. This file is the derivation attempt at the level of one
Hecke letter.

## Inputs (all already in the corpus; nothing new is assumed)

* A letter `σ` at parameter `q` in a `K`-algebra (`s² = h s + 1`, `h = q − q⁻¹`).
* The owner-ruled definition `leftLine q σ` (`LeftLineDefinition.lean`): the eigenline on
  which `σ` acts with eigenvalue of modulus `> 1`. `rightLine` is its complement.
* The corpus vertex `weakVertex q σ` (`LeftLineDefinition.lean`): the one-sided flip that
  acts as `σ⁻¹` on the left line and as `σ` on the right line. By `eq_of_eigen_action`
  (`OneSidedWeakVertex.lean`) these two conditions determine it.

## What this file proves

1. **The vertex insertion is `−h` times the left projector** (`weakVertex_sub_letter`):
   `weakVertex − σ = −(q − q⁻¹)·leftLine`, for every `q` with `q ≠ 0`, `q + q⁻¹ ≠ 0`, in
   both regimes `|q| > 1` and `|q| ≤ 1`. Equivalently
   `weakVertex = σ·rightLine + σ⁻¹·leftLine` (`weakVertex_eq_split`). So the change the
   vertex makes to a free crossing is supported on the left line and vanishes on the right
   line (`insertion_mul_rightLine`, `insertion_mul_leftLine`).
2. **One-sided ⇔ proportional to the left projector** (`one_sided_iff_smul_leftLine`):
   an element `a + bσ` of the letter algebra annihilates the right line iff it is a scalar
   multiple of `leftLine`. So inside one letter, "R does not couple" and "∝ P_L" are the
   same statement; the content of D-H3 is the one-sidedness and the side.
3. **The skein form, label-free** (`skein_dominant_root`): weight the positive crossing by
   its own eigenvalue `t` of modulus `> 1` (either root label, `t = q` or `t = −q⁻¹`).
   Then `t·σ − t⁻¹·σ⁻¹ = (t − t⁻¹)(t + t⁻¹)·leftLine`. This removes the "which crossing
   carries `q` is a convention" caveat of `force-knot-identification` §III: under the
   owner's ruling, the dominant-eigenvalue weighting and the left line are the same choice.
   With `|q| < 1` the `q`-weighting gives the right line instead (`skein_eq_rightLine`).
4. The skein difference and the insertion are the same object up to `−[2]`
   (`skein_eq_neg_bracket_insertion`, `|q| > 1`).

## Scope

* **Derived** (relative to the two ruled definitions above): D-H3 at the level of one
  letter, in the form "vertex insertion = −h·P_L". The proof is short because `leftLine`
  and `weakVertex` already encode the side; the file makes that explicit rather than
  adding a new input.
* **Not derived**: (i) that any corpus object built from several crossings, e.g. the weak
  knot `T(3,5)`, is left-supported. The exact probe
  `computations/probes/weak_knot_left_line_split_probe.py` finds the convention-D trace of
  `(σ₁σ₂)⁵·P₋` equal to `−q²/(q²+1)³ ≠ 0`, so the weak knot as a whole is not. (ii) that
  `weakVertex` is the physical weak coupling; that is a comparison-boundary claim, scope (a).

Base ring (§7c): `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` (the left line needs
an absolute value); generic `[Ring A] [Algebra K A]`. No `ℝ`. No `sorry`, no axiom.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.QuarkState.LeftLineDefinition

namespace QOU.QuarkState.WeakVertexLeftProjector

open QOU.QuarkState.Helicity QOU.QuarkState.OneSidedWeakVertex
  QOU.QuarkState.WeakChiralityRootLabel QOU.QuarkState.LeftLine

variable {K A : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
  [Ring A] [Algebra K A]
variable {q : K} {σ : A}

/-- Every element splits along the two lines. -/
theorem split_lines (hq2 : q + q⁻¹ ≠ 0) (x : A) :
    x = x * leftLine q σ + x * rightLine q σ := by
  rw [← mul_add, leftLine_add_rightLine hq2, mul_one]

/-- The two lines are orthogonal. -/
theorem leftLine_mul_rightLine (hq : q ≠ 0) (hs : IsLetter q σ) :
    leftLine q σ * rightLine q σ = 0 := by
  by_cases h : 1 < |q|
  · rw [leftLine_of_one_lt h, rightLine_of_one_lt h, Pp_mul_Pm hq hs]
  · rw [leftLine_of_not_one_lt h, rightLine_of_not_one_lt h, Pm_mul_Pp hq hs]

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- `σ⁻¹ − σ = −h`. -/
theorem flip_sub_self (q : K) (σ : A) : Helicity.flip q σ - σ = -((q - q⁻¹) • (1 : A)) := by
  unfold Helicity.flip
  abel

/-- **The weak vertex as a split**: `σ⁻¹` on the left line, `σ` on the right line. -/
theorem weakVertex_eq_split (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ) :
    weakVertex q σ = Helicity.flip q σ * leftLine q σ + σ * rightLine q σ := by
  rw [split_lines (σ := σ) hq2 (weakVertex q σ), weakVertex_mul_leftLine hq hq2 hs,
    weakVertex_mul_rightLine hq hq2 hs]

/-- **D-H3, letter level (derived).** The vertex insertion `weakVertex − σ` equals
`−(q − q⁻¹)` times the left projector, in both regimes. -/
theorem weakVertex_sub_letter (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ) :
    weakVertex q σ - σ = -((q - q⁻¹) • leftLine q σ) := by
  have hσ : σ = σ * leftLine q σ + σ * rightLine q σ := split_lines hq2 σ
  conv_lhs => rw [weakVertex_eq_split hq hq2 hs]
  conv_lhs => rhs; rw [hσ]
  rw [add_sub_add_right_eq_sub, ← sub_mul, flip_sub_self, neg_mul, smul_mul_assoc, one_mul]

/-- The insertion annihilates the right line: the right line does not couple. -/
theorem insertion_mul_rightLine (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ) :
    (weakVertex q σ - σ) * rightLine q σ = 0 := by
  rw [weakVertex_sub_letter hq hq2 hs, neg_mul, smul_mul_assoc,
    leftLine_mul_rightLine hq hs, smul_zero, neg_zero]

/-- On the left line the insertion acts by the scalar `−h`. -/
theorem insertion_mul_leftLine (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ)
    (hidem : leftLine q σ * leftLine q σ = leftLine q σ) :
    (weakVertex q σ - σ) * leftLine q σ = -((q - q⁻¹) • leftLine q σ) := by
  rw [weakVertex_sub_letter hq hq2 hs, neg_mul, smul_mul_assoc, hidem]

/-- The left line is idempotent. -/
theorem leftLine_idem (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ) :
    leftLine q σ * leftLine q σ = leftLine q σ := by
  by_cases h : 1 < |q|
  · rw [leftLine_of_one_lt h, Pp_idem hq hq2 hs]
  · rw [leftLine_of_not_one_lt h, Pm_idem hq hq2 hs]

/-- **One-sided ⇔ proportional to the left projector**, inside the letter algebra. -/
theorem one_sided_iff_smul_leftLine (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ)
    (a b : K) :
    (a • (1 : A) + b • σ) * rightLine q σ = 0 ↔
      ∃ c : K, a • (1 : A) + b • σ = c • leftLine q σ := by
  constructor
  · intro h0
    obtain ⟨μ, hμ⟩ := leftLine_eigen_sigma hq hs
    refine ⟨a + b * μ, ?_⟩
    rw [split_lines (σ := σ) hq2 (a • (1 : A) + b • σ), h0, add_zero, add_mul,
      smul_mul_assoc, smul_mul_assoc, one_mul, hμ, smul_smul, add_smul]
  · rintro ⟨c, hc⟩
    rw [hc, smul_mul_assoc, leftLine_mul_rightLine hq hs, smul_zero]

/-- **Skein form, `|q| > 1`.** The `q`-weighted skein difference is `h·[2]·leftLine`. -/
theorem skein_eq_leftLine (hq2 : q + q⁻¹ ≠ 0) (h : 1 < |q|) :
    q • σ - q⁻¹ • Helicity.flip q σ = (q - q⁻¹) • ((q + q⁻¹) • leftLine q σ) := by
  rw [skein_asym_eq hq2, leftLine_of_one_lt h]

/-- **Skein form, `|q| ≤ 1`.** The same weighting then gives the right line. -/
theorem skein_eq_rightLine (hq2 : q + q⁻¹ ≠ 0) (h : ¬ 1 < |q|) :
    q • σ - q⁻¹ • Helicity.flip q σ = (q - q⁻¹) • ((q + q⁻¹) • rightLine q σ) := by
  rw [skein_asym_eq hq2, rightLine_of_not_one_lt h]

/-- **Skein form, label-free.** Weight the positive crossing by its own eigenvalue `t` of
modulus `> 1`, whichever root label (`q` or `−q⁻¹`) that is. The difference is then
`(t − t⁻¹)(t + t⁻¹)·leftLine`. -/
theorem skein_dominant_root (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) {t : K}
    (ht : t = q ∨ t = -q⁻¹) (h1 : 1 < |t|) :
    t • σ - t⁻¹ • Helicity.flip q σ = (t - t⁻¹) • ((t + t⁻¹) • leftLine q σ) := by
  rcases ht with rfl | rfl
  · exact skein_eq_leftLine hq2 h1
  · have ht2 : (-q⁻¹) + (-q⁻¹)⁻¹ ≠ 0 := by
      rw [bracket_neg_inv]; exact neg_ne_zero.mpr hq2
    have hlt : ¬ 1 < |q| := by
      have hpos : 0 < |q| := abs_pos.mpr hq
      rw [abs_neg, abs_inv] at h1
      exact not_lt.mpr ((one_lt_inv₀ hpos).mp h1).le
    rw [← flip_neg_inv (q := q) (s := σ), skein_asym_eq ht2, Pp_neg_inv,
      leftLine_of_not_one_lt hlt]

/-- **The skein difference is the insertion up to `−[2]`** (`|q| > 1`). -/
theorem skein_eq_neg_bracket_insertion (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0)
    (hs : IsLetter q σ) (h : 1 < |q|) :
    q • σ - q⁻¹ • Helicity.flip q σ = -((q + q⁻¹) • (weakVertex q σ - σ)) := by
  rw [skein_eq_leftLine hq2 h, weakVertex_sub_letter hq hq2 hs, smul_neg, neg_neg,
    smul_smul, smul_smul, mul_comm]

/-- The insertion vanishes iff `h = 0`, provided the left line is nonzero. -/
theorem insertion_eq_zero_iff (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ)
    (hL : leftLine q σ ≠ 0) :
    weakVertex q σ - σ = 0 ↔ q - q⁻¹ = 0 := by
  rw [weakVertex_sub_letter hq hq2 hs, neg_eq_zero]
  constructor
  · intro h0
    by_contra hh
    exact hL (by simpa [hh] using congrArg (fun x => (q - q⁻¹)⁻¹ • x) h0)
  · intro hh; rw [hh, zero_smul]

end QOU.QuarkState.WeakVertexLeftProjector
