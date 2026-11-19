import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:per-isotope-binding",
  title: "Per-isotope binding $B(K) = m_e \\cdot \\sum_\\lambda y_\\lambda \\chi^\\lambda \\Delta_\\lambda$",
  uses: [
    "prop:delta-lambda-dt-index-unification",
    "rem:term6-binding-density",
    "thm:knot-mass-formula-unified",
    "alg:markov-trace",
    "prop:linear-chain-bond-count",
    // ²H reeb-flow tier (owner ruling 2026-07-07: kept, NEAR-MATCH label)
    "prop:reeb-pn-magnitude-criticality",
    "conj:reeb-linking-cwf-normalization",
  ],
  computation: {
    engine: "python+mpmath",
    script: "qou-mass/src/qou_mass/api.py",
    witness: "computations/canonical-mass-table-242ppb.witness.json",
    status: "experimental",
  },
  tags: [
    "mba",
    "step-9b",
    "binding-energy",
    "delta-lambda",
    "per-isotope",
    "canonical-chain",
    "open-gate",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization and repo pointers moved out of published prose: the $[n]_q!$-normalized carrier $q$-lift ($c(q) = 1$) is probe-verified and not yet formalized in Lean; the per-partition value is formalized in `dtEuler_eq_deltaLambda_unconditional`; the weak-sector recurrence kernel-constraints file is `QBetaCKRecursionKernelConstraints.lean` (no binding-sector Lean analogue yet); and the experimental `B_unified` generating-function probe lives in `computations/probes/strong_unified_binding_probe.py` (no witness; PR #5765 aligned the Python snippet with `qou_mass.api.predict`).",
    },
    {
      kind: "note",
      date: "2026-08-25",
      body: "**Corrected 2026-08-25 (PR #5765).** This contract previously named\n`dashboard_and_sweep_results.md`, which **does not exist anywhere in the repo**\n(`find` → 0 hits) and disagreed with the `.ts` manifest. Two things a consumer should\nknow about the witness that *is* declared:\n\n- It carries **no provenance**: `computedAt`, `commitSha`, `witness.scriptHash`,\n  `witness.scriptFile` and `witness.scriptCommitSha` are **all `null`**, so no\n  staleness check can key on it and no producer can be resolved from it. It is marked\n  `auditOnly`.\n- Its numbers are **not** the live pipeline's. It records D +23 %, T +6 %, ³He +13 %,\n  ⁴He +3.6 % — i.e. *over*-binding — computed at the 242-ppb nucleon level that the\n  [2026-07-04 audit](../../../docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md)\n  identified as a fitted-Habiro regression and removed. The live `mass_binding_dashboard`\n  *under*-binds: ²H −27.5 %, ³H +38 %, ³He +44 %, ⁴He +69 % (`err sym` 0.79 / 1.38 /\n  1.44 / 3.26). **Do not cite the witness figures as this step's current accuracy.**",
    },
  ],
});
