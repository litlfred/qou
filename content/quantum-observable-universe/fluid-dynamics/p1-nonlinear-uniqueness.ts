import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While these steps mirror the standard Ladyzhenskaya/enstrophy arguments for classical 2D fluid uniqueness, the mathematical novelty is demonstrating that this precise package of estimates lifts identically to the non-commutative algebraic $q$-deformed categorical setting without modification, anchoring the well-posedness natively in the quantum group Sobolev spaces rather than classical function spaces." },
  ],
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
});
