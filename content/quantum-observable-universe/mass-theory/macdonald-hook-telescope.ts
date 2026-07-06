import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:macdonald-hook-telescope",
  title:
    "Macdonald hook-content telescope for $Z_n$ and clean $y_\\lambda$ closed form",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.macdonald_hook_telescope",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "computations/y_lambda_macdonald_telescope.py",
    witness: "computations/y-lambda-macdonald-telescope.witness.json",
    status: "verified",
    requires: ["sympy", "mpmath"],
  },
  uses: [
    "prop:y-lambda-closed-form-wenzl-bridge",
  ],
  cites: ["macdonald1995", "stanley1999", "wenzl1988"],
  tags: [
    "y-lambda",
    "macdonald-hook",
    "telescope",
    "closed-form",
    "principal-specialization",
    "wenzl-bridge",
    "schur-element",
    "kostka-frobenius",
    "crystal-basis-shortcut",
  ],
});
