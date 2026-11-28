import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jvw-tractable-orders",
  title: "Orders of the Jones-tractable points",
  lean: { ref: "qou:QOU.Information.JonesTractable.jvw_orders" },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-28",
      body:
        "Lean: `QOU/InformationTheory/JonesTractableOrders.lean` — `jvw_orders`, `jvw_no_order_six`, `four_not_dvd_six`. The hardness theorem itself is cited (`jaeger1990`). The `t = q^{±2}` sentence is a direct computation (square roots of the six points) and is not formalised. This corrects the earlier `n ∣ 6` statement in `conj:qou-p-neq-np`, whose own list of points included `±i` (order 4) and `e^{±iπ/3}` (order 6, not a JVW point).",
    },
  ],
  tags: ["Jones-polynomial", "roots-of-unity", "cyclotomic"],
  uses: [],
  cites: ["jaeger1990"],
});
