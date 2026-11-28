import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-beltrami-regular-flow",
  lean: {
    ref: "qou:QOU.FluidDynamics.BeltramiSteadyEuler.L3.deformation_V",
    validation: "not_checked",
  },
  title: "The fibre-rotation field of $\\mathrm{UT}(\\Sigma_4)$ is a regular Navier--Stokes flow",
  uses: [
    "def:brings-surface",
    "thm:ns-singularity-descartes",
  ],
  cites: ["ebin-marsden1970", "etnyre-ghrist2000"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-28",
      body:
        "**Contact-Beltrami provenance (`etnyre-ghrist2000`).** Etnyre and Ghrist (2000, Theorem 2.1 and Corollary 2.2) prove that on any oriented Riemannian $3$-manifold, non-singular rotational Beltrami fields ($\\mathrm{curl}\\,u = \\lambda u$, $\\lambda \\neq 0$) are up to smooth rescaling identical to Reeb vector fields of contact forms, and generate steady incompressible Euler solutions. Here $V/s$ satisfies $\\mathrm{curl}(V/s) = -s(V/s)$ on $(M, g_s)$ with $M = \\mathrm{UT}(\\Sigma_4)$, realising the Boothby--Wang contact Reeb field of the Bring-cone link. **Claim boundary:** Etnyre--Ghrist identifies steady Euler ($\\nu = 0$) with Reeb dynamics for a compatible metric; the viscous Navier--Stokes persistence at $\\nu > 0$ under $L_{\\mathrm{Def}}, L_H, L_B$ uses the Killing/Weitzenb\u00f6ck identities proved in `QOU.FluidDynamics.BeltramiSteadyEuler` and covers only the one-dimensional ray $\\mathbb{R}\\cdot V$, not generic initial data.",
    },
  ],
  tags: [
    "navier-stokes",
    "euler",
    "beltrami",
    "killing-field",
    "reeb",
    "descartes",
    "regularity",
  ],
});
