# Habiro → ladder bridge — the unifying structural statement

**Date:** 2026-06-01
**Probe:** [`habiro_ladder_bridge.py`](../../computations/habiro/habiro_ladder_bridge.py)
→ `habiro-ladder-bridge.witness.json`
**Goal arm:** 1ppQ-Q_β.
**Unifies:** the order audit (#1593), eigenphase≠f (#1602), and the
q-difference spectrum + mode solve (#1622).
**Status:** exact characterization. The change of variable `u=√q ↦
u_ladder=b·ℏ²` resolves to ONE consistent statement; `f` remains the
open object, now fully constrained.

---

## The closed form

```
Δtr_M(q) = (−2q^{9/2} + 4q^{5/2} − 2√q − q⁵ − q⁴ − 2q³ + 2q² + q + 1)
           / [4q²(q+1)]
```

## The two variables (both around q=1, ε = q−1)

| variable | expansion | order |
|---|---|---|
| Habiro `u = √q` | `1 + ε/2 − ε²/8 + …` | O(1) (→1 at q=1) |
| Ladder `u_ladder = b·ℏ²` | `(√3/2)ε² − √3 ε³ + …` | O(ε²) (→0 at q=1) |
| `Δtr_M(q)` | `−5ε/4 − 3ε²/8 − …` | O(ε¹) |

## The unifying statement

Three facts, each previously found by a separate probe, are one
consistent structure:

1. **`Δtr_M(q=1) = 0` exactly** — proton & neutron Markov traces coincide
   at the classical point. This is the q-space form of #1622's *d=2
   bar-mode vanishing* (`Δtr_M = 0` at ζ_2).
2. **`Δtr_M` is `O(√u_ladder)`** (leads at ε¹, while `u_ladder` is O(ε²)).
   This is exactly #1593's *order audit*: the trace difference lives at
   order √u, not at the ladder's integer u-orders.
3. **The ladder `c_k` multiply `u_ladder^k` (k≥2).** So `Δtr_M` *alone*
   cannot supply the `c_k`. A scaling map `f: Δtr_M ↦ Q_β` must **lift
   order √u_ladder to u_ladder²** — the *u¹-cancellation / bar-even*
   constraint of #1602.

## What `f` must do (now fully constrained)

`f` is a **bar-even (charge-conjugation-symmetric) map** that lifts the
`O(√u_ladder)` trace difference to the `O(u_ladder²)` ladder, while
reproducing the #1622 modular data:

- the ζ_4 residue `∓i/2` (WRT level-4 modular phase),
- the modular sector's bar-even content `= 1/2`.

No `c_k` value is fabricated. `f` remains the open object — but it is now
constrained from four independent directions (order, symmetry, modular
residue, classical vanishing), which is a far sharper target than the
value-chasing that produced the four-session flip-flop.

## Why this is progress, not closure

The bridge does **not** close Q_β — the explicit `f` is still unknown.
What it does is convert the open problem from "find a value for c_3"
(repeatedly refuted) into "find the bar-even lifting map `f` with the
known modular data" — a structurally-specified object. This is the
honest state: the modes are exact, the constraints on `f` are exact, and
the remaining work is constructing `f`, not guessing coefficients.

## Discipline

Exact symbolic; both assertions pass; **no fitted `c_k`; no closure
claimed.** `u` collision kept explicit per `notation-collisions.md §u`.

## Cross-references

- Order audit: [`2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`](2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md)
- Eigenphase ≠ f: [`2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md`](2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md)
- q-difference spectrum: [`2026-06-01-habiro-q-difference-fourier-spectrum.md`](2026-06-01-habiro-q-difference-fourier-spectrum.md)
- q-difference mode solve: [`2026-06-01-habiro-q-difference-mode-solve.md`](2026-06-01-habiro-q-difference-mode-solve.md)
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
