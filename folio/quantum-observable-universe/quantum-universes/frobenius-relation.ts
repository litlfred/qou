import { proposition } from "../../schema/builders";

export default proposition({
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
