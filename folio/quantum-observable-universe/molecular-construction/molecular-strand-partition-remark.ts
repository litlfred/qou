import { remark } from "../../schema/builders";

export default remark({
  label: "rem:molecular-strand-partition-remark",
  title: "Strand-partitions are fixed by connectivity",
  interprets: "def:molecular-strand-partition",
  tags: ["definition-commentary"],
  uses: [
    "def:molecular-strand-partition",
    "ex:benzene-symmetric-projector",
  ],
});
