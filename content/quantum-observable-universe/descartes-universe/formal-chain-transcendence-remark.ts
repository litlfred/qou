import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hyperbolic-volume-transcendence",
  label: "rem:formal-chain-transcendence",
  title:
    "The formal derivation chain does not depend on transcendence status",
  tags: [
    "ground-ring",
    "laurent-polynomial",
    "formal-chain",
    "symbolic-computation",
  ],
  uses: ["conj:hyperbolic-volume-transcendence"],
});
