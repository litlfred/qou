# q-Bessel off-shell resolvent: the quadratic propagator is origin-regular (qbk2 follow-up)

**Date:** 2026-06-20
**Branch:** `claude/qbk2-offshell-resolvent-2026-06-20`
**Status:** Structural identification — formalize-first, derive-or-refute, no fit, nothing wired
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md)
**Follows:** PR #2530 ([`2026-06-20-qbessel-second-kind-quadratic-action-gate.md`](2026-06-20-qbessel-second-kind-quadratic-action-gate.md))
**Script:** [`computations/qbeta/qbessel_offshell_resolvent_quadratic_correction.py`](../../computations/qbeta/qbessel_offshell_resolvent_quadratic_correction.py) (`ALL PASSED`, exit 0)

## The one live channel from the gate

PR #2530 proved the q-Bessel 2nd-kind solution `g₂ ~ w^{−ν}` is **singular** at the
substrate origin, so it is excluded from the on-shell binding sum as a *linear*
matrix coefficient. It left exactly one live channel: the owner's **"quadratic
action"** — the q-Bessel **Green's function / resolvent**, which is **bilinear** in
`(g₁, g₂)`. This note tests the precise structural question that channel raises.

> **Is the coincidence-limit propagator `G(w) = g₁(w) g₂(w) / D(w)` regular at the
> origin, even though `g₂` alone is singular?**

(`D(w) = g₁(w)g₂(qw) − g₁(qw)g₂(w)` is the q-Casoratian; by PR #2530's q-Abel law
`D(qw)=q^{−ν}D(w)`, so `D(w) = const·w^{−ν}`.)

## Result (60 dps, `ALL PASSED`)

| | Fact | Evidence |
|---|------|----------|
| A | The off-diagonal kernel `K(w,w′) = g₁(w_<)g₂(w_>)/D(w′)` solves `(☆)` in `w` for `w≠w′` — a genuine 2-point propagator | `|L_w K| ~ 1e-61` |
| B | `D(w) → (q^{−ν}−1)·w^{−ν}` as `w→0` | matches `q^{−ν}−1` to 1e-10 |
| **C** | **`G(w) = g₁(w)g₂(w)/D(w)` is REGULAR at `w→0`**, finite limit `1/(q^{−ν}−1)` | `G(1e-8)` converges to `1/(q^{−ν}−1)`; stays `O(1)`, does **not** blow up like `g₂` |
| D | Bar-parity of `G` under `q→1/q` is **ν-dependent** (not a single sector) | `ν=2.5`→odd, `ν=1.5,3.5`→even |

## What it means

**The quadratic combination rescues the 2nd kind on-shell.** The `w^{−ν}` singularity
of `g₂` cancels exactly against the `w^{−ν}` of the Casoratian `D`, so the bilinear
propagator `G(w)` is origin-regular and admissible — while the *linear* `g₂` is not.
The owner's **"quadratic action" names exactly the channel in which the 2nd kind
survives on-shell**, as a bilinear (propagator / one-loop) object. This **refines**,
and does not contradict, PR #2530: the *linear* matrix-coefficient exclusion stands;
the *quadratic* propagator is a distinct, admissible object.

This is the structurally correct reading of "a quadratic action's contribution is its
propagator `L^{−1}`": the coincidence-limit propagator `G(w)` is the q-analogue of a
one-loop / heat-kernel correction, and it is finite at the substrate point.

## Honest scope — NOT a closure (TIERED)

- **(A)(B)(C) proved.** The admissible quadratic object is identified and verified.
- **The binding-correction claim is OPEN.** Turning `G(w)` into a *falsifiable*
  mass/binding correction still needs **two** ingredients this note does not supply:
  1. the **physical source** the propagator is contracted against (the `−w` term of
     `(☆)` is the operator-level source; its physical identification is not fixed here);
  2. the **cross-anchor gate** — a single substrate-fixed coupling reproducing the
     correction at **both** the proton and muon anchors with **no per-anchor refit**
     (a refit is a refutation, not a result).
- **Bar-parity caveat (gate 2).** `G`'s sector under `q→1/q` is **ν-dependent**
  (mixed across orders), so the quadratic correction is **not** confined to a single
  bar sector a priori — any binding use must declare the order and sector explicitly,
  and the mixed parity is itself a constraint to satisfy (or a refutation signal).

No fit; nothing wired; `c_k`/`Δ_λ` stay cal-anchored. The owner closes the bean
(§4a); this records the off-shell channel's structural state for that decision.
