import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:brane-tower-z-habiro",
  lean: { ref: "qou:QOU.BraidKnot.BraneTowerZHabiro" },
  title: "Brane tower lives in the $z$-Habiro ring",
  uses: [
    "def:z-habiro-ring",
    "def:habiro-ring",
    "cor:quantum-dilogarithm",
  ],
  tags: [
    "brane-tower",
    "habiro-ring",
    "cyclotomic-completion",
    "regularization",
    "quantum-dilogarithm",
    "open-problem",
    "partial-refutation-six-families",
    "closure-2026-05-11",
    "phase-3-leverage-15-users",
    "algebraic-cauchy-limit-half-open",
  ],
});
