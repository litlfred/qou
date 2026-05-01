import { prose } from "../../schema/builders";

export default prose({
  label: "tm-inductive-construction",
  title: "Inductive construction ($A \\to A+1$)",
  uses: [
    "def:transfer-matrix-operator",
    "prop:shell-closure-normal-form",
    "prop:shell-closure-stability",
    "rem:generator-volume-decomposition",
  ],
  tags: [
    "transfer-matrix",
    "inductive",
    "shell-closure",
    "shell-folding",
    "complexity",
    "magic-numbers",
    "groebner",
    "appendix",
  ],
});
