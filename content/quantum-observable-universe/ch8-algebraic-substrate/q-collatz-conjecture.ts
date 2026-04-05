import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-collatz",
  title:
    "The $q$-Collatz conjecture: Reeb-rotated Hecke iteration over $\\mathbb{G}_m$",
  lean: {
    decl: "QOU.Substrate.reeb_averaged_contraction",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-reeb-derivation",
    "def:frobenius-hopf-substrate",
    "def:categorical-q-reeb-flow",
    "prop:skein-generation",
    "prop:reeb-operations-per-planck",
    "rem:substrate-gm-torsion",
    "def:classical-limit-obstruction",
    "thm:qou-obstruction-reduction",
    "conj:p-vs-np-boundary",
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
    "horizon",
  ],
  cites: ["collatz1937", "lagarias2010"],
});
