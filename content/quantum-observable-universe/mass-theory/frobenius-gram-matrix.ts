import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-gram-matrix",
  lean: { ref: "qou:QOU.Archimedean.frobenius_gram_matrix", validation: "not_checked" },
  title: "Frobenius Gram matrix and dual construction in $H_3(q)$",
  uses: [],
  tags: [
    "gram-matrix",
    "frobenius-dual",
    "hecke-algebra",
    "markov-trace",
    "knot-operator",
    "pair-production",
    "annihilation",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probes/frobenius_gram_matrix_probe.py",
    witness: "computations/probes/frobenius-gram-matrix-probe.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-04",
      body: "**Markov-bug fix.** Earlier versions of this block asserted $\\mathrm{tr}_M(e^-) = z^3$ and offered a 'peel-from-the-right' derivation. This was incorrect: $\\sigma_1\\sigma_0$ is **not** in the sub-algebra $H_2 = \\langle \\sigma_0 \\rangle$ (the Markov axiom $\\mathrm{tr}_M(\\sigma_n \\cdot x) = z\\,\\mathrm{tr}_M(x)$ requires $x \\in H_n$), so the Markov-property step cannot be applied directly to $\\sigma_1 \\cdot \\sigma_0\\sigma_0$ after the cyclicity step. The canonical Ocneanu–Wenzl recursion gives $\\mathrm{tr}_M(e^-) = hz^2 + z$, verified independently in `docs/audits/-trm5-markov-bug.md` against the y-lambda Wenzl-bridge consistency $\\mathrm{tr}_M(b_i) = \\sum_\\lambda y_\\lambda(q) \\chi_\\lambda(b_i)$ (residual $\\sim 10^{-32}$ after fix; $\\sim 0.12$ before). The fix has been applied to `tools/pyhecke/python/pyhecke/gram.py` and the Gram matrix table below.",
    },
    {
      kind: "note",
      date: "2026-06-04",
      body: "**Symbolic Gram entries require recomputation.** The proposition's matrix and $g_{ij}$ formulas were derived assuming $\\mathrm{tr}_M(e^-) = z^3$ (now known to be incorrect — see Markov-bug note above). The entries that involve $\\mathrm{tr}_M$ applied to a product whose Hecke normal form contains $e^-$ must be rederived with $\\mathrm{tr}_M(e^-) = hz^2 + z$. Numerically, the post-fix Gram matrix is symmetric to machine precision and reproduces the y-lambda Wenzl-bridge identity exactly (Markov-bug audit, § 'Visible symptom: Gram matrix non-symmetric'). The corrected Python compute lives at `tools/pyhecke/python/pyhecke/gram.py`; a follow-up commit will recompute the symbolic table below.",
    },
  ],
});
