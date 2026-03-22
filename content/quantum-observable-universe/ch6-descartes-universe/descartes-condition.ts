import { definition } from "../../schema/builders";

export default definition({
  label: "def:descartes-condition",
  lean: { decl: "QOU.DescartesCondition" },
  status: "not_started",
  title: "Descartes condition",
  tags: ["descartes-universe", "euler-characteristic"],
  uses: [
    "def:quantum-observable-universe",
    "thm:qu-to-qou",
  ],
});
