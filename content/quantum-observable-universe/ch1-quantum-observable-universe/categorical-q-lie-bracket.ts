import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-lie-bracket",
  title: "Categorical $q$-Lie bracket",
  tags: ["lie-bracket", "deformation"],
  lean: {
    decl: "QOU.CategoricalQLieBracket",
    validation: "not_checked",
  },
  status: "stated",
  uses: [
    "def:categorical-reeb",
    "def:substrate-parameter",
  ],
});
