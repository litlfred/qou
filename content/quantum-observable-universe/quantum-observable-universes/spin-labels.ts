import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spin-labels",
  title: "Spin labels and the fundamental object",
  lean: {
    decl: "QOU.SpinDecomposition",
    validation: "axioms_only",
  },
  uses: ["thm:su2-emergence"],
  proofs: ["prf:spin-labels"],
  examples: ["ex:spin-labels-su2"],
  tags: ["spin", "gauge-group"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/spin-labels-0.svg", blockIndex: 0, hash: "0be1727b0fb3" },
  ],

});
