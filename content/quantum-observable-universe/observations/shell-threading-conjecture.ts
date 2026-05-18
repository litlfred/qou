import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:shell-threading-energy",
  title:
    "Shell energy from the Skein smoothing at the beta-decay vertex",
  lean: {
    ref: "qou:QOU.ShellThreadingEnergy.ShellThreadingEnergy",
    validation: "not_checked",
  },
  tags: [
    "shell-correction",
    "threading-link",
    "skein-resolution",
    "beta-decay",
    "half-life",
    "lambda-shell",
    "molecular-hopf-ring",
  ],
  uses: [
    "def:molecular-hopf-ring",
    "ex:half-life-shell-worked",
  ],
});
