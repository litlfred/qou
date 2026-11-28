import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:classical-riemann-hypothesis",
  title: "Classical Riemann hypothesis",
  lean: {
    ref: "qou:BraidKnotOctonion.ClassicalRiemannHypothesis",
    validation: "stub",
  },
  uses: [
    "quantum-observable-universe:def:classical-riemann-zeta",
  ],
  tags: ["tier:famous", "riemann-hypothesis", "zeta-function", "millennium"],
});
