# Knot operators give recurrences via the Gram form — and where the odd channel escapes

**Date:** 2026-07-18 · **Axis:** braid/knot algebra ↔ q-holonomic structure ·
**Tier:** exact structural (Lean-verified + sympy-verified) — no fit, nothing wired.
Answers the owner question *"can we use knot operators to get recurrences? gram inverse?"*

**Lean:** [`QOU/BraidKnot/KnotOperatorRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KnotOperatorRecurrence.lean)
(lean-direct exit 0, sorry-free). **Probe:**
[`knot_operator_gram_recurrence.py`](../../computations/probes/knot_operator_gram_recurrence.py)
→ witness `knot-operator-gram-recurrence.witness.json`.

## Yes — the mechanism, in three steps

1. **A knot operator that is a power of a fixed braiding element acts on a
   finite-dimensional module.** The twist region of a twist knot is `σ²` (one clasp
   twist) on `TL₂ = span{1, e}` (`e² = δe`, `δ = −A² − A⁻²`, `σ = A·1 + A⁻¹·e`) — a **2×2**
   operator, `tr σ² = (A⁸+1)/A⁶`, `det σ² = A⁻⁴`.

2. **Cayley–Hamilton ⇒ a linear recurrence.** A `d×d` operator satisfies its degree-`d`
   characteristic polynomial, so its powers obey an order-`d` recurrence
   (`pow_two_step`), and the Markov trace / closure — a *linear* functional — carries it to
   the knot invariants (`trace_two_step`):
   `tr(σ^{2(n+1)}) = tr·tr(σ^{2n}) − det·tr(σ^{2(n−1)})`. This **is** the twist-knot
   Jones-polynomial recurrence; the coefficients are the elementary symmetric functions of
   the two eigen-channels `A²`, `A⁻⁶`. (Twist knots `4₁, 5₂, 6₁, 7₂` are the closures at
   `n = 1,2,3,4`.)

3. **The Gram inverse is what diagonalises it.** The module carries the Markov-pairing
   **Gram matrix** `G = [[δ,1],[1,δ]]` (`⟨a,b⟩ = tr_M(ab)`), with
   `det G = (A²−A+1)(A²+A+1)(A⁴−A²+1)/A⁴` (cyclotomic / quantum-integer content). `σ²` is
   **G-self-adjoint** (`twist_gram_selfAdjoint`), hence diagonalisable in the Gram inner
   product; **`G⁻¹` builds the dual / Jones–Wenzl projector basis** on which `σ²` is
   diagonal. "`G⁻¹` → recurrence coefficients" and "`G⁻¹` → LP/SDP dual (shadow prices)"
   in the confinement machinery are the *same* object.

## The general picture — this is the quantum A-polynomial / AJ structure

The twist case is the smallest instance of a general fact: **colored Jones at color `N`
lives on an `(N+1)`-dimensional module, so Cayley–Hamilton gives an order-`(N+1)`
`q`-difference recurrence — and that recurrence operator is the quantum A-polynomial**
(the AJ conjecture). So the framework's knot-operator + Gram-inverse machinery does not
merely *admit* recurrences; it **computes the `q`-holonomic (AJ) recurrences** of the
even/geometric channel directly.

## Where the odd channel escapes — the KC22 connection

This sharpens why the bar-odd `Q_β` result is what it is. A `q`-holonomic recurrence is
*exactly* the "finite-dimensional module + Gram inverse" class above. KC22
([`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)) proved the
bar-odd `Q_β` D-ladder `D(ũ)` is **not** low-order `(q-)holonomic` in any tested class
(prime-certified). In the language here: **the odd channel is not the trace of powers of a
knot operator on any finite-dimensional Gram module** — it has no quantum-A-polynomial /
AJ recurrence, which is precisely why the closure route is transcendental / resurgent
(Écalle), not a knot-operator recurrence. The geometric/even channel *is* knot-operator +
Gram-inverse (this file); the odd channel provably is *not* (KC22). That dichotomy is the
structural content of the μ–p (even) vs `Q_β` (odd) split.

## Scope

Generic `CommRing` for the Lean core (`A`, `δ` formal); exact sympy over `ℚ(A)` for the
demonstration. Nothing wired; no fit; no tier change. This records the *mechanism* and its
boundary (KC22), not a new closure.
