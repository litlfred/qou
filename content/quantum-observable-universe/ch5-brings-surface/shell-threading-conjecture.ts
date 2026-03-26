import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:shell-threading-energy",
  title:
    "Shell energy from the Skein smoothing at the beta-decay vertex",
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
    "prop:hadron-half-life",
    "conj:skein-shell-correction",
    "def:molecular-hopf-ring",
    "def:threading-link",
    "def:skein-binding-lagrangian",
    "def:stable-nucleus",
    "rem:skein-crossing-asymmetry",
    "ex:half-life-shell-worked",
  ],
});
