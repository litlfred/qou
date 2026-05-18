import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-collatz",
  title:
    "The $q$-Collatz conjecture: Skein-module crossing resolution",
  uses: [
    "rem:substrate-gm-torsion",
    "thm:qou-obstruction-reduction",
  ],
  tags: [
    "collatz",
    "skein-module",
    "hecke-algebra",
    "number-theory",
    "q-deformation",
    "crossing-resolution",
    "convexity",
    "jones-polynomial",
    "markov-trace",
  ],
  cites: ["collatz1937", "lagarias2010"],
});
