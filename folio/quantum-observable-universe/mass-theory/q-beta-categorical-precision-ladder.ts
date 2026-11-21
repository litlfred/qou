import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-categorical-precision-ladder",
  lean: {
    ref: "qou:QOU.BraidKnot.q_beta_categorical_precision_ladder",
    validation: "not_checked",
  },
  title:
    "$\\mathfrak{Q}_\\beta$ categorical-derivation precision ladder",
  uses: [],
  cites: [
    "jones1985",
    "wenzl1988",
    "kashiwara1990",
    "hoefsmit1974",
  ],
  tags: [
    "q-beta",
    "categorical-derivation",
    "precision-ladder",
    "kashiwara-crystal",
    "hopf-jones",
    "classical-limit",
    "KL-decategorification",
    "1ppb-roadmap",
    "n-p-mass-split",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/qbeta/qbeta_precision_ladder_n5.py",
    witness: [
      "computations/qbeta/qbeta-precision-ladder-n5.witness.json",
      "computations/q-beta-operator-valued-N3.witness.json",
      "computations/delta-S-chain-audit.witness.json"
    ],
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): (per [$\\mathfrak{Q}_\\beta$ spectral bridge](#conj:q-beta-spectral-bridge))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): from [Symbolic $Q$-value of free neutron decay](#prop:neutron-qvalue-symbolic)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , below the $0.0094$ ppm $N=3$ c(K) ceiling from the [exponential decay of the archimedean brane-tower truncation remainder](#conj:archimedean-remainder-exponential-decay); at the canonical proton pin the same five rungs give $+0.0377$ ppm, which does not clear that ceiling." },
    {
      kind: "status",
      date: "2026-08-31",
      body:
        "**Headline sign corrected; tables 2 and 3 recomputed.** The published " +
        "residual was $-0.0066$ ppm. In this block's own convention " +
        "$(\\mathfrak{Q}_\\beta^{\\mathrm{cat}} - \\mathfrak{Q}_\\beta^{\\mathrm{CODATA}}) / " +
        "\\mathfrak{Q}_\\beta^{\\mathrm{CODATA}}$ — the convention its own table 2 rows " +
        "are quoted in — the ladder descends to CODATA from above and no documented " +
        "coefficient assignment reaches a negative residual at either pin, so the minus " +
        "was wrong; the published magnitude has no reproducible provenance at either " +
        "input epoch. The declared producer was also replaced: " +
        "`probe_q_beta_operator_valued_N3.py` stops at $N=3$, carries no $c_5$, and " +
        "is a different ladder (its $N=1$ rung is $\\cos(\\alpha_{N=1})$). See the " +
        "provenance section of the context block, and bean `qou-54g5`.",
      see: "computations/qbeta/qbeta_precision_ladder_n5.py",
    },
  ],
});
