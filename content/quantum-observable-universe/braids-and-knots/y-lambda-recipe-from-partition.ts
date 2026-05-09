import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:y-lambda-recipe-from-partition",
  title:
    "Recipe: $\\lambda \\mapsto y_\\lambda(q)$ — explicit q-rational construction in $\\sqrt q$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.y_lambda_recipe_from_partition",
    validation: "not_checked",
  },
  uses: [
    "prop:y-lambda-closed-form-wenzl-bridge",
    "prop:y-lambda-cyclotomic-factorization",
    "prop:hoefsmit-seminormal-form",
    "thm:jones-markov-trace",
  ],
  cites: ["wenzl1988", "macdonald1995"],
  tags: [
    "y-lambda",
    "recipe",
    "algorithm",
    "wenzl-bridge",
    "schur-element",
    "cyclotomic",
    "closed-form",
    "principal-specialization",
  ],
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/probe_wedderburn_weight_scheme.py",
    witness: [
      "folio-assistant/computations/probe-proton-with-wenzl-weights.witness.json",
      "folio-assistant/computations/probe-wedderburn-weight-scheme.witness.json",
    ],
    status: "not_run",
  },
});
