import { definition } from "../../schema/builders";

export default definition({
  label: "def:descartes-condition",
  lean: { ref: "qou:QOU.DescartesCondition", validation: "not_checked" },
  title: "Descartes condition",
  tags: ["descartes-universe", "euler-characteristic"],
  uses: ["thm:qu-to-qou"],
});
