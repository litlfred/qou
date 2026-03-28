import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-filter-classification",
  title:
    "Fermion--boson classification by commutator with curvature",
  tags: ["fermion", "boson", "algebraic-filter", "curvature", "classification"],
  lean: {
    decl: "QOU.Torsion.algebraic_filter_classification",
    validation: "not_checked",
  },
  uses: ["rem:q-harmonic-basis-brane"],
});
