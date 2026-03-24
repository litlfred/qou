import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-relation",
  lean: {
    decl: "QOU.frobenius_relation",
    validation: "not_checked",
  },
  title: "Frobenius relation",
  uses: ["def:quantum-universe", "def:frobenius-pairing"],
  proofs: ["prf:frobenius-relation"],
  examples: ["ex:frobenius-su2"],
  tags: ["category-theory", "frobenius"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/frobenius-relation-0.svg", blockIndex: 0, hash: "bf89ade962b6" },
  ],

});
