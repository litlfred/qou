import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-lie-bracket",
  title: "Categorical $q$-Lie bracket",
  tags: ["lie-bracket", "deformation"],
  lean: { ref: "qou:QOU.CategoricalQLieBracket",
    validation: "not_checked",
  },
  uses: ["def:substrate-parameter"],
});
