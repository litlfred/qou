import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:rj-canonical-inner-product",
  proofs: ["prf:rj-canonical-inner-product"],
  title:
    "Canonical inner product on $R(H_r(q))$ via Schur orthogonality",
  tags: [
    "rosso-jones",
    "representation-ring",
    "inner-product",
    "schur-orthogonality",
    "quantum-dimension",
    "markov-trace",
    "uniqueness",
  ],
  lean: { ref: "qou:QOU.Archimedean.rj_canonical_inner_product",
    validation: "not_checked",
  },
  uses: [
    "prop:cohomological-embedding",
  ],
  cites: [
    "rosso-jones1993",
  ],
});
