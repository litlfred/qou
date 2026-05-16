import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-cos-resummation",
  lean: {
    ref: "qou:QOU.Interactions.q_beta_cos_resummation",
    validation: "not_checked",
  },
  title:
    "$Q_\\beta$ cos-resummation: $Q_\\beta^{A,\\cos} = Q_\\beta^A \\cdot \\cos((z-1)h/2)$ tightens the CODATA residual by $5.49\\times$ via classical-cos eigenphase symmetrization (conditional on the transfer-matrix eigenphase identification)",
  uses: [
    "prop:neutron-qvalue-symbolic",
    "prop:q-beta-spectral-bridge",
    "prop:beta-decay-transfer-matrix",
  ],
  cites: [
    "jones1985",
    "wenzl1988",
  ],
  tags: [
    "q-beta",
    "cos-resummation",
    "eigenphase-average",
    "markov-cyclicity",
    "classical-decategorification",
    "1ppb-roadmap",
    "prediction",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_q_beta_tightening_landscape.py",
    witness: [
      "folio-assistant/computations/q-beta-tightening-landscape.witness.json",
      "folio-assistant/computations/delta-S-chain-audit.witness.json",
    ],
    status: "experimental",
  },
});
