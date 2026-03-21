import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-jet-prolongation",
  title: "Jet prolongation",
  hasProof: false,
  tags: ["jet-bundle", "frobenius-hopf", "category-theory"],
  uses: [
    "def:categorical-connection",
    "def:categorical-jet",
  ],
  lean: {
    decl: "QOU.categorical_jet_prolongation",
    file: "QOU/CategoricalJetProlongation.lean",
    validation: "leanok",
  },
});
