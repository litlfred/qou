import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-dirac-operator",
  title: "Categorical Dirac operator",
  tags: ["dirac", "connection", "q-deformed"],
  lean: {
    decl: "QOU.CategoricalDiracOperator",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-observable-universe",
    "def:categorical-connection",
    "def:substrate-parameter",
    "def:categorical-reeb",
  ],
});
