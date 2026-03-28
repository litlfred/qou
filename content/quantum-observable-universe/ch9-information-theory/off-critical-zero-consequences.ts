import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-critical-line",
  label: "rem:off-critical-zero-consequences",
  title: "Why off-critical zeros cannot arise: the unitarity argument",
  tags: [
    "zeta-function",
    "critical-line",
    "unitarity",
    "r-matrix",
    "information-theory",
    "hausdorff-dimension",
  ],
  uses: [
    "prop:q-critical-line",
    "def:q-logarithmic-zeta",
    "def:operational-entropy",
    "rem:hausdorff-dimension-recurrence",
    "rem:discrete-planck-step",
  ],
});
