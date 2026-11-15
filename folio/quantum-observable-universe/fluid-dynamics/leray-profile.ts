import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:leray-profile",
  lean: { ref: "qou:QOU.FluidDynamics.leray_profile", validation: "not_checked" },
  title:
    "Discretely self-similar blowup profile: the Leray equations with $\\mathrm{SU}_q(2)$ constraints",
  uses: ["thm:ns-singularity-descartes"],
  tags: [
    "leray",
    "discretely-self-similar",
    "blowup-profile",
    "elliptic",
    "representation-theory",
    "construction",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-07-18",
      body:
        "Re-scoped from *continuous* backward-self-similar to **discretely self-similar** ($s$-periodic in Leray's similarity variables). The continuous ($s$-independent) finite-energy Leray profile is excluded by Nečas–Růžička–Šverák (Acta Math. 176, 1996) + Tsai (1998); the QOU root-of-unity scaling $\\lambda_\\kappa$ supplies the surviving discrete symmetry. The Lean sibling is unaffected — it proves a finite-dimensional reconstruction identity, not an existence claim. Rationale: audit 2026-07-18 Finding 1; bean `qou-xq2w`.",
      see: "../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md",
    },
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "Scope note added per owner decision (Q-VO9T-2 = 1, beans qou-nzyr, qou-507c, qou-hjl0): " +
        "`thm:ns-singularity-descartes` now states only the global Reeb bundle topology ($e(\\xi) = -6 \\in H^2(\\mathcal{S}, \\mathbb{Z})$), " +
        "and the 5-mode Peter–Weyl ODE truncation at $q \\approx 1.110$ is a finite Galerkin/cascade model whose behaviour " +
        "does not by itself transfer to the unforced 3D Navier–Stokes PDE (Tao, J. Amer. Math. Soc. 29 (2016), 601–674; " +
        "`docs/audits/2026-10-12-ns-v3-tao-barrier.md`, row 15).",
      see: "../../../../docs/audits/2026-10-12-ns-v3-tao-barrier.md",
    },
  ],
});
