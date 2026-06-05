import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:algebraic-geometric-dilog-equivalence",
  title:
    "Algebraic-geometric dilogarithm equivalence: $\\Phi_n(x; q)$ poles map to ideal-tetrahedron cusps",
  lean: {
    ref: "qou:QOU.QPochhammer.algebraic_geometric_equivalence",
    validation: "not_checked",
  },
  uses: [
    "conj:dilogarithm-archimedean-limit",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "neumann-zagier1985",
    "thurston1978",
    "zagier1986",
  ],
  tags: [
    "q-pochhammer",
    "dilogarithm",
    "bloch-wigner",
    "kashaev",
    "phi-q",
    "algebraic-geometric",
    "open-problem",
  ],
});
