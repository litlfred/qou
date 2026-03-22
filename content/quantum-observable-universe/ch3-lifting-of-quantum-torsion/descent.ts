import { definition } from "../../schema/builders";

export default definition({
  label: "def:descent",
  lean: { decl: "QOU.Descent" },
  status: "stated",
  title: "Descent",
  tags: ["descent", "brane-tower", "restriction"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "thm:qu-to-qou",
  ],
});
