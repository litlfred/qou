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
  lean: { ref: "qou:QOU.Descartes.BetaDecaySkein",
    validation: "not_checked",
  },
  uses: ["def:positron-knot"],
});
