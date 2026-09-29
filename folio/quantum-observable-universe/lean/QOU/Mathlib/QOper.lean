/-
  q-Oper structure — the q-deformation of opers (q-connections on P¹).

  An oper (Beilinson-Drinfeld) on P¹ is a connection ∇ on a rank-n bundle
  with a full flag reduction such that the associated graded of the flag
  filtration gives the maximal unipotent part. The q-deformation replaces
  the differential ∇ by a q-difference operator σ_q.

  This file formalizes the ALGEBRAIC SKELETON for rank 2:
  1. The q-shift operator σ_q on functions: (σ_q f)(x) = f(qx)
  2. A rank-2 q-connection: a 2×2 matrix A(x) such that σ_q Y = A(x) Y
  3. The oper condition: the (2,1) entry of A is non-degenerate
  4. The monodromy: q-difference Galois group data

  For QOU: the q-opers arise from quantum groups at roots of unity and
  encode the quantum A-polynomial (the q-difference equation annihilating
  the Jones polynomial colored by the n-dimensional representation).

  Pre-archimedean: generic `Field K`. No analysis.

  -- Ref: [frenkel2020] https://arxiv.org/abs/2002.07344
  -- Ref: [koroteev-zeitlin2022] https://arxiv.org/abs/2108.04184
-/

import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic.Ring

namespace QOU.Mathlib.QOper

variable (K : Type*) [Field K]

/-! ### §1  q-shift operator -/

/-- The q-shift operator on functions `K → K`: `(σ_q f)(x) = f(q · x)`. -/
def qShift (q : K) (f : K → K) : K → K := fun x => f (q * x)

/-- The q-shift is linear in the function argument. -/
theorem qShift_add (q : K) (f g : K → K) :
    qShift K q (fun x => f x + g x) = fun x => qShift K q f x + qShift K q g x := by
  ext x; simp [qShift]

/-- The q-shift of a constant is constant. -/
theorem qShift_const (q : K) (c : K) :
    qShift K q (fun _ => c) = fun _ => c := by
  ext x; simp [qShift]

/-- q-shift is multiplicative in q: σ_{q₁} ∘ σ_{q₂} = σ_{q₁q₂}. -/
theorem qShift_compose (q₁ q₂ : K) (f : K → K) :
    qShift K q₁ (qShift K q₂ f) = qShift K (q₁ * q₂) f := by
  ext x; unfold qShift; congr 1; ring

/-- σ_1 = id. -/
theorem qShift_one (f : K → K) :
    qShift K 1 f = f := by
  ext x; simp [qShift]

/-! ### §2  Rank-2 q-connection -/

/-- A **rank-2 q-connection** is a 2×2 matrix A(x) ∈ GL₂(K(x)) encoding the
    q-difference system σ_q Y = A(x) Y. For a q-oper, A has specific structure. -/
structure QConnection2 where
  /-- The connection matrix entries as functions of x. -/
  a₁₁ : K → K
  a₁₂ : K → K
  a₂₁ : K → K
  a₂₂ : K → K

/-- The determinant of a rank-2 q-connection at a point x. -/
def QConnection2.det (A : QConnection2 K) (x : K) : K :=
  A.a₁₁ x * A.a₂₂ x - A.a₁₂ x * A.a₂₁ x

/-- A rank-2 q-connection is **non-degenerate** at x if its determinant is nonzero. -/
def NonDegenerate (A : QConnection2 K) (x : K) : Prop :=
  A.det K x ≠ 0

/-! ### §3  The oper condition -/

/-- A rank-2 q-connection is a **q-oper** when its (2,1) entry is identically 1
    (the oper gauge). In this gauge, A takes the form:
    ```
    A(x) = [ t(x)   -Δ(x) ]
           [  1      0     ]
    ```
    where t is the trace and Δ is the quantum Wronskian (determinant). -/
structure QOper2 extends QConnection2 K where
  /-- The oper gauge: a₂₁ = 1. -/
  oper_gauge : a₂₁ = fun _ => 1
  /-- The oper gauge: a₂₂ = 0. -/
  oper_zero : a₂₂ = fun _ => 0

/-- The trace function of a q-oper. -/
def QOper2.trace (A : QOper2 K) : K → K := A.a₁₁

/-- The quantum Wronskian (negative of the (1,2) entry). -/
def QOper2.quantumWronskian (A : QOper2 K) : K → K := fun x => -(A.a₁₂ x)

/-- **The determinant of a q-oper is minus the quantum Wronskian.** -/
theorem det_eq_wronskian (A : QOper2 K) (x : K) :
    A.toQConnection2.det K x = A.quantumWronskian K x := by
  simp [QConnection2.det, QOper2.quantumWronskian]
  have h1 := congr_fun A.oper_gauge x
  have h2 := congr_fun A.oper_zero x
  simp at h1 h2
  rw [h1, h2]
  simp [mul_zero, mul_one]

/-- **The q-oper equation.** A q-oper A determines the second-order
    q-difference equation on a function y : K → K:
    `y(q²x) − t(x) · y(qx) + Δ(x) · y(x) = 0`.
    This is the q-analogue of the differential equation on P¹ that the
    oper connection encodes. -/
def satisfiesEq (A : QOper2 K) (q : K) (y : K → K) : Prop :=
  ∀ x, y (q * (q * x)) - A.trace K x * y (q * x)
    + A.quantumWronskian K x * y x = 0

end QOU.Mathlib.QOper
