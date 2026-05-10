import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gb-depth-period-correspondence",
  title:
    "GS-depth $\\leftrightarrow$ Goncharov period-depth correspondence",
  uses: [
    "def:frobenius-hopf-substrate",
    "def:archimedean-realization-functor",
    "prop:archimedean-functor-uniqueness",
    "prop:q-dilogarithm-exists",
    "prop:quantum-dilogarithm-stratified",
    "prop:curvature-rank-gb-stratification",
    "prop:categorical-laplace-unique",
    "def:q-resolvent",
    "lem:surreal-squeeze",
    "rem:figure-8-archimedean-illustration",
    "rem:algebraic-core-survives",
  ],
  cites: [
    "kontsevich1995",
    "zagier1986",
    "bloch2000",
    "suslin1991",
    "neumann-zagier1985",
  ],
  tags: [
    "graded-mikusinski",
    "goncharov-periods",
    "archimedean-wall",
    "iterated-integral-depth",
    "surreal-envelope",
    "wall-crossing-criterion",
    "open-problem",
    "keystone",
  ],
});
