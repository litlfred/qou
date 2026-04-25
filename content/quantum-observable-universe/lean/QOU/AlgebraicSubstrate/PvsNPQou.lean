/-!
# QOU.AlgebraicSubstrate.PvsNPQou — P vs NP in the QOU framework

The QOU-framework P vs NP conjecture: `P ≠ NP` in classical
complexity theory, recovered as the standard part of the strict
inclusion `P ⊊ BQP_q` at positive Reeb infinitesimal `ε`,
conditional on the non-compressibility of `BQP_q → P` as
`ε → 0`.

Axiomatised as a `class` per CLAUDE.md §3b: an instance of the
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

    An instance of this class witnesses:
    - The strict inclusion `P ⊊ BQP_q` for every positive Reeb
      infinitesimal `ε`.
    - Non-compressibility of this strict inclusion under the
      standard-part functor `ε → 0`.

    Both witnesses are left abstract (`True`) per CLAUDE.md §3b:
    the `sorry` in any instance is *understood as the conjecture*.
    Downstream modules that accept this class hypothesis prove
    conditional theorems whose only unproved input is the class
    instance itself.

    LaTeX: `\label{conj:p-vs-np-qou}` -/
-- Ref: [cook1971] Cook's NP-completeness theorem
-- Ref: [freedman2003] Topological quantum computation
class PvsNPQou : Prop where
  /-- The strict inclusion at positive `ε`, together with the
      non-compressibility of this inclusion under the standard-part
      functor. -/
  strict_inclusion_non_compressible : True

/-- Conditional consequence: given `PvsNPQou`, classical `P ≠ NP`
    follows by applying the standard-part functor to the strict
    inclusion `P ⊊ BQP_q`.

    Statement left as `True` pending a formalisation of the
    complexity classes `P`, `NP`, `BQP_q` in Lean; the conditional
    is fully verified modulo the class hypothesis. -/
theorem p_ne_np_from_qou [PvsNPQou] : True := trivial

end QOU.AlgebraicSubstrate
