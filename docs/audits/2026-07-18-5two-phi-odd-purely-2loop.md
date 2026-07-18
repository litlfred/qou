# φ_odd is a purely 2-loop datum — the classical bar-odd phase vanishes by σ₁/σ₂ conjugate symmetry

**Date:** 2026-07-18 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ (5₂ φ_odd) · **Tier:**
numerical scope-(a)/(b) (an exact vanishing + a mechanism) · **Discipline:** no fit,
no c_k wired, nothing to production, no tier change.

## Context

The sibling classical-strip program extracts the intrinsic bar-odd datum of the 5₂
substrate saddle-pair as `φ_odd = phi_odd_arg_sum = −0.004144702346` (with
`mag_odd_ratio−1 = 0.0864`), via the **certified 2-loop (238) strip** + a 2×2 ray
solve. This probe attacks the same quantity from a **different context** — the
classical (1-loop) saddle data alone, from the verified 5₂ quantum-volume machinery.

## Result — the classical bar-odd phase vanishes exactly

[`qbeta_5two_phi_odd_oneloop_vanishing_probe.py`](../../computations/probes/qbeta_5two_phi_odd_oneloop_vanishing_probe.py):
the 5₂ substrate cubic `(m²y−1)(y−1)(m²−y) − m²y² = 0` has **three saddles**:

| saddle | Re V | Im V | `arg(a)`, `a=1/√(iδ)` | role |
|---|---|---|---|---|
| σ₃ | `6.913` | `−3.642` | `−π/4` | real; exponentially ray-absent |
| **σ₁** | `1.815` | `−2.293` | `−0.80385` | co-dominant pair |
| **σ₂** | `1.815` | `+2.293` | `−0.76695` | co-dominant pair |

σ₁, σ₂ are a **conjugate pair** (equal Re V, opposite Im V) — the ray-co-dominant pair.
For it, the classical amplitude arg-sum is **exactly −π/2 for both the pair and its bar
image**:

> `arg(a₁)+arg(a₂) = −π/2`  and  `arg(b₁)+arg(b₂) = −π/2`  ⇒  **`φ_odd(1-loop) = 0` exactly.**

## Insight — φ_odd is intrinsically quantum / 2-loop

Since the classical (1-loop) bar-odd phase is **identically zero** by the σ₁/σ₂
conjugate symmetry, the sibling's `φ_odd = −0.004145` is generated **entirely by the
sub-leading quantum amplitude** — the 2-loop (238) correction. The classical geometric
saddle data (V, δ) carries **no** bar-odd datum.

This is the **mechanism** behind the corpus's repeated *"geometric routes are
anchor-smooth / null"* findings (5₂ quantum volume anchor-smooth; classical CS
anchor-invariant; branch-point locus generic): the bar-odd datum is **invisible to the
classical volume/Hessian** by conjugate symmetry, so it can only live in the quantum
(2-loop) amplitude. Independently — from the classical side — this **confirms the
sibling's certified 2-loop strip is essential, not optional**, and explains why every
classical/geometric probe returned a null.

## Scope (anti-laundering)

A proved 1-loop **vanishing** (arg-sum `= −π/2` exactly, conjugate symmetry). Does
**not** compute φ_odd's value — that is the 2-loop amplitude, sibling-owned. No fit;
no c_k; no tier change.

## Cross-references

- Sibling extraction (the −0.004145 value): `qbeta_g3_5two_classical_strip.py` (2-loop (238) strip)
- Sibling Prony / M-dictionary: #3991, #4011–#4015 (block/saddle, Stokes)
- Verified 5₂ saddle: [`qbeta_5two_quantum_volume_probe.py`](../../computations/probes/qbeta_5two_quantum_volume_probe.py)
- Dilog closed-form home: [`2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md`](2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md)
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
