import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:grobner-shirshov-basis-exists",
  title: "Presentation of the distribution algebra",
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body: "Rewritten to the source, arXiv:math/0602138 Prop. 2.4 and Thm. 1.9. The earlier statement (the $q$-Serre relations form a Gröbner–Shirshov system, \"Proposition 3.8 and Theorem 3.15\") is not in the paper. No Lean declaration: the former `Fred2005.grobner_shirshov_basis_exists` proved existence with the identity reduction, which carries no content, and is removed.",
    },
  ],
  tags: ["groebner-shirshov", "presentation", "pbw"],
  uses: [
    "def:non-commutative-formal-group",
    "def:grobner-shirshov-basis",
    "def:skewed-poisson-structure",
  ],
  cites: ["leitner2006"],
});
