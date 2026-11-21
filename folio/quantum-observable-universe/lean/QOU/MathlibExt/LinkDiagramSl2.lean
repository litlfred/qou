import QOU.MathlibExt.LinkDiagramStateSum
import Mathlib.Tactic.FieldSimp

/-!
# The quantum `sl₂` state-sum model on link diagram codes

The labels are `Bool` (`false` and `true` are the two weight vectors of the fundamental
representation). The braiding `Ř` on `V ⊗ V`, with `h = q − q⁻¹`, is

    Ř (v₀ ⊗ v₀) = q v₀ ⊗ v₀,        Ř (v₀ ⊗ v₁) = v₁ ⊗ v₀,
    Ř (v₁ ⊗ v₀) = v₀ ⊗ v₁ + h v₁ ⊗ v₀,   Ř (v₁ ⊗ v₁) = q v₁ ⊗ v₁,

and the turn weight is `K = diag(q, q⁻¹)`. A positive crossing reads `Ř` from the incoming labels
`(oin, uin)` to the outgoing labels `(uout, oout)`, a negative crossing reads `Ř⁻¹` from
`(uin, oin)` to `(oout, uout)`.

`sl2Model_invariant` proves the four local identities of `Model.Invariant` with framing factor
`θ = q²`, so by `normValue_eq` the writhe-normalised value of this model is an invariant of
`ReidemeisterEquiv`. A circle with one turn has value `q + q⁻¹` (`sl2Model_value_circle`).
Identifying the invariant with the Jones polynomial needs the value of a braid closure, which is
not done here.

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VIII (the R-matrix of `V ⊗ V`) and Ch. XIV
-- Ref: [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links", Invent. Math. 92
-/

namespace QOU.MathlibExt.PL.Diagram

variable {𝕜 : Type*} [Field 𝕜]

/-- The braiding `Ř`: `sl2R q c d a b` is the coefficient of `v_c ⊗ v_d` in `Ř (v_a ⊗ v_b)`. -/
def sl2R (q : 𝕜) : Bool → Bool → Bool → Bool → 𝕜
  | false, false, false, false => q
  | true, false, false, true => 1
  | false, true, true, false => 1
  | true, false, true, false => q - q⁻¹
  | true, true, true, true => q
  | _, _, _, _ => 0

/-- The inverse braiding `Ř⁻¹ = Ř − (q − q⁻¹)`, with the same index convention. -/
def sl2Rinv (q : 𝕜) : Bool → Bool → Bool → Bool → 𝕜
  | false, false, false, false => q⁻¹
  | true, false, false, true => 1
  | false, true, false, true => -(q - q⁻¹)
  | false, true, true, false => 1
  | true, true, true, true => q⁻¹
  | _, _, _, _ => 0

/-- **The quantum `sl₂` model** at a nonzero `q`. -/
def sl2Model (q : 𝕜) (hq : q ≠ 0) : Model 𝕜 Bool where
  X s uin uout oin oout := if s then sl2R q uout oout oin uin else sl2Rinv q oout uout uin oin
  K i := if i then (Units.mk0 q hq)⁻¹ else Units.mk0 q hq
  base := false

variable (q : 𝕜) (hq : q ≠ 0)

theorem sl2Model_r1 (u s : Bool) (x y : Bool) :
    ∑ i, kinkW (sl2Model q hq) u s x y i * (((sl2Model q hq).K i ^ kinkTurn u s : 𝕜ˣ) : 𝕜) =
      ((Units.mk0 q hq ^ 2) ^ signZ s : 𝕜ˣ) * if x = y then 1 else 0 := by
  simp only [Fintype.sum_bool]
  cases u <;> cases s <;> cases x <;> cases y <;>
    simp [kinkW, sl2Model, sl2R, sl2Rinv, kinkTurn, signZ] <;> field_simp <;> ring

set_option maxHeartbeats 1000000 in
theorem sl2Model_r2par (s a b c d : Bool) :
    ∑ i, ∑ j, (sl2Model q hq).X s c j a i * (sl2Model q hq).X (!s) j d i b =
      if a = b ∧ c = d then 1 else 0 := by
  simp only [Fintype.sum_bool]
  cases s <;> cases a <;> cases b <;> cases c <;> cases d <;>
    simp [sl2Model, sl2R, sl2Rinv] <;> field_simp

set_option maxHeartbeats 1000000 in
theorem sl2Model_r2anti (s a b c d : Bool) :
    ∑ i, ∑ k, (sl2Model q hq).X s k d a i * (((sl2Model q hq).K i ^ bigonTurn s : 𝕜ˣ) : 𝕜) *
      (sl2Model q hq).X (!s) c k i b =
      if a = b ∧ c = d then (((sl2Model q hq).K a ^ bigonTurn s : 𝕜ˣ) : 𝕜) else 0 := by
  simp only [Fintype.sum_bool]
  cases s <;> cases a <;> cases b <;> cases c <;> cases d <;>
    simp [sl2Model, sl2R, sl2Rinv, bigonTurn] <;> field_simp <;> ring

set_option maxHeartbeats 1000000 in
theorem sl2Model_r3 (a₀ a₂ b₀ b₂ c₀ c₂ : Bool) :
    ∑ i, ∑ j, ∑ k, (sl2Model q hq).X true b₀ j a₀ i * (sl2Model q hq).X true c₀ k i a₂ *
      (sl2Model q hq).X true k c₂ j b₂ =
    ∑ i, ∑ j, ∑ k, (sl2Model q hq).X true c₀ k b₀ j * (sl2Model q hq).X true k c₂ a₀ i *
      (sl2Model q hq).X true j b₂ i a₂ := by
  simp only [Fintype.sum_bool]
  cases a₀ <;> cases a₂ <;> cases b₀ <;> cases b₂ <;> cases c₀ <;> cases c₂ <;>
    simp [sl2Model, sl2R] <;> field_simp <;> ring

theorem sl2Model_slide (s : Bool) (t : ℤ) (a b c d : Bool) :
    (((sl2Model q hq).K a ^ t * (sl2Model q hq).K c ^ t : 𝕜ˣ) : 𝕜) * (sl2Model q hq).X s a b c d =
      (sl2Model q hq).X s a b c d * (((sl2Model q hq).K b ^ t * (sl2Model q hq).K d ^ t : 𝕜ˣ) : 𝕜) := by
  cases s <;> cases a <;> cases b <;> cases c <;> cases d <;>
    simp [sl2Model, sl2R, sl2Rinv] <;> ring

/-- **The quantum `sl₂` model satisfies the local identities**, with framing factor `q²`. -/
theorem sl2Model_invariant : (sl2Model q hq).Invariant (Units.mk0 q hq ^ 2) where
  r1 := sl2Model_r1 q hq
  r2par := sl2Model_r2par q hq
  r2anti := sl2Model_r2anti q hq
  r3 := sl2Model_r3 q hq
  slide := sl2Model_slide q hq

/-- **A circle with one full turn has value `q + q⁻¹`**, the quantum dimension of `V`. Without the
turn the same circle has value `2`; this is why codes carry turn numbers. -/
theorem sl2Model_value_circle :
    value (sl2Model q hq) (Code.ofJs {((), (), 1)} : Code Unit) = q + q⁻¹ := by
  classical
  rw [value, ← (Equiv.funUnique Unit Bool).symm.sum_comp, Fintype.sum_bool]
  simp [weight, xw, jw, uf, Code.Occurs, Code.ofJs, sl2Model, add_comm]

end QOU.MathlibExt.PL.Diagram
