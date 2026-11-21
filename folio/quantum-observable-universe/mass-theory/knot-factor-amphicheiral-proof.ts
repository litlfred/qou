import { proof } from "../../schema/builders";

export default proof({
  label: "prf:knot-factor-amphicheiral",
  title: "Proof of knot factor amphicheiral",
  uses: ["cor:knot-factor-amphicheiral"],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "An earlier version of this corollary stated $\\chi_\\lambda(\\beta_\\mathcal{K}^*) = (-1)^{[\\lambda = (1^n)]}\\chi_\\lambda(\\beta_\\mathcal{K})$ (\"sign-flip on the alternating block\") and collapsed the formula to $a = 1 - h^2$ with $h := \\chi_{(1^n)}/\\chi_{(1^n)}(\\mathbf{1})$. The sign-flip claim is empirically false on $4_1$: the 1-dimensional alternating character factors through writhe, which is $0$ for both $\\beta_{4_1}$ and its mirror, so both compute to $+1$ rather than to opposite signs. In addition, the collapse to $1 - h^2$ silently invoked $\\sum_{\\lambda \\neq (1^n)} w_\\lambda (\\chi_\\lambda/\\chi_\\lambda(\\mathbf{1}))^2 = 1$, which is a Cauchy–Schwarz bound, not an identity. The Markov-amphicheirality framework above replaces both defects with a single, structural condition (conjugacy of $\\beta_K^*$ to $\\beta_K$ in $H_n$) that $4_1$ in fact satisfies, and gives the clean sum-of-positive-squares formula. See the computational verification in the canonical formalism.",
    },
  ],
});
