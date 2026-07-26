# `r = g₂ − 1` is the deuteron binding residual magnified by `1/h²` — the decisive terminus of the g₂ chase

**Date:** 2026-07-26 · **Branch:** `claude/geometric-qdilog-amplitude-r-2026-07-26` ·
**Axis:** Δ_λ binding — μ₀ −9% closure, the exact residual `r = g₂ − 1` · **Owner steer:** *"keep
pushing"* · **Tier:** exact affine/amplification structure (Lean-proved) reproducing the corpus `g₂`;
precision-requirement derivation (**scope-(a); no fit; no AME inversion**; nothing wired).

## 0. What "keep pushing" surfaced

The prior step (#4369) refuted the eigenspace-shape lifted dilog (`r ≈ −2.1%`, wrong sign) and proved
the four-shape octahedron degenerates at the pinch. Pushing further — into **how the corpus actually
defines `g₂`** — resolves the whole chase. The answer is not another amplitude; it is that **`r` is
not a separable special-function quantity at all.**

## 1. The definition of `g₂` (Magnus/E_unit route, #4158)

The bar-even coefficient is *defined*
([`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md),
`eunit_magnus_order2_probe.py`) as

$$g_2 = \frac{E_{\text{AME}}/E^{+} - 1}{h^2}, \qquad E^{+} = \frac{E_{\text{rot}}}{1 - t},$$

with every ingredient **except one** a pure function of the substrate `q₀`:

| symbol | value | nature |
|---|---|---|
| `E_rot = μ₀ ℏ_q [j]_q[j+1]_q` (j=3) | `2.0195829` MeV | **pure theory** |
| `t = (v−v⁻¹)/[2]_v`, `v=√q₀` | `0.0521` | **pure theory** (bar-odd impurity) |
| `h = q−q⁻¹` | `0.2091` | **pure theory** |
| `E_AME` | `2.2245662` MeV | **measured** (deuteron binding) |

Plugging in reproduces the corpus value **exactly**: `g₂ = 1.0086522`, `r = +0.8652%`. So the
bookkeeping is confirmed — this *is* the corpus's `g₂`.

## 2. `g₂` is an affine image of the measured binding — amplification `≈ 23.9`

Since `E⁺` and `h` are pure theory, `g₂` is an **affine function of the measured binding `E_AME`**:

$$g_2 = E_{\text{AME}}\cdot\frac{1}{E^{+}h^2} - \frac{1}{h^2}, \qquad \frac{\partial g_2}{\partial (E_{\text{AME}}/E_{\text{AME}})} = \frac{E_{\text{AME}}}{E^{+}h^2} \approx 23.9.$$

Machine-checked sorry-free (`Field` identity, §7c):
[`BindingResidualAmplification.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BindingResidualAmplification.lean)
(`g2_affine`, `g2_amplification`, `r_amplification`). The `1/h²` **magnifies** the binding's relative
error by `≈ 24×`.

## 3. The precision consequence — `r` is a 36-ppm slice of the binding

| to resolve | required precision on `B(deuteron)` |
|---|---|
| distinguish `g₂ = 1.0087` from `g₂ = 1` (see `r` at all) | `≈ 362 ppm` |
| pin `r` to `10%` | `≈ 36 ppm` |
| framework's **current** first-order accuracy (`−9.21%`) | `92100 ppm` |

Pinning `r` to `10%` needs the deuteron binding predicted **`~2540×` tighter** than the framework can
currently manage. Worse, `r` sits **below the tabulated input floor**: rounding `E_rot` to its
displayed `2.0196` MeV (a `10⁻⁴` MeV rounding) already shifts `g₂` by **`2.3%` of `r`**.

## 4. Verdict — the decisive reframing

**`r = g₂ − 1` is not a special-function puzzle separable from the binding.** Because `g₂` is affine
in the measured `E_AME`, **deriving `r` is *equivalent to* predicting the deuteron binding energy to
`~36 ppm`** — i.e. `r` **is** the Δ_λ deuteron-binding closure (the Track A blocker), viewed through a
`1/h²` magnifier. This explains the entire four-session g₂ saga at a stroke:

- **Why every principled amplitude gives `g₂ ≈ 1`** (cosh channel `9/8`; Rogers dilog `0`; lifted
  dilog `0.979`; ladder units; `2(cosh 2θ−1)=h²`): they all reproduce the **derived leading term**
  `g₂_leading = 1` (#4339, real coloring, exact). None pins `r` because `r` is the *binding residual*,
  which the framework does not predict at `36 ppm`.
- **Why the §2e entropy warning was right, quantified:** a `~36 ppm` target carries essentially zero
  information to fit a special function against. The search was chasing a magnified image of the
  unclosed binding.

| statement | status |
|---|---|
| `g₂ = (E_AME/E⁺−1)/h²` reproduces the corpus `1.00865` (bookkeeping) | **exact, confirmed** |
| `g₂` affine in the measured binding, amplification `≈ 23.9` | **Lean-proved sorry-free** |
| deriving `r` ⇔ predicting `B(deuteron)` to `~36 ppm` (`~2540×` current) | **derived** |
| `g₂_leading = 1` | **derived, exact** (#4339) |
| the exact `r = +0.87%` | **OPEN = the Δ_λ deuteron closure at `~36 ppm`**, not a separable amplitude |

**Recommendation.** Formally **pause the `g₂`/`r` chase.** `g₂_leading = 1` is derived and banked; the
residual `r` reduces to the general Δ_λ binding-energy closure (open-for-all per the 2026-07-13
reversal) at a precision `~2500×` beyond current reach. Future effort on `r` should be effort on the
deuteron binding-energy prediction itself, not on special-function amplitudes for a `36 ppm` residual.

Refs: probe
[`deuteron_r_is_binding_residual_probe.py`](../../computations/deltalambda/deuteron_r_is_binding_residual_probe.py);
Lean [`BindingResidualAmplification.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BindingResidualAmplification.lean);
`g₂` definition [`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md); #4369
(lifted-dilog refutation + pinch degeneracy); #4339 (`g₂_leading=1`); #4347 (frontier).
