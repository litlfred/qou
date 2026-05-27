import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:proton-brane-tower-correction",
  title: "Proton brane-tower correction d₄=46, d₅=4, d₆=-29",
  lean: { ref: "qou:QOU.BraidKnot.ProtonBraneTowerCorrection" },
  uses: [
    "prop:mass-endomorphism-tower",
    "prop:borromean-markov-trace-closed-form",
    "prop:habiro-precision-ladder-equivalence",
    "def:atomic-braid",
  ],
  cites: ["jones1987", "habiro2000", "wenzl1988"],
  tags: [
    "brane-tower",
    "proton-mass",
    "1ppQ",
    "correction-tower",
    "categorical-derivation",
  ],
});
