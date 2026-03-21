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
  rendered: [
    { mime: "image/svg+xml", url: "rendered/terminal-resolution-0.svg", blockIndex: 0, hash: "819cd133b41b" },
    { mime: "image/svg+xml", url: "rendered/terminal-resolution-1.svg", blockIndex: 1, hash: "8800cf8145b6" },
    { mime: "image/svg+xml", url: "rendered/terminal-resolution-2.svg", blockIndex: 2, hash: "c65bdec0bd3a" },
  ],

});
