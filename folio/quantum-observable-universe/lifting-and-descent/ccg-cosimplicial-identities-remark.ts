import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:ccg-cosimplicial-identities",
  label: "rem:ccg-cosimplicial-identities-remark",
  title: "Why the cosimplicial identities hold",
  uses: ["def:ccg-cosimplicial-identities", "lem:descent"],
});
