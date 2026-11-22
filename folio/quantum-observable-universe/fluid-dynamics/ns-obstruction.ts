import { definition } from "../../schema/builders";

export default definition({
  label: "def:ns-obstruction",
  title: "NS obstruction class $\\mathrm{NS}(A)$",
  lean: { ref: "qou:QOU.FluidDynamics.NSObstruction",
    validation: "not_checked",
  },
  uses: ["def:ns-regular-qou"],
  tags: [
    "definition",
    "obstruction",
    "navier-stokes",
    "euler-characteristic",
    "categorical",
    "spectral-gap",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Aligned with `def:ns-regular-qou` per owner decision (Q-VO9T-2 = 1, beans qou-nzyr, qou-hjl0): " +
        "$\\mathrm{NS}(A)$ is placed in the global surface cohomology $H^2(\\mathcal{S}, \\mathbb{Z}) \\cong \\mathbb{Z}$ " +
        "as the Reeb Euler class $e(\\xi)$ of degree $\\chi(A)$ (resolving the degree mismatch between $H^3_{\\mathrm{loc}}(A, \\varTheta)$ " +
        "and $H^2(\\Sigma, \\mathcal{B})$ noted in `docs/audits/2026-10-12-ns-v3-tao-barrier.md` rows 8 and 10), " +
        "and the link to classical unforced 3D Navier–Stokes regularity/blowup is scoped as a framework model correspondence.",
      see: "../../../../docs/audits/2026-10-12-ns-v3-tao-barrier.md",
    },
  ],
});
