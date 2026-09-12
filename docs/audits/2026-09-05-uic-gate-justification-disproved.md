# The gate that forces the sign rests on a duality the corpus already disproved

**Date:** 2026-09-05 · **Bean:** `qou-sv7h` · **Scope:** (a) ·
Follow-on to [`2026-09-05-uic-sign-forced-by-gate.md`](2026-09-05-uic-sign-forced-by-gate.md)

> ## ✅ ACTED ON, 2026-09-12 — the gate is gone
>
> **Bean `qou-jgx7`; PR #7253.** This document's conclusion was enacted: the
> owner ruled to drop the Pass-2 sign gate, and
> `unified_iterative_correction` now returns the **ungated** sum. PR #7251
> additionally *hunted the primal LP* and refuted CS-on-it sorry-free
> (`QOU.MassTheory.UICGateNotFromComplementarySlackness`, four mismatches +
> a scope-(b) invariant), so this audit's "disproved duality" reading is now
> backed by machine-checked Lean rather than by inference from the content
> block alone.
>
> **Two things this document could not have known.** First, the `y_0` finding
> below is *stronger* than stated: `y_0* = 0` holds for the **NF-basis**
> instance (the cost vector IS a Gram row), but PR #7251 measured the
> **block-indexed** instance at `y_0* = 0.0346905` (²H) / `0.0129979` (⁴He) —
> so "the dual is identically zero" is basis-dependent, and the version of it
> that applies here is the NF one. Second, and correcting the companion audit
> rather than this one: **removing the gate does not fix the sign.** Every
> ungated total is negative and larger in magnitude. The drop buys honesty,
> not accuracy.

The companion audit measures **that** the Pass-2 gate forces `B < 0` — a claim
**retracted 2026-09-12**; read it as "biases", see the banner at the top of that
file. This one asks whether the gate's *justification* holds, and connects two
things the corpus has kept apart for eleven days.

## What the corpus already proves

[`mass-theory/operator-selection-lp.md`](../../content/quantum-observable-universe/mass-theory/operator-selection-lp.md)
(commit `6b7d2ec4a8`, 2026-08-25) proves the operator-selection LP is
**degenerate**:

- The NF basis begins with the empty word, so `b₁ = 1` and `G[1][j] = t_j` — the
  first Frobenius-positivity row **is** the objective vector. The program
  minimises `t·x` subject to `t·x ≥ 0`, so its optimum is **identically 0**.
- By strong duality `n_target · y_0* = 0` with `n_target > 0`, hence
  **`y_0* = 0`**: the net constraint carries no shadow price.
- The minimiser set is a **positive-dimensional face** — six vertices at n = 3,
  in mirror pairs — so which one a solver returns is a pivoting artefact.

That commit corrected the **content blocks** and deliberately proposed no
replacement ("choosing one is a decision about the physics"). It did not touch
`hecke_core_legacy.py`, which still reads the LP the old way in two places.

## Connection 1 — `lp_shadow_price`'s `y_0` is not the LP's dual

`lp_shadow_price` sets `y_0 = 1/[k]_q!` and its docstring calls it *"the dual
variable of the normalisation constraint"*. The LP proves that dual is **0**.

| k | `y_0` used | proved `y_0*` | partitions zeroed |
|---|---|---|---|
| 2 | 0.497290545605 | 0 | 2 of 2 |
| 3 | 0.163383228056 | 0 | 2 of 3 |
| 4 | 0.0397556822422 | 0 | 2 of 5 |
| 5 | 0.00761538731028 | 0 | 2 of 7 |
| 6 | 0.00119212336909 | 0 | 2 of 11 |
| 7 | 0.000156337035543 | 0 | 2 of 15 |

Never zero, so it is not that dual — against a proof already in this corpus.

**What the choice actually does.** `1/[k]_q!` *is* `min_λ(w_λ/d_λ)` (verified
k = 2..11), so subtracting it zeroes exactly the two extreme partitions `(k)`
and `(1^k)` — the **trivial and sign representations** — at every level, and
nothing else. It is not needed for non-negativity either: `w_λ/d_λ > 0` already,
so `y_λ ≥ 0` holds with or without the shift.

## Connection 2 — the proved `y_0*` does not repair the sign

| atom | A | as-is (`y_0 = 1/[k]_q!`) | with proved `y_0* = 0` | AME |
|---|---|---|---|---|
| ²H | 2 | −1.3657 | **−1.6092** | +2.225 |
| ³H | 3 | −0.9704 | **−1.2142** | +8.482 |
| ⁴He | 4 | −0.8021 | **−0.9095** | +28.296 |
| ⁶Li | 6 | −1.0770 | **−1.6065** | +31.994 |

It makes the sign **more** negative, not less — because the gate still keeps
`Tr ≤ 0` and now more partitions carry weight.

*(The `y_λ = 0` partitions cannot be rescaled by the linearity argument used
here and are dropped, so this is a lower bound on the change, not a full
recomputation.)*

## Consequence

**The sign cannot be repaired by correcting the dual variables.** Correcting
`y_0` is *necessary* — the present identification is disproved — and *not
sufficient*. The gate itself, "keep the partitions with `Tr ≤ 0`", is what
forces the sign, and its stated justification does not survive the degeneracy
proof: complementary slackness cannot single out a partition set for a program
whose optimum is identically 0 and whose minimiser set is a positive-dimensional
face.

There is a second, independent tension noted in the companion audit: for a
constraint `tr ≥ 0`, *tight* means `tr = 0`, but the code admits all `tr ≤ 0` —
and the contribution `∝ ln|tr|` diverges exactly at `tr = 0`.

## What is not claimed

What the replacement should be. That is the same physics decision `6b7d2ec4a8`
declined to make about the objective, one level down — and it belongs to whoever
owns `prop:mass-coefficient-shadow-price`.

Not claimed that the accumulator diverges: it does not, per
[`2026-09-05-uic-a1-vanishing-trace.md`](2026-09-05-uic-a1-vanishing-trace.md),
which retracts an earlier claim of mine that it did.

Reproduce: [`computations/probes/uic_gate_justification_disproved_probe.py`](../../computations/probes/uic_gate_justification_disproved_probe.py) — 5/5 checks.
