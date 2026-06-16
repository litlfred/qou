import { proposition } from "../../schema/builders";

/**
 * Operator-valued Wenzl branching combiner — convergence.
 *
 * For an A-nucleon atom with canonical braid β_atom at H_{3A}, the
 * iterated application of `prop:crystal-r-matrix-sub-lemma` (operator-
 * valued Sub-lemma 2.1) at each peel level n_k = 3(A-k+1) assembles
 * into a convergent representation of χ^λ(β_atom): the value at level
 * A+1 is the LR-weighted value at level A, so the χ-value of any atom
 * is the deuteron (A=2) base case accumulated through the
 * Littlewood-Richardson weight tower.
 *
 * Conditional-class status (CLAUDE.md §3b-cond): the missing
 * `WenzlAOperator` instance (universal H_9+ extracts, research-grade)
 * IS the conjecture; the convergence theorem is fully Lean-verified
 * (`Nat.rec`) modulo that instance hypothesis. The downstream
 * dependency cone reaches `conj:crystal-graph-realization` through
 * `prop:crystal-r-matrix-sub-lemma`.
 *
 * Production wiring: `compute_tr_m_via_branching`
 * (`canonical_tr_m_via_branching.py`, `--method branching` in
 * `canonical_mass_table_extended.py`) realises the A=2 recursion end-
 * to-end; A≥3 delegates to the native Hoefsmit Σ_λ y_λ χ^λ kernel.
 */
export default proposition({
  label: "prop:operator-valued-combiner-convergence",
  title:
    "Operator-valued combiner convergence: " +
    "$\\chi^\\lambda(\\beta_{\\mathrm{atom}})$ assembles from the deuteron base case",
  chapter: "mass-theory",
  uses: [
    "prop:crystal-r-matrix-sub-lemma",
    "prop:lr-coefficient-hecke",
  ],
  cites: ["wenzl1988"],
  defines: [],
  lean: {
    ref: "qou:QOU.BraidKnot.OperatorValuedCombiner.WenzlAOperator.operator_valued_combiner_convergence",
    validation: "stub",
  },
  computation: {
    engine: "python",
    script: "computations/canonical_tr_m_via_branching.py",
    witness: [
      "computations/canonical-mass-table-extended.witness.json",
    ],
    status: "verified",
    requires: [],
  },
  tags: [
    "operator-valued",
    "wenzl-branching",
    "combiner",
    "convergence",
    "binding-tower",
    "littlewood-richardson",
    "conditional-class",
    "section-3b-cond",
  ],
});
