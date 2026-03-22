import { definition } from "../../schema/builders";

export default definition({
  label: "def:brane-boundary",
  lean: { decl: "QOU.BraneBoundary" },
  status: "stated",
  title: "Defining boundary of the brane",
  tags: ["brane-boundary", "kernel", "degeneracy-locus"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "lem:descent",
  ],
});
