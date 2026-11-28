import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-three-forms",
  title: "Proposed braid, Laurent, and residue faces of $q$-Collatz, and what remains unconstructed",
  interprets: "conj:q-collatz",
  uses: [
    "conj:q-collatz",
    "conj:collatz-contact-boundary",
  ],
  tags: ["collatz", "hecke-algebra", "markov-trace", "dictionary"],
});
