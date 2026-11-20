import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:alpha-k-derivation-procedure",
  title:
    "Linear-system procedure for Jones--Markov weights $y_\\lambda$ and stratum prefactors $\\alpha_k$ at $H_n(R, q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.alpha_k_derivation_procedure",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-tower-coefficient-stratification",
    "conj:spectral-sequence-h3-explicit",
  ],
  tags: [
    "alpha-k",
    "jones-markov",
    "mass-tower",
    "linear-system",
    "wedderburn",
    "procedure",
    "parameterised",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
  ],
});
