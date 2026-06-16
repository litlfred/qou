import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-c-k-closed-forms",
  lean: {
    ref: "qou:QOU.BraidKnot.QBetaCKClosedForms",
    validation: "not_checked",
  },
  title:
    "Closed-form conjectures for $c_4, c_5, c_6, c_7$ in the $\\mathfrak{Q}_\\beta$ precision ladder: empirical pattern-matches to sub-percent residual; first-principles derivation open (Khovanov-Rozansky at finite $q$ or KLR canonical-basis trace)",
  uses: ["rem:per-block-hopf-jones-absorption-pattern"],
  cites: [
    "khovanov2000",
    "khovanov-rozansky-2008",
    "khovanov-lauda-2009",
    "wenzl1988",
    "hoefsmit1974",
    "jones1985",
  ],
  tags: [
    "lean-infrastructure",
    "open-rd",
    "precision-ladder",
    "empirical-conjecture",
    "khovanov-rozansky",
    "klr-canonical-basis",
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta/qbeta_decay_sdp_full_ck.py",
    witness: [
      "computations/qbeta/qbeta-decay-sdp-full-ck-derivation.witness.json",
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "Per CLAUDE.md §3b-cond conditional-class exception, the existing\n[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)\nLean class `QBetaPrecisionLadderCoefficients` (which axiomatises\nthe c_k values as class fields) is the correct integration point.\nDownstream provable claims taking\n`[QBetaPrecisionLadderCoefficients q]` as a hypothesis are\n**rigorous conditional results** modulo this conjecture.\n\nThe current canonical instance `qBetaPrecisionLadderCoeffsCanonical`\non main provides the empirical closed forms; this conjecture block\nstates the conditions under which those instance values are\n**proved** rather than **fit**.",
    },
  ],
});
