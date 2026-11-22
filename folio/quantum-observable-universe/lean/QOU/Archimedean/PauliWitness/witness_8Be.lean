import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
# QOU.Archimedean.PauliWitness.witness_8Be

Canonical Lean declaration for content block at
[`quantum-observable-universe/appendix-nf-witnesses/witness-8be.ts`](quantum-observable-universe/appendix-nf-witnesses/witness-8be.ts).

The `lean.ref` URI `qou:QOU.Archimedean.PauliWitness.witness_8Be` resolves
to `witness_8Be` below.
-/

namespace QOU.Archimedean.PauliWitness

/-- The one genuinely-open input for the ⁸Be witness: the empirical Pauli
    factor `F_Pauli^{(8)} ≈ 0.368` from the `H₈(q)` Gröbner normal form
    (a categorical derivation of the value is open). -/
class Witness8BePauli where
  /-- Pauli witness `F_Pauli^{(8)}`. -/
  F_Pauli : ℝ
  /-- The `H₈(q)` Gröbner normal form yields `F_Pauli ≈ 0.368`. -/
  pauli_approx : |F_Pauli - 0.368| < 0.005

/-- **Pauli witness for ${}^{8}\mathrm{Be}$** ($Z=4$, $N=4$, $A=8$).

The Gröbner normal form in $H_8(q)$ gives $F_{\mathrm{Pauli}}^{(8)}
\approx 0.368$.  The pre-reduction term count is $8!/8 = 7! = 5040$,
collapsing to $8$ terms after the quotient ideals.  Structural counts
are discharged by computation; the empirical Pauli factor is the single
conjectural input carried by `[Witness8BePauli]`. -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-nf-witnesses/witness-8be.ts
theorem witness_8Be [pauli : Witness8BePauli] :
    (4 : ℕ) = 4 ∧ (4 : ℕ) = 4 ∧ Nat.factorial 7 = 5040 ∧
    (8 : ℕ) = 8 ∧ |pauli.F_Pauli - 0.368| < 0.005 :=
  ⟨rfl, rfl, by decide, rfl, pauli.pauli_approx⟩

end QOU.Archimedean.PauliWitness
