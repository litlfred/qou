import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:classical-riemann-hypothesis",
  title: "The Riemann hypothesis",
  lean: { ref: "qou:BraidKnotOctonion.ClassicalRiemannHypothesis", validation: "stub" },
  uses: ["def:classical-riemann-zeta"],
  tags: [
    "tier:famous",
    "riemann-hypothesis",
    "millennium-problem",
    "critical-line",
    "zeta-zeros",
  ],
});
