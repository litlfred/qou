import { proposition } from "../../schema/builders";

export default proposition({
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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): - Sibling Lean identity (cyclotomic strand-doubling): [`cyclotomic-strand-doubling.md`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/mass-theory/cyclotomic-strand-doubling.md)" },
  ],
});
