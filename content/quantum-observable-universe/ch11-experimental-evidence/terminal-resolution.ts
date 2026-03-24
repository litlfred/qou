import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:terminal-resolution",
  lean: {
    decl: "QOU.Experimental.terminal_resolution",
    validation: "not_checked",
  },
  title: "Terminal Resolution of Hadronic Mass (Observation)",
  uses: ["prop:skein-mass-relation", "ex:c-quantum-observable-universe"],
  proofs: ["prf:terminal-resolution"],
  tags: ["mass", "hadronic"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/terminal-resolution-0.svg", blockIndex: 0, hash: "819cd133b41b" },
    { mime: "image/svg+xml", url: "rendered/terminal-resolution-1.svg", blockIndex: 1, hash: "8800cf8145b6" },
    { mime: "image/svg+xml", url: "rendered/terminal-resolution-2.svg", blockIndex: 2, hash: "c65bdec0bd3a" },
  ],

});
