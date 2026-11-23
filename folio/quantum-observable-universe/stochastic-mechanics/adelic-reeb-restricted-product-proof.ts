import { proof } from "../../schema/builders";

export default proof({
  label: "prf:adelic-reeb-restricted-product",
  title: "Proof of adelic reeb restricted product",
  uses: ["prop:adelic-reeb-restricted-product"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Proof.** Both parts are proved formally over the abstract value group\n$\\Gamma$ in\n[`adelic-reeb-restricted-product.lean`](adelic-reeb-restricted-product.lean).\n\nThe squeeze\n is `Finset.sum_lt_sum`: a finite sum of\n\n(formalised in Lean as a linearly ordered abelian group:\n`AddCommGroup` $+$ `LinearOrder` $+$ `IsOrderedCancelAddMonoid`)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): promotes the single global $\\varepsilon$-squeeze of\n[surreal squeeze](#lem:surreal-squeeze) to a *separate squeeze at each prime*,\nwhich is the local–global content used by\n[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): : it is what makes the two dual archimedean reductions of\n[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze) — the fibre functor\n$\\tau_{\\mathrm{arch}} = \\pi_\\infty$ across places, and the standard part\n$\\mathrm{St} : \\mathbf{No} \\to \\mathbb{R}$ along the filtration — land in the\nsame ordered target, and it is the natural place to look for further exploitable\nrigidity (e.g. the automorphic generalisation flagged in the outlook of\n[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Downstream.** This proposition supplies the local–global skeleton consumed by\n[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze) and, through it, the\nleading-coefficient reduction of [BSD surreal bound](#rem:bsd-surreal-bound).\nThe squeeze content is purely structural: it takes the per-place inequalities\nas hypotheses and is therefore independent of the q-NS conjecture cone behind\n[surreal squeeze](#lem:surreal-squeeze)." },
  ],
});
