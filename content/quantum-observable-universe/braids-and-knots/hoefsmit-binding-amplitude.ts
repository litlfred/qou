import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-binding-amplitude",
  proofs: ["prf:hoefsmit-binding-amplitude"],
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
