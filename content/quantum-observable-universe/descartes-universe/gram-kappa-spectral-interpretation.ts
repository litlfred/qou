import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gram-kappa-spectral-interpretation",
  title:
    "Plancherel form of $\\kappa$ replaces the 2-jet hand calculation",
  interprets: "prop:gram-determinant-plancherel-ratio",
  uses: ["prop:gram-determinant-plancherel-ratio"],
  tags: [
    "interpretation",
    "kappa",
    "plancherel",
    "numerical-evaluation",
    "no-hand-calculation",
  ],
});
