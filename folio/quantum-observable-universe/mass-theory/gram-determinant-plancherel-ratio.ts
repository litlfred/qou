import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gram-determinant-plancherel-ratio",
  title:
    "Gram-determinant ratio $\\kappa$ as a Plancherel-weighted character product",
  uses: ["def:cs-gram-determinant-ratio", "rem:gram-matrix-spectral-connection"],
  lean: {
    ref: "qou:QOU.Archimedean.GramDeterminantPlancherelRatio",
    validation: "leanok",
  },
  authorNotes: [
    {
      kind: "note",
      body: "Formalised over an arbitrary field K (§7c, zero R specialisation) via class GramDeterminantPlancherelRatio.",
    },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "Demoted from proposition to open conjecture (owner choice, 2026-11-15). " +
        "The product formula is not well defined as written (the two torus knots " +
        "live on 2 and 3 strands; the exponents are not integers), and the old " +
        "proof only asserted the conclusion. The definition of kappa moved to " +
        "def:cs-gram-determinant-ratio. The alpha_EM value 1.7216 is computed " +
        "from the Gram determinants directly and does not use this formula.",
    },
  ],
  tags: [
    "gram-matrix",
    "plancherel",
    "wedderburn",
    "character-ratio",
    "chern-simons",
    "kappa",
    "open-conjecture",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/all_nuclides_sdp_admissibility_mp.py",
    witness: "computations/all-nuclides-sdp-admissibility-mp.witness.json",
    status: "verified",
  },
});
