import { proposition } from "../../schema/builders";

/**
 * The Wigner-2 coefficient at k=6 derived from the LP dual:
 * C_{321} = w_{321} · h/2 = [2][4][6]h/(2[3]²[5]).
 *
 * The h/2 is a THEOREM about self-conjugate partitions:
 * conjugation pairs SYT T↔T' with opposite axial distances,
 * and the seminormal paired sum identity gives h per pair.
 */
export default proposition({
  label: "prop:wigner-2-coefficient",
  proofs: ["prf:wigner-2-coefficient"],
  title:
    "Wigner-2 coefficient $C_{[3,2,1]} = w_{[3,2,1]} \\cdot h/2$ from self-conjugate trace pairing",
  lean: { ref: "qou:QOU.BraidKnot.wigner2_coefficient",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-coefficient-shadow-price",
    "prop:hoefsmit-seminormal-form",
  ],
  tags: [
    "wigner",
    "self-conjugate",
    "seminormal",
    "shadow-price",
    "isospin",
    "cyclotomic",
  ],
});
