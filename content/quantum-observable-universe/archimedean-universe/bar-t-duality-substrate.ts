import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bar-t-duality-substrate",
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
    ref: "qou:QOU.Descartes.BarTDualitySubstrate.bar_t_duality_substrate",
    validation: "not_checked",
  },
  uses: [
    "prop:descartes-elliptic-curve",
    "rem:t-duality-elliptic",
    "prop:golden-skew-dual-node",
    "prop:bar-self-dual-confinement-band",
  ],
});
