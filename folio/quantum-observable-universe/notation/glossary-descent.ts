import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-descent",
  lean: { ref: "qou:QOU.DescentData", validation: "not_checked" },
  title: "Descent",
  tags: ["glossary", "descent", "brane-tower", "restriction"],
  uses: ["thm:qu-to-qou"],
});
