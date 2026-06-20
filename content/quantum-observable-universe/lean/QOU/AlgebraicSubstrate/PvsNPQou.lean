/-!
# QOU.AlgebraicSubstrate.PvsNPQou — P vs NP in the QOU framework

The QOU-framework P vs NP conjecture: `P ≠ NP` in classical
complexity theory, recovered as the standard part of the strict
inclusion `P ⊊ BQP_q` at positive Reeb infinitesimal `ε`,
conditional on the non-compressibility of `BQP_q → P` as
`ε → 0`.

Axiomatised as a `class` per AGENTS.md §3b: an instance of the
class corresponds to a proof of the conjecture.  Downstream
consequences (e.g. separation of specific complexity classes) are
stated as conditional theorems under a `[PvsNPQou]` hypothesis.

LaTeX label: `conj:p-vs-np-qou`.

## References

- [cook1971] Cook, *The complexity of theorem-proving procedures*,
  STOC 1971. DOI:10.1145/800157.805047.
- [freedman2003] Freedman–Kitaev–Larsen–Wang, *Topological Quantum
  Computation*, Bull. AMS 40 (2003) 31–38.
- [manuscript] Chapter 8 §5 (P vs NP in the QOU).
-/

namespace QOU.AlgebraicSubstrate

/-- **PvsNPQou**: the QOU-framework P vs NP conjecture.

    Encoded as an empty marker `Prop` class per AGENTS.md §3b.
    The complexity classes `P`, `NP`, `BQP_q` are not yet
    formalised in Lean, so the meaningful Prop content cannot
    be written down at this layer; the class therefore carries
    no fields and serves only as a typeclass hypothesis on
    downstream conditional theorems.

    The narrative formulation lives in `conj:p-vs-np-qou` in the
    `algebraic-substrate` chapter.  Informally, an instance of
    this class is intended to witness:

    * the strict inclusion `P ⊊ BQP_q` for every positive Reeb
      infinitesimal `ε`, AND
    * non-compressibility of this strict inclusion under the
      standard-part functor `ε → 0`.

    The `Ow`-valuation reading (cost > budget, `1 > -3`) is
    recorded in `rem:p-vs-np-surreal-bound`.  Both bullet points
    above will become explicit `Prop` fields once `P`, `NP`, and
    `BQP_q` have Mathlib-level definitions.

    LaTeX: `\label{conj:p-vs-np-qou}` -/
-- Ref: [cook1971] Cook's NP-completeness theorem
-- Ref: [freedman2003] Topological quantum computation
class PvsNPQou : Prop

end QOU.AlgebraicSubstrate
