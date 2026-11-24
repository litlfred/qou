import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation refutation & repair record (`qou-x60n`, `qou-lsib`): `docs/audits/artifacts/2026-08-28-eigenvalue-norm-sq-axiom-refutation.lean` derives `False` from the former `eigenvalue_norm_sq_axiom` at `eigenvalues = 0`, which was repaired by adding `eigenvalues_ne_zero` and proving the norm-squared equality.",
      see: "docs/audits/artifacts/2026-08-28-eigenvalue-norm-sq-axiom-refutation.lean",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "caveat", date: "2026-08-29", body: "The two Weil inputs are carried as the hypothesis class `IsWeilZeta` (AGENTS.md §3b-cond), not as global axioms. Asserted universally over `LocalQZetaFunction` they proved `False` --- the structure records the shape of a zeta function, not that the shape comes from a curve --- so `hasse_weil_bound` is a conditional theorem, sorry-free and `#print axioms`-clean. `weilZetaExample` witnesses that the class is inhabited. Bean `qou-hwax`." },
  ],
  label: "thm:hasse-weil-bound",
  title: "Hasse--Weil bound for the fundamental eigenvalues",
  lean: { ref: "qou:QOU.Core.AlgebraicSubstrate.hasse_weil_bound",
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
