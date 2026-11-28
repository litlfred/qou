import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-hausdorff-comparison",
  title: "Heuristic comparison between the Hausdorff recurrence and real-$q$ Collatz step ratios",
  interprets: "conj:q-collatz",
  uses: [
    "sec:collatz-intro",
    "conj:q-collatz",
    "conj:collatz-contact-boundary",
    "quantum-observable-universe:rem:hausdorff-dimension-recurrence",
    "quantum-observable-universe:def:operational-entropy",
  ],
  tags: ["collatz", "hausdorff-recurrence", "heuristic"],
});
