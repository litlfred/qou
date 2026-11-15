import { definition } from "../../schema/builders";

export default definition({
  label: "def:higher-forms",
  title: "Higher differential forms",
  tags: ["differential-forms", "category-theory"],
  lean: { ref: "qou:QOU.HigherForms",
    validation: "not_checked",
  },
  uses: ["def:quantum-universe"],
  examples: ["ex:higher-forms-su2"],
});
