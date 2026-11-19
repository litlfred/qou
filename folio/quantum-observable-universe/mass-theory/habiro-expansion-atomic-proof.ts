import { proof } from "../../schema/builders";

export default proof({
  label: "prf:habiro-expansion-atomic",
  title: "Proof of habiro expansion atomic",
  uses: ["cor:habiro-expansion-atomic"],
  computation: {
    engine: "mpmath",
    script: "computations/habiro/habiro_interpolate_cross_validator.py",
    witness: "computations/habiro/habiro-interpolate-cross-validation.witness.json",
    status: "verified",
  },
});
