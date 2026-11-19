import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:collatz-contact-boundary",
  label: "rem:collatz-contact-boundary-remark",
  title: "Contact with {[2]}$ and the two sides of the Collatz boundary",
  uses: ["def:collatz-contact-boundary", "conj:q-collatz"],
});
