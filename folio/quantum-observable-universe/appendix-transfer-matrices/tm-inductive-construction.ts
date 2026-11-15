import { prose } from "../../schema/builders";

export default prose({
  label: "tm-inductive-construction",
  title: "Inductive construction ($A \\to A+1$)",
  uses: [
    "prop:shell-closure-stability",
    "prop:generator-volume-decomposition",
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
