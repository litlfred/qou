import { definition } from "../../schema/builders";

export default definition({
  label: "def:descent-involution",
  examples: ["ex:descent-involution-su2"],
  lean: { ref: "qou:QOU.DescentInvolution", validation: "not_checked" },
  title: "Descent involution",
  tags: ["descent", "involution", "idempotent"],
  uses: ["lem:descent"],
});
