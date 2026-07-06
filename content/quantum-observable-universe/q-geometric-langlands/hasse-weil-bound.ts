import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "thm:hasse-weil-bound",
  title: "Hasse--Weil bound for the fundamental eigenvalues",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.hasse_weil_bound",
    validation: "not_checked",
  },
  uses: ["def:local-q-zeta-function"],
  tags: [
    "hasse-weil",
    "eigenvalue-bound",
    "frobenius",
    "castelnuovo-severi",
    "riemann-hypothesis-finite-field",
  ],
  cites: ["weil1948", "rosen2002", "milne2013"],
});
