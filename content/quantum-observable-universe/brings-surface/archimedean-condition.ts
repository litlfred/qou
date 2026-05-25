import { definition } from "../../schema/builders";

export default definition({
  label: "def:archimedean-condition",
  lean: { ref: "qou:QOU.ArchimedeanCondition", validation: "not_checked" },
  title: "Descartes condition",
  tags: ["archimedean-universe", "euler-characteristic"],
  uses: ["thm:qu-to-qou"],
});
