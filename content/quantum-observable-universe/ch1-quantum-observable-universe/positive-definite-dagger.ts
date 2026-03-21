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
  rendered: [
    { mime: "image/svg+xml", url: "rendered/positive-definite-dagger-0.svg", blockIndex: 0, hash: "60707ebb7060" },
  ],

});
