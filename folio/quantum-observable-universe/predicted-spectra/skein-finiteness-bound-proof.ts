import { proof } from "../../schema/builders";

export default proof({
  label: "prf:skein-finiteness-bound",
  title: "Proof of the Skein finiteness bound",
  uses: ["prop:skein-finiteness-bound", "prop:skein-polynomial-transfer-matrix"],
  computation: {
    engine: "python",
    script: "computations/em_linking_upper_bound_precision_budget.py",
    witness: "computations/em-linking-upper-bound-precision-budget.witness.json",
    status: "verified",
  },
});
