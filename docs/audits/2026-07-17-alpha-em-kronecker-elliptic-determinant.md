# α_EM `1/(8π)` wall — the Kronecker elliptic determinant (prune-or-proceed on the abelian lane)

**Date:** 2026-07-17 · **Axis:** α_EM single wall (Front-3, `1/(π b₁)` photon 1-loop normalization) ·
**Tier:** symbolic-exact structural (mpmath; Ray–Singer/OPS + Kronecker limit + modular-invariance checks) ·
**No 8π manufactured, nothing wired, no tier change.** A scope-(a) prune-or-proceed on one wall.

Probe [`alpha_em_kronecker_elliptic_determinant_probe.py`](../../computations/alpha_em/alpha_em_kronecker_elliptic_determinant_probe.py)
→ [witness](../../computations/alpha_em/alpha-em-kronecker-elliptic-determinant.witness.json) (5/5).

## The one machinery no sibling used

The target is to derive `1/(π b₁) = 1/(8π)` (b₁ = 2g = 8, g = 4) as the photon
1-loop determinant normalization on `J(M) = H¹/H¹(ℤ)`. The three merged Front-3
prunes all worked on **generic flat tori / covolume**:

- **#3834** — `ζ_{Δ₁}(0) = −b₁`, area-free (Epstein). The *count*, not the measure.
- **#3842** — flat-torus determinant `μ`-trap: `Z(μ) = μ^{ζ(0)}·(det'Δ)^{∓1/2}`,
  and `μ` absorbs any constant. The reciprocal+π sit in the μ-sector.
- **#3848** — abelian RS-torsion `= √det G = Vol(J)` (covolume) — the
  data-**excluded** `1/Area` branch (−1419 ppb / 9500σ).

None computed the **Kronecker-limit elliptic determinant** of the *actual*
isogeny factor `E = Bring/S₄` of `Jac(Bring) ~ E⁴` (Riera–Rodríguez;
[`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)):

$$
  \det{}'\Delta_{E_\tau} \;=\; \mathrm{area}\cdot\big(\underbrace{\operatorname{Im}\tau\,|\eta(\tau)|^4}_{\text{modular-invariant SHAPE}}\big),
  \qquad (\text{Ray–Singer / OPS; textbook } (\operatorname{Im}\tau)^2|\eta|^4 \text{ at covolume area}).
$$

## Pre-registered kill criteria and what the computation returns

| # | Kill criterion | Result |
|---|---|---|
| **K1** | measure collapses to a covolume/area factor (tracks SCALE) ⇒ #3848 again, Lane-1 dead | **FAILS for the measure** — the properly zero-mode-integrated boson 1-loop measure `Z = √area/√det'Δ = 1/(√Im τ · |η(τ)|²)` is **scale-free**: the area cancels (`√area/√(area·SHAPE)`). Verified constant across `area ∈ {0.5, 1, 7.3, 137}` while `√det G` tracks the area 1:1. |
| **K2** | measure is scale-free + modular (a distinct category) ⇒ #3848 does not cover it | **HOLDS** — `Z` is modular-invariant (S,T to 1e-28) and covolume-free. A genuine *third* category, distinct from both #3842's flat det and #3848's covolume torsion. |
| **K3** | is the reciprocal `π` FORCED by the modular data? | **NEGATIVE** — `Z = 1/(√Im τ|η|²)` is **π-free**. The only π's dressing a boson 1-loop are the zero-mode `(2π)`-Gaussian normalizations; any per-mode rescaling `λ ∈ {1, 2π, 1/π}` yields an equally modular-invariant `λ·Z`, so the π is a **convention / RT-framing μ-sector** factor, not a modular observable. (Exactly the "do not μ-tune until 8π appears" trap the spec warns of.) |

## What this buys, and what it does not

- **Buys (K1/K2 — refines the abelian prune's scope).** #3848 correctly showed
  the abelian *covolume/torsion* factor is `Vol(J) = √det G` (the excluded
  `1/Area` category). But the **complementary 1-loop determinant factor** — the
  object that carries the actual `det'Δ` — is the **scale-free modular constant**
  `1/(√Im τ|η|²)`, which #3848 did not compute. So #3848's "`1/(π b₁)` is
  derivable from *no* abelian normalization" is **scope-limited**: the covolume
  object is pruned, the modular-determinant object is *not*. The abelian lane is
  not fully covolume-dead — there is a genuine, previously-uncomputed
  modular factor (the η-value at the fixed Bring modulus).
- **Does not buy (K3 — the π stays Front-2/RT).** The modular determinant is
  **π-free**; it does *not* supply the reciprocal `1/(π b₁)`. So the abelian
  lane still does **not close α_EM by itself** — consistent with the siblings'
  steer of the π to the nonabelian **RT `(2π)`-framing prescription** (the
  `4c70433c1` shared-wall acceptance gate, Front-2 `D(ζ)=8`).

## Net reduction (scope-(a))

$$
  \frac{1}{8\pi}
  \;=\;
  \underbrace{\frac{1}{\sqrt{\operatorname{Im}\tau_{\text{Bring}}}\,|\eta(\tau_{\text{Bring}})|^2}}_{\text{η-modular value at the FIXED Bring modulus (magnitude/shape)}}
  \;\times\;
  \underbrace{[\,\text{RT }(2\pi)\text{-framing prescription}\,]}_{\text{the reciprocal }\pi,\ \text{Front-2/RT}}.
$$

The immediate open sub-step is therefore the **bounded-open `j(E)/τ_Bring`**
computation flagged in
[`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md` §"Explicit j(E)"](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
(the elementary symmetric invariants collapse to a genus-0 subfield; `τ_Bring`
needs the fixed field `K(Bring)^{S₄}`, the periods of the invariant differential,
or the 5:1 branch data). The π is handed to Front-2 / the RT prescription.

## Scope guard (STRICT)

- **No 8π manufactured.** The probe never solves for `τ_Bring` from CODATA and
  never tunes any normalization to make `8π` appear (the fitting trap the spec
  §3 forbids). It measures the *category* of the elliptic determinant.
- **Not a closure.** K3 is negative — the abelian modular determinant does not
  supply the π; α_EM stays open.
- **Nothing wired, no tier change.** Pure scope-(a) structural measurement.

## Cross-references

- Attack spec (Front-3): [`2026-07-17-three-front-attack-specs.md §3`](2026-07-17-three-front-attack-specs.md)
- Derivability map (the wall isolated): [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- E⁴ isogeny + bounded-open j(E): [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
- Sibling prunes refined/complemented: #3834 (count), #3842 (μ-trap), #3848 (covolume torsion)
- The π's destination (shared-wall gate): `alpha_em_wlambda_shared_wall_acceptance_gate_probe.py` (`4c70433c1`), Front-2 `D(ζ)=8`
- Proved 1/(12π) template (the mirror): `predicted-spectra/photon-ir-zero-mode-bring.md`, `QOU.Archimedean.PhotonIRZeroMode`
