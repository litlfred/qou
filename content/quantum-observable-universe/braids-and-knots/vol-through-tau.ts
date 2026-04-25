import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vol-through-tau",
  title:
    "$\\mathrm{Vol}(K)$ factors strictly through the fibre functor $\\tau$",
  tags: ["fibre-functor", "knot-volume", "archimedean", "factorization"],
  uses: [
    "def:algebraic-quantum-volume",
    "def:archimedean-realization-functor",
    "def:adelic-substrate",
    "def:quantum-observable-universe",
  ],
  cites: ["kashaev1997", "murakami-murakami2001"],
  lean: {
    ref: "qou:QOU.BraidsKnots.VolThroughTau",
    validation: "not_checked",
  },
});
