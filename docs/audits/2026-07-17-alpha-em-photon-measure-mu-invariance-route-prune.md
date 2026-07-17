# α_EM Front 3 (cont.): `1/(π b₁)` — μ-invariant `b₁` derived, reciprocal+π is a fitting trap

**Date:** 2026-07-17 · **Axis:** α_EM per-loop measure · **Tier:** measurement
(scope-(a) structural + route-prune; no `α_k` wired; no fit; `1/(8π)` stays a
phase-4 identification). **Branch:**
`claude/alpha-em-photon-determinant-reciprocal-2026-07-17` (PR #3842).
Continues #3834 (`ζ_{Δ₁}(0)=−b₁`, area-free).

## The wall, restated precisely

The [2026-07-14 derivability map](2026-07-14-alpha-em-2loop-derivability-map.md)
isolates the α_EM single wall as the **per-loop measure** `1/(π b₁) = 1/(8π)`:
data excludes `1/Area` (−1419 ppb) and selects the bare-`b₁` form; `b₁ = 8` is
proven (Lean `PhotonIRZeroMode`, PR #2114); the *form* `1/(π b₁)` is a phase-4
identification. The map's target: *"why is the photon 1-loop normalization the
count `b₁`, not the surface area? — turning 'governed by `b₁`' into the exact
`1/(π b₁)` is the RT shadow-world 1-loop determinant on the genus-4 Jacobian."*

## The decomposition: μ-invariant vs μ-sector

The free 1-loop (Maxwell / scalar) fluctuation measure on the Jacobian torus
`J(M) = T^{b₁}` with UV normalization scale `μ` is

```
Z_fluc(μ) = μ^{ζ_{Δ₁}(0)} · (det'Δ₁)^{∓1/2}          [Hawking μ-scaling]
```

— the normalized Gaussian measure `∏_k √(μ²/2π) dφ_k` gives one factor of `μ`
per mode, and the ζ-regularized mode count is `ζ(0)`. With `ζ_{Δ₁}(0) = −b₁`
(#3834), the μ-power is **exactly `−b₁`**, area-free.

### 1. μ-INVARIANT (derived): the `b₁`, area-free

The only place `b₁` enters μ-invariantly is the anomaly coefficient
`ζ_{Δ₁}(0) = −b₁`, verified area-free in #3834 (Epstein `E_Λ(0) = −1` for every
lattice; covolume only in the regular `1/(s−d/2)` pole). This **is** the
derivability-map's "why `b₁`, not Area" mechanism: the loop measure's `b₁` is
the ζ-regularized **scale-anomaly count**, not the covolume. Derived.

### 2. μ-SECTOR (fitting trap): the reciprocal `1/b₁` and the `π`

The μ-power is `μ^{−b₁}` — **exponential** in `b₁`, not the reciprocal `1/b₁`.
So the `1/(π b₁)` reciprocal form is **not** produced by the anomaly; it sits in
the per-mode normalization / μ-choice sector. The probe demonstrates this
explicitly: for the measure `Z_fluc(μ) = μ^{−b₁}·const`, solving `μ = m^{−1/b₁}`
reproduces **any** target value `m`:

| target `m` | `μ*` | `Z_fluc(μ*)` |
|---|---|---|
| `1/(8π) ≈ 0.039789` | 1.496339 | 0.039789 (|Δ|≈6e-33) |
| 0.001 | 2.371374 | 0.001 |
| 1.0 | 1.0 | 1.0 |
| 7.3 | 0.779982 | 7.3 |

Any constant — including `1/(8π)` — is reachable by choosing μ. So a flat-torus
determinant **cannot discriminate** `1/(π b₁)` from any other constant without
fixing μ externally. Tuning μ until `8π` appears is exactly the spec's
**forbidden fitting trap** ([three-front spec §3](2026-07-17-three-front-attack-specs.md):
"the ζ-determinant μ-dependence can absorb any constant; that is the fitting
trap").

### 3. CONSEQUENCE — the flat-torus determinant route is PRUNED

The honest, non-fitting content extractable on `T^{b₁}` is the μ-invariant
anomaly `−ζ_{Δ₁}(0) = b₁` (area-free; done, #3834). The reciprocal-and-`π` of
`1/(π b₁)` is μ-normalization-dependent and therefore requires an **independent**
μ-fixing — the categorical **RT / Reshetikhin–Turaev shadow-world**
normalization on the genus-4 Jacobian (a TQFT-side, hence μ-invariant,
prescription), **not** a flat-torus determinant μ-tune. The wall is sharpened:
the residual is specifically the **RT μ-prescription**.

## Why this is a positive contribution

It (a) proves the μ-invariant half is genuinely done (`b₁`, area-free), (b)
**removes a fitting trap** the program could have fallen into — "μ-tune a
flat-torus determinant to derive 8π" — by showing μ absorbs any constant, and
(c) names the exact remaining object (the RT μ-prescription). This is the
anti-fitting discipline applied *forward*: it certifies where a real derivation
must come from and where it provably cannot.

## Scope / discipline

- Scope-(a) structural + route-prune; no `α_k` value produced or wired; no fit;
  does not manufacture 8π; `1/(8π)` stays a phase-4 identification; L2 unchanged.
- Corpus-checked: `b₁ = 8` proven (Lean `QOU.Archimedean.PhotonIRZeroMode`, PR
  #2114); not touched here. Builds on merged #3834; complementary to #3812.

## Cross-references

- #3834 (`ζ_{Δ₁}(0)=−b₁` area-free): [`2026-07-17-alpha-em-zeta-anomaly-b1-count.md`](2026-07-17-alpha-em-zeta-anomaly-b1-count.md)
- Wall map: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- Ledger: [`alpha-em.md`](../coordination/alpha-em.md)
- Witness: `computations/alpha_em/alpha-em-photon-measure-mu-invariance.witness.json`
