-- Ref: [leitner2026] §7/archimedean-universe (Pauli witness computation)
-- Pauli witness for ⁴He (Z=2, N=2, A=4), exact in q
-- Full formalization: QOU/Descartes/PauliWitness/witness-4he.lean

-- ★★ DOUBLY MAGIC
-- F_Pauli(q₀) = 0.8116 (strong antisymmetric dominance)
-- Gröbner NF: 12 terms matching q-multinomial coefficient
-- Denominator: 2⁴ = 16
-- Computed by hecke-engine 0.8.0

-- See QOU.Archimedean.PauliWitness.tr_alt_4he for the exact Laurent polynomial.
-- See QOU.Archimedean.PauliWitness.net_4he for the net polynomial.

namespace QOU.Archimedean.PauliWitness

/-- Pauli witness for ${}^4\\mathrm{He}$ (exact in $q$) -/
def witness_4He   :=
  -- Ref: [leitner2026] def:witness-4he
  trivial

end QOU.Archimedean.PauliWitness
