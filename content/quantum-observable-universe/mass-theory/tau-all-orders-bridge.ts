import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tau-all-orders-bridge",
  title:
    "Status of the fibre functor $\\tau$ at all orders of the $h$-expansion: order-mixing map or distinct invariants?",
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
    "geom",
    "non-abelian-stokes",
    "open-problem",
    "fibre-functor",
    "h-expansion",
    "order-mixing",
    "bring-surface",
  ],
});
