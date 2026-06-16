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
  uses: ["conj:gs-archimedean-agreement-trace"],
  cites: ["habiro2004"],
  computation: {
    engine: "sympy",
    script: "computations/term6_full_pole_sum.py",
    witness: [
      "computations/term6-full-pole-sum.witness.json",
      "computations/q-pinning-50-digit.witness.json",
    ],
    status: "verified",
  },
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
