import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:adelic-reeb-restricted-product",
  proofs: ["prf:adelic-reeb-restricted-product"],
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
        "`rem:adelic-tate-squeeze`. **Lean: verified to compile EXIT=0** against " +
        "the Mathlib v4.24.0 olean cache (`lake-cache/qou-v4-24-0`) via a direct " +
        "`lean` invocation — the elan release server is firewalled in the web " +
        "sandbox, so `lake build` itself cannot run; `validation` stays " +
        "`not_checked` until lean CI confirms. The build caught a real bug: the " +
        "bundled `LinearOrderedAddCommGroup` was removed in this Mathlib pin " +
        "(hierarchy flattened), now stated as `AddCommGroup` + `LinearOrder` + " +
        "`IsOrderedCancelAddMonoid`. Proof uses `Finset.sum_add_distrib` + " +
        "`Finset.sum_lt_sum` (both confirmed present in the pin).",
    },
  ],
});
