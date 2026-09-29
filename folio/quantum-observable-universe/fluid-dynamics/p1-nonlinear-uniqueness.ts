import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-ns-nonlinear-uniqueness",
  lean: { ref: "qou:QOU.FluidDynamics.p1_nonlinear_uniqueness", validation: "not_checked" },
  title:
    "Nonlinear estimates and uniqueness for the $q$-Navier--Stokes system",
  uses: [
    "prop:q-spectral-sobolev",
    "thm:q-ns-wellposedness",
  ],
  tags: [
    "nonlinear-estimate",
    "uniqueness",
    "enstrophy",
    "gronwall",
    "energy-method",
    "regularity",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/FluidDynamics/p1_nonlinear_uniqueness.lean` uses " +
        "`Real.exp`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
