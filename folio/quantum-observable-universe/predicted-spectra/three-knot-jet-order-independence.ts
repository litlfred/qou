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
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean formalisation (`QOU.Archimedean.JetOrderIndependence`): base-order LU certificate `jetOrder3_certificate`; full-rank base minor `jetJacobianBase_rank`; abstract monotonicity principle `jacobianRank_eq_three_of_base`; surreal bridge uniformity and composition `transport_uniform_bound`, `transport_shadow_vanishes`.",
    },
  ],
});
