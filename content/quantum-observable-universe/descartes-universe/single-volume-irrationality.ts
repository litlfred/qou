import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:single-volume-irrationality",
  title: "Irrationality of a single hyperbolic knot volume",
  tags: [
    "irrationality",
    "hyperbolic-volume",
    "bloch-wigner",
    "clausen-function",
    "open-problem",
  ],
  uses: [
    "conj:hyperbolic-volume-transcendence",
  ],
});
