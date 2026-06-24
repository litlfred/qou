import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borromean-markov-trace-closed-form",
  proofs: ["prf:borromean-markov-trace-closed-form"],
  title:
    "Borromean Markov trace $\\mathrm{tr}_M(\\beta_{\\mathrm{Bor}}) = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4)$",
  lean: { ref: "qou:QOU.BraidsAndKnots.borromean_markov_trace_closed_form" },
  uses: [
    "thm:jones-markov-trace",
    "def:frobenius-hopf-substrate",
    // broken-ref removed (Phase 7): prop:borromean-vol-8G
  ],
  cites: [
    "jones1987",
    "murasugi1996",
  ],
  computation: {
    engine: "mpmath",
    script:
      "computations/borromean_markov_trace_h_expansion_50dps.py",
    witness:
      "computations/borromean-markov-trace-h-expansion-50dps.witness.json",
    consumers: [
      "computations/mass_formula_6term_mpfr_50dps.py",
    ],
    status: "verified",
  },
  tags: [
    "borromean",
    "markov-trace",
    "jones-polynomial",
    "closed-form",
    "h-expansion",
    "topological-invariant",
    "linking-weight",
  ],
});
