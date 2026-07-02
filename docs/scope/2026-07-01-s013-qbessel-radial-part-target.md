# s013 — the q-Bessel radial-part target, sharpened (per-block d_q shape)

**Bean:** [`s013`](../../.beans/s013--keystone-value-map-colored-lawrence-rozansky-s-mat.md)
**Date:** 2026-07-01. **Status:** scope note — records the sharpened target for the owner-gated
q-Bessel / DG realization. No new math; no fit; no fabricated correspondence.

## Where the value step actually sits

The keystone reduced to `bwS0 λ = d_q(λ)/D` (`KeystoneVerlindeSMatrixBridge.lean`,
`BWVacuumRowIsHecke`). Two prior results bound the remaining work:

1. **Arena settled** ([`2026-06-22-keystone-modular-category-identification.md`](../audits/2026-06-22-keystone-modular-category-identification.md)):
   `q₀ ≈ 1.10998 > 1` is the **non-compact** `SU_q(2) → E_q(2)` growth regime — Hahn–Exton
   q-Bessel, *not* a compact root-of-unity MTC.
2. **q-Bessel gate run** ([`2026-06-20-keystone-qbessel-heat-kernel-lead.md`](../audits/2026-06-20-keystone-qbessel-heat-kernel-lead.md),
   `keystone_qbessel_plancherel_precheck.py`): P2 (conjugation `W_λ=W_{λ'}`) ✅, P3 (table) ✅,
   P1 (normalisation) ⚠ fails by `1−Z(5)=0.0178`. It located the open object as **(a) the
   radial-part identity** — is the q-Bessel (2nd-kind) orthogonality measure ∝ `W_λ` at the
   partition points? — plus **(b)** the manifold (owner-gated DG).

This session added the **colored Σ(2,3,5)** realization of the geometric side (merged #3190:
E₈-exponent family, 4↔4 monotone bwS0 correspondence, H₄ ⊂ E₈ folding) and the **value-map screen**
(merged #3197). The screen sharpens step (a) as follows.

## The sharpened step-(a) target

The n=5 vacuum row (4 conjugation classes) that the q-Bessel radial-part measure must reproduce is
**not** a uniform shape. Three of the four blocks are **single balanced q-integers**; only one is a
genuine product:

| conjugation class | d_q shape | value at q₀ | difficulty |
|---|---|--:|---|
| (5) ~ (1⁵) | `[1]_q` | 1.0000 | trivial |
| (4,1) ~ (2,1,1,1) | `[4]_q` | 4.1097 | trivial (standard-rep family `[n−1]_q`) |
| (3,2) ~ (2,2,1) | `[5]_q` | 5.2204 | trivial |
| **(3,1,1) self-conjugate** | **`[4]_q[3]_q/[2]_q`** | **6.2204** | **the hard block** |

So a q-Bessel radial-part measure that realizes `bwS0` must:

- **On near-standard blocks** — return a *single* balanced q-integer `[m]_q` (the natural Hecke
  label `m ∈ {1,4,5}`, **not** the E₈ exponent). The compact sine-kernel `sin(πe/30)` and the
  exponent q-dimension `[e]_q` were both **refuted** for this (#3197), consistent with the
  non-compact arena.
- **On the self-conjugate ≥3-row block `(3,1,1)`** — return the **product** `[4]_q[3]_q/[2]_q`.
  This is the sole non-single-q-integer weight and is exactly the ≥3-row block where the compact
  SU(2)/spin-j gate failed ([`2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md`](../audits/2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md)).
  **The realization difficulty is concentrated here.**

## The one missing ingredient (why this is DG, not numerics)

Step (a) needs the **partition-λ → q-Bessel-domain-point** correspondence — where each `λ ⊢ 5` sits
on the Hahn–Exton q-Bessel lattice/zero set (Koelink–Swarttouw orthogonality). That map is **not**
established anywhere in the corpus; it **is** the open construction. The q-Bessel orthogonality
weights have a known closed form, but assigning partitions to lattice points without the geometry
would be inventing the correspondence — outside the no-fit / no-fabrication discipline. Hence step
(a) is the owner-gated DG object (#2503), not an in-session numeric.

## Handoff to the DG session

When the partition→lattice map is supplied by the geometry, the **falsifiable check** is:
the q-Bessel 2nd-kind measure at the four `λ⊢5` points returns `{[1]_q, [4]_q, [5]_q,
[4]_q[3]_q/[2]_q}` (up to the global `1/D` from `D²=Σd_q²`, and modulo the `Z(5)=0.9822`
partition-function normalisation the precheck isolated). A candidate map that gets the three
single-q-integer blocks but misses the `[4][3]/[2]` self-conjugate weight is wrong — the
self-conjugate block is the discriminating test.

## Cross-references

- Colored family + 4↔4: [`2026-06-30-keystone-colored-sigma235-e8-family.md`](../audits/2026-06-30-keystone-colored-sigma235-e8-family.md), `computations/probes/keystone_colored_sigma235_wrt.py`.
- Value-map screen: `computations/probes/keystone_valuemap_screen_s013.py` (compact candidates refuted).
- q-Bessel precheck: `docs/audits/scripts/keystone_qbessel_plancherel_precheck.py`.
- Ledger: [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md); DG plan [PR #2503](https://github.com/litlfred/qou/pull/2503).
