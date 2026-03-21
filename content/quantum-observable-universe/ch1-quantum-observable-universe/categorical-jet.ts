import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-jet",
  title: "Categorical jet object",
  lean: {
    decl: "QOU.CategoricalJet",
    validation: "axioms_only",
  },
  status: "not_started",
  uses: ["def:quantum-universe", "def:categorical-connection"],
  tags: ["jet"],
});
