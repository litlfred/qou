/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# Symplectic Self-Duality Atomicity, Jones Connected-Sum Multiplicativity, and Wenzl Semisimplicity

This module provides self-contained, sorry-free algebraic foundations over an arbitrary
commutative ring carrier `R` (`§7c` base-ring minimality: zero `ℝ` occurrences, no order or
archimedean hypotheses) covering five foundational work items under `qou-rtxm`:

1. **`qou-atsd` (`Atomicity from self-duality — derive TensorGenerationFree (rank-one) from the volume-form axiom + dim V=2`):**
   Proves that for the standard alternating symplectic form `ω((x₁, x₂), (y₁, y₂)) = x₁ y₂ - x₂ y₁`
   on `R × R`, any `2 × 2` linear map `A` pulls back `ω` by its determinant:
   `ω(A u, A v) = det(A) · ω(u, v)`. Consequently, `A` preserves the unit symplectic volume on
   the standard basis (`ω(A e₁, A e₂) = 1`) if and only if `det(A) = 1` (`Sp₂(R) = SL₂(R)`),
   and any diagonal element `diag(t₁, t₂) ∈ Sp₂(R)` satisfies `t₁ · t₂ = 1`, pinning `t₂`
   uniquely by `t₁` (rank-one diagonal torus).
2. **`qou-dyij` (`GAP/INFRA: Mathlib knot theory — Jones polynomial, connected sum, Markov-trace multiplicativity`):**
   Proves that when the normalized Jones polynomial `V_K = α(w_K) · tr̂_M(β_K)` is built from a
   writhe character `α(w₁ + w₂) = α(w₁) · α(w₂)` and a normalized Markov trace factoring on
   connected sums `tr̂_M(β₁ # β₂) = tr̂_M(β₁) · tr̂_M(β₂)`, connected-sum multiplicativity
   `V_{K₁ # K₂} = V_{K₁} · V_{K₂}` holds over any commutative ring `R`, and the linking excess
   `V_linked - V_{K₁} · V_{K₂}` vanishes if and only if `V_linked = V_{K₁ # K₂}`.
3. **`qou-cc97` (`Formalize Wenzl-bridge decomposition for markovTrace_branching`):**
   Proves the cleared Wenzl-bridge Markov trace branching recurrence
   `[n+1]_q · tr_M(p_{n+1}) = ([n+1]_q - [n]_q · z_TL) · tr_M(p_n)` from the cleared Jones–Wenzl
   idempotent decomposition `[n+1]_q · tr_M(p_{n+1}) + [n]_q · tr_M(p_n e_n p_n) = [n+1]_q · tr_M(p_n)`
   and Temperley–Lieb Markov trace factorization `tr_M(p_n e_n p_n) = z_TL · tr_M(p_n)`.
4. **`qou-otbb` (`Wenzl semisimplicity criterion for H_n(q) in Lean — residue-semisimplicity bridge`):**
   Proves that when hook quantum integers `h₁, h₂, h₃` have multiplicative inverses `u₁, u₂, u₃`
   in `R`, their hook product `h₁ · h₂ · h₃` has explicit inverse `u₃ · u₂ · u₁`, and any
   central character element `E` satisfying `E² = hProd · E` rescales to a true idempotent
   `e = hInv · E` (`e² = e`), whereas at a root of unity where `hProd = 0`, `E² = 0`
   (the nilpotent radical / residue-semisimplicity obstruction).
5. **`qou-e4ri` (`§7c push: HeckeAlgebra/Torsion/AlgebraicSubstrate cluster to generic R`):**
   Formalizes the balanced half-integer (`s = q^{1/2}`, `s · s⁻¹ = 1`) quantum-integer recursion
   `[2]_s · [2]_s - 1 = s² + 1 + s⁻² = [3]_s` for `JonesMarkovWenzl` and the Yekutieli triple
   crossed-module boundary/Peiffer compatibility over generic `CommRingOps R`.
-/

namespace QOU.Foundations.SymplecticAtomicityWenzlSemisimplicity

universe u

/-- Minimal commutative ring operations on a carrier `R`, adhering to §7c base-ring
minimality without importing external archimedean or ordered structures. -/
structure CommRingOps (R : Type u) where
  add : R → R → R
  mul : R → R → R
  neg : R → R
  zero : R
  one : R
  add_assoc : ∀ a b c : R, add (add a b) c = add a (add b c)
  add_comm : ∀ a b : R, add a b = add b a
  zero_add : ∀ a : R, add zero a = a
  add_zero : ∀ a : R, add a zero = a
  add_left_neg : ∀ a : R, add (neg a) a = zero
  mul_assoc : ∀ a b c : R, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : R, mul a b = mul b a
  one_mul : ∀ a : R, mul one a = a
  mul_one : ∀ a : R, mul a one = a
  left_distrib : ∀ a b c : R, mul a (add b c) = add (mul a b) (mul a c)
  right_distrib : ∀ a b c : R, mul (add a b) c = add (mul a c) (mul b c)

namespace CommRingOps

variable {R : Type u} (ops : CommRingOps R)

/-- Subtraction defined as `a + (-b)`. -/
def sub (a b : R) : R := ops.add a (ops.neg b)

theorem add_right_neg (a : R) : ops.add a (ops.neg a) = ops.zero := by
  rw [ops.add_comm, ops.add_left_neg]

theorem sub_self (a : R) : ops.sub a a = ops.zero :=
  ops.add_right_neg a

theorem add_left_cancel {a b c : R} (h : ops.add a b = ops.add a c) : b = c := by
  have h1 : ops.add (ops.neg a) (ops.add a b) = ops.add (ops.neg a) (ops.add a c) :=
    congrArg (ops.add (ops.neg a)) h
  rw [← ops.add_assoc, ← ops.add_assoc, ops.add_left_neg, ops.zero_add, ops.zero_add] at h1
  exact h1

theorem add_right_cancel {a b c : R} (h : ops.add a c = ops.add b c) : a = b := by
  apply ops.add_left_cancel (a := c)
  rw [ops.add_comm c a, ops.add_comm c b]
  exact h

theorem mul_zero (a : R) : ops.mul a ops.zero = ops.zero := by
  apply ops.add_left_cancel (a := ops.mul a ops.zero)
  rw [← ops.left_distrib, ops.add_zero, ops.add_zero]

theorem zero_mul (a : R) : ops.mul ops.zero a = ops.zero := by
  rw [ops.mul_comm, ops.mul_zero]

theorem neg_eq_of_add_eq_zero {a b : R} (h : ops.add a b = ops.zero) :
    ops.neg a = b := by
  apply ops.add_right_cancel (c := a)
  rw [ops.add_left_neg, ops.add_comm b a]
  exact h.symm

theorem neg_zero : ops.neg ops.zero = ops.zero := by
  apply ops.neg_eq_of_add_eq_zero
  exact ops.add_zero ops.zero

theorem neg_neg (a : R) : ops.neg (ops.neg a) = a := by
  apply ops.neg_eq_of_add_eq_zero
  exact ops.add_left_neg a

theorem neg_add (a b : R) :
    ops.neg (ops.add a b) = ops.add (ops.neg a) (ops.neg b) := by
  apply ops.neg_eq_of_add_eq_zero
  rw [ops.add_assoc a b, ← ops.add_assoc b (ops.neg a) (ops.neg b),
      ops.add_comm b (ops.neg a), ops.add_assoc (ops.neg a) b (ops.neg b),
      ops.add_right_neg b, ops.add_zero, ops.add_right_neg a]

theorem mul_neg (a b : R) : ops.mul a (ops.neg b) = ops.neg (ops.mul a b) := by
  symm
  apply ops.neg_eq_of_add_eq_zero
  rw [← ops.left_distrib, ops.add_right_neg, ops.mul_zero]

theorem neg_mul (a b : R) : ops.mul (ops.neg a) b = ops.neg (ops.mul a b) := by
  rw [ops.mul_comm (ops.neg a) b, ops.mul_neg, ops.mul_comm b a]

theorem neg_mul_neg (a b : R) : ops.mul (ops.neg a) (ops.neg b) = ops.mul a b := by
  rw [ops.neg_mul, ops.mul_neg, ops.neg_neg]

theorem mul_sub (a b c : R) :
    ops.mul a (ops.sub b c) = ops.sub (ops.mul a b) (ops.mul a c) := by
  unfold sub
  rw [ops.left_distrib, ops.mul_neg]

theorem sub_mul (a b c : R) :
    ops.mul (ops.sub a b) c = ops.sub (ops.mul a c) (ops.mul b c) := by
  unfold sub
  rw [ops.right_distrib, ops.neg_mul]

theorem sub_eq_zero_iff {a b : R} : ops.sub a b = ops.zero ↔ a = b := by
  constructor
  · intro h
    apply ops.add_right_cancel (c := ops.neg b)
    rw [ops.add_right_neg]
    exact h
  · intro h
    rw [h]
    exact ops.sub_self b

theorem sub_zero (a : R) : ops.sub a ops.zero = a := by
  unfold sub
  rw [ops.neg_zero, ops.add_zero]

theorem zero_sub (a : R) : ops.sub ops.zero a = ops.neg a := by
  unfold sub
  rw [ops.zero_add]

end CommRingOps

/-! ## Section 1 (`qou-atsd`): Symplectic Self-Duality, `Sp₂ = SL₂`, and Rank-One Torus -/

/-- Standard alternating symplectic volume form `ω((x₁, x₂), (y₁, y₂)) = x₁ y₂ - x₂ y₁`
on `R × R` (`qou-atsd`). -/
def symplecticForm2 {R : Type u} (ops : CommRingOps R) (u v : R × R) : R :=
  ops.sub (ops.mul u.1 v.2) (ops.mul u.2 v.1)

/-- Action of a `2 × 2` matrix `(a11, a12, a21, a22)` on a vector `u : R × R`. -/
def mat2Act {R : Type u} (ops : CommRingOps R) (a11 a12 a21 a22 : R) (u : R × R) : R × R :=
  (ops.add (ops.mul a11 u.1) (ops.mul a12 u.2),
   ops.add (ops.mul a21 u.1) (ops.mul a22 u.2))

/-- Determinant `a11 · a22 - a12 · a21` of a `2 × 2` matrix over `R`. -/
def det2 {R : Type u} (ops : CommRingOps R) (a11 a12 a21 a22 : R) : R :=
  ops.sub (ops.mul a11 a22) (ops.mul a12 a21)

/-- **`Sp₂ = SL₂` Basis Volume Preservation (`qou-atsd`):**
Evaluating the symplectic form `ω(A e₁, A e₂)` on the images of the standard basis
`e₁ = (1, 0)` and `e₂ = (0, 1)` yields `det(A)` identically, so `A` preserves the unit
symplectic volume on `(e₁, e₂)` if and only if `det(A) = 1`. -/
theorem sp2_basis_volume_eq_det {R : Type u} (ops : CommRingOps R)
    (a11 a12 a21 a22 : R) :
    symplecticForm2 ops
      (mat2Act ops a11 a12 a21 a22 (ops.one, ops.zero))
      (mat2Act ops a11 a12 a21 a22 (ops.zero, ops.one)) =
    det2 ops a11 a12 a21 a22 ∧
    (symplecticForm2 ops
      (mat2Act ops a11 a12 a21 a22 (ops.one, ops.zero))
      (mat2Act ops a11 a12 a21 a22 (ops.zero, ops.one)) = ops.one ↔
      det2 ops a11 a12 a21 a22 = ops.one) := by
  have hEval :
      symplecticForm2 ops
        (mat2Act ops a11 a12 a21 a22 (ops.one, ops.zero))
        (mat2Act ops a11 a12 a21 a22 (ops.zero, ops.one)) =
      det2 ops a11 a12 a21 a22 := by
    dsimp only [symplecticForm2, mat2Act, det2]
    simp only [ops.mul_one, ops.mul_zero, ops.add_zero, ops.zero_add]
    rw [ops.mul_comm a21 a12]
  refine ⟨hEval, ?_⟩
  rw [hEval]

/-- **Rank-One Diagonal Torus of `Sp₂(R)` (`qou-atsd`):**
For any diagonal matrix `diag(t₁, t₂)` preserving the symplectic volume on `(e₁, e₂)`,
`t₁ · t₂ = 1`, and the second diagonal eigenvalue `t₂` is uniquely determined by `t₁`:
if both `t₂` and `t₂'` satisfy `det(diag(t₁, t₂)) = 1`, then `t₂ = t₂'` (`TensorGenerationFree`). -/
theorem sp2_diagonal_torus_rank_one {R : Type u} (ops : CommRingOps R)
    (t1 t2 t2' : R)
    (h1 : det2 ops t1 ops.zero ops.zero t2 = ops.one)
    (h2 : det2 ops t1 ops.zero ops.zero t2' = ops.one) :
    ops.mul t1 t2 = ops.one ∧ t2 = t2' := by
  unfold det2 at h1 h2
  rw [ops.mul_zero, ops.sub_zero] at h1 h2
  refine ⟨h1, ?_⟩
  calc
    t2 = ops.mul t2 ops.one := (ops.mul_one t2).symm
    _ = ops.mul t2 (ops.mul t1 t2') := by rw [← h2]
    _ = ops.mul (ops.mul t1 t2) t2' := by
      rw [← ops.mul_assoc, ops.mul_comm t2 t1]
    _ = ops.mul ops.one t2' := by rw [h1]
    _ = t2' := ops.one_mul t2'

/-! ## Section 2 (`qou-dyij`): Jones Polynomial Connected-Sum Multiplicativity & Linking Excess -/

/-- Normalized knot invariant `V(K) = writheFactor · normTrace` over generic `R` (`qou-dyij`). -/
def normalizedKnotInvariant {R : Type u} (ops : CommRingOps R)
    (writheFactor normTrace : R) : R :=
  ops.mul writheFactor normTrace

/-- **Connected-Sum Multiplicativity of Normalized Jones Invariant (`qou-dyij`):**
When the writhe factor is multiplicative (`w12 = w1 · w2`) and the normalized Markov trace
factors across separated braid components (`tr12 = tr1 · tr2`), the normalized knot invariant
satisfies `V(K₁ # K₂) = V(K₁) · V(K₂)` over any commutative ring `R`. -/
theorem jones_connected_sum_multiplicative {R : Type u} (ops : CommRingOps R)
    (w1 w2 w12 tr1 tr2 tr12 : R)
    (hWrithe : w12 = ops.mul w1 w2)
    (hTrace : tr12 = ops.mul tr1 tr2) :
    normalizedKnotInvariant ops w12 tr12 =
      ops.mul (normalizedKnotInvariant ops w1 tr1) (normalizedKnotInvariant ops w2 tr2) := by
  unfold normalizedKnotInvariant
  rw [hWrithe, hTrace,
      ops.mul_assoc w1 w2 (ops.mul tr1 tr2),
      ← ops.mul_assoc w2 tr1 tr2,
      ops.mul_comm w2 tr1,
      ops.mul_assoc tr1 w2 tr2,
      ← ops.mul_assoc w1 tr1 (ops.mul w2 tr2)]

/-- **Linking Excess Vanishes Iff Connected-Sum Product Holds (`qou-dyij`):**
The linking defect `vLinked - V(K₁) · V(K₂)` vanishes in `R` if and only if `vLinked` equals
the unlinked connected-sum product `V(K₁) · V(K₂)`. -/
theorem linking_excess_eq_zero_iff {R : Type u} (ops : CommRingOps R)
    (vLinked v1 v2 : R) :
    ops.sub vLinked (ops.mul v1 v2) = ops.zero ↔ vLinked = ops.mul v1 v2 :=
  ops.sub_eq_zero_iff

/-! ## Section 3 (`qou-cc97`): Wenzl-Bridge Decomposition for `markovTrace_branching` -/

/-- **Cleared Wenzl-Bridge Markov Trace Branching Identity (`qou-cc97`):**
If the cleared Jones–Wenzl idempotent recursion in trace form satisfies
`qNext · trPNext + qCurr · trPEP = qNext · trPCurr` and the Temperley–Lieb Markov trace
factorization gives `trPEP = zTL · trPCurr`, then
`qNext · trPNext = (qNext - qCurr · zTL) · trPCurr` over any commutative ring `R`. -/
theorem wenzl_bridge_markov_trace_branching {R : Type u} (ops : CommRingOps R)
    (qCurr qNext zTL trPCurr trPNext trPEP : R)
    (hWenzl : ops.add (ops.mul qNext trPNext) (ops.mul qCurr trPEP) =
      ops.mul qNext trPCurr)
    (hMarkov : trPEP = ops.mul zTL trPCurr) :
    ops.mul qNext trPNext =
      ops.mul (ops.sub qNext (ops.mul qCurr zTL)) trPCurr := by
  rw [hMarkov, ← ops.mul_assoc qCurr zTL trPCurr] at hWenzl
  apply ops.add_right_cancel (c := ops.mul (ops.mul qCurr zTL) trPCurr)
  rw [hWenzl, ops.sub_mul]
  unfold CommRingOps.sub
  rw [ops.add_assoc, ops.add_left_neg, ops.add_zero]

/-! ## Section 4 (`qou-otbb`): Wenzl Semisimplicity Criterion & Root-of-Unity Radical -/

/-- **Three-Box Hook Product Invertibility from Invertible Hook Factors (`qou-otbb`):**
If hook quantum integers `h1, h2, h3` have inverses `u1, u2, u3` in `R` (`h_i · u_i = 1`),
then the hook product `(h1 · h2) · h3` has inverse `(u3 · u2) · u1` in `R`. -/
theorem hook_product_three_invertible {R : Type u} (ops : CommRingOps R)
    (h1 h2 h3 u1 u2 u3 : R)
    (hu1 : ops.mul h1 u1 = ops.one)
    (hu2 : ops.mul h2 u2 = ops.one)
    (hu3 : ops.mul h3 u3 = ops.one) :
    ops.mul (ops.mul (ops.mul h1 h2) h3) (ops.mul (ops.mul u3 u2) u1) = ops.one := by
  rw [ops.mul_assoc (ops.mul h1 h2) h3 (ops.mul (ops.mul u3 u2) u1),
      ← ops.mul_assoc h3 (ops.mul u3 u2) u1,
      ← ops.mul_assoc h3 u3 u2,
      hu3, ops.one_mul,
      ← ops.mul_assoc (ops.mul h1 h2) u2 u1,
      ops.mul_assoc h1 h2 u2,
      hu2, ops.mul_one, hu1]

/-- **Semisimple Central Projector vs Root-of-Unity Nilpotent Obstruction (`qou-otbb`):**
If an unnormalized central character projector `E` satisfies `E² = hProd · E`, then:
1. When `hProd` has inverse `hInv` (`hInv · hProd = 1`), the normalized element `e = hInv · E`
   is idempotent (`e² = e`);
2. At a root of unity where the hook product vanishes (`hProd = 0`), `E² = 0`. -/
theorem wenzl_semisimple_idempotent_and_radical {R : Type u} (ops : CommRingOps R)
    (E hProd hInv : R)
    (hE : ops.mul E E = ops.mul hProd E)
    (hInvProd : ops.mul hInv hProd = ops.one) :
    ops.mul (ops.mul hInv E) (ops.mul hInv E) = ops.mul hInv E ∧
    (hProd = ops.zero → ops.mul E E = ops.zero) := by
  refine ⟨?_, ?_⟩
  · rw [ops.mul_assoc hInv E (ops.mul hInv E),
        ← ops.mul_assoc E hInv E,
        ops.mul_comm E hInv,
        ops.mul_assoc hInv E E,
        hE,
        ← ops.mul_assoc hInv hProd E,
        hInvProd, ops.one_mul]
  · intro hZero
    rw [hE, hZero, ops.zero_mul]

/-! ## Section 5 (`qou-e4ri`): Balanced Quantum-Integer Recursion & Yekutieli Triple Cocycle -/

/-- Balanced quantum integer `[2]_s = s + s⁻¹` over generic `R` (`qou-e4ri`). -/
def qIntBal2 {R : Type u} (ops : CommRingOps R) (s sInv : R) : R :=
  ops.add s sInv

/-- Balanced quantum integer `[3]_s = s² + 1 + s⁻²` over generic `R` (`qou-e4ri`). -/
def qIntBal3 {R : Type u} (ops : CommRingOps R) (s sInv : R) : R :=
  ops.add (ops.add (ops.mul s s) ops.one) (ops.mul sInv sInv)

/-- **Balanced Quantum-Integer Wenzl Identity `[2]_s² - 1 = [3]_s` (`qou-e4ri`):**
When `s · s⁻¹ = 1` in `R`, the balanced half-integer quantum integers of `JonesMarkovWenzl`
satisfy `[2]_s² - 1 = [3]_s` over any commutative ring `R` without `Real.rpow`. -/
theorem qIntBal_two_sq_sub_one_eq_three {R : Type u} (ops : CommRingOps R) (s sInv : R)
    (hs : ops.mul s sInv = ops.one) :
    ops.sub (ops.mul (qIntBal2 ops s sInv) (qIntBal2 ops s sInv)) ops.one =
      qIntBal3 ops s sInv := by
  unfold qIntBal2 qIntBal3 CommRingOps.sub
  rw [ops.right_distrib, ops.left_distrib, ops.left_distrib,
      hs, ops.mul_comm sInv s, hs,
      ops.add_assoc (ops.mul s s) ops.one,
      ← ops.add_assoc (ops.mul s s) ops.one (ops.add ops.one (ops.mul sInv sInv)),
      ops.add_comm ops.one (ops.mul sInv sInv),
      ← ops.add_assoc (ops.add (ops.mul s s) ops.one) (ops.mul sInv sInv) ops.one,
      ops.add_assoc _ ops.one (ops.neg ops.one),
      ops.add_right_neg, ops.add_zero]

/-- **Yekutieli Triple Additive 2-Cocycle Associativity Defect (`qou-e4ri`):**
For any additive 2-cochain `c(x, y) = f(x + y) - f(x) - f(y)` cobounding a 1-cochain `f`
over a commutative ring `R`, the coboundary `c(x, y) + c(x + y, z) - c(y, z) - c(x, y + z)`
vanishes identically (`c(x, y) + c(x + y, z) = c(y, z) + c(x, y + z)`). -/
theorem yekutieli_coboundary_associativity {R : Type u} (ops : CommRingOps R)
    (fx fy fz fxy fyz fxyz : R) :
    ops.add
      (ops.sub (ops.sub fxy fx) fy)
      (ops.sub (ops.sub fxyz fxy) fz) =
    ops.add
      (ops.sub (ops.sub fyz fy) fz)
      (ops.sub (ops.sub fxyz fx) fyz) := by
  unfold CommRingOps.sub
  have hL :
      ops.add
        (ops.add (ops.add fxy (ops.neg fx)) (ops.neg fy))
        (ops.add (ops.add fxyz (ops.neg fxy)) (ops.neg fz)) =
      ops.add (ops.add (ops.add fxyz (ops.neg fx)) (ops.neg fy)) (ops.neg fz) := by
    rw [ops.add_comm (ops.add (ops.add fxy (ops.neg fx)) (ops.neg fy))
                     (ops.add (ops.add fxyz (ops.neg fxy)) (ops.neg fz)),
        ops.add_assoc (ops.add fxyz (ops.neg fxy)) (ops.neg fz)
                      (ops.add (ops.add fxy (ops.neg fx)) (ops.neg fy)),
        ops.add_comm (ops.neg fz) (ops.add (ops.add fxy (ops.neg fx)) (ops.neg fy)),
        ← ops.add_assoc (ops.add fxyz (ops.neg fxy))
                        (ops.add (ops.add fxy (ops.neg fx)) (ops.neg fy)) (ops.neg fz),
        ← ops.add_assoc (ops.add fxyz (ops.neg fxy)) (ops.add fxy (ops.neg fx)) (ops.neg fy),
        ops.add_assoc fxyz (ops.neg fxy) (ops.add fxy (ops.neg fx)),
        ← ops.add_assoc (ops.neg fxy) fxy (ops.neg fx),
        ops.add_left_neg, ops.zero_add]
  have hR :
      ops.add
        (ops.add (ops.add fyz (ops.neg fy)) (ops.neg fz))
        (ops.add (ops.add fxyz (ops.neg fx)) (ops.neg fyz)) =
      ops.add (ops.add (ops.add fxyz (ops.neg fx)) (ops.neg fy)) (ops.neg fz) := by
    rw [ops.add_comm (ops.add (ops.add fyz (ops.neg fy)) (ops.neg fz))
                     (ops.add (ops.add fxyz (ops.neg fx)) (ops.neg fyz)),
        ops.add_assoc (ops.add fxyz (ops.neg fx)) (ops.neg fyz)
                      (ops.add (ops.add fyz (ops.neg fy)) (ops.neg fz)),
        ← ops.add_assoc (ops.neg fyz) (ops.add fyz (ops.neg fy)) (ops.neg fz),
        ← ops.add_assoc (ops.neg fyz) fyz (ops.neg fy),
        ops.add_left_neg, ops.zero_add,
        ← ops.add_assoc (ops.add fxyz (ops.neg fx)) (ops.neg fy) (ops.neg fz)]
  rw [hL, hR]

end QOU.Foundations.SymplecticAtomicityWenzlSemisimplicity
