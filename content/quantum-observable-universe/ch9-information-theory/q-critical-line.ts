import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-critical-line",
  title: "Unitarity and the $q$-critical line",
  tags: [
    "zeta-function",
    "critical-line",
    "riemann-hypothesis",
    "q-deformation",
    "hausdorff-dimension",
    "unitarity",
    "r-matrix",
    "open-problem",
  ],
  uses: [
    "def:q-logarithmic-zeta",
    "def:operational-entropy",
    "rem:hausdorff-dimension-recurrence",
  ],
});
