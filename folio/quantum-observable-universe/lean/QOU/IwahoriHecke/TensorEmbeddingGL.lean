/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.IwahoriHecke.TensorEmbedding
import Mathlib.Tactic.Module
import Mathlib.Tactic.LinearCombination

/-!
# The Jimbo `Ř`-matrix action of `H_{m+1}(q)` on `(R^N)^{⊗(m+1)}`, every `N`

`QOU.IwahoriHecke.TensorEmbed.heckeActionN` is the dimension-2 (`U_q(sl₂)`) action in the
coordinate model `V^{⊗n} = ((Fin n → Fin 2) → R)`.  This file is the same construction for the
vector representation of `U_q(gl_N)`, `V = R^N`, in the model `((Fin n → Fin d) → R)`:

* `rCheckN` — Jimbo's `gl_N` R-matrix, with the convention of `RMatrix.rCheck` and of
  `QOU.OrientedSkein.Model.GLnRMatrix.rv` (the `q − qi` term on the increasing pair):
  `Ř(e_i ⊗ e_i) = q e_i ⊗ e_i`, `Ř(e_i ⊗ e_j) = e_j ⊗ e_i + (q − qi) e_i ⊗ e_j` for `i < j`,
  `Ř(e_i ⊗ e_j) = e_j ⊗ e_i` for `i > j`.
* `rCheckN_sq` — the Hecke quadratic `Ř² = (q − qi)Ř + 1`;
* `yangBaxterN` — `Ř₁Ř₂Ř₁ = Ř₂Ř₁Ř₂` on `V^{⊗3}`.  Proved column by column: each side is applied
  to a basis vector `δ_{(a,b,c)}`, and the computation splits on the relative order of `a, b, c`
  (the same thirteen cases as `GLnRMatrix.braid`, which proves the relation in `ModuleCat`).
  Only `q * qi = 1` is used.
* `embedPair`, `embedTriple`, `braidAt`, … — the site embeddings of `TensorEmbedding`, with the
  fibre `Fin 2` replaced by `Fin d`.  Their proofs never used `2`; they are restated here rather
  than generalised in place so that no consumer of the dimension-2 file moves.
* `heckeActionGL` — the algebra map `BalancedHecke (coxA m) q →ₐ End((R^N)^{⊗(m+1)})`.

## Base ring (§7c)

Generic `[CommRing R]`, `q * qi = 1`.  The order on `Fin d` is used only to place the `q − qi`
term; nothing archimedean appears.

-- Ref: [jimbo1986] M. Jimbo, *A q-analogue of U(gl(N+1)), Hecke algebra, and the Yang–Baxter
--   equation*, Lett. Math. Phys. 11 (1986) 247–252.
-/

namespace QOU.IwahoriHecke.TensorEmbedGL

open QOU.MathlibExt.SkeinRelation Matrix

variable {R : Type*} [CommRing R] {d : ℕ}

section RMatrix

/-- **Jimbo's `gl_N` `Ř`-matrix** on `V ⊗ V`, `V = Fin d → R`. -/
def rCheckN (q qi : R) : Matrix (Fin d × Fin d) (Fin d × Fin d) R :=
  Matrix.of fun a b =>
    if a = b then (if b.1 = b.2 then q else if b.1 < b.2 then q - qi else 0)
    else if a = (b.2, b.1) then 1 else 0

variable (q qi : R)

@[simp] theorem rCheckN_apply (a b : Fin d × Fin d) :
    rCheckN q qi a b
      = if a = b then (if b.1 = b.2 then q else if b.1 < b.2 then q - qi else 0)
        else if a = (b.2, b.1) then 1 else 0 := rfl

/-- The basis vector `δ_v`. -/
abbrev δ {ι : Type*} [DecidableEq ι] (v : ι) : ι → R := Pi.single v 1

theorem col_apply (b u : Fin d × Fin d) : (rCheckN q qi *ᵥ δ b) u = rCheckN q qi u b := by
  simp [mulVec_single, δ]

theorem col_self (i : Fin d) : rCheckN q qi *ᵥ δ (i, i) = q • δ (R := R) (i, i) := by
  funext u
  rw [col_apply, rCheckN_apply, Pi.smul_apply, smul_eq_mul, δ, Pi.single_apply]
  by_cases h1 : u = (i, i) <;> simp [h1]

theorem col_lt {i j : Fin d} (h : i < j) :
    rCheckN q qi *ᵥ δ (i, j) = δ (j, i) + (q - qi) • δ (R := R) (i, j) := by
  have hne : i ≠ j := h.ne
  funext u
  rw [col_apply, rCheckN_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul, δ, δ,
    Pi.single_apply, Pi.single_apply]
  by_cases h1 : u = (i, j)
  · subst h1; simp [hne, h, Prod.ext_iff]
  · by_cases h2 : u = (j, i)
    · subst h2; simp [hne, h, Prod.ext_iff, Ne.symm hne]
    · simp [h1, h2]

theorem col_gt {i j : Fin d} (h : j < i) : rCheckN q qi *ᵥ δ (i, j) = δ (R := R) (j, i) := by
  have hne : i ≠ j := h.ne'
  funext u
  rw [col_apply, rCheckN_apply, δ, Pi.single_apply]
  by_cases h1 : u = (i, j)
  · subst h1; simp [hne, Prod.ext_iff, not_lt.mpr h.le]
  · by_cases h2 : u = (j, i)
    · subst h2; simp [hne, Prod.ext_iff, Ne.symm hne]
    · simp [h1, h2]

/-- Two matrices agree if they agree on every basis vector. -/
theorem ext_col {ι : Type*} [Fintype ι] [DecidableEq ι] {A B : Matrix ι ι R}
    (h : ∀ v : ι, A *ᵥ δ v = B *ᵥ δ v) : A = B := by
  ext i j
  have := congrFun (h j) i
  simpa [mulVec_single] using this

/-- Decide an order (in)equality between elements of `Fin d` from the hypotheses. -/
macro "fin_omega" : tactic =>
  `(tactic| (simp only [Fin.lt_iff_val_lt_val, Fin.ext_iff] at *; omega))

/-- **The Hecke quadratic** `Ř² = (q − qi) Ř + 1`. -/
theorem rCheckN_sq (hqi : q * qi = 1) :
    rCheckN (d := d) q qi * rCheckN q qi = (q - qi) • rCheckN q qi + 1 := by
  apply ext_col
  rintro ⟨i, j⟩
  rw [← mulVec_mulVec, add_mulVec, smul_mulVec, one_mulVec]
  rcases lt_trichotomy i j with h | rfl | h
  · rw [col_lt q qi h, mulVec_add, mulVec_smul, col_gt q qi h, col_lt q qi h]
    match_scalars <;> first | ring1 | linear_combination hqi | linear_combination -hqi
  · rw [col_self, mulVec_smul, col_self]
    match_scalars <;> first | ring1 | linear_combination hqi | linear_combination -hqi
  · rw [col_gt q qi h, col_lt q qi h]
    match_scalars <;> first | ring1 | linear_combination hqi | linear_combination -hqi

theorem isHeckeGenerator_rCheckN (hqi : q * qi = 1) :
    IsHeckeGenerator q qi (rCheckN (d := d) q qi) := by
  show rCheckN q qi * rCheckN q qi = algebraMap R _ (q - qi) * rCheckN q qi + 1
  rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  exact rCheckN_sq q qi hqi

/-- `Ř₁ = Ř ⊗ id` on `V^{⊗3}`. -/
def rc1N (q qi : R) : Matrix (Fin d × Fin d × Fin d) (Fin d × Fin d × Fin d) R :=
  Matrix.of fun a b => rCheckN q qi (a.1, a.2.1) (b.1, b.2.1) * (if a.2.2 = b.2.2 then 1 else 0)

/-- `Ř₂ = id ⊗ Ř` on `V^{⊗3}`. -/
def rc2N (q qi : R) : Matrix (Fin d × Fin d × Fin d) (Fin d × Fin d × Fin d) R :=
  Matrix.of fun a b => (if a.1 = b.1 then 1 else 0) * rCheckN q qi (a.2.1, a.2.2) (b.2.1, b.2.2)

theorem rc1N_col (i j c : Fin d) :
    rc1N q qi *ᵥ δ (i, j, c)
      = fun u => (rCheckN q qi *ᵥ δ (i, j)) (u.1, u.2.1) * δ (R := R) c u.2.2 := by
  funext u
  rw [col_apply]
  simp [mulVec_single, rc1N, δ, Pi.single_apply, eq_comm]

theorem rc2N_col (a i j : Fin d) :
    rc2N q qi *ᵥ δ (a, i, j)
      = fun u => δ (R := R) a u.1 * (rCheckN q qi *ᵥ δ (i, j)) (u.2.1, u.2.2) := by
  funext u
  rw [col_apply]
  simp [mulVec_single, rc2N, δ, Pi.single_apply, eq_comm]

theorem tens1 (x y c : Fin d) :
    (fun u : Fin d × Fin d × Fin d => δ (R := R) (x, y) (u.1, u.2.1) * δ c u.2.2)
      = δ (x, y, c) := by
  funext u; rcases u with ⟨a, b, w⟩
  simp only [δ, Pi.single_apply, Prod.ext_iff]
  by_cases h1 : a = x <;> by_cases h2 : b = y <;> by_cases h3 : w = c <;> simp [h1, h2, h3]

theorem tens2 (a x y : Fin d) :
    (fun u : Fin d × Fin d × Fin d => δ (R := R) a u.1 * δ (x, y) (u.2.1, u.2.2))
      = δ (a, x, y) := by
  funext u; rcases u with ⟨b, c, w⟩
  simp only [δ, Pi.single_apply, Prod.ext_iff]
  by_cases h1 : b = a <;> by_cases h2 : c = x <;> by_cases h3 : w = y <;> simp [h1, h2, h3]

theorem c1_self (i c : Fin d) : rc1N q qi *ᵥ δ (i, i, c) = q • δ (R := R) (i, i, c) := by
  rw [rc1N_col, col_self, ← tens1]; funext u; simp [mul_assoc]

theorem c1_lt {i j : Fin d} (c : Fin d) (h : i < j) :
    rc1N q qi *ᵥ δ (i, j, c) = δ (j, i, c) + (q - qi) • δ (R := R) (i, j, c) := by
  rw [rc1N_col, col_lt q qi h, ← tens1, ← tens1]; funext u; simp; ring

theorem c1_gt {i j : Fin d} (c : Fin d) (h : j < i) :
    rc1N q qi *ᵥ δ (i, j, c) = δ (R := R) (j, i, c) := by
  rw [rc1N_col, col_gt q qi h, ← tens1]

theorem c2_self (a i : Fin d) : rc2N q qi *ᵥ δ (a, i, i) = q • δ (R := R) (a, i, i) := by
  rw [rc2N_col, col_self, ← tens2]; funext u; simp; ring

theorem c2_lt {i j : Fin d} (a : Fin d) (h : i < j) :
    rc2N q qi *ᵥ δ (a, i, j) = δ (a, j, i) + (q - qi) • δ (R := R) (a, i, j) := by
  rw [rc2N_col, col_lt q qi h, ← tens2, ← tens2]; funext u; simp; ring

theorem c2_gt {i j : Fin d} (a : Fin d) (h : j < i) :
    rc2N q qi *ᵥ δ (a, i, j) = δ (R := R) (a, j, i) := by
  rw [rc2N_col, col_gt q qi h, ← tens2]

set_option maxHeartbeats 2000000 in
/-- **The Yang–Baxter equation** `Ř₁Ř₂Ř₁ = Ř₂Ř₁Ř₂` on `(R^N)^{⊗3}`, every `N`. -/
theorem yangBaxterN (hqi : q * qi = 1) :
    rc1N (d := d) q qi * rc2N q qi * rc1N q qi = rc2N q qi * rc1N q qi * rc2N q qi := by
  apply ext_col
  rintro ⟨a, b, c⟩
  simp only [← mulVec_mulVec]
  rcases lt_trichotomy a b with h1 | h1 | h1 <;> rcases lt_trichotomy b c with h2 | h2 | h2 <;>
    rcases lt_trichotomy a c with h3 | h3 | h3 <;> (try subst_vars) <;>
    (try (exfalso; fin_omega)) <;>
    simp (disch := fin_omega) only [c1_self, c1_lt, c1_gt, c2_self, c2_lt, c2_gt, mulVec_add,
      mulVec_smul, smul_add, smul_smul] <;>
    match_scalars <;>
    first | ring1 | linear_combination (q - qi) * hqi | linear_combination (qi - q) * hqi | linear_combination hqi | linear_combination -hqi

end RMatrix

variable (q qi : R)

section Sites

variable {n : ℕ}

/-- A two-site operator acting at sites `i` and `j` of `V^{⊗n}` and trivially elsewhere. -/
def embedPair (i j : Fin n) (M : Matrix (Fin d × Fin d) (Fin d × Fin d) R) :
    Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  Matrix.of fun a b =>
    if (∀ k, k ≠ i → k ≠ j → a k = b k) then M (a i, a j) (b i, b j) else 0

theorem embedPair_apply (i j : Fin n) (M : Matrix (Fin d × Fin d) (Fin d × Fin d) R)
    (a b : Fin n → Fin d) :
    embedPair i j M a b
      = if (∀ k, k ≠ i → k ≠ j → a k = b k) then M (a i, a j) (b i, b j) else 0 := rfl

/-- **The two free sites parametrise the states agreeing with `a` elsewhere.** Fixing a
reference state `a`, the assignments to sites `i ≠ j` biject with the states that agree with
`a` off `{i, j}`. This is the one combinatorial fact the site-indexed calculus needs; every
sum below collapses along it from `2^n` terms to `4`. -/
def pairEquiv {i j : Fin n} (hij : i ≠ j) (a : Fin n → Fin d) :
    (Fin d × Fin d) ≃ {c : Fin n → Fin d // ∀ k, k ≠ i → k ≠ j → a k = c k} where
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
theorem sum_collapse {i j : Fin n} (hij : i ≠ j) (a : Fin n → Fin d)
    (F : (Fin n → Fin d) → R)
    (hF : ∀ c, ¬(∀ k, k ≠ i → k ≠ j → a k = c k) → F c = 0) :
    ∑ c, F c
      = ∑ x : Fin d × Fin d, F (Function.update (Function.update a i x.1) j x.2) := by
  classical
  rw [← Finset.sum_filter_of_ne (p := fun c => ∀ k, k ≠ i → k ≠ j → a k = c k)
        (fun c _ hc => by by_contra h; exact hc (hF c h))]
  rw [Finset.sum_subtype _ (fun c => by simp)
        (f := F) (p := fun c => ∀ k, k ≠ i → k ≠ j → a k = c k)]
  exact (Fintype.sum_equiv (pairEquiv hij a) _ _ (fun _ => rfl)).symm

/-! ### The site-indexed embedding is an algebra map -/

variable {i j : Fin n}

private theorem update_left (hij : i ≠ j) (a : Fin n → Fin d) (x : Fin d × Fin d) :
    Function.update (Function.update a i x.1) j x.2 i = x.1 := by
  rw [Function.update_of_ne hij, Function.update_self]

private theorem update_right (a : Fin n → Fin d) (x : Fin d × Fin d) :
    Function.update (Function.update a i x.1) j x.2 j = x.2 := Function.update_self ..

private theorem update_agrees (a : Fin n → Fin d) (x : Fin d × Fin d) :
    ∀ k, k ≠ i → k ≠ j → a k = Function.update (Function.update a i x.1) j x.2 k := by
  intro k hki hkj
  rw [Function.update_of_ne hkj, Function.update_of_ne hki]

/-- The embedded operator's entry from `a` to a state differing only at the two sites. -/
theorem embedPair_apply_update (hij : i ≠ j) (M : Matrix (Fin d × Fin d) (Fin d × Fin d) R)
    (a : Fin n → Fin d) (x : Fin d × Fin d) :
    embedPair i j M a (Function.update (Function.update a i x.1) j x.2) = M (a i, a j) x := by
  rw [embedPair_apply, if_pos (update_agrees a x), update_left hij, update_right]

/-- The embedded operator's entry from such a state to an arbitrary `b`: the off-window
condition is unchanged by the update, so it is `a`'s own condition. -/
theorem embedPair_update_apply (hij : i ≠ j) (N : Matrix (Fin d × Fin d) (Fin d × Fin d) R)
    (a b : Fin n → Fin d) (x : Fin d × Fin d) :
    embedPair i j N (Function.update (Function.update a i x.1) j x.2) b
      = if (∀ k, k ≠ i → k ≠ j → a k = b k) then N x (b i, b j) else 0 := by
  rw [embedPair_apply, update_left hij, update_right]
  congr 1
  refine propext ⟨fun h k hki hkj => ?_, fun h k hki hkj => ?_⟩
  · rw [update_agrees a x k hki hkj]; exact h k hki hkj
  · rw [← update_agrees a x k hki hkj]; exact h k hki hkj

/-- **The site-indexed embedding is multiplicative.** The `2^n`-term sum collapses to the
four assignments to the two sites, which is exactly the matrix product on the window. -/
theorem embedPair_mul (hij : i ≠ j) (M N : Matrix (Fin d × Fin d) (Fin d × Fin d) R) :
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
    embedPair i j (1 : Matrix (Fin d × Fin d) (Fin d × Fin d) R) = 1 := by
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

theorem embedPair_add (M N : Matrix (Fin d × Fin d) (Fin d × Fin d) R) :
    embedPair i j (M + N) = embedPair (R := R) i j M + embedPair i j N := by
  ext a b; simp only [embedPair_apply, Matrix.add_apply]; split_ifs <;> simp

theorem embedPair_smul (c : R) (M : Matrix (Fin d × Fin d) (Fin d × Fin d) R) :
    embedPair i j (c • M) = c • embedPair (R := R) i j M := by
  ext a b
  simp only [embedPair_apply, Matrix.smul_apply, smul_eq_mul]
  split_ifs <;> simp

theorem embedPair_algebraMap (hij : i ≠ j) (r : R) :
    embedPair i j (algebraMap R (Matrix (Fin d × Fin d) (Fin d × Fin d) R) r)
      = algebraMap R (Matrix (Fin n → Fin d) (Fin n → Fin d) R) r := by
  rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one, embedPair_smul,
    embedPair_one (R := R) hij]

/-- **`M ↦ M` at sites `i ≠ j` is an algebra map** `End(V ⊗ V) → End(V^{⊗n})`. -/
def embedPairHom (hij : i ≠ j) :
    Matrix (Fin d × Fin d) (Fin d × Fin d) R →ₐ[R]
      Matrix (Fin n → Fin d) (Fin n → Fin d) R where
  toFun := embedPair i j
  map_one' := embedPair_one hij
  map_mul' _ _ := (embedPair_mul hij _ _).symm
  map_zero' := by ext a b; simp only [embedPair_apply, Matrix.zero_apply]; split_ifs <;> rfl
  map_add' _ _ := embedPair_add _ _
  commutes' := embedPair_algebraMap hij

@[simp] theorem embedPairHom_apply (hij : i ≠ j)
    (M : Matrix (Fin d × Fin d) (Fin d × Fin d) R) :
    embedPairHom (R := R) hij M = embedPair i j M := rfl

/-- **The braiding at two sites of `V^{⊗n}`.** For any `n` and any two distinct sites. -/
def braidAt (q qi : R) (i j : Fin n) : Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  embedPair i j (rCheckN q qi)

/-- **The general-`n` result.** At any number of tensor factors and any two distinct sites,
the embedded R-matrix is a §7a Hecke generator: `Ř_{ij}² = (q − qi) Ř_{ij} + 1`. So it is
invertible, satisfies the skein relation, and factors with eigenvalues `q` and `−qi` — all
inherited through `embedPairHom` at no extra cost. -/
theorem isHeckeGenerator_braidAt (hij : i ≠ j) (hqi : q * qi = 1) :
    IsHeckeGenerator q qi (braidAt (d := d) q qi i j) :=
  QOU.IwahoriHecke.TensorEmbed.IsHeckeGenerator.map (embedPairHom (R := R) hij) (isHeckeGenerator_rCheckN q qi hqi)

/-- Consequently the braiding at any two sites of `V^{⊗n}` is invertible. -/
theorem isUnit_braidAt (hij : i ≠ j) (hqi : q * qi = 1) : IsUnit (braidAt (d := d) q qi i j) :=
  isUnit_of_isHeckeGenerator (isHeckeGenerator_braidAt q qi hij hqi)

/-- And satisfies the skein relation `Ř_{ij} − Ř_{ij}⁻¹ = q − qi`. -/
theorem braidAt_sub_inv (hij : i ≠ j) (hqi : q * qi = 1)
    {S : Matrix (Fin n → Fin d) (Fin n → Fin d) R} (hS : braidAt (d := d) q qi i j * S = 1) :
    braidAt (d := d) q qi i j - S = algebraMap R _ (q - qi) :=
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
    (hli : l ≠ i) (hlj : l ≠ j) (a b : Fin n → Fin d) (x : Fin d × Fin d) :
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
    (M N : Matrix (Fin d × Fin d) (Fin d × Fin d) R) (a b : Fin n → Fin d) :
    (embedPair i j M * embedPair k l N) a b
      = if (∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m)
        then M (a i, a j) (b i, b j) * N (a k, a l) (b k, b l) else 0 := by
  classical
  rw [Matrix.mul_apply,
    sum_collapse hij a (fun c => embedPair i j M a c * embedPair k l N c b)
      (fun c hc => by dsimp only; rw [embedPair_apply, if_neg hc, zero_mul])]
  have hval : ∀ x : Fin d × Fin d,
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
    (hli : l ≠ i) (hlj : l ≠ j) (M N : Matrix (Fin d × Fin d) (Fin d × Fin d) R) :
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
    braidAt (d := d) q qi i j * braidAt (d := d) q qi k l = braidAt (d := d) q qi k l * braidAt (d := d) q qi i j :=
  embedPair_commute hij hkl hki hkj hli hlj _ _

/-! ### Three sites, and the braid relation at general `n`

Far commutation needed only the two-site collapse because its pairs are disjoint. The braid
relation's three factors overlap, so the intermediate states range over three sites at once.
This section builds the three-site embedding, shows the two-site one factors through it, and
then the braid relation is `yangBaxter` transported — no new matrix computation. -/

variable {m₃ : Fin n}

/-- A three-site operator acting at `i`, `j`, `k` and trivially elsewhere. -/
def embedTriple (i j k : Fin n)
    (M : Matrix (Fin d × Fin d × Fin d) (Fin d × Fin d × Fin d) R) :
    Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  Matrix.of fun a b =>
    if (∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m)
    then M (a i, a j, a k) (b i, b j, b k) else 0

theorem embedTriple_apply (i j k : Fin n)
    (M : Matrix (Fin d × Fin d × Fin d) (Fin d × Fin d × Fin d) R) (a b : Fin n → Fin d) :
    embedTriple i j k M a b
      = if (∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m)
        then M (a i, a j, a k) (b i, b j, b k) else 0 := rfl

variable {k : Fin n}

/-- The three free sites parametrise the states agreeing with `a` elsewhere. -/
def tripleEquiv (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) (a : Fin n → Fin d) :
    (Fin d × Fin d × Fin d)
      ≃ {c : Fin n → Fin d // ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m} where
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
theorem sum_collapse3 (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) (a : Fin n → Fin d)
    (F : (Fin n → Fin d) → R)
    (hF : ∀ c, ¬(∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m) → F c = 0) :
    ∑ c, F c
      = ∑ x : Fin d × Fin d × Fin d,
          F (Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2) := by
  classical
  rw [← Finset.sum_filter_of_ne (p := fun c => ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m)
        (fun c _ hc => by by_contra h; exact hc (hF c h))]
  rw [Finset.sum_subtype _ (fun c => by simp)
        (f := F) (p := fun c => ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m)]
  exact (Fintype.sum_equiv (tripleEquiv hij hik hjk a) _ _ (fun _ => rfl)).symm

private theorem upd3_i (hij : i ≠ j) (hik : i ≠ k) (a : Fin n → Fin d)
    (x : Fin d × Fin d × Fin d) :
    Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 i = x.1 := by
  rw [Function.update_of_ne hik, Function.update_of_ne hij, Function.update_self]

private theorem upd3_j (hjk : j ≠ k) (a : Fin n → Fin d) (x : Fin d × Fin d × Fin d) :
    Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 j = x.2.1 := by
  rw [Function.update_of_ne hjk, Function.update_self]

private theorem upd3_k (a : Fin n → Fin d) (x : Fin d × Fin d × Fin d) :
    Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 k = x.2.2 :=
  Function.update_self ..

private theorem upd3_agrees (a : Fin n → Fin d) (x : Fin d × Fin d × Fin d) :
    ∀ m, m ≠ i → m ≠ j → m ≠ k →
      a m = Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2 m := by
  intro m hmi hmj hmk
  rw [Function.update_of_ne hmk, Function.update_of_ne hmj, Function.update_of_ne hmi]

theorem embedTriple_apply_update (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k)
    (M : Matrix (Fin d × Fin d × Fin d) (Fin d × Fin d × Fin d) R)
    (a : Fin n → Fin d) (x : Fin d × Fin d × Fin d) :
    embedTriple i j k M a
        (Function.update (Function.update (Function.update a i x.1) j x.2.1) k x.2.2)
      = M (a i, a j, a k) x := by
  rw [embedTriple_apply, if_pos (upd3_agrees a x), upd3_i hij hik, upd3_j hjk, upd3_k]

theorem embedTriple_update_apply (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k)
    (N : Matrix (Fin d × Fin d × Fin d) (Fin d × Fin d × Fin d) R)
    (a b : Fin n → Fin d) (x : Fin d × Fin d × Fin d) :
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
    (M N : Matrix (Fin d × Fin d × Fin d) (Fin d × Fin d × Fin d) R) :
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
    (M : Matrix (Fin d × Fin d) (Fin d × Fin d) R) :
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
    (N : Matrix (Fin d × Fin d) (Fin d × Fin d) R) :
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
    braidAt (d := d) q qi i j * braidAt (d := d) q qi j k * braidAt (d := d) q qi i j
      = braidAt (d := d) q qi j k * braidAt (d := d) q qi i j * braidAt (d := d) q qi j k := by
  have h1 : braidAt (d := d) q qi i j = embedTriple i j k (rc1N q qi) :=
    embedPair_eq_embedTriple_left hik hjk _
  have h2 : braidAt (d := d) q qi j k = embedTriple i j k (rc2N q qi) :=
    embedPair_eq_embedTriple_right hij hik _
  rw [h1, h2, embedTriple_mul hij hik hjk, embedTriple_mul hij hik hjk,
    embedTriple_mul hij hik hjk, embedTriple_mul hij hik hjk, yangBaxterN q qi hqi]

end Sites

/-! ## The Hecke action of `H_{m+1}(q)` on `V^{⊗(m+1)}`

All three defining families now hold at general `n`, so `liftBalanced` assembles them into
an algebra map. Strand `a` braids sites `a` and `a+1`. -/

section Action

variable {m : ℕ}

/-- The braiding of strand `a`: `Ř` acting at sites `a` and `a+1` of `V^{⊗(m+1)}`. -/
def strandBraid (q qi : R) (a : Fin m) :
    Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) R :=
  braidAt (d := d) q qi a.castSucc a.succ

private theorem cs_ne_succ (a : Fin m) : a.castSucc ≠ a.succ := by
  simp [Fin.ext_iff]

/-- **The Hecke action.** `H_{m+1}(q) → End(V^{⊗(m+1)})`, sending the balanced generator
`σ_a` to the braiding of strand `a`.

All three obligations are discharged by the general-`n` relations above: the quadratic by
`isHeckeGenerator_braidAt`, the braid relation by `braidAt_braid`, far commutation by
`braidAt_commute`. -/
noncomputable def heckeActionGL (hqi : q * qi = 1) :
    QOU.IwahoriHecke.Balanced.BalancedHecke (TensorEmbed.coxA m) q →ₐ[R]
      Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) R :=
  QOU.IwahoriHecke.Balanced.liftBalanced hqi (strandBraid q qi)
    (fun a => isHeckeGenerator_braidAt q qi (cs_ne_succ a) hqi)
    (fun a b => by
      by_cases hab : a = b
      · -- both sides are literally the same term once `a = b`
        subst hab; rfl
      · have hba : b ≠ a := Ne.symm hab
        have hne : (a : ℕ) ≠ (b : ℕ) := fun hc => hab (Fin.ext_iff.mpr hc)
        by_cases hadj : (a : ℕ) + 1 = (b : ℕ) ∨ (b : ℕ) + 1 = (a : ℕ)
        · rw [show TensorEmbed.coxA m a b = 3 from by simp [TensorEmbed.coxA, hab, hadj],
            show TensorEmbed.coxA m b a = 3 from by simp [TensorEmbed.coxA, hba, hadj.symm],
            QOU.MathlibExt.IwahoriHecke.altProd_three,
            QOU.MathlibExt.IwahoriHecke.altProd_three]
          rcases hadj with h | h
          · have hjk : a.succ = b.castSucc := by simp [Fin.ext_iff, h]
            have e := braidAt_braid (R := R) (d := d) q qi (i := a.castSucc) (j := a.succ)
              (k := b.succ) (by simp [Fin.ext_iff])
              (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega) hqi
            simp only [strandBraid, ← hjk]
            rw [← mul_assoc, ← mul_assoc]
            exact e
          · have hjk : b.succ = a.castSucc := by simp [Fin.ext_iff, h]
            have e := braidAt_braid (R := R) (d := d) q qi (i := b.castSucc) (j := b.succ)
              (k := a.succ) (by simp [Fin.ext_iff])
              (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega) hqi
            simp only [strandBraid, ← hjk]
            rw [← mul_assoc, ← mul_assoc]
            exact e.symm
        · have hadj' : ¬((b : ℕ) + 1 = (a : ℕ) ∨ (a : ℕ) + 1 = (b : ℕ)) :=
            fun hc => hadj hc.symm
          rw [show TensorEmbed.coxA m a b = 2 from by simp [TensorEmbed.coxA, hab, hadj],
            show TensorEmbed.coxA m b a = 2 from by simp [TensorEmbed.coxA, hba, hadj'],
            QOU.MathlibExt.IwahoriHecke.altProd_two,
            QOU.MathlibExt.IwahoriHecke.altProd_two]
          exact braidAt_commute q qi (cs_ne_succ a) (cs_ne_succ b)
            (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega)
            (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega))
    TensorEmbed.coxA_symm

@[simp] theorem heckeActionGL_sigma (hqi : q * qi = 1) (a : Fin m) :
    heckeActionGL (d := d) q qi hqi (QOU.IwahoriHecke.Balanced.sigma (TensorEmbed.coxA m) q qi a)
      = strandBraid (d := d) q qi a :=
  QOU.IwahoriHecke.Balanced.liftBalanced_sigma hqi _ _ _ TensorEmbed.coxA_symm a


end Action

end QOU.IwahoriHecke.TensorEmbedGL
