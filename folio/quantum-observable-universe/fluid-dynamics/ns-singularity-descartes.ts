import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ns-singularity-descartes",
  lean: { ref: "qou:QOU.FluidDynamics.ns_singularity_descartes", validation: "not_checked" },
  title:
    "The Descartes universe is NS-singular: Navier--Stokes admits finite-time blowup",
  // `prop:ns-kummer-specialisation` removed 2026-08-15 to break an editorial
  // cycle: it lists this theorem in its own `uses[]`, and its narrative links
  // here while this one never links there. The dependency runs
  // specialisation -> theorem, not both ways.
  uses: [
    "thm:observability-q-independent",
  ],
  tags: [
    "theorem",
    "navier-stokes",
    "blowup",
    "descartes",
    "millennium-problem",
    "categorical",
  ],
});
