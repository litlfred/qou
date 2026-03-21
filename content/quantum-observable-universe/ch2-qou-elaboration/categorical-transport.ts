import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-transport",
  title: "Categorical transport equation",
  tags: ["transport", "categorical", "schrodinger"],
  lean: {
    decl: "QOU.CategoricalTransport",
    file: "QOU/CategoricalTransport.lean",
    validation: "leanok",
  },
  status: "not_started",
  uses: [
    "def:categorical-instanton",
    "def:categorical-q-ext-deriv",
    "def:categorical-jet",
  ],
});
