import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-tail-archimedean-action",
  lean: {
    ref: "qou:QOU.QBeta.HabiroTailAction.habiroAction_eq_pi_sq_div_five",
    validation: "not_checked",
  },
  title:
    "Archimedean $\\rho_\\infty$ Habiro-tail action of $4_1$ is $\\pi^2/5$ (golden-ratio dilogarithm), distinct from the geometric $\\mathrm{Vol}$ face",
  tags: [
    "resurgence",
    "habiro-tail",
    "quantum-dilogarithm",
    "golden-ratio",
    "archimedean",
    "hbar-N-wall",
  ],
  cites: ["hakimoglu-brown2025", "zagier-dilogarithm", "crew2023", "garoufalidis-wheeler-modular"],
  uses: ["def:ecalle-borel-resummation"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-18",
      body:
        "Lean `QOU.QBeta.HabiroTailAction` (lean-direct exit 0, sorry-free): " +
        "`habiroFactor_bar_even` (bar-even, no hypotheses); `li2_inv_phi_sq` " +
        "DERIVES the golden-ratio Landen value $\\mathrm{Li}_2(\\varphi^{-2}) = " +
        "\\pi^2/15 - \\ln^2\\varphi$ from the three standard functional " +
        "equations (Euler reflection, duplication, Landen) packaged as the " +
        "cited class `ClassicalDilog`, by linear elimination at the golden " +
        "points; `habiroAction_eq_pi_sq_div_five` then gives $A_0 = \\pi^2/5$. " +
        "Conditional on the cited (Mathlib-gap) dilog functional equations, " +
        "not on any conjecture. Probe " +
        "`qbeta_fourone_habiro_tail_action_probe` (4/4). The PHYSICAL relevance " +
        "of the real-q face to the $Q_\\beta$ odd channel is the open bridge " +
        "(#3966 b3ix); this block asserts only the archimedean math fact.",
    },
  ],
});
