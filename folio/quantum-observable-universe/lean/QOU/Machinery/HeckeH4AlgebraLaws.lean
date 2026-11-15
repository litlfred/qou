/-
# H₄(q) NF module is an algebra object — `mulNF₄`, laws, associativity, and the `H4A` Ring/Algebra wrapper

Wedderburn tranche W0 (bean `qou-308a`; design provenance: the H₄ Wedderburn
design doc §2 "The domain algebra", session scratchpad
`h4_wedderburn_iso/design.md`). Rank-4 counterpart of the merged
`HeckeH3AlgebraLaws` + `HeckeH3AlgebraInstance` pair, built on the
**subscript** 24-word NF basis of `HeckeH4StabilizationRung` (H₃ Lean basis
`[γ, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]` as prefix, then (length, canonical word)
order) — NOT the distinct `MarkovTraceH4` ASCII-basis order.

Proved here (sorry-free):

* `mulNF₄` — the full H₄(q) NF product `u·v = ∑_j v_j · (u·b_j)`, each
  `u·b_j` composing the subscript `mulσ₀/₁/₂` along the reduced word of
  `b_j`, **first letter innermost** (word `(i₀,i₁,…)` ⇒
  `mulσ_{i_last} (… (mulσ_{i₀} u))`);
* R-bilinearity, zero laws, and the unit laws for `unitNF₄ = γ`;
* the `e₄` basis vectors, `basis_decomp₄`, `mulNF₄_sum_left/right`, and
  `mulNF₄_e_right` (`u·b_j = wordAction j u` — the 24 sparse goals);
* the **structured associativity route** (no 24³ brute force): the three
  generator/product commutation identities
  `mulσₖ (u·v) = u·(v·σₖ)` (`mulσ₀_mulNF₄` / `mulσ₁_mulNF₄` /
  `mulσ₂_mulNF₄`), lifted along the right basis to **`mulNF₄_assoc`**;
* `H4A R h` — wrapper type with `AddCommGroup`, `Module R`, **`Ring`**, and
  **`Algebra R`** instances whose multiplication is the proved `mulNF₄`
  (verbatim `HeckeH3AlgebraInstance.H3A` pattern, `Fin 6 → Fin 24`).

Deliberately NOT imported: `MarkovTraceH4` (its `trM_cyclic` rests on a
cited `sorry`; keeping this file on `HeckeH4StabilizationRung` only keeps
the Wedderburn chain sorry-free by construction). Because that file shares
the `QOU.Machinery.H4` namespace, the basis/unit helpers here carry a `₄`
suffix (`e₄`, `basis_decomp₄`, …) to avoid declaration clashes with its
ASCII-basis `e`/`basis_decomp`.

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): every law below is
discharged by computation over generic `[CommRing R]` — no axiom, no
conditional class, no `native_decide`. The general-n
`HeckeBraidedPresentation` / `MarkovStabilization` classes stay OPEN (see
`HeckeH3AlgebraLaws`); this file is the concrete n = 4 algebra-object rung.
Nothing wired; `1/(8π)` stays phase-4.

Base ring (§7c): generic `[CommRing R]` throughout — no `ℝ`, no ordering,
no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeH4StabilizationRung
import Mathlib.Tactic

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

/-! ## The NF product `mulNF₄` on the subscript 24-word basis -/

/-- The full H₄(q) NF algebra product `u · v = ∑_j v_j · (u · b_j)` on the
**subscript** basis of `HeckeH4StabilizationRung`: `u · b_j` composes
`mulσ₀/₁/₂` along the reduced word of `b_j`, first letter innermost
(word `(i₀,…,i_k)` ⇒ `mulσ_{i_k} (… (mulσ_{i₀} u))`). Basis words in order:
`γ, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀, σ₂, σ₁σ₂, σ₂σ₀, σ₂σ₁, σ₀σ₁σ₂, σ₁σ₀σ₂,
σ₁σ₂σ₁, σ₂σ₀σ₁, σ₂σ₁σ₀, σ₀σ₁σ₀σ₂, σ₀σ₁σ₂σ₁, σ₁σ₀σ₂σ₁, σ₁σ₂σ₁σ₀, σ₂σ₀σ₁σ₀,
σ₀σ₁σ₀σ₂σ₁, σ₀σ₁σ₂σ₁σ₀, σ₁σ₀σ₂σ₁σ₀, σ₀σ₁σ₀σ₂σ₁σ₀`. -/
def mulNF₄ (h : R) (u v : Fin 24 → R) : Fin 24 → R := fun i =>
    v 0 * u i
  + v 1 * (mulσ₀ h u) i
  + v 2 * (mulσ₁ h u) i
  + v 3 * (mulσ₀ h (mulσ₁ h u)) i
  + v 4 * (mulσ₁ h (mulσ₀ h u)) i
  + v 5 * (mulσ₀ h (mulσ₁ h (mulσ₀ h u))) i
  + v 6 * (mulσ₂ h u) i
  + v 7 * (mulσ₂ h (mulσ₁ h u)) i
  + v 8 * (mulσ₀ h (mulσ₂ h u)) i
  + v 9 * (mulσ₁ h (mulσ₂ h u)) i
  + v 10 * (mulσ₂ h (mulσ₁ h (mulσ₀ h u))) i
  + v 11 * (mulσ₂ h (mulσ₀ h (mulσ₁ h u))) i
  + v 12 * (mulσ₁ h (mulσ₂ h (mulσ₁ h u))) i
  + v 13 * (mulσ₁ h (mulσ₀ h (mulσ₂ h u))) i
  + v 14 * (mulσ₀ h (mulσ₁ h (mulσ₂ h u))) i
  + v 15 * (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))) i
  + v 16 * (mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h u)))) i
  + v 17 * (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h u)))) i
  + v 18 * (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h u)))) i
  + v 19 * (mulσ₀ h (mulσ₁ h (mulσ₀ h (mulσ₂ h u)))) i
  + v 20 * (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u))))) i
  + v 21 * (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h u))))) i
  + v 22 * (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h u))))) i
  + v 23 * (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))))) i

/-- The right action of the `j`-th NF basis word, `u ↦ u · b_j` — the same
24 composites `mulNF₄` sums over, packaged as a function so that
`mulNF₄_e_right` and the associativity word-induction can name them. -/
def wordAction (h : R) : Fin 24 → (Fin 24 → R) → (Fin 24 → R) := ![
  fun u => u,
  fun u => mulσ₀ h u,
  fun u => mulσ₁ h u,
  fun u => mulσ₀ h (mulσ₁ h u),
  fun u => mulσ₁ h (mulσ₀ h u),
  fun u => mulσ₀ h (mulσ₁ h (mulσ₀ h u)),
  fun u => mulσ₂ h u,
  fun u => mulσ₂ h (mulσ₁ h u),
  fun u => mulσ₀ h (mulσ₂ h u),
  fun u => mulσ₁ h (mulσ₂ h u),
  fun u => mulσ₂ h (mulσ₁ h (mulσ₀ h u)),
  fun u => mulσ₂ h (mulσ₀ h (mulσ₁ h u)),
  fun u => mulσ₁ h (mulσ₂ h (mulσ₁ h u)),
  fun u => mulσ₁ h (mulσ₀ h (mulσ₂ h u)),
  fun u => mulσ₀ h (mulσ₁ h (mulσ₂ h u)),
  fun u => mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u))),
  fun u => mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h u))),
  fun u => mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h u))),
  fun u => mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h u))),
  fun u => mulσ₀ h (mulσ₁ h (mulσ₀ h (mulσ₂ h u))),
  fun u => mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))),
  fun u => mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h u)))),
  fun u => mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h u)))),
  fun u => mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))))]

/-! ## Generator linearity (subscript operators, kept opaque downstream) -/

/-- `mulσ₀` is additive. -/
theorem mulσ₀_add (h : R) (u u' : Fin 24 → R) :
    mulσ₀ h (u + u') = mulσ₀ h u + mulσ₀ h u' := by
  funext i; fin_cases i <;> simp [mulσ₀, Pi.add_apply] <;> ring

/-- `mulσ₁` is additive. -/
theorem mulσ₁_add (h : R) (u u' : Fin 24 → R) :
    mulσ₁ h (u + u') = mulσ₁ h u + mulσ₁ h u' := by
  funext i; fin_cases i <;> simp [mulσ₁, Pi.add_apply] <;> ring

/-- `mulσ₂` is additive. -/
theorem mulσ₂_add (h : R) (u u' : Fin 24 → R) :
    mulσ₂ h (u + u') = mulσ₂ h u + mulσ₂ h u' := by
  funext i; fin_cases i <;> simp [mulσ₂, Pi.add_apply] <;> ring

/-- `mulσ₀` is R-homogeneous. -/
theorem mulσ₀_smul (h c : R) (u : Fin 24 → R) :
    mulσ₀ h (c • u) = c • mulσ₀ h u := by
  funext i; fin_cases i <;> simp [mulσ₀, Pi.smul_apply, smul_eq_mul] <;> ring

/-- `mulσ₁` is R-homogeneous. -/
theorem mulσ₁_smul (h c : R) (u : Fin 24 → R) :
    mulσ₁ h (c • u) = c • mulσ₁ h u := by
  funext i; fin_cases i <;> simp [mulσ₁, Pi.smul_apply, smul_eq_mul] <;> ring

/-- `mulσ₂` is R-homogeneous. -/
theorem mulσ₂_smul (h c : R) (u : Fin 24 → R) :
    mulσ₂ h (c • u) = c • mulσ₂ h u := by
  funext i; fin_cases i <;> simp [mulσ₂, Pi.smul_apply, smul_eq_mul] <;> ring

/-- `mulσ₀` kills zero. -/
theorem mulσ₀_zero (h : R) : mulσ₀ h (0 : Fin 24 → R) = 0 := by
  funext i; fin_cases i <;> simp [mulσ₀]

/-- `mulσ₁` kills zero. -/
theorem mulσ₁_zero (h : R) : mulσ₁ h (0 : Fin 24 → R) = 0 := by
  funext i; fin_cases i <;> simp [mulσ₁]

/-- `mulσ₂` kills zero. -/
theorem mulσ₂_zero (h : R) : mulσ₂ h (0 : Fin 24 → R) = 0 := by
  funext i; fin_cases i <;> simp [mulσ₂]

/-! ## Bilinearity of `mulNF₄` (generator actions kept opaque) -/

/-- `mulNF₄` is additive in the left factor. -/
theorem mulNF₄_add_left (h : R) (u u' v : Fin 24 → R) :
    mulNF₄ h (u + u') v = mulNF₄ h u v + mulNF₄ h u' v := by
  funext i
  simp only [mulNF₄, mulσ₀_add, mulσ₁_add, mulσ₂_add, Pi.add_apply]; ring

/-- `mulNF₄` is additive in the right factor. -/
theorem mulNF₄_add_right (h : R) (u v v' : Fin 24 → R) :
    mulNF₄ h u (v + v') = mulNF₄ h u v + mulNF₄ h u v' := by
  funext i; simp only [mulNF₄, Pi.add_apply]; ring

/-- `mulNF₄` is R-homogeneous in the left factor. -/
theorem mulNF₄_smul_left (h c : R) (u v : Fin 24 → R) :
    mulNF₄ h (c • u) v = c • mulNF₄ h u v := by
  funext i
  simp only [mulNF₄, mulσ₀_smul, mulσ₁_smul, mulσ₂_smul, Pi.smul_apply,
    smul_eq_mul]
  ring

/-- `mulNF₄` is R-homogeneous in the right factor. -/
theorem mulNF₄_smul_right (h c : R) (u v : Fin 24 → R) :
    mulNF₄ h u (c • v) = c • mulNF₄ h u v := by
  funext i; simp only [mulNF₄, Pi.smul_apply, smul_eq_mul]; ring

/-- Left zero law. -/
theorem mulNF₄_zero_left (h : R) (v : Fin 24 → R) :
    mulNF₄ h (0 : Fin 24 → R) v = 0 := by
  funext i
  simp only [mulNF₄, mulσ₀_zero, mulσ₁_zero, mulσ₂_zero, Pi.zero_apply,
    mul_zero, add_zero]

/-- Right zero law. -/
theorem mulNF₄_zero_right (h : R) (u : Fin 24 → R) :
    mulNF₄ h u (0 : Fin 24 → R) = 0 := by
  funext i
  simp only [mulNF₄, Pi.zero_apply, zero_mul, add_zero]

/-! ## Unit -/

/-- The unit of the NF algebra: γ = e₀ = `![1, 0, …, 0]`. -/
def unitNF₄ : Fin 24 → R :=
  ![1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

/-- **Right unit law**: `u · γ = u` (only the `v 0` term survives). -/
theorem mulNF₄_one_right (h : R) (u : Fin 24 → R) :
    mulNF₄ h u unitNF₄ = u := by
  funext i; simp [mulNF₄, unitNF₄]

set_option maxHeartbeats 1600000 in
/-- **Left unit law**: `γ · v = v` — each basis word applied to γ reproduces
the corresponding NF basis element (`word_j(γ) = b_j`). -/
theorem mulNF₄_one_left (h : R) (v : Fin 24 → R) :
    mulNF₄ h unitNF₄ v = v := by
  funext i
  fin_cases i <;> simp [mulNF₄, unitNF₄, mulσ₀, mulσ₁, mulσ₂]

/-! ## Basis vectors and decomposition -/

/-- The `i`-th NF basis vector `e₄ i = b_i` (subscript basis; the `₄` suffix
avoids a declaration clash with the ASCII-basis `e` of `MarkovTraceH4`,
which shares this namespace). -/
def e₄ (i : Fin 24) : Fin 24 → R := Pi.single i (1 : R)

/-- Basis decomposition `u = ∑ᵢ uᵢ • e₄ i`. -/
theorem basis_decomp₄ (u : Fin 24 → R) : u = ∑ i, u i • (e₄ (R := R) i) := by
  funext j
  rw [Finset.sum_apply]
  simp [e₄, Pi.single_apply, smul_eq_mul, Finset.sum_ite_eq]

/-- `mulNF₄ · v` commutes with finite sums in the left argument. -/
theorem mulNF₄_sum_left (h : R) (s : Finset (Fin 24))
    (f : Fin 24 → (Fin 24 → R)) (v : Fin 24 → R) :
    mulNF₄ h (∑ i ∈ s, f i) v = ∑ i ∈ s, mulNF₄ h (f i) v := by
  induction s using Finset.induction with
  | empty => simp [mulNF₄_zero_left]
  | @insert a s h1 ih =>
    rw [Finset.sum_insert h1, Finset.sum_insert h1, mulNF₄_add_left, ih]

/-- `mulNF₄ w ·` commutes with finite sums in the right argument. -/
theorem mulNF₄_sum_right (h : R) (w : Fin 24 → R) (s : Finset (Fin 24))
    (f : Fin 24 → (Fin 24 → R)) :
    mulNF₄ h w (∑ j ∈ s, f j) = ∑ j ∈ s, mulNF₄ h w (f j) := by
  induction s using Finset.induction with
  | empty => exact mulNF₄_zero_right h w
  | @insert a s h1 ih =>
    rw [Finset.sum_insert h1, Finset.sum_insert h1, mulNF₄_add_right, ih]

/-- **Right basis action**: `u · b_j = wordAction j u` — the 24 sparse
goals (the coefficient vector `e₄ j` selects exactly the `j`-th composite). -/
theorem mulNF₄_e_right (h : R) (u : Fin 24 → R) (j : Fin 24) :
    mulNF₄ h u (e₄ j) = wordAction h j u := by
  fin_cases j <;> (funext i; simp [mulNF₄, e₄, wordAction])

/-- Expansion of the NF product along the right basis:
`x · w = ∑_j w_j • (x · b_j)`. -/
theorem mulNF₄_expand_right (h : R) (x w : Fin 24 → R) :
    mulNF₄ h x w = ∑ j, w j • wordAction h j x := by
  conv_lhs => rw [basis_decomp₄ w]
  rw [mulNF₄_sum_right]
  exact Finset.sum_congr rfl fun j _ => by
    rw [mulNF₄_smul_right, mulNF₄_e_right]

/-! ## The structured associativity route

Per the design (§2): (1) the three generator/product commutation identities
`mulσₖ (u·v) = u·(v·σₖ)` — each a `Fin 24` computation whose left side only
ever applies one generator table on top of the `mulNF₄` expansion (the
sparse trick that makes the `MarkovTraceH4` Gram closure feasible); (2) the
word induction over the 24 basis composites; (3) `mulNF₄_assoc` by
right-linearity. No 24³ brute force is ever elaborated. -/

set_option maxHeartbeats 3200000 in
/-- Generator commutation `(u·v)·σ₀ = u·(v·σ₀)` — the σ₀ slice of
associativity, proved by direct `Fin 24` computation. -/
theorem mulσ₀_mulNF₄ (h : R) (u v : Fin 24 → R) :
    mulσ₀ h (mulNF₄ h u v) = mulNF₄ h u (mulσ₀ h v) := by
  funext m
  fin_cases m <;> simp [mulNF₄, mulσ₀, mulσ₁, mulσ₂] <;> ring

set_option maxHeartbeats 3200000 in
/-- Generator commutation `(u·v)·σ₁ = u·(v·σ₁)` — the σ₁ slice of
associativity, proved by direct `Fin 24` computation. -/
theorem mulσ₁_mulNF₄ (h : R) (u v : Fin 24 → R) :
    mulσ₁ h (mulNF₄ h u v) = mulNF₄ h u (mulσ₁ h v) := by
  funext m
  fin_cases m <;> simp [mulNF₄, mulσ₀, mulσ₁, mulσ₂] <;> ring

set_option maxHeartbeats 3200000 in
/-- Generator commutation `(u·v)·σ₂ = u·(v·σ₂)` — the σ₂ slice of
associativity, proved by direct `Fin 24` computation. -/
theorem mulσ₂_mulNF₄ (h : R) (u v : Fin 24 → R) :
    mulσ₂ h (mulNF₄ h u v) = mulNF₄ h u (mulσ₂ h v) := by
  funext m
  fin_cases m <;> simp [mulNF₄, mulσ₀, mulσ₁, mulσ₂] <;> ring

/-- Word commutation `(u·v)·b_j = u·(v·b_j)` for every NF basis word — the
finite word induction: each of the 24 composites is a chain of the three
generator commutations. -/
theorem wordAction_mulNF₄ (h : R) (j : Fin 24) (u v : Fin 24 → R) :
    wordAction h j (mulNF₄ h u v) = mulNF₄ h u (wordAction h j v) := by
  fin_cases j <;> simp [wordAction, mulσ₀_mulNF₄, mulσ₁_mulNF₄, mulσ₂_mulNF₄]

/-- **Associativity of the full H₄(q) NF product**: `(u·v)·w = u·(v·w)` —
by right-linearity in `w` (`mulNF₄_expand_right`) and the word commutation
`wordAction_mulNF₄`. The load-bearing algebra-object law at rank 4. -/
theorem mulNF₄_assoc (h : R) (u v w : Fin 24 → R) :
    mulNF₄ h (mulNF₄ h u v) w = mulNF₄ h u (mulNF₄ h v w) := by
  rw [mulNF₄_expand_right h (mulNF₄ h u v) w, mulNF₄_expand_right h v w,
    mulNF₄_sum_right]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [mulNF₄_smul_right, wordAction_mulNF₄]

/-! ## The `H4A` wrapper: H₄(q) as a genuine `Ring`/`Algebra`

Verbatim `HeckeH3AlgebraInstance.H3A` pattern (`Fin 6 → Fin 24`,
`mulNF → mulNF₄`). -/

/-- Wrapper for the H₄(q) NF module: a distinct type carrying the `mulNF₄ h`
ring structure. The parameter `h = q − q⁻¹` pins the product. -/
@[ext]
structure H4A (R : Type*) [CommRing R] (h : R) where
  /-- NF coordinates on the subscript 24-word basis (H₃ basis as prefix). -/
  v : Fin 24 → R

namespace H4A

variable {h : R}

/-- Zero: the zero coordinate vector. -/
instance : Zero (H4A R h) := ⟨⟨0⟩⟩

/-- Addition: coordinatewise. -/
instance : Add (H4A R h) := ⟨fun x y => ⟨x.v + y.v⟩⟩

/-- Negation: coordinatewise. -/
instance : Neg (H4A R h) := ⟨fun x => ⟨-x.v⟩⟩

/-- Subtraction: coordinatewise. -/
instance : Sub (H4A R h) := ⟨fun x y => ⟨x.v - y.v⟩⟩

/-- ℕ-scalar action: coordinatewise. -/
instance : SMul ℕ (H4A R h) := ⟨fun n x => ⟨n • x.v⟩⟩

/-- ℤ-scalar action: coordinatewise. -/
instance : SMul ℤ (H4A R h) := ⟨fun n x => ⟨n • x.v⟩⟩

/-- R-scalar action: coordinatewise. -/
instance : SMul R (H4A R h) := ⟨fun c x => ⟨c • x.v⟩⟩

@[simp] lemma zero_v : (0 : H4A R h).v = 0 := rfl
@[simp] lemma add_v (x y : H4A R h) : (x + y).v = x.v + y.v := rfl
@[simp] lemma neg_v (x : H4A R h) : (-x).v = -x.v := rfl
@[simp] lemma smul_v (c : R) (x : H4A R h) : (c • x).v = c • x.v := rfl

/-- Coordinate projection is injective (transport vehicle). -/
lemma v_injective : Function.Injective (v : H4A R h → Fin 24 → R) :=
  fun a b hab => by cases a; cases b; simpa using hab

/-- Additive group, transported along the coordinates. -/
instance : AddCommGroup (H4A R h) :=
  v_injective.addCommGroup v rfl (fun _ _ => rfl) (fun _ => rfl)
    (fun _ _ => rfl) (fun _ _ => rfl) (fun _ _ => rfl)

/-- The additive-group hom onto NF coordinates (transport vehicle). -/
def vHom : H4A R h →+ (Fin 24 → R) :=
  { toFun := v, map_zero' := rfl, map_add' := fun _ _ => rfl }

/-- R-module structure, transported along the coordinates. -/
instance : Module R (H4A R h) :=
  v_injective.module R vHom (fun _ _ => rfl)

/-- Multiplication: the proved NF product `mulNF₄`. -/
instance : Mul (H4A R h) := ⟨fun x y => ⟨mulNF₄ h x.v y.v⟩⟩

/-- One: the NF unit γ. -/
instance : One (H4A R h) := ⟨⟨unitNF₄⟩⟩

@[simp] lemma mul_v (x y : H4A R h) : (x * y).v = mulNF₄ h x.v y.v := rfl
@[simp] lemma one_v : (1 : H4A R h).v = unitNF₄ := rfl

/-- **The H₄(q) NF module is a `Ring`** — multiplication `mulNF₄`, unit γ,
all laws discharged by the theorems above (associativity via the structured
generator-commutation route). -/
instance : Ring (H4A R h) where
  __ := (inferInstance : AddCommGroup (H4A R h))
  mul := (· * ·)
  one := 1
  mul_assoc a b c := H4A.ext (mulNF₄_assoc h a.v b.v c.v)
  one_mul a := H4A.ext (mulNF₄_one_left h a.v)
  mul_one a := H4A.ext (mulNF₄_one_right h a.v)
  left_distrib a b c := H4A.ext (mulNF₄_add_right h a.v b.v c.v)
  right_distrib a b c := H4A.ext (mulNF₄_add_left h a.v b.v c.v)
  zero_mul a := H4A.ext (mulNF₄_zero_left h a.v)
  mul_zero a := H4A.ext (mulNF₄_zero_right h a.v)

/-- **The H₄(q) NF module is an `R`-algebra** — scalar action compatible
with `mulNF₄` on both sides (the proved homogeneity laws). -/
instance : Algebra R (H4A R h) :=
  Algebra.ofModule
    (fun c x y => H4A.ext (mulNF₄_smul_left h c x.v y.v))
    (fun c x y => H4A.ext (mulNF₄_smul_right h c x.v y.v))

end H4A

end QOU.Machinery.H4
