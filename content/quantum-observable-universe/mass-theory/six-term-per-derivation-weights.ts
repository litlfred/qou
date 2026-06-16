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
});
