import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:terms-2-6-higher-operations",
  title:
    "Terms 2 and 6: infinite Wedderburn / Habiro-cyclotomic sum and GB root-of-unity residue sum",
  lean: {
    ref: "qou:QOU.BraidKnot.terms_2_6_higher_operations",
    validation: "not_checked",
  },
  uses: ["prop:spectral-sequence-h3-explicit"],
  authorNotes: [
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
