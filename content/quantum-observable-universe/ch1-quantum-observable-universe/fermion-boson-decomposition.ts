import { definition } from "../../schema/builders";

export default definition({
  label: "def:fermion-boson-decomposition",
  title: "Fermion--Boson decomposition",
  tags: ["fermion", "boson", "particle"],
  lean: {
    decl: "QOU.Fermion",
    validation: "leanok",
  },
  status: "stated",
  uses: ["def:q-harmonic-form", "def:weight-decomposition"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/fermion-boson-decomposition-0.svg", blockIndex: 0, hash: "e2cd03af6567" },
    { mime: "image/svg+xml", url: "rendered/fermion-boson-decomposition-1.svg", blockIndex: 1, hash: "468ace28c05e" },
  ],

});
