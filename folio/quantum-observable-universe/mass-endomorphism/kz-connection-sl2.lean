import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Logic.Equiv.Basic
import Mathlib.Tactic.Abel
import Mathlib.GroupTheory.Perm.Fin

/-!
# The `𝔰𝔩₂` Knizhnik–Zamolodchikov connection and its flatness

Content block `def:kz-connection-sl2`.

**The connection.** On the configuration space of `n` distinct points
`z₁, …, zₙ ∈ ℂ` with fibre `V^{⊗n}`, `V = ℂ²`, the KZ connection is
`∇ = d − λ ω`, `ω = Σ_{i<j} Ω_{ij} dlog(z_i − z_j)`, where `Ω_{ij}` is the split
Casimir `e ⊗ f + f ⊗ e + ½ h ⊗ h` acting in tensor slots `i, j`.

**Why the residues live in the symmetric-group algebra.** On `ℂ² ⊗ ℂ²` the split
Casimir is `Ω = P − ½`, with `P` the flip of the two factors: it is `½` on the
triplet (where `P = 1`) and `−3/2` on the singlet (where `P = −1`); see
`QOU.Mass.KohnoTwoPoint.casimir_eq_flip`. So in slots `i, j` of `V^{⊗n}`,
`Ω_{ij} = s_{ij} − ½`, with `s_{ij}` the transposition of those two tensor factors.
The residues are therefore images of the elements `(i j) − ½` of the group algebra
`R[S_n]`, and we state everything there (`kzResidue`), over any commutative ring
in which `2` is invertible (§7c: no `ℝ`, no `ℂ` needed).

**Flatness, as a statement that can fail.** For a logarithmic connection
`ω = Σ M_{ij} dlog(z_i − z_j)`, flatness `dω − ω ∧ ω = 0` reduces, by `dω = 0` and the
Arnold relation among the forms `dlog(z_i − z_j)`, to the *infinitesimal pure braid
relations* (Kohno 1987, §1.1; Drinfeld 1991, §2):

* `[M_{ij}, M_{kl}] = 0` when `{i, j} ∩ {k, l} = ∅`,
* `[M_{ij}, M_{ik} + M_{jk}] = 0` when `i, j, k` are distinct.

`IsFlatLogConnection` is that predicate on an arbitrary family of residues. The
reduction from `dω − ω∧ω = 0` to these relations is the cited step, not formalised
here. `kz_isFlat` proves the predicate for the KZ residues, and
`not_isFlat_example` exhibits a family of residues for which it is false, so the
predicate has content (contrast `QOU.QFlatConnection`, which is `trivial`).
-/

namespace QOU.Mass.KZConnectionSl2

open Equiv

variable {R : Type*} [CommRing R] {n : ℕ}

/-- The symmetric-group algebra `R[S_n]`. -/
abbrev SymAlg (R : Type*) [CommRing R] (n : ℕ) := MonoidAlgebra R (Perm (Fin n))

/-- The KZ residue in slots `i, j`: the split Casimir `Ω_{ij} = s_{ij} − ½`. Here `half`
is meant to be `2⁻¹`; nothing below uses that, since the scalar part is central and
drops out of every commutator. -/
noncomputable def kzResidue (half : R) (i j : Fin n) : SymAlg R n :=
  MonoidAlgebra.of R (Perm (Fin n)) (swap i j) - algebraMap R (SymAlg R n) half

/-- **Flatness of a logarithmic connection** with residues `M`: the infinitesimal
pure braid relations. -/
def IsFlatLogConnection {A : Type*} [Ring A] (M : Fin n → Fin n → A) : Prop :=
  (∀ i j k l : Fin n, i ≠ k → i ≠ l → j ≠ k → j ≠ l →
      M i j * M k l = M k l * M i j) ∧
  (∀ i j k : Fin n, i ≠ j → i ≠ k → j ≠ k →
      M i j * (M i k + M j k) = (M i k + M j k) * M i j)

lemma swap_conj_left {i j k : Fin n} (_hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) :
    swap i j * swap i k = swap j k * swap i j := by
  have h := swap_apply_apply (swap i j) i k
  rw [swap_apply_left, swap_apply_of_ne_of_ne hik.symm hjk.symm] at h
  rw [h, swap_inv, mul_assoc, mul_assoc, swap_mul_self, mul_one]

lemma swap_conj_right {i j k : Fin n} (_hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) :
    swap i j * swap j k = swap i k * swap i j := by
  have h := swap_apply_apply (swap i j) j k
  rw [swap_apply_right, swap_apply_of_ne_of_ne hik.symm hjk.symm] at h
  rw [h, swap_inv, mul_assoc, mul_assoc, swap_mul_self, mul_one]

lemma swap_commute_disjoint {i j k l : Fin n} (hik : i ≠ k) (hil : i ≠ l) (hjk : j ≠ k)
    (hjl : j ≠ l) : swap i j * swap k l = swap k l * swap i j := by
  have h := swap_apply_apply (swap i j) k l
  rw [swap_apply_of_ne_of_ne hik.symm hjk.symm, swap_apply_of_ne_of_ne hil.symm hjl.symm] at h
  conv_rhs => rw [h]
  rw [swap_inv, mul_assoc, mul_assoc, swap_mul_self, mul_one]

/-- Subtracting central scalars does not change whether two elements commute. -/
lemma commute_sub_scalar {X Y : SymAlg R n} (h : X * Y = Y * X) (a b : R) :
    (X - algebraMap R _ a) * (Y - algebraMap R _ b) =
      (Y - algebraMap R _ b) * (X - algebraMap R _ a) := by
  have ha : ∀ Z : SymAlg R n, algebraMap R _ a * Z = Z * algebraMap R _ a :=
    fun Z => Algebra.commutes a Z
  have hb : ∀ Z : SymAlg R n, algebraMap R _ b * Z = Z * algebraMap R _ b :=
    fun Z => Algebra.commutes b Z
  simp only [sub_mul, mul_sub, h, ha Y, hb X, ← map_mul, mul_comm a b]
  abel

local notation "σ" => MonoidAlgebra.of R (Perm (Fin n))

/-- **The `𝔰𝔩₂` KZ connection is flat**: its residues satisfy the infinitesimal pure
braid relations. -/
theorem kz_isFlat (half : R) : IsFlatLogConnection (kzResidue (R := R) (n := n) half) := by
  refine ⟨fun i j k l hik hil hjk hjl => ?_, fun i j k hij hik hjk => ?_⟩
  · apply commute_sub_scalar
    rw [← map_mul, ← map_mul, swap_commute_disjoint hik hil hjk hjl]
  · have hsum : kzResidue half i k + kzResidue half j k =
        (σ (swap i k) + σ (swap j k)) - algebraMap R (SymAlg R n) (half + half) := by
      simp only [kzResidue, map_add]; abel
    rw [hsum]
    apply commute_sub_scalar
    rw [mul_add, add_mul, ← map_mul, ← map_mul, ← map_mul, ← map_mul,
      swap_conj_left hij hik hjk, swap_conj_right hij hik hjk, add_comm]

/-- **The predicate has content**: a family of residues on three points that is not
flat. Take `M₀₁ = s₀₁`, `M₀₂ = s₁₂` and every other residue `0`; then
`M₀₁ (M₀₂ + M₁₂) = s₀₁ s₁₂ ≠ s₁₂ s₀₁ = (M₀₂ + M₁₂) M₀₁`. -/
theorem not_isFlat_example [Nontrivial R] :
    ¬ IsFlatLogConnection (fun i j : Fin 3 =>
      if i = 0 ∧ j = 1 then MonoidAlgebra.of R (Perm (Fin 3)) (swap 0 1)
      else if i = 0 ∧ j = 2 then MonoidAlgebra.of R (Perm (Fin 3)) (swap 1 2)
      else 0) := by
  intro h
  have h2 := h.2 0 1 2 (by decide) (by decide) (by decide)
  simp only [Fin.isValue, and_true, Fin.reduceEq, and_false, if_true,
    if_false, add_zero] at h2
  rw [← map_mul, ← map_mul] at h2
  exact absurd (MonoidAlgebra.of_injective h2) (by decide)

end QOU.Mass.KZConnectionSl2
