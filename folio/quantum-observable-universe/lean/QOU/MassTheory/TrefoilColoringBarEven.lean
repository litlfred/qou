/-
# The trefoil (deuteron) boundary-parabolic coloring deviates from flat by an exact bar-even square

**The one-parameter, fully-pinned coloring.** The deuteron `σ₁³` closure is the trefoil
`⟨u,v | uvu = vuv⟩`. Its irreducible `SL₂` representations form a **one-parameter family** in the
meridian eigenvalue `m` (parabolic `m = 1`): with `ρ(u) = [[m,1],[0,m⁻¹]]`,
`ρ(v) = [[m,0],[c,m⁻¹]]`, the braid relation forces the off-diagonal **coloring**

  `c(m) = −(m⁴ − m² + 1)/m²`

(reducible `c = 0` ⟺ `m⁴ − m² + 1 = 0` ⟺ the Alexander-polynomial roots `m² = e^{±iπ/3}`; parabolic
`m = 1 ⟹ c = −1`, the flat/pinched rep). Because the substrate pins the single knob `m ↔ q₀`, the
coloring has **no residual freedom** — the downstream `e₂`/`g₂` is a forward number, not a scan.

This file records the exact algebraic backbone: the coloring's **deviation from the flat value `−1`
is a perfect bar-even square**,

  `c(m) + 1 = −(m − m⁻¹)²`.

`m − m⁻¹` is bar-**odd** (`m ↦ m⁻¹` flips its sign), so `(m − m⁻¹)²` is bar-**even** — the parity of
the `g₂` correction. At the quantum-meridian pin `m = q₀` this is `−(q₀ − q₀⁻¹)² = −h²` (the #4158
bar-even gap `h = q − q⁻¹`); at `m = √q₀` it is `−(v − v⁻¹)²`. This **identifies the bar-even scale**
as `h²` (an exact identity, not a fit); it does **not** derive the coefficient `g₂` — that is the
`e₂` finite part in the pinched limit. §7c: purely algebraic (a field, `m ≠ 0`); base ring generic.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.MassTheory

variable {F : Type*} [Field F]

/-- The trefoil boundary-parabolic **coloring** `c(m) = −(m⁴ − m² + 1)/m²` — the off-diagonal entry of
`ρ(v)` forced by the braid relation `uvu = vuv`, as a function of the meridian eigenvalue `m`. -/
noncomputable def trefoilColoring (m : F) : F := -(m ^ 4 - m ^ 2 + 1) / m ^ 2

/-- **The coloring's deviation from flat is an exact bar-even square:** `c(m) + 1 = −(m − m⁻¹)²`.
Since `m − m⁻¹` is bar-odd (`m ↦ m⁻¹` negates it), the deviation is bar-**even** — the parity of the
`g₂` correction; at `m = q₀` it equals `−(q₀ − q₀⁻¹)² = −h²`. -/
theorem trefoilColoring_add_one (m : F) (hm : m ≠ 0) :
    trefoilColoring m + 1 = -(m - m⁻¹) ^ 2 := by
  unfold trefoilColoring
  field_simp
  ring

/-- **Flat/pinched value.** At the parabolic meridian `m = 1` the coloring is `c = −1` (the flat rep,
`c + 1 = 0`). -/
@[simp] theorem trefoilColoring_one : trefoilColoring (1 : F) = -1 := by
  unfold trefoilColoring; norm_num

/-- **Reducibility locus.** `c(m) = 0` exactly when `m⁴ − m² + 1 = 0` (the Alexander-polynomial roots
`m² = e^{±iπ/3}`) — the boundary between reducible and irreducible representations. -/
theorem trefoilColoring_eq_zero_iff (m : F) (hm : m ≠ 0) :
    trefoilColoring m = 0 ↔ m ^ 4 - m ^ 2 + 1 = 0 := by
  unfold trefoilColoring
  rw [div_eq_zero_iff, neg_eq_zero, pow_eq_zero_iff (two_ne_zero)]
  simp only [hm, or_false]

end QOU.MassTheory
