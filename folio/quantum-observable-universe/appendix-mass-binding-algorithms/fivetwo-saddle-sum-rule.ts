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
  uses: ["prop:fivetwo-trace-field", "prop:hyperbolic-knot-shape-fields"],
  cites: ["zagier1986", "ohtsuki2016"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Original wording: \"Every step uses only the standard axioms, and `SaddleRoots` is inhabited via the intermediate value theorem\"; \"a statement about a hyperbolic manifold, which is not formalised here\"." },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "**\u00a77c base-ring note (archimedean specialisation).** " +
        "`FiveTwoComplexPentagon.lean` is archimedean throughout, and has " +
        "to be: the statement is an identity among values of `Li_2^ext` at " +
        "complex algebraic points, with `Real.log t` and `Complex.arg a` on " +
        "the right-hand side. `arg` and `log` have no generic-`CommRing` " +
        "form, and the branch bookkeeping that produces the " +
        "$(\\arg a - \\pi)^2$ term is a statement about the real line. " +
        "The \u211d is forced by the statement rather than chosen, so this " +
        "is the \u00a77c archimedean-evaluation row and not a file that " +
        "wants splitting.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "**Merged with a duplicate; this block is the survivor.** " +
        "`thm:five-two-saddle-sum-rule` in `mass-theory` stated the same " +
        "identity, with the same existence quantifier, pointing at the same " +
        "declaration — two statement-bearing blocks owning one Lean " +
        "declaration, which `lean-ref-owns-decl` flags because the formal " +
        "graph can attach it to only one. Not a deliberate pair: that block " +
        "landed 2026-08-15 as exposition, and the 2026-08-19 commit that " +
        "created this one opens \"~180 probes and 33 sorry-free Lean files " +
        "of 5_2 work, and not one content block anywhere in the paper\" — " +
        "the differing slugs (`five-two-` against `fivetwo-`) are why the " +
        "search missed it. This block survives on consumers: three blocks " +
        "read it, none read the other. Its `cites: [zagier1986]`, its " +
        "`uses` of `prop:hyperbolic-knot-shape-fields`, and the two " +
        "passages its prose carried that this one did not — the " +
        "volume-conjecture disclaimer and the shape-field contrast with " +
        "$4_1$ — are folded in here.",
    },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "**What the `not_checked` means, since the retired duplicate said " +
        "`leanok`.** Verified here: the declaration exists — " +
        "`theorem fiveTwo_saddle_sum_rule` at " +
        "`FiveTwoComplexPentagon.lean:1865`, namespace " +
        "`QOU.QBeta.FiveTwoComplexPentagon`, so the ref resolves — and the " +
        "file contains no `sorry`. NOT verified: that it builds. The " +
        "duplicate's `leanok` rested on a `lake env lean` run of " +
        "2026-08-15, which is not a current build, and this container " +
        "cannot produce one — the restored olean cache is dependencies-only " +
        "(zero `QOU.*` modules, by construction), and a `lake build` evicts " +
        "it. Carrying `leanok` forward would assert something nobody has " +
        "checked since August; the provenance is recorded instead.",
    },
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
