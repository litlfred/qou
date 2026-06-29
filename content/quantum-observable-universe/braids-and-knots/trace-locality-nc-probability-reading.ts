import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:trace-locality-meets-gs-non-locality",
  label: "rem:trace-locality-nc-probability-reading",
  title:
    "Non-commutative probability reading of the locality/non-locality reconciliation",
  tags: [
    "locality",
    "markov-property",
    "non-commutative-probability",
    "grobner-shirshov",
  ],
  uses: [
    "prop:trace-locality-meets-gs-non-locality",
    "rem:non-commutative-probability-dictionary",
  ],
});
