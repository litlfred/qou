import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-neutron-unique",
  title: "Uniqueness of the categorical neutron up to braid isotopy",
  lean: { ref: "qou:QOU.CategoricalNeutron.unique_up_to_isotopy",
    validation: "not_checked",
  },
  uses: [
    "prop:categorical-neutron-exists",
    "prop:hadron-unique",
  ],
  proofs: ["prf:categorical-neutron-unique"],
  tags: ["uniqueness", "neutron"],
});
