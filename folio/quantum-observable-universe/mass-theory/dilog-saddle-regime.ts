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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Blocks that invoke the dilog saddle regime — the\ncontinuum $c_3$ geometry discussion, the\n[$\\Phi_q$/AJ machinery identification](#prop:phi-q-aj-machinery-identification),\nand the\n[$q_0$ Stokes-region identification](#conj:q-zero-stokes-region-identification)\n— reference this derivation rather than repeating it." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Clausen function $\\mathrm{Cl}_2$](#rem:clausen-function-mathlib-filler))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ([Clausen function Mathlib filler](#rem:clausen-function-mathlib-filler))" },
    {
      kind: "status",
      date: "2026-07-26",
      body:
        "The 4₁ volume-conjecture limit is now DISCHARGED in Lean, sorry-free: " +
        "`(2π/N)·log⟨4₁⟩_N → 2·Cl₂(π/3) = Vol(4₁)` is machine-proved as " +
        "`QOU.Knot.FigureEightVolume.tendsto_log_kashaev_vol` " +
        "(`FigureEightVolumeSqueeze.lean`), and the `VolumeConjecture41` " +
        "instance carries the proof — no cited sorry remains. The route is the " +
        "saddle program's elementary Riemann-sum squeeze (bricks E1–E5d, " +
        "milestone qou-cpfn): the Kashaev log-sum is squeezed onto the Clausen " +
        "primitive uniformly in k with master error E(N) → 0, the saddle grid " +
        "term at k = ⌊5N/6⌋ supplies the lower envelope, and the Cl₂ global " +
        "minimum at 5π/3 the upper. This required the honest target repair " +
        "VOL_4_1 := 2·Cl₂(π/3) exact (the earlier truncated decimal made the " +
        "statement false as stated). The two notes below are HISTORICAL: their " +
        "'does NOT discharge' caveats described the pre-E5d state and are now " +
        "superseded.",
    },
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
