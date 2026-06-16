# Q_β Habiro recursion — pre-archimedean derivation + bridge

**Date:** 2026-06-02
**Branch:** `claude/qbeta-habiro-recursion-and-bridge-2026-06-02`
**Trigger:** Owner directives — (1) "can we use uniqueness/existence theorems"; (2) "do all 3" (integrality + bridge Lean); (3) "recursion ↔ PDE via q-difference"; (4) "do as much pre-archimedean".

## The redirect: stop fitting at q_0, derive symbolically

All prior Q_β c_k work was **archimedean** — numerical, fitted at q_0 ≈ 1.10998, hence the "c_4+ extracted from CODATA residual" circularity. The owner's directive is to work **pre-archimedean**: formal q, symbolic, where the c_k genuinely live as Habiro/Taylor coefficients (CLAUDE.md §"Im(q) fibre vs observable", §7c base-ring convention).

The enabling fact (from `qbeta-decay-sdp-knot-operator.witness.json`):

> τ_M(T_β)(q) is a sum of z(q)^k contributions for k=0..3, with z(q) = 1/(√q + q^{−1/2}) the Markov parameter. The c_k extraction is "a finite algebraic exercise" comparing τ_M(T_β)(q) to Q_A(q)·cos(...) term-by-term in (q−1).

So τ_M(T_β)(q) is an **exact algebraic function of q** (pre-archimedean). Its Taylor coefficients around q=1 are EXACT — not fitted.

## recursion ↔ q-difference ↔ PDE (the owner's identity)

`z(q) = √q/(1+q)` is **algebraic** ⇒ **D-finite** ⇒ its Taylor coefficients around q=1 satisfy an explicit **P-recursive recursion** (the discrete shadow of the differential/q-difference equation `z` satisfies). Concretely, from `(2+w)·z = √(1+w)` (w = q−1):

```
(2+w)² z² = 1+w   ⇒   ODE for z(w)   ⇒   recursion for [z]_n
```

This recursion:
- is **explicit and pre-archimedean** (the "PDE" the owner asked for),
- **extends the coefficients to all orders k≫10** by iteration (no CODATA input — answers "can we do c_k for k≫10"),
- is the **defining q-difference equation** of the Habiro element (feeds the existence/uniqueness bridge).

## Plan

1. **Pre-archimedean recursion** — derive the explicit recursion for the Taylor coefficients of `z(q)^k` around q=1 (exact, from the algebraic ODE). Extend τ_M(T_β)'s `a_n` to high order. *(this file's first probe)*
2. **c_k extraction, symbolic** — perform the "finite algebraic exercise": `c_k` from `τ_M(T_β)(q) / (Q_base · cos)` term-by-term in (q−1), exactly. Compare the symbolic c_k to the CODATA-fitted ones — agreement = the ladder IS the Markov-trace expansion (derivation, not fit).
3. **Integrality / Habiro membership (existence)** — symbolic `(q;q)_n` expansion of the correction factor; check coefficients ∈ ℤ[q]. Pass ⇒ element ∈ Habiro ring (`habiro_integral`).
4. **Uniqueness + bridge instance (Lean)** — cite `habiro_terminates` (Habiro injectivity, already in `habiro-precision-ladder-equivalence.lean`); discharge the `QbetaHabiroTaylorBridgeClass` §3b-cond instance. Converts c_3+ from *fitted* to *the unique Taylor coefficients of the canonical Habiro element* — no closed form needed.

## Forbidden (CLAUDE.md)

- No ansatz fits for c_k (the recursion is DERIVED from z(q)'s algebraicity, not guessed).
- No production wiring until cross-anchor validation.
- Tiered reporting throughout.

## Cross-references

- T_β knot operator witness: `computations/qbeta/qbeta-decay-sdp-knot-operator.witness.json`
- Habiro-ladder equivalence Lean: `content/quantum-observable-universe/braids-and-knots/habiro-precision-ladder-equivalence.lean`
- PR #1727 audit (archimedean simple-pole / fibre-level): `docs/audits/2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md`
- Master ledger: `docs/coordination/1ppq-qbeta.md`
