import { remark } from "../../schema/builders";

/**
 * The algebraic consequence of the chain form: a connected-sum closure makes
 * every multiplicative invariant a product over the chain, and the Markov
 * trace of the full 3A-strand canonical word is the product of TWO-strand
 * traces of the per-generator Hecke polynomials (200-bit, ~1e-59 at A ≤ 4).
 * The interface factors are z + d, so the arc's three bond constants are
 * -log(z + d) — an identity, not a sixty-digit coincidence — and the canonical
 * closure carries no many-body binding by theorem. The affine law and the
 * factor algebra are in `lean/QOU/Mass/ChainTraceFactor.lean` (sorry-free);
 * the factorisation of the H_{3A} trace itself is checked, not formalised.
 */
export default remark({
  interprets: "prop:canonical-closure-torus-chain",
  label: "rem:canonical-trace-factorises-over-chain",
  title:
    "The canonical mass trace factorises over the chain: the bond constants are $-\\log(z+d)$ and the canonical closure carries no many-body binding",
  lean: {
    ref: "qou:QOU.Mass.ChainTraceFactor.twoStrandTrace_eq",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: [
    "prop:canonical-closure-torus-chain",
    "thm:markov-trace-factorization",
    "rem:ks-multiplicativity-via-markov",
  ],
  cites: ["birman1974", "lickorish1997"],
  tags: [
    "mass-theory",
    "markov-trace",
    "connected-sum",
    "binding-energy",
    "lean-formalised",
    "draft",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , recorded in\n[the free-energy reading](#rem:bond-log-ratio-is-a-free-energy)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): which the Lean\nformalisation of that result took as its *named structural input*\n\nThe corpus's live builder\n`atom_braid_word_3A` does assemble it that way\n\nidentified against its Lean closed form to\n\n`QOU.Mass.IntraOrderingInvariance` proves the split. Given the\n\nartefact. Not formalised, as ever, is the connected-sum multiplicativity itself.\nMeasured in\n`the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe.py`; which\nword is $\\beta_{\\mathrm{Bor}}$ is measured in\n`nf_vs_canonical_word_order_probe.py`.\n\n## What is formalised, what is checked, what is cited\n\n`QOU.Mass.ChainTraceFactor` proves the factor algebra: the\naffine law $\\mathrm{tr}_2(\\sigma + d) = z + d$ from the level-2 Wenzl weights\n; the mirror\n\nand not formalised. Nothing here says" },
  ],
});
