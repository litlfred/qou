import { definition } from "../../schema/builders";

export default definition({
  label: "def:yekutieli-triple",
  lean: { decl: "QOU.YekutieliTriple" },
  status: "not_started",
  title: "Yekutieli triple mapping",
  tags: ["yekutieli", "triple", "gerbe", "transition-function"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "prop:jet-prolongation",
    "lem:descent",
  ],
});
