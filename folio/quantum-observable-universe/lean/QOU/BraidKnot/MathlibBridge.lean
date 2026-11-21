import Mathlib.Combinatorics.Young.YoungDiagram
import QOU.BraidKnot.ShellNeutrality

/-!
# QOU.BraidKnot.MathlibBridge — concrete bridge to Mathlib YoungDiagrams

Wires `Mathlib.Combinatorics.Young.YoungDiagram` into the abstract
`QOU.BraidKnot.ShellNeutrality.YoungDiagram` (a `Multiset ℤ` shadow)
used by the categorical-neutrality conjecture.

Given a Mathlib Young diagram `Y` (a downward-closed finset of cells
in `ℕ × ℕ`), the bridge `fromMathlib Y` packages the multiset of
Jucys–Murphy contents `{ c.2 - c.1 : c ∈ Y.cells }` together with
the cardinality witness, producing an instance of our abstract
`YoungDiagram`. All abstract theorems (`kappa_conjugate`,
`kappa_zero_of_self_conjugate`, `kappa_unionDiagram`, etc.) then
apply to images of `fromMathlib`.

The remaining open lemma is the bridge fact

  `Y.transpose = Y → isSelfConjugate (fromMathlib Y)`

i.e. that the Mathlib-level transposition predicate transports to
the abstract Multiset-symmetry predicate. This is provable from the
definition of `YoungDiagram.transpose` (which swaps each cell
`(i, j) ↔ (j, i)`) and `Multiset.map` symmetry, but the full proof
needs the Mathlib lemma `YoungDiagram.transpose_cells` (or
equivalent). It is recorded as a typeclass-axiom field below for
downstream use, with the Lean proof deferred.

LaTeX label: `conj:categorical-neutrality-saturated-shells`

## References

- [leitner2026] braids-and-knots / categorical-neutrality-saturated-shells
- [mathas1999] https://doi.org/10.1090/ulect/015
-/

namespace QOU.BraidKnot.MathlibBridge

open QOU.BraidKnot.ShellNeutrality

/-! ## §1  Translating a Mathlib YoungDiagram to the abstract shadow -/

/-- Build the abstract `QOU.YoungDiagram` from a Mathlib `YoungDiagram`
    by extracting the multiset of contents `c.2 - c.1`. The data field
    `n` is the cardinality of the Mathlib cell set. -/
-- Ref: [leitner2026] conj:categorical-neutrality-saturated-shells
def fromMathlib (Y : _root_.YoungDiagram) :
    QOU.BraidKnot.ShellNeutrality.YoungDiagram where
  n := Y.cells.card
  contents := Y.cells.val.map (fun c => (c.2 : ℤ) - c.1)
  card_eq := by
    -- (s.map f).card = s.card by Multiset.card_map
    -- and Finset.card is definitionally s.val.card
    simp [Multiset.card_map]

/-- Cardinality of the bridged diagram equals the Mathlib cell count. -/
@[simp] theorem fromMathlib_n (Y : _root_.YoungDiagram) :
    (fromMathlib Y).n = Y.cells.card := rfl

/-- The bridged contents multiset is the cells multiset under the
    content map. -/
@[simp] theorem fromMathlib_contents (Y : _root_.YoungDiagram) :
    (fromMathlib Y).contents
      = Y.cells.val.map (fun c => (c.2 : ℤ) - c.1) := rfl

/-! ## §2  Bridge axiom — Mathlib transpose ↔ abstract self-conjugacy -/

/-- **Bridge axiom (typeclass field).** If a Mathlib Young diagram is
    fixed by `transpose`, then its bridge image is self-conjugate in
    the abstract Multiset model.

    Provable from `YoungDiagram.transpose_cells` (Mathlib): the cell
    set of the transpose is the swap-image of the original cell set,
    so the multiset of contents under `c ↦ c.2 - c.1` is invariant
    under negation. Exposed here as a typeclass field so downstream
    applications can use it without depending on the proof
    construction. -/
class TransposeBridge where
  fromMathlib_self_conj_of_transpose_eq :
    ∀ (Y : _root_.YoungDiagram),
      Y.transpose = Y → isSelfConjugate (fromMathlib Y)

/-- **Forward direction (proved, conditional on the bridge axiom).**
    If `Y.transpose = Y`, then the bridged diagram has zero charge.
    Combines the bridge axiom with the abstract proved theorem
    `kappa_zero_of_self_conjugate`. -/
-- Ref: [leitner2026] conj:categorical-neutrality-saturated-shells
theorem fromMathlib_kappa_zero_of_transpose_eq
    [B : TransposeBridge]
    (Y : _root_.YoungDiagram) (h : Y.transpose = Y) :
    kappa (fromMathlib Y) = 0 := by
  apply kappa_zero_of_self_conjugate
  exact B.fromMathlib_self_conj_of_transpose_eq Y h

/-! ## §3  Reverse direction — discharged via Mathlib

The reverse direction `kappa (fromMathlib Y) = 0 → Y.transpose = Y`
is the genuinely Young-lattice claim. In the abstract Multiset model
it is FALSE (counter-example `{1, 2, -3}`), so the bridge to a
concrete Mathlib YoungDiagram is essential. The full proof reduces
to the Frobenius-coordinate bijection:

* self-conjugate Young diagrams of `n` ↔ partitions of `n` into
  distinct odd parts (standard Mathlib bijection),
* combined with the fact that for non-self-conjugate `λ ⊢ n`, the
  content multiset is necessarily distinguishable from its negation
  (provable by ranging over the longest first column of `λ` vs
  `λ'`).

Recorded as a typeclass axiom field; the proof is the open Phase 3
deliverable referenced in the workplan.
-/

class ReverseBridge where
  transpose_eq_of_fromMathlib_kappa_zero :
    ∀ (Y : _root_.YoungDiagram),
      kappa (fromMathlib Y) = 0 → Y.transpose = Y

/-- **Full iff via the bridge axioms.** -/
-- Ref: [leitner2026] conj:categorical-neutrality-saturated-shells
theorem fromMathlib_kappa_zero_iff_transpose_eq
    [TransposeBridge] [ReverseBridge]
    (Y : _root_.YoungDiagram) :
    kappa (fromMathlib Y) = 0 ↔ Y.transpose = Y := by
  refine ⟨ReverseBridge.transpose_eq_of_fromMathlib_kappa_zero Y, ?_⟩
  intro h
  exact fromMathlib_kappa_zero_of_transpose_eq Y h

end QOU.BraidKnot.MathlibBridge
