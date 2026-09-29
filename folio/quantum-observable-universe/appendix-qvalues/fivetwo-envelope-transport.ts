import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fivetwo-envelope-transport",
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoDeformedSaddle.envelopeS_total",
    validation: "not_checked",
  },
  title:
    "The $5_2$ envelope transports to $S(\\pi) - S(0) = \\pi^2$, tolerating the one point where the root labelling fails",
  tags: [
    "five-two",
    "envelope",
    "monodromy",
    "symmetric-function",
    "deformed-saddle",
    "non-vacuity",
  ],
  uses: ["prop:fivetwo-saddle-sum-rule"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-19",
      body:
        "**Proved sorry-free** — Lean " +
        "`QOU.QBeta.FiveTwoDeformedSaddle.envelopeS_total` " +
        "(`FiveTwoTransport.lean`), via `envelope_integrate`, together with " +
        "`envelopeS_total_nonvacuous`. The arc machinery (`arcX`, " +
        "`hasDerivAt_arcX`, `arcX_arg`, the branch-cut avoidance lemmas) is " +
        "proved in the same file.",
    },
    {
      kind: "caveat",
      date: "2026-08-19",
      body:
        "**The derivative is a hypothesis, not a result.** What is formalised " +
        "is the passage from $dS/d\\varphi = 2\\varphi$ to the total " +
        "$\\pi^2$ — the integration step, tolerating one exceptional point. " +
        "The identification of the integrand is **numerical** (Route 30: " +
        "$S' = 2\\varphi$ per root to $4.6 \\times 10^{-41}$, summed to " +
        "$9.2 \\times 10^{-41}$) and is not formalised. Likewise the three " +
        "root-paths are parameters, not constructed.",
    },
    {
      kind: "note",
      date: "2026-08-19",
      body:
        "The non-vacuity theorem is worth noticing as authoring practice. A " +
        "conditional whose hypotheses are unsatisfiable proves nothing, and " +
        "`envelopeS_total_nonvacuous` rules that reading out explicitly by " +
        "exhibiting $S(\\varphi) = \\varphi^2$. The example is deliberately " +
        "trivial — it exists to establish non-emptiness, not to supply " +
        "evidence — and the file says so. This is the honest counterpart to " +
        "the anti-vacuity discipline in AGENTS.md §Strict Lean Discipline.",
    },
    {
      kind: "note",
      date: "2026-08-19",
      body:
        "The reusable structural point, stated in the block body: a " +
        "**symmetric** function of a family of roots is insensitive to the " +
        "monodromy that permutes them, so an obstruction to labelling the " +
        "branches is not an obstruction to the symmetric total. That is why " +
        "one exceptional point suffices here, and it is not specific to " +
        "$5_2$.",
    },
  ],
});
