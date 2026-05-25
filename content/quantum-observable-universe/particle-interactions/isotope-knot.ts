import { definition } from "../../schema/builders";

export default definition({
  label: "def:isotope-knot",
  title: "Isotope as a knot variant of fixed proton block",
  lean: { ref: "qou:QOU.BraidKnot.IsotopeKnot",
    validation: "not_checked",
  },
  uses: ["def:unstable-atom"],
  cites: [],
  tags: [
    "isotope",
    "knot",
    "proton-block",
    "neutron-block",
    "categorical",
  ],
});
