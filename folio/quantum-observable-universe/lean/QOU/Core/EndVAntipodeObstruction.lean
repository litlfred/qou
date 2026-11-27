import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination


/-!
# End(V) cannot carry an involutive braided antipode at generic q

Scope-limited negative (bean `qou-b5w7`): this concerns the single candidate
`A = End(V) = V ⊗ V∨` in the Kauffman / Temperley–Lieb model of
`Rep U_q(sl₂)`, with the antipode taken in `span{1, e}` on the two strands.
It does not exclude every Frobenius–Hopf object.

Model (pure algebra over a commutative ring `R`, `A · Ai = 1`):
* cup `u = (0, A, −A⁻¹, 0)`, cap `c = (0, −A, A⁻¹, 0)`, `e = u ∘ c`;
* braiding `σ = A · 1 + A⁻¹ · e`, and `β_{A,A} = σ₂σ₃σ₁σ₂` on `V^{⊗4}`;
* multiplication `μ = 1 ⊗ c ⊗ 1`;
* candidate antipode `S = a · 1 + b · e`.

**Theorem** `endV_antipode_obstruction`: if `S` is braided
anti-multiplicative on the basis vector `e₀₀₁₁`
(`S ∘ μ = μ ∘ β ∘ (S ⊗ S)`) and `S ∘ S = id`, then `A⁸ = 1`, i.e. `q⁴ = 1`
with `q = A²`.  The anti-multiplicative solutions are `S = 0` and
`S = −A³σ`, whose square is `A⁸` on the adjoint summand.  So a q-faithful
witness on `End(V)` needs a twisted QOU (`S²` = pivotal conjugation), not the
involutive one.
-/

open BigOperators

namespace QOU.EndVObstruction

variable {R : Type*} [CommRing R] (A Ai : R)

/-- local two-strand operator: entry (out₁,out₂ ; in₁,in₂) -/
abbrev Op2 (R : Type*) := Fin 2 → Fin 2 → Fin 2 → Fin 2 → R

/-- cup vector `u` and cap covector `c` (Kauffman normalisation, `Ai = A⁻¹`) -/
def cup (i j : Fin 2) : R := if i = 0 ∧ j = 1 then A else if i = 1 ∧ j = 0 then -Ai else 0
def cap (i j : Fin 2) : R := if i = 0 ∧ j = 1 then -A else if i = 1 ∧ j = 0 then Ai else 0

/-- `e = cup ∘ cap`, `σ = A·1 + A⁻¹·e`, `S = a·1 + b·e` -/
def eOp : Op2 R := fun o1 o2 i1 i2 => cup A Ai o1 o2 * cap A Ai i1 i2
def idOp : Op2 R := fun o1 o2 i1 i2 => if o1 = i1 ∧ o2 = i2 then 1 else 0
def lin (x y : R) : Op2 R := fun o1 o2 i1 i2 => x * idOp o1 o2 i1 i2 + y * eOp A Ai o1 o2 i1 i2

abbrev T4 (R : Type*) := Fin 2 → Fin 2 → Fin 2 → Fin 2 → R
abbrev T2 (R : Type*) := Fin 2 → Fin 2 → R

def on12 (M : Op2 R) (v : T4 R) : T4 R := fun a b c d => ∑ x, ∑ y, M a b x y * v x y c d
def on23 (M : Op2 R) (v : T4 R) : T4 R := fun a b c d => ∑ x, ∑ y, M b c x y * v a x y d
def on34 (M : Op2 R) (v : T4 R) : T4 R := fun a b c d => ∑ x, ∑ y, M c d x y * v a b x y
/-- `μ = 1 ⊗ cap ⊗ 1` -/
def mu (v : T4 R) : T2 R := fun a d => ∑ x, ∑ y, cap A Ai x y * v a x y d
def act2 (M : Op2 R) (w : T2 R) : T2 R := fun a b => ∑ x, ∑ y, M a b x y * w x y

/-- basis vector `e_{0,0,1,1}` -/
def bv : T4 R := fun a b c d => if a = 0 ∧ b = 0 ∧ c = 1 ∧ d = 1 then 1 else 0

variable (a b : R)

/-- `β_{A,A} = σ₂ σ₃ σ₁ σ₂` on `A ⊗ A = V^{⊗4}` -/
def beta (v : T4 R) : T4 R :=
  let σ := lin A Ai A Ai
  on23 σ (on34 σ (on12 σ (on23 σ v)))

/-- composition of two-strand operators -/
def comp2 (M N : Op2 R) : Op2 R := fun o1 o2 i1 i2 => ∑ x, ∑ y, M o1 o2 x y * N x y i1 i2

lemma anti_entries (h : A * Ai = 1)
    (hanti : act2 (lin A Ai a b) (mu A Ai bv) =
      mu A Ai (beta A Ai (on12 (lin A Ai a b) (on34 (lin A Ai a b) bv)))) :
    a - A ^ 2 * b = 0 ∧ A ^ 6 * b + a ^ 2 = 0 := by
  have t1 := congrFun (congrFun hanti 0) 1
  have t2 := congrFun (congrFun hanti 1) 0
  simp [beta, act2, mu, on12, on23, on34, lin, idOp, eOp, cup, cap, bv, Fin.sum_univ_two] at t1 t2
  constructor
  · linear_combination (-Ai) * t1 + (A^6*Ai^6*a^2 + A^6*Ai^2*a^2 - 2*A^5*Ai^5*a^2 - A^5*Ai*a^2 + A^4*Ai^8*a^2 + 2*A^4*Ai^4*a^2 - A^3*Ai^7*a^2 + A^2*b - a) * h
  · linear_combination (-A^5) * t2 + (-A^10*Ai^6*a^2 - A^8*Ai^8*a^2 - A^7*Ai^7*a^2 - A^6*Ai^6*a^2 - A^6*b - A^5*Ai^5*a^2 - A^4*Ai^4*a^2 - A^3*Ai^3*a^2 - A^2*Ai^2*a^2 - A*Ai*a^2 - a^2) * h

lemma sq_entry (hsq : comp2 (lin A Ai a b) (lin A Ai a b) = idOp) : a ^ 2 = 1 := by
  have := congrFun (congrFun (congrFun (congrFun hsq 0) 0) 0) 0
  simp [comp2, lin, idOp, eOp, cup, cap, Fin.sum_univ_two] at this
  linear_combination this

/-- **No involutive braided antipode on `End(V)` at generic `q`.**  In the Kauffman
model of `Rep(U_q(sl₂))` (`V = R²`, loop value `−A² − A⁻²`, `q = A⁻²`), an
equivariant `S = a·1 + b·e` on `A = V ⊗ V` that is braided anti-multiplicative
(`S ∘ μ = μ ∘ β_{A,A} ∘ (S ⊗ S)`) and involutive forces `A⁸ = 1`, i.e. `q⁴ = 1`. -/
theorem endV_antipode_obstruction (h : A * Ai = 1)
    (hanti : act2 (lin A Ai a b) (mu A Ai bv) =
      mu A Ai (beta A Ai (on12 (lin A Ai a b) (on34 (lin A Ai a b) bv))))
    (hsq : comp2 (lin A Ai a b) (lin A Ai a b) = idOp) : A ^ 8 = 1 := by
  obtain ⟨e1, e2⟩ := anti_entries A Ai a b h hanti
  have e3 := sq_entry A Ai a b hsq
  linear_combination (-A ^ 8) * e3 + (A ^ 4 * a - 1) * (A ^ 4 * e1 + e2 - e3)

end QOU.EndVObstruction
