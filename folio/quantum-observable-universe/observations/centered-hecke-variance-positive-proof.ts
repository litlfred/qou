import { proof } from "../../schema/builders";

export default proof({
  label: "prf:centered-hecke-variance-positive",
  title: "Proof: centred Hecke variance is strictly positive",
  uses: ["prop:centered-hecke-variance-positive"],
  computation: {
    engine: "python+mpmath",
    script: "computations/y_lambda_cyclotomic_factor.py",
    witness: "computations/y-lambda-cyclotomic-factor.witness.json",
    status: "verified",
  },
});
