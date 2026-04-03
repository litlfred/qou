import { example } from "../../schema/builders";

export default example({
  interprets: "def:molecular-hopf-chain",
  label: "ex:carbon-chain-c6",
  title: "Linear $\\mathrm{C}_6$ Hopf chain",
  tags: [
    "carbon",
    "c6",
    "linear-chain",
    "carbyne",
    "cumulene",
    "spring",
    "open-chain",
  ],
  uses: [
    "rem:carbon-valence",
    "rem:chain-spring-modes",
  ],
});
