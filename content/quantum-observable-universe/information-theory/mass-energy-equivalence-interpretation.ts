import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:mass-energy-equivalence",
  label: "rem:mass-energy-equivalence-interpretation",
  title:
    "Regime behaviour, the electron consistency check, and pair creation",
  uses: [
    "thm:mass-energy-equivalence",
    "cor:mass-identity-C",
    "rem:mass-energy-electron-check",
    "rem:mass-energy-pair-creation",
  ],
  cites: ["yekutieli2015"],
});
