import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-parity-to-divisor",
  title: "Parity at $q = -1$, odd-step outputs, and real-$q$ polynomial margins",
  interprets: "conj:q-collatz",
  uses: [
    "conj:q-collatz",
    "conj:collatz-contact-boundary",
    "quantum-observable-universe:def:two-q-adic-valuation",
    "quantum-observable-universe:prop:q-syracuse-lift",
  ],
  tags: ["collatz", "kummer", "contact-order"],
});
