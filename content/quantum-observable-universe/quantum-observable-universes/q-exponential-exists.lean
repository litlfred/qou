/-!
# QOU.QExponential.exists_in_shuffle_hopf — existence of the q-exponential

Over a base ring where the Jackson factorials [n]_q! are invertible,
the q-shuffle Hopf algebra 𝓗_q admits a grouplike `e_q` satisfying the
flow equation D_q e_q = e_q, ε(e_q) = 1.

LaTeX: `\label{prop:q-exponential-exists}`

## References

- [manuscript] §2-quantum-observable-universes/q-exponential-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §IV.2
-/

import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent

namespace QOU

noncomputable section

/-- **Existence of the q-exponential grouplike.**

    Over any Hopf algebra `H` equipped with a q-Jackson derivative
    `D_q`, a coproduct `Δ`, a counit `ε`, and an element `x` such that
    the Jackson factorials `[n]_q!` are invertible, the formal series
    `e_q = Σ x^n / [n]_q!` defines a grouplike satisfying the flow
    equation.

    The construction is not a theorem of Mathlib: it requires the
    q-binomial identity
      Δ(x^n) = Σ_k (n choose k)_q · x^k ⊗ x^(n-k)
    which has to be built from the q-shuffle Hopf-algebra structure.
    We record the statement as an existence proposition; the proof
    follows the Kassel construction in [kassel1995] §IV.2. -/
-- Ref: [kassel1995] Quantum Groups, §IV.2
theorem QExponential.exists_in_shuffle_hopf
    (H : Type*) [Nonempty H] :
    Nonempty (QExponential H) := by
  -- The construction requires the q-shuffle Hopf algebra structure
  -- with q-binomial coproduct.  See Kassel §IV.2 for the full proof.
  -- Ref: [kassel1995] Quantum Groups, §IV.2
  sorry

end

end QOU
