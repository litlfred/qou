import BraidKnotOctonion.WeightSpaceY3IsHeckeIdempotent

/-!
# The sign and mixed block weights of the convention-D trace on `H₃(q)`

Companion to `HeckeTrivialBlockWeight` (the trivial block, `τ(p₃) = y₃`). Here:

* `b_i = σ_i − q`, with `σ_i b_i = b_i σ_i = −q⁻¹ b_i`, and the antisymmetriser
  `x₋ = b₀b₁b₀ − b₀`, which satisfies `x₋ y = y x₋ = χ₋(y) x₋` for the sign character
  `χ₋ : σ ↦ −q⁻¹`.
* `jimboTrace_antisymm3`: **`τ(x₋) = 0`** for every `q` with `q² + 1 ≠ 0`. So the sign block
  carries weight `y₁₁₁ = 0`, by the Markov property alone (no matrices).
* `p111 = x₋/χ₋(x₋)` is a central idempotent, orthogonal to `p₃`.
* `p21 = 1 − p₃ − p₁₁₁` is a central idempotent (`p21_mul_p21`, `p21_mul`, `mul_p21`) and
  **`τ(p21) = 2q²/(q² + 1)² = 2·y₂₁`** (`jimboTrace_p21_eq_two_y21`), with `y₂₁ = 1/[2]²` the
  weight-space value in `WeightSpaceMarkov`. The factor `2` is the dimension of the `(2,1)` block.

So all three weights `y₃, y₂₁, y₁₁₁` of `WeightSpaceMarkov` are traces of central idempotents
of `H₃(q)` itself. Generic field. No measured value enters.
-/

namespace QOU.IwahoriHecke.HeckeMixedBlockWeight

open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion QOU.SchurWeyl.JimboActionKernel
open QOU.IwahoriHecke.TLKernelRootOfUnity QOU.IwahoriHecke.HeckeTrivialBlockWeight
open QOU.IwahoriHecke.WeightSpaceY3IsHeckeIdempotent

variable {K : Type*} [Field K] (q : K) (hq : q ≠ 0)

local notation "H" => Hecke K q q⁻¹ 2

/-- `b_i = σ_i − q`, the `−q⁻¹`-eigenvector of `σ_i` up to scale. -/
noncomputable def b (i : Fin 2) : H := Hecke.σ K q q⁻¹ 2 i - q • 1

include hq in
theorem b_mul_σ (i : Fin 2) : b q i * Hecke.σ K q q⁻¹ 2 i = (-q⁻¹) • b q i := by
  have h := Hecke.σ_quadratic_qou K q q⁻¹ 2 (mul_inv_cancel₀ hq) i
  rw [b, sub_mul, h, smul_mul_assoc, one_mul]
  match_scalars <;> field_simp <;> ring

include hq in
theorem σ_mul_b (i : Fin 2) : Hecke.σ K q q⁻¹ 2 i * b q i = (-q⁻¹) • b q i := by
  have h := Hecke.σ_quadratic_qou K q q⁻¹ 2 (mul_inv_cancel₀ hq) i
  rw [b, mul_sub, h, mul_smul_comm, mul_one]
  match_scalars <;> field_simp <;> ring

include hq in
theorem b_braid : b q 0 * b q 1 * b q 0 - b q 0 = b q 1 * b q 0 * b q 1 - b q 1 := by
  have hb := Hecke.σ_braid K q q⁻¹ 2 0 (by norm_num)
  have h0 := Hecke.σ_quadratic_qou K q q⁻¹ 2 (mul_inv_cancel₀ hq) 0
  have h1 := Hecke.σ_quadratic_qou K q q⁻¹ 2 (mul_inv_cancel₀ hq) 1
  have hb' : Hecke.σ K q q⁻¹ 2 0 * (Hecke.σ K q q⁻¹ 2 1 * Hecke.σ K q q⁻¹ 2 0)
      = Hecke.σ K q q⁻¹ 2 1 * (Hecke.σ K q q⁻¹ 2 0 * Hecke.σ K q q⁻¹ 2 1) := by
    simpa only [mul_assoc] using hb
  simp only [b, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
    smul_sub, mul_assoc]
  rw [hb', h0, h1]
  match_scalars <;> field_simp <;> ring

/-- `x₋ = b₀b₁b₀ − b₀`, the unnormalised antisymmetriser. -/
noncomputable def antisymm3 : H := b q 0 * b q 1 * b q 0 - b q 0

include hq in
theorem antisymm3_mul_σ (i : Fin 2) :
    antisymm3 q * Hecke.σ K q q⁻¹ 2 i = (-q⁻¹) • antisymm3 q := by
  fin_cases i
  · show (b q 0 * b q 1 * b q 0 - b q 0) * Hecke.σ K q q⁻¹ 2 0 = _
    rw [sub_mul, mul_assoc (b q 0 * b q 1), b_mul_σ q hq, mul_smul_comm, antisymm3, smul_sub]
  · show (b q 0 * b q 1 * b q 0 - b q 0) * Hecke.σ K q q⁻¹ 2 1 = _
    rw [b_braid q hq, sub_mul, mul_assoc (b q 1 * b q 0), b_mul_σ q hq,
      mul_smul_comm, antisymm3, b_braid q hq, smul_sub]

include hq in
theorem σ_mul_antisymm3 (i : Fin 2) :
    Hecke.σ K q q⁻¹ 2 i * antisymm3 q = (-q⁻¹) • antisymm3 q := by
  fin_cases i
  · show Hecke.σ K q q⁻¹ 2 0 * (b q 0 * b q 1 * b q 0 - b q 0) = _
    rw [mul_sub, ← mul_assoc, ← mul_assoc, σ_mul_b q hq, smul_mul_assoc, smul_mul_assoc,
      antisymm3, smul_sub]
  · show Hecke.σ K q q⁻¹ 2 1 * (b q 0 * b q 1 * b q 0 - b q 0) = _
    rw [b_braid q hq, mul_sub, ← mul_assoc, ← mul_assoc, σ_mul_b q hq, smul_mul_assoc,
      smul_mul_assoc, antisymm3, b_braid q hq, smul_sub]

/-- The sign character `σ_i ↦ −q⁻¹`. -/
noncomputable def chiS : H →ₐ[K] K :=
  Hecke.lift K q q⁻¹ 2 (fun _ => -q⁻¹)
    (fun _ => by
      simp only [smul_eq_mul, mul_one]
      field_simp
      ring)
    (fun _ _ => rfl) (fun _ _ _ => mul_comm _ _)

@[simp] theorem chiS_σ (i : Fin 2) : chiS q hq (Hecke.σ K q q⁻¹ 2 i) = -q⁻¹ :=
  Hecke.lift_σ K q q⁻¹ 2 _ _ _ _ i

theorem antisymm3_mul (y : H) : antisymm3 q * y = chiS q hq y • antisymm3 q := by
  have hy : y ∈ Algebra.adjoin K (Set.range (Hecke.σ K q q⁻¹ 2)) := by
    rw [HeckeInclusion.adjoin_range_σ_eq_top]; exact Algebra.mem_top
  induction hy using Algebra.adjoin_induction with
  | mem y hy =>
    obtain ⟨i, rfl⟩ := hy
    rw [chiS_σ, antisymm3_mul_σ q hq]
  | algebraMap r =>
    rw [AlgHom.commutes, Algebra.algebraMap_self, RingHom.id_apply,
      Algebra.algebraMap_eq_smul_one, mul_smul_comm, mul_one]
  | add y z _ _ hy hz => rw [mul_add, hy, hz, map_add, add_smul]
  | mul y z _ _ hy hz => rw [← mul_assoc, hy, smul_mul_assoc, hz, smul_smul, map_mul]

theorem mul_antisymm3 (y : H) : y * antisymm3 q = chiS q hq y • antisymm3 q := by
  have hy : y ∈ Algebra.adjoin K (Set.range (Hecke.σ K q q⁻¹ 2)) := by
    rw [HeckeInclusion.adjoin_range_σ_eq_top]; exact Algebra.mem_top
  induction hy using Algebra.adjoin_induction with
  | mem y hy =>
    obtain ⟨i, rfl⟩ := hy
    rw [chiS_σ, σ_mul_antisymm3 q hq]
  | algebraMap r =>
    rw [AlgHom.commutes, Algebra.algebraMap_self, RingHom.id_apply,
      Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  | add y z _ _ hy hz => rw [add_mul, hy, hz, map_add, add_smul]
  | mul y z _ _ hy hz => rw [mul_assoc, hz, mul_smul_comm, hy, smul_smul, map_mul, mul_comm]

theorem chiS_b (i : Fin 2) : chiS q hq (b q i) = -(q + q⁻¹) := by
  rw [b, map_sub, chiS_σ, map_smul, map_one, smul_eq_mul, mul_one]; ring

/-- `χ₋(x₋) = −[2][3]`, in closed form `−(q² + 1)(q⁴ + q² + 1)/q³`. -/
theorem chiS_antisymm3_eq :
    chiS q hq (antisymm3 q) = -((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / q ^ 3) := by
  rw [antisymm3, map_sub, map_mul, map_mul, chiS_b, chiS_b]
  field_simp
  ring

/-- The trivial character kills `x₋` (`χ(b_i) = 0`). -/
theorem chi_antisymm3 : chi q hq (antisymm3 q) = 0 := by
  have : chi q hq (b q 0) = 0 := by
    rw [b, map_sub, chi_σ, map_smul, map_one, smul_eq_mul, mul_one, sub_self]
  rw [antisymm3, map_sub, map_mul, map_mul, this]; ring

theorem b_zero_eq_incl :
    b q 0 = heckeIncl K q q⁻¹ 1 (Hecke.σ K q q⁻¹ 1 (Fin.last 0) - q • 1) := by
  rw [map_sub, map_smul, map_one, heckeIncl_σ]
  rfl

theorem b_one_eq : b q 1 = Hecke.σ K q q⁻¹ 2 (Fin.last 1) - q • 1 := rfl

include hq in
theorem b_mul_self (i : Fin 2) : b q i * b q i = (-(q + q⁻¹)) • b q i := by
  conv_lhs => rw [show b q i = Hecke.σ K q q⁻¹ 2 i - q • 1 from rfl, mul_sub]
  rw [← b, b_mul_σ q hq, mul_smul_comm, mul_one]
  match_scalars <;> ring

include hq in
/-- **`τ(x₋) = 0`**: the sign block has convention-D weight `0`. -/
theorem jimboTrace_antisymm3 (hq21 : q ^ 2 + 1 ≠ 0) : jimboTrace q hq 2 (antisymm3 q) = 0 := by
  let T := jimboMarkov q hq hq21
  have hT : ∀ n x, jimboTrace q hq n x = T.tr n x := fun _ _ => rfl
  set c : Hecke K q q⁻¹ 1 := Hecke.σ K q q⁻¹ 1 (Fin.last 0) - q • 1 with hc
  set u : K := q ^ 3 / (q ^ 2 + 1) - q with hu
  have hc0 : T.tr 1 c = u := by
    rw [hc, map_sub, map_smul, T.param_eq, T.tr_one, smul_eq_mul, mul_one]
  have hb0 : T.tr 2 (b q 0) = u := by rw [b_zero_eq_incl, ← hc, T.tr_incl, hc0]
  have hb01 : T.tr 2 (b q 0 * b q 1) = u * u := by
    rw [b_zero_eq_incl, ← hc, b_one_eq, mul_sub, map_sub, T.tr_markov, mul_smul_comm, mul_one,
      map_smul, T.tr_incl, hc0, smul_eq_mul, hu]
    ring
  rw [hT, antisymm3, map_sub, T.tr_cyclic, ← mul_assoc, b_mul_self q hq, smul_mul_assoc,
    map_smul, hb01, hb0, smul_eq_mul, hu]
  field_simp
  ring

/-- The central idempotent of the sign block, `p₁₁₁ = x₋/χ₋(x₋)`. -/
noncomputable def p111 : H := (chiS q hq (antisymm3 q))⁻¹ • antisymm3 q

include hq in
theorem chiS_antisymm3_ne_zero (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    chiS q hq (antisymm3 q) ≠ 0 := by
  rw [chiS_antisymm3_eq]
  exact neg_ne_zero.mpr (div_ne_zero (mul_ne_zero hq21 h3) (pow_ne_zero _ hq))

include hq in
theorem p111_mul_p111 (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    p111 q hq * p111 q hq = p111 q hq := by
  have hc := chiS_antisymm3_ne_zero q hq hq21 h3
  rw [p111, smul_mul_smul_comm, antisymm3_mul q hq, smul_smul]
  congr 1
  field_simp

theorem p111_mul (y : H) : p111 q hq * y = chiS q hq y • p111 q hq := by
  rw [p111, smul_mul_assoc, antisymm3_mul q hq, smul_comm]

theorem mul_p111 (y : H) : y * p111 q hq = chiS q hq y • p111 q hq := by
  rw [p111, mul_smul_comm, mul_antisymm3 q hq, smul_comm]

include hq in
theorem jimboTrace_p111 (hq21 : q ^ 2 + 1 ≠ 0) : jimboTrace q hq 2 (p111 q hq) = 0 := by
  rw [p111, map_smul, jimboTrace_antisymm3 q hq hq21, smul_zero]

/-- `p₃ p₁₁₁ = 0`. -/
theorem p3_mul_p111 : p3 q hq * p111 q hq = 0 := by
  rw [p3_mul, p111, map_smul, chi_antisymm3, smul_zero, zero_smul]

theorem p111_mul_p3 : p111 q hq * p3 q hq = 0 := by
  rw [mul_p3, p111, map_smul, chi_antisymm3, smul_zero, zero_smul]

/-- The central idempotent of the mixed `(2,1)` block. -/
noncomputable def p21 : H := 1 - p3 q hq - p111 q hq

theorem p21_mul (y : H) : p21 q hq * y = y * p21 q hq := by
  rw [p21, sub_mul, sub_mul, mul_sub, mul_sub, one_mul, mul_one, p3_mul, mul_p3, p111_mul,
    mul_p111]

include hq in
theorem p21_mul_p21 (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    p21 q hq * p21 q hq = p21 q hq := by
  have e3 := p3_mul_p3 q hq hq21 h3
  have e1 := p111_mul_p111 q hq hq21 h3
  have e31 := p3_mul_p111 q hq
  have e13 := p111_mul_p3 q hq
  simp only [p21, sub_mul, mul_sub, one_mul, mul_one, e3, e1, e31, e13]
  abel

include hq in
/-- **`τ(p₂₁) = 2q²/(q² + 1)²`.** -/
theorem jimboTrace_p21 (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    jimboTrace q hq 2 (p21 q hq) = 2 * q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  let T := jimboMarkov q hq hq21
  have h1 : jimboTrace q hq 2 1 = 1 := T.tr_one 2
  rw [p21, map_sub, map_sub, h1, jimboTrace_p3 q hq hq21 h3, jimboTrace_p111 q hq hq21]
  field_simp
  ring

include hq in
/-- **`τ(p₂₁) = 2·y₂₁`**: the weight-space `y₂₁ = 1/[2]²` times the block dimension `2`. -/
theorem jimboTrace_p21_eq_two_y21 (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    jimboTrace q hq 2 (p21 q hq) = 2 * QOU.QBeta.WeightSpaceMarkov.y21 q := by
  rw [jimboTrace_p21 q hq hq21 h3, QOU.QBeta.WeightSpaceMarkov.y21]
  have e : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [e]
  field_simp

end QOU.IwahoriHecke.HeckeMixedBlockWeight
