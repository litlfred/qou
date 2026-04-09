import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:nuclear-groebner-reduction",
  label: "rem:nucleon-nf-observability",
  title:
    "Observability structure of the nucleon normal form",
  tags: [
    "normal-form",
    "observable",
    "virtual",
    "color-tube",
    "hecke-algebra",
    "nucleon",
    "neutron",
    "proton",
    "beta-decay",
    "sign-pattern",
    "computational-witness",
  ],
  uses: [
    "prop:nuclear-groebner-reduction",
    "def:categorical-neutron",
    "def:categorical-proton",
    "def:color-tube-fibers",
  ],
});
