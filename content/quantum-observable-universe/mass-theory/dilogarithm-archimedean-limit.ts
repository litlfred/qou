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
      kind: "note",
      date: "2026-07-19",
      body: "**Part A progress (not conjecture closure).** Two analytic ingredients of Part A (the elementary $q\\to1^-$ side) are now Lean-proved sorry-free in `QOU.Archimedean.DilogReflection`: the dilogarithm derivative `hasDerivAt_LiTwo` ($d/dx\\,\\mathrm{Li}_2 = -\\log(1-x)/x$, which Mathlib lacked), and the integral representation `LiTwo_eq_integral` ($\\mathrm{Li}_2(x)=\\int_0^x -\\log(1-t)/t$) — the integral-representation bottleneck named in the 2026-06-07 Part-A audit. The Euler reflection `LiTwo_reflection'` also landed. This narrows Part A to the remaining Riemann-sum$\\to$integral convergence; it does **not** touch Part B (the substrate continuation $q\\to1^+$ and $x\\to1^-$ uniformity), which remains the genuine open content of the conjecture.",
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
