import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:adelic-reeb-restricted-product",
  title:
    "Restricted-product structure of the Reeb $\\omega$-order: additivity over places and local--global squeeze",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.adelic_reeb_order_additive",
    validation: "not_checked",
  },
  uses: ["def:reeb-epsilon"],
  cites: ["tate1967", "conway1976"],
  tags: [
    "adeles",
    "tate-thesis",
    "restricted-product",
    "surreal",
    "omega-order",
    "valuation",
    "local-global",
    "squeeze",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-06-09",
      body:
        "**proposition (structural, unconditional).** Both Lean theorems " +
        "(`adelic_reeb_order_additive`, `adelic_reeb_squeeze_local_to_global`) " +
        "are stated over an abstract common value group `Γ` and depend on no " +
        "conjecture (the per-place squeeze enters only as a hypothesis), so the " +
        "block is a clean `proposition` rather than a conjecture-downstream " +
        "remark. Promoted from interpretive content inside " +
        "`rem:adelic-tate-squeeze`. **Lean `validation: not_checked`:** the elan " +
        "release server is firewalled in the web sandbox (`release.lean-lang.org` " +
        "parse error), so `lake build QOU` could not run this session; the proof " +
        "uses only `Finset.sum_add_distrib` and `Finset.sum_lt_sum` and is " +
        "expected to compile, but is unverified pending a CI / cache-restore build.",
    },
  ],
});
