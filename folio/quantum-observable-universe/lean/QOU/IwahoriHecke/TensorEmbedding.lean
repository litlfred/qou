import QOU.IwahoriHecke.RMatrixSl2
import QOU.MassTheory.PiTensorMonomialBasis
import Mathlib.LinearAlgebra.Matrix.ToLin

/-!
# Embedding a braiding into a larger tensor product

`QOU.IwahoriHecke.RMatrixSl2` proved the two relations for Jimbo's `Ř` and assembled the
Hecke action of `H₃(q)` on `V^{⊗3}`. Everything there is at a fixed, small number of
tensor factors. This file supplies what a general `n` needs: the operation "act on this
factor, do nothing to the rest", and the fact that it preserves every relation in sight.

## The two embeddings

For index types `σ`, `ρ` (the acted-on factor and the spectator factor):

* `tensorId M = M ⊗ 1` on `σ × ρ`;
* `idTensor N = 1 ⊗ N` on `σ × ρ`.

Both are **algebra maps** (`tensorIdHom`, `idTensorHom`), which is the whole point: an
algebra map transports the §7a quadratic (`IsHeckeGenerator.map`), the braid relation, and
anything else stated as an equation between products. So the results of `RMatrixSl2` hold
for the embedded operators for free, at any size.

## What this gives, and what it does not

**Gives**, at arbitrary spectator size:

* `isHeckeGenerator_tensorId_rCheck` — `Ř ⊗ 1` is still a §7a Hecke generator;
* `tensorId_commute_idTensor` — operators on disjoint factors commute, which is the **far
  commutation** relation `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2`;
* `yangBaxter_tensorId` — the braid relation survives the embedding.

## Site-indexed, on `V^{⊗n}`

The second half does supply sites, in the model `V^{⊗n} = ((Fin n → Fin 2) → R)` whose
monomial basis is `Fin n → Fin 2` — the model `QOU.MassTheory.PiTensorMonomialBasis`
identifies with the genuine `PiTensorProduct`. `embedPair i j` acts at **any** two distinct
sites, adjacent or not; `embedPairHom` is its algebra-map packaging; and
`isHeckeGenerator_braidAt` is the general-`n` statement:

> for every `n`, and every pair of distinct sites `i ≠ j` of `V^{⊗n}`, the embedded
> R-matrix satisfies `Ř_{ij}² = (q − qi) Ř_{ij} + 1`.

`braidAt_commute` and `braidAt_braid` are the other two:

> braidings at **disjoint** pairs of sites commute — `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2`;
> and three distinct sites satisfy the **braid relation**
> `Ř_{ij} Ř_{jk} Ř_{ij} = Ř_{jk} Ř_{ij} Ř_{jk}`.

All three defining families, so `heckeActionN` assembles them into an actual algebra map

> `H_{m+1}(q) → End(V^{⊗(m+1)})`,  `σ_a ↦ Ř` at sites `a`, `a+1`.

The engine for both is `sum_collapse`: a `2^n`-term sum whose summand is supported on the
states agreeing with `a` off `{i, j}` is a 4-term sum over the assignments to those sites.
Far commutation needs no second collapse — `sum_collapse` is applied once to each side and
both reduce to the same four-index normal form
(`embedPair_mul_apply_of_disjoint`), which is symmetric in the two pairs because the base
ring is commutative.

-- Ref: [jimbo1986]; [leitner2026] bean qou-k4oq
-/

namespace QOU.IwahoriHecke.TensorEmbed

open QOU.MathlibExt.SkeinRelation QOU.IwahoriHecke.RMatrix
open scoped TensorProduct

variable {R : Type*} [CommRing R]

/-! ## Algebra maps transport the Hecke relation -/

/-- **`IsHeckeGenerator` is preserved by every algebra map.** The §7a quadratic is an
equation between products and scalars, so any `R`-algebra map carries it along. This is
what makes the embeddings below cost nothing. -/
theorem IsHeckeGenerator.map {A B : Type*} [Ring A] [Algebra R A] [Ring B] [Algebra R B]
    (φ : A →ₐ[R] B) {q qi : R} {x : A} (h : IsHeckeGenerator q qi x) :
    IsHeckeGenerator q qi (φ x) := by
  have h' := congrArg φ h.eq
  rw [map_mul, map_add, map_mul, map_one, AlgHom.commutes] at h'
  exact h'

/-! ## The two embeddings -/

-- Each lemma below uses a different subset of the four index-type instances (the `if`s
-- need `DecidableEq`, the sums need `Fintype`), so per-declaration `omit` lines would
-- outnumber the proofs.
set_option linter.unusedSectionVars false

variable {σ ρ : Type*} [Fintype σ] [DecidableEq σ] [Fintype ρ] [DecidableEq ρ]

/-- `M ⊗ 1`: act by `M` on the `σ`-factor, do nothing to the `ρ`-factor. -/
def tensorId (M : Matrix σ σ R) : Matrix (σ × ρ) (σ × ρ) R :=
  Matrix.of fun a b => M a.1 b.1 * (if a.2 = b.2 then 1 else 0)

/-- `1 ⊗ N`: act by `N` on the `ρ`-factor, do nothing to the `σ`-factor. -/
def idTensor (N : Matrix ρ ρ R) : Matrix (σ × ρ) (σ × ρ) R :=
  Matrix.of fun a b => (if a.1 = b.1 then 1 else 0) * N a.2 b.2

@[simp] theorem tensorId_apply (M : Matrix σ σ R) (a b : σ × ρ) :
    tensorId M a b = M a.1 b.1 * (if a.2 = b.2 then 1 else 0) := rfl

@[simp] theorem idTensor_apply (N : Matrix ρ ρ R) (a b : σ × ρ) :
    idTensor (σ := σ) N a b = (if a.1 = b.1 then 1 else 0) * N a.2 b.2 := rfl

theorem tensorId_mul (M N : Matrix σ σ R) :
    (tensorId M : Matrix (σ × ρ) (σ × ρ) R) * tensorId N = tensorId (M * N) := by
  ext a b
  simp only [tensorId_apply, Matrix.mul_apply, Fintype.sum_prod_type]
  rw [Finset.sum_comm]
  simp [Finset.mul_sum, Finset.sum_ite_eq, mul_comm]

theorem idTensor_mul (M N : Matrix ρ ρ R) :
    (idTensor M : Matrix (σ × ρ) (σ × ρ) R) * idTensor N = idTensor (M * N) := by
  ext a b
  simp only [idTensor_apply, Matrix.mul_apply, Fintype.sum_prod_type]
  simp [Finset.sum_ite_eq, mul_comm]

@[simp] theorem tensorId_one : (tensorId (1 : Matrix σ σ R) : Matrix (σ × ρ) (σ × ρ) R) = 1 := by
  ext a b
  simp [tensorId, Matrix.one_apply, Prod.ext_iff, ite_and]
  split_ifs <;> rfl

@[simp] theorem idTensor_one : (idTensor (1 : Matrix ρ ρ R) : Matrix (σ × ρ) (σ × ρ) R) = 1 := by
  ext a b
  simp [idTensor, Matrix.one_apply, Prod.ext_iff, ite_and]
  split_ifs <;> rfl

theorem tensorId_add (M N : Matrix σ σ R) :
    (tensorId (M + N) : Matrix (σ × ρ) (σ × ρ) R) = tensorId M + tensorId N := by
  ext a b; simp [tensorId]; split_ifs <;> simp

theorem idTensor_add (M N : Matrix ρ ρ R) :
    (idTensor (M + N) : Matrix (σ × ρ) (σ × ρ) R) = idTensor M + idTensor N := by
  ext a b; simp [idTensor]; split_ifs <;> simp

theorem tensorId_algebraMap [Nonempty ρ] (r : R) :
    (tensorId (algebraMap R (Matrix σ σ R) r) : Matrix (σ × ρ) (σ × ρ) R)
      = algebraMap R _ r := by
  ext a b
  simp [tensorId, Algebra.algebraMap_eq_smul_one, Matrix.one_apply, Prod.ext_iff, ite_and]
  split_ifs <;> rfl

theorem idTensor_algebraMap [Nonempty σ] (r : R) :
    (idTensor (algebraMap R (Matrix ρ ρ R) r) : Matrix (σ × ρ) (σ × ρ) R)
      = algebraMap R _ r := by
  ext a b
  simp [idTensor, Algebra.algebraMap_eq_smul_one, Matrix.one_apply, Prod.ext_iff, ite_and]
  split_ifs <;> rfl

/-- **`M ↦ M ⊗ 1` is an algebra map.** Everything in this file follows from this and its
mirror image. -/
def tensorIdHom [Nonempty ρ] : Matrix σ σ R →ₐ[R] Matrix (σ × ρ) (σ × ρ) R where
  toFun := tensorId
  map_one' := tensorId_one
  map_mul' _ _ := (tensorId_mul _ _).symm
  map_zero' := by ext a b; simp [tensorId]
  map_add' _ _ := tensorId_add _ _
  commutes' := tensorId_algebraMap

/-- **`N ↦ 1 ⊗ N` is an algebra map.** -/
def idTensorHom [Nonempty σ] : Matrix ρ ρ R →ₐ[R] Matrix (σ × ρ) (σ × ρ) R where
  toFun := idTensor
  map_one' := idTensor_one
  map_mul' _ _ := (idTensor_mul _ _).symm
  map_zero' := by ext a b; simp [idTensor]
  map_add' _ _ := idTensor_add _ _
  commutes' := idTensor_algebraMap

@[simp] theorem tensorIdHom_apply [Nonempty ρ] (M : Matrix σ σ R) :
    (tensorIdHom (ρ := ρ) M : Matrix (σ × ρ) (σ × ρ) R) = tensorId M := rfl

@[simp] theorem idTensorHom_apply [Nonempty σ] (N : Matrix ρ ρ R) :
    (idTensorHom (σ := σ) N : Matrix (σ × ρ) (σ × ρ) R) = idTensor N := rfl

/-! ## Far commutation

Operators acting on disjoint tensor factors commute. This **is** the far-commutation
relation `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2` — the third defining family of the Hecke
algebra, and the only one that needs no computation with `Ř` at all. -/

/-- **Operators on disjoint factors commute.** -/
theorem tensorId_commute_idTensor (M : Matrix σ σ R) (N : Matrix ρ ρ R) :
    (tensorId M : Matrix (σ × ρ) (σ × ρ) R) * idTensor N
      = idTensor N * tensorId M := by
  ext a b
  simp only [tensorId_apply, idTensor_apply, Matrix.mul_apply, Fintype.sum_prod_type]
  simp [Finset.sum_ite_eq, mul_comm]

/-! ## The `Ř` relations survive the embedding

Each of these is the corresponding result of `RMatrixSl2` pushed along an algebra map, so
none of them costs a new matrix computation. -/

variable (q qi : R)

/-- **The embedded braiding is still a §7a Hecke generator**, for a spectator factor of any
size. -/
theorem isHeckeGenerator_tensorId_rCheck [Nonempty ρ] (hqi : q * qi = 1) :
    IsHeckeGenerator q qi
      (tensorId (ρ := ρ) (rCheck q qi) : Matrix ((Fin 2 × Fin 2) × ρ) _ R) :=
  IsHeckeGenerator.map (tensorIdHom (R := R) (σ := Fin 2 × Fin 2) (ρ := ρ))
    (isHeckeGenerator_rCheck q qi hqi)

/-- **Yang–Baxter survives the embedding.** The braid relation for the two embedded
adjacent braidings, at any spectator size. -/
theorem yangBaxter_tensorId [Nonempty ρ] (hqi : q * qi = 1) :
    (tensorId (ρ := ρ) (rc1 q qi) : Matrix ((Fin 2 × Fin 2 × Fin 2) × ρ) _ R)
        * tensorId (rc2 q qi) * tensorId (rc1 q qi)
      = tensorId (rc2 q qi) * tensorId (rc1 q qi) * tensorId (rc2 q qi) := by
  have h := congrArg (tensorIdHom (R := R) (σ := Fin 2 × Fin 2 × Fin 2) (ρ := ρ))
    (yangBaxter q qi hqi)
  simpa [map_mul] using h

/-- The embedded braidings at *disjoint* pairs of sites commute — far commutation, obtained
with no computation. -/
theorem farCommute_rCheck (N : Matrix ρ ρ R) :
    (tensorId (ρ := ρ) (rCheck q qi) : Matrix ((Fin 2 × Fin 2) × ρ) _ R) * idTensor N
      = idTensor N * tensorId (rCheck q qi) :=
  tensorId_commute_idTensor _ _

/-! ## Site-indexed embedding on `V^{⊗n}`

The section above is size-agnostic but has no notion of a *site*. This one supplies it, in
the model `V^{⊗n} = ((Fin n → Fin 2) → R)` whose monomial basis is indexed by `Fin n → Fin 2`
— the same model `QOU.MassTheory.PiTensorMonomialBasis` identifies with the genuine
`PiTensorProduct`.

`embedPair i j M` acts by `M` on sites `i` and `j` and by the identity everywhere else, for
**any** two distinct sites, adjacent or not. -/

section Sites

variable {n : ℕ}

/-- A two-site operator acting at sites `i` and `j` of `V^{⊗n}` and trivially elsewhere. -/
def embedPair (i j : Fin n) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    Matrix (Fin n → Fin 2) (Fin n → Fin 2) R :=
  Matrix.of fun a b =>
    if (∀ k, k ≠ i → k ≠ j → a k = b k) then M (a i, a j) (b i, b j) else 0

theorem embedPair_apply (i j : Fin n) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R)
    (a b : Fin n → Fin 2) :
    embedPair i j M a b
      = if (∀ k, k ≠ i → k ≠ j → a k = b k) then M (a i, a j) (b i, b j) else 0 := rfl

/-- **The two free sites parametrise the states agreeing with `a` elsewhere.** Fixing a
reference state `a`, the assignments to sites `i ≠ j` biject with the states that agree with
`a` off `{i, j}`. This is the one combinatorial fact the site-indexed calculus needs; every
sum below collapses along it from `2^n` terms to `4`. -/
def pairEquiv {i j : Fin n} (hij : i ≠ j) (a : Fin n → Fin 2) :
    (Fin 2 × Fin 2) ≃ {c : Fin n → Fin 2 // ∀ k, k ≠ i → k ≠ j → a k = c k} where
  toFun x := ⟨Function.update (Function.update a i x.1) j x.2, by
    intro k hki hkj
    rw [Function.update_of_ne hkj, Function.update_of_ne hki]⟩
  invFun c := (c.1 i, c.1 j)
  left_inv x := by
    have hi : Function.update (Function.update a i x.1) j x.2 i = x.1 := by
      rw [Function.update_of_ne hij, Function.update_self]
    simp [hi, Function.update_self]
  right_inv c := by
    refine Subtype.ext (funext fun k => ?_)
    dsimp only
    by_cases hkj : k = j
    · subst hkj; rw [Function.update_self]
    · rw [Function.update_of_ne hkj]
      by_cases hki : k = i
      · subst hki; rw [Function.update_self]
      · rw [Function.update_of_ne hki]
        exact c.2 k hki hkj

/-- The collapse: a sum over all `2^n` states of a function supported on the states agreeing
with `a` off `{i, j}` is a sum over the four assignments to those two sites. -/
theorem sum_collapse {i j : Fin n} (hij : i ≠ j) (a : Fin n → Fin 2)
    (F : (Fin n → Fin 2) → R)
    (hF : ∀ c, ¬(∀ k, k ≠ i → k ≠ j → a k = c k) → F c = 0) :
    ∑ c, F c
      = ∑ x : Fin 2 × Fin 2, F (Function.update (Function.update a i x.1) j x.2) := by
  classical
  rw [← Finset.sum_filter_of_ne (p := fun c => ∀ k, k ≠ i → k ≠ j → a k = c k)
        (fun c _ hc => by by_contra h; exact hc (hF c h))]
  rw [Finset.sum_subtype _ (fun c => by simp)
        (f := F) (p := fun c => ∀ k, k ≠ i → k ≠ j → a k = c k)]
  exact (Fintype.sum_equiv (pairEquiv hij a) _ _ (fun _ => rfl)).symm

/-! ### The site-indexed embedding is an algebra map -/

variable {i j : Fin n}

private theorem update_left (hij : i ≠ j) (a : Fin n → Fin 2) (x : Fin 2 × Fin 2) :
    Function.update (Function.update a i x.1) j x.2 i = x.1 := by
  rw [Function.update_of_ne hij, Function.update_self]

private theorem update_right (a : Fin n → Fin 2) (x : Fin 2 × Fin 2) :
    Function.update (Function.update a i x.1) j x.2 j = x.2 := Function.update_self ..

private theorem update_agrees (a : Fin n → Fin 2) (x : Fin 2 × Fin 2) :
    ∀ k, k ≠ i → k ≠ j → a k = Function.update (Function.update a i x.1) j x.2 k := by
  intro k hki hkj
  rw [Function.update_of_ne hkj, Function.update_of_ne hki]

/-- The embedded operator's entry from `a` to a state differing only at the two sites. -/
theorem embedPair_apply_update (hij : i ≠ j) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R)
    (a : Fin n → Fin 2) (x : Fin 2 × Fin 2) :
    embedPair i j M a (Function.update (Function.update a i x.1) j x.2) = M (a i, a j) x := by
  rw [embedPair_apply, if_pos (update_agrees a x), update_left hij, update_right]

/-- The embedded operator's entry from such a state to an arbitrary `b`: the off-window
condition is unchanged by the update, so it is `a`'s own condition. -/
theorem embedPair_update_apply (hij : i ≠ j) (N : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R)
    (a b : Fin n → Fin 2) (x : Fin 2 × Fin 2) :
    embedPair i j N (Function.update (Function.update a i x.1) j x.2) b
      = if (∀ k, k ≠ i → k ≠ j → a k = b k) then N x (b i, b j) else 0 := by
  rw [embedPair_apply, update_left hij, update_right]
  congr 1
  refine propext ⟨fun h k hki hkj => ?_, fun h k hki hkj => ?_⟩
  · rw [update_agrees a x k hki hkj]; exact h k hki hkj
  · rw [← update_agrees a x k hki hkj]; exact h k hki hkj

/-- **The site-indexed embedding is multiplicative.** The `2^n`-term sum collapses to the
four assignments to the two sites, which is exactly the matrix product on the window. -/
theorem embedPair_mul (hij : i ≠ j) (M N : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    embedPair i j M * embedPair i j N = embedPair i j (M * N) := by
  classical
  ext a b
  rw [Matrix.mul_apply]
  rw [sum_collapse hij a (fun c => embedPair i j M a c * embedPair i j N c b)
    (fun c hc => by dsimp only; rw [embedPair_apply, if_neg hc, zero_mul])]
  simp only [embedPair_apply_update hij, embedPair_update_apply hij]
  by_cases hab : ∀ k, k ≠ i → k ≠ j → a k = b k
  · simp only [if_pos hab]
    rw [embedPair_apply, if_pos hab, Matrix.mul_apply]
  · simp [hab, embedPair_apply]

@[simp] theorem embedPair_one (hij : i ≠ j) :
    embedPair i j (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) = 1 := by
  classical
  ext a b
  rw [embedPair_apply, Matrix.one_apply, Matrix.one_apply]
  by_cases hab : ∀ k, k ≠ i → k ≠ j → a k = b k
  · rw [if_pos hab]
    by_cases h : a = b
    · subst h; simp
    · rw [if_neg h]
      refine if_neg (fun hx => h (funext fun k => ?_))
      by_cases hki : k = i
      · subst hki; exact congrArg Prod.fst hx
      · by_cases hkj : k = j
        · subst hkj; exact congrArg Prod.snd hx
        · exact hab k hki hkj
  · rw [if_neg hab, if_neg (fun h => hab (fun k _ _ => by rw [h]))]

theorem embedPair_add (M N : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    embedPair i j (M + N) = embedPair (R := R) i j M + embedPair i j N := by
  ext a b; simp only [embedPair_apply, Matrix.add_apply]; split_ifs <;> simp

theorem embedPair_smul (c : R) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    embedPair i j (c • M) = c • embedPair (R := R) i j M := by
  ext a b
  simp only [embedPair_apply, Matrix.smul_apply, smul_eq_mul]
  split_ifs <;> simp

theorem embedPair_algebraMap (hij : i ≠ j) (r : R) :
    embedPair i j (algebraMap R (Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) r)
      = algebraMap R (Matrix (Fin n → Fin 2) (Fin n → Fin 2) R) r := by
  rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one, embedPair_smul,
    embedPair_one (R := R) hij]

/-- **`M ↦ M` at sites `i ≠ j` is an algebra map** `End(V ⊗ V) → End(V^{⊗n})`. -/
def embedPairHom (hij : i ≠ j) :
    Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R →ₐ[R]
      Matrix (Fin n → Fin 2) (Fin n → Fin 2) R where
  toFun := embedPair i j
  map_one' := embedPair_one hij
  map_mul' _ _ := (embedPair_mul hij _ _).symm
  map_zero' := by ext a b; simp only [embedPair_apply, Matrix.zero_apply]; split_ifs <;> rfl
  map_add' _ _ := embedPair_add _ _
  commutes' := embedPair_algebraMap hij

@[simp] theorem embedPairHom_apply (hij : i ≠ j)
    (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    embedPairHom (R := R) hij M = embedPair i j M := rfl

/-- **The braiding at two sites of `V^{⊗n}`.** For any `n` and any two distinct sites. -/
def braidAt (q qi : R) (i j : Fin n) : Matrix (Fin n → Fin 2) (Fin n → Fin 2) R :=
  embedPair i j (rCheck q qi)

/-- **The general-`n` result.** At any number of tensor factors and any two distinct sites,
the embedded R-matrix is a §7a Hecke generator: `Ř_{ij}² = (q − qi) Ř_{ij} + 1`. So it is
invertible, satisfies the skein relation, and factors with eigenvalues `q` and `−qi` — all
inherited through `embedPairHom` at no extra cost. -/
theorem isHeckeGenerator_braidAt (hij : i ≠ j) (hqi : q * qi = 1) :
    IsHeckeGenerator q qi (braidAt q qi i j) :=
  IsHeckeGenerator.map (embedPairHom (R := R) hij) (isHeckeGenerator_rCheck q qi hqi)

/-- Consequently the braiding at any two sites of `V^{⊗n}` is invertible. -/
theorem isUnit_braidAt (hij : i ≠ j) (hqi : q * qi = 1) : IsUnit (braidAt q qi i j) :=
  isUnit_of_isHeckeGenerator (isHeckeGenerator_braidAt q qi hij hqi)

/-- And satisfies the skein relation `Ř_{ij} − Ř_{ij}⁻¹ = q − qi`. -/
theorem braidAt_sub_inv (hij : i ≠ j) (hqi : q * qi = 1)
    {S : Matrix (Fin n → Fin 2) (Fin n → Fin 2) R} (hS : braidAt q qi i j * S = 1) :
    braidAt q qi i j - S = algebraMap R _ (q - qi) :=
  sub_inv_eq (isHeckeGenerator_braidAt q qi hij hqi) hS

/-! ### Far commutation at general `n`

The second defining family, in the site-indexed model: braidings at **disjoint** pairs of
sites commute. No new collapse lemma is needed — `sum_collapse` is applied once to each
side and both reduce to the same four-index normal form, which is symmetric in the two
pairs because the base ring is commutative. -/

variable {k l : Fin n}

/-- After updating `a` at sites `i, j`, agreement with `b` off `{k,l}` splits into the two
window values matching `b` and agreement off all four sites. -/
private theorem agree_update_iff (hij : i ≠ j) (hki : k ≠ i) (hkj : k ≠ j)
    (hli : l ≠ i) (hlj : l ≠ j) (a b : Fin n → Fin 2) (x : Fin 2 × Fin 2) :
    (∀ m, m ≠ k → m ≠ l → Function.update (Function.update a i x.1) j x.2 m = b m)
      ↔ (x = (b i, b j) ∧ ∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m) := by
  constructor
  · intro h
    refine ⟨Prod.ext ?_ ?_, fun m hmi hmj hmk hml => ?_⟩
    · rw [← update_left hij a x]; exact h i (Ne.symm hki) (Ne.symm hli)
    · rw [← update_right a x]; exact h j (Ne.symm hkj) (Ne.symm hlj)
    · rw [update_agrees a x m hmi hmj]; exact h m hmk hml
  · rintro ⟨rfl, h3⟩ m hmk hml
    by_cases hmi : m = i
    · subst hmi; exact update_left hij a _
    · by_cases hmj : m = j
      · subst hmj; exact update_right a _
      · rw [← update_agrees a _ m hmi hmj]; exact h3 m hmi hmj hmk hml

/-- **The four-index normal form.** A product of braidings at two disjoint pairs of sites
has one entry per pair, gated by agreement off all four sites. -/
private theorem embedPair_mul_apply_of_disjoint (hij : i ≠ j) (hki : k ≠ i) (hkj : k ≠ j)
    (hli : l ≠ i) (hlj : l ≠ j)
    (M N : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) (a b : Fin n → Fin 2) :
    (embedPair i j M * embedPair k l N) a b
      = if (∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m)
        then M (a i, a j) (b i, b j) * N (a k, a l) (b k, b l) else 0 := by
  classical
  rw [Matrix.mul_apply,
    sum_collapse hij a (fun c => embedPair i j M a c * embedPair k l N c b)
      (fun c hc => by dsimp only; rw [embedPair_apply, if_neg hc, zero_mul])]
  have hval : ∀ x : Fin 2 × Fin 2,
      embedPair i j M a (Function.update (Function.update a i x.1) j x.2)
          * embedPair k l N (Function.update (Function.update a i x.1) j x.2) b
        = M (a i, a j) x
          * (if (x = (b i, b j) ∧ ∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m)
             then N (a k, a l) (b k, b l) else 0) := by
    intro x
    rw [embedPair_apply_update hij, embedPair_apply,
      ← update_agrees a x k hki hkj, ← update_agrees a x l hli hlj]
    simp only [agree_update_iff hij hki hkj hli hlj]
  rw [Finset.sum_congr rfl (fun x _ => hval x)]
  by_cases hP : ∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m
  · rw [if_pos hP]
    simp only [eq_true hP, and_true, mul_ite, mul_zero]
    simp
  · rw [if_neg hP]
    simp [hP]

/-- **Far commutation.** Braidings at disjoint pairs of sites commute, at any `n`. This is
the defining relation `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2`, in the site-indexed model. -/
theorem embedPair_commute (hij : i ≠ j) (hkl : k ≠ l) (hki : k ≠ i) (hkj : k ≠ j)
    (hli : l ≠ i) (hlj : l ≠ j) (M N : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    embedPair i j M * embedPair k l N = embedPair k l N * embedPair i j M := by
  ext a b
  rw [embedPair_mul_apply_of_disjoint hij hki hkj hli hlj,
    embedPair_mul_apply_of_disjoint hkl (Ne.symm hki) (Ne.symm hli)
      (Ne.symm hkj) (Ne.symm hlj)]
  by_cases h : ∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m
  · rw [if_pos h, if_pos (fun m h1 h2 h3 h4 => h m h3 h4 h1 h2), mul_comm]
  · rw [if_neg h, if_neg (fun hc => h (fun m h1 h2 h3 h4 => hc m h3 h4 h1 h2))]

/-- **The braidings at disjoint site pairs commute** — far commutation for `Ř` itself. -/
theorem braidAt_commute (hij : i ≠ j) (hkl : k ≠ l) (hki : k ≠ i) (hkj : k ≠ j)
    (hli : l ≠ i) (hlj : l ≠ j) :
    braidAt q qi i j * braidAt q qi k l = braidAt q qi k l * braidAt q qi i j :=
  embedPair_commute hij hkl hki hkj hli hlj _ _

/-! ### Three sites, and the braid relation at general `n`

Far commutation needed only the two-site collapse because its pairs are disjoint. The braid
relation's three factors overlap, so the intermediate states range over three sites at once.
This section builds the three-site embedding, shows the two-site one factors through it, and
then the braid relation is `yangBaxter` transported — no new matrix computation. -/

variable {m₃ : Fin n}

/-- A three-site operator acting at `i`, `j`, `k` and trivially elsewhere. -/
def embedTriple (i j k : Fin n)
    (M : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R) :
    Matrix (Fin n → Fin 2) (Fin n → Fin 2) R :=
  Matrix.of fun a b =>
    if (∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m)
    then M (a i, a j, a k) (b i, b j, b k) else 0

theorem embedTriple_apply (i j k : Fin n)
    (M : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R) (a b : Fin n → Fin 2) :
    embedTriple i j k M a b
      = if (∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m)
        then M (a i, a j, a k) (b i, b j, b k) else 0 := rfl

variable {k : Fin n}

/-- The three free sites parametrise the states agreeing with `a` elsewhere. -/
def tripleEquiv (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) (a : Fin n → Fin 2) :
    (Fin 2 × Fin 2 × Fin 2)
      ≃ {c : Fin n → Fin 2 // ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m} where
  toFun x := ⟨Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2, by
    intro m hmi hmj hmk
    rw [Function.update_of_ne hmk, Function.update_of_ne hmj, Function.update_of_ne hmi]⟩
  invFun c := (c.1 i, c.1 j, c.1 k)
  left_inv x := by
    have hi : Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 i
        = x.1 := by
      rw [Function.update_of_ne hik, Function.update_of_ne hij, Function.update_self]
    have hj : Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 j
        = x.2.1 := by
      rw [Function.update_of_ne hjk, Function.update_self]
    simp [hi, hj, Function.update_self]
  right_inv c := by
    refine Subtype.ext (funext fun m => ?_)
    dsimp only
    by_cases hmk : m = k
    · subst hmk; rw [Function.update_self]
    · rw [Function.update_of_ne hmk]
      by_cases hmj : m = j
      · subst hmj; rw [Function.update_self]
      · rw [Function.update_of_ne hmj]
        by_cases hmi : m = i
        · subst hmi; rw [Function.update_self]
        · rw [Function.update_of_ne hmi]; exact c.2 m hmi hmj hmk

/-- The three-site collapse: `2^n` terms become `8`. -/
theorem sum_collapse3 (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) (a : Fin n → Fin 2)
    (F : (Fin n → Fin 2) → R)
    (hF : ∀ c, ¬(∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m) → F c = 0) :
    ∑ c, F c
      = ∑ x : Fin 2 × Fin 2 × Fin 2,
          F (Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2) := by
  classical
  rw [← Finset.sum_filter_of_ne (p := fun c => ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m)
        (fun c _ hc => by by_contra h; exact hc (hF c h))]
  rw [Finset.sum_subtype _ (fun c => by simp)
        (f := F) (p := fun c => ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m)]
  exact (Fintype.sum_equiv (tripleEquiv hij hik hjk a) _ _ (fun _ => rfl)).symm

private theorem upd3_i (hij : i ≠ j) (hik : i ≠ k) (a : Fin n → Fin 2)
    (x : Fin 2 × Fin 2 × Fin 2) :
    Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 i = x.1 := by
  rw [Function.update_of_ne hik, Function.update_of_ne hij, Function.update_self]

private theorem upd3_j (hjk : j ≠ k) (a : Fin n → Fin 2) (x : Fin 2 × Fin 2 × Fin 2) :
    Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 j = x.2.1 := by
  rw [Function.update_of_ne hjk, Function.update_self]

private theorem upd3_k (a : Fin n → Fin 2) (x : Fin 2 × Fin 2 × Fin 2) :
    Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 k = x.2.2 :=
  Function.update_self ..

private theorem upd3_agrees (a : Fin n → Fin 2) (x : Fin 2 × Fin 2 × Fin 2) :
    ∀ m, m ≠ i → m ≠ j → m ≠ k →
      a m = Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 m := by
  intro m hmi hmj hmk
  rw [Function.update_of_ne hmk, Function.update_of_ne hmj, Function.update_of_ne hmi]

theorem embedTriple_apply_update (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k)
    (M : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R)
    (a : Fin n → Fin 2) (x : Fin 2 × Fin 2 × Fin 2) :
    embedTriple i j k M a
        (Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2)
      = M (a i, a j, a k) x := by
  rw [embedTriple_apply, if_pos (upd3_agrees a x), upd3_i hij hik, upd3_j hjk, upd3_k]

theorem embedTriple_update_apply (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k)
    (N : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R)
    (a b : Fin n → Fin 2) (x : Fin 2 × Fin 2 × Fin 2) :
    embedTriple i j k N
        (Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2) b
      = if (∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m)
        then N x (b i, b j, b k) else 0 := by
  rw [embedTriple_apply, upd3_i hij hik, upd3_j hjk, upd3_k]
  congr 1
  refine propext ⟨fun h m hmi hmj hmk => ?_, fun h m hmi hmj hmk => ?_⟩
  · rw [upd3_agrees a x m hmi hmj hmk]; exact h m hmi hmj hmk
  · rw [← upd3_agrees a x m hmi hmj hmk]; exact h m hmi hmj hmk

/-- **The three-site embedding is multiplicative.** -/
theorem embedTriple_mul (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k)
    (M N : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R) :
    embedTriple i j k M * embedTriple i j k N = embedTriple i j k (M * N) := by
  classical
  ext a b
  rw [Matrix.mul_apply,
    sum_collapse3 hij hik hjk a (fun c => embedTriple i j k M a c * embedTriple i j k N c b)
      (fun c hc => by dsimp only; rw [embedTriple_apply, if_neg hc, zero_mul])]
  simp only [embedTriple_apply_update hij hik hjk, embedTriple_update_apply hij hik hjk]
  by_cases hab : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
  · simp only [if_pos hab]
    rw [embedTriple_apply, if_pos hab, Matrix.mul_apply]
  · simp [hab, embedTriple_apply]

/-! #### The two-site embedding factors through the three-site one -/

/-- `Ř` at sites `i, j` is `Ř ⊗ 1` at sites `i, j, k`. -/
theorem embedPair_eq_embedTriple_left (hik : i ≠ k) (hjk : j ≠ k)
    (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    embedPair i j M
      = embedTriple i j k
          (Matrix.of fun u v => M (u.1, u.2.1) (v.1, v.2.1)
            * (if u.2.2 = v.2.2 then 1 else 0)) := by
  classical
  ext a b
  rw [embedPair_apply, embedTriple_apply]
  by_cases hk : a k = b k
  · by_cases h3 : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
    · rw [if_pos h3, if_pos (fun m hmi hmj => by
        by_cases hmk : m = k
        · subst hmk; exact hk
        · exact h3 m hmi hmj hmk)]
      simp [hk]
    · rw [if_neg h3, if_neg (fun h2 => h3 (fun m hmi hmj _ => h2 m hmi hmj))]
  · rw [if_neg (fun h2 => hk (h2 k (Ne.symm hik) (Ne.symm hjk)))]
    by_cases h3 : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
    · rw [if_pos h3]; simp [hk]
    · rw [if_neg h3]

/-- `Ř` at sites `j, k` is `1 ⊗ Ř` at sites `i, j, k`. -/
theorem embedPair_eq_embedTriple_right (hij : i ≠ j) (hik : i ≠ k)
    (N : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    embedPair j k N
      = embedTriple i j k
          (Matrix.of fun u v => (if u.1 = v.1 then 1 else 0)
            * N (u.2.1, u.2.2) (v.2.1, v.2.2)) := by
  classical
  ext a b
  rw [embedPair_apply, embedTriple_apply]
  by_cases hi : a i = b i
  · by_cases h3 : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
    · rw [if_pos h3, if_pos (fun m hmj hmk => by
        by_cases hmi : m = i
        · subst hmi; exact hi
        · exact h3 m hmi hmj hmk)]
      simp [hi]
    · rw [if_neg h3, if_neg (fun h2 => h3 (fun m _ hmj hmk => h2 m hmj hmk))]
  · rw [if_neg (fun h2 => hi (h2 i hij hik))]
    by_cases h3 : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
    · rw [if_pos h3]; simp [hi]
    · rw [if_neg h3]

/-- **The braid relation at general `n`.** `Ř_{ij} Ř_{jk} Ř_{ij} = Ř_{jk} Ř_{ij} Ř_{jk}` for
three distinct sites — `yangBaxter` transported through the three-site embedding, with no
new matrix computation. -/
theorem braidAt_braid (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) (hqi : q * qi = 1) :
    braidAt q qi i j * braidAt q qi j k * braidAt q qi i j
      = braidAt q qi j k * braidAt q qi i j * braidAt q qi j k := by
  have h1 : braidAt q qi i j = embedTriple i j k (rc1 q qi) :=
    embedPair_eq_embedTriple_left hik hjk _
  have h2 : braidAt q qi j k = embedTriple i j k (rc2 q qi) :=
    embedPair_eq_embedTriple_right hij hik _
  rw [h1, h2, embedTriple_mul hij hik hjk, embedTriple_mul hij hik hjk,
    embedTriple_mul hij hik hjk, embedTriple_mul hij hik hjk, yangBaxter q qi hqi]

end Sites

/-! ## The Hecke action of `H_{m+1}(q)` on `V^{⊗(m+1)}`

All three defining families now hold at general `n`, so `liftBalanced` assembles them into
an algebra map. Strand `a` braids sites `a` and `a+1`. -/

section Action

variable {m : ℕ}

/-- The type-`A` Coxeter matrix on `m` generators: adjacent strands braid (`3`), distant
ones commute (`2`). -/
def coxA (m : ℕ) : Fin m → Fin m → ℕ := fun a b =>
  if a = b then 1 else if (a : ℕ) + 1 = (b : ℕ) ∨ (b : ℕ) + 1 = (a : ℕ) then 3 else 2

theorem coxA_symm : ∀ a b : Fin m, coxA m a b = coxA m b a := by
  intro a b
  unfold coxA
  by_cases hab : a = b
  · subst hab; rfl
  · rw [if_neg hab, if_neg (Ne.symm hab)]
    by_cases h : (a : ℕ) + 1 = (b : ℕ) ∨ (b : ℕ) + 1 = (a : ℕ)
    · rw [if_pos h, if_pos h.symm]
    · rw [if_neg h, if_neg (fun hc => h hc.symm)]

/-- The braiding of strand `a`: `Ř` acting at sites `a` and `a+1` of `V^{⊗(m+1)}`. -/
def strandBraid (q qi : R) (a : Fin m) :
    Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  braidAt q qi a.castSucc a.succ

private theorem cs_ne_succ (a : Fin m) : a.castSucc ≠ a.succ := by
  simp [Fin.ext_iff]

/-- **The Hecke action.** `H_{m+1}(q) → End(V^{⊗(m+1)})`, sending the balanced generator
`σ_a` to the braiding of strand `a`.

All three obligations are discharged by the general-`n` relations above: the quadratic by
`isHeckeGenerator_braidAt`, the braid relation by `braidAt_braid`, far commutation by
`braidAt_commute`. -/
noncomputable def heckeActionN (hqi : q * qi = 1) :
    QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q →ₐ[R]
      Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  QOU.IwahoriHecke.Balanced.liftBalanced hqi (strandBraid q qi)
    (fun a => isHeckeGenerator_braidAt q qi (cs_ne_succ a) hqi)
    (fun a b => by
      by_cases hab : a = b
      · -- both sides are literally the same term once `a = b`
        subst hab; rfl
      · have hba : b ≠ a := Ne.symm hab
        have hne : (a : ℕ) ≠ (b : ℕ) := fun hc => hab (Fin.ext_iff.mpr hc)
        by_cases hadj : (a : ℕ) + 1 = (b : ℕ) ∨ (b : ℕ) + 1 = (a : ℕ)
        · rw [show coxA m a b = 3 from by simp [coxA, hab, hadj],
            show coxA m b a = 3 from by simp [coxA, hba, hadj.symm],
            QOU.MathlibExt.IwahoriHecke.altProd_three,
            QOU.MathlibExt.IwahoriHecke.altProd_three]
          rcases hadj with h | h
          · have hjk : a.succ = b.castSucc := by simp [Fin.ext_iff, h]
            have e := braidAt_braid (R := R) q qi (i := a.castSucc) (j := a.succ)
              (k := b.succ) (by simp [Fin.ext_iff])
              (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega) hqi
            simp only [strandBraid, ← hjk]
            rw [← mul_assoc, ← mul_assoc]
            exact e
          · have hjk : b.succ = a.castSucc := by simp [Fin.ext_iff, h]
            have e := braidAt_braid (R := R) q qi (i := b.castSucc) (j := b.succ)
              (k := a.succ) (by simp [Fin.ext_iff])
              (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega) hqi
            simp only [strandBraid, ← hjk]
            rw [← mul_assoc, ← mul_assoc]
            exact e.symm
        · have hadj' : ¬((b : ℕ) + 1 = (a : ℕ) ∨ (a : ℕ) + 1 = (b : ℕ)) :=
            fun hc => hadj hc.symm
          rw [show coxA m a b = 2 from by simp [coxA, hab, hadj],
            show coxA m b a = 2 from by simp [coxA, hba, hadj'],
            QOU.MathlibExt.IwahoriHecke.altProd_two,
            QOU.MathlibExt.IwahoriHecke.altProd_two]
          exact braidAt_commute q qi (cs_ne_succ a) (cs_ne_succ b)
            (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega)
            (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega))
    coxA_symm

@[simp] theorem heckeActionN_sigma (hqi : q * qi = 1) (a : Fin m) :
    heckeActionN q qi hqi (QOU.IwahoriHecke.Balanced.sigma (coxA m) q qi a)
      = strandBraid q qi a :=
  QOU.IwahoriHecke.Balanced.liftBalanced_sigma hqi _ _ _ coxA_symm a

/-! ### On the genuine `PiTensorProduct`

The action above lives in the coordinate model `V^{⊗n} = ((Fin n → Fin 2) → R)`.
`QOU.MassTheory.monoEquiv` identifies that with `⨂[R] _ : Fin n, (Fin 2 → R)` — the
monomial basis Mathlib does not supply — so the action transports along it. -/

/-- **The Hecke action on the genuine tensor power.** `H_{m+1}(q)` acting on
`⨂[R] _ : Fin (m+1), (Fin 2 → R)` by `R`-linear endomorphisms, obtained from
`heckeActionN` by reading matrices as linear maps and conjugating along `monoEquiv`.

Both steps are algebra *equivalences*, so nothing is lost: this is the same action, stated
about the object the corpus's other tensor-power results (`TensorPowerTrace`,
`WeightedPermutationCharacter`) are stated about. -/
noncomputable def heckeActionTensor (hqi : q * qi = 1) :
    QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q →ₐ[R]
      Module.End R (⨂[R] _ : Fin (m + 1), (Fin 2 → R)) :=
  AlgHom.comp
    (AlgEquiv.toAlgHom
      ((QOU.MassTheory.monoEquiv (R := R) (α := Fin (m + 1)) (κ := Fin 2)).symm.algConj R))
    (AlgHom.comp (AlgEquiv.toAlgHom Matrix.toLinAlgEquiv') (heckeActionN q qi hqi))

@[simp] theorem heckeActionTensor_sigma (hqi : q * qi = 1) (a : Fin m) :
    heckeActionTensor q qi hqi (QOU.IwahoriHecke.Balanced.sigma (coxA m) q qi a)
      = ((QOU.MassTheory.monoEquiv (R := R) (α := Fin (m + 1)) (κ := Fin 2)).symm.algConj R)
          (Matrix.toLinAlgEquiv' (strandBraid q qi a)) := by
  simp [heckeActionTensor]

end Action

/-! ## What `heckeActionN` does NOT say

The three relations and the action are proved at every `n`. Four things are still open, and
none of them follows from what is here:

1. **Nothing about the image.** `heckeActionN` is an algebra map. That it is *surjective
   onto the commutant* of the quantum-group action — the Schur–Weyl statement proper, and
   the reason one wants this map — is **not proved here**.

   🛑 **And injectivity is not an open question: at this fibre it is FALSE.** An earlier
   version of this note said injectivity "would need the `T_w` basis
   (`QOU.IwahoriHecke.Tw`, still open on Matsumoto)", which framed it as a theorem awaiting
   machinery. `q`-Schur–Weyl `H_n(q) → End_{U_q𝔰𝔩_N}(V^{⊗n})` is injective only when
   `N ≥ n`, and item 2 fixes `N = 2`. So for `n ≥ 3` the map has a kernel — spanned by the
   blocks with more than two rows, i.e. `ker(H_n ↠ TL_n)`, of dimension `n! − Catalan(n)`:
   `1, 10, 78, 588, 4611, 38890` at `n = 3 … 8`. `heckeActionN` is therefore already
   non-injective at `m = 2`, and so was the `H₃(q)` action of `RMatrixSl2`.

   Matsumoto would buy the *basis* of `H_n(q)`, which is worth having; it cannot make a map
   with a nontrivial kernel injective, so it is not what stands between this file and
   injectivity. Note also that at `N = 2` "surjective onto the commutant" and "not
   injective" are two faces of one fact, the image being `TL_n(q)`.

   **None of that is proved here either** — it is the standard statement, and the corpus
   records the same kernel dimensions at
   [`wedderburn_jones_markov.py`](../../../../computations/wedderburn_jones_markov.py) off
   the sorry-free `QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`. Recorded because
   the earlier wording pointed future work at the wrong obstruction. Raised by a sibling
   session on PR #6817; the kernel dimensions were re-derived here from the hook-length
   formula before the correction was made.
2. **Fibre `Fin 2` only.** The general `gl_k` R-matrix
   `Ř = q Σ_i E_ii⊗E_ii + Σ_{i≠j} E_ji⊗E_ij + (q − q⁻¹) Σ_{i<j} E_ii⊗E_jj`
   satisfies the same relations for any linearly ordered fibre; only `sl₂` is done, because
   `Fin 2` is the fibre every consumer in this corpus uses.
3. **No trace.** The `q`-deformed character of
   `QOU.MassTheory.WeightedPermutationCharacter` is the trace-weight half of quantum
   Schur–Weyl; nothing here connects the braiding to it, and the Markov trace on `H_n(q)` is
   still `opaque` in `QOU.IwahoriHecke.MarkovTrace`.

All three are mathematics. The one item on this list that was mere bookkeeping — that the
action lived in the coordinate model rather than on `PiTensorProduct` — is closed by
`heckeActionTensor`. -/

end QOU.IwahoriHecke.TensorEmbed
