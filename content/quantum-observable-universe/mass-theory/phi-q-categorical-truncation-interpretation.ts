import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:phi-q-categorical-truncation",
  label: "rem:phi-q-categorical-truncation-interpretation",
  title: "Disambiguating the three depth invariants and the empirical truncation behaviour",
  uses: [
    "prop:phi-q-categorical-truncation",
    "cor:habiro-expansion-atomic",
    "conj:brane-tower-z-habiro",
  ],
});
