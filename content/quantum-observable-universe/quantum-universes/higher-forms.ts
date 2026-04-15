import { definition } from "../../schema/builders";

export default definition({
  label: "def:higher-forms",
  title: "Higher differential forms",
  tags: ["differential-forms", "category-theory"],
  lean: {
    decl: "QOU.HigherForms",
    validation: "not_checked",
  },
  uses: ["def:quantum-universe"],
  examples: ["ex:higher-forms-su2"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/higher-forms-0.svg", blockIndex: 0, hash: "eee96a54ef11" },
  ],

});
