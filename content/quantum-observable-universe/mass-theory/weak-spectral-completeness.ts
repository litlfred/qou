import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:weak-spectral-completeness",
  lean: { ref: "qou:QOU.BraidKnot.WeakSpectralCompleteness" },
  title:
    "Plancherel completeness for the EW/Higgs $\\{T(2,4), T(2,6), T(2,8)\\}$ idempotent decomposition",
  uses: ["thm:em-spectral-completeness"],
  tags: [
    "electroweak",
    "spectral-completeness",
    "plancherel",
    "weak-coupling",
    "force-carrier",
    "nv-1",
    "open-problem",
  ],
});
