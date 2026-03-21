import { definition } from "../../schema/builders";

export default definition({
  label: "def:involutive-structure",
  title: "Involutive structure ($\\ast$-structure)",
  lean: {
    decl: "QOU.InvolutiveStructure",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:rigid-monoidal-category"],
  examples: ["ex:dagger-su2"],
  tags: ["category-theory", "involutive"],
});
