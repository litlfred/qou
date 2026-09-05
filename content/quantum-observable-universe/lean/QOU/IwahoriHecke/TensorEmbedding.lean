import QOU.IwahoriHecke.RMatrixSl2

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

and `braidAt_commute` is the second defining family at general `n`:

> braidings at **disjoint** pairs of sites commute — `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2`.

The engine for both is `sum_collapse`: a `2^n`-term sum whose summand is supported on the
states agreeing with `a` off `{i, j}` is a 4-term sum over the assignments to those sites.
Far commutation needs no second collapse — `sum_collapse` is applied once to each side and
both reduce to the same four-index normal form
(`embedPair_mul_apply_of_disjoint`), which is symmetric in the two pairs because the base
ring is commutative.

-- Ref: [jimbo1986]; [manuscript] bean qou-k4oq
-/

namespace QOU.IwahoriHecke.TensorEmbed

open QOU.MathlibExt.SkeinRelation QOU.IwahoriHecke.RMatrix

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

end Sites

/-! ## What is still missing for a literal `H_n(q) → End(V^{⊗n})`

Two of the three defining families now hold in the site-indexed model at general `n`:

* the **quadratic** — `isHeckeGenerator_braidAt`, every `n`, every `i ≠ j`;
* **far commutation** — `braidAt_commute`, every `n`, disjoint pairs.

The **braid relation** `Ř_{ij} Ř_{jk} Ř_{ij} = Ř_{jk} Ř_{ij} Ř_{jk}` is **not** proved at
sites. It holds at three factors (`yangBaxter`) and survives an abstract spectator
(`yangBaxter_tensorId`), but neither is transported to `Fin n → Fin 2`, so there is still
no algebra map out of `H_n(q)` for `n > 3`.

Why that one is harder than far commutation: the two pairs there are **disjoint**, so each
factor's window survives the other's update untouched and one application of `sum_collapse`
per side suffices. The braid relation's three factors **overlap** in the site `j`, so the
intermediate states range over three sites at once and the product does not factor. It
needs a genuine three-site collapse:

    sitesEquiv (s : Finset (Fin n)) (a : Fin n → Fin 2) :
        (s → Fin 2) ≃ {c : Fin n → Fin 2 // ∀ k ∉ s, a k = c k}

with `toFun x k = if h : k ∈ s then x ⟨k, h⟩ else a k`. That form is **easier** than
`pairEquiv` above, not harder: the `dite` needs no `Function.update` juggling and no
`i ≠ j` side condition, because membership in `s` already separates the cases. `pairEquiv`
should be re-derived from it rather than kept as a special case. The remaining step after
that is the reindex `({i,j,k} → Fin 2) ≃ Fin 2 × Fin 2 × Fin 2` carrying `yangBaxter` over.

Until that lands, do **not** describe this file as giving a Hecke action on `V^{⊗n}`: it
gives two relations of three at general `n`, and all three at three factors. -/

end QOU.IwahoriHecke.TensorEmbed
