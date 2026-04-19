import { proposition } from "../../schema/builders";

/**
 * Neutron-proton mass splitting from quark crossing change.
 */
export default proposition({
  label: "prop:neutron-proton-splitting",
  lean: {
    decl: "QOU.ParticleInteractions.neutron_proton_splitting",
    file: "QOU/ParticleInteractions.lean",
    validation: "not_checked",
  },
  title: "Neutron--proton mass splitting",
  uses: ["def:atomic-braid", "prop:wedderburn-mass-formula"],
});
