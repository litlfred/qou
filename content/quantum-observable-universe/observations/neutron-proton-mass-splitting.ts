import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:neutron-proton-mass-splitting",
  title: "Neutron--proton mass splitting from quark crossing change",
  uses: [
    "prop:wedderburn-mass-formula",
    "def:categorical-proton",
    "def:categorical-neutron",
  ],
});
