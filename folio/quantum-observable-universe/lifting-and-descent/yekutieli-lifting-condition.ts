import { definition } from "../../schema/builders";

export default definition({
  label: "def:yekutieli-lifting-condition",
  lean: { ref: "qou:QOU.YekutieliLiftingCondition", validation: "not_checked" },
  title: "Quantum Lifting Condition",
  tags: ["yekutieli", "gerbe", "cohomology", "lifting"],
  cites: ["yekutieli2010"],
  examples: ["ex:yekutieli-lifting-condition-su2"],
  uses: [],
});
