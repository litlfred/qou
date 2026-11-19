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
    {
      kind: "note",
      body: "Computational provenance: the_pn_bond_is_an_average_and_cannot_be_extremal_probe.py.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/probes/the_pn_bond_is_an_average_and_cannot_be_extremal_probe.py",
    witness: [
      "computations/probes/the_pn_bond_is_an_average_and_cannot_be_extremal_probe.witness.json",
      "computations/binding-per-bond-decomposition.witness.json",
    ],
    status: "verified",
  },
});
