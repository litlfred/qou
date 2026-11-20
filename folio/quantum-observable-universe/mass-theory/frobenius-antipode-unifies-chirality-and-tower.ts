import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:frobenius-antipode-unifies-chirality-and-tower",
  title:
    "Frobenius antipode $S\\colon \\sigma \\leftrightarrow \\sigma^{-1}$ unifies chirality (Term 5) and neutron-tower closure",
  lean: {
    ref: "qou:QOU.BraidKnot.frobenius_antipode_unifies",
    validation: "not_checked",
  },
  uses: [
    "prop:chirality-dual-space-derivation",
    "conj:six-term-mass-formula-complete",
  ],
  cites: ["kassel1995"],
  tags: [
    "frobenius",
    "antipode",
    "chirality",
    "neutron-tower",
    "alpha-blend",
    "catalan",
    "unification",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
  ],
});
