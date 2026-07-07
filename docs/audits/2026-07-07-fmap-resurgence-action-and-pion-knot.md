# The f-map's resurgence action + the even-channel knot is the pion (half-figure-eight)

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone (resurgence + knot id)
· **Tier:** structural-exact (knot id, volumes, sign obstruction) + preliminary-numerical (action A)
· **Discipline:** no fit, no c_k value, no wiring, no tier change. Scope-(a)/(b) classified.

Follow-up to [PR #3474](https://github.com/litlfred/qou/pull/3474) (the f-map is the
resurgence connection, not a coefficient re-basing). Answers two session questions:
**(1) compute the resurgence Stokes datum**, and **(2) identify the even-channel
knot** — plus the *"do we need na-Stokes?"* question.

## Task 1 — the resurgence instanton action A (the f-map's Stokes datum)

The f-map connects the trivial-connection perturbative series (the c_k) to the
geometric-connection Ohtsuki series (κ_k). Its content is the **instanton action
A** = the gap between the two saddle actions, read from the large-order growth
`κ_n ~ C·Γ(n+β)/A^n ⇒ κ_{n+1}/κ_n ~ n/A`. Probe
[`qbeta_resurgence_action_halffig8.py`](scripts/qbeta_resurgence_action_halffig8.py)
(6/6, dps 100) computes the 4₁ Ohtsuki ladder to order 6 (Vol recovered to rel
`2.4×10⁻¹⁸`): `κ = (0.554, 0.731, 2.655, 13.10, 83.88, 788.27)` — factorially
growing (divergent, as required).

Per-order action estimates `A_n = n·κ_n/κ_{n+1}`:
`0.758, 0.551, 0.608, 0.625, 0.532`. **These oscillate** rather than converge —
the signature of a **complex / paired action** (the `±Vol` conjugate geometric
connections, `𝔙 = Vol ± iCS`). Magnitude `|A| ≈ 0.5–0.6`, **near
`Λ(π/3) = Vol(4₁)/4 ≈ 0.507`** but **NOT established** — 6 orders is far short of
the ~20 orders / Borel–Padé needed to pin it. Recorded as **preliminary**.

**This is genuine progress on the object, not the value:** A *is* the f-map (the
Stokes datum), it is `O(Vol/2π)`-scale, and its oscillation already tells us the
action is complex — consistent with the complex volume `𝔙`, not a real number.

## Task 2 — the even-channel knot is the pion = half-figure-eight

Corpus ([`pion-half-figure-eight.md`](../../content/quantum-observable-universe/braids-and-knots/pion-half-figure-eight.md)):
the pion braid `𝔐₊ = (σ₁σ₂)²σ₂σ₁ ≡ σ₁σ₂⁻¹` (the half-figure-eight), and **the
figure-eight operator `(σ₁σ₂⁻¹)²` is the *square* of the pion rotation.** So the
even channel (cosh / CAL-3 / meson) sits at **half** the figure-eight action,
`Vol(4₁)/2 = 1.0149`, and the 4₁ prefactor `3^(−1/4)` square-rooted lands the even
channel in **ℚ(√3)** — matching the measured `e₁ = 3√3/4`. The prior one-scale
test used the *square* (full 4₁), the wrong object.

**But a knot-independent sign obstruction settles it.** The 4₁ Ohtsuki κ_k are all
**positive** (`+,+,+,+`); the half-ladder `κ/2` (since `4₁ = (half)²` ⇒
`log J^half = ½ log J^full`) is also all positive. The even-channel rungs e_k have
signs `(+,−,−,−)`. A real one-scale re-basing `κ_k·λ^k` **cannot flip sign
per-rung** (`κ_k > 0 ⇒ κ_k·λ^k > 0` for every real λ), so **neither the full nor
the half knot re-bases to the even channel.** The correct-knot identification
sharpens the geometry (√3, the square relationship) but does **not** rescue
re-basing — reinforcing that the f-map is resurgence, not a coefficient map.

## "Do we need na-Stokes?" — no for the compute, yes as the fibre origin

Two distinct "Stokes":

| | **non-abelian Stokes** (Yekutieli) | **resurgence Stokes** (Garoufalidis–Gu–Mariño) |
|---|---|---|
| statement | holonomy = surface-ordered curvature integral | Borel resummation jumps across Stokes rays |
| role in chain | builds `𝐂 → H_n(q)` (the fibre braiding) | connects perturbative series across saddles |
| object | the categorical connection | the instanton action A + Stokes constant |

The numerical action A (Task 1) needs **resurgence** Stokes (Borel / large-order),
**not** the non-abelian Stokes theorem. But the two are linked at the level of
**flat connections**: the resurgence saddles (trivial + geometric) are exactly the
flat connections whose holonomies the non-abelian Stokes theorem constructs. And
suggestively, the Yekutieli classes are also written **`κ_n ≠ 0`** and are
"non-vanishing at every level" (perpetual obstruction —
[`archimedean-yekutieli.md`](../../content/quantum-observable-universe/brings-surface/archimedean-yekutieli.md))
— structurally parallel to the *divergent* resurgence κ_k (never vanishing).
**Hypothesis (not a claim):** the Yekutieli non-abelian-Stokes obstruction is the
**fibre-side origin** of the divergent resurgence series — i.e. na-Stokes is why
the two saddles exist, resurgence Stokes is how their series connect. So: not
needed to *compute* A; plausibly needed to *explain* why the resurgence structure
is there at all.

## Bottom line

- The f-map's actual content is the **resurgence instanton action A** (`|A| ≈ 0.5`,
  complex/oscillating, near Vol/4 — **preliminary**, needs Borel–Padé).
- The even-channel knot is the **pion = half-figure-eight** (`4₁ = its square`),
  explaining the √3; but a **knot-independent sign obstruction** confirms the
  f-map is not a re-basing for any knot.
- **na-Stokes** is not needed for the numerical A, but is the plausible fibre
  origin of the two resurgence saddles.

Concrete next step: extend the 4₁ Ohtsuki ladder to ~20 orders + Borel–Padé to
pin A (and confirm/deny the `Vol/4` / complex-`𝔙` reading).

## Cross-references

- Probe: [`qbeta_resurgence_action_halffig8.py`](scripts/qbeta_resurgence_action_halffig8.py)
- Prior (f-map = resurgence): [2026-07-07 c_3-even / S rigidity](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)
- Pion knot: [`pion-half-figure-eight.md`](../../content/quantum-observable-universe/braids-and-knots/pion-half-figure-eight.md)
- na-Stokes: [`archimedean-yekutieli.md`](../../content/quantum-observable-universe/brings-surface/archimedean-yekutieli.md)
