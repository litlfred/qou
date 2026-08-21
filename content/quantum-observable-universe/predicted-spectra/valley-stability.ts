import { simulator } from "../../schema/builders";

export default simulator({
  label: "sim:valley-stability",
  title:
    "Valley of stability: beta-stability curve vs integer lattice",
  html: "folio-assistant/simulators/valley_stability.html",
  tags: [
    "simulator",
    "valley-of-stability",
    "diophantine",
    "coulomb",
    "nuclear",
    "interactive",
  ],
  uses: ["rem:valley-table"],
  defaultView: {
    name: "default",
    title: "Default: valley of stability",
    params: {
      q: 1.1099785827513808,
      Z_max: 118,
    },
  },
});
