# A-scaling: the A-stability criterion selects the irrep dimension `dim`, not the block `dim²`

**Date:** 2026-07-11 · **Axis:** Δ_λ closure (strong sector), binding magnitude A-scaling ·
**Follows:** the cross-isotope refutation ([PR #3558](https://github.com/litlfred/qou/pull/3558)) ·
**Gate:** Track-A (owner-reversed) · **Tier:** measurement (reuses previous work) ·
**No fit; nothing wired.**

## Scope

#3558 refuted the block-trace magnitude (`dim_q²` blows up 40–450× for T/³He/⁴He) and
validated the derived **sign** cross-isotope. This probe asks the sharper question: **which
magnitude power is A-stable?** — and the answer *selects* a magnitude, on a structural
criterion (A-stability), not a fit.

Probe [`deltalambda_binding_a_scaling_probe.py`](../../computations/deltalambda/deltalambda_binding_a_scaling_probe.py)
→ [witness](../../computations/deltalambda/deltalambda-binding-a-scaling.witness.json) (3/3).

## Result

`B(Δ)/target` with `Δ_λ = sgn·dim(λ)^p`, where **`dim(λ)` is the classical `q=1` integer
dimension** (the #3542 graded-trace magnitude, *not* the `q₀` quantum dimension), reusing the
precomputed `atom-chi-rust` characters and validated `y_λ = y_lambda_at(n,q₀)` (q₀ enters only
through `y_λ` and `χ^λ`; the Δ_λ factor is q-independent):

| p | D | T | ³He | ⁴He | spread | A-behaviour |
|---|---|---|---|---|---|---|
| 0 | 0.023 | 0.003 | 0.004 | 0.000 | 122× | tiny (`y_λ` suppresses) |
| 1 (irrep `dim`) | 0.171 | 0.225 | 0.304 | 0.107 | **2.8×** | **A-stable (min spread)** |
| 1.5 | 0.385 | 2.19 | 3.09 | 3.34 | 8.7× | grows |
| 2 (block `dim²`) | 0.909 | 22.5 | 33.4 | 107.7 | 119× | blows up |

## The selection (structural, not a fit)

The physical binding is **A-bounded** (`B/A ~ O(1)` per nucleon), so the magnitude power must
give an **A-bounded** ratio. The cross-isotope spread is **minimized at `p = 1`** (2.8×) and
grows monotonically on both sides — `p = 0` is `y_λ`-suppressed (122×), `p = 1.5` already grows
(8.7×), and `p = 2` (block `dim²`) blows up (119×). So the **A-stability criterion selects
`Δ_λ = sgn·dim`** — the **#3542 irrep trace** — as the unique A-stable power. This is a criterion
on *A-scaling*, independent of the target magnitude — **not** a fit.

## Consequences

- **The #3542 irrep trace was the right A-scaling all along.** The #3558 block `dim²≈101%` on
  the deuteron was **coincidental** — now doubly confirmed: it both blows up *and* is the wrong
  power by A-stability.
- **The remaining gap is an O(1) multiplicative factor**, not a wrong power. `target/B(dim)`:
  D 5.9, T 4.4, ³He 3.3, ⁴He 9.3 — same power, missing an O(1) coefficient (~3–9).
- **Combined with the cross-isotope sign validation (#3558):** the picture is
  **`Δ_λ = O(1)·sgn·dim(λ)`**, with the **O(1) coefficient the only remaining unknown** — a
  much sharper open problem than "the magnitude is unknown."

## Open (derive, not fit)

The O(1) coefficient (~3–9, mildly isotope-varying) is the remaining Track-A step. It must
be **derived** — e.g. from a per-nucleon / color (×3?) / interface structure — not fitted.
Whether it is exactly constant or carries residual A-structure needs the derivation. **Nothing
wired.**

## Cross-references

- Cross-isotope refutation + sign validation: [PR #3558](https://github.com/litlfred/qou/pull/3558)
- g_ρ / sign derivation: [PR #3542](https://github.com/litlfred/qou/pull/3542)
- Reused: `atom-chi-rust-{d,t,3he,4he}.witness.json`, `wedderburn_jones_markov.y_lambda_at`
