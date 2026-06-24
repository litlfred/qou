import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bar-self-dual-confinement-band",
  proofs: ["prf:bar-self-dual-confinement-band"],
  title:
    "The open interval $(1/\\varphi^2,\\,\\varphi^2)$ is the maximal bar-self-dual confinement band",
  tags: [
    "golden-ratio",
    "bar-involution",
    "skew-symmetry",
    "confinement",
    "deconfinement",
    "phase-boundary",
    "substrate-parameter",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.BarSelfDualConfBand.bar_self_dual_confinement_band",
    validation: "not_checked",
  },
  uses: [
    "prop:golden-skew-dual-node",
    "rem:deconfinement-golden-threshold",
  ],
});
