import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cosimplicial-crossed-groupoid",
  title: "Cosimplicial crossed groupoid",
  tags: ["cosimplicial", "crossed-groupoid", "gerbe", "yekutieli"],
  lean: { decl: "QOU.cosimplicial_crossed_groupoid_exists" },
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:yekutieli-triple",
    "prop:jet-prolongation",
    "lem:descent",
  ],
  proofs: ["prf:cosimplicial-crossed-groupoid"],
});
