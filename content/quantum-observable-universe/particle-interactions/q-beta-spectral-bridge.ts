import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-spectral-bridge",
  lean: {
    ref: "qou:QOU.Interactions.q_beta_spectral_bridge",
    validation: "not_checked",
  },
  title:
    "$\\mathfrak{Q}_\\beta$ spectral bridge: Form A (NF counit) and Form B (transfer-matrix log-ratio) are the same observable in different bases",
  uses: ["prop:neutron-qvalue-symbolic"],
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
  authorNotes: [
    {
      kind: "status",
      body: "* Form A is the canonical predictor used in\n  [prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)\n  ($+0.168\\%$ residual vs CODATA at $N = 0$).\n* Form B is mathematically equivalent via the bridge above; it is\n  retained because the eigenfunction basis is the natural one for\n  $N \\geq 1$ truncation analysis and for the general atom-level\n  binding cascade (where the brane-tower truncation is non-trivial).\n* The exponential-remainder bound is the open conjectural input\n  (conj:archimedean-remainder-exponential-decay);\n  the Taylor-expansion algebra above is unconditional.",
    },
  ],
});
