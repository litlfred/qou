import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:complex-chirality-rotation",
  title: "Chirality as continuous phase rotation in the pre-observable sector",
  uses: [
    "rem:complex-substrate-interpretation",
    "def:substrate-parameter",
    "rem:chirality-trefoil-electron-positron",
    "def:crossing-energy",
    "def:categorical-instanton",
  ],
  tags: ["complex-q", "chirality", "CPT", "phase", "conjecture"],
});
