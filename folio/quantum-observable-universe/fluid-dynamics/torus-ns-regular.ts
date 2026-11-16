import { example } from "../../schema/builders";

export default example({
  label: "ex:torus-ns-regular",
  title: "The torus quantum universe: $\\chi(A) = 0$ and NS regularity",
  uses: [
    "def:ns-obstruction",
    "thm:ns-singularity-descartes",
  ],
  tags: [
    "example",
    "torus",
    "euler-characteristic",
    "ns-regular",
    "contrast",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped per owner decision (Q-VO9T-2 = 1, beans qou-nzyr, qou-507c, qou-hjl0): " +
        "(1) $\\mathrm{NS}(A)$ is now evaluated as the global surface Euler class $e(\\xi) = 0 \\in H^2(\\Sigma_1, \\mathbb{Z})$ " +
        "(rather than the vacuous curve restriction $\\kappa_0|_\\Sigma = 0$), restoring the non-degenerate contrast with Bring's surface ($e(\\xi) = -6$); " +
        "(2) the withdrawn Levi core-flattening sentence and the unqualified classical NS global regularity claim are scoped " +
        "against 2D Ladyzhenskaya regularity vs the 3D Tao averaged-NS barrier (`docs/audits/2026-10-12-ns-v3-tao-barrier.md`, row 9); " +
        "(3) 2D genus-1 spectral surfaces are distinguished from closed 3-manifolds (which all have $\\chi(M^3) = 0$ by Poincaré duality).",
      see: "../../../../docs/audits/2026-10-12-ns-v3-tao-barrier.md",
    },
  ],
});
