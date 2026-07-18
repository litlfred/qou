# DGG tetrahedron-index S₃ triality — pinned (2026-07-18)

**Tier:** compute unblock for the G3 3d-index route
([`2026-07-14-g3-stokes-via-3d-index.md`](2026-07-14-g3-stokes-via-3d-index.md),
#3805). Audit-only; no production wiring; scope-(a); comparison-only.

## The blocker this closes

The G3 keystone route (odd-channel Stokes constant `A_ω` as an integer
count from the GGM 3d-index of 4₁) is gated on the DGG tetrahedron index
`I_Δ(m,e)(q)` passing its **triality self-test** before the two-tetrahedron
4₁ gluing is assembled on top of it. #3805 found the naive transcription
**red** on negative-`e` cases: it tested `I_Δ(m,e) = (±q^?)^e I_Δ(−e−m, m)`
and the `(−√q)^e` form matched `m=e=1` to ~1e-41 but negative-`e` cases
missed by O(0.3). It then (correctly, per anti-guessing) refused to build
the gluing on an unvalidated `I_Δ` and gated on the primary source.

## Method — pin the prefactor from the exact series, don't guess it

The tetrahedron index

$$I_\Delta(m,e)(q)=\sum_{n\ge \max(0,-e)}(-1)^n\,\frac{q^{\,n(n+1)/2-(n+e/2)m}}{(q;q)_n\,(q;q)_{n+e}}$$

is an **exact** q-series, and the S₃ triality on the edge-charge triple
`(m, e, f)` with `f = −m−e` is a theorem — so for every `(m,e)` the ratio
to a triality image is a **signed q-monomial** `±q^{k(m,e)}` whatever the
paper's normalization. Probe
[`tetrahedron_index_triality_pin.py`](../../computations/probes/tetrahedron_index_triality_pin.py)
therefore *extracts* the sign and exponent numerically at a clean real `q`
and identifies `k(m,e)` as a closed form (fit over `{1,m,e,m²,e²,me}` to
half-integers), cross-checking at a second `q` to rule out an accidental fit.

## Result — the full S₃, both generators green

| generator | pinned relation | check |
|---|---|---|
| **ℤ/3 (cyclic)** | `I_Δ(m,e) = (−q^{1/2})^m · I_Δ(−e−m, m)` | greens **49/49** on `(m,e)∈[−3,3]²`, worst residual 1.5e-43 |
| **ℤ/2 (reflection)** | `I_Δ(m,e) = I_Δ(−e, −m)`  (no prefactor) | greens **49/49**, worst residual 5.6e-44 |

- **Exponent extraction:** `k(m,e) = +½·m` for the cyclic ratio (sign
  `(−1)^m`); `k = 0` for the reflection — identical at `q=0.1` and
  `q=0.137` (residuals ≤ 2.6e-36), so it is a genuine identity, not a fit.
- **Group laws verified:** cyclic `C³ = id` (the prefactors
  `(−q^{1/2})^{m+(−e−m)+e} = 1` multiply to unity; residual 2.6e-54);
  reflection `R² = id` on the index map (exact).

## The correction to #3805

The prefactor depends on **`m`, not `e`**:
`(−q^{1/2})^m`, **not** `(±q^?)^e`. That single variable swap is why the
negative-`e` cases were red — the test was probing the wrong monomial. With
the `m`-form both S₃ generators pass on the full grid including all negative
`e`.

## Unblocks

The self-test gate is now green. The 4₁ two-tetrahedron gluing
`I_{4₁}(0,e)(q)` can be assembled on the validated `I_Δ` (with the pinned
triality available to simplify the double sum), then its q-series
coefficients read as the GGM integer Stokes data — the next step of the
#3805 plan (validate against a published coefficient, then run the
formalize-first derivation-vs-fit check against the even-face action
`Vol(4₁)/π` and the odd-face band `[0.147, 0.168]` from
[`2026-07-17-onepq-path-reevaluation.md`](2026-07-17-onepq-path-reevaluation.md)).

No `A_ω` or `c_k` wired; nothing reaches production until a Stokes constant
is genuinely *derived* from the index (not fitted). scope-(a).
