# α_EM `1/(8π)`: reconciling the three readings of the `1/π` origin

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure · **Tier:** coordination /
reconciliation (scope-(a); no fit; nothing wired; `1/(8π)` stays a phase-4
identification). Resolves the `/coordinate` §6 divergence surfaced across the
2026-07-17/18 Front-3 α_EM sweep.

## The divergence

The photon per-loop measure `1/(π b₁) = 1/(8π)` (`b₁ = dim H¹(M_Bring) = 8`)
factors into a **mode count** `b₁` and a **`1/π` per-mode weight**. The count is
settled — `−ζ_{Δ₁}(0) = b₁`, area-free (merged #3834, and independently #3831).
The **`1/π` origin** was left with **three different readings** across three PRs:

| # | PR | Reading of the `1/π` |
|---|----|----|
| R1 | #3864 (open) + #3842 (merged) | the `(2π)`-Gaussian zero-mode **convention** — μ-sector, **not forced** by anything computed; `Z = 1/(√Im τ·\|η\|²)` is π-free |
| R2 | #3879 (merged) | the **universal 1-loop** heat-kernel factor `(4π)^{d/2}\|_{d=2}=4π`, so `8π = 2·4π` — π *forced* by loop universality |
| R3 | #3831 (merged) | reduces to the open **`conj:dilogarithm-archimedean-limit`** (Bloch–Suslin archimedean π) **+ a `2πg` genus identity** — π *forced* by geometry/the dilog |

These are not three labels for one fact: R1 says the `1/π` is **not derivable**
(a convention); R2 and R3 say it **is** derivable but from **different** sources
(loop universality vs the dilog/genus). They are genuinely competing.

## Ruling (owner, 2026-07-18): R1 is the canonical *status*; R2 and R3 are named *candidate derivation hypotheses*

- **Canonical current status = R1 (convention / μ-sector).** This is the
  conservative, honest state: **the `1/π` is not forced by anything computed to
  date.** It is consistent with the two independent negative results — the
  flat-torus determinant is a μ-fitting-trap (#3842) and the abelian modular
  determinant `Z` is π-free (#3864 K3). The ledger status of `1/(8π)` therefore
  stays **OPEN phase-4 identification**, with the `1/π` specifically flagged
  *not-derived*.
- **R2 and R3 are the two open routes that *would* derive it** — kept as named
  hypotheses, not contradictions:
  - **R2 (loop-universality):** prove the photon self-energy's per-loop measure
    is the universal `d=2` heat-kernel `4π` (with the `2` a spin/multiplicity
    factor), so `8π = 2·4π`. Status: structural argument only (#3879); no proof
    the multiplicity is exactly `2` rather than `b₁`.
  - **R3 (dilog + genus):** prove the `2πg` genus identity on Bring *and* close
    `conj:dilogarithm-archimedean-limit` (#3831). Status: both inputs open.
- **These do not contradict R1** — they are candidate *derivations* of a quantity
  R1 currently records as underived. If either R2 or R3 is proved, it supersedes
  R1 for that quantity. Until then R1 is the status and R2/R3 are the leads.

## Why not "split the difference"

Per `/coordinate` §6, the readings are recorded as they stand — not blended. R1
is a *status* (underived); R2/R3 are *hypotheses* (candidate proofs). Labeling
R1 canonical does not endorse R2 over R3 or vice-versa; it records that **neither
is proved**, which is the honest state.

## Consequence for the shared-wall lead

The R1/R2/R3 question is downstream of the count `b₁`, which is settled. The
separate shared-wall test — is the count `b₁` the keystone total quantum
dimension `D`? — is **closed negative on both sides**: observable `D(q₀)=11.357`
(#3871), fibre `D(ζ)∈{1.66…3.80}` (#3883), both ∉ {8, 8π}. So the surviving
α_EM lead is the **non-`D` route** for how `b₁` enters (per-irrep `d_λ` / an
index), tracked separately.

## Cross-references

- Count `b₁` area-free: #3834 / #3831 · Merged prunes: #3842 (μ-trap), #3848 (covolume)
- π readings: #3879 (R2), #3831 (R3), #3864 + #3842 (R1)
- Shared-wall closed both sides: #3853 (gate), #3871 (observable), #3883 (fibre)
- Ledger: `docs/coordination/alpha-em.md` (currency fix in-flight on #3864 — the R1 status + R2/R3 leads should land there once #3864 rebases)
