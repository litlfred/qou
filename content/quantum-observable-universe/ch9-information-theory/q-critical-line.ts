import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-critical-line",
  title: "Critical line of the $q$-logarithmic zeta function",
  tags: [
    "zeta-function",
    "critical-line",
    "riemann-hypothesis",
    "q-deformation",
    "hausdorff-dimension",
  ],
  uses: [
    "def:q-logarithmic-zeta",
    "def:operational-entropy",
    "rem:hausdorff-dimension-recurrence",
  ],
});
