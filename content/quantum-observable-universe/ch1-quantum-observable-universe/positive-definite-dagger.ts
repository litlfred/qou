import { definition } from "../../schema/builders";

export default definition({
  label: "def:positive-definite-dagger",
  title: "Positive-definite structure",
  lean: {
    decl: "QOU.PositiveDefiniteStructure",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:involutive-structure"],
  tags: ["category-theory", "positive-definite"],
});
