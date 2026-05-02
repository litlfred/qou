import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-archimedean-agreement-residue",
  title:
    "Archimedean agreement (proton instance): degree-48 Habiro trace at $u_0$",
  lean: {
    ref:
      "qou:QOU.BraidKnot.HabiroResidueSumEquivalence.protonExample.archimedean_agreement",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:habiro-residue-sum-equivalence",
    "conj:gs-archimedean-agreement-trace",
    "conj:gs-spectral-decomposition-existence",
  ],
  cites: ["habiro2004"],
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "habiro-ring",
    "archimedean-agreement",
    "proton",
    "concrete-instance",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
});
