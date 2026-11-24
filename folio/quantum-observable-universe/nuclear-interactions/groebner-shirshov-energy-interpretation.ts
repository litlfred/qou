import { remark } from "../../schema/builders";

export default remark({
  label: "rem:groebner-shirshov-energy-interpretation",
  title:
    "Role of Gröbner--Shirshov reduction: Markov-trace evaluation engine, flat coefficient shadow, and word-length norm",
  tags: [
    "groebner-shirshov",
    "hecke-algebra",
    "energy",
    "markov-trace",
    "normal-form",
  ],
  interprets: "thm:groebner-shirshov-energy",
  uses: [
    "thm:groebner-shirshov-energy",
    "def:categorical-hamiltonian",
  ],
});
