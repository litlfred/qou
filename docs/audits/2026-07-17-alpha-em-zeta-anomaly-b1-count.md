# α_EM Front 3: `ζ_{Δ₁}(0) = −b₁` — the area-free home of the bare `b₁` count

**Date:** 2026-07-17 · **Axis:** α_EM per-loop measure · **Tier:** measurement
(scope-(a) POSITIVE-partial; no `α_k` wired; no fit; `1/(8π)` stays a phase-4
identification). **Branch:** `claude/alpha-em-zeta-anomaly-b1-count-2026-07-17`
(PR #3834). Executes the structural lead of Front 3
([`2026-07-17-three-front-attack-specs.md §3`](2026-07-17-three-front-attack-specs.md)).

## The wall this addresses

Per [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md),
the α_EM single remaining wall is the **per-loop measure** `1/(π b₁) = 1/(8π)`:

- Data decisively **excludes `1/Area`** (−1419 ppb) and selects the bare-`b₁`
  form (works: +1.67 ppb 1-loop, −0.20 ppb 2-loop).
- But the bare `b₁ = dim H¹(M_Bring) = 8` count is **not derived** — it is a
  phase-4 identification `1/(8π) = 1/(π·dim H¹)`.

The spec's structural lead: *"the flat-torus scale anomaly `ζ(0) = −b₁` — the
one place a bare `b₁` count (not an area/covolume) canonically appears in a
ζ-regularized determinant."* This audit records the exact test of that lead.

## Result — `ζ_{Δ₁}(0) = −b₁`, exactly and area-free

The photon target is `J(M) = H¹/H¹(ℤ)`, a flat torus `T^{b₁}` (`Jac(Bring) ~ E⁴`,
`b₁ = 8`). The 1-loop operator is the Hodge Laplacian on 1-forms `Δ₁`. On a flat
torus the Levi-Civita connection is flat, so `Δ₁ = Δ₀ ⊗ Id_{ℝ^{b₁}}` — `b₁`
decoupled copies of the scalar Laplacian, with the `b₁` constant `ℝ^{b₁}`-valued
functions = the `b₁` harmonic 1-forms `dx_i` = the zero modes. Hence

```
ζ_{Δ₁}(0) = b₁ · E_Λ(0)
```

where `E_Λ(s) = Σ'_{n∈Λ} |n|^{-2s}` is the scalar Epstein zeta. The key fact:

> **`E_Λ(0) = −1` for every lattice `Λ`, in every dimension, independent of the
> covolume.** It is the `−1/s` residue of the small-`t` heat-kernel constant
> term (the `−1` that removes the zero mode from `θ_Λ(t)`), killed by the
> `π^s/Γ(s) ~ s` prefactor. The covolume `√det G` enters **only** the regular
> `1/(s − d/2)` pole and the (finite) dual-lattice integral — never the `−1/s`
> residue.

[`alpha_em_zeta_anomaly_b1_count_probe.py`](../../computations/alpha_em/alpha_em_zeta_anomaly_b1_count_probe.py)
verifies this via the completed-zeta heat-kernel split:

| lattice | `E_Λ(0)` | `\|E(0)+1\|` | `ζ_{Δ₁}(0) = d·E(0)` |
|---|---|---|---|
| ℤ¹ | −1.0000000 | 3.7e-8 | −1 |
| ℤ² | −1.0000000 | 2.6e-8 | −2 |
| ℤ³ | −1.0000000 | 2.2e-8 | −3 |
| **ℤ⁸** | −1.0000000 | 1.1e-8 | **−8** |
| non-cubic 2D, Gram `[[2,1],[1,2]]`, det 3 | −1.0000000 | 2.1e-8 | — (area-free ✓) |

The non-cubic det≠1 lattice confirms area/shape-independence: the `−1` does not
know the covolume. So `ζ_{Δ₁}(0) = −b₁ = −8` is the **bare count**, area-free —
the μ-scale-anomaly weight (`log det'Δ₁ → log det'Δ₁ − 2σ·ζ_{Δ₁}(0)` under
`g → e^{2σ}g`) carries a bare `−b₁`, exactly the object the spec pointed to.

## What is and is not derived (STRICT — anti-fitting)

- ✓ **`ζ_{Δ₁}(0) = −b₁`, area-free.** A *positive* structural finding: it answers
  "where does a bare `b₁` (not Area) come from?" and is **necessary** structure
  for the data-selected `1/(π b₁)`. This is the opposite of the kill-criterion's
  "only Area factors appear" negative.
- ✗ **Not the full `1/(π b₁)`.** `ζ(0)` fixes the bare `b₁` count (the numerator's
  mode count / μ-anomaly weight), but the `π` and the **reciprocal** form
  `1/(π b₁)` require the full determinant and the per-mode weight, not `ζ(0)`
  alone. These remain **OPEN** — the residual wall.
- The probe does **not** stretch μ-conventions to manufacture `8π`
  (the spec's fitting trap). It reports only what `ζ(0) = −b₁` genuinely gives.

## Scope / discipline

- Scope-(a) POSITIVE-partial measurement; no `α_k` value produced or wired; no
  fit to QOU observables; `1/(8π)` remains a phase-4 identification; L2 count
  unchanged.
- **Coordination:** distinct object from #3812 (α_EM per-loop-measure scoping) —
  this is the `ζ(0)` *source* of the bare `b₁`, not the per-loop weight. Intent
  posted on #3812.
- **Bib note:** the ζ-determinant / Epstein-zeta facts used are standard
  (Epstein 1903; Ray–Singer analytic torsion) — cited in prose only; no Lean
  `-- Ref:` is introduced here (the probe is compute-only), so no new
  `references.ts` entry is required for this PR.

## Cross-references

- Wall map: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- Bring Jacobian `E⁴` elliptic W-plane: [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
- Ledger: [`alpha-em.md`](../coordination/alpha-em.md)
- Witness: `computations/alpha_em/alpha-em-zeta-anomaly-b1-count.witness.json`
