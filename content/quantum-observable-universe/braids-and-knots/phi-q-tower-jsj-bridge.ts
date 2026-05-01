import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:phi-q-tower-jsj-bridge",
  title:
    "Φ$_q$ tower equals $\\rho_q \\cdot \\sum_S \\mathrm{Vol}(K_S)$ (archimedean bridge)",
  lean: {
    ref: "qou:QOU.PhiQJSJ.bridge",
    validation: "not_checked",
  },
  uses: [
    "def:phi-q-piece",
    "conj:kashaev-volume-conjecture",
    "prop:mass-endomorphism-tower",
    "prop:topological-mass-formula",
    "rem:kashaev-as-archimedean-realization",
    "cor:quantum-dilogarithm",
    "rem:quantum-bloch-group",
    "prop:gb-spectral-sequence",
    "prop:graded-trace-residue-split",
    "prop:markov-pair-z2",
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
