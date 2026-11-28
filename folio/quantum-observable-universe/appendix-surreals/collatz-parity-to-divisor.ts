import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-parity-to-divisor",
  title:
    "From integer parity to the $[2]_q$-divisor",
  interprets: "conj:collatz-contact-boundary",
  uses: [
    "def:two-q-adic-valuation",
    "conj:q-collatz",
    "prop:root-of-unity-truncation",
  ],
  tags: [
    "collatz",
    "parity",
    "divisor",
    "kummer",
    "contact-order",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-28", body: "Corrected a false claim: an odd step's output need not be q-even (R(-1)=1+P'(-1); the fixed point -q^-2 is a counterexample). Dropped the 'empirical <v>' table row." },
  ],
});
