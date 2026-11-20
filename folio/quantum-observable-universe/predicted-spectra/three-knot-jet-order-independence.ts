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
    validation: "stub",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): , `jetOrder3_certificate`)" },
  ],
});
