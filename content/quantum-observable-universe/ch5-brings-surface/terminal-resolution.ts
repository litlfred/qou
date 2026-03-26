import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:terminal-resolution",
  lean: {
    decl: "QOU.Experimental.terminal_resolution",
    validation: "not_checked",
  },
  title: "Terminal Resolution of Hadronic Mass",
  uses: [
    "rem:skein-mass-relation",
    "ex:c-quantum-observable-universe",
    "def:mass-identity",
    "thm:topological-mass",
    "cor:mass-identity-C",
    "prop:topological-mass-formula",
  ],
  proofs: ["prf:terminal-resolution"],
  tags: ["mass", "hadronic"],
});
