import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-cos-resummation",
  lean: {
    ref: "qou:QOU.Interactions.q_beta_cos_resummation",
    validation: "not_checked",
  },
  title:
    "$Q_\\beta$ cos-resummation: $Q_\\beta^{A,\\cos} = Q_\\beta^A \\cdot \\cos((z-1)h/2)$ tightens the CODATA residual by $5.49\\times$ via classical-cos eigenphase symmetrization (conditional on the transfer-matrix eigenphase identification)",
  uses: ["prop:q-beta-spectral-bridge"],
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
      "folio-assistant/computations/delta-S-chain-audit.witness.json"
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "Per [`audit_delta_S_chain.py`](../../folio-assistant/computations/audit_delta_S_chain.py),\nthe n-p mass-split residual $\\varepsilon_{\\Delta S}$ inherits\n$Q_\\beta$'s residual through the algebraic chain identity\n\n$$\n  \\varepsilon_{\\Delta S}\n  \\;=\\;\n  \\frac{Q_\\beta}{Q_\\beta + m_e} \\cdot \\varepsilon_Q\n  \\;\\approx\\;\n  0.605\\,\\varepsilon_Q .\n$$\n\nUnder the cos resummation:\n$\\varepsilon_Q$ drops $1678 \\to 306$ ppm, and consequently\n$\\varepsilon_{\\Delta S}$ drops $1015 \\to 185$ ppm.  This is one\nrung of the precision ladder toward the $1$ ppb target\n($\\varepsilon_Q \\approx 0.0017$ ppm).  The remaining $305$ ppm\ngap calls for the **3-irrep** extension: $V_{(3)}$ and\n$V_{(1,1,1)}$ contribute at $O(h^2)$ to $\\tau_M$ but are not yet\nincluded in the single-eigenphase resummation above.",
    },
    {
      kind: "status",
      body: "This proposition is **conditional** on\n[`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix)'s\nidentification of $\\alpha = (z-1)h/2$ as the single-wrap eigenphase\non $V_{(2,1)}$.  The Lean class\n[`QOU.Interactions.QBetaCosResummation`](q-beta-cos-resummation.lean)\naxiomatises that identification; the cos-resummation theorem then\nfollows from the Markov-cyclicity constraint (1) above by `ring`\non the $\\alpha$ symbolic identity, with the empirical $5.49\\times$\ntightening recorded in the\n[`q-beta-tightening-landscape`](../../folio-assistant/computations/q-beta-tightening-landscape.witness.json)\nwitness as numerical evidence.",
    },
  ],
});
