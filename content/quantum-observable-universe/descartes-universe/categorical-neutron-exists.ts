import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-neutron-exists",
  title: "Existence of the categorical neutron",
  lean: { ref: "qou:QOU.CategoricalNeutron.exists",
    validation: "not_checked",
  },
  uses: ["prop:categorical-proton-exists"],
  proofs: ["prf:categorical-neutron-exists"],
  tags: ["existence", "neutron", "baryon"],
});
