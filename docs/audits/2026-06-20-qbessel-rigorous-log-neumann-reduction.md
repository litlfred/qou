# Rigorous integer-order log-Neumann: the forced Reeb-flow correction is ~2.2× the deuteron binding (+ Lean lemma)

**Date:** 2026-06-20
**Branch:** `claude/qbk2-rigorous-log-neumann-2026-06-20`
**Status:** Rigorous (resonance-free) — strongest evidence yet, but NOT established. No fit, nothing wired.
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md)
**Resolves both #2547 gates:** the `ν=0` confluent solution + a rigorous `Y_n` (no PV).
**Script:** [`computations/qbeta/qbessel_rigorous_log_neumann_reduction.py`](../../computations/qbeta/qbessel_rigorous_log_neumann_reduction.py) (`RIGOROUS TEST COMPLETE`)
**Lean:** [`QOU/QBeta/QCasoratianAbel.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QCasoratianAbel.lean) (sorry-free)

## Construction — reduction of order (resonance-free)

#2547 found `G_q = g₁g₂/D` is singular at *every* forced integer order: a simple pole
for `ν≥1` (the `d_k` Neumann resonance) and a confluent double-root at `ν=0` (dim=1).
The fix uses **only** the regular `g₁` and the Casoratian `D`:

- `g₁` is smooth in `ν` (no resonance); the Casoratian obeys the **q-Abel law**
  `D(qw)=q^{−ν}D(w)` ⇒ `D(w)=w^{−ν}` (clean monomial, *not* the divergent `d_k` series);
- the 2nd solution is recovered by a Jackson sum (up in `w`, `q>1` ⇒ terms vanish):
  `g₂(w) = −g₁(w)·Σ_{j≥0} D(q^j w)/[g₁(q^j w)g₁(q^{j+1}w)]`.

This never touches the `d_k` recurrence, so it is **finite at every integer order** — it
*is* the genuine log-Neumann / confluent 2nd solution. Self-checked (50 dps):

| ν | `L[g₂]` (=0?) | `|Cas − w^{−ν}|` | `G_rig` |
|---|---------------|------------------|---------|
| 0 (confluent) | 3.0e-35 | 2.8e-38 | −0.215 (finite) |
| 4 (was a pole) | −1.6e-33 | 8.3e-38 | 1.937 |
| 8 | 4.0e-30 | 9.0e-32 | −84.0 |
| 15 | 7.6e-38 | 4.1e-40 | −3.698 |

## Result (deuteron, all 11 blocks, forced `ν=dim−1`, `x=θ` Reeb flow)

| Quantity | Value |
|----------|-------|
| `δ_rig(q₀)` | **9.72** |
| `|δ_rig|/(B(D)/m_e ≈ 4.35)` | **2.23** |
| single-block domination | **25.2%** (not dominated) |
| cross-anchor spread (q₀ vs q_μ) | 5.9% (modest) |
| dim=1 confluent blocks | now **finite** (−1.41, 0.78) |

**The progression of the scale ratio as the artifacts were removed:**

| stage | ratio | issue |
|-------|-------|-------|
| #2545 (`ν±0.5` proxy) | 6.16 | proxy artifact (43% swing, 64% dom) |
| #2547 (PV, dim≥2 only) | 1.27 | dim=1 confluent excluded |
| **#2549 (rigorous, all blocks)** | **2.23** | proxy-free, un-dominated, dim=1 included |

## Lean lemma (machinery, sorry-free)

The algebraic backbone — the **q-Casoratian (Abel) law** — is formalised in
`QOU/QBeta/QCasoratianAbel.lean` over a generic `[CommRing R]`:

- `casoratian_abel`: for `a·h₂+b·h₁+c·h₀=0`, two solutions' Casoratian satisfies
  `a·C₁ = c·C₀` (the middle coefficient `b` drops out — `linear_combination`);
- `qbessel_casoratian_qabel`: specialised to `(☆)` (`a=q^ν, c=1`), `q^ν·C(qw)=C(w)`.

Verified sorry-free by `lean`-direct (exit 0). **This is a q-special-function
*machinery* lemma — NOT a binding claim** (per #2536, the wireable lemma is a q-Bessel
fact, not a mass result). It certifies the algebra the exploration runs on.

## Honest verdict — strongest evidence yet, but NOT established

- **What's solid:** the construction is **rigorous, resonance-free, proxy-free**, with
  both integer-order singularities resolved (dim=1 included) and self-checks passing to
  ~1e-30. The forced correction is **on-scale** (`2.23×`), **un-dominated** (25%) — this
  is *not* a proxy or pole artifact. The direction the owner's Reeb-flow steer opened is
  **real**.
- **What's open (the remaining gap, now ~2×):**
  1. **No `y_λ` Markov weights yet** — the sum is unweighted; the proper
     `δB = m_e Σ_λ y_λ χ_λ Δ_λ` weighting will move the `2.23`.
  2. **No bar-parity** declared (gate 2).
  3. **Cross-anchor 5.9%** — modest instability, higher than the PV's 0.76% (the dim=1
     confluent blocks add anchor sensitivity).
- **The number is `2.23×`, not `1×`.** Reaching `1×` must come from the *forced* `y_λ`
  weighting, **not** a tuned prefactor — matching `B(D)` by a chosen normalization is a
  fit and fails the Δ_λ discipline.

**Net:** the rigorous construction confirms the Reeb-flow correction is a genuine,
forced, on-scale (~2×) object — the strongest case so far that the direction is real —
but closing to an established `1×` binding result still needs the `y_λ` weights and
bar-parity. No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.
