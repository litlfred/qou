import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-value-transition",
  title:
    "$\\mathcal{Q}_q$-value: categorical action difference with $q$-anomaly",
  tags: [
    "q-value",
    "transition-energy",
    "beta-decay",
    "crossing-change",
    "recoil",
    "kinetic-energy",
    "skein",
  ],
  lean: {
    decl: "QOU.Descartes.QValueTransition",
    validation: "not_checked",
  },
  uses: [
    "def:q-energy",
    "def:q-momentum",
    "def:q-angular-momentum",
    "def:beta-decay-skein",
    "prop:hadron-half-life",
    "prop:local-substrate-q",
  ],
});
