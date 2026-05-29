import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gs-spectral-decomposition-existence",
  title:
    "Spectral decomposition of the mass into descended trace and residue sum",
  lean: {
    ref: "qou:QOU.BraidKnot.GBResidueSpectralSum.spectral_decomposition",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:gb-residue-spectral-sum",
    "prop:graded-trace-residue-split",
    "prop:gs-graded-markov-trace-existence",
    "prop:gs-residue-at-root-existence",
    "thm:knot-mass-formula-unified",
  ],
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "mass",
    "spectral-decomposition",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
});
