import { proof } from "../../schema/builders";

export default proof({
  label: "prf:terminal-resolution",
  title: "Proof of Terminal Resolution of Hadronic Mass",
  uses: ["prop:terminal-resolution"],
  lean: {
    decl: "QOU.HadronicMass.terminal_resolution_hadronic_mass",
    validation: "leanok",
  },
});
