import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:horizon-conformal-invariance",
  proofs: ["prf:horizon-conformal-invariance"],
  title: "Conformal invariance at the jet horizon",
  tags: [
    "jet-horizon", "conformal-invariance", "aeon",
    "observability", "degree-zero",
  ],
  lean: { ref: "qou:QOU.horizon_conformal_invariance",
    validation: "not_checked",
  },
  uses: [
    "def:aeon",
    "def:observation",
  ],
  cites: ["penrose2010"],
});
