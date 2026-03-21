import { definition } from "../../schema/builders";

export default definition({
  label: "def:observation",
  title: "Observation",
  tags: ["observation", "quantum"],
  lean: {
    decl: "QOU.Observation",
    validation: "not_checked",
  },
  status: "not_started",
  uses: [
    "def:quantum-observable-universe",
    "def:substrate-parameter",
    "def:categorical-point",
  ],
});
