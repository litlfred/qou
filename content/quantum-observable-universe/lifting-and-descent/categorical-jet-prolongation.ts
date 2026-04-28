import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-jet-prolongation",
  lean: { ref: "qou:QOU.categorical_jet_prolongation",
    validation: "not_checked",
  },
  title: "Jet prolongation",
  proofs: ["prf:categorical-jet-prolongation"],
  tags: ["jet-bundle", "frobenius-hopf", "category-theory"],
  uses: ["def:categorical-jet"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-jet-prolongation-0.svg", blockIndex: 0, hash: "4cae20680c94" },
  ],

});
