import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:gs-spectral-sum-finite",
  title:
    "Finiteness of the GS residue spectral sum",
  lean: {
    ref: "qou:QOU.BraidKnot.spectral_sum_finite",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:gb-residue-spectral-sum",
    "prop:confinement-level-exists",
    "prop:confinement-level-unique",
    "prop:gs-residue-at-root-existence",
  ],
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "finiteness",
    "confinement-level",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
});
