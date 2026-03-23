import { definition } from "../../schema/builders";

export default definition({
  label: "def:recursive-brane-tower",
  lean: { decl: "QOU.RecursiveBraneTower" },
  status: "stated",
  title: "Recursive Brane Tower",
  tags: ["brane-tower", "jet-bundle", "frobenius-hopf"],
  examples: ["ex:recursive-brane-tower-su2"],
  uses: ["def:quantum-observable-universe", "prop:jet-prolongation"],
});
