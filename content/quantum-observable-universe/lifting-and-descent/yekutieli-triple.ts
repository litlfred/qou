import { definition } from "../../schema/builders";

export default definition({
  label: "def:yekutieli-triple",
  lean: { ref: "qou:QOU.YekutieliTripleMapping", validation: "not_checked" },
  title: "Lifting triple mapping",
  tags: ["yekutieli", "triple", "gerbe", "transition-function"],
  uses: ["lem:descent"],
});
