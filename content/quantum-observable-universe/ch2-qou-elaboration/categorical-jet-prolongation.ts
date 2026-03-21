import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-jet-prolongation",
  title: "Jet prolongation",
  hasProof: false,
  tags: ["jet-bundle", "categorical"],
  lean: {
    decl: "QOU.categorical_jet_prolongation",
    file: "QOU/CategoricalJetProlongation.lean",
    validation: "leanok",
  },
  uses: [
    "def:categorical-connection",
    "def:categorical-jet",
  ],
});
