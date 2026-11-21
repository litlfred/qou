import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Lean now states the relation with an honest `sorry`. The context field `claim_frobenius_relation`, which was the conclusion, is deleted (round-trip audit pass 2, C09). The previous proof paired a map $A \\otimes A \\to A \\otimes A$ with a single test element of $A$; it is rewritten." },
  ],
  label: "prop:frobenius-relation",
  lean: { ref: "qou:QOU.frobenius_relation",
    validation: "not_checked",
  },
  title: "Frobenius relation",
  uses: ["def:frobenius-pairing"],
  proofs: ["prf:frobenius-relation"],
  examples: ["ex:frobenius-su2", "ex:frobenius-relation-su2"],
  tags: ["category-theory", "frobenius"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/frobenius-relation-0.svg", blockIndex: 0, hash: "d6fa534adf36" },
  ],

});
