import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hook-weight-derivation",
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
