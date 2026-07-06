# The qbk2 wiring unblocker is structurally refuted: the forced order is the Neumann log-resonance

**Date:** 2026-06-20
**Branch:** `claude/qbk2-unblocker-refutation-2026-06-20`
**Status:** Decisive refutation — derive-or-refute, no fit, nothing wired
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md) (binding direction CLOSED)
**Follows:** PR #2536 (wiring gate: DO NOT WIRE)
**Script:** [`computations/qbeta/qbessel_unblocker_forced_order_refutation.py`](../../computations/qbeta/qbessel_unblocker_forced_order_refutation.py) (`REFUTATION COMPLETE`)

## The question

PR #2536 verdict (DO NOT WIRE) rested on the `(ν_λ, w_λ)` order+argument map being a
free functional knob (63% swing). The owner asked to **attempt the unblocker**: is there
a substrate principle that *forces* the map, making the binding correction parameter-free
after all? This note attempts it and **refutes it structurally** — the obstruction is not
a failed search, it is the representation theory.

## The only representation-theoretically forced order is integer — and integer is resonant (R1, computed)

In the `SU_q(2) → E_q(2)` harmonic analysis (Vaksman–Korogodsky 1989; Koelink 1994,
cited in [`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md)),
the Hahn–Exton q-Bessel `J_ν(x;q)` is the `E_q(2)` matrix coefficient with **`ν` the
angular-momentum label (integer)** and **`x` the radial coordinate (continuous)**. So the
only forced order on a Wedderburn block is an **integer** — the rep's angular/Chebyshev
label `dim_λ − 1`, or the Jacobi–Anger tower level `2m+1`.

The script computes, for every deuteron block (n=6):

| λ | dim_λ | ν = dim−1 | integer? | power-series `g₂` |
|---|------|-----------|----------|-------------------|
| [3,1,1,1] | 10 | 9 | yes | **SINGULAR (k=9)** |
| [4,2] | 9 | 8 | yes | **SINGULAR (k=8)** |
| [5,1] | 5 | 4 | yes | **SINGULAR (k=4)** |
| … | | | | |
| [6] | 1 | 0 | yes | trivial ν=0 |

**Every forced order is an integer, and every nonzero one is a Neumann log-resonance:**
the power-series 2nd-kind recurrence `(q^k − q^ν)d_k = −q^{k−1}d_{k−1}` has a zero
denominator at `k = ν`. So the substrate-forced order **does not even admit the #2533
power-series propagator** — that propagator exists only at the *unphysical half-integer*
orders #2536 was forced to use.

## At the forced (integer) order, the log-Neumann solution reintroduces the unforced radial scale (R2, structural)

At integer order the genuine second solution is the **logarithmic Neumann** function
`Y_n(x) ~ J_n(x)·log(x) + (regular)`. Its value depends on the **radial argument `x`**.

But the framework's per-block data fixes only the **angular** Reeb phase
`θ_λ = arccos/arccosh(χ_λ/dim_λ)` — the character *phase*. In `E_q(2)`, **angular `θ`
and radial `x` are independent coordinates**; the Markov trace supplies no canonical
`θ → x` map. So the log scale `x` is exactly the free knob that produced the 63% swing
in #2536 — now identified by name: it is the missing radial coordinate.

## Verdict — UNBLOCKER REFUTED (structural, not a failed search)

The two halves compose into a clean closure:

1. **(R1)** the representation-theoretically forced order is integer → the #2533
   power-series propagator is singular there (Neumann resonance);
2. **(R2)** the genuine integer-order (log-Neumann) solution needs a radial argument the
   Markov trace does not provide.

> A parameter-free binding correction from the q-Bessel quadratic action would require a
> **new substrate datum — a canonical per-block radial coordinate** — that the angular
> Markov-trace data structurally cannot supply. Until such a radial datum is derived
> (independently, not chosen), the correction is unforced. **qbk2's binding direction is
> closed.**

This *explains* #2536's 63% swing (the unforced knob is the radial `x`, an independent
`E_q(2)` coordinate) rather than merely observing it. The admissible quadratic object
(PRs #2530/#2533) remains real and correctly identified; what is refuted is its use as a
*parameter-free* mass/binding correction.

No fit; nothing wired; `c_k`/`Δ_λ` stay cal-anchored. Owner closes the bean (§4a).
