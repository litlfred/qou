import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the construction of $R[q, q^{-1}][i]/(i^2+1)$ is routine commutative algebra, its mathematical novelty here is that this specific elementary ring is proven to universally parameterise the chart-transition data of the quantum projective line. Instead of taking the deformation parameter $q$ and the imaginary unit $i$ as externally posited constants, this algebraic derivation strictly recovers them as the unavoidable geometric consequences of requiring chart-transition invertibility and chart-swap reflection within the non-commutative coordinate algebra." },
  ],
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
  uses: ["rem:affine-chart-origin-of-i-and-q"],
});
