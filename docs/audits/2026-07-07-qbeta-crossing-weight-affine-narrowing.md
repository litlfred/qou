# Q_β crossing-weight AFFINE narrowing — the ladder-factor bar-parity split

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone (the archimedean evaluation,
sharpened) · **Follows:** the [eval-map bar-decomposition](2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md)
(registry KC18) · **Tier:** proved-lean + symbolic-exact · **No `c_k` value, no
wiring, no tier change** (registry §8 flip-flop guard).

## Context — where this sits

KC17 excluded the naive `u`-side re-expansion; KC18 localized the odd (decay)
channel to the **archimedean evaluation map** — the Frobenius counit `ε` /
Markov trace `tr_M` on the `N=0` nucleon Hecke NF difference — and decomposed
its **numerator** `E(w) = h²/2 − h·w` into a bar-even identity term `h²/2` and a
bar-odd crossing/loop term `−h·w` (`h = q − q⁻¹` bar-odd; the crossing weight
`w` bar-even, `z` at leading order, KC13). The sharpened keystone it left open:
*derive the higher-order crossing weight whose odd part reproduces the
`c_3 → −2` shadow.* This audit analyses the object where the `c_k` actually
live — the **ladder factor** `L(w) = E(w)/E(w₀)` — and narrows that target.

## Result — the evaluation map is affine in the crossing weight

Probe [`qbeta_crossing_weight_affine_probe.py`](../../computations/qbeta/qbeta_crossing_weight_affine_probe.py)
→ [witness](../../computations/qbeta/qbeta-crossing-weight-affine.witness.json)
(12/12, sympy-exact) + sorry-free Lean
[`QOU/QBeta/CrossingWeightAffine.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/CrossingWeightAffine.lean)
(`lean`-direct exit 0, generic field char ≠ 2):

- **(A) Affine.** `E(w) = h²/2 − h·w` has `∂E/∂w = −h` (constant): the
  evaluation map is **degree-1 in the crossing weight** — it introduces no
  nonlinearity. (`evalMap_affine`.)
- **(M) Möbius.** In lowest terms (multiply top and bottom by `2/h`, `h ≠ 0`)
  the ladder factor collapses to the clean fractional-linear form
  `L(w) = (h − 2w)/(h − 2w₀)`. (`evalMap_ratio`.)
- **(O) Odd part linear in the departure.** With bar involution `h ↦ −h`
  (`w, w₀` fixed), the bar-**odd** (decay/swing) part of `L` is **exactly**

  `L_odd = 2h·(w − w₀) / (4w₀² − h²)`

  — LINEAR in the crossing-weight departure `(w − w₀)`, times the **fixed
  bar-odd kernel** `K(q) = 2h/(4w₀² − h²)`. (`ladder_odd_part`.)
- **(E) Even part.** `L_even = (4·w·w₀ − h²)/(4w₀² − h²)` — bar-even, the
  shadow/mass channel. (`ladder_even_part`.)
- **(C2) Counit reference.** At `w₀ = 1` (the counit `ε`), `L − 1 = −2(w−1)/(h−2)`.
  (`ladder_counit_ref`.)

## Why this matters — two sharpenings

1. **The keystone reduces to a scalar.** Because `E` is affine in `w`, the
   entire `c_k` odd channel (including the `c_3 → −2` odd signature) is the
   image of the **single scalar bar-even departure `(w − w₀)`** under the fixed
   kernel `K(q)`. The evaluation contributes only `K(q)`; there is no
   self-interaction, no cross-term mixing at the evaluation stage. The open
   task "derive the higher-order crossing weight" is now precisely: *exhibit
   `(w − w₀)` as a function of the ladder variable* — a bounded scalar target,
   not an operator/`u`-series search.

2. **Trace-side corroboration that `c_3` cannot be a fixed real-q number.**
   `K(q) = 2h/(4w₀² − h²)` is a **fixed rational function of `q`** — no anchor
   enters the evaluation map. So the observed 2.375% `c_3` anchor-swing
   ([c_3-not-exact verdict](2026-07-06-c3-not-exact-cross-anchor-verdict.md))
   **cannot** originate in the evaluation; it must live entirely in the
   crossing weight `w(q)`'s fibre structure. This is an independent, trace-side
   restatement of the fibre/root-of-unity requirement (Invariant 1 of the
   refuted-class map): the evaluation is anchor-rigid, so all anchor-dependence
   is upstream in `w`.

This sharpens KC18 (numerator split) to the ladder factor where the `c_k`
live, and it does so without touching production: `c_2 = −1` remains the one
derived rung; `c_3+` remain open (precision floor).

## Scope / discipline

Structural narrowing (scope-(a)), **not** a `c_3` derivation. No `c_k` value is
produced; nothing is wired (flip-flop guard, registry §8). The two open pieces
the narrowing exposes:

- **the scalar crossing weight `w(u)` beyond leading order** — what `(w − w₀)`
  is as a function of the ladder variable `u = b·ℏ_q²`; and
- **the substrate→archimedean pullback** from the fibre parity carriers
  (KC15 `D(q)`, KC16 index-parity) into `w` — KC18's evaluation-map identity is
  the bridge, and this audit shows the bridge is affine, so the carrier feeds
  `w` linearly.

## Suggested registry row

**KC19** — evaluation map affine in the crossing weight ⇒ ladder factor Möbius;
bar-odd part `= 2h(w−w₀)/(4w₀²−h²)` (linear in `(w−w₀)`, fixed anchor-free
bar-odd kernel); anchor-rigidity of the evaluation ⇒ `c_3` swing lives in
`w(q)`. Tier: proved-lean (`CrossingWeightAffine.lean`) + symbolic-exact.
(To be added to [`ck-dk-canonical-registry.md §9`](../coordination/ck-dk-canonical-registry.md)
+ JSON twin when the keystone tranche branch #3449 next touches the registry —
coordinated there to avoid a cross-branch §9 edit collision.)

## Cross-references

- Evaluation map (KC18): [`2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md`](2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md)
- Numerator Lean: `QOU.Interactions.QBetaCounitTrace` (`trMNP = h²/2 − h·z`)
- `z` bar-even: `QOU.QBeta.z_bar_invariant` (KC13)
- `c_3` not exact: [`2026-07-06-c3-not-exact-cross-anchor-verdict.md`](2026-07-06-c3-not-exact-cross-anchor-verdict.md)
- Keystone ledger: [`docs/coordination/z-ck-fmap-keystone.md`](../coordination/z-ck-fmap-keystone.md)
