import { proposition } from "../../schema/builders";

/**
 * Neutron-proton mass splitting from quark crossing change.
 */
export default proposition({
  label: "prop:neutron-proton-splitting",
  lean: { ref: "qou:QOU.Torsion.neutron_proton_splitting", validation: "not_started" },
  title: "Neutron--proton mass splitting",
  uses: ["thm:wedderburn-mass-formula"],
});
