import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:magic-A-binding-formula",
  title:
    "Doubly-magic light-nucleus binding formula: $\\mathfrak{B}(^A_Z\\mathfrak{X}) = \\rho_F \\cdot \\mathfrak{m}_e \\cdot A \\cdot 8G$",
  chapter: "mass-theory",
  cites: ["jones1987", "wenzl1988"],
  uses: [
    "prop:binding-alpha-shift-extension",
    "prop:diagrammatic-double-magic-lr-fusion",
    "rem:strutinsky-from-graded-trace",
  ],
  defines: [],
  tags: [
    "binding",
    "magic-A",
    "doubly-magic",
    "shell-closure",
    "borromean-residue",
    "no-fitting",
    "regime-dispatch",
  ],
  lean: { ref: "qou:QOU.BraidKnot.magic_A_binding_formula" },
});
