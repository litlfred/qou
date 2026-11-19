import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-q-tower-algebraic-stratification",
  title:
    "Algebraic stratification of the Φ$_q$ tower in $H_n(R, q)$ (no 3-manifold language)",
  lean: {
    ref: "qou:QOU.BraidKnot.phi_q_tower_algebraic_stratification",
    validation: "leanok",
  },
  uses: ["def:phi-q-piece"],
  cites: ["shirshov1962", "jones1987"],
  tags: [
    "phi-q",
    "stratification",
    "hecke-algebra",
    "gs-filtration",
    "descent-tower",
    "no-3-manifold",
    "narrative-anchor",
  ],
});
