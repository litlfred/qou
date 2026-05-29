import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hecke-anyonic-substrate",
  label: "rem:anyon-observation-collapse",
  title:
    "Anyon ladder: generic $q$ ↔ root-of-unity ↔ $q \\to 1$",
  uses: [
    "prop:root-of-unity-mtc-truncation",
    "prop:kazhdan-lusztig-classical-limit",
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
