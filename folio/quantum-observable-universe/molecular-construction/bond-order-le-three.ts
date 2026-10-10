import { proposition } from "../../schema/builders";

/**
 * Spatial-dimension bound on bond order: pairwise-orthogonal nonzero channels
 * in ℝ³ number at most 3, so no p-block bond exceeds order three. Resolves to
 * the library theorem QOU.Molecular.orthogonal_channels_le_dim (sorry-free).
 */
export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). Here the $\\mathbb{R}$ is load-bearing in the " +
        "proposition itself, not incidental, so it is recorded rather than " +
        "removed. `QOU.Molecular.orthogonal_channels_le_dim` reads a family " +
        "`v : ι → EuclideanSpace ℝ (Fin 3)` that is pairwise `inner`-orthogonal " +
        "and nowhere zero, and concludes `Fintype.card ι ≤ 3`. The step that " +
        "does the work is *orthogonal and nonzero implies linearly " +
        "independent*, and that step is false without positive-definiteness: " +
        "over a general commutative ring there is no inner product at all, and " +
        "over a general field a symmetric bilinear form admits isotropic " +
        "vectors, so an \"orthogonal\" family of nonzero vectors can be " +
        "dependent. Definiteness is an order condition, which §7c places on " +
        "the archimedean side. The physical reading is the same: the bound is " +
        "the dimension of *space*, so the ambient object is $\\mathbb{R}^3$.\n\n" +
        "Two generalisations were considered and rejected as wall-dodges " +
        "rather than wall-crossings. Widening `ℝ` to `[RCLike 𝕜]` (which is " +
        "what Mathlib's `linearIndependent_of_ne_zero_of_inner_eq_zero` " +
        "supports) only reparametrises \"$\\mathbb{R}$ or $\\mathbb{C}$\" and " +
        "leaves the analysis intact; widening to `[LinearOrderedField R]` is " +
        "explicitly still archimedean-side in the §7c table. The only genuinely " +
        "ring-generic step, *linearly independent in rank 3 implies " +
        "cardinality $\\le 3$*, is already a one-line Mathlib citation " +
        "(`LinearIndependent.fintype_card_le_finrank`) and gains nothing from " +
        "being restated here.\n\n" +
        "The supporting `EmbeddableKnotOperator` structure in the same file is " +
        "archimedean for an independent reason: its fields `weight_pos` " +
        "($0 < w$) and `weight_le_one` ($w \\le 1$) are order hypotheses on a " +
        "real overlap weight, and `baseBinding` is an energy. The one " +
        "genuinely algebraic fact there — `multipleBond_binding`, " +
        "$\\sum = b\\,(1 + m w)$ — is a `CommRing` identity, but it is stated " +
        "about that ordered structure and so cannot be lifted off " +
        "$\\mathbb{R}$ without dropping the order fields that carry the " +
        "physics.",
      see: "folio/quantum-observable-universe/lean/QOU/Molecular/EmbeddableKnotOperator.lean",
    },
  ],
  label: "prop:bond-order-le-three",
  title: "Bond order bounded by spatial dimension",
  lean: {
    ref: "qou:QOU.Molecular.orthogonal_channels_le_dim",
    validation: "not_checked",
  },
  uses: ["def:embeddable-knot-operator"],
  tags: [
    "bond-order",
    "spatial-dimension",
    "orthogonal-channels",
    "p-block",
    "sigma-pi",
  ],
});
