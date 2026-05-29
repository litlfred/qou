import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pontryagin-dual-coxeter-character",
  title:
    "Pontryagin duality on abelianised Coxeter character — character ↔ measure on dual group",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.PontryaginDualCoxeterCharacter",
    validation: "not_checked",
  },
  uses: [
    "def:hecke-normal-form",
    "def:bar-involution",
  ],
  cites: [
    "pontryagin1934",
    "hewitt-ross1979",
  ],
  tags: [
    "pontryagin",
    "duality-d20",
    "abelianised-coxeter",
    "character-measure",
    "low-priority",
    "non-abelian-restriction",
    "axiom-class",
    "open-problem",
    "non-scholarly-voice-exception",
  ],
});
