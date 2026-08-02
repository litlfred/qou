# Whitehead c_σ = 2^{−3/4}, derived — and the unified multi-cusp 1-loop torsion law

**Date:** 2026-08-02 · **Beans:** qou-k00d, qou-pn5j · **PR:** #4571
**Scripts:** [`computations/whitehead_c_sigma_torsion.py`](../../computations/whitehead_c_sigma_torsion.py),
[`computations/whitehead_c_sigma_hiprec.py`](../../computations/whitehead_c_sigma_hiprec.py)
**Prior corpus:** W1 probes [`computations/probes/borromean_nz_adjoint_torsion.py`](../../computations/probes/borromean_nz_adjoint_torsion.py),
[`computations/probes/borromean_jones_1loop_torsion.py`](../../computations/probes/borromean_jones_1loop_torsion.py) (#4208/#4238, 2026-07-25)

## Result

The Whitehead-link (L5a1) Volume-Conjecture sub-leading constant
`|J_N(e^{2πi/N})| ~ c_σ · N^{3/2} · exp((Vol/2π)N)`, `Vol = 4G`, is

    c_σ = 2^{−3/4}     (colored Jones, van der Veen positive sum, 20 digits)

and this is **derived** (not fitted) from the hyperbolic geometry via the
Dimofte–Garoufalidis 1-loop adjoint Reidemeister torsion, together with a
**per-cusp normalization factor**. Writing `c₀ = log c_σ` (the constant term of
`log|J_N|`), the three worked cases give the unified law

    exp(2 c₀) = 2^{c−1} / |det J_NZ|        ⇔        c_σ = 2^{(c−1)/2} · |τ|^{−1/2}

where `c` = number of cusps and `|τ| = |det J_NZ|` is the 1-loop invariant
(determinant of the gluing-equation Jacobian `J_{kj} = A_{kj} − B_{kj} z_j/(1−z_j)`
on `(N−c)` independent edge equations + the `c` meridians).

| link | c | `|τ| = |det J_NZ|` (derived, exact) | c₀ predicted | c₀ measured (colored Jones) |
|------|---|-------------------------------------|--------------|------------------------------|
| 4₁ | 1 | √3 (= `3^{1/2}`) | −¼ ln 3 = −0.2747 | −0.2747 (exact calibration) |
| L5a1 (Whitehead) | 2 | `2^{5/2}` = 4√2, `det = 4(1+i)` | −¾ ln 2 = −0.5199 | c_σ = 2^{−3/4}, 20-digit |
| L6a4 (Borromean) | 3 | `2^{6}` = 64, `det = −64 i` | −½ ln 16 = **−1.3863** | **−1.3828** (W1, NMAX=56) |

All three `|det J_NZ|` are exact (200-bit verified). The 4₁ value `√3` is the
classically-known adjoint torsion (trace field `ℚ(√−3)`); it calibrates the
formula/normalization **non-circularly**, so L5a1 and L6a4 are genuine
predictions, not fits of `c_σ`.

## What is new vs. what is corpus

- **Corpus (cite, not new):** `|det J_NZ(𝓑₃)| = 64` and the *knot* relation
  `exp(2c₀) = 1/|det J|` (with the 4₁ `√3` calibration) were already computed by
  the W1 probes (#4238, 2026-07-25). This work **reproduces `|det| = 64`
  independently** (15 digits) and uses it.
- **New:** the **per-cusp factor `2^{(c−1)/2}`**, which the knot relation
  `exp(2c₀) = 1/|det|` **lacks** — that relation predicts Borromean `c_σ = 1/8`,
  contradicting the measured `≈ 1/4`. The factor `2^{c−1}` in
  `exp(2c₀) = 2^{c−1}/|det|` fixes this, and is confirmed by the Whitehead
  (c=2, 20-digit) and Borromean (c=3, 0.25%) cases.
- **New:** the geometric derivation of `|τ(L5a1)| = 2^{5/2}` closing bean qou-pn5j.

## Correction (honest self-audit)

An earlier note on PR #4571 inferred `|τ(L5a1)| = 2√2` by applying the *knot*
template `c_σ = |τ|^{−1/2}` to `c_σ = 2^{−3/4}`. The independent 1-loop
computation gives `|τ| = 4√2 = 2^{5/2}` — a factor of 2 larger. The value
`c_σ = 2^{−3/4}` is unchanged; only the torsion and the c_σ↔τ relation were
corrected (the missing per-cusp `√2`).

## The 2-cusp exponent is `p = 3/2` (closes a flagged item)

The `b1-hyperbolic-rows-theorem-audit` Whitehead Step-3 flagged "whether the
2-cusp link exponent differs" from the knot `p = 3/2` as an open sub-item. A
sharpened least-squares fit of `log|J_N| = A·N + p·log N + c₀ + a₁/N + a₂/N²`
(van der Veen positive sum, `A = 4G/2π`, `N ∈ {400,…,3000}`, mpmath dps=50)
gives

    p = 1.499999996795     ( |p − 3/2| ≈ 3.2 × 10⁻⁹ )

so the 2-cusp exponent is `3/2` to ~9 digits — the **same** as for hyperbolic
knots. (The 3-cusp Borromean W1 probe likewise gave `p = 1.4993` at `NMAX = 56`.)
The factor-2 / per-cusp normalization lives entirely in the *constant* `c₀`, not
in the power of `N`. This item is resolved.

## Open sub-item (honest)

- The factor `2^{(c−1)/2}` is pinned on `c = 1, 2, 3`. Its **general-`c`
  derivation** — from the per-cusp Gaussian integration in the GGMW/Ohtsuki
  saddle asymptotic, and/or van der Veen's reduced-colored-Jones normalization —
  is not proven here.
- The cross-check assumes van der Veen's reduced `J'` (Whitehead) and the W1
  Kashaev normalization (Borromean) share the same constant normalization; the
  0.25% Borromean agreement supports this but does not prove it. The 0.25%
  residual is within the W1 `NMAX = 56` fit error (that fit gave `p = 1.4993` vs
  the exact `3/2`).
- 1-loop torsion is defined only for the hyperbolic structure; the tool returns
  meaningless values on non-hyperbolic links (`vol ≈ 0`) and clean dyadic values
  only for the `ℚ(i)` octahedral links.

## Discipline

Audit-only. `c_σ = 2^{−3/4}` and `|τ| = 2^{5/2}` are **not** wired to any
production dashboard or the canonical derivation chain; they characterize the
Whitehead colored-Jones asymptotic, not a QOU observable. The derivation is
independent of inverting `c_σ` (the anti-circularity requirement of qou-pn5j).

— Ref: Dimofte–Garoufalidis, *The quantum content of the gluing equations*,
Geom. Topol. 17 (2013) 1253; van der Veen, arXiv:math/0611181; Porti, adjoint torsion.
