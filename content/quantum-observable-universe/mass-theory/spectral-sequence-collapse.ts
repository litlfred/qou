import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spectral-sequence-collapse",
  proofs: ["prf:spectral-sequence-collapse"],
  title: "GB spectral sequence collapses at E_1 (semisimple cohomology vanishing)",
  lean: {
    ref: "qou:QOU.WedderburnMass.spectral_sequence_collapses_to_centre",
    validation: "not_checked",
  },
  uses: ["prop:curvature-rank-gb-stratification"],
});
