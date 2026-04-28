import { definition } from "../../schema/builders";

export default definition({
  label: "def:brane-boundary",
  lean: { ref: "qou:QOU.braneBoundary", validation: "not_checked" },
  title: "Defining boundary of the brane",
  tags: ["brane-boundary", "kernel", "degeneracy-locus"],
  uses: ["lem:descent"],
});
