import { remark } from "../../schema/builders";

/**
 * U-spin, V-spin, and the Coleman-Glashow relation.
 *
 * The THIRD member of the eightfold-way null-result family:
 *
 *   - rem:meson-mass-splitting     GMO is an identity        -> content-FREE
 *   - rem:decuplet-equal-spacing   equal spacing is an identity -> content-FREE
 *   - rem:u-spin-coleman-glashow   CG is an identity         -> content-FREE
 *   - rem:vector-meson-nonet       mixing is UNCONSTRAINED   -> content-BEARING
 *
 * ANTI-FITTING: nothing here is fitted and nothing is wired. PDG values
 * are comparators. This block records a NEGATIVE result — the relation
 * vanishes identically for all six first-order parameters, so
 * reproducing it is evidence for no mechanism.
 *
 * One genuine difference from the other two nulls, and it is stated
 * rather than smoothed over: CG rests on a CONJUNCTION of premises
 * (isospin exact in the strong sector AND the EM self-energy a U-spin
 * scalar), and dropping the second makes the combination non-zero. So
 * it does test those two premises — just nothing beyond them.
 *
 * Also closes half of the qou-7lio "no baryon octet block" gap: the
 * octet previously appeared only as a passing paragraph inside
 * borromean-decuplet-derivation, and this gives it real content.
 *
 * Created 2026-08-15 (bean qou-7lio). The U-spin question was flagged
 * in the SM/eightfold cheat sheet as "plausibly the same null-result
 * class, worth checking rather than assuming" — checked, and it is.
 */
export default remark({
  label: "rem:u-spin-coleman-glashow",
  title: "U-spin and the Coleman–Glashow relation: a third null result",
  interprets: "prop:borromean-decuplet",
  // The ref names a DECLARATION, following rem:meson-mass-splitting and
  // rem:decuplet-equal-spacing. `cg_cannot_discriminate` is the negative
  // result: two different six-parameter breaking patterns give the same
  // (vanishing) combination, so the relation selects no mechanism.
  lean: {
    ref: "qou:QOU.Eightfold.ColemanGlashowIdentity.cg_cannot_discriminate",
  },
  uses: [
    "prop:borromean-decuplet",
    "rem:meson-mass-splitting",
    "rem:decuplet-equal-spacing",
  ],
  cites: ["colemanglashow1961"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is\na theorem, machine-checked in\n`QOU/Eightfold/ColemanGlashowIdentity.lean`: the combination" },
  ],
});
