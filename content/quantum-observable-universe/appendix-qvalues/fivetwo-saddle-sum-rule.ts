import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fivetwo-saddle-sum-rule",
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule",
    validation: "not_checked",
  },
  title:
    "The $5_2$ saddle sum rule: the dilogarithm trace over the three tetrahedron shapes closes to $-\\pi^2/6 - \\tfrac12\\log^2 t + \\tfrac23(\\arg a - \\pi)^2$",
  tags: [
    "five-two",
    "saddle-sum-rule",
    "dilogarithm",
    "five-term-identity",
    "trace-field",
    "bar-even",
  ],
  uses: ["prop:fivetwo-trace-field"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-19",
      body:
        "**Proved sorry-free on the standard axioms** — Lean " +
        "`QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule` " +
        "(`FiveTwoComplexPentagon.lean`), with `fiveTwoSaddleSumRule_holds` " +
        "alongside it. The chain named in the Lean docstring: the complex " +
        "five-term identity at $(y_3,y_1)$ and $(y_3,y_2)$; the anharmonic " +
        "evaluations; the branch equations from $y^2 = (1-y)^3$; the root " +
        "data; the logarithm evaluations. `SaddleRoots` is inhabited via " +
        "`ofRealRoot` (intermediate value theorem), so the statement is about " +
        "the actual roots rather than a possibly-empty structure — the " +
        "existence quantifier is discharged, not assumed.",
    },
    {
      kind: "caveat",
      date: "2026-08-19",
      body:
        "**Bar-EVEN.** The identity is symmetric under $a \\leftrightarrow " +
        "\\bar a$, so the quantity it pins carries no bar-odd information. It " +
        "supplies no bar-odd action value and none is claimed. A bar-odd " +
        "datum requires the *difference* across the conjugate pair, which " +
        "lands on the $\\sqrt{-23}$ line of the trace field " +
        "(`prop:fivetwo-trace-field`) and is a separate question. Recorded " +
        "explicitly because the $5_2$ lane exists to chase the bar-odd " +
        "channel, and a strong bar-even result is easy to mis-read as " +
        "progress on it.",
    },
    {
      kind: "note",
      date: "2026-08-19",
      body:
        "The coefficient $2/3$ is traced in the block body to the branch " +
        "relation $2\\ell_j - 3m_j = 2\\pi i\\varepsilon_j$ imposed by the " +
        "gluing equation $y^2 = (1-y)^3$ — i.e. it is the $2$ and $3$ of the " +
        "gluing exponents, not a fitted constant. Verified against the Lean " +
        "rather than inferred: the contraction " +
        "$\\sum_j \\ell_j m_j = \\tfrac23\\sum_j \\ell_j^2 - " +
        "\\tfrac{2\\pi i}{3}\\sum_j \\varepsilon_j \\ell_j$ appears in " +
        "`FiveTwoComplexPentagon.lean` as the step that introduces it.",
    },
  ],
});
