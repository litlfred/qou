# α_EM `1/(8π)`: the non-D route — `b₁` enters as a mode-COUNT index, not a quantum dimension

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure · **Tier:** structural probe
(scope-(a) POSITIVE-for-count; C14; no fit; nothing wired; `1/(8π)` stays a
phase-4 identification).

## The question this closes (positively, for the count)

The photon per-loop measure `1/(π b₁) = 1/(8π)` (`b₁ = dim H¹(M_Bring) = 2g = 8`)
factors into a **count** `b₁` and a **`1/π` per-mode weight**. The shared-wall
hypothesis (#3853) proposed that `b₁` enters as the keystone **total quantum
dimension** `D = √(Σ_λ d_λ²)` under a nonabelian `S₀₀ = 1/D`. That was
**falsified on both sides**:

| side | object | value | ∈ {8, 8π}? | PR |
|---|---|---|---|---|
| observable | `D(q₀) = √(Σ_{λ⊢5} d_q(λ)²)` | `11.3569` | no (`D/8 = 1.4196`) | #3871 |
| fibre | `D(ζ)`, `ζ=e^{iπ/5}`, E8-mark / SU2₃ MTC, 2 flat conns | `{1.663, 2.351, 2.690, 3.804}` | no (`D/8 = 0.208…0.476`) | #3883 |

The falsifications explicitly left open the alternative: **does `b₁` enter as a
mode-COUNT trace — an integer index `Tr_{H¹}(1) = b₁ = 2g` — rather than as the
total quantum dimension?** This probe tests exactly that, head-to-head.

## Result — the count SUCCEEDS on the non-D route

Reusing the merged Epstein `E_Λ(0) = −1` / `ζ_{Δ₁}(0) = b₁·E_Λ(0)` machinery
(#3834), the probe recomputes the index and contrasts it with the two failed `D`
objects:

```
INDEX  Tr_{H¹}(1) = −ζ_{Δ₁}(0) = 2g   =  8.00000009   → EXACT integer     ✓
D_obs(q₀)  = √(Σ d_q²)                 = 11.3569       → miss (1.4196)     ✗
D_fibre(ζ) ∈ {1.663, 2.351, 2.690, 3.804}             → miss (0.21…0.48)  ✗
```

(`Tr_{H¹}(1) = 8.00000009` is the Epstein integral's numerical `8` to `9e-8`;
`E_{ℤ^d}(0) = −1` verified for `d = 1,2,3,8`.)

**`b₁` is a homological integer index — `Tr` of the identity over the `b₁`
harmonic 1-form sectors, `= −ζ_{Δ₁}(0) = 2g`, area-free and q-INDEPENDENT.** The
`D` route's failure was an **object-type error**, not a numeric near-miss: `D(q)`
is a transcendental function of `q` (grows with `q`; `D(1) = √120 = 10.954`) and
was *never* going to equal the integer `8`. The correct object is the index, and
the corpus already established it exactly (#3834). **D was the wrong object; the
mode-count index is the right one.**

## What remains open — STRICT scope, no over-claim

This probe settles **only the COUNT**. The two residual pieces are:

1. **The reciprocal FORM (`1/b₁` vs `b₁`).** This is **orthogonal** to
   count-vs-dimension: whether `b₁` is read as an index or as `D`, the measure
   still uses the *reciprocal* `1/b₁`, and **nothing here forces `1/b₁` over
   `b₁`**. The index reading is **not** cleaner than `D` on this axis — the
   reciprocal-form problem is exactly as unforced under either. The win is
   object-type (the count is a genuine integer index), not the form.
2. **The `π`.** Untouched here. Its status is R1 canonical / R2·R3 candidate
   leads per
   [`docs/audits/2026-07-18-alpha-em-pi-origin-three-reading-reconciliation.md`](2026-07-18-alpha-em-pi-origin-three-reading-reconciliation.md).
   This probe does **not** re-open it and does **not** manufacture `8π`.

So the residual α_EM wall narrows to EXACTLY two orthogonal pieces — the
reciprocal form and the `π` — with the **count** now on a firm non-D footing.

## Verdict

Scope-(a) **POSITIVE-for-count** (per the anti-over-claim discipline): the non-D
route succeeds for the count. `b₁ = 8` enters the measure as the integer
mode-count index `Tr_{H¹}(1) = −ζ_{Δ₁}(0) = 2g`, exact and area-free — the object
the D route mis-identified. This is a positive structural finding, not a
derivation of `1/(8π)`: the reciprocal form and the `π` stay open, `1/(8π)`
remains a phase-4 identification, no `α_k` wired, no fit.

## Artifacts

- Probe: [`computations/alpha_em/alpha_em_nonD_index_route_probe.py`](../../computations/alpha_em/alpha_em_nonD_index_route_probe.py)
- Witness: [`computations/alpha_em/alpha-em-nonD-index-route.witness.json`](../../computations/alpha_em/alpha-em-nonD-index-route.witness.json)

## Cross-references

- Count area-free (index home): #3834 · Epstein `E_Λ(0)=−1` machinery reused here
- Shared-wall falsified observable side: #3871 ·
  [`2026-07-18-alpha-em-shared-wall-gate-falsified-observable-side.md`](2026-07-18-alpha-em-shared-wall-gate-falsified-observable-side.md)
- Shared-wall falsified fibre side: #3883 ·
  [`2026-07-18-alpha-em-fibre-Dzeta-shared-wall.md`](2026-07-18-alpha-em-fibre-Dzeta-shared-wall.md)
- `π` origin reconciliation (do not re-open): #3864 / #3879 / #3831 ·
  [`2026-07-18-alpha-em-pi-origin-three-reading-reconciliation.md`](2026-07-18-alpha-em-pi-origin-three-reading-reconciliation.md)
- Ledger: `docs/coordination/alpha-em.md`
