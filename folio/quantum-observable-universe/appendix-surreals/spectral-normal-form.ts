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
    {
      kind: "note",
      body:
        "Lean formalisation prerequisites: specialising rational/polynomial expressions in R_q at q = 1 + epsilon, Hahn-series substrate, and (for the transcendental case) Berarducci–Mantova exp/log on No.",
    },
  ],
});
