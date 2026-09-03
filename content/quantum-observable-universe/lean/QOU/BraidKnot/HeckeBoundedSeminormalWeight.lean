import QOU.BraidKnot.HeckeBoundedFullTwist

/-!
# `IsJMWeight` on the bounded presentation — and a genuine `dim > 1` witness

The last piece of the port begun in `HeckeBoundedJucysMurphy.lean`, and the one `qou-t1kv` was
actually after: a Jucys–Murphy **weight vector** on a module of dimension greater than one.

## Why this needed the bounded class

`HeckeSeminormalWeight.IsJMWeight` is stated for a `HeckeGenerators`, and
`HeckeStableScalarCascade.stdTwo_no_stable_extension` proves no irreducible representation is one.
So every witness for the unbounded predicate is forced into the **one-dimensional**
`scalarGenerators`.  `IsJMWeightB` lifts that restriction.

## Transport

`HeckeGeneratorsBelow.map` pushes a bounded presentation along an `A ≃ₐ[R] B`.  That is what lets
the explicit `2×2` matrices — which carry no `Module (Matrix …) (Fin 2 → K)` instance in Mathlib —
act as endomorphisms, where `Module.End K V` supplies `Module`, `IsScalarTower` and `Algebra`
together.  `Matrix.toLinAlgEquiv'` is the transport.

## The witness

`stdTwoBelow3_isJMWeight` : on the 2-dimensional `(2,1)` representation of `H₃(q)`, the vector
`e₀ = (1,0)` is a JM weight vector with eigenvalues `q^{2c}`, `c = 0, 1, −1` — the contents of the
standard tableau `[[1,2],[3]]`.

This is the first `IsJMWeight`-style witness in the corpus on a module of dimension `> 1`.
-/

namespace QOU.BraidKnot.Hecke

open Finset Matrix

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R} {n : ℕ}
variable {V : Type*} [AddCommGroup V] [Module A V] [Module R V] [IsScalarTower R A V]

/-! ## §1  The weight predicate -/

/-- **A Jucys–Murphy weight vector** on the bounded presentation: every `Lₖ` with `k < m` acts on
`v` by a scalar `cₖ`. -/
def IsJMWeightB (H : HeckeGeneratorsBelow R A q n) (v : V) (c : ℕ → R) (m : ℕ) : Prop :=
  ∀ k, k < m → jmRawB H k • v = c k • v

/-- The ordered product acts by the product of the eigenvalues. -/
theorem jmProdB_smul_of_weight (H : HeckeGeneratorsBelow R A q n) (v : V) (c : ℕ → R) :
    ∀ m : ℕ, IsJMWeightB H v c m → jmProdB H m • v = (∏ k ∈ Finset.range m, c k) • v := by
  intro m
  induction m with
  | zero => intro _; simp [jmProdB]
  | succ l ih =>
      intro hw
      have hl := ih fun k hk => hw k (by omega)
      rw [jmProdB_succ, MulAction.mul_smul, hw l (by omega), smul_comm, hl, smul_smul,
        Finset.prod_range_succ, mul_comm]

/-- **The full twist acts by the product of the eigenvalues.**  The bound `l < n` is the one
`jmProdB_eq_deltaB_pow` needs. -/
theorem fullTwistB_smul_of_weight (H : HeckeGeneratorsBelow R A q n) (v : V) (c : ℕ → R) (l : ℕ)
    (hl : l < n) (hw : IsJMWeightB H v c (l + 1)) :
    (deltaB H l ^ (l + 1)) • v = (∏ k ∈ Finset.range (l + 1), c k) • v := by
  rw [← jmProdB_eq_deltaB_pow H l hl]
  exact jmProdB_smul_of_weight H v c (l + 1) hw

/-! ## §2  Transport along an algebra equivalence -/

/-- Push a bounded presentation along an algebra equivalence.  Every relation is an equation
between products of generators and `algebraMap`s, all of which an `AlgEquiv` preserves. -/
def HeckeGeneratorsBelow.map {B : Type*} [Ring B] [Algebra R B]
    (H : HeckeGeneratorsBelow R A q n) (f : A ≃ₐ[R] B) : HeckeGeneratorsBelow R B q n where
  σ i := f (H.σ i)
  hecke i hi := by
    have := congrArg f (H.hecke i hi)
    simpa [map_mul, map_add, map_one, AlgEquiv.commutes] using this
  braid i hi := by
    have := congrArg f (H.braid i hi)
    simpa [map_mul] using this
  far i j hij hjn := by
    have := congrArg f (H.far i j hij hjn)
    simpa [map_mul] using this

@[simp] theorem map_σ {B : Type*} [Ring B] [Algebra R B]
    (H : HeckeGeneratorsBelow R A q n) (f : A ≃ₐ[R] B) (i : ℕ) :
    (H.map f).σ i = f (H.σ i) := rfl

/-- The JM elements transport too. -/
@[simp] theorem jmRawB_map {B : Type*} [Ring B] [Algebra R B]
    (H : HeckeGeneratorsBelow R A q n) (f : A ≃ₐ[R] B) :
    ∀ k, jmRawB (H.map f) k = f (jmRawB H k)
  | 0 => by simp [jmRawB]
  | (i + 1) => by rw [jmRawB_succ, jmRawB_succ, jmRawB_map H f i, map_σ, map_mul, map_mul]

/-! ## §3  The `dim > 1` witness -/

section StdThree

variable {K : Type*} [Field K]

/-- The `(2,1)` representation of `H₃(q)` as endomorphisms of `Fin 2 → K`, where the module
structure `IsJMWeightB` needs actually exists. -/
noncomputable def stdTwoEnd3 (q : K) (hq : q ≠ 0) :
    HeckeGeneratorsBelow K (Module.End K (Fin 2 → K)) q 3 :=
  (stdTwoBelow3 q hq).map Matrix.toLinAlgEquiv'

/-- Acting by a transported matrix is `mulVec`. -/
theorem toLinAlgEquiv'_smul (M : Matrix (Fin 2) (Fin 2) K) (v : Fin 2 → K) :
    (Matrix.toLinAlgEquiv' M) • v = M.mulVec v := rfl

/-- **The `dim > 1` Jucys–Murphy weight vector.**

On the 2-dimensional `(2,1)` representation of `H₃(q)`, `e₀ = (1,0)` is a JM weight vector with
eigenvalues `q^{2c}` for the contents `c = 0, 1, −1` of the standard tableau `[[1,2],[3]]`.

Every previous witness for this predicate in the corpus was one-dimensional, and necessarily so:
`stdTwo_no_stable_extension` shows the unbounded presentation admits no irreducible representation
at all. -/
theorem stdTwoBelow3_isJMWeight (q : K) (hq : q ≠ 0) :
    IsJMWeightB (stdTwoEnd3 q hq) (seminormalE0 K)
      (fun k => if k = 0 then 1 else if k = 1 then q ^ 2 else (q ^ 2)⁻¹) 3 := by
  intro k hk
  have h : k = 0 ∨ k = 1 ∨ k = 2 := by omega
  rcases h with rfl | rfl | rfl
  · simp [stdTwoEnd3]
  · rw [stdTwoEnd3, jmRawB_map, stdTwoBelow3_jmRaw_one, toLinAlgEquiv'_smul]
    show _ = q ^ 2 • seminormalE0 K
    exact stdTwo_jm1_smul q
  · rw [stdTwoEnd3, jmRawB_map, stdTwoBelow3_jmRaw_two, toLinAlgEquiv'_smul]
    show _ = (q ^ 2)⁻¹ • seminormalE0 K
    exact stdTwo_jm2_smul q hq

end StdThree

end QOU.BraidKnot.Hecke
