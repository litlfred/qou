import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-tower-open-problems-classes",
  title:
    "The four remaining mass-tower open problems, carried as hypotheses",
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
  uses: ["prop:em-coupling-bring-zero-mode"],
  cites: ["borel1974", "bloch2000", "suslin1991", "kashaev1997"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the four hypotheses are the classes `Term7ShellCorrectionClass`, `ChiralityFactorClass`, `ZHabiroConvergenceClass` and `AlphaOver4PiClass`.",
    },
  ],
});
