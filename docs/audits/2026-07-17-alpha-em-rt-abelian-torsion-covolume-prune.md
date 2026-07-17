# α_EM Front 3: abelian RT/RS torsion is a covolume, not the count `b₁` — abelian route pruned

**Date:** 2026-07-17 · **Axis:** α_EM per-loop measure · **Tier:** measurement
(scope-(a) route-narrowing; no `α_k` wired; no fit; `1/(8π)` stays a phase-4
identification). **Branch:** `claude/alpha-em-rt-shadow-b1-vs-quantumdim-2026-07-17`
(PR #3848). Continues #3842.

## Context

#3842 pruned the flat-torus determinant route to `1/(π b₁) = 1/(8π)` (the
reciprocal+π is μ-sector; μ absorbs any constant) and named the RT / Reshetikhin–
Turaev shadow-world μ-prescription as the residual wall. This audit takes the
decisive bounded step on the **abelian** (U(1) photon) side of that wall.

## The question

> Does the abelian RT / Ray–Singer torsion normalization of the U(1) photon on
> the Jacobian `J(M) = H¹/H¹(ℤ)` carry a bare **count `b₁`**, or a **covolume
> `D`**?

Same discriminant the data settled at the value level (`1/(π b₁)` works,
`1/Area` −1419 ppb) — now on the RT-side normalization structure.

## Result — a covolume, not a count

The Ray–Singer analytic torsion of the trivial U(1) connection is the covolume
of the harmonic lattice, `Vol(J) = √det G` (G = period/intersection Gram of
`H¹(M;ℤ)`). It is a `b₁`-dimensional volume, shape-dependent:

| lattice | `Vol(J) = √det G` |
|---|---|
| ℤ² (square) | 1.000 |
| hexagonal (Gram `[[2,1],[1,2]]`) | 1.732 |
| rectangular 1×3 | 3.000 |
| skew (Gram `[[3,1],[1,5]]`) | 3.742 |

The covolume varies continuously with shape while `b₁ = d` is a fixed integer.
So the abelian RS torsion is a **covolume**, in the **`1/Area` category — the
branch the data excluded** (−1419 ppb). The abelian RT route does **not** produce
`1/(π b₁)`.

## The narrowed wall

- The only count-`b₁` object remains `ζ_{Δ₁}(0) = −b₁` (area-free, #3834). Neither
  the flat-torus determinant (μ-power `μ^{−b₁}`, #3842) nor the abelian RS
  torsion (covolume, this probe) turns that count into the **reciprocal** `1/b₁`.
- Therefore `1/(π b₁)` is **not** an abelian-normalization object. The
  reciprocal-count `1/b₁` — one photon "democratically averaged" over the `b₁`
  harmonic-1-form directions — survives only via the **nonabelian RT S-matrix**
  normalization (the W_λ keystone route, Front 2) or a genuine phase-4
  identification.

## Front-3 arc (this session)

| PR | Result |
|---|---|
| #3834 | `ζ_{Δ₁}(0)=−b₁`, area-free — the count-`b₁` "why b₁, not Area" mechanism |
| #3842 | flat-torus determinant route pruned — reciprocal+π is a μ-sector fitting trap |
| #3848 (this) | abelian RT/RS torsion route pruned — it's a covolume, not a count |

Net: `1/(π b₁)` is derivable from **no** abelian photon normalization. The target
converges onto the **nonabelian S-matrix** route — where Front-2 siblings
(#3822 W_λ attack, #3823 McKay-mark refutation) already work. This is a genuine
cross-front link: the α_EM per-loop measure and the m_p/m_μ W_λ keystone may
share the same nonabelian RT S-matrix normalization as their common wall.

## Scope / discipline

- Scope-(a) route-narrowing; no `α_k` value produced or wired; no fit; does not
  manufacture `1/(π b₁)`; `1/(8π)` stays a phase-4 identification; L2 unchanged.
- Corpus-checked: the RT/quantum-dimension corpus is nonabelian W_λ (Beasley–
  Witten localization, colored Σ(2,3,5)); this abelian-torsion angle is distinct.

## Cross-references

- #3842 (μ-invariance prune): [`2026-07-17-alpha-em-photon-measure-mu-invariance-route-prune.md`](2026-07-17-alpha-em-photon-measure-mu-invariance-route-prune.md)
- #3834 (`ζ(0)=−b₁`): [`2026-07-17-alpha-em-zeta-anomaly-b1-count.md`](2026-07-17-alpha-em-zeta-anomaly-b1-count.md)
- Wall map: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- W_λ nonabelian RT (Front 2): [`2026-06-20-keystone-wlambda-beasley-witten-localization.md`](2026-06-20-keystone-wlambda-beasley-witten-localization.md)
- Ledger: [`alpha-em.md`](../coordination/alpha-em.md)
- Witness: `computations/alpha_em/alpha-em-rt-abelian-torsion-count-vs-covolume.witness.json`
