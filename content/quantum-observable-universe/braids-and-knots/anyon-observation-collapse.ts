import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hecke-anyonic-substrate",
  label: "rem:anyon-observation-collapse",
  title:
    "Anyon ladder: generic $q$ ↔ root-of-unity ↔ $q \\to 1$",
  uses: [
    "conj:hecke-anyonic-substrate",
    "conj:root-of-unity-mtc-truncation",
    "conj:kazhdan-lusztig-classical-limit",
    "def:observation",
  ],
  tags: [
    "anyon",
    "ladder",
    "modular-tensor-category",
    "classical-limit",
    "observation-frame",
    "synthesis",
  ],
});
