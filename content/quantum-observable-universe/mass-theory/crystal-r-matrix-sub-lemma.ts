import { proposition } from "../../schema/builders";

/**
 * Operator-valued Sub-lemma 2.1 in crystal-R-matrix form.
 *
 * Closes the operator-valued residual of `prop:confinement-nf-partial-proof`
 * Theorem T_2 conditional on `conj:crystal-graph-realization`.
 *
 * Statement (audit Step 2): the matrix-entry pole order of
 * A^λ_{μν}(σ_i) at q = 0 on any SYT T in the (μ, ν)-block is
 *   1 iff ρ_T(i) ≤ -1, else 0
 * where ρ_T(i) = c(cell of i+1) - c(cell of i) is the axial distance
 * and c(cell) = col - row.
 *
 * Recovers α_shift(T_{(p,k)}) = k(p-1) (prop:alpha-shift-torus-knot)
 * combinatorially via column-SYT axial-distance counting (audit Step 4).
 * Verified numerically by `crystal_pole_order.py` (21/21 assertions,
 * including AXKIA chain T_{2,9}=9 and T_{3,5}=10).
 *
 * Conditional-class status (AGENTS.md §3b-cond): the upstream
 * `conj:crystal-graph-realization` is class-axiomatised as
 * `QOU.BraidKnot.CrystalGraphRealization`.  This block declares a
 * downstream class `CrystalRMatrixSubLemma` taking the upstream as
 * an `[Instance]` hypothesis, and a trivial model proving consistency.
 */
export default proposition({
  label: "prop:crystal-r-matrix-sub-lemma",
  title:
    "Crystal R-matrix Sub-lemma 2.1 (operator-valued)",
  uses: [
    "conj:crystal-graph-realization",
    "prop:alpha-shift-torus-knot",
  ],
  cites: [
    "mathas1999",
    "hoefsmit1974",
    "wenzl1988",
    "brundankleshchev2009",
    "kashiwara1991",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.CrystalRMatrixSubLemma",
    validation: "stub",
  },
  computation: {
    engine: "python",
    script: "computations/crystal_pole_order.py",
    witness: [
      "computations/crystal-pole-order.witness.json",
    ],
    status: "verified",
    requires: [],
  },
  tags: [
    "crystal-r-matrix",
    "sub-lemma-2-1",
    "operator-valued",
    "pole-order",
    "axial-distance",
    "hecke-branching",
    "conditional-class",
    "section-3b-cond",
  ],
});
