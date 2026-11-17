---
# thmb
title: Picard–Lefschetz / thimble route to the 5₂ volume conjecture — literature + feasibility
status: in-progress
pr: 8298
type: task
priority: normal
tags:
    - thimbles
    - hyperbolic-volume
    - literature
    - "5_2"
    - reorg-2026-10-04
created_at: 2026-08-09T19:15:46Z
updated_at: 2026-11-17T10:22:30Z
parent: qou-n4nr
---

**Why this bean exists.** The figure-eight volume conjecture is *machine-proved in this
repo* — `QOU/Knot/FigureEightVolumeSqueeze.lean`, `tendsto_log_kashaev_vol`, verified
2026-08-09 sorry-free with axioms `[propext, Classical.choice, Quot.sound]`, per-module
build exit 0 / 3159 jobs with the `.olean` deleted first. The obvious question is whether
the same method reaches 5₂. **It does not, for a structural reason:**

`⟨4₁⟩_N = Σ_k ∏_j (2 − 2cos(2πj/N))` is a sum of **non-negative reals**. That is the
whole proof: `log Σ = max log-term ± log N`, upper envelope from `log N + log sup`, lower
envelope from the single grid term at `k* = ⌊5N/6⌋`, and the max term is a Riemann sum
for Clausen. **`⟨5₂⟩_N` has no positivity** — it oscillates, and its saddle is complex
(`y₁ = 0.78492 + 1.30714i`, the root the whole `qou-xblo` lane is about). No positivity
⟹ no squeeze. What is needed instead is genuine control of oscillatory cancellation:
steepest descent / Picard–Lefschetz thimble decomposition, i.e. which thimbles the
contour actually decomposes into and with what Stokes data.

**Task 1 — settle the literature before pricing anything.** I believe Ohtsuki (2016),
*On the asymptotic expansion of the Kashaev invariant of the 5₂ knot*, proves the volume
conjecture for 5₂ via asymptotic expansion. **This is stated from memory and has NOT been
verified — verify it first.** It decides whether this is "formalise a known theorem"
(expensive but bounded) or "prove something open" (a research programme). Do not let
either framing propagate into a claim until checked. Related: Ohtsuki–Yokota on the
general asymptotic-expansion machinery.

**Task 2 — inventory the corpus's own thimble infra, which is real but scattered.**
`thurston-relaxation.md` already asserts the correspondence: "the residue sum becomes the
Picard–Lefschetz thimble decomposition of the Seiberg–Witten action `S(z)`", with
Gröbner–Shirshov reduction depth ↔ number of ideal tetrahedra, and SDP
complementary-slackness rank ↔ number of thimble flows realising the optimum. Live files
mentioning thimbles/Lefschetz include `lifting-and-descent/motivic-substrate.{md,lean}`,
`mass-theory/gb-residue-spectral-sum.md`, `mass-theory/pre-tau-vs-post-tau.md`,
`mass-theory/poincare-lefschetz-borromean.{md,lean}`. A substantial deprecated set sits
in `_deprecated/thimble-content/` — including `archimedean-remainder-exponential-decay.lean`
(growth bounds) and `algebraic-quantum-volume-specialization.lean`. Decide what is
recoverable rather than assuming it is all dead.

**Task 3 — the honest scoping question.** Even granting thimble infra, the deliverable is
an asymptotic with *oscillatory* error control, which is a different formalisation animal
from the 4₁ squeeze. Price it against bean `rvnc` (Rivin concavity → `Vol(5₂) = 3·D(y₁)`
geometrically), which is far cheaper and buys the *volume*, though not the *volume
conjecture*. Those are different targets and the difference should be stated wherever
either is claimed.

**What surreal/standard-part infra can and cannot do here** (see bean `hypr`). It cannot
replace the ε–δ: the goal shape is `Tendsto … atTop`, and `Hyperreal.IsSt` only gives
convergence along `hyperfilter ℕ ≤ atTop`, which is strictly weaker; the converse arrow
does not exist. Where surreal/asymptotic infra *would* genuinely pay is the bookkeeping of
orders of growth — the 4₁ proof's real cost is hand-assembling
`masterErr N = |Cl₂(2π/N)|/2 + (π/N)|log(2 sin(π/N))| + 7(π/N)(|log(2 sin(π/N))| + log 2)`
and proving it `→ 0`. A Hardy-field / Landau-symbol layer (the corpus has
`AppendixSurreals/Asymptotics.lean`, `BirthdayGrading.lean`, `Blowup{,Calculus}.lean`)
would carry that as one order symbol. That is an ergonomics win, not a soundness one.

**Control.** The trefoil `3₁` is a torus knot, not hyperbolic — `Vol = 0`,
`Vol_q(β_{3₁}) = 0`. Its Kashaev sum does not grow. Any thimble/asymptotic story must
reproduce *no exponential growth* for `3₁`; if it hands the trefoil a volume, it is wrong.

---
**2026-08-09 — Task 1 SETTLED, and the identification is better than expected.**

The paper was uploaded to `main` (`library/104171-qt-83/10.4171-qt-83.pdf`, blob `632e54ac`,
commit `21e1e81`) and read here, 67 pages. **Ohtsuki 2016 is confirmed**:
*On the asymptotic expansion of the Kashaev invariant of the 5₂ knot*, Quantum
Topol. **7** (2016) 669–735, DOI 10.4171/QT/83. The 5₂ volume conjecture is a
**published theorem**. So route C is "formalise a known theorem", not "prove
something open" — reprice accordingly. (A second commit `7f95cbf` was also
pointed at; it is an **empty** commit, tree identical to its parent, same blob.
Nothing extra in it.)

Structure: §2 the invariant, **§3 the saddle point method**, §4 Poisson
summation, §5 proof of Thm 1.1, App. A properties of φ, App. B convergence,
**App. C critical points**, App. D.

**THE FINDING.** Ohtsuki's potential (p. 671) is
`V̂(x,y) = Li₂(xy) + Li₂(1/(xy)) + Li₂(y) − Li₂(1/y) − Li₂(1/x) − Li₂(1)` and his
critical system (App. C) is `(1−x)y = 1`, `x(y−1)² = 1`. Eliminating gives
`x³ = (1−x)²` — which **is the corpus's own saddle cubic `y² = (1−y)³` under
`x = 1 − y`**, exactly. The exchange is the reflection `z ↦ 1−z` already proved
in Lean here as `cRogersL_add_one_sub`.

Now in Lean, sorry-free: `QOU/QBeta/FiveTwoOhtsukiCriticalPoint.lean` —
`ohtsuki_elim` (polynomial, over any `CommRing`, needing **no** `1−x ≠ 0`),
`ohtsuki_cubic_iff_saddle_cubic`, `saddle_cubic_of_ohtsuki_system`. Axioms
standard; `ohtsuki_elim` needs only `[propext, Quot.sound]`.

**AND THE VOLUME.** Probe `qbeta_5two_route71_ohtsuki_critical_point_probe.py`,
80 dps, 5 gates all passing: at the **complex** critical point,
`Im V̂ = Vol(5₂)` — residual `4.9e-50`, which is the precision floor of the
corpus's own SnapPy HP 50-dps constant. Extended here to 79 dps:
`2.8281220883307831627638988092766349427709813173006494770435203272588025483`.
G4 is the control: the **real** critical point gives `1.7668…`, not the volume,
so branch selection is analytic input that no algebraic statement supplies.

**Method lesson, recorded because it nearly became a false report.** The first
run showed a `3.8e-13` mismatch, *stable* across dps 40/60/80/120 — so not a
precision artifact, and it looked like a real gap. The cause was a `Vol(5₂)`
constant typed from memory, wrong from the 12th digit. The corpus's recorded
value is authoritative and its own docstring already warns a 15-dps literature
anchor (`2.82812208833410`) was wrong. **A residual that does not shrink with dps
is evidence about the inputs, not about the identity.**

**Still not done:** the asymptotic. §3–§5 is where the oscillatory control lives,
and none of it is formalised. The identification above is a bridge to the
*critical value*, not to the *limit*.


## Round 58 Update (PR #8298)
- **Status:** `in-progress` (PR `litlfred/qou#8298`, head `92f8a80b907a40e6db76eb1a8a85f081c5960913`, Commit 1 `df446885b17718b4f18e584a2765ba2e802adb68`).
- **Lean 4.24.0 Modules:** `folio/quantum-observable-universe/lean/QOU/BraidKnot/N5LevelSixRootThresholdAndThreeLinkTriad.lean` and `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoSaddleHessianAndFourOneStokesCrossCheck.lean` (`0` `sorry`, `0` `axiom`, `0` warnings, `0` advisories across all 5 static audits).
- **80-dps Probe & Witness:** `computations/probes/round58_n5_level_six_ohtsuki_thimble_fourone_stokes_dilog_probe.py` and `computations/probes/round58-n5-level-six-ohtsuki-thimble-fourone-stokes-dilog.witness.json` (`allPassed: true`, `0` raw `float64`).
