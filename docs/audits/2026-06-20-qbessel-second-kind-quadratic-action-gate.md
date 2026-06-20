# q-Bessel 2nd-kind "quadratic action": on-shell-excluded, off-shell-only (qbk2 gate)

**Date:** 2026-06-20
**Branch:** `claude/fervent-noether-zssd1k`
**Status:** Formalize-first structural gate — derive-or-refute, no fit, nothing wired
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md) (owner-seeded; parent `qz9k`)
**Script:** [`computations/qbeta/qbessel_second_kind_quadratic_action_gate.py`](../../computations/qbeta/qbessel_second_kind_quadratic_action_gate.py) (`ALL PASSED`, exit 0)
**Builds on:** [`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md), [`qbessel_second_order_qdifference_equation.py`](../../computations/qbeta/qbessel_second_order_qdifference_equation.py)

## The owner's seed

> "The 2nd kind has a quadratic action that can be used in mass/binding as corrections."

The Hahn–Exton q-Bessel q-difference equation `(☆)` is **second order**, so it has a
second linearly independent solution — the q-analogue of the Neumann/second-kind
`Y_ν`. The corpus develops only the first kind `J_ν` (rotation) and modified `I_ν`
(growth). This note develops the second-kind solution far enough to **gate** the
binding-correction idea *before* any wide cross-anchor scan (per CLAUDE.md
§Formalize-first probe discipline + the bean's own 5-point gate).

## The second solution

`(☆)`: `q^ν g(q²w) − (1 + q^ν − w) g(qw) + g(w) = 0`. Its indicial equation at `w=0`
(drop the subleading `−w`, set `g ~ w^ρ`, `y = q^ρ`) factors:

```
q^ν y² − (1+q^ν) y + 1 = (q^ν y − 1)(y − 1) = 0   ⇒   ρ = 0  and  ρ = −ν.
```

- `ρ = 0`: the regular 1st-kind solution `g₁` (`J_ν ~ x^ν`, vanishes at the origin).
- `ρ = −ν`: the **second-kind** solution `g₂(w) = w^{−ν} Σ_k d_k w^k`, `d_0 = 1`,
  with `(q^k − 1)(q^k − q^ν) d_k = −q^{k−1} d_{k−1}` (non-integer `ν`; integer `ν` is
  the log/Neumann resonance `q^k = q^ν`).

## Three verified facts (60 dps; non-integer ν to avoid the log resonance)

| | Fact | Evidence |
|---|------|----------|
| **A** | `g₂` is a genuine 2nd solution of `(☆)` | residual `~1e-57` at three `(ν,q,w)` |
| **B** | `g₁, g₂` independent; q-Casoratian `D(w)=g₁g₂(qw)−g₁(qw)g₂` obeys the **q-Abel law** `D(qw)=q^{−ν}D(w)` ⇒ `D(w)·w^ν = const` | Abel residual `~1e-58`; `D·w^ν` constant per case |
| **C** | `g₂(w) ~ w^{−ν}` → **diverges** as `w→0` (Neumann `Y_ν ~ x^{−ν}`) | `g₂(10⁻⁸)·w^ν → 1`, `|g₂|` up to `10²⁸` |

## Gate result (TIERED)

**(B) ⇒ parameter-free.** The 2nd-kind normalization relative to the 1st is fixed by
the q-Casoratian (q-Abel), **not** a free per-block knob. So a 2nd-kind term is **not**
a disguised 7th `Δ_λ` ansatz — it adds no fitted multiplier. (Bean gate 1 ✓.)

**(C) ⇒ on-shell-excluded.** The on-shell binding sum
`B = m_e Σ_λ y_λ χ^λ Δ_λ` is built from **regular-representation** Markov-trace matrix
coefficients — the `J` / little-q-Jacobi "regular at the identity" world (per the
2026-06-13 dictionary). Regularity at the substrate origin **excludes** the
`x^{−ν}`-singular 2nd-kind solution from any on-shell matrix coefficient — the *same*
regularity that excludes `Y_ν` from the `E_q(2)`/`SU_q(2)` unitary matrix coefficients.

> **Therefore the 2nd-kind "quadratic action" correction is identically zero in the
> on-shell (regular-rep) binding sum.** It is non-trivial **only off-shell**, in the
> q-Bessel **Green's function / resolvent** `G ~ g₁(x_<) g₂(x_>)/D(x)`, sourced by the
> linear `−w` term of `(☆)`. The owner's "quadratic action" reading is structurally
> correct — a quadratic (free-field) action's contribution **is** its propagator — but
> that propagator is an **off-shell** object with an explicit source, not a
> redefinition of the on-shell trace.

**Bar sector (gate 2).** `g₁` already carries both bar parities via Jacobi–Anger; the
2nd-kind enters off-shell *paired with* `g₁` through the Casoratian, so it does **not**
define a new independent bar sector.

**Regime (gate 5).** Rotation `(J, Y)` real `η` vs growth `(I, K)` imaginary `η`; the
2nd-kind is `Y` (rotation) / `K` (growth), kept explicit — no silent `.real`.

## What this prunes

No on-shell binding scan is warranted: the on-shell channel is structurally empty.
Any continuation of `qbk2` must be an **off-shell resolvent** computation carrying an
explicit source (the `−w` term), and must still clear the cross-anchor gate (gate 3)
before any closure claim. `c_k` / `Δ_λ` stay cal-anchored; nothing is wired to
production. The owner closes the bean (per CLAUDE.md §4a); this note records the gate
outcome for that decision.
