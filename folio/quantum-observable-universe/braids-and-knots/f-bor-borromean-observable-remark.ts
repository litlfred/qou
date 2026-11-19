import { remark } from "../../schema/builders";

export default remark({
  label: "rem:f-bor-borromean-observable-remark",
  title: "The Borromean observable as a normalised Markov trace",
  interprets: "def:f-bor-borromean-observable",
  tags: ["borromean", "markov-trace"],
  uses: [
    "def:f-bor-borromean-observable",
    "prop:y-lambda-closed-form-wenzl-bridge",
    "prop:borromean-markov-trace-closed-form",
  ],
});
