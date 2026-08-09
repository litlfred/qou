import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:dilogarithm-archimedean-limit",
  title:
    "$(1{-}q)\\,\\log\\Phi_n(x; q) \\to \\mathrm{Li}_2(x)$ under $\\tau_{\\mathrm{arch}}$",
  lean: {
    ref: "qou:QOU.QPochhammer.ArchimedeanLimit",
    validation: "not_checked",
  },
  uses: [
    "def:q-pochhammer-partial-product",
    "cor:quantum-dilogarithm",
    "def:archimedean-realization-functor",
    "rem:kashaev-as-archimedean-realization",
  ],
  cites: ["faddeev1994", "kashaev1997", "zagier1986"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-24",
      body: "**Part A CLOSED (Lean-proved sorry-free).** The elementary $q\\to1^-$ convergence $(1-q)\\log\\Phi_n(x;q)\\to\\mathrm{Li}_2(x)$ is now fully proved for all $x\\in(0,1)$: the `ArchimedeanLimit x` typeclass is inhabited off $x=0$ by `archimedeanLimit_Ioo` in `QOU.Archimedean.DilogPartAConvergence` (B3.5). The Tauberian/Riemann-sum$\\to$integral exchange is discharged via the telescoping error bound `riemann_error_bound`, the tail bound `tail_bound`, and $\\int_0^1 -\\log(1-xu)/u\\,du=\\mathrm{Li}_2(x)$ (`integral_zero_one_eq_LiTwo`), with $q^n\\le e^{-n(1-q)}$ (`pow_le_exp_neg_mul`) controlling the $\\varepsilon$-$\\delta$ tail. The unconditional consumer form `partialProduct_to_LiTwo_Ioo` wires it into downstream use. Part A no longer contains open content; **the conjecture's remaining open content is entirely Part B** — the substrate continuation $q\\to1^+$ and the $x\\to1^-$ cross-cusp uniformity. Landed via #4157 (supersedes the #4106 Riemann-sum route).",
    },
    {
      kind: "note",
      date: "2026-07-25",
      body: "**Part B remains the genuine open content — and why it is hard.** Part A closes only the elementary $q\\to1^-$ convergence for fixed $x\\in(0,1)$. Part B — the substrate continuation $q\\to1^+$ (to $q_0\\approx1.11$) and the $x\\to1^-$ uniformity — is untouched, and it is not more of the same estimate: there the factors $1-xq^k$ **change sign**, so the poles of $\\Phi_n$ approach the $\\mathrm{Li}_2$ branch cut and the Frobenius-pairing pole cancellation must do real work. The conjecture as a whole (the full Faddeev/Kashaev cross-cusp statement) stays open.",
    },
    {
      kind: "note",
      date: "2026-07-19",
      body: "**Part A ingredients (superseded by the 2026-07-24 closure above).** Two analytic ingredients of Part A (the elementary $q\\to1^-$ side) landed sorry-free in `QOU.Archimedean.DilogReflection`: the dilogarithm derivative `hasDerivAt_LiTwo` ($d/dx\\,\\mathrm{Li}_2 = -\\log(1-x)/x$, which Mathlib lacked), and the integral representation `LiTwo_eq_integral` ($\\mathrm{Li}_2(x)=\\int_0^x -\\log(1-t)/t$) — the integral-representation bottleneck named in the 2026-06-07 Part-A audit. The Euler reflection `LiTwo_reflection'` also landed.",
    },
  ],
  tags: [
    "tier:keystone",
    "q-pochhammer",
    "dilogarithm",
    "bloch-wigner",
    "archimedean",
    "saddle-point",
    "open-problem",
  ],
});
