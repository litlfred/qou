import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:mass-energy-equivalence",
  label: "rem:information-causality",
  title: "Information causality and the light cone",
  tags: [
    "information-causality",
    "speed-of-light",
    "causal-structure",
    "lieb-robinson",
    "margolus-levitin",
    "bekenstein-bound",
  ],
  uses: ["thm:mass-energy-equivalence"],
  cites: [
    "margolus1998",
    "lloyd2000",
    "jacobson1995",
    "bekenstein1981",
    "pawlowski2009",
  ],
});
