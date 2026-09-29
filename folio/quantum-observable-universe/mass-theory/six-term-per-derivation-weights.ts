import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:six-term-per-derivation-weights",
  title: "Per-derivation weights for the six-term mass formula",
  lean: {
    ref: "qou:QOU.BraidKnot.SixTermPerDerivationWeights.binding_assembly",
    validation: "not_checked",
  },
  uses: [
    "thm:six-term-mass-formula-complete",
    "prop:chirality-dual-space-derivation",
    "prop:full-pole-structure-mass-trace",
  ],
  cites: [],
  computation: {
    engine: "python",
    script: "computations/sweeps/paper_six_term_isotope_sweep.py",
    witness: [
      "computations/sweeps/paper-six-term-isotope-sweep.witness.json",
      "computations/codata-masses.witness.json",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/BraidKnot/SixTermPerDerivationWeights/binding_assembly.lean` " +
        "carries `atomic_mass` and the six per-derivation `term_weights` as physical quantities. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
