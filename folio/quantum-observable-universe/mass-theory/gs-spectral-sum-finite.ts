import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-spectral-sum-finite",
  title:
    "Finiteness of the GS residue spectral sum",
  lean: {
    ref: "qou:QOU.BraidKnot.spectral_sum_finite",
    validation: "not_checked",
  },
  uses: ["conj:gs-residue-at-root-existence"],
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "finiteness",
    "confinement-level",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
});
