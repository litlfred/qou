import { definition } from "../../schema/builders";

export default definition({
  label: "def:gauge-action-groupoid",
  title: "Gauge action groupoid",
  tags: ["appendix", "standard-model", "gauge-theory", "groupoid", "action"],
  lean: {
    ref: "qou:QOU.StandardModel.GaugeActionGroupoid",
    validation: "not_checked",
  },
  uses: ["def:categorical-action", "def:categorical-lagrangian"],
});
