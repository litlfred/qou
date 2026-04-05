import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-collatz",
  title:
    "The $q$-Collatz conjecture: Reeb-driven Hecke iteration over $\\mathbb{G}_m$",
  uses: [
    "def:categorical-reeb-derivation",
    "def:frobenius-hopf-substrate",
    "prop:skein-generation",
    "def:local-q-zeta-function",
    "thm:tannaka-krein-isomorphism",
    "conj:classical-riemann-hypothesis",
    "rem:substrate-gm-torsion",
    "rem:reeb-flow-bridge",
    "prop:reeb-operations-per-planck",
    "def:categorical-q-reeb-flow",
    "prop:root-of-unity-truncation",
    "def:skein-resolution-obstruction",
    "def:operational-entropy",
    "prop:p-bandwidth-bound",
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
