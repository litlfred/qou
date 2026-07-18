import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:regularity-breakdown",
  lean: { ref: "qou:QOU.FluidDynamics.RegularityBreakdown" },
  title: "Regularity breakdown at $q = 1$: the classical limit as a phase transition",
  uses: [
    "thm:q-ns-wellposedness",
    "prop:q-turbulence-spectrum",
    "rem:hamilton-jacobi-phase",
  ],
  tags: [
    "tier:famous",
    "navier-stokes",
    "millennium-problem",
    "regularity",
    "phase-transition",
    "critical-exponent",
    "blowup",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-07-18",
      body:
        "Three audit-2026-07-18 findings landed. (i) Item 3 re-scoped from continuous backward-self-similar to *discretely* self-similar ($s$-periodic), the continuous case excluded by Nečas–Růžička–Šverák (Acta Math. 176, 1996); see `prop:leray-profile`. (ii) The critical exponent $\\alpha$ is now presented as closure-dependent, not a single boxed value: $\\alpha = 1$ (dissipation closure $\\varepsilon = \\nu_q\\Omega$, Lean `enstrophy_alpha_one_of_dissipation_closure`) vs $\\alpha = 4/3$ (Kolmogorov cascade), neither rigorous — see `p2-critical-exponent`. (iii) Item 2 now flags the $d_H = 2$ (spatial) vs Caffarelli–Kohn–Nirenberg (parabolic $\\le 1$) reconciliation as a required, not-yet-carried-out step. The three obstructions remain motivation (energy-supercriticality of 3D NS), not proof ingredients. Bean `qou-15gb`.",
      see: "../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md",
    },
  ],
});
