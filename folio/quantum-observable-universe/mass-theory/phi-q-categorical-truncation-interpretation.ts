import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:phi-q-categorical-truncation",
  label: "rem:phi-q-categorical-truncation-interpretation",
  title: "Disambiguating the three depth invariants and the empirical truncation behaviour",
  uses: [
    "conj:phi-q-categorical-truncation",
    "cor:habiro-expansion-atomic",
    "conj:brane-tower-z-habiro",
    "prop:cell-depth-truncation",
  ],
});
