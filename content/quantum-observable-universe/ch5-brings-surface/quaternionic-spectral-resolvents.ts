import { definition } from "../../schema/builders";

export default definition({
  label: "def:quaternionic-spectral-resolvents",
  title: "Quaternionic spectral resolvents",
  tags: ["brings-surface", "quaternion"],
  uses: [
    "def:brings-surface",
    "rem:jet-shell",
  ],
});
