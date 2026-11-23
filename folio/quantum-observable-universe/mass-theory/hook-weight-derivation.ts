import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hook-weight-derivation",
  title:
    "Hook weight $\\beta_4 = -\\tfrac{1}{2} w_{[2,2]}(4)$ from baryon Wedderburn-Artin decomposition",
  lean: { ref: "qou:QOU.BaryonWeight.beta4_hook",
    validation: "not_checked",
  },
  uses: [
    "prop:degree-two-baryon-weight",
    "conj:shell-transition-knot",
  ],
  authorNotes: [
    { kind: "status", date: "2026-11-21", body: "Demoted from `conj:hook-weight-derivation` (owner, #8526, 2026-11-21; bean qou-tm3c). In the Lean, $\\beta_4 = -\\tfrac12 w_{[2,2]}(4)$ is the definition of $\\beta_4$. That this is the coefficient of $\\Phi_4$ in the four-channel mass formula is not derived. The weight $w_{[2,2]}(4) = ([4]_q/[2]_q)^2/[4]_q!$ is itself computable." },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The `ℝ` in `lean/QOU/BaryonWeight/beta4_hook.lean` carries an " +
        "**empirical numerical value with a tolerance**: the class field " +
        "`w_22_approx : |w_22 - 0.166| < 0.01` records the Wedderburn-Artin " +
        "weight `w_{[2,2]}(4)` read off the `H₄(R, q)` decomposition at the " +
        "substrate, and the derived bound is `|β₄ + 0.083| < 0.005`. Decimal " +
        "literals with an experimental tolerance are the §7c \"experimental " +
        "value → `ℝ`\" row, so the `ℝ` is forced by the statement rather than " +
        "chosen.",
    },
  ],
});
