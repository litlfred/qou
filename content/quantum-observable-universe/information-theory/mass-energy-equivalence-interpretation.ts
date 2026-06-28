import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:mass-energy-equivalence",
  label: "rem:mass-energy-equivalence-interpretation",
  title:
    "Regime behaviour, the electron consistency check, and pair creation",
  uses: [
    "thm:mass-energy-equivalence",
    "rem:pair-creation-energy",
    "ex:mass-identity-C",
  ],
  cites: ["yekutieli2015"],
});
