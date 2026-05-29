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
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/q_pinning_50_digit.py",
    witness: "folio-assistant/computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
