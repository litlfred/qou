# α_EM per-loop measure: where does the `π` in `1/(π b₁)=1/(8π)` come from? — universal 1-loop factor, not the geometric Gauss–Bonnet π

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure π-decomposition · **Tier:**
structural (scope-(a); **NOT a fit, NOT a derivation**) · **Discipline:** no `8π`
manufactured; no `α_k` wired; no fit; `1/(8π)` stays a phase-4 identification.
**Branch:** `claude/alpha-em-pi-decomposition-2026-07-18`.

## Question

The α_EM ladder closes as `1/α = T + α·H` with per-loop measure `H = [2]_q/(π·D)`,
`D = dim H¹(M_Bring) = b₁ = 8`, i.e. the denominator `π·D = 8π`. The forcedness
measurement (`2026-07-17-alpha-em-perloop-integer-forcedness.md`) pinned the
**integer** `8` to the 4th decimal as `dim H¹` (3500σ vs 7 and 9). This probe asks
the orthogonal, still-open **π question**: is the `π` in `1/(π b₁)`

- **(U)** the **universal 1-loop factor** — loop-momentum `∫d^d k/(2π)^d` and/or the
  Schwinger `∫ds/s` heat-kernel Gaussian normalization `(4πs)^{-d/2}`; or
- **(G)** a **geometric / categorical** `π` — a Gauss–Bonnet Area factor, a period,
  or a single archimedean `π` multiplying the topological count `b₁`?

Note this is independently useful **regardless** of the shared-wall falsification
(#3871: `D(q₀)=11.357 ∉ {8,8π}`): that ruled out the α_EM↔W_λ unification, but the
provenance of the α_EM measure's own `π` is a separate structural fact.

## Method — the proved precedent as the lever

The corpus has **one proved α_EM π-template**: the photon IR zero-mode
(`QOU.Archimedean.PhotonIRZeroMode`, PR #2114),

    δ(1/α_EM)_IR = b₁ / Area = b₁ / (4π(g−1)) = 8/(12π) = 2/(3π)   (g = 4).

In that **proved** form the `π` is unambiguously **geometric**: it is the
Gauss–Bonnet hyperbolic area `Area = −2πχ = 4π(g−1)`. The zero-mode is the kernel
of the 1-form Laplacian `Δ₁` (harmonic forms — **no** momentum integration)
normalized by the surface area: a ratio of two geometric quantities, so its `π` is
the area's `π`. This is the natural home of hypothesis (G).

The probe (`computations/alpha_em/alpha_em_pi_universal_loop_factor_probe.py`,
mpmath, 40 dps, exit 0, 3/3 assertions) computes three exact facts.

## Result — three exact facts

1. **Proved zero-mode π = geometric Area π.** `b₁/Area = 8/(12π) = 2/(3π)` exactly.
   The `π` there is `Area = 4π(g−1)` — geometric, no loop.

2. **The self-energy π-home ≠ the geometric Area π — they differ by a pure
   topological ratio.**

   ```
   self-energy π-home:  π·b₁ = 8π  = 25.1327…
   geometric π-home:    Area  = 12π = 37.6991…
   Area/(π·b₁) = 12π/8π = 2(g−1)/g = 3/2   (exact, g=4)
   ```

   `8π ≠ 12π`. The self-energy `π` is therefore **not** the proved geometric
   Gauss–Bonnet `π`: if it were, the denominator would be the Area `12π`, and
   `D = Area/π = 12` is the corpus's **9500σ / −1419 ppb FALSIFICATION**
   (`alpha_em_perloop_integer_forcedness`). The two π-homes are separated by the
   pure topological factor `2(g−1)/g = 3/2` — a clean demonstration that they are
   **distinct** π's related by topology, not the same π.

3. **`8π` matches the universal 2D 1-loop heat-kernel factor.** The photon loop
   lives strictly on the 2-surface (the zero-mode doc's own
   dimensional-reduction argument rules out `M_g × S¹`). Among universal `d=2`
   loop constants:

   | universal constant | value at `d=2` | shape | `8π /` it |
   |---|---|---|---|
   | heat-kernel `(4π)^{d/2}` | `4π` | single `π` | `2` (clean) |
   | momentum `(2π)^d` | `4π²` | `π²` (wrong) | `2/π` |
   | Schwinger `∫ds/s` | dimensionless | no `π` | — |

   Only the 2D heat-kernel Gaussian normalization `(4π)^{d/2}|_{d=2} = 4π` has the
   single-`π` shape, and `8π = 2·(4π)`.

## Verdict — leaning (U), residual OPEN (scope-(a))

- **(G) excluded (as "the same geometric Area π").** The one π we have *proved*
  geometric is demonstrably a *different* π from the self-energy's — off by the
  topological factor `3/2`, and its Area value `12π` is data-falsified. The
  self-energy `π` cannot be the proved Gauss–Bonnet Area π.
- **(U) supported.** The `n=2` self-energy (the `α·H` term, the `α²` in `1/α`) is a
  **genuine 1-loop diagram**; by universality its measure `π` is the
  loop-integration factor. `8π = 2·(4π)` matches the universal 2D heat-kernel
  Gaussian normalization — the only universal constant of the right (single-`π`)
  shape.
- **RESIDUAL OPEN (STRICT — not manufactured).** The **exact** bare-`π` reciprocal
  normalization is not derived. `8π` is compatible with both `(4π)·2`
  [universal loop × symmetry-2] and `(π)·(b₁=8)` [one loop-`π` × an 8-mode trace
  over the `b₁` harmonic sectors]. **Both** are universal-loop-family readings, so
  the coarse (G)/(U) question resolves toward (U); the *fine* question — which
  multiplicity (`2` vs `b₁`) and why the reciprocal form — is the open wall. Note
  the two readings are not exclusive: the loop trace over the `b₁ = 8` harmonic
  `Δ₁` sectors (each carrying the universal loop `π`) *is* how a single loop-`π`
  and the count `b₁` co-occur, consistent with the merged `ζ_{Δ₁}(0) = −b₁`
  area-free mode-count (#3834).

This does **not** derive `1/(8π)`; it decides *where the `π` comes from* (universal
loop, not geometric Area) and leaves the exact normalization as the well-posed
residual. No `8π` manufactured; no `α_k` wired; no fit; `1/(8π)` stays a phase-4
identification.

## Cross-references

- Proved geometric-π template (`1/(12π)`, `2/(3π)`): [`../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean), [`../../content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md`](../../content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md)
- Forcedness of the integer `8`: [`2026-07-17-alpha-em-perloop-integer-forcedness.md`](2026-07-17-alpha-em-perloop-integer-forcedness.md)
- Area-free bare-`b₁` mode-count `ζ_{Δ₁}(0)=−b₁` (#3834): [`2026-07-17-alpha-em-zeta-anomaly-b1-count.md`](2026-07-17-alpha-em-zeta-anomaly-b1-count.md)
- Shared-wall falsification on the observable side (#3871): [`2026-07-18-alpha-em-shared-wall-gate-falsified-observable-side.md`](2026-07-18-alpha-em-shared-wall-gate-falsified-observable-side.md)
- Probe + witness: [`../../computations/alpha_em/alpha_em_pi_universal_loop_factor_probe.py`](../../computations/alpha_em/alpha_em_pi_universal_loop_factor_probe.py), `computations/alpha_em/alpha-em-pi-decomposition.witness.json`
