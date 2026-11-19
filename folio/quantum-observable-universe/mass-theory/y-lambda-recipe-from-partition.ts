import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:y-lambda-recipe-from-partition",
  title:
    "Recipe: $\\lambda \\mapsto y_\\lambda(q)$ — explicit q-rational construction over $\\mathbb{Q}(q)$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.y_lambda_recipe_from_partition",
    validation: "not_checked",
  },
  uses: ["prop:y-lambda-cyclotomic-factorization"],
  cites: ["wenzl1988", "macdonald1995"],
  computation: {
    engine: "python",
    script: "computations/markov_z_full_bar_condition_probe.py",
    witness: ["computations/markov-z-full-bar-condition.witness.json"],
    status: "verified",
  },
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
});
