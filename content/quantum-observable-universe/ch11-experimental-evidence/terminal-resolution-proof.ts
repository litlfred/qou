import { proof } from "../../schema/builders";

export default proof({
  label: "prf:terminal-resolution",
  title: "Proof of Terminal Resolution of Hadronic Mass",
  uses: [
    "prop:terminal-resolution",
    "prop:skein-mass-relation",
    "prop:skein-generation",
    "prop:knot-eigenbasis-complete",
  ],
  lean: {
    decl: "QOU.HadronicMass.terminal_resolution_hadronic_mass",
    validation: "leanok",
  },
});
