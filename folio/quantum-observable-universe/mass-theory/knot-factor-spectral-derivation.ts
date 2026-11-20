import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-factor-spectral-form",
  title:
    "Knot factor $a_K$ as a central Gram pairing",
  lean: {
    ref: "qou:QOU.BraidKnot.knot_factor_spectral_form",
    validation: "not_checked",
  },
  // rem:gram-matrix-spectral-connection dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // not cited in the statement or proof. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: [],
  tags: [
    "knot-factor",
    "chirality",
    "gram-matrix",
    "plancherel",
    "wedderburn",
    "amphicheiral",
    "borromean",
    "shell-closed",
    "no-ad-hoc-fits",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body:
        "**Restated 2026-11-16 (QA finding: da-non-sequitur, critical).** The block " +
        "previously set $a_K = G_{\\beta,\\beta^*}/G_{\\mathbf{1},\\mathbf{1}}$ with weights " +
        "$\\dim_q^2 V_\\lambda/[n]_q!$. At $\\beta = \\mathbf{1}$ that gave " +
        "$1 = \\sum_\\lambda \\dim_q^2 V_\\lambda/[n]_q!$, which the block itself said is false " +
        "for $q \\neq 1$, and the proof treated a braid as central. The knot factor is now " +
        "defined through the central projection $\\pi$, with weights $w_\\lambda = \\tau(e_\\lambda)$, " +
        "which sum to $1$. No compute consumes this formula: the $a_K$ scripts " +
        "(`chirality_avg_content_atomic.py`, `a_K_via_lp_dual`) use their own definitions.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "**§7c base ring — de-specialised off $\\mathbb{R}$ (2026-08-09).** " +
        "The Lean sibling previously typed `HeckeExpansion`'s `c`, `weight` " +
        "and `trivial` fields as `List ℕ → ℝ`, contradicting this block's " +
        "own narrative (*\"we work over $A = H_n(R, q)$… the identity holds " +
        "exactly in $R$\"*). Nothing in the file used an ordering, `Real.*`, " +
        "or any archimedean input, so the specialisation was gratuitous and " +
        "has been removed: `HeckeExpansion`, `knotFactor` and " +
        "`knot_factor_spectral_form` are now generic over " +
        "`{R : Type*} [Field R]`. The change propagates to " +
        "[`cor:knot-factor-amphicheiral`](knot-factor-amphicheiral.md), " +
        "whose 2026-08-07 §7c note attributed its own $\\mathbb{R}$ to this " +
        "file and is superseded there.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "**§7c base-ring-minimal adjudication: the field is essential.** " +
        "With the block now on the algebraic side, the advisory flags the " +
        "`[Field R]` binders (`KnotFactorSpectralDerivation.lean` L42/49/64). " +
        "Adjudged **no change — not a Laurent identity**: the Gram pairing " +
        "is *normalised* by $\\chi_\\lambda(\\mathbf{1})^2 = " +
        "(\\dim_q V_\\lambda)^2$, and $\\dim_q V_\\lambda$ is a Laurent " +
        "polynomial in $q$, not a unit of $\\mathbb{Z}[q^{\\pm 1}]$, so the " +
        "quotient genuinely leaves the Laurent ring for its fraction field " +
        "$\\mathbb{Q}(q)$. A `Units`/$R^\\times$ restatement would assert " +
        "invertibility of every $\\dim_q V_\\lambda$, which is false over " +
        "$\\mathbb{Z}[q^{\\pm 1}]$; `[Field R]` is the weakest §7c class " +
        "admitting the construction. Net effect of the de-specialisation: " +
        "one critical `wall-side-correct` failure retired, one warn-level " +
        "advisory accepted with this adjudication.",
    },
  ],
});
