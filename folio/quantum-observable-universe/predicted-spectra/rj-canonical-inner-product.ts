import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:rj-canonical-inner-product",
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
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "`HeckeRepRingContext` types `q`, `qDim`, `fullTwistEig`, " +
        "`rjPairing`, `jonesPoly` and `tr_M_char` over `ℝ`: these are " +
        "*evaluated* representation-ring quantities at the substrate " +
        "anchor, not the Laurent-polynomial objects they specialise. The " +
        "module also sits under `QOU/Archimedean/`, which is the " +
        "directory-level statement of the same fact.",
    },
  ],
});
