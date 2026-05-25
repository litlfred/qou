import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-residue-sum-equivalence",
  title:
    "Habiro completion ≡ Gröbner–Shirshov residue spectral sum (equivalence)",
  lean: {
    ref: "qou:QOU.BraidKnot.HabiroResidueSumEquivalence",
    validation: "not_checked",
  },
  uses: [
    "prop:full-pole-structure-mass-trace",
    "prop:gb-residue-spectral-sum",
    "def:habiro-ring",
  ],
  cites: ["habiro2004", "jones1987"],
  tags: [
    "habiro-ring",
    "cyclotomic-completion",
    "markov-trace",
    "residue",
    "spectral-sequence",
    "equivalence",
    "computational-witness",
  ],
});
