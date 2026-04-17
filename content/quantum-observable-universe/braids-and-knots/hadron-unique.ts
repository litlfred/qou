import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hadron-unique",
  title: "Uniqueness of hadrons up to braid isotopy",
  lean: {
    decl: "QOU.Hadron.unique_up_to_isotopy",
    validation: "not_checked",
  },
  uses: [
    "def:hadron",
    "prop:hadron-exists",
  ],
  proofs: ["prf:hadron-unique"],
  tags: ["uniqueness", "hadron", "isotopy"],
});
