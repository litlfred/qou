import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:neutron-proton-mass-splitting",
  proofs: ["prf:neutron-proton-mass-splitting"],
  title: "Neutron--proton mass splitting from quark crossing change",
  lean: { ref: "qou:QOU.NeutronProtonSplitting.splitting_value",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
});
