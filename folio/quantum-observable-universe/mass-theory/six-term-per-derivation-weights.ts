import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:six-term-per-derivation-weights",
  title: "Per-derivation weights for the six-term mass formula",
  lean: {
    ref: "qou:QOU.BraidKnot.SixTermPerDerivationWeights.binding_assembly",
    validation: "not_checked",
  },
  uses: [
    "conj:six-term-mass-formula-complete",
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
      kind: "caveat",
      date: "2026-11-16",
      body: "The headline 0.184% mean error is on TOTAL atomic mass with a CODATA nucleon baseline. On binding energy (same Table 3) the assembly gives D +3.7% but 3H -50.9%, 3He -22.3%, 4He -69.2%, 6Li -41.3%, 7Li -40.1%, 9Be -35.5%. The 'zero empirical fits' wording was replaced: no parameter is tuned, but E_{0,beta} is the CODATA Q_beta (CAL-2 proxy), not the ruled z_D base. Mass-pipeline flag; numbers unchanged.",
    },
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
