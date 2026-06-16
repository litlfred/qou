import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:y-lambda-cyclotomic-factorization",
  title:
    "Cyclotomic factorisation of $y_\\lambda$ at $H_n(R, q)$ for small $n$ via Wenzl-bridge",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.y_lambda_cyclotomic_factorization",
    validation: "not_checked",
  },
  uses: ["prop:y-lambda-closed-form-wenzl-bridge"],
  cites: ["wenzl1988", "macdonald1995"],
  tags: [
    "y-lambda",
    "cyclotomic-polynomial",
    "schur-element",
    "closed-form",
    "wenzl-bridge",
    "q-rational",
    "principal-specialization",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probes/y_lambda_cyclotomic_factorization_probe.py",
    witness: "computations/probes/y-lambda-cyclotomic-factorization-probe.witness.json",
    status: "verified",
  },
});
