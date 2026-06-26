import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "The synthesis that knot types form a complete eigenbasis for $\\varinjlim V^{\\otimes n}$, which conceptually replaces Feynman's continuum integral, is a genuinely framework-specific and novel mathematical synthesis. The accompanying Lean formalization achieves a careful combining and conditional proof over bundled standard results." },
  ],
  label: "prop:knot-eigenbasis-complete",
  lean: { ref: "qou:QOU.Braiding.knot_eigenbasis_complete",
    validation: "not_checked",
  },
  title: "Completeness of the knot-type eigenbasis",
  tags: ["braid-group", "hecke-algebra", "knot-invariant", "schur-weyl"],
  uses: ["prop:braid-action-tensor"],
  proofs: ["prf:knot-eigenbasis-complete"],
});
