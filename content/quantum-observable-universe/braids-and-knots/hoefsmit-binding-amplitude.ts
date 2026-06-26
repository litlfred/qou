import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the computation of the Hoefsmit seminormal matrix is a standard algebraic procedure within Hecke representation theory, the mathematical novelty is demonstrating that this specific exact rational relation ($1-b^2 = 1/[2]_q^2$) directly governs the discrete geometric de-entanglement fraction of the pion's mass, reinterpreting an abstract representation-theoretic off-diagonal matrix element as a topological binding constraint." },
  ],
  label: "prop:hoefsmit-binding-amplitude",
  title:
    "Hoefsmit binding amplitude $b^2 = [3]_q / [2]_q^2$",
  lean: { ref: "qou:QOU.BraidsAndKnots.hoefsmit_b_sq_eq_q3_over_q2sq" },
  uses: ["prop:frobenius-lepton-meson-bridge"],
  cites: [
    "wenzl1988c",
  ],
  tags: [
    "hoefsmit",
    "binding-amplitude",
    "meson",
    "pion-decay",
    "q-integer",
    "lepton-meson-bridge",
  ],
});
