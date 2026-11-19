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
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "note",
      date: "2026-07-25",
      body:
        "**Sustained forcing is the surviving classical-blow-up channel.** The surreal-bridge campaign (ledger `docs/audits/2026-07-25-qns-surreal-bridge-campaign-ledger.md`) progressively localised where the singular data $v_0$ of this conjecture can live: fixed Gevrey data is grade-0 regular (theorem `gevrey_grade_zero`); the anti-parallel-pair collision channel regularises in-model for every positive core size (analytic race $u = 1 - (V_{1,0}/d_0^2)^{2/3} < 1$, Lean `overlap_race_strict`, witnesses `qns-overlap-race-probe` / `qns-pair-riccati-probe`); the dissipation closure excludes grade-1-deep cascades (`closure_excludes_deep_cascade`). The regime not excluded by any of these — and where the enstrophy-grade probe measures $\\alpha \\approx 4/3$ exceeding the grade-1 cap — is **sustained/forced turbulence**. Candidate $v_0$ searches should therefore target sustained-forcing-like spectra, not clean finite structures. All in-model/scope-(a); this conjecture remains open.",
      see: "../../../../docs/audits/2026-07-25-qns-surreal-bridge-campaign-ledger.md",
    },
    {
      kind: "refined-framing",
      date: "2026-07-18",
      body:
        "Three audit-2026-07-18 findings landed. (i) Item 3 re-scoped from continuous backward-self-similar to *discretely* self-similar ($s$-periodic), the continuous case excluded by Nečas–Růžička–Šverák (Acta Math. 176, 1996); see `prop:leray-profile`. (ii) The critical exponent $\\alpha$ is now presented as closure-dependent, not a single boxed value: $\\alpha = 1$ (dissipation closure $\\varepsilon = \\nu_q\\Omega$, Lean `enstrophy_alpha_one_of_dissipation_closure`) vs $\\alpha = 4/3$ (Kolmogorov cascade), neither rigorous — see `p2-critical-exponent`. (iii) Item 2 now flags the $d_H = 2$ (spatial) vs Caffarelli–Kohn–Nirenberg (parabolic $\\le 1$) reconciliation as a required, not-yet-carried-out step. The three obstructions remain motivation (energy-supercriticality of 3D NS), not proof ingredients. Bean `qou-15gb`.",
      see: "../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md",
    },
  ],
});
