import { remark } from "../../schema/builders";

export default remark({
  label: "rem:neutron-horizontal-blindness",
  title: "The neutron is blind to horizontal photon polarisation in the pair-creation channel",
  interprets: "prop:four-term-pair-nucleon",
  uses: [
    "prop:four-term-pair-nucleon",
    "def:categorical-neutron",
    "def:categorical-proton",
    "rem:photon-nucleon-hecke-action",
  ],
  tags: [
    "neutron", "proton", "flavor-asymmetry", "pair-creation",
    "polarisation", "testable", "photon-nucleon",
  ],
});
