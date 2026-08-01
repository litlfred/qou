# Conjugation parity is orthogonal to the A=3 magnitude — an honest negative closing the route

**Date:** 2026-08-01 · **Branch:** `claude/deltalambda-parity-consolidate-a3-magnitude-2026-08-01` ·
**PR:** #4486 · **Axis:** Δ_λ binding — A=3 magnitude gate vs the conjugation-parity structure ·
**Tier:** scope-(a) honest negative (exact `n=9` structure + two orthogonality arguments; **no fit**;
nothing wired).

## Question

GAP-1 (#4399) narrowed the Δ_λ **weight class** via conjugation parity (symmetric `Δ_λ` excluded for
even A ⇒ principal specialization survives). Can the same parity structure constrain the standing A=3
**magnitude** gap — `c₃ = E₀(1 − τ_Borr) = 0.63×μ₃` (`μ₃ = +0.4708`), a `~1.6×` near-miss
(option-e ledger; #4364)?

## Answer — No; parity is orthogonal to the magnitude

**The `n=9` (Borromean, A=3) conjugation structure:** 30 partitions = **14 conjugate pairs + 2
self-conjugate** `{(5,1,1,1,1), (3,3,3)}`, with `sgn = (−1)^{n-1} = +1` — the *opposite* regime from
the deuteron (`n=6`, `sgn=−1`). So at A=3 the self-conjugate blocks feed the bar-**even** channel, and
a conjugation-symmetric `Δ_λ` is **not** excluded (GAP-1 gives no exclusion here).

Two independent reasons parity cannot touch the magnitude:

- **R1 — parity is a relabeling, not a rescaling.** The signed parity map
  `T_λ(q⁻¹) = (−1)^{n-1} T_{λ'}(q)` sorts the H₉ Wedderburn terms into bar-even/bar-odd channels; each
  partition still contributes its **full derived amount**. Parity fixes *which channel* a term lands
  in, never *how big* it is — so it supplies no coefficient, and the `~1.6×` cannot come from parity.
- **R2 — the gap lives at the bare-trace level.** `c₃ = E₀(1 − τ_Borr)` is a *single* Markov trace
  with a proved closed form (`1 − τ_Borr = h⁴(3+h²)/(h²+4)`); the `Δ_λ` per-partition dressing (where
  conjugation parity acts) is a different, downstream object. The `c₃` vs `μ₃` gap is a property of the
  bare trace, which the `Δ_λ` parity structure does not enter.

## Verdict

**The conjugation-parity structure is orthogonal to the A=3 magnitude.** It narrows the *weight class*
(GAP-1) but cannot supply the `~1.6×` coefficient — that remains the standing Track-A magnitude gate
(derived `c₃ = 0.297` vs `μ₃ = +0.4708`). This closes the "use parity for the magnitude" route so
future sessions do not re-try it.

| statement | status |
|---|---|
| `n=9` structure: 14 conjugate pairs + 2 self-conjugate, `sgn=+1` | **exact** |
| parity relabels, does not rescale (R1); gap is bare-trace (R2) | **argued** |
| parity constrains the A=3 magnitude | **refuted (scope-(a) negative)** |
| the A=3 magnitude `~1.6×` coefficient | **OPEN — Track-A gate** (unchanged) |

Refs: probe
[`a3_magnitude_parity_orthogonal_probe.py`](../../computations/deltalambda/a3_magnitude_parity_orthogonal_probe.py);
option-e ledger (A=3 magnitude, `μ₃`); #4399 (GAP-1 weight-class exclusion); #4481 (Milnor convergence).
