import { remark } from "../../schema/builders";

/**
 * The pn interface letter is by definition the convex combination of the pp
 * and nn letters, and the two-strand trace is affine in the offset, so
 * L_pp < L_pn < L_nn is forced for every q and every delta in (0,2). At A=2,
 * where no ordering or arrangement convention is in play, that ranks the
 * unbound dineutron above the bound deuteron. Proved in
 * `lean/QOU/Mass/ChainTraceFactor.lean` (`L_strict_mono`, sorry-free);
 * measured in `the_pn_bond_is_an_average_and_cannot_be_extremal_probe.py`.
 *
 * The no-spin caveat is stated in the block itself, before the conclusion:
 * the bound/unbound split at A=2 is a 3S1-vs-1S0 effect and a spinless bond
 * constant cannot be expected to reproduce it. The ORDER is the finding.
 */
export default remark({
  interprets: "thm:markov-trace-factorization",
  label: "rem:pn-bond-cannot-be-extremal",
  title:
    "The $pn$ bond constant is a convex combination of the $pp$ and $nn$ constants, so it can never be extremal",
  lean: {
    ref: "qou:QOU.Mass.ChainTraceFactor.L_strict_mono",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: [
    "thm:markov-trace-factorization",
    "rem:canonical-trace-factorises-over-chain",
  ],
  tags: [
    "mass-theory",
    "markov-trace",
    "binding-energy",
    "bond-constants",
    "open-problem",
    "lean-formalised",
    "draft",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): in\n[the free-energy reading](#rem:bond-log-ratio-is-a-free-energy)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## What is formalised\n\n`QOU.Mass.ChainTraceFactor`: the convex-combination identity\n, the strict betweenness of the offsets\nfor $0 < \\delta < 2$, its transport through the affine\ntrace, and the ordering $L_{pp} < L_{pn} < L_{nn}$\nitself. Not formalised, because it is empirical input: that\nonly $pn$ binds. The measurement, the $\\delta$ bound and the Wigner reading are\n`the_pn_bond_is_an_average_and_cannot_be_extremal_probe.py`." },
  ],
});
