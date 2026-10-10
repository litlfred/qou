import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-filter-classification",
  title:
    "Fermion--boson classification by commutator with curvature",
  tags: ["fermion", "boson", "algebraic-filter", "curvature", "classification"],
  lean: { ref: "qou:QOU.Torsion.algebraic_filter_classification",
    validation: "not_checked",
  },
  uses: ["rem:q-harmonic-basis-brane"],
  examples: ["rem:q-harmonic-basis-brane", "rem:weight-space-decomposition", "rem:algebraic-filter", "rem:distributional-connection"],
});
