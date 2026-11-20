import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:terms-2-6-higher-operations",
  title:
    "Terms 2 and 6: infinite Wedderburn / Habiro-cyclotomic sum and GB root-of-unity residue sum",
  lean: {
    ref: "qou:QOU.BraidKnot.terms_2_6_higher_operations",
    validation: "not_checked",
  },
  uses: ["conj:spectral-sequence-h3-explicit"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
    {
      kind: "note",
      body: "**Historical record — closed dead-end routes for Term 2.** Earlier drafts of this block searched for the source of the $\\Phi_q$ Cauchy kernel in the Hochschild cohomology of $H_n(R, q)$ (a Gerstenhaber cup-product tower of $[\\sigma_i] \\in HH^1$). This route is **closed**: direct symbolic computation gives $HH^1(H_3(R, q)) = 0$ at generic $q$ (dim Der = dim Inner = 3), consistent with semisimplicity (every derivation of a matrix algebra is inner), so there is no non-trivial class to take cup products of. The deformation-cohomology route ($H_3(R, q)$ as a deformation of $\\mathbb{R}[S_3]$) is also closed: $HH^2(\\mathbb{R}[S_3]) = 0$ by Burghelea's theorem (group cohomology of a finite group over a characteristic-0 field vanishes in positive degree), so the Hecke deformation is gauge-trivial in cohomology. The naive proxy $\\mathrm{tr}_M(\\sigma_0^k) \\propto 1/(q;q)_k$ was also tested and is FALSE (the algebra power oscillates rather than matching $\\Phi_q$ growth; cup product in $HH^*$ is the cochain-level product, not algebra multiplication). The surviving correct framing is the infinite Wedderburn / Habiro-cyclotomic reading in the statement. Remaining open items are reindexing questions (which $E_\\infty^{\\ell, *}$ page corresponds to the infinite-level Wedderburn sum) and verification that the $\\ell \\geq 2$ cyclotomic residue reproduces the empirical Term 6 corrections — not missing-derivation questions.",
    },
  ],
  tags: [
    "spectral-sequence",
    "hochschild",
    "habiro",
    "colored-jones",
    "kashaev",
    "wedderburn",
    "cup-product",
    "higher-operations",
    "term-2",
    "term-6",
  ],
});
