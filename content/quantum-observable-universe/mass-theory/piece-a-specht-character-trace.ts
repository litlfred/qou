import { lemma } from "../../schema/builders";

/**
 * The central element C₂ = Σ_i L_i² (sum of squared Jucys–Murphy elements)
 * traced on a Specht module and on the regular representation.
 *
 * This is the representation-theoretic half of the Piece A arc: it produces
 * the content-square sum Σ_□ c(□)² as a SPECTRUM rather than a combinatorial
 * sum, which is what lets the Plancherel average of that quantity (Piece B)
 * be read off the identity coefficient of ℂ[S_n].
 */
export default lemma({
  label: "lem:piece-a-specht-character-trace",
  title:
    "Trace of the central element $C_2 = \\sum_i L_i^2$ on $S^\\mu$ and on the regular representation",
  lean: {
    ref: "qou:QOU.BraidKnot.PieceA.trace_centralC2_specht_module",
    validation: "not_checked",
  },
  uses: ["prop:jucys-murphy-central-elements-qou"],
  cites: ["macdonald1995", "jucys1974", "murphy1992"],
  tags: [
    "piece-a",
    "jucys-murphy",
    "central-element",
    "specht-module",
    "regular-representation",
    "artin-wedderburn",
    "cell-content",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "**\u00a77c base-ring adjudication: the field is essential.** " +
        "`wall-base-ring-minimal` flags `[Field k] [CharZero k]` in " +
        "`PieceASpechtCharacter.lean` as possibly restatable over " +
        "\u2124[q,q\u207b\u00b9]. It is not: the statement is about " +
        "`LinearMap.trace` and `Module.finrank` of a submodule, both of " +
        "which need a field to have the meaning used here, and `CharZero` " +
        "is what keeps `dim S^\u03bc` from collapsing in the regular-" +
        "representation decomposition. The advisory is adjudicated, not " +
        "outstanding.",
    },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "**This route supplies the content side, not the whole of Piece A.** " +
        "Both traces here are sorry-free in " +
        "`lean/QOU/BraidKnot/PieceASpechtCharacter.lean`. The file's third " +
        "declaration, `pieceA_hook_sq_eq_content_sq_add_n_sq`, states Piece A " +
        "itself — but its Lean proof **delegates** to the combinatorial " +
        "theorem `IdentityI.sumSqHooks_eq_sumSqContents_add_sq`. So the " +
        "hook side is not obtained representation-theoretically anywhere in " +
        "the corpus; closing that gap would need the class-function " +
        "evaluation on transposition cycle type, which is not written.",
    },
  ],
});
