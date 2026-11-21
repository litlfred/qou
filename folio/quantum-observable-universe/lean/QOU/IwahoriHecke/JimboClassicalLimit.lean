import QOU.IwahoriHecke.TensorEmbeddingGL

/-!
# QOU.IwahoriHecke.JimboClassicalLimit — a classical colour Lie action meets the tower only at `q = 1`

Bean `qou-cb3r` (parent `qou-8lxd`). Audit:
`docs/audits/2026-11-15-colour-stabilizer-bridge.md`.

The octonion colour stabilizer `su3 e` is a classical Lie algebra (the corpus's octonions carry no
`q`). A Lie algebra acts on `V ⊗ V` through the **primitive** coproduct `Δx = x ⊗ 1 + 1 ⊗ x`.
The tower's colour channel is the `gl₃` Jimbo action, whose crossing is `rCheckN q qi`.

`primitive_commute_rCheckN_iff`: at `d = 3`, the primitive coproduct of the matrix unit `E₀₁`
(a root vector of `sl₃`) commutes with Jimbo's `Ř` **iff `q = 1` and `qi = 1`**. So no Lie-algebra
action, `su3 e` or any other, commutes with the tower's crossing away from the classical point. A
bridge to the tower at `q₀ ≠ 1` cannot be a Lie action through the primitive coproduct; it lives
either at `q = 1` (the classical limit) or through a deformed coproduct (`U_q`), which the octonion
side does not carry.

The four nonzero entries of `[Ř, Δ E₀₁]` are `qi − 1`, `q − 1`, `1 − qi`, `1 − q`, found by
expanding `Ř` affinely in `(q, qi)` and checked in exact integer arithmetic before being stated.

Base ring: generic `CommRing R` (§7c).

LaTeX label: `prop:jimbo-classical-limit`
-/

namespace QOU.IwahoriHecke.JimboClassicalLimit

open QOU.IwahoriHecke.TensorEmbedGL Matrix

variable {R : Type*} [CommRing R]

/-- The primitive coproduct `x ⊗ 1 + 1 ⊗ x` of a `d × d` matrix, as a matrix on `V ⊗ V`. -/
def primDelta {d : ℕ} (x : Matrix (Fin d) (Fin d) R) : Matrix (Fin d × Fin d) (Fin d × Fin d) R :=
  Matrix.of fun a b => (if a.2 = b.2 then x a.1 b.1 else 0) + (if a.1 = b.1 then x a.2 b.2 else 0)

/-- The `sl₃` root vector `E₀₁`. -/
def e01 : Matrix (Fin 3) (Fin 3) R := Matrix.of fun i j => if i = 0 ∧ j = 1 then 1 else 0

/-- The `((0,0),(1,0))` entry of the commutator is `q − 1`. -/
theorem comm_entry_q (q qi : R) :
    (rCheckN q qi * primDelta (e01 : Matrix (Fin 3) (Fin 3) R)
      - primDelta e01 * rCheckN q qi : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R)
      (0, 0) (1, 0) = q - 1 := by
  simp [Matrix.mul_apply, Matrix.sub_apply, Fintype.sum_prod_type, Fin.sum_univ_three,
    primDelta, e01, rCheckN_apply, Prod.ext_iff]

/-- The `((0,0),(0,1))` entry of the commutator is `qi − 1`. -/
theorem comm_entry_qi (q qi : R) :
    (rCheckN q qi * primDelta (e01 : Matrix (Fin 3) (Fin 3) R)
      - primDelta e01 * rCheckN q qi : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R)
      (0, 0) (0, 1) = qi - 1 := by
  simp [Matrix.mul_apply, Matrix.sub_apply, Fintype.sum_prod_type, Fin.sum_univ_three,
    primDelta, e01, rCheckN_apply, Prod.ext_iff]
  ring

/-- At `q = qi = 1`, Jimbo's `Ř` is the flip `a ↦ a.swap` (proof infrastructure). -/
private def swapM (d : ℕ) : Matrix (Fin d × Fin d) (Fin d × Fin d) R :=
  Matrix.of fun a b => if a = b.swap then 1 else 0

private theorem rCheckN_one_one {d : ℕ} : rCheckN (d := d) (1 : R) 1 = swapM d := by
  ext ⟨a1, a2⟩ ⟨b1, b2⟩
  simp only [rCheckN_apply, swapM, Matrix.of_apply, Prod.swap_prod_mk, Prod.mk.injEq, sub_self]
  split_ifs <;> simp_all

private theorem swapM_mul {d : ℕ} (M : Matrix (Fin d × Fin d) (Fin d × Fin d) R)
    (a b : Fin d × Fin d) :
    (swapM d * M : Matrix (Fin d × Fin d) (Fin d × Fin d) R) a b = M a.swap b := by
  have hx : ∀ x : Fin d × Fin d, (a = x.swap) ↔ (x = a.swap) := fun x =>
    ⟨fun h => by subst h; simp, fun h => by subst h; simp⟩
  rw [Matrix.mul_apply]
  simp [swapM, hx]

private theorem mul_swapM {d : ℕ} (M : Matrix (Fin d × Fin d) (Fin d × Fin d) R)
    (a b : Fin d × Fin d) :
    (M * swapM d : Matrix (Fin d × Fin d) (Fin d × Fin d) R) a b = M a b.swap := by
  rw [Matrix.mul_apply]
  simp [swapM]

/-- **A classical `sl₃` root vector commutes with Jimbo's `Ř` only at `q = qi = 1`.** -/
theorem primitive_commute_rCheckN_iff (q qi : R) :
    rCheckN q qi * primDelta (e01 : Matrix (Fin 3) (Fin 3) R)
      = primDelta e01 * rCheckN q qi ↔ q = 1 ∧ qi = 1 := by
  constructor
  · intro h
    have hz := sub_eq_zero.mpr h
    have h1 := comm_entry_q q qi
    have h2 := comm_entry_qi q qi
    rw [hz] at h1 h2
    exact ⟨(sub_eq_zero.mp (by simpa using h1.symm)), (sub_eq_zero.mp (by simpa using h2.symm))⟩
  · rintro ⟨rfl, rfl⟩
    rw [rCheckN_one_one (R := R)]
    ext ⟨a1, a2⟩ ⟨b1, b2⟩
    rw [swapM_mul, mul_swapM]
    simp only [primDelta, Matrix.of_apply, Prod.swap_prod_mk]
    rw [add_comm]

end QOU.IwahoriHecke.JimboClassicalLimit
