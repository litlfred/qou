# Lever-1 `tr B`: the quantum-integer form + monodromy classification (Sage-free)

**Date:** 2026-06-24
**Branch:** `claude/clever-volta-uir8ay`
**Status:** sharpens the "identify `E(q)`" keystone step into the canonical
variable and pins the monodromy type — **no closure, no fit, no owner-gated step
taken**. Sage-free (sympy + mpmath, 50 dps).
**Probe:** [`computations/substrate/lever1_trB_quantum_integer_form.py`](../../computations/substrate/lever1_trB_quantum_integer_form.py)
**Witness:** [`computations/substrate/lever1-trB-quantum-integer-form.witness.json`](../../computations/substrate/lever1-trB-quantum-integer-form.witness.json)
**Builds on:** [`2026-06-24-lever1-trB-geometric-target.md`](2026-06-24-lever1-trB-geometric-target.md)
(the `tr B = 3(3q⁴+8q²+3)/(4q(q+1)²)` target + torus-shortcut refutation).

## What "identify `E(q)`" was, and what this changes

The lever-1 identification `a_D^(n) = lw(n−1)` reduces (via the proved depth-2
`det B = 1` recurrence `a_{n+2} = τ·a_{n+1} − a_n`) to one number, `τ = tr B`. The
menu framing was *"identify the elliptic curve `E(q)`, compute `j(Bring/S₄)`, and
test `tr M(q₀) = 2.6424`."* Two facts move that target without touching any
Sage/owner-gated step.

### (Q) The trace is a rational function of `[2]_q` alone

In the SL₂/Chebyshev variable `s = q + q⁻¹ = [2]_q` (the quantum dimension of the
Hecke fundamental), the selection-rule periods and the trace are all rational
in `s`:

$$
a_D^{(2)} = 1,\qquad
a_D^{(3)} = \frac{s+2}{3},\qquad
a_D^{(4)} = \frac{3s^2-2}{4},\qquad
\operatorname{tr} B = \frac{3\,(3s^2+2)}{4\,(s+2)}.
$$

Each is symbolically identical to its `q`-form (sympy) and numerically equal to
50 dps at `q₀` and four random `q` (probe checks Q). Note `s+2 = (q^{1/2}+q^{-1/2})²`,
so `a_D^(3) = (q^{1/2}+q^{-1/2})²/3`. **`tr B` depends on `q` only through `[2]_q`.**
That is the signature of a q-difference / quantum-group connection, not of a
generic transcendental period — and it is the first concrete reason to expect the
keystone object to be a **q-difference system**, not a classical elliptic surface.

### (M) The monodromy is hyperbolic with a non-integer trace

`det B = 1` (proved, `prop:sl2-prolongation-recurrence`) and `tr B ≈ 2.6424 > 2`
make `B` a **hyperbolic** element of `SL₂(ℝ)`, with eigenvalues

$$
\lambda,\ \lambda^{-1}=\frac{\tau\pm\sqrt{\tau^2-4}}{2},\qquad \lambda \approx 2.18465 .
$$

The trace is **not an integer**. The topological π₁-monodromy of an elliptic
fibration lies in `SL₂(ℤ)` and has *integer* trace; `2.6424` cannot. So `B` is
**not** a topological monodromy of an elliptic surface — it is the rank-2
**q-difference (Gauss–Manin / Habiro) connection matrix** on the `W = H¹` factor.
This is decisive for the search: looking for an elliptic surface whose monodromy
hits `2.6424` is looking for the wrong object.

### (C) The rank-2 source is a CM/isogeny factor (Sage-free reconfirmation)

Plain-Python `S₅`/`A₅` character theory (probe check C) reconfirms the Sage
result of `lever1_bring_period_trB.sage` without Sage: `H^{1,0}(Bring)` is the
standard 4-dim `S₅` irrep, `⟨χ,χ⟩_{S₅}=1`, and it restricts **`A₅`-irreducibly**
(`⟨χ|_{A₅},χ|_{A₅}⟩_{A₅}=1`). Hence there is **no `A₅`-invariant rank-2 subspace
of holomorphic differentials**: the rank-2 `W` of `H¹(Bring) = 2W` must be an
isogeny/CM factor of `Jac(Bring)` (Riera–Rodríguez), realized at the de
Rham/q-family level — not a sub-representation of the forms.

## Net — the restated keystone target

> **Find the rank-2 q-difference system on the `W = H¹` CM/isogeny factor of
> `Jac(Bring)` whose connection matrix `B` satisfies `det B = 1` and**
> $$\operatorname{tr} B = \frac{3\,(3\,[2]_q^{2}+2)}{4\,([2]_q+2)}\quad(\lambda\approx 2.18465\ \text{at }q_0).$$

This is sharper than "identify `E(q)`" in three ways: the target is **rational in
`[2]_q`** (a quantum-group invariant, not a transcendental period), the monodromy
is **typed** (hyperbolic, non-integer trace ⇒ q-difference, not `SL₂(ℤ)`), and the
carrier is **named** (a CM/isogeny factor, not a form-subrep).

## What is *not* done (honest scope)

- **No closure.** The q-family connection `B` itself — the actual `E(q)` /
  Gauss–Manin matrix `M` — is **not** constructed. That is the owner-gated s5-so3
  keystone (the narrow 2026-06-19 reversal covers its geometric realization; this
  probe does not perform it).
- **`j(Bring/S₄)` not computed.** Sage is not provisioned in this sandbox; the
  fixed-curve `j`-invariant and the explicit `Jac(Bring)` isogeny decomposition
  remain Sage/Magma-gated and literature-dependent (Riera–Rodríguez). No value is
  asserted here.
- **No fit anywhere.** Every identity is exact (symbolic) or verified to 50 dps.
