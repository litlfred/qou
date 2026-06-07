import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:three-knot-jet-order-independence",
  title: "Jet-order algebraic independence (QOU-attackable reduction)",
  tags: [
    "hyperbolic-volume",
    "transcendence",
    "jet-order",
    "habiro-ring",
    "groebner-shirshov",
    "surreal-error-bound",
    "open-problem",
  ],
  uses: [
    "conj:hyperbolic-volume-transcendence",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.JetOrderIndependence",
    validation: "not_checked",
  },
});
