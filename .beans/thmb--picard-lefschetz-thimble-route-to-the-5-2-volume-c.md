---
# thmb
title: 'Picard–Lefschetz / thimble route to the 5₂ volume conjecture — literature + feasibility'
status: todo
type: task
priority: normal
tags:
    - thimbles
    - hyperbolic-volume
    - literature
    - 5_2
created_at: 2026-08-09T19:15:46Z
updated_at: 2026-08-09T19:15:46Z
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
