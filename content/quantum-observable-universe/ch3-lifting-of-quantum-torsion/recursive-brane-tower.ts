import { definition } from "../../schema/builders";

export default definition({
  label: "def:recursive-brane-tower",
  lean: { decl: "QOU.RecursiveBraneTower" },
  status: "not_started",
  title: "Recursive Brane Tower",
  tags: ["brane-tower", "jet-bundle", "frobenius-hopf"],
  uses: ["def:quantum-observable-universe", "prop:jet-prolongation"],
});
