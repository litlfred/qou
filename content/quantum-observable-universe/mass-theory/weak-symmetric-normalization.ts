import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:weak-symmetric-normalization",
  title:
    "Weak-sector symmetric-channel Plancherel normalization $\\mathcal{N}_{\\rm sym}(q)$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.weak_symmetric_normalization",
    validation: "not_checked",
  },
  uses: [
    "conj:weak-spectral-completeness",
    // broken-ref removed (Phase 7): conj:electroweak-higgs-torus-link-triplet
    "prop:gram-determinant-plancherel-ratio",
    "prop:knot-operator-lp-selection",
  ],
  tags: [
    "plancherel",
    "weak-coupling",
    "symmetric-channel",
    "wedderburn",
    "n-sym",
    "nv-1",
    "categorical-normalization",
  ],
  // computation removed: incomplete schema (had witness without engine/script/status).
});
