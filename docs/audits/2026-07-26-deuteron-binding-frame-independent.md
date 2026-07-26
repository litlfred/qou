# B(deuteron), frame-independent — the total correction `C = B/E₀`, honest accuracy `~0.5%`, and why `g₂`'s precision was frame-flattered

**Date:** 2026-07-26 · **Branch:** `claude/geometric-qdilog-amplitude-r-2026-07-26` ·
**Axis:** Δ_λ binding — μ₀ −9% closure, frame-independent `B(deuteron)` · **Owner steer:**
*"B(deuteron) in a frame-independent formulation"* · **Tier:** frame-invariant reformulation +
motivated-form accuracy spread + Lean-proved `O(t²)` frame ambiguity (**scope-(a); no fit**; nothing
wired).

## 0. The move

The prior audit showed `r = g₂ − 1` is a frame artifact (`12×` convention spread). The fix the owner
asked for: drop the frame-dependent tier split entirely and state `B(deuteron)` as a single
frame-invariant object with a well-defined accuracy.

## 1. The frame-invariant object

$$B(\text{deuteron}) = E_0 \cdot C(q_0), \qquad E_0 = \mu_0\,\hbar_q\,[3]_q[4]_q,$$

the naive q-deformed rotational Casimir (`μ₀ = 2m_e/(3h)`, `ℏ_q = 1−q⁻¹`, `[n]_q = (qⁿ−q⁻ⁿ)/(q−q⁻¹)`).
Numerically `E₀ = 2.0195829` MeV (`−9.215%` vs AME `2.2245662`). The **total correction**

$$C \equiv \frac{B}{E_0} = 1.1014978$$

is the single **frame-invariant** number the framework must predict. It carries **no `g₂`, no `t`** —
those are frame-dependent decompositions *of* `C`. (Equivalently `B/μ₀ = 1.3652`.)

## 2. A clean parameter-free closed form

Since `ℏ_q·q = q−1` exactly, the bar-conjugate of `ℏ_q` gives a single closed form with no
convention:

$$B(\text{deuteron}) \approx \mu_0\,(q-1)\,[3]_q[4]_q, \qquad \text{err } +0.77\%.$$

## 3. The honest frame-independent accuracy is `~0.5%`, not `0.036%`

Motivated single closed forms for `C`, and their errors on `B`:

| form for `C` | story | err on `B` |
|---|---|---|
| `1` | naive q-Casimir | `−9.215%` |
| `1 + t + h²` | `O(h²)` additive | `−0.515%` |
| `(1+t)(1+h²)` | `O(h²)` factored | `−0.308%` |
| `exp(t)(1+h²)` | exp bar-odd | `−0.177%` |
| `1/((1−t)(1−h²))` | both resummed | `+0.155%` |
| `1/(1−t)·(1+h²)` | **corpus** resummed | `−0.036%` |
| `q`  (`ℏ_q→q−1`) | bar-conjugate | `+0.770%` |

The motivated-form error **spread is `[−0.51%, +0.77%]`**. All frames agree through **first order in
`t` (= `O(h)`)**; the `~0.5%` residual is the frame/resummation-dependent tail. The headline `0.036%`
needs the *specific* `(1+h²)/(1−t)` resummation — and competing resummations differ at exactly
**`O(t²) = O(h²)`**, the *same order as the entire bar-even signal `g₂h²`*:

$$\frac{1}{1-t} - (1+t) = \frac{t^2}{1-t}.$$

Machine-checked sorry-free (`Field`, §7c):
[`FrameAmbiguitySecondOrder.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/FrameAmbiguitySecondOrder.lean)
(`frame_diff_second_order`, `g_frame_difference`). So `0.036%` and the coefficient `g₂ = 1.0087` are
**resummation-flattered** — one frame's residual, not a frame-independent accuracy.

## 4. Verdict

| statement | status |
|---|---|
| frame-invariant object: `C = B/E₀ = 1.1015` (no tier split) | **well-posed** |
| clean form `B ≈ μ₀(q−1)[3]_q[4]_q` (`ℏ_q→q−1`) | **derived, +0.77%** |
| `B(deuteron)` predicted parameter-free to `~0.5%` (`20×` over the naive `9.2%`), controlled at `O(h)` | **derived, robust** |
| `0.036%` accuracy / `g₂ = 1.0087` as genuine precision | **false** — resummation-flattered (`O(h²)` frame ambiguity, Lean-proved) |
| the real open target | predict `C = 1.1015` **below `~0.5%`** by a *derived* higher-order structure (not a chosen resummation) = the Δ_λ closure, frame-independently |

**The honest headline:** the framework predicts the deuteron binding **parameter-free to `~0.5%`** — a
genuine `~20×` improvement over the naive q-Casimir, and a real, frame-independent success. What it
does **not** deliver is the `0.036%` / `g₂ = 1.0087` sub-`0.1%` precision: that is one resummation's
frame-flattered residual, and the `r`-chase was chasing that flattering. The well-posed way forward is
to predict the frame-invariant `C` below `~0.5%` from *derived* higher-order structure — the Δ_λ
closure stated on `C`, not on `g₂`.

## 5. Can `C` have a closed form for all orders? — the base already does; `C` is a single number

A structural clarification on "all orders":

- **The rotational base `E₀ = μ₀ℏ_q[3]_q[4]_q` is already an exact all-orders closed form.** The
  q-integers `[n]_q` resum the entire `h`-expansion of the q-deformed Casimir exactly — there is no
  order-by-order tail on the base.
- **There is no Magnus tower to resum.** For the deuteron word `σ₁³` (a *single* braid generator)
  every commutator `[a,a] = 0`, so `Ω_{k≥2} = 0` exactly (#4158). The "higher orders" of `C` are
  therefore **not** a dynamical series — `C = B/E₀ = 1.10150` is a **single number**, the
  frame-projection / many-body binding residual on top of the exact q-Casimir.
- **No elementary closed form is exact.** Structurally-motivated forms cluster at `0.04–0.8%`
  (`C ≈ q`: `+0.77%`; `C ≈ (1+h²)/(1−t)`: `−0.036%`, frame-flattered); ratios of neighbouring
  q-Casimirs `[j+1]_q/[j]_q` miss by `6–23%`. Scanning special functions for a sub-`0.05%` hit is the
  §2e-forbidden fit and is refused.

So "closed form for all orders" splits cleanly: **yes** for the base (exact q-Casimir), and the
correction `C` is a single number whose *exact* closed form would **be** the Δ_λ many-body binding
closure — not an elementary resummation. The categorical target is therefore to derive `C` from
`tr_M = Σ_λ y_λ χ^λ` (the Frobenius-paired Markov trace over the two Wedderburn blocks `(2)`, `(1,1)`
of the `p`–`n` channel), where the bar-odd eigenvalue structure (`tr σ₁³ = q³−q⁻³`, purely bar-odd)
is dressed by the bar-even Markov weights `y_λ` — the frame-independent home of the `~0.5%` residual.

Refs: probe
[`deuteron_binding_frame_independent_probe.py`](../../computations/deltalambda/deuteron_binding_frame_independent_probe.py);
Lean [`FrameAmbiguitySecondOrder.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/FrameAmbiguitySecondOrder.lean);
#4369 (`r` = frame artifact / binding residual magnified `1/h²`); `g₂` tier definition
[`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md).
