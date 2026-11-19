import { example } from "../../schema/builders";

export default example({
  label: "ex:two-row-stratum",
  title: "The two-row stratum at n = 12",
  interprets: "def:two-row-stratum",
  uses: [
    "def:two-row-stratum",
    "prop:he4-two-row-dominance",
  ],
});
