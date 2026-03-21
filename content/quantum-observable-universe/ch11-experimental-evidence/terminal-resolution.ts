import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:terminal-resolution",
  title: "Terminal Resolution of Hadronic Mass",
  uses: ["prop:skein-mass-relation"],
  hasProof: true,
  lean: {
    decl: "QOU.HadronicMass.terminal_resolution_hadronic_mass",
    validation: "leanok",
  },
  tags: ["mass", "hadronic"],
});
