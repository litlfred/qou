import { proof } from "../../schema/builders";

export default proof({
  label: "prf:confinement-sdp",
  title: "Proof of confinement sdp",
  uses: ["prop:confinement-sdp"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): 3. **The scalar LP is the diagonal restriction.** When every Wedderburn\n   block decouples (no off-diagonal pair constraint binds), the matrix\n   SDP collapses block-by-block to the\n   [confinement LP](#prop:confinement-lp), with equal primal/dual values." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (`ctx.slaterStrictFeasible`: ...)\n\nThe Lean sibling encodes the data as `ConfinementSDPData` and states\n`confinement_sdp` conditional on `slaterStrictFeasible`; the conic-duality\nstep is deferred there via `sorry` (`-- Ref: [leitner2026]`), pending a\nMathlib SDP strong-duality API. $\\square$" },
  ],
});
