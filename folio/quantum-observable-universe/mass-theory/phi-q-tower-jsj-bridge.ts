import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-q-tower-jsj-bridge",
  interprets: "prop:phi-q-tower-algebraic-stratification",
  title:
    "Φ$_q$ tower equals $\\rho_q \\cdot \\sum_S \\mathrm{Vol}(K_S)$ (archimedean bridge)",
  lean: {
    ref: "qou:QOU.PhiQJSJ.bridge",
    validation: "not_checked",
  },
  uses: [
    "prop:phi-q-tower-algebraic-stratification",
    "conj:kashaev-volume-conjecture",
    "cor:quantum-dilogarithm",
    "prop:gb-spectral-sequence",
  ],
  cites: ["kashaev1997", "murakami-murakami2001", "thurston1978", "neumann-zagier1985", "zagier1986"],
  tags: [
    "phi-q",
    "kashaev",
    "archimedean",
    "bridge",
    "jsj",
    "mass",
    "open-problem",
  ],
});
