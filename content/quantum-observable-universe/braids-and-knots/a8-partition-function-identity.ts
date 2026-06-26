import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "This result records the numerical coincidence that the $a_8$ coefficients $(1,2,3,5,7)$ match the partition numbers $p(1..5)$. It is an empirical Habiro-shell observation rather than a new deductive argument, utilizing standard partition values, with the identity proved formally via ring equivalences." },
  ],
  label: "prop:a-8-partition-function-identity",
  title:
    "$a_8$ partition-function identity: $a_8(X) = \\sum_{n=1}^{5} p(n)\\,X^{5-n}$",
  lean: {
    ref: "qou:QOU.BraidKnot.A8Partition.a_8_eq_partition_sum",
  },
  uses: [
    "prop:cyclotomic-strand-doubling",
  ],
  cites: [
    "habiro2000",
  ],
  tags: [
    "habiro-ring",
    "partition-function",
    "qbeta",
    "1ppQ",
    "draft",
  ],
});
