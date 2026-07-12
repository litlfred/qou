import { remark } from "../../schema/builders";

export default remark({
  label: "rem:dilog-saddle-regime",
  title:
    "Dilog saddle regime: the $\\theta = \\pi/3$ saddle of $\\mathrm{Im}\\,\\mathrm{Li}_2(e^{i\\theta})$ and $\\mathrm{Vol}(4_1)$",
  interprets: "conj:kashaev-volume-conjecture",
  uses: ["conj:kashaev-volume-conjecture"],
  cites: ["kashaev1997", "murakami-murakami2001", "thurston1978"],
  tags: [
    "kashaev",
    "saddle-point",
    "dilogarithm",
    "clausen",
    "hyperbolic-volume",
    "figure-8-knot",
    "consolidation-home",
  ],
});
