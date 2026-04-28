import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cosmological-chirality-flip",
  title: "Chirality reversal at cosmological extremes",
  interprets: "def:quantum-observable-universe",
  uses: [
    "ex:cosmological-limits",
    "rem:time-reversal-energy-barrier",
    "sec:cp-violation-evidence",
    "prop:u1-equivariant-reduction",
    "rem:symmetry-preserving-leptons",
  ],
  tags: [
    "big-bang", "heat-death", "chirality", "cosmological",
    "observability", "frobenius-degeneration", "aeon",
  ],
});
