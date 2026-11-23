import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lusztig-vs-hermitian-bar",
  lean: {
    ref: "qou:QOU.BraidKnot.LusztigVsHermitianBar.lusztig_eq_hermitian_iff_real",
    validation: "not_checked",
  },
  title:
    "Lusztig bar ($q \\mapsto q^{-1}$) vs Hermitian-$\\ast$ ($q \\mapsto \\overline{q}^{-1}$) on the complex Hecke algebra: the two anti-involutions coincide on the parameter iff $q \\in \\mathbb{R}$. On the unit circle $|q| = 1$, Lusztig coincides with complex conjugation ($\\overline{q} = q^{-1}$) while Hermitian becomes the identity on $q$; on general $|q| > 1$ with $\\mathrm{Im}(q) \\neq 0$ the three involutions (Lusztig, Hermitian, complex conjugation) are pairwise distinct. The split is the categorical home for any future $\\mathrm{Im}(q_0)$ contribution.",
  uses: ["prop:q-zero-complex-extension"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean formalization specialises to $\\mathbb{R}$ for the archimedean evaluation at the substrate $q_0$." },
    {
      kind: "status",
      date: "2026-05-24",
      body: "**Research-grade infrastructure (PR #1127).** Distinguishes the Lusztig algebra anti-involution from the Hermitian $\\ast$ on the complex Hecke algebra. The two coincide on $q \\in \\mathbb{R}$ (current framework convention), so the framework has not had to distinguish them; the split is *invisible* in the real-axis specialization and only becomes meaningful if $\\mathrm{Im}(q_0) \\neq 0$. This is infrastructure for a possible future refinement of the bar-symmetric / bar-anti-symmetric decomposition (cheat-sheet §4); it does **not** propose $\\mathrm{Im}(q_0) \\neq 0$.",
    },
  ],
  tags: [
    "bar-involution",
    "involution",
    "complex-q",
    "hermitian",
    "research-grade",
  ],
  cites: [
    "wenzl1988",
  ],
});
