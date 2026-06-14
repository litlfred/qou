import QOU.AppendixSurreals.Basic

/-!
# QOU.AppendixSurreals.KComplex — Complex extension of a SurrealField

This module provides the **complex extension** `KComplex K := K × K`
of a `SurrealField K`, modelled as ordered pairs `(a, b)` representing
`a + b · i`.  We provide:

- the **Manhattan modulus** `|a| + |b|` (placeholder for `√(a²+b²)`);
- the **multiplicative unit** `KComplex.one := (1, 0)`;
- the **imaginary unit** `KComplex.I := (0, 1)`;
- complex multiplication `KComplex.mul (a,b) (c,d) := (ac − bd, ad + bc)`
  as a named operation (we deliberately do **not** override `Prod`'s
  componentwise `*` instance, since `KComplex K := K × K` is an
  abbreviation);
- the **conjugate** `KComplex.conj (a,b) := (a, -b)`;
- the **algebraic-norm** `KComplex.normSq (a,b) := a² + b²` valued in
  `K`.

The named operations satisfy the standard ring identities (one,
commutativity, associativity, `i² = -1`), the conjugation identities
(involution, `z · conj z = (normSq z, 0)`), and the algebraic norm is
multiplicative and faithful (`normSq_mul`, `normSq_eq_zero`).

This unblocks Lean-level reasoning about the coloured-Jones placeholder
`ColoredJones : Knot → KComplex K → K → KComplex K` (for example, the
`KashaevSurreal` deep proof sketch needs `KComplex K` to be a ring).

LaTeX label: `def:k-complex`
-/

namespace QOU.AppendixSurreals

open SurrealField

universe u

variable {K : Type u} [SurrealField K]

/-- The **complexification of `K`** as the ordered pair
    `(real-part, imaginary-part)`.  Faithful as a set-level
    representation of `K[i]/(i²+1)`. -/
abbrev KComplex (K : Type u) [SurrealField K] : Type u := K × K

/-- The **Manhattan modulus** `|a + bi| := |a| + |b|`.  Placeholder
    for the Euclidean modulus `√(a²+b²)`. -/
def KComplex.abs {K : Type u} [SurrealField K] : KComplex K → K :=
  fun ab => |ab.1| + |ab.2|

/-- The **multiplicative unit** in `KComplex K`, i.e. `1 + 0·i`. -/
def KComplex.one (K : Type u) [SurrealField K] : KComplex K := (1, 0)

/-- The **imaginary unit** `i ∈ KComplex K`. -/
def KComplex.I (K : Type u) [SurrealField K] : KComplex K := (0, 1)

/-- **Complex multiplication** `(a, b) · (c, d) := (ac − bd, ad + bc)`,
    realising `KComplex K` as `K[X]/(X² + 1)`. -/
def KComplex.mul (z w : KComplex K) : KComplex K :=
  (z.1 * w.1 - z.2 * w.2, z.1 * w.2 + z.2 * w.1)

/-- **Complex conjugation** `(a, b) ↦ (a, −b)`. -/
def KComplex.conj (z : KComplex K) : KComplex K := (z.1, -z.2)

/-- **Algebraic norm** `‖a + bi‖² := a² + b²` valued in `K`.  Always
    non-negative. -/
def KComplex.normSq (z : KComplex K) : K := z.1 * z.1 + z.2 * z.2

/-! ### Algebraic identities for `KComplex.mul` -/

/-- Left identity for `KComplex.mul`. -/
theorem KComplex.one_mul (z : KComplex K) :
    KComplex.mul (KComplex.one K) z = z := by
  unfold KComplex.one KComplex.mul
  refine Prod.ext ?_ ?_ <;> simp

/-- Right identity for `KComplex.mul`. -/
theorem KComplex.mul_one (z : KComplex K) :
    KComplex.mul z (KComplex.one K) = z := by
  unfold KComplex.one KComplex.mul
  refine Prod.ext ?_ ?_ <;> simp

/-- `KComplex.mul` is commutative. -/
theorem KComplex.mul_comm (z w : KComplex K) :
    KComplex.mul z w = KComplex.mul w z := by
  unfold KComplex.mul
  refine Prod.ext ?_ ?_ <;> · simp; ring

/-- `KComplex.mul` is associative. -/
theorem KComplex.mul_assoc (a b c : KComplex K) :
    KComplex.mul (KComplex.mul a b) c =
      KComplex.mul a (KComplex.mul b c) := by
  unfold KComplex.mul
  refine Prod.ext ?_ ?_ <;> · simp; ring

/-! ### Imaginary-unit identity `i² = −1` -/

/-- The imaginary unit squares to `−1 + 0·i`. -/
theorem KComplex.I_mul_I :
    KComplex.mul (KComplex.I K) (KComplex.I K)
      = (-(1 : K), (0 : K)) := by
  unfold KComplex.mul KComplex.I
  refine Prod.ext ?_ ?_ <;> simp

/-! ### Conjugate identities -/

/-- Conjugation is involutive. -/
theorem KComplex.conj_conj (z : KComplex K) :
    KComplex.conj (KComplex.conj z) = z := by
  unfold KComplex.conj
  refine Prod.ext ?_ ?_ <;> simp

/-- `z · conj z = (‖z‖², 0)`. -/
theorem KComplex.mul_conj (z : KComplex K) :
    KComplex.mul z (KComplex.conj z) = (KComplex.normSq z, 0) := by
  unfold KComplex.mul KComplex.conj KComplex.normSq
  refine Prod.ext ?_ ?_ <;> · simp; try ring

/-! ### Norm-squared identities -/

/-- `‖z · w‖² = ‖z‖² · ‖w‖²` (Brahmagupta–Fibonacci). -/
theorem KComplex.normSq_mul (z w : KComplex K) :
    KComplex.normSq (KComplex.mul z w)
      = KComplex.normSq z * KComplex.normSq w := by
  unfold KComplex.mul KComplex.normSq
  simp; ring

/-- `‖z‖² ≥ 0` (always). -/
theorem KComplex.normSq_nonneg (z : KComplex K) :
    0 ≤ KComplex.normSq z := by
  unfold KComplex.normSq
  have h1 : (0 : K) ≤ z.1 * z.1 := mul_self_nonneg _
  have h2 : (0 : K) ≤ z.2 * z.2 := mul_self_nonneg _
  linarith

/-- The algebraic norm is faithful: `‖z‖² = 0 ↔ z = 0`. -/
theorem KComplex.normSq_eq_zero (z : KComplex K) :
    KComplex.normSq z = 0 ↔ z = 0 := by
  unfold KComplex.normSq
  refine ⟨fun h => ?_, fun h => ?_⟩
  · have h1 : (0 : K) ≤ z.1 * z.1 := mul_self_nonneg _
    have h2 : (0 : K) ≤ z.2 * z.2 := mul_self_nonneg _
    have ha : z.1 * z.1 = 0 := by linarith
    have hb : z.2 * z.2 = 0 := by linarith
    have ha' : z.1 = 0 := mul_self_eq_zero.mp ha
    have hb' : z.2 = 0 := mul_self_eq_zero.mp hb
    exact Prod.ext ha' hb'
  · subst h
    show (0 : K) * 0 + 0 * 0 = 0
    ring

end QOU.AppendixSurreals
