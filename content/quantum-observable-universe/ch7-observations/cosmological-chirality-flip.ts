import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cosmological-chirality-flip",
  title: "Chirality reversal at cosmological extremes",
  interprets: "rem:cosmological-limits",
  uses: [
    "rem:cosmological-limits",
    "rem:time-reversal-energy-barrier",
    "rem:complex-substrate-interpretation",
    "def:exceptional-divisor",
    "def:substrate-parameter",
    "rem:heisenberg-commutator",
    "sec:cp-violation-evidence",
  ],
  tags: [
    "big-bang", "heat-death", "chirality", "cosmological",
    "observability", "frobenius-degeneration", "aeon",
  ],
});
