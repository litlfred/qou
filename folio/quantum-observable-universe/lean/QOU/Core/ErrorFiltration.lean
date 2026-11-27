import QOU.Core.QuantaleCut
import Mathlib.RingTheory.Ideal.Operations
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Action.Basic
import Mathlib.Data.Fintype.Card

/-!
# QOU.Core.ErrorFiltration — quadratic and higher-order error as a filtration of ideals

Owner question (2026-11-27): manage quadratic and higher-order error bounds with an
ideal of words, a filtration, S-polynomials and their iterates, and the symmetry group
of each level, as in the algebraic (Galois-conjugate) proof of the `4₁` volume-conjecture
bound in `QOU.Core.KashaevReflection`.

## The picture

An **error filtration** is a descending chain of ideals `F 0 = ⊤ ⊇ F 1 ⊇ F 2 ⊇ …` with
`F a · F b ⊆ F (a + b)`. "`x` equals `y` up to order `n`" means `x − y ∈ F n`. This is
exactly the existing adic near system `adicNear` of `QOU.Core.QuantaleCut`, so error
tracking stays inside the one cut core and needs no new axiom and no `ε–δ`.

* **Order of a product of errors adds** (`mul_mem`, `pow_mem`). The quadratic term
  `(x − y)(u − v)` of a product lies in `F (a + b)`, so the first-order (Leibniz)
  linearisation `y v + y (u − v) + (x − y) v` is exact modulo `F (a + b)`
  (`mul_linearize`). Iterating gives the order-`n` jet of any polynomial expression.
* **Symmetry of each level.** If a finite group `G` acts by ring automorphisms and
  preserves every `F n`, then the near relation is `G`-invariant (`near_smul`), and the
  **norm** `∏_{g ∈ G} g • e` of an order-`n` error is `G`-invariant
  (`norm_smul`) and of order `n · |G|` (`norm_mem`). This is the shape of the
  Galois-conjugate argument for `⟨4₁⟩_N`: work with the invariant product over all
  conjugates, which lands in the fixed ring.
* **Surreal read-out.** A ring map `φ : R → K` that sends the generating ideal `I` into
  `ε · B` (with `B` a subring containing `φ R`) sends `I ^ n` into `ε ^ n · B`
  (`map_pow_mem`). Taking `K` a surreal field, `B` the convex subring of finite elements
  and `ε` infinitesimal, an order-`n` error reads out as `O(ε ^ n)` in the Hahn sense.
  The statement itself is purely algebraic: no order, no limit, no empirical value.

## Where Gröbner bases enter (not formalised here)

When the error ideal is presented by words (a two-sided ideal of a free algebra), a
Gröbner–Shirshov basis of `I + F (N + 1)` for an admissible order compatible with the
weight decides `x − y ∈ F n` by normal form, and its leading word gives the exact error
order. S-polynomials and their iterates are the completion; jet-stratified completion
(`UGB.GrobnerShirshov.jet_stratified_gs_criterion`) checks only the new pairs at each
level. That package is separate (`ugb`), so the bridge is a follow-up.

No `sorry`, no axiom beyond Lean's three, no empirical value.
-/

namespace QOU.Core.Error

open QOU.Core.LawvereCut

/-- A multiplicative error filtration on a commutative ring. -/
structure ErrorFiltration (R : Type*) [CommRing R] where
  F : ℕ → Ideal R
  anti : Antitone F
  zero_top : F 0 = ⊤
  mul_le : ∀ a b, F a * F b ≤ F (a + b)

namespace ErrorFiltration

variable {R : Type*} [CommRing R] (E : ErrorFiltration R)

/-- The near system "agree to order `n`": `x − y ∈ F n`, the adic instance of the one
cut core. -/
def near : NearSystem AdicLevel R := adicNear E.F E.anti

theorem near_iff {n : ℕ} {x y : R} : E.near.near ⟨n⟩ x y ↔ x - y ∈ E.F n := Iff.rfl

/-- Orders of errors add under multiplication. -/
theorem mul_mem {a b : ℕ} {x y : R} (hx : x ∈ E.F a) (hy : y ∈ E.F b) :
    x * y ∈ E.F (a + b) :=
  E.mul_le a b (Ideal.mul_mem_mul hx hy)

/-- An order-`a` error to the `n`-th power has order `a · n`. -/
theorem pow_mem {a : ℕ} {x : R} (hx : x ∈ E.F a) : ∀ n : ℕ, x ^ n ∈ E.F (a * n)
  | 0 => by simp [E.zero_top]
  | n + 1 => by
    rw [pow_succ, Nat.mul_succ]
    exact E.mul_mem (pow_mem hx n) hx

/-- **Quadratic remainder.** If `x ≡ y` to order `a` and `u ≡ v` to order `b`, the
first-order linearisation of `x u` about `(y, v)` is exact to order `a + b`. -/
theorem mul_linearize {a b : ℕ} {x y u v : R} (h₁ : x - y ∈ E.F a) (h₂ : u - v ∈ E.F b) :
    x * u - (y * v + y * (u - v) + (x - y) * v) ∈ E.F (a + b) := by
  have e : x * u - (y * v + y * (u - v) + (x - y) * v) = (x - y) * (u - v) := by ring
  rw [e]
  exact E.mul_mem h₁ h₂

/-- Products of near pairs are near at the coarser order. -/
theorem mul_near {a b : ℕ} {x y u v : R} (h₁ : x - y ∈ E.F a) (h₂ : u - v ∈ E.F b) :
    x * u - y * v ∈ E.F (min a b) := by
  have e : x * u - y * v = x * (u - v) + (x - y) * v := by ring
  rw [e]
  exact Ideal.add_mem _ (E.anti (min_le_right a b) (Ideal.mul_mem_left _ x h₂))
    (E.anti (min_le_left a b) (Ideal.mul_mem_right v _ h₁))

/-- The `I`-adic filtration `F n = I ^ n`. -/
def ofIdeal (I : Ideal R) : ErrorFiltration R where
  F n := I ^ n
  anti _ _ h := Ideal.pow_le_pow_right h
  zero_top := by rw [pow_zero, Ideal.one_eq_top]
  mul_le a b := (pow_add I a b).ge

/-! ### Symmetry of each level -/

section Symmetry

variable {G : Type*} [Group G] [MulSemiringAction G R]

/-- `G` preserves every level of the filtration. -/
def Stable : Prop := ∀ (g : G) (n : ℕ) (x : R), x ∈ E.F n → g • x ∈ E.F n

/-- A stable symmetry preserves "agree to order `n`". -/
theorem near_smul (hS : E.Stable (G := G)) (g : G) {n : ℕ} {x y : R}
    (h : x - y ∈ E.F n) : g • x - g • y ∈ E.F n := by
  rw [← smul_sub]
  exact hS g n _ h

variable [Fintype G]

/-- The norm `∏_{g ∈ G} g • x`. -/
def norm (x : R) : R := ∏ g : G, g • x

/-- The norm is `G`-invariant: it lies in the fixed ring. -/
theorem norm_smul (h : G) (x : R) : h • norm (G := G) x = norm (G := G) x := by
  unfold norm
  rw [Finset.smul_prod']
  simp_rw [smul_smul]
  exact Fintype.prod_equiv (Equiv.mulLeft h) _ _ (fun _ => rfl)

/-- Finite products of order-`n` errors have order `n · (number of factors)`. -/
theorem prod_mem {ι : Type*} (s : Finset ι) (f : ι → R) {n : ℕ}
    (hf : ∀ i ∈ s, f i ∈ E.F n) : ∏ i ∈ s, f i ∈ E.F (n * s.card) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [E.zero_top]
  | insert i s hi ih =>
    rw [Finset.prod_insert hi, Finset.card_insert_of_notMem hi, Nat.mul_succ, add_comm]
    exact E.mul_mem (hf i (Finset.mem_insert_self _ _))
      (ih fun j hj => hf j (Finset.mem_insert_of_mem hj))

/-- **Norm of an order-`n` error.** It is invariant and of order `n · |G|`. -/
theorem norm_mem (hS : E.Stable (G := G)) {n : ℕ} {x : R} (hx : x ∈ E.F n) :
    norm (G := G) x ∈ E.F (n * Fintype.card G) :=
  E.prod_mem Finset.univ _ (fun g _ => hS g n x hx)

end Symmetry

end ErrorFiltration

/-! ### Surreal read-out: order `n` maps into the band `ε ^ n · B` -/

section Readout

variable {R K : Type*} [CommRing R] [CommRing K]

/-- If `φ` sends `R` into the subring `B` and the generating ideal `I` into `ε · B`, then it
sends `I ^ n` into `ε ^ n · B`. With `K` surreal, `B` the finite elements and `ε`
infinitesimal, an order-`n` error is `O(ε ^ n)`. -/
theorem map_pow_mem (φ : R →+* K) (B : Subring K) (ε : K) (I : Ideal R)
    (hR : ∀ r, φ r ∈ B) (hI : ∀ x ∈ I, ∃ b ∈ B, φ x = ε * b) :
    ∀ n : ℕ, ∀ x ∈ I ^ n, ∃ b ∈ B, φ x = ε ^ n * b
  | 0, x, _ => ⟨φ x, hR x, by simp⟩
  | n + 1, x, hx => by
    rw [pow_succ] at hx
    refine Submodule.mul_induction_on hx ?_ ?_
    · intro m hm k hk
      obtain ⟨b₁, hb₁, e₁⟩ := map_pow_mem φ B ε I hR hI n m hm
      obtain ⟨b₂, hb₂, e₂⟩ := hI k hk
      refine ⟨b₁ * b₂, B.mul_mem hb₁ hb₂, ?_⟩
      rw [map_mul, e₁, e₂]
      ring
    · rintro y z ⟨b₁, hb₁, e₁⟩ ⟨b₂, hb₂, e₂⟩
      exact ⟨b₁ + b₂, B.add_mem hb₁ hb₂, by rw [map_add, e₁, e₂]; ring⟩

/-- Order-`n` agreement in the `I`-adic filtration reads out as an `ε ^ n · B` difference. -/
theorem readout_near (φ : R →+* K) (B : Subring K) (ε : K) (I : Ideal R)
    (hR : ∀ r, φ r ∈ B) (hI : ∀ x ∈ I, ∃ b ∈ B, φ x = ε * b) {n : ℕ} {x y : R}
    (h : x - y ∈ (ErrorFiltration.ofIdeal I).F n) :
    ∃ b ∈ B, φ x - φ y = ε ^ n * b := by
  obtain ⟨b, hb, e⟩ := map_pow_mem φ B ε I hR hI n _ h
  exact ⟨b, hb, by rw [← map_sub, e]⟩

end Readout

end QOU.Core.Error
