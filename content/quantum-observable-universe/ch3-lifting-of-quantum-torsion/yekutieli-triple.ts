import { definition } from "../../schema/builders";

export default definition({
  label: "def:yekutieli-triple",
  lean: { decl: "QOU.YekutieliTripleMapping" },
  title: "Yekutieli triple mapping",
  tags: ["yekutieli", "triple", "gerbe", "transition-function"],
  uses: ["lem:descent"],
});
