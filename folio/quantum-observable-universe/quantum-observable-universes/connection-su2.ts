import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-connection",
  label: "ex:connection-su2",
  title: "Connection and curvature on $\\mathcal{O}(\\mathrm{SU}(2))$",
  lean: { ref: "qou:QOU.Examples.su2Connection", validation: "not_checked" },
  uses: ["def:categorical-connection", "ex:fiber-adjoint-su2"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Upon deformation by $q$, this differential structure lifts to the Woronowicz left-covariant calculus on $\\mathcal{O}_q(\\mathrm{SU}(2))$. The left-covariant formulation is used explicitly, as the failure of bi-covariance controls the deformation of the exterior derivative." },
  ],
  tags: ["su2", "connection"],
  cites: [
    "woronowicz1987-twisted-su2",
  ],
});
