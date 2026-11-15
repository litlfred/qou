import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-09-05",
      body: "**⚠ Readout corrected 2026-09-05.** This line published $z \\cdot (M_i)_{11} + (M_i)_{21}$, which is the readout of the **deprecated** `fsh-guts/deprecated/computations/transfer_matrix_symbolic.py` (`V_hat_i = z * M_i[0,0] + M_i[1,0]`), not the live one. Measured against the Lean-proved single-crossing factor [$\\mathrm{tr}_2(\\sigma + d) = z + d$](#rem:canonical-trace-factorises-over-chain) on a one-crossing matrix, all three bonds:\n\n| bond | $z + d$ | published $z(M)_{11} + (M)_{21}$ | corrected $z(M)_{21} + (M)_{22}$ |\n|---|---:|---:|---:|\n| $pp$ | $0.612688037146$ | $1.128088744114$ | $0.612688037146$ |\n| $nn$ | $0.403627738351$ | $1.000000000000$ | $0.403627738351$ |\n| $pn$ | $0.508229789377$ | $1.064088425325$ | $0.508229789377$ |\n\nThe corrected readout reproduces $z + d$ exactly; the published one misses every bond and is not even monotone in $d$. The factorisation statement itself is unaffected — what was wrong was the recipe for reading $(a_i, b_i)$ off $M_i$, i.e. $a_i = (M_i)_{21}$ and $b_i = (M_i)_{22}$. The same wrong readout is recorded as a trap in `no_within_generator_noncommutativity_probe.py`, whose docstring reports the identical $1.128089$ at $q_0$ from an earlier encounter with it.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "thm:markov-trace-factorization",
  title:
    "Exact factorization of the nuclear Markov trace",
  tags: [
    "markov-trace",
    "factorization",
    "jones-polynomial",
    "link-invariant",
    "hecke-algebra",
    "chebyshev",
    "generator-volume",
    "nuclear",
  ],
  lean: { ref: "qou:QOU.Archimedean.markov_trace_factorization",
    validation: "not_checked",
  },
  uses: ["prop:generator-volume-decomposition"],
});
