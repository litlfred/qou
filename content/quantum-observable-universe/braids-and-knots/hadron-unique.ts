import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hadron-unique",
  title: "Uniqueness of hadrons up to braid isotopy",
  lean: { ref: "qou:QOU.Hadron.unique_up_to_isotopy",
    validation: "not_checked",
  },
  uses: [
    "prop:hadron-exists",
    "def:hecke-normal-form",
  ],
  proofs: ["prf:hadron-unique"],
  tags: ["uniqueness", "hadron", "isotopy"],
});
