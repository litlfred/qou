# The α_EM per-loop 8π is NOT Gauss–Bonnet — the "8" is homological b₁, the π is the flat heat kernel

**Date:** 2026-07-19 · **Axis:** α_EM 2-loop / 1ppQ (#3612, magnitude leg) · **Tier:**
numerical scope-(a) · **Discipline:** no fit, no 8π manufactured, no c_k wired, no tier change.

## Question

Owner: *"π not from Gauss–Bonnet?"* — i.e. does the π in the α_EM per-loop `1/(8π)`
come from the surface's Gauss–Bonnet data (Euler characteristic / hyperbolic area)
rather than the flat 2-D heat kernel `1/(4π)` settled in #3909?

## Gauss–Bonnet facts for Bring

Bring's curve is **genus 4**. Under hyperbolic uniformization (`K = −1`):

| g | χ = 2−2g | GB Euler `−χ = 2g−2` | homological `b₁ = 2g` | GB area `−2πχ = 2π(2g−2)` |
|---|---|---|---|---|
| 3 | −4 | 4 | 6 | **8π** |
| **4 (Bring)** | **−6** | **6** | **8** | **12π** |
| 5 | −8 | 8 | 10 | 16π |

So `8π` is the Gauss–Bonnet area only at **genus 5**, and `8 = −χ` only at genus 5.
For Bring (g=4) the genuine GB invariants are **6** (Euler) and **12π** (area).

## Result — both factors point away from Gauss–Bonnet

[`alpha_em_perloop_pi_not_gauss_bonnet_probe.py`](../../computations/alpha_em/alpha_em_perloop_pi_not_gauss_bonnet_probe.py)
(6/6 assertions):

1. **The "8" is homological, not Gauss–Bonnet.** The settled count (#3896) is
   `b₁ = 2g = 8`. Bring's Gauss–Bonnet Euler number is `−χ = 2g−2 = 6 ≠ 8`. The "8"
   in `8π` is the first Betti number, **not** the Euler characteristic.

2. **The π is not a GB area.** The polarized determinant measure `8.2263` (#4064)
   matches **no** Gauss–Bonnet invariant of Bring:

   | ratio | value |
   |---|---|
   | measure / 12π (GB area) | 0.218 |
   | measure / 6 (`−χ`) | 1.371 |
   | measure / 6π (`−χ·π`) | 0.436 |
   | measure / 8 (`b₁`) | **1.028** (2.8% off) |

   It is **π-free**, sitting at `b₁ = 8`. The Polyakov / conformal-anomaly π
   (`∫R = 4πχ`, `χ = −6`) is **divided out** by the holomorphic factorization — the
   polarized object carries no anomaly π.

The `π·φ² = 1.00018` near-hit (0.018%) is a **coincidence** — Bring's A₅ / golden-ratio
symmetry (cf. the 4₁ bar-even action `π²/5`) makes it tempting, but at 40-digit
compute the digits kill it; it is not an identity.

## Conclusion

The per-loop `8π` splits as **(count `b₁ = 8`) × (flat heat-kernel π, #3909)** — not a
single Gauss–Bonnet area (which would be `12π` for Bring) and not with an Euler-number
count (which would be `6`). **Gauss–Bonnet is the wrong origin for both factors at
Bring's genus.** The residual 2.8% (`8.2263` vs `8`) is not a `χ`-correction and remains
for the q-holomorphic (`Φ_b`) deformation.

## Scope (anti-laundering)

Tests and rejects the Gauss–Bonnet attribution on the numbers; keeps the
homological-count × heat-kernel split. No `8π` manufactured; no fit; no c_k; no tier change.

## Cross-references

- Polarized determinant (measure 8.226, b₁=8 2.8% off): [`2026-07-19-alpha-em-polarized-determinant-removes-blowup.md`](2026-07-19-alpha-em-polarized-determinant-removes-blowup.md), #4064
- "8" = b₁ homological count: #3896
- π = 2-D heat kernel 1/(4π): #3909
- Genus-4 Epstein det′Δ (unpolarized): merged #3934
