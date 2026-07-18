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
      kind: "caveat",
      date: "2026-07-18",
      body:
        "**Self-similar clause (item 3) re-scope + critical-exponent inconsistency.** (i) The backward-self-similar Leray profile posited in item 3 is excluded by Nečas–Růžička–Šverák (Acta Math. 176, 1996) — re-scope to discretely-self-similar / Type-II. (ii) The critical exponent $\\alpha$ is over-determined, not undetermined: the corpus boxes $\\alpha = 4/3$ (cascade-depth, `p2-critical-exponent`) while the Gronwall bound in the same file gives $\\alpha = 1$; the dissipation closure $\\varepsilon = \\nu_q\\Omega$ also gives $\\alpha = 1$ (Lean `enstrophy_alpha_one_of_dissipation_closure`). Each value is conditional on its named closure; none is rigorous. (iii) The Hausdorff claim $d_H = 2$ should be reconciled with the Caffarelli–Kohn–Nirenberg parabolic bound $\\le 1$. The three obstructions are motivation (energy-supercriticality of 3D NS), not proof ingredients. Tracked under beans `qou-xq2w` / `qou-15gb`.",
      see: "../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md",
    },
  ],
});
