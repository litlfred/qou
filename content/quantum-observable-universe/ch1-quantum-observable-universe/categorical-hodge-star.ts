import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-hodge-star",
  title: "Categorical Hodge star",
  lean: {
    decl: "QOU.CatHodgeInvolution",
    validation: "not_checked",
  },
  status: "stated",
  uses: ["def:quantum-universe", "def:higher-forms"],
  examples: ["ex:hodge-su2"],
  tags: ["hodge-star"],
});
