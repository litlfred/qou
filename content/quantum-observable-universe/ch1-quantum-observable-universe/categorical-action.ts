import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-action",
  title: "Categorical action",
  tags: ["action", "categorical"],
  lean: {
    decl: "QOU.CategoricalAction",
    validation: "not_checked",
  },
  status: "not_started",
  uses: [
    "def:quantum-universe",
    "def:quantum-observable-universe",
    "def:categorical-connection",
    "def:substrate-parameter",
    "def:q-hodge-star",
  ],
});
