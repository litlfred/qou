import { algorithm } from "../../schema/builders";

export default algorithm({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "Maintenance contract (working channel, not published prose): the " +
        "$\\mathfrak{Q}_\\beta$ subdir ledger `docs/coordination/1ppq-qbeta.md` " +
        "carries the $c_k$ reversal-history table. Any inclusion/exclusion " +
        "decision must update both that ledger and the canonical witness " +
        "`computations/q-beta-predicted.witness.json`.",
    },
  ],
  label: "alg:ck-truncation-ladder",
  title: "$c_k$ truncation ladder — tiered classification",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_beta_predicted.py",
    witness: "computations/q-beta-predicted.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "sidecar",
    "ck-truncation",
    "q-beta",
    "tiered-coefficients",
  ],
});
