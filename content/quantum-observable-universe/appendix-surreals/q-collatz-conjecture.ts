import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:q-collatz",
  title:
    "The $q$-Collatz conjecture: Skein-module crossing resolution",
  lean: { ref: "qou:QOU.AppendixSurreals.QCollatz", validation: "stub" },
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
