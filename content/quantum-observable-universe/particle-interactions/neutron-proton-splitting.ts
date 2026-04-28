import { proposition } from "../../schema/builders";

/**
 * Neutron-proton mass splitting from quark crossing change.
 */
export default proposition({
  label: "prop:neutron-proton-splitting",
  title: "Neutron--proton mass splitting",
  uses: ["prop:wedderburn-mass-formula"],
});
