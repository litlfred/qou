import { definition } from "../../schema/builders";

export default definition({
  label: "def:recursive-brane-tower",
  lean: { decl: "QOU.RecursiveBraneTower" },
  title: "Recursive Brane Tower",
  tags: ["brane-tower", "jet-bundle", "frobenius-hopf"],
  examples: ["ex:recursive-brane-tower-su2"],
  uses: ["prop:jet-prolongation"],
});
