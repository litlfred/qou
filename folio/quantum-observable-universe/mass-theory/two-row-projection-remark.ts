import { remark } from "../../schema/builders";

export default remark({
  label: "rem:two-row-projection-remark",
  title: "Idempotence and the two-row splitting of the Markov trace",
  interprets: "def:two-row-projection",
  uses: [
    "def:two-row-projection",
    "def:two-row-stratum",
    "prop:wedderburn-weight-canonical",
  ],
});
