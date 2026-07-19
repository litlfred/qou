import { remark } from "../../schema/builders";

export default remark({
  label: "rem:dilog-saddle-regime",
  title:
    "Dilog saddle regime: the $\\theta = \\pi/3$ saddle of $\\mathrm{Im}\\,\\mathrm{Li}_2(e^{i\\theta})$ and $\\mathrm{Vol}(4_1)$",
  interprets: "conj:kashaev-volume-conjecture",
  uses: ["conj:kashaev-volume-conjecture"],
  cites: ["kashaev1997", "murakami-murakami2001", "thurston1978"],
  tags: [
    "kashaev",
    "saddle-point",
    "dilogarithm",
    "clausen",
    "hyperbolic-volume",
    "figure-8-knot",
    "consolidation-home",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-19",
      body:
        "The block's DERIVATIVE claim `V'(θ) = −log(2 sin(θ/2))` is now " +
        "Lean-proved sorry-free on both sides of the series↔integral bridge: " +
        "integral side `QOU.Knot.hasDerivAt_clausen` (FTC) and series side " +
        "`QOU.Knot.hasDerivAt_cl_2` (Abel-regularised assembly closing the " +
        "term-by-term derivative of `Cl_2`), with the classical Zagier bridge " +
        "itself machine-proved as `QOU.Knot.clausen_eq_series` " +
        "(`QOU/Knot/Clausen.lean`, 14 sorry-free theorems; PR #3787). Combined " +
        "with `saddle_critical_point` (2026-07-13 note below), the full " +
        "critical-point analysis `V'(θ) = 0 ⟺ θ = π/3` is machine-checked. " +
        "The VALUE `V(π/3) = Cl₂(π/3)` (hence `Vol(4₁) = 2 Cl₂(π/3)`) remains " +
        "narrative — no elementary closed form exists (it is the " +
        "ideal-tetrahedron volume; transcendental), tracked in bean qou-44ma. " +
        "This also does NOT discharge the 4₁ volume-conjecture sorry (saddle " +
        "existence/value, Andersen–Hansen/Ohtsuki).",
    },
    {
      kind: "note",
      date: "2026-07-13",
      body:
        "The central saddle critical-point claim of this block — `V'(θ) = " +
        "−log(2 sin(θ/2)) = 0 ⟺ 2 sin(θ/2) = 1 ⟺ θ = π/3` on `(0, π)` — is now " +
        "Lean-proved sorry-free as `QOU.Knot.FigureEightVolume." +
        "saddle_critical_point` (`FigureEightVolumeSaddle.lean`), needing no " +
        "Clausen function (only `sin(π/6) = 1/2` + injectivity of `sin` on " +
        "`[−π/2, π/2]`). It is the *same* critical point as the figure-eight " +
        "Kashaev saddle: the `4 sin²(πj/N)` factors of `kashaevProd_eq_sin` " +
        "cross 1 there. The value `V(π/3) = Cl₂(π/3)` and hence `Vol(4₁) = " +
        "2 Cl₂(π/3)` remain narrative (the Clausen/Lobachevsky evaluation is " +
        "not yet in Mathlib — the load-bearing saddle-value brick).",
    },
  ],
});
