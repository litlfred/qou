# Hopf-sector cubic ↔ crossing-weight scalar: shadow match, substrate wall (KC19 × KC20)

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone · **Follows:** KC19
([affine crossing-weight narrowing](2026-07-07-qbeta-crossing-weight-affine-narrowing.md))
+ KC20 ([ζ₄-residue exclusion / Hopf cubic](2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md))
· **Tier:** proved-lean (shadow identity) + symbolic-exact (substrate rigidity)
· **No `c_k` value, no wiring, no tier change** (registry §8).

## The question

The two 2026-07-07 landings converge on one object from opposite sides:

- **KC19** (sibling, PR #3473): the archimedean evaluation map is **affine** in the
  crossing weight `w`, so the entire c_k odd channel is `K(q)·(w−w₀)` with
  `K(q) = 2h/(4w₀²−h²)` a **fixed, anchor-rigid** rational function. The open
  scalar is `w(q)` (its `u³` coefficient **is** `c_3`).
- **KC20** (PR #3467): the odd carrier's non-cyclotomic content is the
  **irreducible cubic** `C(y) = y³−4y²+3y−2` in `y = q²+q⁻²`, sourced by the
  **Hopf (2-crossing)** sector `C_Hopf(y) = y³−6y²+10y−6`.

Does the Hopf-sector cubic determine the open crossing-weight scalar / `c_3`?

## Result — yes at the q=1 shadow, no at the substrate

**(1) Shadow level (q=1, `y=2`) — exact match.** The c_3 q=1 shadow is `−2`
(KC10, `= J_Hopf(q=1)`). The Hopf-sector cubic reproduces it exactly:

`C_Hopf(2) = 8 − 24 + 20 − 6 = −2`.

So the c_3→−2 classical shadow **is** the Hopf-sector cubic's value at the
classical trace point — a carrier-side confirmation of KC20's attribution of the
cubic to the Hopf link. (Honest nuance: the identity-sector quadratic also gives
`C_unknot(2) = −2`, so the shadow matches each *per-sector* value; the *total*
carrier is `C(2) = −4 = C_Hopf(2) + C_unknot(2)`. The match is with the
Hopf-link classical Jones `J_Hopf(1) = −2`, which is exactly the known c_3
shadow.)

**(2) Substrate level — no bridge; the swing is upstream in `w(q)`.** At the
substrate trace value `y₀ = q₀²+q₀⁻² ≈ 2.04371`, the Hopf cubic evaluates to a
value that is **anchor-rigid** — identical at the proton and muon pins to 8
digits — `C_Hopf(y₀) ≈ −2.0873`. But the physical `c_3` **swings 2.375%**
(`−2.0693` proton, `−2.0202` muon,
[c_3-not-exact verdict](2026-07-06-c3-not-exact-cross-anchor-verdict.md)). An
anchor-rigid quantity cannot equal an anchor-swinging one at both anchors, so:

- **`C_Hopf(y₀)` does NOT determine `c_3`.** The `−2.0873 ≈ −2.07` proximity is
  a near-coincidence (numerology-flagged), not an identity — its gap to `c_3` is
  the same order as the c_3 swing itself.
- This **confirms KC19 from the carrier side**: both the carrier (KC20) and the
  evaluation kernel `K(q)` (KC19) are anchor-rigid algebraic objects; **all of
  c_3's anchor-dependence lives in `w(q)`'s fibre structure**, which neither the
  cubic field nor the affine evaluation supplies.

## Reconciliation of KC19 and KC20

| level | carrier / cubic (KC20) | eval kernel (KC19) | physical c_3 |
|---|---|---|---|
| q=1 shadow | `C_Hopf(2) = −2` | — | `−2` (matches) |
| substrate q₀ | `C_Hopf(y₀) ≈ −2.087` (rigid) | `K(q₀)` rigid | swings 2.375% |

The cubic field of `C_Hopf` is the arithmetic of the **carrier** (a fixed
q-function); it fixes the classical shadow but is anchor-rigid, so it does not
carry the substrate swing. The keystone's open scalar `w(q)` beyond leading
order remains the sole locus of the c_3 anchor-dependence (KC19's conclusion),
now corroborated from the Hopf-cubic side.

## Discipline

Structural reconciliation (scope-(a)); no `c_3` value, no fit, no wiring, no
tier change (flip-flop guard §8). The shadow identity `C_Hopf(2) = −2` is
Lean-certified; the substrate rigidity is an exact-arithmetic witness.

## Cross-references

- KC19 affine narrowing: [`2026-07-07-qbeta-crossing-weight-affine-narrowing.md`](2026-07-07-qbeta-crossing-weight-affine-narrowing.md)
- KC20 Hopf cubic: [`2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md`](2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md)
- c_3 not exact: [`2026-07-06-c3-not-exact-cross-anchor-verdict.md`](2026-07-06-c3-not-exact-cross-anchor-verdict.md)
- c_3 q=1 shadow (KC10): [`ck-dk-canonical-registry.md §9`](../coordination/ck-dk-canonical-registry.md)
