import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-graded-markov-trace-existence",
  title:
    "Existence of the graded Markov trace on the GS filtration",
  lean: {
    ref: "qou:QOU.BraidKnot.GBResidueSpectralSum.gradedTrace",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:gb-residue-spectral-sum",
    "prop:graded-markov-trace-from-gs-filtration",
    "def:confinement-level",
    "thm:jones-markov-trace",
  ],
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "graded-trace",
    "markov-trace",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
});
