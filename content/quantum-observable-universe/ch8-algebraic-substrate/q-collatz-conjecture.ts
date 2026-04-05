import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-collatz",
  title:
    "The $q$-Collatz conjecture: Reeb-driven Hecke iteration over $\\mathbb{G}_m$",
  uses: [
    "def:categorical-reeb-derivation",
    "def:frobenius-hopf-substrate",
    "prop:skein-generation",
    "rem:substrate-gm-torsion",
    "def:categorical-q-reeb-flow",
    "prop:reeb-operations-per-planck",
    "def:classical-limit-obstruction",
    "thm:qou-obstruction-reduction",
  ],
  tags: [
    "collatz",
    "hecke-algebra",
    "number-theory",
    "q-deformation",
    "skein-relation",
    "dynamical-system",
    "categorical",
    "reeb-flow",
    "gm-torsion",
    "obstruction",
  ],
  cites: ["collatz1937", "lagarias2010"],
});
