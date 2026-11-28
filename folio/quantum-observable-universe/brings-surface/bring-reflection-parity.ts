import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-reflection-parity",
  title: "Reflection parity of the harmonics of Bring's surface",
  lean: { ref: "qou:QOU.Brings.ReflectionParity.hopf_trace_h1_reversing" },
  uses: ["prop:bring-harmonic-types", "lem:bring-map-euler-characteristic"],
  cites: ["edge1978"],
  tags: ["brings-surface", "harmonics", "representation-theory", "maass", "reflection", "combinatorial-map"],
  proofs: ["prf:bring-reflection-parity"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Bean `qou-u81q`, the recommended next step after `prop:bring-harmonic-types`. Lean, sorry-free, axioms `propext`, `Classical.choice`, `Quot.sound` only: `QOU/BringsSurface/BringReflectionParity.lean`; the Laplace reading (`parity_types_from_quotient_spectra`) is in `QOU/Transcendental/BringsSurface/BringMaassTypes.lean`. Cell counts are computed over all 120 darts by `decide`. No eigenvalue is computed or used.",
    },
  ],
});
