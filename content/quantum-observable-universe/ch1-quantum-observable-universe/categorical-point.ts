import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-point",
  title: "Categorical point",
  tags: ["point", "categorical"],
  lean: {
    decl: "QOU.CategoricalPoint",
    validation: "not_checked",
  },
  status: "stated",
  uses: ["def:quantum-universe"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-point-0.svg", blockIndex: 0, hash: "209c12202df6" },
  ],

});
