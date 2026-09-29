import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fivetwo-three-sevens",
  interprets: "prop:fivetwo-trace-field",
  title:
    "Three different sevens attach to $5_2$ — the determinant, the $\\tau$-even Stokes sum, and the cyclotomic level — and none of them is the trace field",
  tags: [
    "five-two",
    "notation-collision",
    "trace-field",
    "alexander-polynomial",
    "cyclotomic",
    "anti-conflation",
  ],
  uses: [
    "prop:fivetwo-trace-field",
    "prop:fivetwo-dt-spectrum-split",
    "prop:fivetwo-level-seven-ladder",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-19",
      body:
        "Interpretive; every constituent is established in the propositions " +
        "it cites. The two comparisons are checked, not asserted: " +
        "$\\mathbb{Q}(\\sqrt{-7}) \\not\\subset K$ by the tower law " +
        "($2 \\nmid 3$), and $\\mathbb{Q}(\\zeta_7)^{+} \\neq K$ by " +
        "discriminant — $49$, totally real, cyclic, versus $-23$, one real " +
        "place, non-Galois with group $S_3$. Both computed directly from the " +
        "minimal polynomials rather than recalled.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-19",
      body:
        "This block exists because the conflation it warns against has " +
        "already cost the corpus a claim: " +
        "`docs/audits/2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md` " +
        "read the invariant trace field off $\\det(5_2) = 7$ and was " +
        "retracted 2026-08-11 (bean `qou-ynff`, PR #5271). The near-miss " +
        "recorded in the body is the reason a bare degree check is not " +
        "enough: $\\mathbb{Q}(\\zeta_7)^{+}$ and $K$ are **both cubic** and " +
        "their minimal polynomials **both open $x^3 - 2x^2$**, so agreement " +
        "of degree and of leading coefficients is worth nothing on its own. " +
        "(A companion over-claim about degree — that an $n$-tetrahedron " +
        "knot's trace field is generically degree $n$ — was itself corrected " +
        "in bean `qou-5gh6`.)",
    },
  ],
});
