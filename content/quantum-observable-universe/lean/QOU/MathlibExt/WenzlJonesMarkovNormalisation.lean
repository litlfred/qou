import QOU.MathlibExt.WenzlSchurElementBridge
import QOU.SchurWeyl.WenzlNormalisation
import QOU.Mathlib.SYTEnumerationFintype

/-!
# QOU.MathlibExt.WenzlJonesMarkovNormalisation — the unconditional M1 on the List carrier

The Markov-trace normalisation `tr_M(𝟙) = 1` for the concrete List-carrier
Jones–Markov weights `jonesMarkovCoeff`, **general `n`, unconditional** — derived
from (not assumed alongside) the general Macdonald hook telescope already proved
on the YoungDiagram carrier.

The general telescope is `QOU.SchurWeyl.sum_dim_wenzlWeight_eq_one`:

  `∑_{ν : |ν| = n} f^ν · wenzlWeight r Q ν = 1`,

sorry-free for every level `r` and rank `n`. The **carrier bridge**
(`WenzlSchurElementBridge.schurElement_eq_schurPrincipal`) plus
`YoungDiagram.ofRowLens_to_rowLens_eq_self` gives, per diagram,

  `jonesMarkovCoeff Q (Q^r) ν.rowLens = wenzlWeight r Q ν`,

so the two sums are termwise equal and the List-carrier weights inherit the
normalisation. This discharges — for the principal specialisation `X = Q^r` —
the conditional `jonesMarkov_normalisation_of_telescope`, on the natural index
set (the SYT-weighted diagrams of size `n`) rather than an ad-hoc partition list.

## References

- [wenzl1988] Wenzl, "Hecke algebras of type $A_n$ and subfactors," Invent. Math. 92.
- [macdonald1995] Macdonald, *Symmetric Functions and Hall Polynomials*, §I.3.
-/

namespace QOU.MathlibExt.WenzlJonesMarkovNormalisation

open QOU.MathlibExt.WenzlSchurElement
open QOU.MathlibExt.QPartitionCombinatorics

/-- The sum of a diagram's row lengths is its number of cells. Reuses
`card_cells_ofRowLens` on `μ.rowLens`, which reconstitutes `μ` via
`ofRowLens_to_rowLens_eq_self`. -/
theorem rowLens_sum_eq_card (ν : YoungDiagram) : ν.rowLens.sum = ν.cells.card := by
  have h := QOU.Mathlib.SYTEnum.card_cells_ofRowLens ν.rowLens ν.rowLens_sorted
  rw [YoungDiagram.ofRowLens_to_rowLens_eq_self] at h
  exact h.symm

/-- The Wenzl level bracket `[r]_Q = ∑_{i<r} Q^i` in the `(1−X)/(1−Q)` form used
by `wenzlNormalisation` at `X = Q^r`. -/
theorem levelBracket_eq (r : ℕ) (Q : ℝ) (hQ1 : Q ≠ 1) :
    QOU.SchurWeyl.levelBracket r Q = (1 - Q ^ r) / (1 - Q) := by
  unfold QOU.SchurWeyl.levelBracket
  rw [geom_sum_eq hQ1, ← neg_sub 1 (Q ^ r), ← neg_sub 1 Q, neg_div_neg_eq]

/-- **Per-diagram carrier identity.** The List-carrier Jones–Markov weight on the
row-length list of `ν` is the YoungDiagram-carrier Wenzl weight of `ν`, at the
principal specialisation `X = Q^r`. Numerator by the carrier bridge
(`schurElement Q (Q^r) ν.rowLens = schurPrincipal r Q ν`), denominator by
`wenzlNormalisation (|ν|) = [r]_Q^{|ν|}`. -/
theorem jonesMarkovCoeff_rowLens_eq_wenzlWeight (r : ℕ) (Q : ℝ) (hQ0 : Q ≠ 0)
    (hQ1 : Q ≠ 1) (ν : YoungDiagram) :
    jonesMarkovCoeff Q (Q ^ r) ν.rowLens = QOU.SchurWeyl.wenzlWeight r Q ν := by
  unfold jonesMarkovCoeff QOU.SchurWeyl.wenzlWeight
  rw [QOU.MathlibExt.WenzlSchurElementBridge.schurElement_eq_schurPrincipal r Q hQ0
        ν.rowLens ν.rowLens_sorted ν.pos_of_mem_rowLens,
      YoungDiagram.ofRowLens_to_rowLens_eq_self]
  congr 1
  rw [wenzlNormalisation, ← levelBracket_eq r Q hQ1]
  congr 1
  show ν.rowLens.sum = ν.cells.card
  exact rowLens_sum_eq_card ν

/-- **The unconditional M1 on the List carrier.** For the principal specialisation
`X = Q^r`, the concrete Jones–Markov weights, summed over the SYT-weighted
diagrams of size `n`, normalise to one:

  `∑_{ν : |ν| = n} f^ν · jonesMarkovCoeff Q (Q^r) ν.rowLens = 1`.

Termwise equal (via `jonesMarkovCoeff_rowLens_eq_wenzlWeight`) to the proved
`QOU.SchurWeyl.sum_dim_wenzlWeight_eq_one`; the normalisation is *derived*, not
assumed. -/
theorem sum_dim_jonesMarkovCoeff_eq_one (r : ℕ) (Q : ℝ) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hbr : QOU.SchurWeyl.levelBracket r Q ≠ 0)
    (hQ1 : Q ≠ 1) (n : ℕ) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ)
          * jonesMarkovCoeff Q (Q ^ r) ν.1.rowLens) = 1 := by
  have hcongr : ∀ ν : {ν : YoungDiagram // ν.cells.card = n},
      (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ)
          * jonesMarkovCoeff Q (Q ^ r) ν.1.rowLens
        = (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ)
          * QOU.SchurWeyl.wenzlWeight r Q ν.1 := by
    intro ν
    rw [jonesMarkovCoeff_rowLens_eq_wenzlWeight r Q hQ0 hQ1 ν.1]
  rw [Finset.sum_congr rfl (fun ν _ => hcongr ν)]
  exact QOU.SchurWeyl.sum_dim_wenzlWeight_eq_one Q hQ0 hgen hbr hQ1 n

end QOU.MathlibExt.WenzlJonesMarkovNormalisation
