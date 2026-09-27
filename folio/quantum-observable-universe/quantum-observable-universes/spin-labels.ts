import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spin-labels",
  title: "Spin labels and the fundamental object",
  lean: { ref: "qou:QOU.SpinDecomposition",
    validation: "axioms_only",
  },
  uses: ["thm:su2-emergence"],
  proofs: ["prf:spin-labels"],
  examples: ["ex:spin-labels-su2"],
  tags: ["spin", "gauge-group"],
});
