import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:terminal-resolution",
  lean: { ref: "qou:QOU.Experimental.terminal_resolution",
    validation: "not_checked",
  },
  title: "Terminal Resolution of Hadronic Mass",
  uses: [
    "rem:skein-mass-relation",
    "cor:mass-identity-C",
  ],
  proofs: ["prf:terminal-resolution"],
  tags: ["mass", "hadronic"],
});
