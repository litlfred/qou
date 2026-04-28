import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-dirac-operator",
  title: "Categorical Dirac operator",
  tags: ["dirac", "connection", "q-deformed"],
  lean: { ref: "qou:QOU.CategoricalDiracOperator",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-connection",
    "def:substrate-parameter",
  ],
});
