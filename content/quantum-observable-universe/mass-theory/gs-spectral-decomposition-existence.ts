import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-spectral-decomposition-existence",
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
    "conj:gs-graded-markov-trace-existence",
    "conj:gs-residue-at-root-existence",
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
