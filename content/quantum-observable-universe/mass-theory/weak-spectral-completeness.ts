import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:weak-spectral-completeness",
  lean: { ref: "qou:QOU.BraidKnot.WeakSpectralCompleteness" },
  title:
    "Plancherel completeness for the EW/Higgs $\\{T(2,4), T(2,6), T(2,8)\\}$ idempotent decomposition",
  uses: ["thm:em-spectral-completeness"],
  tags: [
    "tier:S",
    "electroweak",
    "spectral-completeness",
    "plancherel",
    "weak-coupling",
    "force-carrier",
    "nv-1",
    "open-problem",
  ],
});
