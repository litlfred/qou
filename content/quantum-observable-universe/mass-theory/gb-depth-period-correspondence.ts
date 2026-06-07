import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gb-depth-period-correspondence",
  title:
    "GS-depth $\\leftrightarrow$ Goncharov period-depth correspondence",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.GBDepthPeriodCorrespondence",
    validation: "not_checked",
  },
  uses: [
    "prop:q-dilogarithm-exists",
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
