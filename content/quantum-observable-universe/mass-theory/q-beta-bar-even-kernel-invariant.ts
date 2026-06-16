import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-bar-even-kernel-invariant",
  title:
    "$\\mathfrak{Q}_\\beta$ precision-ladder $\\bar{}$-even discriminant — the kernel $R(q,\\xi)$ produces a clean integer-$u$ ladder $\\prod_k(1+c_k\\,u^k)$ if and only if $R$ is even under $t \\mapsto -t$ ($t = q-1$); $(1-u^2)$ at N=2 is the prototype",
  lean: {
    ref: "qou:QOU.QBeta.BarEvenInvariant.bar_even_quadratic_term_in_t_squared",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-c-2-eq-neg-one-structural",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004"],
  computation: {
    engine: "sympy",
    script:
      "folio-assistant/computations/qbeta/qbeta_bar_even_kernel_invariant_probe.py",
    witness:
      "folio-assistant/computations/qbeta/qbeta-bar-even-kernel-invariant-probe.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "precision-ladder",
    "structural",
    "bar-involution",
    "kernel-invariant",
    "no-fit",
    "formalize-first",
  ],
  authorNotes: [
    {
      kind: "status",
      body:
        "**Theorem (this proposition).** Sorry-free Lean proof " +
        "(`q-beta-bar-even-kernel-invariant.lean`) — one-line `ring` identity " +
        "over `CommRing R` plus a symbolic substitution check on the N=2 " +
        "factor. **Compute (sympy):** verified in " +
        "`qbeta_bar_even_kernel_invariant_probe.py` (witness " +
        "`qbeta-bar-even-kernel-invariant-probe.witness.json`), assertion " +
        "`bar_even_invariant_holds_for_N2_factor` (passing).",
    },
  ],
});
