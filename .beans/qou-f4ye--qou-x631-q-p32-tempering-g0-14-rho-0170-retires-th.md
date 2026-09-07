---
# qou-f4ye
title: 'qou-x631: Q ~ P^{3/2} tempering; g''(0) -> -1/4; rho -> -0.170 retires the -1/(2pi) coincidence'
status: done
type: task
created_at: 2026-09-07T08:17:41Z
updated_at: 2026-09-07T08:17:41Z
---


Follows `qou-h4fe`. Three results, one of which **retires a constant I recorded
myself** two rounds earlier.

## The reframing: this is tempering

Since `P(λ) = (f^λ)²/k!`, the tilt family is exactly a power of Plancherel:

    Q_t ∝ P^{1+t/2},   so   Q ∝ P^{3/2}.

The conjecture, stated plainly: **sharpening the Plancherel measure toward its
mode makes `E[Σ₃]` negative.**

## g'(0) converges, apparently to −1/4

| k | 16 | 24 | 32 | 40 | 44 | 48 |
|---|---|---|---|---|---|---|
| g'(0) | −0.2318 | −0.2379 | −0.2427 | −0.2462 | −0.2469 | −0.2483 |

Monotone from below, with successive differences −0.0060, −0.0049, −0.0035,
−0.0007, −0.0014 — **decaying**, so this is convergence, not the drift I worried
about. Last round I gave −0.245 as a target; it is better read as approaching
−1/4.

**−1/4 is a target to check a derivation against, never a criterion to search
on.** The data is consistent with it and does not establish it.

## ρ tightens to −0.170 — and that retires `−1/(2π)`

At the same k, ρ = g(1) is −0.1732, −0.1691, −0.1714, −0.1733, −0.1666, −0.1694
— oscillating, no trend, **−0.170 ± 0.004**.

`qou-ujil` recorded a coincidence: the `k^{3/2}` coefficient looked like
`√3/(2π)`, equivalently `ρ → −1/(2π) = −0.15915`. It was quarantined explicitly
as *"a target to check a future derivation against, never a criterion to search
on"*. **The check now fails**: −0.15915 is 6.8 % from −0.170, outside the
tightened bar. Treat `−1/(2π)` as **disfavoured**.

This is the quarantine working as designed. Had that constant been fitted to
rather than merely recorded, three rounds of subsequent work would have been
aimed at the wrong number — and the failure would have surfaced only after a
derivation was built around it.

## The correlation *coefficient* decays; only the product is O(1)

| k | 12 | 20 | 28 | 36 | 40 |
|---|---|---|---|---|---|
| `sd_P(log f)` | 0.492 | 0.568 | 0.635 | 0.689 | 0.712 |
| `corr(log f, Σ₃)` | −0.450 | −0.404 | −0.374 | −0.352 | −0.346 |

`sd_P(log f^λ)` **grows** and the correlation coefficient **decays**, their
product `g'(0) = corr · sd_P(log f)` staying near −1/4.

This refines `qou-ujil`, which called the effect *"an O(1) correlation"*. That is
right in units of `sd(Σ₃)` and **wrong as a statement about the correlation
coefficient**, which is o(1). A method assuming `log f^λ` has bounded
fluctuations, or that the two observables stay comparably correlated, is assuming
something false.

## Standing targets after this round

- `g'(0) → −1/4` (quarantined), the Plancherel linear-response coefficient.
- `ρ = g(1) ≈ −0.170`, the conjecture's constant. No candidate closed form; the
  one that existed is now disfavoured.
