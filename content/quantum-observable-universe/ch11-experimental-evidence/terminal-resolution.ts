import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:terminal-resolution",
  title: "Terminal Resolution of Hadronic Mass (Observation)",
  uses: ["prop:skein-mass-relation"],
  proofs: ["prf:terminal-resolution"],
  tags: ["mass", "hadronic"],

});
