import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-c-k-closed-forms",
  lean: {
    ref: "qou:QOU.BraidKnot.QBetaCKClosedForms",
    validation: "not_checked",
  },
  title:
    "Closed-form conjectures for $c_4, c_5, c_6, c_7$ in the $Q_\\beta$ precision ladder: empirical pattern-matches to sub-percent residual; first-principles derivation open (Khovanov-Rozansky at finite $q$ or KLR canonical-basis trace)",
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
    script: "folio-assistant/computations/qbeta/qbeta_decay_sdp_full_ck.py",
    witness: [
      "folio-assistant/computations/qbeta/qbeta-decay-sdp-full-ck-derivation.witness.json",
    ],
    status: "experimental",
  },
});
