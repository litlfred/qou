import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lp-dual-stability",
  lean: { ref: "qou:QOU.ParticleInteractions.lp_dual_stability", validation: "not_checked" },
  title:
    "LP dual stability: confined hadrons have bounded shadow prices",
  tags: [
    "lp-duality",
    "stability",
    "confinement",
    "frobenius",
    "gram-matrix",
    "shadow-price",
    "hadron",
    "quark",
  ],
  uses: ["rem:confinement-nucleon-unit"],
});
