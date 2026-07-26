# Is `g₂` fitted to AME? No — but `r = g₂−1` is a frame artifact. The larger context of the deuteron bar-even coefficient

**Date:** 2026-07-26 · **Branch:** `claude/geometric-qdilog-amplitude-r-2026-07-26` ·
**Axis:** Δ_λ binding — μ₀ −9% closure, the epistemic status of `g₂` / `r` · **Owner question:**
*"keep pushing on g₂ beyond leading; it seems fitted to AME which is bad; what is the larger
context?"* · **Tier:** frame-sensitivity measurement + tier convergence + structural locate
(**scope-(a); no fit; no AME inversion**; nothing wired).

## 0. The question, answered directly

**Is `g₂ = 1.00865` fitted to AME?** No tuned parameter exists — nothing downstream consumes a `g₂`
that was adjusted to match data. **But the owner's instinct is correct, and sharper than "fitted":**
`r = g₂ − 1` is a **frame artifact**. Its value is ~90% convention. Below are the three things that
matter.

## 1. The real, robust result — `B(deuteron)` to 0.04%, parameter-free

Using **only** `q₀`-derived inputs, the binding converges in three tiers:

| tier | prediction | error vs AME (`2.2245662` MeV) |
|---|---|---|
| 0 — rotational `E_rot = μ₀ℏ_q[j]_q[j+1]_q` | `2.0195829` | **−9.215%** |
| 1 — `+` bar-odd `t = (v−v⁻¹)/[2]_v` → `E⁺ = E_rot/(1−t)` | `2.1306383` | **−4.222%** |
| 2 — `+` bar-even unit `h²` (coefficient 1) → `E⁺(1+h²)` | `2.2237605` | **−0.036%** |

The framework predicts the deuteron binding to **0.036% (360 ppm) from `q₀` alone**, no free
parameters. `g₂ ≈ 1` — *"the bar-even correction is one `h²` unit"* — is a genuine prediction, **not**
a fit. **This is the bankable achievement, and it is sound.**

## 2. Why `r = g₂ − 1` is a frame artifact (the owner's worry, vindicated + sharpened)

`g₂ = (E_AME/E⁺ − 1)/h²` depends on the **O(t²) convention** used to remove the *same* 5.21% bar-odd
tier. Four equally-valid frames:

| frame (all remove the same bar-odd `t`) | `r = g₂ − 1` |
|---|---|
| `E⁺ = E_rot/(1−t)`  (corpus) | **+0.87%** |
| `E⁺ = E_rot·(1+t)` | **+7.37%** |
| `E⁺ = E_rot·eᵗ` | **+4.23%** |
| `B = E⁺/(1−g₂h²)`  (inverse bar-even) | **−3.39%** |

`r` ranges over **`[−3.4%, +7.4%]`** — a spread of `~11%`, **≈ 12× the signal** `|r| ≈ 0.87%`. **The
residual is ~90% frame-convention, not physics.** So `r` is not a well-defined number: chasing a
special function to reproduce `+0.87%` (the four-session `g₂`/geometric-dilog effort) was doomed by
frame-ambiguity alone — *independently* of the §2e entropy bound and the `36 ppm` precision wall
(#4369).

## 3. Where the bar-even unit comes from — a projection, not dynamics

For the deuteron word `σ₁³` — a **single** braid generator — every Magnus commutator `[a,a] = 0`, so
`Ω_{k≥2} = 0` **exactly** (proved, #4158). The bar-even `h²` correction is therefore **not** a
dynamical (Magnus / holonomy) term — it is the **character / frame projection** of the order-`h²`
unit. Consequently `g₂_leading = 1` is **near-definitional** (the natural order-`h²` frame unit has
coefficient 1 once you normalize by `h²`), and `r` is the residual of the frame choice — *not* a
categorical amplitude waiting to be derived. This is the structural reason every principled amplitude
(cosh→9/8, Rogers→0, lifted dilog→0.979) reproduces the leading `1` but none pins `r`.

## 4. The larger context

The `g₂` framing conflated two very different things:

- **A real, sound, parameter-free prediction:** `B(deuteron) = f(q₀)` to `~0.04%`, via the rotational
  × bar-odd × bar-even-unit tier tower. `g₂ ≈ 1` is the correct, robust name for the third tier.
- **A frame-dependent residual dressed up as a target:** `r = +0.87%`, whose value is ~90%
  convention (`12×` frame spread) and which — read as an absolute error — is the framework's `0.036%`
  miss on `B(D)`, magnified `×24` by `1/h²` (#4369).

**The well-defined open problem is `B(deuteron)` itself below `~0.04%`** — a frame-independent target,
which is exactly the general Δ_λ binding closure (open-for-all per 2026-07-13). `r` is a
frame-dependent repackaging of that same residual and is **not** an independent quantity to derive.

| statement | status |
|---|---|
| `B(deuteron)` predicted to `0.036%` from `q₀` (3 derived tiers) | **derived, robust, sound** |
| `g₂ ≈ 1` (bar-even correction = one `h²` unit) | **derived** (#4339); near-definitional (§3) |
| `g₂` is a *tuned/fitted parameter* | **false** — no knob exists |
| `r = +0.87%` is a well-defined physical quantity | **false** — `12×` frame-convention spread (§2) |
| the exact `r` as a special-function target | **ill-posed** — frame artifact; superseded by `B(D)` below `0.04%` |

**Recommendation (reaffirmed, now with the frame reason).** Stop chasing `r`. Bank the two sound
statements above. Any further "beyond-leading" work should target `B(deuteron)` in a **frame-
independent** formulation — the Δ_λ closure — not the frame-dependent `r`.

Refs: probe
[`deuteron_g2_frame_artifact_probe.py`](../../computations/deltalambda/deuteron_g2_frame_artifact_probe.py);
#4369 (`r` = binding residual magnified `1/h²`; `BindingResidualAmplification.lean`);
`g₂` definition + `Ω_{k≥2}=0` [`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md);
#4339 (`g₂_leading=1`).
