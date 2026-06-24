import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bar-t-duality-substrate",
  proofs: ["prf:bar-t-duality-substrate"],
  title:
    "Substrate-level bar T-duality: $\\mathcal{E}_q \\leftrightarrow \\mathcal{E}_{1/q}$",
  tags: [
    "t-duality",
    "bar-involution",
    "skew-symmetry",
    "elliptic-curve",
    "substrate-parameter",
    "hecke-bar",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.BarTDualitySubstrate.bar_t_duality_substrate",
    validation: "not_checked",
  },
  uses: [
    "rem:t-duality-elliptic",
    "prop:bar-self-dual-confinement-band",
  ],
});
