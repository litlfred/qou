import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-critical-line",
  title: "Unitarity forces zeros onto the $q$-critical line",
  tags: [
    "zeta-function",
    "critical-line",
    "riemann-hypothesis",
    "q-deformation",
    "hausdorff-dimension",
    "unitarity",
    "r-matrix",
  ],
  lean: {
    decl: "QOU.Information.qCriticalLine",
    validation: "not_checked",
  },
  uses: [
    "def:q-logarithmic-zeta",
    "def:operational-entropy",
    "rem:hausdorff-dimension-recurrence",
  ],
});
