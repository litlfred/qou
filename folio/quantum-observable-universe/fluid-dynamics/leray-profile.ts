import { definition } from "../../schema/builders";

export default definition({
  label: "def:leray-profile",
  renamedFrom: ["prop:leray-profile"],
  lean: { ref: "qou:QOU.FluidDynamics.LerayProfile.DSSLerayProfile" },
  title: "Discretely self-similar Leray profile",
  defines: ["discretely-self-similar"],
  uses: [],
  tags: [
    "leray",
    "discretely-self-similar",
    "blowup-profile",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body:
        "**Base ring (§7c).** The Lean sibling `leray-profile.lean` is archimedean by construction and states its types over `ℝ`: the Leray rescaling uses `Real.sqrt`, `Real.log` and `Real.exp`, the field lives on Euclidean `ℝ³`, and the hypothesis `t < T*` is an order condition. It is a post-wall specialisation; no generic-ring statement of the rescaling exists.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Demoted from `prop:leray-profile` to a definition on owner instruction (issue #8864). The proposition proved nothing: it stated a definition, a literature exclusion, and three claims now withdrawn — that the root-of-unity ladder $q_\\kappa = e^{i\\pi/\\kappa}$ fixes a scaling $\\lambda_\\kappa$ (it is a root of unity, excluded by `def:substrate-parameter`), that the profile decomposes into $\\mathrm{SU}_q(2)$ weight-$j$ components (velocity fields carry only integer degrees), and that the truncation at $k_{\\max} \\approx 4$ is an exact finite ODE system (it is a Galerkin truncation). It also stated the Nečas--Růžička--Šverák hypothesis as $V \\in L^2$; it is $V \\in L^3$. The exclusions and the Tao scope note moved to `rem:leray-profile-exclusions`. The Lean sibling `leray-profile.lean` now proves that $s$-periodicity implies discrete scaling invariance (the converse is stated in prose and not formalised) with $P = 2\\log\\lambda$; the former library theorem `QOU.FluidDynamics.leray_profile` is kept as a Galerkin reconstruction identity.",
    },
  ],
});
