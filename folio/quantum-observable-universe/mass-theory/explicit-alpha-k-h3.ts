import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:explicit-alpha-k-h3",
  title: "Explicit $\\alpha_k$ at $H_3(R, q)$: closed-form structural prefactors",
  lean: { ref: "qou:QOU.BraidsAndKnots.explicit_alpha_k_h3",
    validation: "leanok",
  },
  uses: ["prop:spectral-sequence-h3-explicit"],
  tags: [
    "spectral-sequence",
    "alpha-k",
    "hecke-algebra",
    "markov-trace",
    "jones-markov",
    "h3",
    "structural-derivation",
    "q-algebraic",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body: "**Promoted to `proposition` (2026-11-27, PR #9670 and its follow-up).** The values were already derived (W8b). The open part was whether the representatives are the $E_\\infty$ classes, and it is settled by `prop:spectral-sequence-h3-explicit`. In the cocentre, $r_1 = \\sigma_1 - \\sigma_2$ is a sum of commutators, which is why $\\alpha_1 = 0$ for every trace. $r_3$ is not a new class, since $\\alpha_3 = h\\alpha_2 + \\mathrm{tr}\\,\\sigma_1$. The $E_\\infty$ classes are $1, \\sigma_1, \\sigma_1\\sigma_2$. The statement now names the representatives and the trace explicitly, and the boxed values are unchanged.",
    },
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Values derived; identification still open (W8b).** The Lean theorem was a vacuous existential (four `rfl`s). It now derives $\\alpha_0=1$, $\\alpha_1=0$, $\\alpha_2=z^2$, $\\alpha_3=hz^2+z$ as Markov traces of the representatives $1,\\ \\sigma_1-\\sigma_2,\\ \\sigma_1\\sigma_2,\\ \\sigma_1\\sigma_2\\sigma_1$ from the Markov axioms and the Hecke relation alone, sorry-free. That these traces are the curvature-rank prefactors (that the representatives are the $E_\\infty$ classes) is the content of `prop:spectral-sequence-h3-explicit` and stays open, so the block stays a conjecture. Open consistency questions in the proof sketch: $\\sigma_1-\\sigma_2$ is not central, and four classes are listed while $Z(H_3)$ has dimension 3.",
    },
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
  ],
});
