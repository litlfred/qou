import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:leray-profile",
  lean: { ref: "qou:QOU.FluidDynamics.leray_profile", validation: "not_checked" },
  title:
    "Self-similar blowup profile: the Leray equations with $\\mathrm{SU}_q(2)$ constraints",
  uses: ["thm:ns-singularity-descartes"],
  tags: [
    "leray",
    "self-similar",
    "blowup-profile",
    "elliptic",
    "representation-theory",
    "construction",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-07-18",
      body:
        "**Backward-self-similar profile excluded (Nečas–Růžička–Šverák 1996).** A nontrivial *backward-self-similar* Leray profile with finite-energy ($V \\in L^2$, resp. $V \\in L^3$) is ruled out by Nečas, Růžička & Šverák, *On Leray's self-similar solutions of the Navier–Stokes equations*, Acta Math. **176** (1996) 283–294 (and Tsai 1998 for local-energy conditions): any such $V$ is trivial. The finite-dimensional reduction proved in the Lean sibling is unaffected (it is a reconstruction identity, not an existence claim), but the *self-similar existence* clause must be re-scoped to **discretely-self-similar** or **Type-II** (non-self-similar) asymptotics. Tracked under bean `qou-xq2w`.",
      see: "../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md",
    },
  ],
});
