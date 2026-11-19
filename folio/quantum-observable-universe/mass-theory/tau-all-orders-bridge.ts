import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tau-all-orders-bridge",
  title:
    "Order-mixing map versus distinct invariants for the fibre functor $\\tau$ across the $h$-expansion",
  lean: {
    ref: "qou:QOU.MassTheory.tau_all_orders_bridge",
    validation: "not_checked",
  },
  uses: [
    "prop:crossed-module-euler-characteristic",
    "conj:geom-universality",
    "rem:geom-bridge-status",
  ],
  cites: ["yekutieli2015", "neumann-zagier1985"],
  tags: [
    "tier:S",
    "geom",
    "non-abelian-stokes",
    "open-problem",
    "fibre-functor",
    "h-expansion",
    "order-mixing",
    "bring-surface",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
