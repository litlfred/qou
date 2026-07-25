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
      date: "2026-07-25",
      body: "**Part A CLOSED (elementary $q\\to1^-$ side, off $x=0$), sorry-free.** The Faddeev limit $(1-q)\\log\\Phi_n(x;q)\\to\\mathrm{Li}_2(x)$ for $x\\in(0,1)$ is now a Lean theorem: `QOU.Archimedean.archimedeanLimit_Ioo` produces the `ArchimedeanLimit x` instance for every $0<x<1$, wired into the conditional consumer. The proof (`QOU.Archimedean.DilogPartAConvergence`, with `DilogPartARiemannSum` and `DilogReflection`) assembles: Brick 1 $\\log\\Phi_n=-\\sum\\log(1-xq^k)$; Brick 2 the geometric-partition left-Riemann sum; B3.1 $\\int_0^1 -\\log(1-xu)/u=\\mathrm{Li}_2(x)$; B3.2 monotonicity of the integrand (convex-slope); B3.3 per-cell + telescoping error $\\le(1-q)(-\\log(1-x))$; B3.4 tail $\\le q^n x/(1-x)$; B3.5 the $\\varepsilon$-$\\delta$ instance with $q^n\\le e^{-n(1-q)}$. Supersedes the 2026-07-19 progress note. **Part B is still OPEN** (below).",
    },
    {
      kind: "note",
      date: "2026-07-25",
      body: "**Part B remains the genuine open content.** Part A closes only the elementary $q\\to1^-$ convergence for fixed $x\\in(0,1)$. Part B — the substrate continuation $q\\to1^+$ (to $q_0\\approx1.11$) and the $x\\to1^-$ uniformity, where the factors $1-xq^k$ change sign (the poles of $\\Phi_n$ approach the $\\mathrm{Li}_2$ branch cut) and the Frobenius-pairing pole cancellation must do real work — is untouched. The conjecture as a whole (the full Faddeev/Kashaev cross-cusp statement) stays open.",
    },
    {
      kind: "note",
      date: "2026-07-19",
      body: "**Part A progress (historical).** Two analytic ingredients of Part A were Lean-proved sorry-free in `QOU.Archimedean.DilogReflection`: the dilogarithm derivative `hasDerivAt_LiTwo` ($d/dx\\,\\mathrm{Li}_2 = -\\log(1-x)/x$, which Mathlib lacked), and the integral representation `LiTwo_eq_integral` ($\\mathrm{Li}_2(x)=\\int_0^x -\\log(1-t)/t$) — the integral-representation bottleneck named in the 2026-06-07 Part-A audit. The Euler reflection `LiTwo_reflection'` also landed. Superseded by the 2026-07-25 closure note above.",
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
