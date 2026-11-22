import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borromean-h4-categorical-derivation",
  title:
    "Borromean $h^4 = -3/4$ derived as $(-3) \\cdot (1/4)$ via R-matrix + Markov normalisation",
  lean: { ref: "qou:QOU.BraidsAndKnots.borromean_h4_numeric_factorisation" },
  uses: [
    "prop:borromean-markov-trace-closed-form",
    "prop:h3-markov-wenzl-weights",
    "prop:habiro-residue-sum-equivalence",
  ],
  cites: [
    "jones1987",
  ],
  computation: {
    engine: "mpmath",
    script:
      "computations/probes/gap_a4_T15_character_polynomial_probe.py",
    witness:
      "computations/probes/gap-a4-T15-character-polynomial-probe.witness.json",
    consumers: [
      "computations/probes/gap_a4_T18_markov_normalization_probe.py",
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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the companion Lean states the rational factorisation $(-3)\\cdot(1/4) = -3/4$ over $\\mathbb{R}$" },
  ],
});
