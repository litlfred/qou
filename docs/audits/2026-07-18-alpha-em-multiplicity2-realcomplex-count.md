# α_EM per-loop measure `1/(8π)`: the `8π = 2·(4π)` multiplicity is the real-vs-complex Hodge doubling (count FORCED real-`b₁`; normalization form OPEN)

**Date:** 2026-07-18 · **Axis:** α_EM 2-loop / 1ppQ (#3612 headline) · **Tier:**
structural (scope-(a) — real count FORCED; reciprocal normalization form OPEN) ·
**Discipline:** no fit wired, no `c_k`, no tier change; no CODATA read; no
convention tuned toward `8π`.

## Question (the last crisp piece of the per-loop measure)

The α_EM ladder closes as the fixed point of `1/α = T + α·H`, with the per-loop
measure `H = [2]_q/(π·b₁)`, `b₁ = dim H¹(M_Bring) = 2g = 8` at genus `g = 4`.
Two axes were closed by the Front-3 cluster:

- **count axis** — `b₁ = 8` is settled as the area-free homological index
  `Tr_{H¹}(1) = −ζ_{Δ₁}(0) = 2g` (#3834 / #3896), the uniquely data-selected
  integer at ~3500σ (#3612-forcedness);
- **π-power axis** — the bare `1/π` closes to the archimedean 2D heat-kernel
  `(4πs)^{−d/2}|_{d=2} = 1/(4π)`, forced power `−1` (#3909 adjudication).

Both leave **one** residual, tracked as the "multiplicity `2` vs `b₁` / why
reciprocal" wall: `8π = 2·(4π)`. Sharp question (owner directive "2y"):

> Is the per-loop mode count the **real** harmonic-1-form count
> `b₁ = dim_ℝ H¹(M,ℝ) = 2g = 8`, or the **holomorphic** count
> `g = dim_ℂ H^{1,0} = 4`? Is the factor `2` the real-vs-complex Hodge doubling
> `b₁ = 2g` (FORCED), or a conflation of the heat-kernel base `4π` (d=2) with a
> distinct, un-forced loop multiplicity `2`?

## Lever (a proved corpus invariant)

The count enters as the ζ-regularized index of the **real Hodge–de Rham
Laplacian** `Δ₁` acting on `Ω¹(M,ℝ)`:

```
Tr_{H¹}(1) = −ζ_{Δ₁}(0) = b₁ = 2g = 8         (#3834 / #3896, area-free)
```

`Δ₁` is the Laplacian on **real** 1-forms; its harmonic kernel is `H¹(M,ℝ)`, of
real dimension `b₁ = 2g` — **not** the `∂̄`-Laplacian on `H^{1,0}` (dimension
`g`). The photon is a **real** `U(1)` gauge field (its connection is a real
1-form), so the self-energy propagator that carries the per-loop measure lives on
the *same* real harmonic sector as the proved n=1 zero-mode
`photonZeroModeShift = b₁/Area` (#2114). Hence the count is the real `b₁`, and
the `b₁ = 2g` doubling is the real⊕complex Hodge splitting

```
H¹(M,ℝ) ⊗ ℂ = H^{1,0} ⊕ H^{0,1},   each summand dim_ℂ = g.
```

## Result

### A. Real-vs-holomorphic sub-question — CLOSES (scope-(a), forced)

The per-loop mode count is the **real** harmonic-1-form count `b₁ = 2g = 8`, not
the holomorphic `g = 4`:

| reading | denominator | vs target `8π` |
|---|---|---|
| **real** `π·b₁` | `π·8 = 8π` | ✓ hits `8π` |
| holomorphic `π·g` | `π·4 = 4π` | ✗ a **factor 2 short** |

The merged real-`Δ₁` ζ-index `−ζ_{Δ₁}(0) = 2g` selects the real count, and the
reality of the gauge field forbids the holomorphic reading. The factor `2` in
`8π = 2·(4π)` **is** the real⊕complex Hodge doubling — FORCED by the reality of
`Δ₁`, not a conflation.

**Lean (sorry-free, `lean`-direct exit 0).** Added to
[`QOU.Archimedean.PhotonIRZeroMode`](../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean):

- `holomorphicOneFormCount (g) : ℕ := g` — `dim_ℂ H^{1,0}`;
- `betti1_eq_two_holomorphic : betti1 g = 2 * holomorphicOneFormCount g` — the
  real-vs-complex doubling `b₁ = 2·g`, pinning where the `2` lives;
- `selfEnergyDenominator_count_is_real :
  selfEnergyDenominator g = π·(2·holomorphicOneFormCount g)` — the self-energy
  denominator is `π·b₁` with the **real** count, `= 2·(π·g)` exhibiting the
  forced doubling.

### B. Normalization-FORM sub-question — stays OPEN (scope-(a))

This does **not** derive the reciprocal form `1/(π·b₁)`. `8π` admits two
numerically identical but structurally distinct normalization readings:

- **(P)** `π · b₁` — one bare loop-`π` traced over the `b₁ = 8` real harmonic
  sectors (count-carrying, single `π`; the #3896 index home);
- **(H)** `(4π) · 2` — the 2D heat-kernel Gaussian base `(4π)^{d/2}|_{d=2} = 4π`
  (the #3909-adjudicated *derived* `π`) × a residual `2`.

Under reading (H) the `4π` is the archimedean heat-kernel Gaussian — **not**
`π·g` — so its residual `2` is a *distinct* loop-multiplicity that the
real-vs-complex argument does **not** supply. No proved invariant selects (P)
over (H). The reciprocal-form derivation (why the count enters as `1/(π·b₁)`
rather than `b₁/(4π)` or `1/(4π·b₁)`) remains the open wall.

## What this does and does NOT establish

- **DOES:** settles the *count* — real `b₁ = 8`, not holomorphic `g = 4` — and
  proves (Lean, sorry-free) that the `8π`'s factor `2` is exactly the
  real⊕complex Hodge doubling `b₁ = 2g`, forced by the reality of the photon
  Laplacian.
- **DOES NOT:** derive the reciprocal normalization *form*. A factor of `2` is
  the single easiest thing to fit; this probe claims **only** the count (via the
  proved real ζ-index), and explicitly does **not** claim the form. The `1/(8π)`
  measure stays a phase-4 identification.

## Scope discipline (anti-laundering)

No CODATA read; no convention tuned toward `8π`; the real count is FORCED by the
reality of the merged `Δ₁`-index (a proved corpus invariant), not chosen. The
normalization-form residual is stated OPEN, not papered over. No `α_k` wired; no
fit; no tier change.

## Cross-references

- π-power adjudication (closed the `1/π` to the heat-kernel, flagged this exact multiplicity residual): [`2026-07-18-alpha-em-pi-origin-adjudication.md`](2026-07-18-alpha-em-pi-origin-adjudication.md)
- π-decomposition (the `8π = 2·(4π)` vs `π·b₁` two-reading split): [`2026-07-18-alpha-em-pi-decomposition.md`](2026-07-18-alpha-em-pi-decomposition.md)
- Homological-index count `−ζ_{Δ₁}(0) = 2g` (#3896) + area-free ζ-anomaly (#3834): [`2026-07-17-alpha-em-zeta-anomaly-b1-count.md`](2026-07-17-alpha-em-zeta-anomaly-b1-count.md)
- Forcedness of the integer `8` (~3500σ): [`2026-07-17-alpha-em-perloop-integer-forcedness.md`](2026-07-17-alpha-em-perloop-integer-forcedness.md)
- Count-carrying-object negative (`Σd_i²` reproduces 8 only trivially): [`2026-07-18-alpha-em-count-carrying-object.md`](2026-07-18-alpha-em-count-carrying-object.md)
- Proved n=1 zero-mode `b₁/Area` + Lean home: [`../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean)
- Probe + witness: [`../../computations/alpha_em/alpha_em_multiplicity2_realcomplex_probe.py`](../../computations/alpha_em/alpha_em_multiplicity2_realcomplex_probe.py), `computations/alpha_em/alpha-em-multiplicity2-realcomplex.witness.json`
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
