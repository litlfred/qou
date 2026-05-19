import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-spectral-bridge",
  lean: {
    ref: "qou:QOU.Interactions.q_beta_spectral_bridge",
    validation: "not_checked",
  },
  title:
    "$Q_\\beta$ spectral bridge: Form A (NF counit) and Form B (transfer-matrix log-ratio) are the same observable in different bases",
  uses: [
    "prop:neutron-qvalue-symbolic",
    "prop:beta-decay-transfer-matrix",
    "conj:archimedean-remainder-exponential-decay",
  ],
  cites: [
    "wenzl1988",
    "jones1985",
  ],
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/gram-matrix-dual.py",
    witness: "folio-assistant/computations/gram-matrix-dual.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "spectral-bridge",
    "basis-change",
    "markov-parameter",
    "eigenfunction-dampening",
    "beta-decay",
    "prediction",
  ],
});
