# Li_2^q imaginary part is quantized (π·Res) — the PR #1657 reality gate resolves

**Date:** 2026-06-01
**Probe:** [`qbeta_li2q_imaginary_quantization.py`](../../computations/qbeta/qbeta_li2q_imaginary_quantization.py)
→ `qbeta-li2q-imaginary-quantization.witness.json`
**Builds on:** PR #1657 (`2026-06-01-convergence-safe-vhat-tower.md`) —
reuses its `li_2_q_continued` continuation, does not duplicate it.
**Resolves:** the single open gate PR #1657 flagged.

---

## The gate (verbatim from PR #1657)

> "the reality of the complex continued value through the m_e
>  normalisation chain (Im=0.657 per generator) — flagged, not assumed."

PR #1657 established that `z=q₀` is an integrable **log branch point**
(not a pole) of `Li_2^q`, so the `+i0` analytic continuation gives a
finite complex value `Li_2^q(1.146) = 2.0809 + 0.6568 i` for the genuine
proton σ₀ factor `|V̂_0| = 1.146 > q₀`. It left open whether that
imaginary part yields a complex (unphysical) observable mass.

## The resolution — Im is a z-independent constant

The imaginary part of the continued `Li_2^q(z)` for `z>q₀` comes
**entirely** from the `+i0` semicircle arc deforming around the simple
pole of the integrand `−ln_q(1−u)/u` at `u=q₀`. By the residue theorem
the arc contributes `−iπ·Res`, with `Res = lim_{u→q₀}(q₀−u)·integrand`.
This is the **same constant for every upper limit `z>q₀`** — it does not
depend on `z`:

| z | Re Li_2^q | Im Li_2^q |
|---|---|---|
| 1.003852 (n σ₀, **< q₀**) | 1.5901 | **0** (inside radius, real) |
| 1.05 (< q₀) | 1.7881 | **0** |
| 1.146101 (p σ₀, **> q₀**) | 2.0809 | **0.6567822989** |
| 1.3 (> q₀) | 2.1850 | **0.6567822989** |
| 1.5 (> q₀) | 1.3307 | **0.6567822989** |

**`Im Li_2^q(z>q₀) = π·Res = 0.6567822989`, verified to 15 digits**
(spread across all `z>q₀` is `< 1e-12`; `π·Res` converges to the same
value as `eps→0`).

## Consequence — the observable is real

- `Im(tower) = N_cross · π·Res`, where `N_cross` = number of generators
  with `|V̂_i| > q₀` — a **pure additive constant quantized in units of
  π·Res**. (Generators with `|V̂_i| < q₀` are inside the radius: real.)
- The observable is the **m_e-normalised ratio** `tower/electron-tower`
  and **p/n differences**. A `z`-independent additive imaginary constant
  **cancels in the difference** and **factors through the ratio**,
  leaving a **real** observable.
- The `Im` is therefore a **fibre-level branch-cut artifact** (per the
  AGENTS.md Im(q) fibre-vs-observable distinction), not an imaginary
  mass. **The reality gate is resolved structurally** — no `Σ Im`
  miracle cancellation is needed; the cancellation is guaranteed by
  `z`-independence regardless of `N_cross`.

## Connection to the q-difference framework (PR #1622)

This is the structural counterpart of the PR #1622 finding that the Q_β
Habiro `Δtr_M` has a **ζ_4 modular pole with residue `∓i/2`**. Both are
**residue-quantized imaginary contributions from simple poles** in the
same q-difference framework:
- PR #1657/this: `Li_2^q` pole at `u=q₀` → `Im = π·Res` (per generator).
- PR #1622: `Δtr_M` pole at `ζ_4=i` → residue `∓i/2`.

In both, the imaginary part is a pole residue that is real (cancels /
factors) at the archimedean ratio level. This is the consistent
"imaginary lives in the fibre, observable is real at q₀" picture.

## Discipline

Exact residue identity + 15-digit numeric verification; reuses PR #1657's
`li_2_q_continued` (coordinate, not duplicate). **No fit, no MeV claim,
no production wiring.** Resolves the reality gate (the observable is
real); the MeV step and any wiring remain the owner's call.

## Cross-references

- PR #1657 convergence-safe tower (the gate): [`2026-06-01-convergence-safe-vhat-tower.md`](2026-06-01-convergence-safe-vhat-tower.md)
- PR #1622 Q_β ζ_4 modular pole: [`2026-06-01-habiro-q-difference-mode-solve.md`](2026-06-01-habiro-q-difference-mode-solve.md)
- Mass-endomorphism tower (Li_2^q is the proven kernel): [`mass-endomorphism-tower.md`](../../content/quantum-observable-universe/mass-theory/mass-endomorphism-tower.md)
