import { proof } from "../../schema/builders";

export default proof({
  label: "prf:ring-closure-barrier-quantitative",
  title: "Quantitative ring-closure barrier (sympy + experimental data)",
  tags: [
    "ring-closure",
    "barrier",
    "verification",
    "computation",
    "sympy",
    "experimental-comparison",
  ],
  uses: ["prop:ring-closure-barrier-quantitative"],
  computation: {
    engine: "sympy",
    script: "computations/ring_closure_barrier.py",
    witness: "computations/ring-closure-barrier.witness.json",
    status: "verified",
  },
});
