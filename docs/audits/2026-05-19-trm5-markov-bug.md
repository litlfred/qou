# Bug fix: pyhecke.gram TR_M[5] Markov-trace value at H_3(q)

**Date:** 2026-05-19
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Discovery context:** while extending the SDP-T_β derivation to per-Wedderburn-block decomposition (Path B of the closure roadmap), found that the y_λ values from `y-lambda-at-q0.witness.json` did NOT satisfy `tr_M(b_i) = Σ_λ y_λ·χ_λ(b_i)` for the NF basis element `e_- = σ_0·σ_1·σ_0`. Least-squares residual ~0.12 instead of 0.

## The bug

`tools/pyhecke/python/pyhecke/gram.py` line 50 had:

```python
TR_M = np.array([1.0, z, z, z ** 2, z ** 2, z ** 3])
```

The last entry (for NF basis element `e_- = (0,1,0) = σ_0·σ_1·σ_0`) was `z³`, but the **correct value via Markov-trace recursion** is `h·z² + z`.

Same bug pattern at line 178 in `_TR_M_FRAC` (Fraction version): `_Z_FRAC ** 3` → should be `_H_FRAC * _Z_FRAC**2 + _Z_FRAC`.

## Markov-trace derivation (correct value)

For the Geck-Lambropoulou / Ocneanu-Wenzl Markov trace on H_3(q) defined by:
- `tr_M(1) = 1`
- `tr_M(σ_i·x) = z·tr_M(x)` for `x ∈ H_{i}` (sub-algebra)
- cyclicity: `tr_M(xy) = tr_M(yx)`
- Hecke: `σ_i² = h·σ_i + 1`

The value of `tr_M(σ_0·σ_1·σ_0)` reduces:

```
tr_M(σ_0·σ_1·σ_0)
  = tr_M(σ_1·σ_0·σ_0)   (cyclicity)
  = tr_M(σ_1·σ_0²)
  = tr_M(σ_1·(h·σ_0 + 1))    (Hecke)
  = h·tr_M(σ_1·σ_0) + tr_M(σ_1)
  = h·(z·tr_M(σ_0)) + z·tr_M(1)    (Markov axiom, σ_0 ∈ H_2)
  = h·z² + z
```

At q_0 ≈ 1.110:
- `h·z² + z = 0.2091·0.0623 + 0.4993 = 0.5514`
- `z³ = 0.1245`

The discrepancy is a factor of 4.4× — significant.

## Visible symptom: Gram matrix non-symmetric

Before the fix, the Gram matrix `G[i,j] = tr_M(b_i · b_j)` was non-symmetric (∥G − G^T∥ > 1e-3) — because b_i·b_j and b_j·b_i are NF-equal up to braid relations, but their bug-affected trace evaluations differed when products had e_- components.

After the fix, `G` is symmetric to machine precision. This was the visible artifact that motivated the bug hunt.

## Impact on downstream computations

The bug affects any computation that:

1. Uses `pyhecke.gram.TR_M` directly for the trace of a NF-basis element with non-zero `e_-` coefficient, OR
2. Uses `pyhecke.gram.G` (the Gram matrix `tr_M(b_i·b_j)`), since many products reduce to NF elements involving `e_-`.

Modules importing `pyhecke.gram.TR_M` (from grep):

- `computations/aK_via_lp_dual_hecke_basis.py`
- `computations/qbeta/qbeta_decay_sdp_solver.py` (mine — in this PR)
- `computations/confinement-operator-selection.py`
- `computations/gram-matrix-dual.py`
- `computations/pn_alpha_lp_dual.py`
- `computations/molecular-frobenius-lp.py`
- Several files in `_deprecated/`

**Verification needed for each downstream module:** rerun its primary computation against its existing witness and check the diff. Modules using NF elements without `e_-` coefficient (e.g., pure γ, σ_0, σ_1 expansions) are unaffected.

## My SDP-T_β: impact analysis

The SDP-T_β min-L2-norm fit with `t·x = Q_β/E_0` has its NF coefficients **change** when TR_M is corrected:

| Element | Old x* (bug) | New x* (fixed) |
|---------|------------:|---------------:|
| γ       | 0.11406659  | 0.09698419     |
| σ_0     | 0.05695577  | 0.04842618     |
| σ_1     | 0.05695577  | 0.04842618     |
| L_+     | 0.02843917  | 0.02418018     |
| L_-     | 0.02843917  | 0.02418018     |
| **e_-** | **0.01420026** | **0.05348129** |

The e_- coefficient quadrupled (proportionally to TR_M[5]'s correction).

**However**, the c_k extraction via R(q_0) = Q_β/(Q_A·cos) is **unchanged** because R(q_0) depends only on Q_β, Q_A, and cos — none of which involve the NF Markov trace. So:

- `qbeta-decay-sdp-knot-operator.witness.json` — T_β NF coefficients need updating
- `qbeta-decay-sdp-full-ck-derivation.witness.json` — c_k values UNCHANGED (verified)

## Per-Wedderburn-block consistency restored

The bug made the linear system `tr_M(b_i) = Σ_λ y_λ·χ_λ(b_i)` over-determined and inconsistent (least-squares residual 0.12). After the fix:

- Residual: **3.7e-32** (essentially zero — exact identity)
- y_λ values from `y-lambda-at-q0.witness.json` now satisfy the identity EXACTLY

This was the motivation: per-Wedderburn-block decomposition for the c_k derivation requires this consistency. The path is now unblocked.

## Downstream verification sweep (2026-05-19, parallel agent)

Verified all 5 modules importing `pyhecke.gram.TR_M`:

| Module | Status | Diagnosis |
|--------|--------|-----------|
| `aK_via_lp_dual_hecke_basis.py` | **MAJOR** | x_star changes ~30×, now σ₀↔σ₁ symmetric (was asymmetric pre-fix). LP active-set unchanged, strong duality holds. Post-fix is correct. |
| `confinement-operator-selection.py` | **MAJOR** | Gram determinant changes −0.36 → −0.19, eigenvalues shift; NF decompositions of operators unchanged. Post-fix Gram is symmetric (was non-symmetric pre-fix). |
| `gram-matrix-dual.py` | **MAJOR** | Markov trace of e_⁻ corrected: 0.124 → 0.551. Eigenvalues shift accordingly. Post-fix is correct. |
| `pn_alpha_lp_dual.py` | **UNAFFECTED via import** but **LATENT SHADOWING BUG** at line 206: `TR_M_BASIS = np.array([1.0, z_mark, z_mark, z_mark**2, z_mark**2, z_mark**3])` — locally redefines TR_M with the buggy `z**3` pattern, shadowing the imported (fixed) `_PG_TR_M`. Script must be patched separately. |
| `molecular-frobenius-lp.py` | **UNAFFECTED via import** but **LATENT SHADOWING BUG** at line 56: `TR_M = np.array([1.0, z, z, z**2, z**2, z**3])` — same shadowing pattern. Script must be patched separately. |

**Action: NEW bug fix needed** — `pn_alpha_lp_dual.py:206` and `molecular-frobenius-lp.py:56` both have local TR_M arrays that hard-code `z**3` (the same bug). Fix: remove the local arrays, use the imported `_PG_TR_M`.

**Recommendation per the verification agent**: handle witness regeneration + script-shadow cleanup in a **dedicated follow-up PR**. This PR's scope is the core `pyhecke.gram` fix; the downstream consequences are quantitatively significant (e.g., aK x_star changes 30×) and warrant their own review.

## Cross-references

- `tools/pyhecke/python/pyhecke/gram.py` lines 50 + 178 — fix locations
- `computations/y-lambda-at-q0.witness.json` — y_λ values (correct, now consistent)
- `computations/qbeta/qbeta-decay-sdp-knot-operator.witness.json` — needs T_β NF coeff update
- `docs/audits/2026-05-19-qbeta-ladder-sdp-c2-c3-derived.md` — SDP-T_β derivation (c_k unchanged by fix)
- `docs/audits/2026-05-19-qbeta-ladder-knot-operator-general-statement.md` — Path B per-block scaffolding (now usable)
- `computations/pn_alpha_lp_dual.py` line 206 — latent shadowing bug, needs follow-up fix
- `computations/molecular-frobenius-lp.py` line 56 — latent shadowing bug, needs follow-up fix
