# Habiro q-difference equation — mode-by-mode solve (partial-fraction = Fourier modes)

**Date:** 2026-06-01
**Probe:** [`habiro_q_difference_mode_solve.py`](../../computations/habiro/habiro_q_difference_mode_solve.py)
→ `habiro-q-difference-mode-solve.witness.json`
**Goal arm:** 1ppQ-Q_β (`docs/coordination/1ppq-qbeta.md`)
**Builds on:** the root-of-unity spectrum of PR #1622.
**Status:** spectral **solve** (exact, no fit). Decomposes Δtr_M into its
exact q-difference Fourier modes; the bridge to the ladder `c_k` remains
the one open step.

---

## TL;DR

Solving the Habiro q-difference equation `(1−σ_q)F = δ(q;q)_∞` is, under
the Fourier transform that diagonalises the shift `σ_q`, exactly the
**partial-fraction decomposition** of the rational `Δtr_M(u)` over its
poles (`u = q^{1/2}`). It splits into three exact spectral sectors:

```
Δtr_M = [ −u⁴/4 − u³/2 + u/2 − 1/2 ]      (A) entire polynomial
      + [ 1/(u²+1) ]                       (B) ζ_4 cyclotomic pole pair
      + [ 1/(2u) − 1/(2u³) + 1/(4u⁴) ]     (C) u=0 Laurent tower
```

Reconstruction `A+B+C = Δtr_M` holds **exactly** (assertion, sorry-free).

## The three sectors as q-difference modes

Each pole of `Δtr_M` is one Fourier mode of `σ_q`:

| Sector | Form | Physical reading |
|---|---|---|
| **A — entire** | `−u⁴/4 − u³/2 + u/2 − 1/2` | the polynomial "bulk" (no singularity) |
| **B — ζ_4 cyclotomic** | `1/(u²+1)`, residues `∓i/2` at `u=±i` | the WRT **level-4 modular mode** — the genuine q-difference singularity |
| **C — u=0 tower** | `u^{-1}, u^{-3}, u^{-4}` with coeffs `½, −½, ¼` | the short-distance / high-energy modes |

## The modular data (exact constraint on f)

The ζ_4 residues are `Res_{u=+i} = −i/2`, `Res_{u=−i} = +i/2` — a clean
**conjugate pair `∓i/2`**. This `1/2` is the WRT level-4 modular phase.
Any candidate scaling map `f` must reproduce this exact half-integer
modular residue — a hard structural constraint, not a fitted value.

## Bar-symmetry: the physical content is a clean 1/2

Under charge conjugation `u ↦ 1/u` (= `q ↦ q⁻¹`, exact since `u=√q`),
splitting each sector into bar-even (physical) / bar-odd:

- **Sector B (ζ_4 modular) bar-even part = exactly `1/2`** — a pure
  constant. The modular sector's charge-conjugation-symmetric (physical)
  content is a phase-`1/2`.
- Sectors A and C have non-trivial bar-even parts (rational in `u`).

PR #1602 established that `f` must be the bar-even (cancellation)
construction. This solve identifies the **exact bar-even content of each
mode** — most cleanly, the modular sector contributes the constant `1/2`.

## What remains open (the one bridge)

The mode decomposition is now **exact** in the Habiro variable `u = √q`.
The single remaining step is the **change of variable** `u = √q ↦
u_ladder = b·ℏ²` to read off the ladder coefficients `c_k` from these
modes. Because the modes are known exactly, this bridge is a **defined
computation**, not a search:

- the entire sector (A) contributes a finite polynomial in `c_k`;
- the modular sector (B) contributes the `1/2` modular phase;
- the `u=0` tower (C) contributes the short-distance corrections.

This is the concrete next probe. Note the `u`-collision discipline
(registered in `notation-collisions.md`, PR #1622): the bridge must keep
the two `u`'s explicitly distinct (`u` Habiro vs `u_ladder`).

## Discipline

Exact symbolic throughout; reconstruction verified exact; 3 assertions
pass. **No fitted form; no `c_k` value claimed; no closure.** The solve
characterizes the q-difference mode structure; the ladder bridge is the
remaining open step. Tiered per `canonical-ck-tiered-not-binary`.

## Cross-references

- Root-of-unity spectrum (boundary data): [`2026-06-01-habiro-q-difference-fourier-spectrum.md`](2026-06-01-habiro-q-difference-fourier-spectrum.md)
- Eigenphase ≠ f (bar-even constraint): [`2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md`](2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md)
- Order audit (per-block √u vs ladder u³): [`2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`](2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md)
- Habiro derivation gap plan: [`2026-05-30-qbeta-habiro-derivation-gap-plan.md`](2026-05-30-qbeta-habiro-derivation-gap-plan.md)
- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
