# The A=3 amplitude `E` is the frame-free Birkhoff CROSS-RATIO `χ(P)`; constructing it, and the WALL is its VALUE

**Date:** 2026-08-08 · **Bean:** `qou-wiub` (A=3 magnitude keystone; epic `qou-x631`) ·
**Branch:** `claude/deltalambda-birkhoff-amplitude-e-2026-08-08` ·
**Tier:** formalize-first (Lean, sorry-free, `lean`-direct exit 0, `#print axioms` shows no `sorryAx`) ·
**Scope:** WALL — scope-(a); nothing fitted, nothing wired, `q₀`-derivation not routed through.
**Lean:** [`QOU/QBeta/BirkhoffAmplitudeE.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BirkhoffAmplitudeE.lean)
— exit 0, 0 real sorries, axioms `[propext, Classical.choice, Quot.sound]` only.

## The assignment

`QOU.QBeta.A3AntiSelfAdjointLift` (merged #4611) bracketed the A=3 Δ_λ magnitude lift
`r* = μ₃/c₃ ≈ 1.585` to **exactly one free real DOF** — the anti-self-adjoint off-block
amplitude `E`. Two prior results this week pinned `E`'s value to the **GLOBAL `0↔∞`
Birkhoff connection matrix** `P = (X^{(∞)})⁻¹ X^{(0)}` of the C1 module (= the DM q-cubic
`conj:qdifference-kernel-prolongation-symbol` = RSZ route-A `L1`): the LOCAL Stokes route
is empty (#4811, `StokesAmplitudeE.lean`), and the DT-index route is bar-parity excluded
(#4810, `DTIndexAmplitudeE.lean`). This front took the **construction** angle: build `P`'s
structural content from the existing q-difference D-module infra and try to derive `E`, or
prove the precise next wall.

## Convergence with the well-posedness sibling (not a contradiction)

Mid-task, the parallel well-posedness sibling (`BirkhoffAmplitudeWellPosed.lean`, sorry-free)
proved the decisive fact, and this front converged onto it:

> **`E` must be the gauge-invariant CROSS-RATIO of `P`, not a single matrix entry.**

Why: C1's local solution bases are unique only up to a `q`-invariant (elliptic) diagonal
normalization (`QCharacter.IsQChar.ratio_qInvariant`), so `P` carries the gauge
`P_{ij} ↦ (d_{∞,i})⁻¹ P_{ij} d_{0,j}`. A bare entry moves under that gauge (ill-posed as a
physical scalar); the cross-ratio `χ(P) = P₀₁P₁₀/(P₀₀P₁₁)` is the **unique** gauge-invariant
functional (4 entries − 3 gauge dims = 1 invariant). Since `E` is frame-free
(`A3AntiSelfAdjointLift.amplitude_injective`), `E = χ(P)`.

An earlier draft of this file argued the *opposite* interpretation (that `E` is a bare entry,
so `χ` is blind to it). The **algebra** in that draft was correct; the **interpretation** had
the identification backwards. The corrected file keeps the algebra — which in fact
*independently confirms* the sibling — and flips the reading. This is exactly the intended
outcome of parallel work (AGENTS.md §Parallel exploration): a second context reaching the
same object from a different direction, then converging on landing.

## What was proved (sorry-free)

| Theorem | Content |
|---|---|
| `offBlock_multiplier` | an off-block entry `f/g` (0-side / ∞-side q-characters) has σ_q-multiplier `c₀/c∞` (unconditional in a field) |
| `crossRatio_conn_qInvariant` | **construction lemma** — the cross-ratio of the four connection entries is σ_q-invariant (elliptic) **because the exponent multipliers cancel**: multiplier `(c₀₁c₁₀)/(c₀₀c₁₁) = 1` under the connection balance |
| `connMultiplier_balance` | the connection multipliers `c_{ij}=c_{0,j}/c_{∞,i}` satisfy `c₀₁c₁₀ = c₀₀c₁₁` (both `= c₀₀c₀₁/(c∞₀c∞₁)`) — so the ellipticity is automatic, not an extra hypothesis |
| `offBlock_elliptic_of_resonant` | resonance `c₀=c∞` ⇒ an entry is itself elliptic (`IsQChar.ratio_qInvariant`); a generic entry is non-resonant, only the balanced cross-ratio is elliptic |
| `crossRatio_gauge_invariant` | `χ(P)` invariant under the diagonal normalization gauge (independent confirmation of the sibling) |
| `entry_gauge_movable` | a bare entry is movable to any nonzero value under a χ-preserving gauge ⇒ ill-posed as `E` (sibling `entry_not_gauge_invariant`) |
| `distinct_entries_share_crossRatio` | two distinct nonzero entries sit over one cross-ratio ⇒ a bare entry is not a well-posed functional |
| `lift_injective_in_crossRatio` | since `E = χ(P)` and `E ↦ factor` is injective (`amplitude_injective`), the A=3 lift is a well-defined function of the connection cross-ratio |
| `lift_reachable_by_crossRatio` | every target factor is reached by some cross-ratio value (`amplitude_surjective`) — so deriving `χ(P)` pins the lift; *choosing* it to hit `r*` is the forbidden fit |

The **construction lemma** `crossRatio_conn_qInvariant` is the genuine new content: it derives
`χ(P)`'s ellipticity — the abstract reason it is theta-valued and
`C1ConnectionPoles.connRatio_elliptic` holds — straight from the q-character algebra, and it
singles out the cross-ratio (not any entry) as the well-posed `E`-carrier.

## The wall — the VALUE of `χ(P)`

The wall is no longer "which functional of `P` is `E`" (answered: the cross-ratio). It is the
**VALUE of `χ(P)`**, and it decomposes cleanly:

- **0-side (Fuchsian) exponent — DETERMINED.** Root of C1's indicial equation
  `c₀² + (q−1)c₀ + (q−1) = 0` (`C1FuchsianExponents`, `C1ZeroSideExponents`).
- **∞-side exponent — OPEN.** C1 is slope-`½` irregular at `∞`; its canonical solution needs
  the q-native wild / alien datum (RSZ route closed as a mis-citation,
  `2026-08-08-rsz-c1-infinity-route-closed.md`; bean `qou-vkg5`).
- **Cross-ratio closed form — OPEN.** `χ(P)` has a conjectured theta closed form whose
  *ellipticity* is proved (`C1ConnectionPoles.connRatio_elliptic`); `χ(P) = closed form` is
  unproved (needs the analytic construction; bean `qou-wgnx`).

## Open successor (§3b, no instance)

`BirkhoffCrossRatioSuppliesAmplitude` — content-bearing dependent-conjecture class carrying:
the DETERMINED 0-exponent (indicial root); the OPEN ∞-exponent (nonzero, non-resonant); the
well-posed identity `E = χ(P)`; a **bar-odd** consistency clause `σ E = −E` (matching
`DTIndexAmplitudeE.amplitude_barOdd`); and the physical lift. **No instance** — deriving
`χ(P)`'s value from the analytic construction is the open keystone; *choosing* it to hit `κ`
(`lift_reachable_by_crossRatio`) is the forbidden fit and is not done. This corrects
`StokesAmplitudeE.GlobalBirkhoffSuppliesAmplitude` (whose `multislope` necessary condition is
C1-inapplicable — C1's `∞` is single-slope, `RSZ.rszIsoformalDim = 0`) and aligns with the
sibling's `AmplitudeIsGaugeInvariantCrossRatio`.

## Honesty ledger

- **No fit.** `E`/`χ(P)` never solved from `r*`/`μ₃`/`c₃`; the surjectivity witness is
  exhibited precisely to label *pinning* the value as the forbidden fit.
- **No axiomatized conclusion.** The class carries genuine sub-hypotheses (determined
  0-exponent, open ∞-exponent, bar-odd consistency) and the well-posed identity; **no instance**.
- **`q₀`-derivation not routed through** (the permanent gate is respected).
- **Formalize-first, machine-verified.** `lean`-direct exit 0; axioms
  `[propext, Classical.choice, Quot.sound]`, no `sorryAx`; deps `A3AntiSelfAdjointLift` +
  `QCharacter` built from source against the restored Mathlib olean cone.
- **Converges with, does not overturn, the well-posedness sibling.**

## Cross-references

- Lean (new): [`BirkhoffAmplitudeE.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BirkhoffAmplitudeE.lean).
- Amplitude bracket (source): [`A3AntiSelfAdjointLift.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/A3AntiSelfAdjointLift.lean).
- q-character infra: [`QCharacter.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/QCharacter.lean).
- Connection matrix + cross-ratio χ: [`C1ConnectionPoles.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/C1ConnectionPoles.lean); 0-side exponents [`C1FuchsianExponents.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/C1FuchsianExponents.lean).
- Sibling routes: local Stokes wall [`2026-08-08-stokes-amplitude-e-local-wall.md`](2026-08-08-stokes-amplitude-e-local-wall.md); DT-index exclusion [`2026-08-08-dtindex-amplitude-e-bar-parity-exclusion.md`](2026-08-08-dtindex-amplitude-e-bar-parity-exclusion.md); RSZ ∞-route closed [`2026-08-08-rsz-c1-infinity-route-closed.md`](2026-08-08-rsz-c1-infinity-route-closed.md); Birkhoff object [`2026-08-01-branch-selection-birkhoff-connection-matrix.md`](2026-08-01-branch-selection-birkhoff-connection-matrix.md).
- Ledger: [`docs/coordination/option-e.md`](../coordination/option-e.md) (ROUTE 2-c-BIRKHOFF row).

-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (q-characters, connection matrix)
-- Ref: [manuscript] docs/audits/2026-08-08-stokes-amplitude-e-local-wall.md
-- Ref: [manuscript] docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md
