import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:centre-cocentre-descent",
  title:
    "Centre–cocentre splitting: $A = Z(A)\\oplus[A,A]$ gives a unique descended/transient split that every trace sees only through its central part",
  lean: {
    ref: "qou:QOU.MassCore.CentreCocentre.trace_eq_trace_desc",
  },
  uses: ["def:hochschild-homology", "def:descent-involution"],
  cites: ["geckpfeiffer2000", "dipper-james1986"],
  tags: ["mass-endomorphism", "centre", "cocentre", "trace", "descent", "hecke-algebra"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): that the matrices satisfy the Hecke presentation is verified by hand, not in Lean." },
    {
      kind: "status",
      date: "2026-11-16",
      body: "Proved algebraic core of conj:mass-categorical-descent (issue #8094). Items 1-5 and 7 are sorry-free in the sibling .lean over a generic commutative ring (lean-direct exit 0; axioms propext, Classical.choice, Quot.sound). Item 6 (the Hecke formula for the central projection) is classical and proved on paper only: Mathlib has no Hecke algebra.",
    },
  ],
});
