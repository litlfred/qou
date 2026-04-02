import { simulator } from "../../schema/builders";

export default simulator({
  label: "sim:valley-stability",
  title:
    "Valley of stability: beta-stability curve vs integer lattice",
  tags: [
    "simulator",
    "valley-of-stability",
    "diophantine",
    "coulomb",
    "nuclear",
    "interactive",
  ],
  uses: [
    "prop:integer-stability",
    "prop:beta-stability",
    "rem:diophantine-valley",
    "rem:valley-table",
    "def:coulomb-charge",
    "def:substrate-parameter",
    "prop:local-substrate-q",
  ],
  html: "folio-assistant/simulators/valley_stability.html",
  defaultView: {
    name: "default",
    title: "Default valley-of-stability view",
    params: {},
  },
});
