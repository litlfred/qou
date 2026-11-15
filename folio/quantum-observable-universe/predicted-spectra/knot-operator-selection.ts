import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-selection",
  lean: { ref: "qou:QOU.Archimedean.knot_operator_selection", validation: "not_checked" },
  title: "Knot operator selection via Frobenius dual",
  uses: ["prop:rj-canonical-inner-product"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-09-14",
      body:
        "**(iii) corrected: the Frobenius pairing is DEGENERATE at $H_3(q)$ " +
        "under the canonical Markov convention.** The clause previously read " +
        "*\"the Frobenius pairing is non-degenerate (QUO-1), so for every " +
        "nonzero demand profile a unique minimal-norm supply satisfies it\"*, " +
        "with no convention note anywhere in the block. That is false under " +
        "convention D, and the corpus decides it outright: " +
        "`QOU.Interactions.GramMatrixH3Symbolic.gramMatrixD_det_eq_zero` " +
        "proves $\\det G = 0$ for **every real $q$**, sorry-free — not merely " +
        "at the substrate anchor — alongside `gramMatrixD_not_posDef` and " +
        "`gramMatrixD_mulVec_radical`. Convention D is in fact a *root* of the " +
        "$H_3$ Gram determinant as a polynomial in $z$, so the degeneracy is " +
        "identical in $q$ rather than accidental.\n\n" +
        "Two consequences the old wording hid. A minimal-norm supply is unique " +
        "only **modulo the radical**, since generalized inverses of a singular " +
        "Gram differ precisely by radical terms. And existence fails outright " +
        "for a demand profile with nonzero radical component — " +
        "`pyhecke.lp_dual_solver.gram_pseudo_inverse_solve` raises rather than " +
        "returning a vector, on the stated ground that answering a question " +
        "the inputs cannot support is the failure mode that arc keeps finding. " +
        "That case is not hypothetical: the sign-representation observable has " +
        "$|\\cos|$ to the radical measured at exactly $1.0$ — it **is** the " +
        "radical, and is not dualisable at all.\n\n" +
        "The surviving construction is the quotient $H_3(q)/\\mathrm{rad}$, " +
        "which is what `pyhecke.gram.G_PINV` computes (Moore-Penrose, chosen " +
        "deliberately over a 5-dimensional coordinate restriction) and what " +
        "`gram_quotient_inverse()` returns; `gram_inverse()` deliberately " +
        "raises and `G_INV` is left undefined rather than rebound. Related " +
        "hazard, not fixed here: the companion Lean carrier " +
        "`KnotOperatorLPSelection` assumes `frob_nondegenerate`, which is the " +
        "same false hypothesis, and has no instance anywhere in the tree.",
    },
  ],
  tags: [
    "knot-operator",
    "pair-production",
    "frobenius-dual",
    "operator-selection",
    "hecke-algebra",
    "categorical-action",
    "rigid-duality",
    "multi-channel",
  ],
});
