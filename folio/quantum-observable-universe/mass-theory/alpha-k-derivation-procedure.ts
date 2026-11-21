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
      body: "**$n=3$ invertibility proved (W8b, 2026-11-20, gap 1 of `qou-w8cg`).** The Lean took the character matrix's invertibility as a hypothesis. At $n = 3$ it is now proved: the $H_3(q)$ character matrix on $1, \\sigma_0, \\sigma_0\\sigma_1$ has determinant $-[2]_q[3]_q$, so the system has a unique solution whenever $[2]_q[3]_q \\neq 0$. General $n$ remains a hypothesis (semisimplicity plus Tits deformation, not formalised). Ground ring generalised from $\\mathbb{R}$ to a generic field.",
    },
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
  ],
});
