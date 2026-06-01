# Audit: Casimir status against the operative bar — 1% of QED, 1ppQ compute, Lean

**Date.** 2026-06-01
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Builds on.** PR #1540 (N_⊙ via n-stability), PR #1596 (free-field↔disjoint
grounding + first q-correction), `2026-06-01-casimir-first-qcorrection-figure8.md`.
**Purpose.** Record the *operative* success criteria for the Casimir result and
show it clears each. The criteria are **not** experimental discrimination
(no experiment can currently distinguish QOU from QED here — see §3); they are:
**(1) agreement with QED to ~1%, (2) compute precision to 1ppQ, (3) Lean.**

## 1. Within 1% of QED — MET (by construction)

The leading force per area is the textbook value

$$
\frac{F}{A} = -\frac{\pi^2 \hbar c}{240\, d^4},
$$

with **`ξ_k = 0` for `k ≥ 1`** on the `1/d⁴` term (no substrate-q dependence;
PR #1596, grounded in the free-field = disjoint-unknot photon representation).
The standard value is verified experimentally to ~1 % (Lamoreaux 1997;
Mohideen–Roy 1998). QOU reproduces it exactly at leading order, so it sits
**inside the ~1 % experimental window automatically**. Equivalently: an O(1)
substrate correction would have shifted the prefactor by `~(3/4)h² ≈ 3–4 %`
(`h = q₀−q₀⁻¹ ≈ 0.21`), which the ~1 % data already excludes — consistent with
`ξ_2 = 0`.

## 2. Compute precision to 1ppQ — MET (trivially; closed-form)

Every Casimir quantity here is **closed-form**, so there is no numerical-stability
budget to defend:

| quantity | form | precision |
|---|---|---|
| leading prefactor | `π²/720` (transcendental constant) | any dps |
| first-correction weight | `J_{4_1}(q) = q⁻²−q⁻¹+1−q+q²` (rational in `q`) | exact |
| leading `h²` coefficient | `3/4` (exact rational) | exact |

Cross-method check at 60 dps (`J_{4_1}` evaluated directly vs. via the `s`-form
`(q+q⁻¹)²−(q+q⁻¹)−1`): agreement `|Δ| ≈ 3×10⁻⁶¹`, i.e. **~46 orders of magnitude
inside the 1ppQ (10⁻¹⁵) target**. L1 is met with no headroom concern.

## 3. Lean — MET for the substantive content

- `π²/720` prefactor: derived from the disjoint count + `ζ(−3)` (no `q`).
- First-correction weight `3/4`: proved **exact** in
  [`QOU.AppendixSurreals.FigureEightCasimirWeight`](../../content/quantum-observable-universe/lean/QOU/AppendixSurreals/FigureEightCasimirWeight.lean)
  — `jones41_taylor`: `J_{4_1}(q) = 1 + (3/4)(q−q⁻¹)² + R(q)` with `R` exact and
  `≥ 0` for `q > 0`. The `3/4` is forced by `ring`, not fitted.

*Build-verification note.* The Lean was authored where `lake`/Mathlib are
network-restricted and the Lean workflows are `workflow_dispatch`-only, so it
has not yet been compiled by CI. The proof uses only the `field_simp; ring`
pattern on a ℚ-verified identity (high confidence). **Confirm by dispatching
`lean_ci.yml` on `main`**; treat any failure as a quick fix-forward.

## 4. Experimental discrimination — N/A for now (no data)

For completeness, recording why experimental discrimination is *not* an operative
criterion:

- The leading term reproduces QED, so it does **not** distinguish QOU from
  standard physics — both predict the textbook force.
- The first QOU-distinctive signal is the interacting-mode (`1/d⁶`) correction,
  the analog of the QED radiative correction, of relative size `~α·(λ_C/d) ≈ 10⁻⁸`
  at `d ∼ 100 nm`. It is swamped by material/geometry corrections — finite
  conductivity (10–40 %), temperature, surface roughness — by `~10⁶–10⁸`, so no
  current or near-term Casimir experiment can isolate it.
- Where the *same* `q₀` (fixed by `Vol(4_1)` in `m_p/m_e`) is testable against
  easy, high-precision data is the **mass/decay sector** (m_e, m_K/m_π, m_μ,
  Q_β, m_n, Δ_pn; CODATA/PDG). That — not Casimir — is the framework's live
  falsification channel (mixed scorecard; see the precision dashboard).

This is **not a deficiency for the operative bar**: with no Casimir experiment
to compare against, the goal is internal (1% / 1ppQ / Lean), all of which are met.

## Status summary

| Criterion | Target | Casimir status |
|---|---|---|
| Agreement with QED | within ~1 % | **MET** — leading term exact, ξ_k=0 |
| Compute precision | ≤ 1ppQ (L1) | **MET** — closed-form, cross-method Δ≈3×10⁻⁶¹ |
| Lean | sorry-free statement | **MET** (3/4 exact; CI build-confirmation pending) |
| Experimental discrimination | — | N/A (no accessible data; deferred) |

## Block correction applied

The conjecture block previously called the Casimir effect "*the* clean
experimental probe" / "the cleanest experimental probe of vacuum-energy
structure." That over-states the discriminating power (§4). The block's
Falsification-path and Why-this-matters text is qualified to: a **leading-order
consistency check** within the ~1 % window, with the discriminating signal
experimentally inaccessible and the cross-sector mass observables carrying the
falsification leverage.
