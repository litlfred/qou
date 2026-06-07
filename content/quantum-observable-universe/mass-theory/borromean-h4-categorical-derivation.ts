import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borromean-h4-categorical-derivation",
  title:
    "Borromean $h^4 = -3/4$ derived as $(-3) \\cdot (1/4)$ via R-matrix + Markov normalisation",
  lean: { ref: "qou:QOU.BraidsAndKnots.BorromeanH4CategoricalDerivation" },
  uses: [
    "prop:borromean-markov-trace-closed-form",
  ],
  cites: [
    "jones1987",
  ],
  computation: {
    engine: "mpmath",
    script:
      "folio-assistant/computations/probes/gap_a4_T17_schur_weyl_rmatrix_probe.py",
    witness:
      "folio-assistant/computations/probes/gap-a4-T17-schur-weyl-rmatrix-probe.witness.json",
    consumers: [
      "folio-assistant/computations/probes/gap_a4_T18_markov_normalization_probe.py",
    ],
    status: "verified",
  },
  tags: [
    "borromean",
    "markov-trace",
    "schur-weyl",
    "r-matrix",
    "categorical-derivation",
    "h-expansion",
    "wenzl-weights",
  ],
});
