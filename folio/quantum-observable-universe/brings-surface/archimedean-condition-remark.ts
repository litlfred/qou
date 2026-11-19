import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:archimedean-condition",
  label: "rem:archimedean-condition-remark",
  title: "Consequences and scope of the Descartes condition",
  uses: ["def:archimedean-condition", "thm:qu-to-qou", "rem:three-euler-characteristics"],
});
