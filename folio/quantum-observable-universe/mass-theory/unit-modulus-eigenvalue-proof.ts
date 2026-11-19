import { proof } from "../../schema/builders";

export default proof({
  label: "prf:unit-modulus-eigenvalue",
  title: "Proof of unit modulus eigenvalue",
  uses: ["prop:unit-modulus-eigenvalue"],
  computation: {
    engine: "python+mpmath",
    script: "computations/e0_lambda_composite.py",
    witness: "computations/e0-lambda-composite.witness.json",
    status: "verified",
  },
});
