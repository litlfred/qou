import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-precision-ladder-equivalence",
  title:
    "Precision-ladder coefficients are Habiro integer evaluations",
  lean: {
    ref: "qou:QOU.BraidKnot.HabiroPrecisionLadderEquivalence",
  },
  uses: [
    "thm:jones-markov-trace",
    "prop:q-schur-y-lambda-closed-form",
    "prop:mass-endomorphism-tower",
  ],
  cites: [
    "habiro2000",
    "jones1987",
    "wenzl1988",
  ],
  tags: [
    "habiro-ring",
    "precision-ladder",
    "cyclotomic-integrality",
    "1ppQ",
    "categorical-derivation",
  ],
});
