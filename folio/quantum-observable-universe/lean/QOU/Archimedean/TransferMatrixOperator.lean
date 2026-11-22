import Mathlib.Tactic

/-!
# QOU.Archimedean.TransferMatrixOperator

**Canonical declaration** for content block at
[`quantum-observable-universe/mass-theory/transfer-matrix-operator-properties.ts`](quantum-observable-universe/mass-theory/transfer-matrix-operator-properties.ts).

Formalises the manuscript action of the transfer matrix `T = cσ + d` on a
Gröbner–Shirshov-reduced Hecke chain `aσ + b`: left-multiply and reduce with
the Hecke relation `σ² = (q − q⁻¹)σ + 1`, giving `a'σ + b'` with

`a' = ca(q − q⁻¹) + cb + da`,  `b' = ca + db`.

Generic over any field (§7c: `q⁻¹` needs `Field`; no ordering/archimedean use).
-/

namespace QOU.Archimedean

/-- Data for the transfer-matrix reduction `(cσ+d)(aσ+b) → a'σ + b'`.

    A `definition` carrier: the substrate `q` and the two reduced
    coordinates `reduceA = a'`, `reduceB = b'` pinned to the Hecke-reduced
    coefficients of the product. -/
structure TransferMatrixOperator (R : Type*) [Field R] where
  /-- Substrate parameter `q`. -/
  q : R
  /-- Reduced `σ`-coefficient `a'` of `(cσ+d)(aσ+b)`. -/
  reduceA : R → R → R → R → R
  /-- Reduced constant `b'` of `(cσ+d)(aσ+b)`. -/
  reduceB : R → R → R → R → R
  /-- `a' = ca(q − q⁻¹) + cb + da` (the `σ`-part after `σ² = (q−q⁻¹)σ + 1`). -/
  reduceA_def : ∀ a b c d : R,
    reduceA a b c d = c * a * (q - q⁻¹) + c * b + d * a
  /-- `b' = ca + db` (the constant part). -/
  reduceB_def : ∀ a b c d : R, reduceB a b c d = c * a + d * b

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/transfer-matrix-operator-properties.ts

/-- The identity operator `T = 0·σ + 1` acts trivially: `(aσ+b) ↦ aσ + b`. -/
theorem reduce_identity {R : Type*} [Field R]
    (T : TransferMatrixOperator R) (a b : R) :
    T.reduceA a b 0 1 = a ∧ T.reduceB a b 0 1 = b := by
  refine ⟨?_, ?_⟩
  · rw [T.reduceA_def]; ring
  · rw [T.reduceB_def]; ring

/-- Reducing `σ·σ` (i.e. `T = σ` acting on `σ`, `a=c=1`, `b=d=0`) recovers the
    Hecke relation `σ² = (q − q⁻¹)σ + 1`. -/
theorem TransferMatrixOperator.reduce_sigma_squared {R : Type*} [Field R]
    (T : TransferMatrixOperator R) :
    T.reduceA 1 0 1 0 = T.q - T.q⁻¹ ∧ T.reduceB 1 0 1 0 = 1 := by
  refine ⟨?_, ?_⟩
  · rw [T.reduceA_def]; ring
  · rw [T.reduceB_def]; ring

end QOU.Archimedean
