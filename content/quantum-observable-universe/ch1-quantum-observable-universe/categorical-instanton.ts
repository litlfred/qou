import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-instanton",
  title: "Categorical instanton",
  tags: ["instanton", "self-dual"],
  lean: {
    decl: "QOU.CategoricalInstanton",
    validation: "leanok",
  },
  status: "not_started",
  uses: [
    "def:quantum-observable-universe",
    "def:categorical-connection",
    "def:q-hodge-star",
  ],
});
