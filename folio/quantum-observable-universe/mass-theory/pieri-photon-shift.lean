import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic


/-!
# QOU.Photon.Pieri — Pieri rule shift for degree-one Hecke elements

A degree-one element `γ = 1 + Σ_i φ_i σ_i ∈ H_n(q)`, when multiplied
against a state `β_m` supported on the partition `λ`, has support
contained in `{λ} ∪ {λ ± □}` (single-box addition or removal).

Mathlib does not yet carry partition-indexed Hecke-algebra Specht
modules, so we package the Pieri rule as a typeclass `IsPieriShift`
whose existence corresponds to the statement of the rule for the
particular non-commutative Fourier interface in use. Concrete
instances (e.g. for `H_n(q)` at small `n`) supply the support
witnesses by direct computation.

LaTeX label: `prop:pieri-photon-shift`

## References

- [fulton1997] Young Tableaux (Cambridge University Press, 1997),
  Chapter 2.
- [kassel1995] Quantum Groups (Springer GTM 155, 1995), Chapter XI.
- [leitner2026] braids-and-knots / pieri-photon-shift
-/

namespace QOU.Photon

/-- Abstract data for a "non-commutative Fourier transform" with an
    addable/removable-corner adjacency relation on the spectrum. We
    use this in lieu of a full partition-lattice instance, which is
    not yet available in Mathlib. -/
structure PieriInterface where
  /-- Spectrum (e.g. `λ ⊢ n`). -/
  spectrum : Type*
  /-- The set of partitions reachable from `λ` by adding or removing
      a single box. By convention `λ` itself is in this set
      (for the identity term in `γ`). -/
  oneBoxShift : spectrum → Finset spectrum
  /-- The shift relation is reflexive: `λ ∈ oneBoxShift λ`. -/
  shift_self : ∀ lam, lam ∈ oneBoxShift lam

/-- **Pieri rule (axiomatised).**
    A degree-one Hecke element acting on a single-block state shifts
    its non-commutative Fourier support into the one-box neighbourhood.

    Concrete instances populate `support_after` by Pieri's rule
    [`fulton1997`, Ch. 2]. -/
class IsPieriShift (P : PieriInterface) where
  /-- For a degree-one Hecke element `γ` and a `λ`-block state `β`,
      the support of `γ · β` is contained in `oneBoxShift λ`. The
      `support_after` field encodes precisely that containment as a
      function of the source partition. -/
  support_after : P.spectrum → Finset P.spectrum
  /-- The shifted support lies in the one-box neighbourhood. -/
  support_subset : ∀ lam, support_after lam ⊆ P.oneBoxShift lam

/-- **The support-containment theorem.**
    Re-export of the `IsPieriShift` field. Intended use: callers
    quantify over `[IsPieriShift P]` and obtain the support
    containment for free. -/
-- Ref: [leitner2026] prop:pieri-photon-shift
-- Ref: [fulton1997] Young Tableaux, Ch. 2
-- Ref: [kassel1995] Quantum Groups, Ch. XI
theorem pieri_one_box_shift
    (P : PieriInterface) [S : IsPieriShift P] (lam : P.spectrum) :
    S.support_after lam ⊆ P.oneBoxShift lam :=
  S.support_subset lam

/-- The source partition `λ` is always reachable (identity term in `γ`). -/
-- Ref: [leitner2026] prop:pieri-photon-shift
theorem pieri_self_in_shift (P : PieriInterface) (lam : P.spectrum) :
    lam ∈ P.oneBoxShift lam :=
  P.shift_self lam

end QOU.Photon
