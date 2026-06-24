import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:transfer-matrix-identities",
  proofs: ["prf:transfer-matrix-identities"],
  lean: { ref: "qou:QOU.ParticleInteractions.transfer_matrix_identities", validation: "not_checked" },
  title: "Transfer matrix identities: $T_{pp}T_{nn} = I$ and $T_{pn}^2 = [2]_q^2/4 \\cdot I$",
  uses: [
    "prop:beta-decay-transfer-matrix",
    "def:typed-crossing-operator",
  ],
  tags: [
    "transfer-matrix",
    "identity",
    "hecke-algebra",
    "inverse",
    "binding",
  ],
});
