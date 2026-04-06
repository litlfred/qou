import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:horizon-conformal-invariance",
  title: "Conformal invariance at the jet horizon",
  tags: [
    "jet-horizon", "conformal-invariance", "aeon",
    "observability", "degree-zero",
  ],
  lean: {
    decl: "QOU.horizon_conformal_invariance",
    validation: "not_checked",
  },
  uses: [
    "def:jet-horizon",
    "def:aeon",
    "def:observation",
    "def:big-bang-state",
  ],
  cites: ["penrose2010"],
});
