import { remark } from "../../schema/builders";

export default remark({
  label: "rem:terminal-resolution",
  lean: {
    decl: "QOU.Experimental.terminal_resolution",
    validation: "not_checked",
  },
  title: "Terminal Resolution of Hadronic Mass (Observation)",
  uses: [
    "rem:skein-mass-relation",
    "ex:c-quantum-observable-universe",
    "def:mass-identity",
    "thm:topological-mass",
    "cor:mass-identity-C",
    "conj:topological-mass-formula",
  ],
  tags: ["mass", "hadronic"],
});
