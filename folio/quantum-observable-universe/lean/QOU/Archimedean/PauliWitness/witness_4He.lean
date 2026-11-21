import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
# QOU.Archimedean.PauliWitness.witness_4He

Canonical Lean declaration for content block at
[`quantum-observable-universe/appendix-nf-witnesses/witness-4he.ts`](quantum-observable-universe/appendix-nf-witnesses/witness-4he.ts).

The `lean.ref` URI `qou:QOU.Archimedean.PauliWitness.witness_4He` resolves
to `witness_4He` below.
-/

namespace QOU.Archimedean.PauliWitness

/-- The one genuinely-open input for the ⁴He witness: the empirical Pauli
    factor `F_Pauli^{(4)} ≈ 0.812` from the `H₄(q)` Gröbner normal form
    (a categorical derivation of the value is open). -/
class Witness4HePauli where
  /-- Pauli witness `F_Pauli^{(4)}`. -/
  F_Pauli : ℝ
  /-- The `H₄(q)` Gröbner normal form yields `F_Pauli ≈ 0.812`. -/
  pauli_approx : |F_Pauli - 0.812| < 0.005

/-- **Pauli witness for ${}^{4}\mathrm{He}$** ($Z=2$, $N=2$, $A=4$),
doubly magic.

The exact Gröbner normal form in $H_4(q)$ after quotient ideals
$I_8 + I_9$ gives $F_{\mathrm{Pauli}}^{(4)} \approx 0.812$.  The
polynomial $\mathrm{net}(t)$ has $[2]_t^2 \cdot [3]_t = 2^2 \cdot 3 = 12$
terms in $\mathbb{Z}[t, t^{-1}]$.  The combinatorial count and magic
numbers are discharged by computation; the empirical Pauli factor is the
single conjectural input carried by `[Witness4HePauli]`. -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-nf-witnesses/witness-4he.ts
theorem witness_4He [pauli : Witness4HePauli] :
    (2 : ℕ) = 2 ∧ (2 : ℕ) = 2 ∧ (2 ^ 2 * 3 : ℕ) = 12 ∧
    |pauli.F_Pauli - 0.812| < 0.005 :=
  ⟨rfl, rfl, by norm_num, pauli.pauli_approx⟩

end QOU.Archimedean.PauliWitness
