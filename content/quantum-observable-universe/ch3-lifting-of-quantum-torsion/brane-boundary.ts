import { definition } from "../../schema/builders";

export default definition({
  label: "def:brane-boundary",
  title: "Defining boundary of the brane",
  tags: ["brane-boundary", "kernel", "degeneracy-locus"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "lem:descent",
  ],
});
