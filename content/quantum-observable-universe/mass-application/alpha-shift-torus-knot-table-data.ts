import { table } from "../../schema/builders";

export default table({
  label: "tbl:alpha-shift-torus-knot-table-data",
  title:
    "$\\alpha_{\\mathrm{shift}}(T_{p,k})$ per-irrep symbolic evidence (6 test pairs)",
  caption:
    "Pole-order maximiser $\\lambda$, computed $\\alpha_{\\mathrm{shift}}" +
    "(T_{p,k})$, and the closed-form $k(p-1)$ for six test pairs. All " +
    "values match the closed-form formula; all 14 assertions in " +
    "`alpha-shift-torus.witness.json` pass.",
  uses: ["prop:alpha-shift-torus-knot"],
  tags: [
    "torus-knot",
    "alpha-shift",
    "hecke-character",
    "pole-order",
    "witness-table",
  ],
});
