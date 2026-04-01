import { definition } from "../../schema/builders";

export default definition({
  label: "def:descartes-condition",
  lean: { decl: "QOU.DescartesCondition" },
  title: "Descartes condition",
  tags: ["descartes-universe", "euler-characteristic"],
  uses: ["thm:qu-to-qou"],
});
