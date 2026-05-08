import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:quantum-ideal-gas-law",
  label: "rem:quantum-ideal-gas-law-interpretation",
  title: "Noether invariant and comparison with classical $PV = NkT$",
  tags: [
    "ideal-gas",
    "noether",
    "ward-identity",
    "classical-comparison",
    "gibbs",
  ],
  uses: ["prop:quantum-ideal-gas-law"],
});
