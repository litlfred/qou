# S-channel saddle-point / Ohtsuki expansion vs the Q_β c_k ladder — honest negative (2026-08-01)

**Branch** `claude/schannel-saddle-point-ohtsuki-2026-08-01` · **PR** #4488 ·
**Tier** numerical-exact (closed-form κ + structural obstructions + Lean sign
invariant) · **Discipline** scope-(a)/(b); κ derived from geometry never tuned to
c_k or 4.075; **no c_k wired, no SDeformedVolumeChannel instance, u(q₀)/S_eq OPEN**.

The **geometric complement** to Route A's Taylor expansion (PR #4484,
`SLeakMagnitudeTaylorRatio.lean`) and Route B's q* closed-form negative (PR #4483).
Two deliverables were asked; both come back as clean, informative negatives — the
kind the owner (a physicist) wants: the real answer, not a fitted "yes".

## Corpus-grep first (this was NOT re-derived from scratch)

The Ohtsuki κ-tower is **already derived exactly** in the corpus, from the 4₁
Kashaev sum `log J_N` (PSLQ-exact, parity-certified):

| rung | closed form | parity | sign |
|---|---|---|---|
| κ₁ | **11√3π/108** ≈ 0.5542 | odd → √3·π | **+** |
| κ₂ | **2π²/27** ≈ 0.7311 | even → π² | **+** |
| κ₃ | **1081√3π³/21870** ≈ 2.6545 | odd → √3·π³ | **+** |
| κ₄ | **98π⁴/729** ≈ 13.095 | even → π⁴ | **+** |

Sources: [`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md),
[`scripts/qbeta_ohtsuki_kappa1_extract.py`](scripts/qbeta_ohtsuki_kappa1_extract.py),
[`QOU/QBeta/OhtsukiTowerBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/OhtsukiTowerBarParity.lean).
The standing corpus position — **κ_n ≠ c_k; "the bridge from the 4₁ resurgence
action to the physical Q_β observable action remains the open keystone"** — is
here **confirmed from the direct-comparison side**, which had not been run as a
standalone, and the leading κ's are reproduced **independently**.

Probe: [`computations/qbeta/qbeta_ohtsuki_kappa_vs_ck_direct_comparison.py`](../../computations/qbeta/qbeta_ohtsuki_kappa_vs_ck_direct_comparison.py)
(mpmath, 80 dps, exit 0, 9 assertions). Witness
`qbeta-ohtsuki-kappa-vs-ck-direct-comparison.witness.json`.

## (A) Independent κ reproduction (a small positive win)

A fresh Richardson extraction of the raw Kashaev sum
`log J_N(4₁) = log Σ_k exp(2 Σ_{j≤k} log 2sin(πj/N))`, N = 2048…262144, dps 80,
Vandermonde in 1/N — **not** reading any corpus witness — returns

```
κ₁ (fit) = 0.554216472404899899   vs  11√3π/108 = 0.554216472404899899   (~24 digits)
κ₂ (fit) = 0.731081807488100638   vs  2π²/27    = 0.731081807488100638   (~18 digits)
```

Two independent derivations of the same coefficients strengthen the corpus
values (owner directive: parallel derivation of an open result is a feature).

## (B) Deliverable 2 — the prize: do κ_n MATCH c_k? **No.** Four obstructions

At the canonical (muon) substrate `q₀ = 1.10997858…`, `u_ladder = b·ℏ_q² =
0.008517`, the Q_β ladder coefficients are `c₂ = −1` (Lean-proved Taylor-exact)
and `c₃ = −2.0693…` (q₀-extract). The direct comparison:

**[B0] Raw (task pairing κ₁↔c₂, κ₂↔c₃).**

| | κ (derived, geometric) | c (Q_β ladder) | \|Δ\| | signs |
|---|---|---|---|---|
| κ₁ vs c₂ | +0.554216 | −1.000000 | 1.554 | + vs − |
| κ₂ vs c₃ | +0.731082 | −2.069343 | 2.800 | + vs − |

Not a match — not even in sign. The gap is O(1)…O(3), a factor ~10⁶ above the
≤ 1e-6 that an exact identification requires (and far above the c₃ ~3% near-match
that already burned four sessions, PR #1452↔#1479).

**[B1] Universal sign obstruction.** All κ_n **> 0** (positive rationals
11/108, 2/27, 1081/21870, 98/729 times √3^{parity}·π^n); both `c₂, c₃` **< 0**.
Every κ_n differs in sign from every c_k.

**[B2] No real rescaling `u ↦ λ·u` aligns them.** Solving `κ₁·λ = c₂` gives
`λ = −1.8043` (forced negative since κ₁>0, c₂<0); then `κ₂·λ² = +2.380 ≠ c₃ =
−2.069`. The even power `λ²` is sign-blind, so a positive even rung `κ₂·λ² ≥ 0`
can never hit the negative `c₃` — **for any real λ**. The identification survives
no reparametrization of the ladder variable.

**[B3] Field obstruction.** κ_n ∈ ℚ(√3)·π^⌈n/2⌉ carry a factor of **π^n**
(transcendental); `c₂ = −1 ∈ ℚ` is π-free (derived-tier, Taylor-exact). A nonzero
rational multiple of π^k (k ≥ 1) is irrational, so it cannot equal −1.

**[B4] Convergence obstruction.** The Ohtsuki κ_n series is a **divergent**
Gevrey-1 asymptotic series (κ_{n+1}/κ_n = 1.32, 3.63, 4.93, … growing → n!/A^n
tail, corpus #3571). The Q_β `c_k` ladder is **convergent** at u ≈ 0.0085 (the
truncation-order framing). A convergent power series and a divergent asymptotic
series are not the same analytic object.

**Verdict (B): the Q_β `c_k` ladder is NOT the figure-eight Chern–Simons /
Ohtsuki perturbative series.** This is a scope-(a) negative on the raw
identification, hardened to a scope-(b) *sign* exclusion (proved invariant:
even-rung positivity, below). It does **not** close the deeper 4₁-resurgence ↔
Q_β-action bridge — that remains the open keystone. The κ_n are topological
invariants of 4₁; the c_k are the Q_β observable ladder.

## (C) Deliverable 1 — does the geometric saddle series reproduce Route A's 4.075? **No, provably.**

Route A established that the magnitude `|S_p/S_m| = 4.07512700316` is **not a
period** but **anchor-offset arithmetic** near the S-zero:
`S(q) = c₃-target(q) + Vol(4₁)`, with `S`-zero `q* = 1.1099785930315233` and
`|S_p/S_m| ≈ |(q_p−q*)/(q_m−q*)|` ([`2026-08-01-bring-embedding-magnitude.md`](2026-08-01-bring-embedding-magnitude.md)).
The offset-ratio mechanism is confirmed here (the audit's rounded anchor offsets
give ≈ 4.09, matching Route A's exact 4.07512700 up to the pin rounding).

The **geometric saddle / Ohtsuki series** produces a **smooth** `q₀`-evaluated
`Im 𝔙₄₁` (≈ +0.055, the odd-sub-tower resummation, corpus #3654). A smooth
`q₀`-quantity has ratio ≈ 1 across the `Δq ≈ 1.3e-8` anchor gap — the probe's
smooth surrogate `P(q) = c₃-target(q) + 2·Vol(4₁)` (shifted to avoid the
zero-cross) gives `|P_p/P_m| = 0.9759 ≈ 1`. It **cannot** be 4.075. This is the
**SP1 smoothness wall**, already Lean-proved in Route A's
[`SLeakMagnitudeOffsetRatio.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SLeakMagnitudeOffsetRatio.lean)
(`smooth_period_excluded_as_magnitude`), here re-confirmed from the
geometric-series side.

**Honest scope (as the task flagged):** the saddle series supplies S's
*geometric content* — the leading `Vol(4₁)` (0-loop) and the smooth CS scale — but
does **not** remove the magnitude ratio's hypersensitivity. The 4.075 lives in the
near-zero crossing of `S` (an anchor-placement / observable property), not in any
saddle period. This is **L1 structural**, not a new L2 observable; the saddle
series does not "resolve" the magnitude as a prediction.

## Deliverable-1/2 residual-per-order summary (as requested)

- **Magnitude (Deliverable 1):** no per-saddle-order residual is definable — the
  geometric object (smooth `Im 𝔙₄₁`) and the target (hypersensitive anchor-offset
  ratio) are categorically different. The saddle series reproduces `Vol(4₁)` to
  full precision (0-loop) and the smooth `Im 𝔙 ≈ 0.055` (all orders resummed);
  it is provably unable, at **any** order, to produce 4.075.
- **κ_n vs c_k (Deliverable 2):** κ₁ vs c₂ |Δ| = 1.55 (sign +/−); κ₂ vs c₃
  |Δ| = 2.80 (sign +/−). No order matches; the mismatch is structural (sign,
  field, convergence), not a truncation residual.

## The geometric meaning of q* (small positive finding)

At `q* = 1.1099785930…` the bar-odd `S = Im 𝔙₄₁(u(q₀))` vanishes. Under the
corpus channel identity and `Im 𝔙₄₁(u) = κ·(Re²u − Im²u)`
([`FigureEightComplexVolume.imV₄₁_zero_on_diagonal`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean)),
`S = 0` is exactly the **amphichiral / diagonal-crossing** locus `|Re u| = |Im u|`
where the Chern–Simons part vanishes — consistent with
`signflip_forces_diagonal_cross`. So `q*` is where the (open) map `u(q₀)` crosses
the complex-volume diagonal; the anchors sit on opposite sides (the sign flip).
This is a geometric *reading* of `q*`, not a derivation of its value — Route B
already showed `q*` is experiment-limited (Q_codata is measured), so `q*` carries
no closed constant beyond the amphichiral condition.

## Formalized invariant (the (b) behind the negative)

Sorry-free, lean-verify exit 0:
[`QOU/QBeta/OhtsukiKappaVsCkSign.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/OhtsukiKappaVsCkSign.lean).

- **`kappa{1,2,3,4}_pos`** — the derived Ohtsuki closed forms are positive
  (`positivity`).
- **`even_rung_positive_ne_neg`** — the core invariant: `κ·λ² ≥ 0` for `κ > 0`
  and any real `λ`, so it never equals a negative `c < 0`. The even-power sign is
  reparametrization-invariant.
- **`no_real_rescaling_aligns`** — no real `λ` maps the tower onto the ladder
  (`κ₂·λ² = c₃ < 0` is already impossible).
- **`c2_ne_kappa1`, `neg_ck_ne_kappa`** — concrete: `c₂ = −1 ≠ κ₁`; every
  negative `c_k` differs from all four κ_n.

## Discipline compliance

Derive-then-check: κ derived from the Kashaev geometry, compared once, no scan for
4.075 or for a c_k match. Anti-fit: every candidate + residual reported; the raw
comparison, the rescale attempt, and the field/convergence facts are all shown —
none cherry-picked. Anti-laundering: no `c_k` wired, no `SDeformedVolumeChannel`
instance, no `u(q₀)` map claimed; the bridge and `S_eq` stay OPEN. Corpus-grep:
prior Ohtsuki work read and cited, not re-litigated.

## Net

Both deliverables are honest negatives, each with a proved invariant:

1. The geometric saddle series does not (and provably cannot, being smooth)
   reproduce Route A's 4.075 — it is anchor-offset arithmetic, SP1 wall.
2. The Q_β `c_k` ladder is not the 4₁ Ohtsuki series — sign, field, and
   convergence all forbid it; the deeper resurgence-action bridge stays the open
   keystone.

The κ₁, κ₂ independent reproduction and the `q*` amphichiral reading are the
small positive by-products.
