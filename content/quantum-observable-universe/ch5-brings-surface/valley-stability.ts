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
  ],
  simulator: {
    type: "html",
    source: "valley_stability.html",
  },
});
