import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-coordinate-ring",
  lean: {
    ref: "qou:QOU.QuantumObservableUniverse.CategoricalCoordinateRing",
    validation: "not_checked",
  },
  title:
    "The categorical-coordinate ring $R[i, q^{\\pm 1}]$ of " +
    "chart-transition data on $\\mathbb{P}_q(V)$",
  tags: [
    "categorical-coordinate",
    "chart-transition",
    "projective-line",
    "imaginary-unit",
    "substrate-parameter",
    "ring-extension",
    "universal-property",
  ],
  uses: [
    "def:projective-line-object",
    "def:contact-affine-chart",
    "prop:braiding-eigenvalue-extraction",
    "def:quantum-gauge-group",
    "rem:affine-chart-origin-of-i-and-q",
    "rem:braiding-unit-circle-convention",
  ],
});
