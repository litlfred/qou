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
        "decision must update both that ledger and the canonical tiered $c_k$ cache " +
        "`computations/qbeta/qbeta-ck-cache.witness.json` (which is C-frame, " +
        "`markov_convention: \"C\"`, pending the Convention-D re-derivation under " +
        "`qou-cds1` / `qou-wxhi`; invalid $z_D$ substitution proved by `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` and `QOU.QBeta.eigenphase_bar_defect_of_fullBar`; downstream $Q_{N_2}$ consumer: " +
        "`computations/q-beta-predicted.witness.json`).",
    },
  ],
  label: "alg:ck-truncation-ladder",
  title: "$c_k$ truncation ladder — tiered classification",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/qbeta/qbeta_ck_cache.py",
    witness: "computations/qbeta/qbeta-ck-cache.witness.json",
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
