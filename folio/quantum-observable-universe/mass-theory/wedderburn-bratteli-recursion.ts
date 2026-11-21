import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:wedderburn-bratteli-recursion",
  title:
    "Wedderburn--Bratteli recursion for Jones--Markov weights $y_\\lambda$ at $H_n(R, q)$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.wedderburn_bratteli_recursion",
    validation: "not_checked",
  },
  uses: [
    "conj:alpha-k-derivation-procedure",
    "conj:explicit-alpha-k-h3",
  ],
  tags: [
    "wedderburn",
    "bratteli",
    "recursion",
    "jones-markov",
    "y-lambda",
    "q-content",
    "hoefsmit",
    "structural-derivation",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-20",
      body: "Owner ruling 2026-11-20 (bean `qou-w8cg`): the statement wrote the recursion as $y_\\lambda^{(n+1)} = z\\sum_{\\mu\\nearrow\\lambda} F_q\\, y_\\mu^{(n)}$ with $F_q$ unspecified. Each single edge already gives $y_\\lambda$ (checked at $(3,1)$ from both parents), so the sum double-counts. Restated as the two proved forms (restriction sum rule and single-edge relation) with $F_q = [d\\pm1]_q/([2]_q[d]_q)$ explicit. The proof sketch now gives the proof; its older empirical sections are marked convention-C history.",
    },
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Degenerate Lean replaced by the convention-D recursion (W8b, 2026-11-20, gap 3 of `qou-w8cg`).** The Lean sibling's recursion predicate forced $y \\equiv 0$ (its edges had no $\\mu \\subset \\lambda$ constraint and a free content field), it carried an undisclosed `axiom` whose hypothesis could never hold, and the `lean.ref` name did not exist. It now proves, sorry-free over a generic field: the convention-D Jones weights $y_{(a,b)} = [a-b+1]_q/[2]_q^{a+b}$ (two-row shapes; three-row shapes carry weight $0$ under D) satisfy the Bratteli sum rule $y_{(a,b)} = y_{(a+1,b)} + y_{(a,b+1)}$, and the single-edge relations $[2][d]\\,y_{(a+1,b)} = [d+1]\\,y_{(a,b)}$ and $[2][d]\\,y_{(a,b+1)} = [d-1]\\,y_{(a,b)}$ with $d = a-b+1$. At $n=3$ it reproduces $([4]_q/[2]_q^3, 1/[2]_q^2, 0)$. The `.md` summed the edge factor over all incoming edges; restated to the proved forms the same day (see the note above). The normalisation $\\sum_\\lambda f^\\lambda y_\\lambda = 1$ is not encoded (needs a partition type with the branching rule).",
    },
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
  ],
});
