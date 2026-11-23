import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:spectral-normal-form",
  title:
    "Spectral gap closure and singularity formation as $q \\to 1$ read from normal-form exponents",
  lean: { ref: "qou:QOU.AppendixSurreals.SpectralNormalForm", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "spectral-gap",
    "conway-normal-form",
    "leading-exponent",
    "singularity",
    "q-deformation",
    "open-problem",
  ],
  uses: [
    "rem:conway-normal-form",
    "conj:classical-limit-stpart",
  ],
  cites: [
    "conway1976",
    "berarducci-mantova2018",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Original wording: \"Rational-function arithmetic in Lean at $q = 1 + \\varepsilon$ (partial; via specialising `Polynomial (R_q)` at surreal values)\"; \"algebraic case mostly tractable with current Lean + surreal infrastructure. Transcendental case requires Berarducci–Mantova in Lean.\"" },
  ],
});
