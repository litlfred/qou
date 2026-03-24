import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spin-labels",
  title: "Spin labels and the fundamental object",
  lean: {
    decl: "QOU.SpinDecomposition",
    validation: "axioms_only",
  },
  uses: ["def:quantum-observable-universe", "thm:su2-emergence"],
  examples: ["ex:spin-labels-su2"],
  tags: ["spin", "gauge-group"],
});
