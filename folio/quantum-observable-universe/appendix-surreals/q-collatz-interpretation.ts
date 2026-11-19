import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-collatz-interpretation",
  title:
    "Skein-Collatz interpretation: the $(p_1^{k_1}, p_2^{k_2})$ family and uniqueness of $(2,3)$",
  interprets: "conj:q-collatz",
  uses: ["prop:collatz-contact-boundary"],
  tags: [
    "collatz",
    "skein-module",
    "contraction-gap",
    "uniqueness",
    "q-integer",
    "family",
    "monomial",
  ],
  cites: ["collatz1937", "lagarias2010"],
  authorNotes: [
    {
      kind: "note",
      body:
        "Lean theorems for the elementary q-integer identities and gap bounds: skein_divisibility, qInt_gap, qInt3_lt_qInt2_sq, geometric_mean_contraction, qInt_gap_3_4, and qInt_gap_3_8_fails.",
    },
  ],
});
