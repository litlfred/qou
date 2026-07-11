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

`B(Δ)/target` with `Δ_λ = sgn·dim_q(λ)^p`, reusing the precomputed `atom-chi-rust` characters
and validated `y_λ = y_lambda_at(n,q₀)`:

| p | D | T | ³He | ⁴He | A-behaviour |
|---|---|---|---|---|---|
| 1 (irrep `dim`) | 0.18 | 0.30 | 0.40 | 0.21 | **A-bounded** `[0.18,0.40]` |
| 1.5 | 0.42 | 3.3 | 4.7 | 9.3 | grows |
| 2 (block `dim²`) | 1.01 | 39.4 | 59.5 | 449.6 | blows up 40–450× |

## The selection (structural, not a fit)

The physical binding is **A-bounded** (`B/A ~ O(1)` per nucleon), so the magnitude power must
give an **A-bounded** ratio. Only **`p = 1` (the irrep dimension)** does — spread `< 3×` across
the four isotopes — while `p ≥ 1.5` blow up. So the **A-stability criterion selects
`Δ_λ = sgn·dim`** — the **#3542 irrep trace**. This is a criterion on *A-scaling*, independent
of the target magnitude — **not** a fit.

## Consequences

- **The #3542 irrep trace was the right A-scaling all along.** The #3558 block `dim²≈101%` on
  the deuteron was **coincidental** — now doubly confirmed: it both blows up *and* is the wrong
  power by A-stability.
- **The remaining gap is an O(1) multiplicative factor**, not a wrong power. `target/B(dim)`:
  D 5.5, T 3.4, ³He 2.5, ⁴He 4.9 — same power, missing an O(1) coefficient (~2.5–5.5).
- **Combined with the cross-isotope sign validation (#3558):** the picture is
  **`Δ_λ = O(1)·sgn·dim(λ)`**, with the **O(1) coefficient the only remaining unknown** — a
  much sharper open problem than "the magnitude is unknown."

## Open (derive, not fit)

The O(1) coefficient (~2.5–5.5, mildly isotope-varying) is the remaining Track-A step. It must
be **derived** — e.g. from a per-nucleon / color (×3?) / interface structure — not fitted.
Whether it is exactly constant or carries residual A-structure needs the derivation. **Nothing
wired.**

## Cross-references

- Cross-isotope refutation + sign validation: [PR #3558](https://github.com/litlfred/qou/pull/3558)
- g_ρ / sign derivation: [PR #3542](https://github.com/litlfred/qou/pull/3542)
- Reused: `atom-chi-rust-{d,t,3he,4he}.witness.json`, `wedderburn_jones_markov.y_lambda_at`
