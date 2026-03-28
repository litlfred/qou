import { definition } from "../../schema/builders";

export default definition({
  label: "def:beta-decay-skein",
  title:
    "Beta decay as a Skein crossing change on the Gröbner normal form",
  tags: [
    "beta-decay",
    "skein-relation",
    "groebner-basis",
    "hecke-algebra",
    "weak-force",
    "crossing-change",
    "lepton",
    "normal-form",
  ],
  lean: {
    decl: "QOU.Descartes.BetaDecaySkein",
    validation: "not_checked",
  },
  uses: [
    "def:stable-nucleus",
    "def:categorical-proton",
    "def:categorical-neutron",
    "def:electron-knot",
    "def:positron-knot",
    "def:neutrino-knot",
    "prop:nuclear-groebner-reduction",
    "def:braid-group",
    "prop:local-substrate-q",
  ],
});
