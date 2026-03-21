import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cosimplicial-crossed-groupoid",
  title: "Cosimplicial crossed groupoid",
  hasProof: true,
  tags: ["cosimplicial", "crossed-groupoid", "gerbe", "yekutieli"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:yekutieli-triple",
    "prop:jet-prolongation",
    "lem:descent",
  ],
});
