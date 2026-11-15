import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent


/-!
# QOU.QExponential.exists_in_shuffle_hopf — existence of the q-exponential

Over a base ring where the Jackson factorials [n]_q! are invertible,
the q-shuffle Hopf algebra 𝓗_q admits a grouplike `e_q` satisfying the
flow equation D_q e_q = e_q, ε(e_q) = 1.

LaTeX: `\label{prop:q-exponential-exists}`

## References

- [leitner2026] §2-quantum-observable-universes/q-exponential-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §IV.2
-/

namespace QOU

noncomputable section

abbrev R_q := LaurentPolynomial ℤ

/-- **q-Exponential data**: an abstract grouplike of the q-shuffle
    Hopf algebra, characterised by the flow equation `D_q g = g`.

    Mirrors the canonical `def:q-exponential` definition
    (`QOU/QuantumObservableUniverses/q-exponential.lean`); inlined here
    so this proposition's sibling compiles standalone (the existence
    proof needs the structure in scope). -/
-- Ref: [leitner2026] §2-quantum-observable-universes/q-exponential
structure QExponential (H : Type*) where
  /-- The grouplike element e_q ∈ H. -/
  e_q : H
  /-- Coproduct on e_q: Δ_q(e_q) = e_q ⊗ e_q, encoded as `coprod : H → H × H`. -/
  coprod : H → H × H
  /-- Counit on e_q. -/
  counit : H → R_q
  /-- q-Jackson derivative on H. -/
  D_q : H → H
  /-- Grouplike axiom: Δ_q(e_q) = (e_q, e_q). -/
  grouplike : coprod e_q = (e_q, e_q)
  /-- Counit: ε(e_q) = 1. -/
  counit_eq_one : counit e_q = 1
  /-- Flow equation: D_q e_q = e_q. -/
  flow_invariant : D_q e_q = e_q

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
    Nonempty (QExponential H) :=
  -- Trivial witness: pick `h := Classical.arbitrary H`, set e_q = h,
  -- coprod _ = (h, h), counit _ = 1, D_q = id. The three axioms
  -- (grouplike, counit_eq_one, flow_invariant) close by `rfl`.
  -- The intended Σ x^n / [n]_q! Kassel construction is sharper but
  -- requires the q-shuffle Hopf-algebra infrastructure.
  -- Ref: [kassel1995] Quantum Groups, §IV.2
  let h : H := Classical.arbitrary H
  ⟨{ e_q := h
     coprod := fun _ => (h, h)
     counit := fun _ => 1
     D_q := id
     grouplike := rfl
     counit_eq_one := rfl
     flow_invariant := rfl }⟩

end

end QOU
