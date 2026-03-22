import { definition } from "../../schema/builders";

export default definition({
  label: "def:spin-labels",
  title: "Spin labels and the fundamental object",
  lean: {
    decl: "QOU.SpinLabels",
    validation: "axioms_only",
  },
  status: "not_started",
  uses: ["def:quantum-observable-universe", "thm:su2-emergence"],
  examples: ["ex:spin-labels-su2"],
  tags: ["spin", "gauge-group"],
});
