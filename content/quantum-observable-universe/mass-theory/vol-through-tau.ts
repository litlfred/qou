import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vol-through-tau",
  title:
    "$\\mathrm{Vol}(K)$ factors strictly through the fibre functor $\\tau$",
  tags: ["fibre-functor", "knot-volume", "archimedean", "factorization"],
  uses: ["def:archimedean-realization-functor"],
  cites: ["kashaev1997", "murakami-murakami2001"],
  lean: {
    ref: "qou:QOU.BraidsKnots.VolThroughTau",
    validation: "not_checked",
  },
});
