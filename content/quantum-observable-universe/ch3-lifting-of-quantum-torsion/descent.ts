import { definition } from "../../schema/builders";

export default definition({
  label: "def:descent",
  lean: { decl: "QOU.DescentData" },
  title: "Descent",
  tags: ["descent", "brane-tower", "restriction"],
  uses: ["thm:qu-to-qou"],
});
