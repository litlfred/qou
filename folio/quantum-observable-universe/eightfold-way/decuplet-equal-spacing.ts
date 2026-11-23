import { remark } from "../../schema/builders";

/**
 * The decuplet equal-spacing rule and the Omega-minus prediction.
 *
 * The companion to rem:meson-mass-splitting, for the other multiplet
 * and the other historically decisive relation. Gell-Mann's 1962
 * prediction of the Omega-minus used equal spacing within the baryon
 * decuplet; the particle was found in 1964 within 0.6% of the value.
 *
 * ANTI-FITTING: this block records a NEGATIVE result. Equal spacing
 * is an identity of the first-order octet-breaking ansatz — it holds
 * for every choice of the breaking parameters — so reproducing it is
 * not evidence for any mechanism, QOU's included. The structure is
 * exactly parallel to the Gell-Mann-Okubo null result, and it is
 * established here for the same reason: to remove a target that would
 * otherwise have looked like a success.
 *
 * The testable content is relocated to the ~9.2% deviation, for which
 * the framework currently derives no second-order term and therefore
 * predicts zero. Nothing is wired; no number is fitted.
 *
 * Created 2026-08-14 (bean qou-7lio) after the SM/eightfold cheat
 * sheet found the equal-spacing question unasked in the corpus.
 */
export default remark({
  label: "rem:decuplet-equal-spacing",
  title: "The decuplet equal-spacing rule has no discriminating power",
  interprets: "prop:borromean-decuplet",
  // The ref names a DECLARATION, not the module, following the pattern
  // of rem:meson-mass-splitting. `equal_spacing_cannot_discriminate` is
  // the negative result: two different breaking parameter sets (a,b,c)
  // and (a',b',c') give the same (vanishing) second difference, so the
  // rule cannot select between mechanisms.
  lean: {
    ref: "qou:QOU.Eightfold.DecupletEqualSpacing.equal_spacing_cannot_discriminate",
  },
  uses: [
    "prop:borromean-decuplet",
    "rem:meson-mass-splitting",
  ],
  cites: ["gellmann1962"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is a\ntheorem, machine-checked in\n`QOU/Eightfold/DecupletEqualSpacing.lean`: the three\n\n(`octet_casimir_not_function_of_hypercharge`, derived from the octet weight\ndata rather than asserted)" },
  ],
});
