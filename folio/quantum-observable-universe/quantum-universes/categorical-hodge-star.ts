import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-hodge-star",
  title: "Categorical Hodge star",
  lean: { ref: "qou:QOU.CatHodgeInvolution",
    validation: "not_checked",
  },
  uses: ["def:higher-forms"],
  examples: ["ex:hodge-su2"],
  tags: ["hodge-star"],
});
