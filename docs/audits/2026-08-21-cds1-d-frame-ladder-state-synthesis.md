# `qou-cds1` state synthesis — the convention-D Q_β ladder re-derivation

**Date:** 2026-08-21 · **Bean:** `qou-cds1` (S1 of the 2026-08-15 convention-D ruling)
· **Tier:** scope-(a) — consolidation of committed results; no new value, no fit,
no wiring, no tier change · **PR:** #5348 (branch `claude/borel-alien-calculus-n24484`)

## Why this exists

`qou-cds1` — "re-derive the Q_β c_k ladder under D, and this is **not** a z-swap"
— reads as wide-open in its own body (the sensitivity table showing
`c₃ ≈ −974` under D). It is **not** wide-open at the *structural* level: both
legs of the re-derivation are already **forced and formalized**, symbolically,
across S1/S2 and the phase-covariance file. This note consolidates that scattered
state so the remaining open piece is stated precisely — and so the `−974` figure
is not misread as a proposed value.

## Both structural legs are forced and formalized

### Leg 1 — the phase (forced; `LadderPhaseMirrorCovariance.lean`, sorry-free)

The ladder eigenphase `α = (z−1)h/2` must be **bar-odd** (a framing phase rides
a writhe prefactor; writhe is mirror-odd, `WritheMarkovInvariance.writhe_inv`).
The general identity `phaseTwice_bar_anomaly` gives `bar(2α)+2α = h·(z − bar z)`,
so the phase is bar-odd **iff** `z` is bar-fixed (`phaseTwice_bar_odd_iff_z_bar_fixed`).

- **C** (`z_C = √q/(1+q)`) is bar-fixed → the C phase is bar-odd *by structure*,
  but mirror-**blind** (it does not see the crossing-sign exchange).
- **D** (`z_D = q³/(q²+1)`) has anomaly exactly `h` (`zD_sub_bar_eq_h`), because
  `bar(z_D) = z_D − h` is the **negative-stabilisation loop value**: under D, bar
  *exchanges the two Markov loop values*, which is exactly what mirror must do.

The D-frame bar-odd part of the phase is therefore `α_D − h²/4`
(`phaseTwiceD_sub_hsq_bar_odd`), and it is **forced, not fitted**: it is the phase
evaluated at the mean of the two loop values, which under D equals the bar-mean
(`phaseTwice_projected_eq_loopMean` + `zD_bar_mean_eq_loop_mean`). No free
parameter remains. This is why the move is "not a z-swap": swapping `z_D` into
the C-frame `α` keeps the *formula* while breaking the bar parity its downstream
consumers assume — it is the phase *formula* that re-derives, giving the `−h²/4`.

### Leg 2 — the weights (forced, exact ℚ(q); S2 PR #5185, `gram-radical-exact-probe`)

`z_D` satisfies the Jones/Temperley–Lieb pin exactly: `z_D·[2]_q = q²`
(`z_D = q²/[2]_q`, `zD_eq_qsq_div_bracketTwo`) — the mirror of
`decayLadder_zC_not_jones` (C **fails** the pin). So under D the decay trace
factors through TL: `markovWeights_eq_jones_of_threeRow_eq_zero` forces the
Jones-closure weight vector, solved symbolically over ℚ(q) by S2:

| λ | rows | `y_λ` under D | sign, `q>1` |
|---|---|---|---|
| `(3)`   | 1 | `(q⁴+1)/(q²+1)²` | positive |
| `(2,1)` | 2 | `q²/(q²+1)²`     | positive |
| `(1³)`  | 3 | `0`              | exactly zero |

A **positive-semidefinite** form of signature `(5,0,1)` — the third row is
*killed*, not made negative. This resolves the horn left open in
`decayLadder_zC_threeRow_ne_zero` (C is genuinely three-row): **under D the decay
trace is two-row TL**, consistent with the mass channel's two-row forcing.

## What is actually open — and why it is fenced

The c_k **ladder assembly** from these forced ingredients. It is **not** closed,
and the obstruction is the anti-fit fence, not missing structure:

- The forced phase projection `α_D − h²/4` closes **92.03 %** of the D-frame gap
  in the amplifier-free coordinate and leaves a residual **41.94×** the C-frame
  one (`qbeta-eigenphase-branch-and-barodd-projection.witness.json`).
- So the forced ingredients (exact weights + forced phase) do **not** reproduce
  Q_β. Any c_k chosen to absorb that residual is a **fit** — and the standing
  fence (`LadderPhaseMirrorCovariance.lean` §Scope) is explicit: searching for
  further phase corrections is fitting "until one lands with the structural
  standing of `c₂ = −1`." That is the same magnitude wall the c₃ program hits in
  every frame.

## Correction carried by this note — do not misread the sensitivity numbers

The `c₃ ≈ −974.43 / −974.38` and "implied empirical `c₂ ≈ −9.299`" in the cds1
sensitivity table are what the **current C-frame extractor returns when fed
`z_D`** (a naive z-swap, which S1 itself proves is invalid via
`decayLadder_zC_threeRow_ne_zero`). They are **sensitivity measurements, not
proposed D-frame values**, and must not be wired, quoted as "the D-frame c₃", or
read as evidence about anything. The properly re-derived D-frame c_k are not
known — that is precisely the open, fenced piece above.

## Net state of `qou-cds1`

**Structurally determined, numerically fenced.** Both legs (phase + weights) are
forced and formalized symbolically; `z_D` is the two-row Jones parameter; the
positive-definiteness is a *feature* of D. What remains is a c_k assembly that the
forced ingredients cannot complete without a fit — the general c₃/Q_β magnitude
wall, now confirmed to sit in the D frame exactly as it did in C. The
convention-immune facts (the REFUTED-as-real-q verdict, the KC21 parity, the
`c₂ = −1` *proof*) are untouched; only their *objects* now carry the D
convention.

**Formalize-first next step (non-fitting):** before any wide c_k re-fit, state
the structural invariant a *forced* D-frame c₂ would have to satisfy (the D
analogue of C's `c₂ = −1 = 1 − b²ℏ⁴` Taylor-exactness) and check whether the
exact weights + `α_D − h²/4` phase determine it. If they do, that is the first
re-derived coefficient; if they leave freedom, the fence holds and the c_k stay
open. Do **not** run the extractor on `z_D` and report the output as a value.

## Executed 2026-08-21 — the convention is localised to the N=1 phase (forced)

Carrying out that next step, reading `Q_beta_categorical` factor by factor
settles *where* the convention lives, and it is sharper than "the whole ladder
is C-conditional":

- **Only `N1_factor = cos(α − b·ℏ_q²/2)` reads the Markov parameter**, through
  `α = (markovZ' − 1)·h/2`.
- **`N2..N5` — carrying `c₂=−1`, `c₃=−2`, `c₄`, `c₅` — are closed forms in `q`
  through `hoefsmitB` and `hbarQ'` alone**, with no `markovZ'` and no `α`. They
  are the pure Kashiwara/Hopf tails `b^k·ℏ_q^{2k}`.

Formalised sorry-free (`lean`-direct EXIT=0) in
[`QOU/BraidKnot/LadderConventionLocalisation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/LadderConventionLocalisation.lean):
`Q_beta_categorical_eq_ofPhase` (the ladder is the `φ = α q` instance of a
phase-parameterised family) and `Q_beta_categorical_ofPhase_tail_common` (two
phases differ only by their `cos` factors, `ckTail` common).

**Two consequences.**

1. **The categorical `c_k` (k ≥ 2) are z-convention-immune** *as the ladder is
   constructed*. So the C→D move acts on this construction **only** by replacing
   the phase `α q` with the D-frame `α_D − h²/4`; the higher rungs do not move.
   This distinguishes the **categorical** `c_k` (structural, z-free) from the
   **extracted** `c_k` (inverted from full Q_β, z-dependent).
2. **The S1 `c₃ ≈ −974` is exactly the N=1 phase change mis-attributed to the
   higher rungs by the extractor.** Feeding `z_D` into the full-Q_β extractor
   dumps the entire `cos`-factor movement onto the `c_k`; that is the −974, not a
   categorical value. This *reconciles* S1's sensitivity number with the
   z-freeness of the categorical rungs.

**Scope (unchanged fence).** This localises the z-dependence and explains the
artifact; it does **not** claim the *physical* D re-derivation leaves the
Kashiwara tails untouched. Whether `N2..N5` should themselves change under D
(if the Kashiwara operators see the trace normalisation) is the surviving open
question — and closing the residual `41.94×` by adjusting them would still be a
fit until a rung lands with `c₂ = −1`'s structural standing.
