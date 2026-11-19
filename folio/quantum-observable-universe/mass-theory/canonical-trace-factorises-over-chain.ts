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
    {
      kind: "note",
      body: "Computational provenance: the_canonical_mass_trace_factorises_over_the_chain_probe.py, the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe.py, nf_vs_canonical_word_order_probe.py.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/brng-dominant-summand-ursell.witness.json",
      "computations/probes/convention_d_proton_constituent_closed_form_probe.witness.json",
    ],
    status: "verified",
  },
});
