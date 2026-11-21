import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:nuclear-knot-classification",
  title:
    "Nuclear knot classification: braid closure type determines binding scale",
  lean: { ref: "qou:QOU.BraidKnot.nuclear_knot_classification",
    validation: "not_checked",
  },
  uses: ["def:hecke-mass-element"],
  authorNotes: [
    {
      kind: "deprecated",
      date: "2026-11-21",
      body:
        "Rests on superseded premises; not to be reworked on its old basis. " +
        "(1) The pair deviations (pp/nn amphicheiral, epsilon = h^2; pn chiral, epsilon = -h) " +
        "read the pre-2026-11-15 single-crossing bond letters, which the gamma-gamma rule " +
        "now covers (`docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`). " +
        "(2) The Lean classifies by mass number (A = 3 figure-eight, A >= 4 Borromean), " +
        "a per-case dispatch; under the 2026-11-21 ruling words are selected by whole-word " +
        "U(1) neutrality plus reading-3 Frobenius selection " +
        "(`docs/coordination/owner-rulings.md`). The Lean theorem only unfolds that dispatch " +
        "and does not state the binding factor a(N) (sidecar review, PR #8106). " +
        "A redo needs a gamma-gamma-selected word per nucleus.",
    },
  ],
  tags: [
    "knot-classification",
    "hyperbolic",
    "figure-eight",
    "borromean",
    "binding-scale",
  ],
});
