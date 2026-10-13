import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Logic.Equiv.Basic
import Mathlib.Tactic.Abel
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Tactic.Module
import Mathlib.Tactic.FieldSimp
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Mul

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

`IsFlatLogConnection` is that predicate on an arbitrary family of residues. For three
points the reduction is proved below, in both directions: the relations give
`ω∧ω = 0` pointwise (`curvature_zero_of_isFlat`, via the Arnold relation `arnold`), and
`ω∧ω = 0` everywhere gives the relations back (`relations_of_curvature_zero`); each
`d log(z_i − z_j)` is closed (`omegaAt_hasDerivAt`, `omegaAt_closed`). For `n > 3` the
same argument runs triple by triple plus disjoint pairs; that general-`n` bookkeeping is
not formalised. `kz_isFlat` proves the predicate for the KZ residues, and
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


/-! ## From the relations to vanishing curvature (three points)

Here the reduction that the module docstring calls "cited" is proved for `n = 3`.
At a configuration `z` with distinct coordinates, the form `ω_{ij} = d log(z_i − z_j)`
evaluated on a tangent vector `u` is `(u_i − u_j)/(z_i − z_j)` (`omegaAt`).

* `omegaAt_closed`: `ω_{ij}` is closed. Its derivative along `u`, applied to `v`, is
  `−(u_i − u_j)(v_i − v_j)/(z_i − z_j)²`, which is symmetric in `u, v`, so
  `dω_{ij}(u, v) = 0`.
* `arnold`: the Arnold relation
  `ω_{01}∧ω_{12} + ω_{12}∧ω_{20} + ω_{20}∧ω_{01} = 0`, pointwise.
* `curvature_zero_of_isFlat`: for `ω = Σ M_p ω_p` with `M` symmetric and satisfying the
  infinitesimal pure braid relations, `(ω∧ω)(u, v) = ω(u)ω(v) − ω(v)ω(u) = 0` at every
  point and for all `u, v`. With `dω = 0` this is `dω − ω∧ω = 0`: the connection is flat.
* `isFlat_of_curvature_zero`: the converse, so the relations are exactly flatness.
-/

section Curvature

variable {k : Type*} [Field k]

/-- `d log(z_i − z_j)` at the point `z`, evaluated on the tangent vector `u`. -/
def omegaAt (z u : Fin 3 → k) (i j : Fin 3) : k := (u i - u j) / (z i - z j)

/-- The wedge of two scalar 1-forms, evaluated on `(u, v)`. -/
def wedge (a b : (Fin 3 → k) → k) (u v : Fin 3 → k) : k := a u * b v - a v * b u

lemma omegaAt_symm (z u : Fin 3 → k) (i j : Fin 3) : omegaAt z u j i = omegaAt z u i j := by
  unfold omegaAt; rw [← neg_sub (u i), ← neg_sub (z i), neg_div_neg_eq]

/-- **Arnold relation**, pointwise, at a configuration with distinct coordinates. -/
theorem arnold (z : Fin 3 → k) (h01 : z 0 ≠ z 1) (h02 : z 0 ≠ z 2) (h12 : z 1 ≠ z 2)
    (u v : Fin 3 → k) :
    wedge (fun w => omegaAt z w 0 1) (fun w => omegaAt z w 1 2) u v +
      wedge (fun w => omegaAt z w 1 2) (fun w => omegaAt z w 2 0) u v +
      wedge (fun w => omegaAt z w 2 0) (fun w => omegaAt z w 0 1) u v = 0 := by
  have a : z 0 - z 1 ≠ 0 := sub_ne_zero.2 h01
  have b : z 1 - z 2 ≠ 0 := sub_ne_zero.2 h12
  have c : z 2 - z 0 ≠ 0 := sub_ne_zero.2 (Ne.symm h02)
  unfold wedge omegaAt
  field_simp
  ring

variable {A : Type*} [Ring A] [Algebra k A]

/-- The connection form `ω = M₀₁ ω₀₁ + M₀₂ ω₀₂ + M₁₂ ω₁₂` on the tangent vector `u`. -/
def connForm (M : Fin 3 → Fin 3 → A) (z u : Fin 3 → k) : A :=
  omegaAt z u 0 1 • M 0 1 + omegaAt z u 0 2 • M 0 2 + omegaAt z u 1 2 • M 1 2

/-- The quadratic part of the curvature, `(ω ∧ ω)(u, v)`. -/
def omegaWedgeOmega (M : Fin 3 → Fin 3 → A) (z u v : Fin 3 → k) : A :=
  connForm M z u * connForm M z v - connForm M z v * connForm M z u

/-- Expanding `ω∧ω` and using two of the braid relations leaves one commutator times
the left side of the Arnold relation. -/
lemma omegaWedgeOmega_eq (M : Fin 3 → Fin 3 → A) (z u v : Fin 3 → k)
    (hX : M 0 1 * (M 0 2 + M 1 2) = (M 0 2 + M 1 2) * M 0 1)
    (hY : M 0 2 * (M 0 1 + M 1 2) = (M 0 1 + M 1 2) * M 0 2) :
    omegaWedgeOmega M z u v =
      (omegaAt z u 0 1 * omegaAt z v 0 2 - omegaAt z v 0 1 * omegaAt z u 0 2
        - (omegaAt z u 0 1 * omegaAt z v 1 2 - omegaAt z v 0 1 * omegaAt z u 1 2)
        + (omegaAt z u 0 2 * omegaAt z v 1 2 - omegaAt z v 0 2 * omegaAt z u 1 2)) •
      (M 0 1 * M 0 2 - M 0 2 * M 0 1) := by
  have hZX : M 1 2 * M 0 1 = M 0 1 * M 0 2 + M 0 1 * M 1 2 - M 0 2 * M 0 1 := by
    rw [mul_add, add_mul] at hX; rw [eq_sub_iff_add_eq, hX]; abel
  have hZY : M 1 2 * M 0 2 = M 0 2 * M 0 1 + M 0 2 * M 1 2 - M 0 1 * M 0 2 := by
    rw [mul_add, add_mul] at hY; rw [eq_sub_iff_add_eq, hY]; abel
  unfold omegaWedgeOmega connForm
  simp only [add_mul, mul_add, smul_mul_smul_comm, hZX, hZY]
  module

/-- **The relations force zero curvature.** For symmetric residues satisfying the
infinitesimal pure braid relations, `(ω ∧ ω)(u, v) = 0` at every configuration with
distinct coordinates, for all tangent vectors `u, v`. -/
theorem curvature_zero_of_isFlat (M : Fin 3 → Fin 3 → A) (hsym : ∀ i j, M i j = M j i)
    (hM : IsFlatLogConnection M) (z : Fin 3 → k) (h01 : z 0 ≠ z 1) (h02 : z 0 ≠ z 2)
    (h12 : z 1 ≠ z 2) (u v : Fin 3 → k) : omegaWedgeOmega M z u v = 0 := by
  have hX := hM.2 0 1 2 (by decide) (by decide) (by decide)
  have hY := hM.2 0 2 1 (by decide) (by decide) (by decide)
  rw [hsym 2 1] at hY
  rw [omegaWedgeOmega_eq M z u v hX hY]
  have hA := arnold z h01 h02 h12 u v
  unfold wedge at hA
  simp only [omegaAt_symm z u 0 2, omegaAt_symm z v 0 2] at hA
  have : omegaAt z u 0 1 * omegaAt z v 0 2 - omegaAt z v 0 1 * omegaAt z u 0 2
        - (omegaAt z u 0 1 * omegaAt z v 1 2 - omegaAt z v 0 1 * omegaAt z u 1 2)
        + (omegaAt z u 0 2 * omegaAt z v 1 2 - omegaAt z v 0 2 * omegaAt z u 1 2) = 0 := by
    linear_combination -hA
  rw [this, zero_smul]

/-- `ω∧ω` with no relations assumed: the three commutators, each weighted by a
wedge of two of the scalar forms. -/
lemma omegaWedgeOmega_expand (M : Fin 3 → Fin 3 → A) (z u v : Fin 3 → k) :
    omegaWedgeOmega M z u v =
      (omegaAt z u 0 1 * omegaAt z v 0 2 - omegaAt z v 0 1 * omegaAt z u 0 2) •
        (M 0 1 * M 0 2 - M 0 2 * M 0 1) +
      (omegaAt z u 0 1 * omegaAt z v 1 2 - omegaAt z v 0 1 * omegaAt z u 1 2) •
        (M 0 1 * M 1 2 - M 1 2 * M 0 1) +
      (omegaAt z u 0 2 * omegaAt z v 1 2 - omegaAt z v 0 2 * omegaAt z u 1 2) •
        (M 0 2 * M 1 2 - M 1 2 * M 0 2) := by
  unfold omegaWedgeOmega connForm
  simp only [add_mul, mul_add, smul_mul_smul_comm]
  module

/-- **Converse: zero curvature forces the relations.** Pointwise the 2-forms on three
points span a line (translations act trivially), so one configuration gives one equation.
Two configurations, `z = (0, 1, 2)` and `z = (0, 1, 3)` with `u = e₀`, `v = e₁`, give
`½C₁ + C₂ + ½C₃ = 0` and `⅓C₁ + ½C₂ + ⅙C₃ = 0` for the commutators
`C₁ = [M₀₁, M₀₂]`, `C₂ = [M₀₁, M₁₂]`, `C₃ = [M₀₂, M₁₂]`, hence `C₁ + C₂ = 0` and
`C₂ + C₃ = 0`: the three infinitesimal pure braid relations. -/
theorem relations_of_curvature_zero [CharZero k] (M : Fin 3 → Fin 3 → A)
    (hF : ∀ z u v : Fin 3 → k, z 0 ≠ z 1 → z 0 ≠ z 2 → z 1 ≠ z 2 →
      omegaWedgeOmega M z u v = 0) :
    M 0 1 * (M 0 2 + M 1 2) = (M 0 2 + M 1 2) * M 0 1 ∧
    M 0 2 * (M 0 1 + M 1 2) = (M 0 1 + M 1 2) * M 0 2 ∧
    M 1 2 * (M 0 1 + M 0 2) = (M 0 1 + M 0 2) * M 1 2 := by
  have hv : ∀ c : k, c ≠ 1 → c ≠ 0 →
      ((![0, 1, c] : Fin 3 → k) 0 ≠ ![0, 1, c] 1 ∧ (![0, 1, c] : Fin 3 → k) 0 ≠ ![0, 1, c] 2 ∧
        (![0, 1, c] : Fin 3 → k) 1 ≠ ![0, 1, c] 2) := by
    intro c h1 h0
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.head_cons, Matrix.tail_cons]
    exact ⟨zero_ne_one, Ne.symm h0, Ne.symm h1⟩
  obtain ⟨a1, a2, a3⟩ := hv 2 (by norm_num) (by norm_num)
  obtain ⟨b1, b2, b3⟩ := hv 3 (by norm_num) (by norm_num)
  have h1 := hF ![0, 1, 2] ![1, 0, 0] ![0, 1, 0] a1 a2 a3
  have h2 := hF ![0, 1, 3] ![1, 0, 0] ![0, 1, 0] b1 b2 b3
  rw [omegaWedgeOmega_expand] at h1 h2
  simp only [omegaAt, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons] at h1 h2
  norm_num at h1 h2
  have e12 : (M 0 1 * M 0 2 - M 0 2 * M 0 1) + (M 0 1 * M 1 2 - M 1 2 * M 0 1) =
      (6 : k) • ((1 / 3 : k) • (M 0 1 * M 0 2 - M 0 2 * M 0 1) +
        (1 / 2 : k) • (M 0 1 * M 1 2 - M 1 2 * M 0 1) +
        (1 / 6 : k) • (M 0 2 * M 1 2 - M 1 2 * M 0 2)) -
      (2 : k) • ((1 / 2 : k) • (M 0 1 * M 0 2 - M 0 2 * M 0 1) +
        (M 0 1 * M 1 2 - M 1 2 * M 0 1) +
        (1 / 2 : k) • (M 0 2 * M 1 2 - M 1 2 * M 0 2)) := by module
  have e23 : (M 0 1 * M 1 2 - M 1 2 * M 0 1) + (M 0 2 * M 1 2 - M 1 2 * M 0 2) =
      (4 : k) • ((1 / 2 : k) • (M 0 1 * M 0 2 - M 0 2 * M 0 1) +
        (M 0 1 * M 1 2 - M 1 2 * M 0 1) +
        (1 / 2 : k) • (M 0 2 * M 1 2 - M 1 2 * M 0 2)) -
      (6 : k) • ((1 / 3 : k) • (M 0 1 * M 0 2 - M 0 2 * M 0 1) +
        (1 / 2 : k) • (M 0 1 * M 1 2 - M 1 2 * M 0 1) +
        (1 / 6 : k) • (M 0 2 * M 1 2 - M 1 2 * M 0 2)) := by module
  rw [h1, h2, smul_zero, smul_zero, sub_zero] at e12 e23
  refine ⟨?_, ?_, ?_⟩
  · rw [mul_add, add_mul, ← sub_eq_zero, ← e12]; abel
  · rw [mul_add, add_mul, ← sub_eq_zero]
    have : (M 0 1 * M 0 2 - M 0 2 * M 0 1) = -(M 0 1 * M 1 2 - M 1 2 * M 0 1) :=
      eq_neg_of_add_eq_zero_left e12
    have h' : (M 0 2 * M 1 2 - M 1 2 * M 0 2) = -(M 0 1 * M 1 2 - M 1 2 * M 0 1) :=
      eq_neg_of_add_eq_zero_right e23
    calc M 0 2 * M 0 1 + M 0 2 * M 1 2 - (M 0 1 * M 0 2 + M 1 2 * M 0 2)
        = -(M 0 1 * M 0 2 - M 0 2 * M 0 1) + (M 0 2 * M 1 2 - M 1 2 * M 0 2) := by abel
      _ = 0 := by rw [this, h']; abel
  · rw [mul_add, add_mul, ← sub_eq_zero, ← neg_zero (G := A), ← e23]; abel

/-- **The KZ connection has zero curvature** (three points): `ω∧ω = 0` at every
configuration with distinct coordinates, for all tangent vectors. Together with
`omegaAt_closed` this is `dω − ω∧ω = 0`. -/
theorem kz_curvature_zero (half : k) (z : Fin 3 → k) (h01 : z 0 ≠ z 1) (h02 : z 0 ≠ z 2)
    (h12 : z 1 ≠ z 2) (u v : Fin 3 → k) :
    omegaWedgeOmega (kzResidue (R := k) (n := 3) half) z u v = 0 :=
  curvature_zero_of_isFlat _ (fun i j => by simp only [kzResidue, swap_comm])
    (kz_isFlat half) z h01 h02 h12 u v

end Curvature

section Closed

variable {𝕜 : Type*} [NontriviallyNormedField 𝕜]

/-- **`d log(z_i − z_j)` is closed.** Along the line `t ↦ z + t u`, the function
`t ↦ ω_{ij}(z + t u)(v)` has derivative `−(u_i − u_j)(v_i − v_j)/(z_i − z_j)²` at `0`,
which is symmetric in `u` and `v`; so `dω_{ij}(u, v)`, the antisymmetrisation, is `0`. -/
theorem omegaAt_hasDerivAt (z u v : Fin 3 → 𝕜) (i j : Fin 3) (h : z i ≠ z j) :
    HasDerivAt (fun t : 𝕜 => omegaAt (z + t • u) v i j)
      (-(u i - u j) * (v i - v j) / (z i - z j) ^ 2) 0 := by
  have hd : z i - z j ≠ 0 := sub_ne_zero.2 h
  have hlin : HasDerivAt (fun t : 𝕜 => (z i - z j) + t * (u i - u j)) (u i - u j) 0 := by
    have := ((hasDerivAt_id (0 : 𝕜)).mul_const (u i - u j)).const_add (z i - z j)
    simpa only [id, one_mul] using this
  have hinv := hlin.inv (by simpa using hd)
  have hf : (fun t : 𝕜 => omegaAt (z + t • u) v i j) =
      fun t => (v i - v j) * ((z i - z j) + t * (u i - u j))⁻¹ := by
    funext t; simp only [omegaAt, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    rw [div_eq_mul_inv]; congr 2; ring
  rw [hf]
  convert hinv.const_mul (v i - v j) using 1
  simp; ring

theorem omegaAt_closed (z u v : Fin 3 → 𝕜) (i j : Fin 3) :
    -(u i - u j) * (v i - v j) / (z i - z j) ^ 2 -
      -(v i - v j) * (u i - u j) / (z i - z j) ^ 2 = 0 := by
  ring

end Closed

end QOU.Mass.KZConnectionSl2
