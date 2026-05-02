import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-q-tower-algebraic-stratification",
  title:
    "Algebraic stratification of the Φ$_q$ tower in $H_n(R, q)$ (no 3-manifold language)",
  lean: {
    ref: "qou:QOU.BraidKnot.phi_q_tower_algebraic_stratification",
    validation: "not_checked",
  },
  uses: [
    "def:phi-q-piece",
    "prop:mass-endomorphism-tower",
    "prop:graded-markov-trace-from-gs-filtration",
    "prop:gb-spectral-sequence",
  ],
  cites: ["bokut1978", "shirshov1962", "jones1987"],
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
