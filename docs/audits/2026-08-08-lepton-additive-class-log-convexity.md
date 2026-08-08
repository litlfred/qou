# The additive bridge is log-convex — the last shape closes, and only one escape remains

**Date:** 2026-08-08
**Branch:** `claude/agent-pr-4690-stall-s9f5rt` (PR #4714)
**Bean:** `qou-htk4`
**Status:** scope-(b) for positive two-mode additive towers, on a strict
inequality. Sorry-free Lean, `lean`-direct exit 0.

## What was left open

The bend screen ([`2026-08-07-lepton-tower-bend-screening.md`](2026-08-07-lepton-tower-bend-screening.md),
PR #4704) covered the **multiplicative** class `m_w = C·g^w·f(w)^p`, and its
scope note said explicitly:

> **Out of scope entirely** — non-multiplicative bridges. An additive
> interface term is not of the form `C g^w f^p`, so this tool says nothing
> about it.

That was the honest boundary of that result, and it was the last live shape on
`qou-htk4`. It is now closed, by a sharper argument than the one it replaces.

## The result

An additive bridge means the tower is a **sum of geometric modes** — a base
term plus an interface term:

```
  x(w) = c·g^w + d·h^w,      c, d ≥ 0,   g, h > 0.
```

Such a tower is **log-convex**. The sqrt-free Lagrange form of Cauchy–Schwarz
gives the deficit as a perfect square:

```
  x(w)·x(w+4) − x(w+2)²  =  c·d·g^w·h^w·(g² − h²)²  ≥  0
```

hence `bend ≤ 1`. The observed lepton bend is `m_μ²/(m_e·m_τ) ≈ 12.295` — it is
log-**concave**, bending the *other* way. No such tower reproduces the lepton
spectrum, for any coefficients and any rates.

## Why this one is sharp

The multiplicative screen ruled candidates out by *how large* an exponent they
would need — `p = 64.9` for the Markov trace, `8.72` at best — and that is a
judgement at the margin, labelled as such in both the audit and the witness.

This is a strict inequality with **no free parameter left to argue about**:
`bend ≤ 1` versus a measured `12.295`. `not_two_positive_modes_of_bend_gt_one`
states it in contrapositive form, which is how it will actually be used.

Because the deficit is a perfect square, the equality cases are exact: the bend
touches `1` **only** when `g = h` (really one mode) or when a coefficient
vanishes. Positive two-mode towers are otherwise strictly log-convex.

## Three assertions that caught my own errors

The probe's assertions failed on first run — all three were test-design errors
of mine rather than errors in the mathematics, and one was a claim I had
already written into the docstring:

1. **Rounding headroom.** The Lagrange identity is exact, but forming the bend
   as a quotient rounds, so the degenerate single-mode cases land at `1 ± ε`
   and a bare `≤ 1` test fails. Fixed with an explicit tolerance, and the
   excess is now reported rather than hidden.

2. **A real over-claim.** I asserted that turning on a second positive mode
   *monotonically* worsens the bend. **It does not.** Measured, the bend dips
   to an interior minimum (`≈ 0.967` at `d ≈ 1` for the `q`/`q⁻¹` pair) and
   returns to `1` as `d → ∞`, where the second mode simply takes over and the
   tower is single-mode again:

   | `d` | 0 | 0.01 | 0.1 | 1 | 10 | 1000 |
   |---|---|---|---|---|---|---|
   | bend | 1.0 | 0.99938 | 0.99422 | 0.96708 | 0.97046 | 0.99950 |

   The correct statement is the bound together with its equality cases, not a
   monotonicity. The docstring now says so, and says that it was wrong.

3. **The escape was probed in the wrong place.** I tested sign-indefinite
   combinations at `d ≈ −1`, nowhere near the node. For `(c, g, h) = (1, q, q⁻¹)`
   the node in `d` sits at `−q⁶ = −1.8702`, since `x(w) = q^w + d·q^{−w}`
   vanishes there. Approached correctly:

   | `d` | −1.5 | −1.8 | −1.86 | −1.87 |
   |---|---|---|---|---|
   | `x(3)` | 0.2707 | 0.05133 | 0.007457 | 0.0001448 |
   | bend | 1.72 | 6.13 | 38.4 | **1943** |

   The escape is real, and it is now demonstrated at the place where it lives.

## Honest scope

- **Scope-(b)** — positive two-mode additive towers, on the Lagrange identity.
  A strict inequality, not a failed search and not a plausibility judgement.
- **Not claimed: more than two modes.** The same identity generalises by
  symmetrising over pairs — `Σᵢⱼ cᵢcⱼ gᵢ^w gⱼ^w (gᵢ² − gⱼ²)² ≥ 0` — but that is
  **not formalised here**, and is not being waved through. Filed as the
  remaining formalisation gap.
- **Not claimed: sign-indefinite combinations.** They escape, demonstrated
  above.

## The one shape left standing

Sign-indefiniteness now escapes **all three** exclusions, always by the same
mechanism — a node:

| exclusion | what it covers | how sign-indefiniteness escapes |
|---|---|---|
| linear readouts of `H₂(q)` (`qou-lsp9`) | every *positive* `(α, β)` | `α`, `β` of opposite sign put a node in the window |
| multiplicative `C g^w f^p` (`qou-htk4`, #4704) | every geometric / polynomial readout | a readout with a node has unbounded ratios |
| additive `c g^w + d h^w` (this) | every *positive* `c, d` | `d < 0` breaks Cauchy–Schwarz, node at `d = −q^{2w}` |

That convergence is the useful output of this tranche. Every route into the
lepton tower that has been closed was closed by positivity, and every route
that survives does so by having a zero in or near the generation window. Any
future candidate bridge should be checked for a node **first** — it is the only
place the freedom to bend the tower has ever been found.

Whether a node is *physically* available is a separate question this line of
work has not touched: it would require a readout in which the electron sits
near a genuine zero of the underlying quantity, which is a strong and testable
structural claim rather than a fitting knob.

## Artifacts

- **Lean (sorry-free, `lean`-direct exit 0):** `lepton_tower_log_convexity.lean`
  in [QOU/Archimedean/](../../content/quantum-observable-universe/lean/QOU/Archimedean)
  — `twoMode_log_convex`, `bend_le_one_of_two_positive_modes`,
  `not_two_positive_modes_of_bend_gt_one`. Generic ordered field; no `ℝ`, no
  `Real.sqrt`, so §7c-generic.
- **Probe:** [`lepton_tower_additive_screening.py`](../../computations/lepton_tower_additive_screening.py)
  → `lepton-tower-additive-screening.witness.json`. 65 dps, proton pin.
  Identity to 8.6e-49; 40 000-tower positive sweep, max bend `1.0`.
