import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spectral-sequence-collapse",
  title: "GB spectral sequence collapses at E_1 (semisimple cohomology vanishing)",
  lean: {
    ref: "qou:QOU.WedderburnMass.spectral_sequence_collapse",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:three-parameters-wedderburn",
    "prop:curvature-rank-gb-stratification",
    "thm:knot-mass-formula-unified",
    "prop:categorical-mass-markov",
  ],
});
