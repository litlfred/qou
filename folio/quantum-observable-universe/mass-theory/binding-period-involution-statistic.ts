import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-period-involution-statistic",
  lean: {
    ref: "qou:QOU.Mass.BindingInvolutionStatistic.binding_period_involution_statistic_four",
  },
  title:
    "The balanced dimension sum is the involution generating function for $2\\,\\mathrm{maj} + \\mathrm{content} \\circ \\mathrm{RSK}$",
  proofs: ["prf:binding-period-involution-statistic"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-09-07",
      body: "**Correction (2026-09-07).** This paragraph previously asserted that the\nleft side \"is a polynomial in $q$ of degree $n(n-1)$\". That is false for\nevery $n \\ge 2$: it is the degree of the prefactor $q^{n(n-1)/2}$ times the\nnaive bound, not of the product, and it exceeds the truth by\n$H_{\\min}(n) - n = \\Theta(n^{3/2})$. At $n = 3$ the polynomial is\n$q^{4} + 2q^{3} + q^{2}$, of degree $4$, against the claimed $6$; the\ndegrees run $1, 4, 8, 14$ for $n = 2,3,4,5$ against $2, 6, 12, 20$.\nThe identity displayed above is unaffected — only the degree remark was\nwrong. The block's own Lean sibling already carried the counterexample:\n`statExponents_three : statExponents 3 = {2, 3, 3, 4}` is kernel-decided\nand has maximum exponent $4$, so the `.lean` and the `.md` disagreed with\neach other. Derivation and verification:\n[`zn_hook_length_closed_form_probe.py`](../../../computations/deltalambda/zn_hook_length_closed_form_probe.py)\n(6/6, exact integer arithmetic) and\n[`hmin_closed_form_and_rev_sublinearity_probe.py`](../../../computations/deltalambda/hmin_closed_form_and_rev_sublinearity_probe.py)\n(5/5).",
    },
  ],
});
