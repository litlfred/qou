import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-energy",
  label: "rem:mass-energy-equivalence-interpretation",
  title:
    "Regime behaviour, the electron, and pair creation",
  uses: [
    "def:mass-energy",
    "cor:mass-identity-C",
    "rem:mass-energy-electron-check",
    "rem:mass-energy-pair-creation",
  ],
  foreshadows: [
    "rem:mass-energy-electron-check",
    "rem:mass-energy-pair-creation",
  ],
  cites: ["yekutieli2015"],
});
