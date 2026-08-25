import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fivetwo-discriminant-vanishes",
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoDiscriminant.exists_unit_circle_disc_zero",
    validation: "not_checked",
  },
  title:
    "The GGM curve's discriminant vanishes on the unit circle — two root branches do collide on the arc",
  tags: [
    "five-two",
    "discriminant",
    "branch-collision",
    "monodromy",
    "grid-artifact",
    "refutation",
  ],
  uses: ["prop:fivetwo-envelope-transport", "prop:fivetwo-trace-field"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-19",
      body:
        "**Proved sorry-free** — Lean " +
        "`QOU.QBeta.FiveTwoDiscriminant.exists_unit_circle_disc_zero`, via " +
        "`disc_eq_Q` (palindromy, `field_simp; ring`), `Q_neg_two` / " +
        "`Q_neg_one` (`norm_num`), `exists_root_Q` (IVT) and the " +
        "unit-circle lemmas `norm_onCircle` / `onCircle_add_inv`. Polynomial " +
        "algebra plus one IVT application; no analysis of the branches is " +
        "needed. The $Q$ values and the root location $u \\approx -1.4844$ " +
        "were re-checked independently while writing this block.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-19",
      body:
        "This block records a **refuted argument**, and the failure mode is " +
        "worth naming: $\\min|\\mathrm{disc}| = 0.348$ was a *grid* minimum " +
        "from an $\\approx 360$-point scan, treated as a fact about the " +
        "function. The dip is narrow ($|\\mathrm{disc}'| \\approx 87$), so " +
        "refinement gives $0.068$, then $0.0068$, then $0$. **A minimum over " +
        "samples bounds the samples, not the function** — and the constant " +
        "had been carried into a proof step and into an implicit-function " +
        "hypothesis.",
    },
    {
      kind: "caveat",
      date: "2026-08-19",
      body:
        "**The transport's conclusion is not endangered.** $S$ sums over all " +
        "roots and is symmetric, so a collision merely permutes them and a " +
        "symmetric function cannot notice a permutation; numerically " +
        "$S(e^{i\\varphi}) - S(1) = \\varphi^2$ holds to $4 \\times 10^{-40}$ " +
        "**through** the branch point. Only the per-root labelling dies, and " +
        "only the argument used labels. This is exactly why " +
        "`prop:fivetwo-envelope-transport` tolerates one exceptional point — " +
        "the tolerance is the honest shape of the situation, not a hedge.",
    },
    {
      kind: "note",
      date: "2026-08-19",
      body:
        "$-23$ appears twice here and the two are not alike. " +
        "$\\mathrm{disc}(1) = -23$ **is** the trace-field discriminant: at " +
        "$x = 1$ the curve degenerates to the saddle cubic " +
        "$y^3 - 2y^2 + 3y - 1$ (`ggm_one`), so it is the same object " +
        "recovered at the base point. $Q(-1) = -23$ is a **coincidence** — " +
        "$Q$ takes that value at $u = -1$, $u = 1$ and $u = 2$ alike, and " +
        "only $u = 2$ corresponds to $x = 1$. Separated explicitly, since " +
        "this lane has already lost a claim to reading a shared numeral as a " +
        "shared structure (`rem:fivetwo-three-sevens`).",
    },
  ],
});
