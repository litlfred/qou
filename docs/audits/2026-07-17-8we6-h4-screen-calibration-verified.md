# 8we6 critical-eye: the H₄ `O(u⁴)` screen is verified — the nine negatives stand

**Date:** 2026-07-17 · **Branch:** `claude/pr-3660-merge-pipeline-ephmw4` (PR #3833) ·
**Bean:** `8we6` (genuine c₄ rungs → Casoratian W₃ sign test), session `qou-tti3` ·
**Probe:** [`qbeta_h4_screen_calibration_verify.py`](../../computations/qbeta/qbeta_h4_screen_calibration_verify.py) (+ witness) ·
**Tier:** exact (sympy s-series ladder + Cauchy-integral cross-engine; no fit) ·
**Scope:** (a) — a machinery-verification of the screen, plus one self-correction.

## Why this probe

Bean `8we6` item 1 asks for a genuine `c₄^even` rung via an H₄ Hoefsmit build.
The 07-12→13 wave executed **nine** candidate constructions and recorded all
nine as `GATE-FAIL` against a cheap `O(u⁴)` admission screen
([`2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md`](2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md)):
the three owner-authorized Route-A framings + six mid-word-entangled σ₂
candidates. The audit itself warns that a tenth *hand-arranged* candidate would
be "tuning — the fit trap." Before either proposing new framework content or
treating the nine negatives as settled, the **screen those negatives rest on**
must itself be verified. That screen encodes an *unstated* calibration between
the cheap criterion and the full ladder; if it is miscalibrated, the nine
`GATE-FAIL`s are unreliable.

## The calibration identity (made explicit)

The screen judges a candidate by the low-order Taylor coefficients
`φ_i := [sⁱ] log f(1+s)` of the net-ratio `f(q) = Δ(net)₄ / Δ(net)₃`
(`s = q−1`). The link to the actual ladder rung shifts is:

$$
\Delta c_2 = \frac{\varphi_4}{U_2[4]}, \qquad
\Delta c_3 = \frac{\varphi_6 - \Delta c_2\, U_2[6]}{U_3[6]},
$$

where `U₂, U₃` are the `s`-series of `u², u³`, `u = b·ℏ_q²`,
`b = √(q⁴+q²+1)/(q²+1)`. At `q=1`: `U₂[4] = b(1)² = 3/4` and
`U₃[6] = b(1)³ = 3√3/8`, so `Δc₂ = (4/3)·φ₄`. A candidate contributes an
independent `c₄`-first rung only if `φ₄ = φ₆ = 0` (the `[s⁴]=[s⁶]=0` screen).

## What the probe verifies (all pass — witness `allPassed=True`)

1. **Calibration constants exact:** `U₂[4] = 3/4`, `U₃[6] = 3√3/8` (symbolic).
2. **Synthetic test vectors through the *real* ladder solver:** three
   constructed multipliers `g ∈ {1+t⁴, 1+t², 1+t³}` (`t=q−1`) run through
   `ladder_cks`; predicted `Δc₂/Δc₃` match the measured ladder shifts exactly.
   The `1+t³` odd seed confirms the screen's **even-only blindness**
   (`Δc₂ = 0`). These are machinery test vectors — nothing physical, nothing
   tuned.
3. **Two-engine φ agreement (all nine candidates):** the sympy series φ and an
   **independent Cauchy-integral engine** (`mpmath.taylor` method `quad`, no
   sympy series) agree to **~1e-47…1e-50**.
4. **Cross-probe against the published shifts:** `(4/3)·φ₄` reproduces the
   Route-A audit's exact `c₂` shifts **+12, +13/6, −40** for A1/A2/A3.

**Verdict:** the `O(u⁴)` screen is sound. The nine even-order `GATE-FAIL`s are
trustworthy; there is no `c₄^even` rung among the nine, and `W₃` stays gated
(its conditional branch never fires).

## Self-correction (critical-eye on our own probe)

The first run's independent engine was an order-8 **Vandermonde solve on
clustered points** `s = 1e-3…8e-3` — catastrophically ill-conditioned. It
reported `engines_agree = False` with deviations `O(1…10³)` for every
candidate, i.e. `allPassed = False`. This was a defect in **the verifier**, not
the screen: checks (1), (2), (4) all passed exactly in that same run (the
sympy φ were independently confirmed by the exact ladder shifts and the
published-shift cross-check). Replacing the Vandermonde fit with the Cauchy
contour integral (well-conditioned, genuinely independent of sympy's series
algorithm) collapsed the deviation to `~1e-48` and all five assertions pass.
Recorded here as the concrete instance of "some probes may be inaccurate —
keep critical eye" applied to our own instrument.

## Scope note — the screen's blind spot

The `[s⁴]=[s⁶]=0` screen is an admission test **for an even (`c_k^even`)
rung only.** It never inspects the odd coefficients `[s⁵], [s⁷]` of `log f`,
which carry the odd-ladder (`Q_β` / `c_k^odd`) content. The witness records
these per candidate (`odd_leakage_s5`, `odd_leakage_s7`) for the record: a
future H₄ object aimed at an *odd* rung would need a separate odd-order screen.
For the even-`c₄` hunt of bean `8we6` this is not a defect — it is the correct
scope.

## Disposition

- **The nine H₄ negatives are verified sound** — their screen is machine-checked
  calibrated. Bean `8we6` item 1 remains open by an *honest wall*, not a tooling
  artifact: a genuine `c₄`-first H₄ object requires a construction whose
  low-order cancellation is **derived, not arranged** (per the gate-fail audit),
  and the `O(u⁴)` screen is now a *verified* admission test for any future
  proposal.
- No `c_k` wired; no tier change; registry untouched (no rung produced).

## Cross-references

- Nine-negatives audit + gate definition: [`2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md`](2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md)
- Route-B structural prune: [`2026-07-03-8we6-h4-route-b-structural-prune.md`](2026-07-03-8we6-h4-route-b-structural-prune.md)
- Trusted rungs + Casoratian endpoint: [`2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md`](2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md)
