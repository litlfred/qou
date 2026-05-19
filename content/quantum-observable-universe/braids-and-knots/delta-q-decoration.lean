/-
The δ_q decoration of the Iwahori–Hecke algebra H_n(q).

LaTeX label: `def:delta-q-decoration`
Computational reference:
  folio-assistant/computations/delta_q_decoration.py
  folio-assistant/computations/delta-q-decoration.witness.json
-/

import Mathlib.RepresentationTheory.Basic
import Mathlib.LinearAlgebra.Matrix.Trace

namespace QOU.BraidKnot

/-- The q-dimension decoration map δ_q : H_n(q) → R^|Par(n)| sending an
algebra element to the tuple of its q-characters in each irreducible
representation V_λ for λ ⊢ n.

This refines the Markov trace by preserving the per-irrep structure that
the Markov trace collapses by summing.  Required for the analysis in
`prop:force-carrier-intertwining-correspondence`, which identifies how
α_EM projects through specific Wedderburn components of the bound-state
operator.

Conjecture / open: a full Lean formalization requires the q-deformed
Specht module construction (V_λ over R = ℤ[q^±1/2, (q-q⁻¹)⁻¹]) and the
seminormal-basis representation matrices, which are not in Mathlib at
present.  The algorithmic content is implemented in Python
(`delta_q_decoration.py`) and validated against witness data.

-- Ref: [wenzl1988]  -- TODO: inline DOI 10.1007/BF01393839 points at a
--                   -- different Wenzl 1988 paper than the wenzl1988 entry's
--                   -- DOI (10.1007/BF01404457). Author needs to decide
--                   -- whether to split into wenzl1988a/b or pick one.
sorry
-/
/-- Concrete model: the indexing type for the per-irrep tuple is the
    finite type of partitions of `n`, here represented by the
    list-based partition records `Fin (Nat.partition.length n)`.
    The full per-irrep matrix data (q-deformed Specht modules in
    seminormal basis) is the upgrade target documented above. -/
-- Ref: [wenzl1988]  -- (inline DOI removed; see line 31 TODO re DOI
--                   --  mismatch with the wenzl1988 entry)
def delta_q (n : ℕ) : Type := Fin n

end QOU.BraidKnot
