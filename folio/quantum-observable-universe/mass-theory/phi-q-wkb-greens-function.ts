import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:phi-q-wkb-greens-function",
  title:
    "Next Faddeev-WKB order: $S_1 = -\\tfrac{1}{2}\\log\\det \\mathfrak{D}_\\nabla$ is the categorical Green's function",
  lean: {
    ref: "qou:QOU.QPochhammer.WKBGreensFunction",
    validation: "not_checked",
  },
  uses: [
    "def:q-pochhammer-partial-product",
    "def:categorical-dirac-operator",
    "conj:dilogarithm-archimedean-limit",
    "conj:algebraic-geometric-dilog-equivalence",
    "def:archimedean-realization-functor",
    "rem:kashaev-as-archimedean-realization",
    "def:categorical-instanton",
    "def:adelic-substrate",
    "rem:chern-simons-as-knot-invariant",
    "def:phi-q-piece",
    "prop:reeb-u1-chart-swap",
    "rem:yang-mills-surreal-bound",
  ],
  cites: [
    "faddeev1994",
    "kashaev1997",
  ],
  tags: [
    "q-pochhammer",
    "wkb",
    "saddle-point",
    "greens-function",
    "one-loop-determinant",
    "archimedean",
    "open-problem",
  ],
});
