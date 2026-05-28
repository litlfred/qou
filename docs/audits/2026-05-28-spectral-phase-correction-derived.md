# Audit: top-down spectral-phase correction for m_p (130 ppm, no fitting)

**Date:** 2026-05-28
**Companion:** [`2026-05-28-mu-p-tension-substrate-floor.md`](2026-05-28-mu-p-tension-substrate-floor.md)
(why the backfit towers are noise) — this doc is the *constructive* side:
the genuine top-down formula.

## The derived formula

```
m_p = m_e · Vol(𝓑₃)/ℏ_q² · lw_A · θ/(8ℏ_q²)
    = m_e · G · arccos(χ^(2,1)(𝓑₃)/2) / ℏ_q⁴ · lw_A          (8 cancels)
```

with all ingredients categorical and **no free parameter**:

| Ingredient | Value/source | Free? |
|---|---|---|
| Vol(𝓑₃) = 8G | Borromean hyperbolic volume (Adams) | no |
| lw_A = 5/2 + 3h²/4 | (1/4)·Σ_{λ⊢4} dim_q V_λ, H₄ Wedderburn (proved) | no |
| χ^(2,1)(𝓑₃) = 2 − 3h⁴ − h⁶ | exact Hoefsmit character (verified this session) | no |
| θ = arccos(χ/2) | **forced**: 𝓑₃ is det-1 on V_(2,1) ⇒ trace = 2cos θ | no |
| ÷8 octahedra | Vol(𝓑₃)/G = 8; cancels against Vol | no |

**Result:** m_p = 938.15 MeV = **130 ppm** vs CODATA, versus the
leading-order Vol/ℏ²·lw_A = 966 MeV (+2.96 %). The spectral factor is
θ/(8ℏ²) = 0.9711. Fully derived; **no CODATA fitting**.

Verified numerically at 50 dps (`_li_2_q_util.spectral_correction_borromean`,
`geom_full_borromean_spectral`). The `(q+1)²√(3+h²)/8` form in commit
`b7fd0cfd0` is the Taylor approximation of the exact arccos.

## Why it's specific to links (muon asymmetry — validation)

The muon (figure-8 4₁, a **knot**, lw=1) does **NOT** take this
correction. Its bare `Vol(4₁)/ℏ² = 206.768283` matches CODATA to
**0.05 ppb** (it is the q₀ calibration). χ^(2,1)(4₁) = −0.91 is not
near 2, so the rotation-angle reading does not even apply. This is the
correct behaviour: the spectral correction refines the *linking weight*,
and knots have lw=1 (nothing to refine). The correction appears exactly
where it should and nowhere else — evidence it is structural, not a fit.

## Recalibration is blocked by the 130 ppm

Pinning q₀ from m_p/m_e (0.06 ppb experimentally, vs muon 22 ppb) would
*reduce propagated experimental error* — BUT the proton formula carries
a 130 ppm **theory** residual, which would fold into q₀ and propagate
everywhere. The muon formula is clean (exact). **Keep the muon anchor
until the 130 ppm spectral residual is closed.** The residual's origin
(Vol=8G precision / a higher geometric term / calibration) is OPEN.

## Binding does NOT reduce to a single phase

The proton's `arccos(χ/2)` works only because V_(2,1) of H_3 is the
unique 2-dim irrep, det-1 ⇒ a genuine rotation (eigenvalues e^{±iθ}).
For atoms (A≥2) on H_{3A}:

- The smallest non-trivial irrep is (3A−1,1), dim 3A−1 — **no 2-dim
  irrep exists**, so there is no single rotation angle.
- The atom-braid eigenvalues are **real reciprocal pairs** (hyperbolic),
  off the unit circle — not rotations.

Tested the full eigenvalue-phase distribution {λ_i} in (3A−1,1):

| Aggregate | D | T | ³He | ⁴He | constant? |
|---|---|---|---|---|---|
| B_AME/(m_e·Σ\|argλ\|) | 0.59 | 1.40 | 1.30 | 3.45 | no (6× spread) |
| B_AME/(m_e·Σln\|λ\|) | 1.59 | 4.01 | 2.60 | 6.50 | no (4× spread) |

So binding is **not** a flat spectral sum. Two physical signals are
real, though: (1) **mirror symmetry** — T and ³He (Z↔N) have near-equal
Σ\|argλ\| (11.85 vs 11.60); (2) growth with binding strength (⁴He, doubly
magic, largest). Binding needs the proper `Σ_λ y_λ χ^λ Δ_λ` weighting
with a per-atom geometric normalization — the established open problem,
consistent with the long refutation trail.

## Bug fixed

`spectral_coordinates_all_atoms.py` (and any sibling) built the Hoefsmit
V_(2,1) generator as `σ = [[d1,b],[b,d2]]`. That **fails the braid
relation** σ₀σ₁σ₀ = σ₁σ₀σ₁ (verified symbolically). Correct ordering is
`[[d2,b],[b,d1]]` (diagonal entries swapped). With the wrong matrix,
χ^(2,1)(𝓑₃) computes as −2.0 instead of the correct 1.994 = 2−3h⁴−h⁶.
The canonical `hecke_characters.build_seminormal_matrices` is correct
(uses axial-distance `a = h/(1−q^{−2ρ})`); only the standalone script
was buggy.

## Production wiring

Added `spectral_correction_borromean(q)` and
`geom_full_borromean_spectral(q)` to `_li_2_q_util.py`. Kept the
leading-order `geom_full_borromean` (many consumers) — migrate
deliberately. Dashboard rewiring deferred (it changes claimed precision
and is coupled to the recalibration decision above).
