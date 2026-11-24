import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:brings-riemann-hurwitz",
  lean: { ref: "qou:QOU.MassTheory.brings_riemann_hurwitz",
    validation: "not_checked",
  },
  title: "Riemann--Hurwitz count for a degree-4 covering $\\Sigma_4 \\to \\mathbb{P}^1$",
  tags: ["riemann-hurwitz", "ramification", "brings-surface", "s5-symmetry"],
  uses: [],
  proofs: ["prf:brings-riemann-hurwitz"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-22",
      body: "**Statement restated 2026-11-22 to what the Lean proves (owner ruling, round-trip pass 3).** `BringsRiemannHurwitzContext` carries the genera (4 and 0), the degree (`deg_is_four`) and the branch count (`branch_is_six`) as fields; the theorem returns the last two by projection and computes R_tot = 14 by arithmetic. Only the arithmetic is derived. The former statement called the map 'the canonical covering' onto P(V) and attributed the 6 branch points to S₅-symmetry; neither is in the Lean, and the audit flagged both: the canonical map of a genus-4 curve goes to P³, not P¹, and S₅ does not act on P¹ compatibly with such a cover. The Reeb-quotient sentence was dropped as context, not claim. Found by the blind round-trip audit (docs/audits/2026-11-22-roundtrip-blind-audit-pass3.md, block P11).",
    },
  ],
});
