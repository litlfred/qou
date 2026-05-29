import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gs-archimedean-agreement-trace",
  title:
    "Archimedean agreement: Habiro polynomial trace evaluates to GB mass",
  lean: {
    ref:
      "qou:QOU.BraidKnot.HabiroResidueSumEquivalence.archimedean_agreement",
    validation: "not_checked",
  },
  uses: [
    "prop:habiro-residue-sum-equivalence",
    "def:archimedean-realization-functor",
    "prop:gs-spectral-decomposition-existence",
  ],
  cites: ["habiro2004"],
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "habiro-ring",
    "archimedean-agreement",
    "equivalence",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
});
