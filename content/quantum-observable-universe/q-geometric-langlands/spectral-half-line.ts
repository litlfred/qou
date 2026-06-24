import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:spectral-half-line",
  proofs: ["prf:spectral-half-line"],
  title: "All fundamental Reeb modes lie on the critical line",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.spectral_half_line",
    validation: "not_checked",
  },
  uses: ["thm:hasse-weil-bound", "def:categorical-reeb-derivation"],
  tags: ["critical-line", "spectral", "half-line", "reeb-spectrum"],
});
