import { definition } from "../../schema/builders";

export default definition({
  label: "def:molecular-strand-partition",
  title: "Molecular strand-partition $\\lambda$ of $N$ strands",
  lean: {
    ref: "qou:QOU.Molecular.StrandPartition",
    validation: "not_checked",
  },
  uses: ["def:molecular-braid"],
  tags: [
    "strand-partition",
    "young-subgroup",
    "composite",
    "molecular",
    "parabolic",
  ],
});
