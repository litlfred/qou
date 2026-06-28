import { remark } from "../../schema/builders";

export default remark({
  label: "rem:beta-decay-skein-properties",
  interprets: "def:beta-decay-skein",
  title:
    "Weak vertex, $10$-crossing budget, and $Q$-value of the $\\beta$-decay Skein operation",
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
  uses: [
    "def:beta-decay-skein",
    "def:stable-nucleus",
    "prop:nuclear-groebner-reduction",
    "def:categorical-proton",
    "def:categorical-neutron",
    "rem:force-knot-identification",
    "def:Q-value-transition",
  ],
});
