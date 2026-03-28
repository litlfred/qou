import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:q-critical-line",
  label: "rem:off-critical-zero-consequences",
  title: "Consequences of a zero off the $q$-critical line",
  tags: [
    "zeta-function",
    "critical-line",
    "orbit-counting",
    "information-theory",
    "unitarity",
  ],
  uses: [
    "conj:q-critical-line",
    "def:q-logarithmic-zeta",
    "def:operational-entropy",
    "rem:hausdorff-dimension-recurrence",
    "rem:discrete-planck-step",
  ],
});
