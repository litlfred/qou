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
        "`computations/qbeta/qbeta-ck-cache.witness.json`.",
    },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "`computation.script` / `computation.witness` and the .md *Python API* " +
        "and *Witness contract* sections pointed at " +
        "`computations/q_beta_predicted.py` and " +
        "`computations/q-beta-predicted.witness.json`, and asserted that they " +
        "record each $c_k$ with its tier. Neither does: that script has no " +
        "$c_k$ logic and its witness has no `c_k` and no `tier` key. The $c_k$ " +
        "producer is `computations/qbeta/qbeta_ck_cache.py`, which does stamp " +
        "a `tier` on each rung, so all three now point there and the contract " +
        "was relaxed to what that witness holds — the rungs the greedy " +
        "extraction reaches ($k = 2$ and $k = 3$), tiered on the producer's " +
        "own `derived` / `cal-anchored` axis, which is not the editorial tier " +
        "column. `q_beta_predicted.py` remains the step-11 production script " +
        "(`alg:q-beta-truncation`) and still wires no $c_3$+ rung, per " +
        "`docs/coordination/ck-dk-canonical-registry.md` §6.",
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
