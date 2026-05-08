import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-tower-open-problems-classes",
  title:
    "§3b-cond Lean classes for the four remaining mass-tower open problems",
  interprets: "prop:em-coupling-bring-zero-mode",
  tags: [
    "mass-tower",
    "open-problems",
    "conditional-class",
    "term-7",
    "shell-correction",
    "chirality-factor",
    "z-habiro",
    "brane-tower",
    "alpha-em",
    "fine-structure-constant",
    "higher-bloch",
    "polylogarithm",
  ],
  uses: [
    "prop:em-coupling-bring-zero-mode",
    "prop:archimedean-functor-uniqueness",
    "conj:bring-hyperbolic-knot-bloch-decomposition",
  ],
  cites: ["borel1974", "bloch2000", "suslin1991", "kashaev1997"],
});
