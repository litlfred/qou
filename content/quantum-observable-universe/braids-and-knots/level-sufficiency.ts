import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:level-sufficiency",
  title:
    "Level sufficiency: Markov trace computable in the coarsest confinement algebra",
  lean: {
    decl: "QOU.BraidKnot.LevelSufficiency",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "def:confinement-category",
    "def:confinement-level",
    "def:hecke-normal-form",
    "prop:confinement-sdp",
    "prop:confinement-topological",
    "prop:confinement-operator-selection",
  ],
  tags: [
    "confinement",
    "markov-trace",
    "filtration",
    "hecke-inclusion",
    "computational-minimality",
  ],
});
