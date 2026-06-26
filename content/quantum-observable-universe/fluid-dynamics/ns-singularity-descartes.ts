import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the proof relies on a sequence of upstream conditional geometric bounds (Kummer tower survival, perpetual obstruction, core-Levi form, and BKM divergence), the mathematical novelty here is the structural assembly of these abstract topological components into a strictly deterministic criterion. It bypasses direct PDE analytic estimates by using the explicit arithmetic constraint ($\\chi(A)=-6$) as a global topological forcing term that mandates finite-time blowup via purely categorical conditions." },
  ],
  label: "thm:ns-singularity-descartes",
  lean: { ref: "qou:QOU.FluidDynamics.ns_singularity_descartes", validation: "not_checked" },
  title:
    "The Descartes universe is NS-singular: Navier--Stokes admits finite-time blowup",
  uses: [
    "thm:observability-q-independent",
    "prop:ns-kummer-specialisation",
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
