# Binding lever-1: the depth-2 kernel `R=x²−τx+1` is anchor-limited — it does NOT generate the selection-rule values `lw(c)` beyond c≤3

**Date:** 2026-06-24
**Branch:** `claude/binding-lw-recurrence-reach-2026-06-24`
**Bean:** `z2bn` (Lever 1 — fibre q-difference kernel `R(q,x)`).
**Status:** a previously-unrun **falsifiable reach test** of the landed depth-2 kernel (PR #2718). EXPLORATORY, **zero free parameters**, no production rewire.
**Script:** [`binding_lw_recurrence_reach_probe.py`](../../computations/binding_lw_recurrence_reach_probe.py) · **Witness:** [`binding-lw-recurrence-reach.witness.json`](../../computations/binding-lw-recurrence-reach.witness.json)

## What was tested

PR #2718 landed the depth-2 binding kernel `R(q,x) = x² − τx + 1` (det=1; recurrence
`a_{n+2}=τ·a_{n+1}−a_n`) with the SW-period anchors identified as the canonical
selection-rule values

  `lw(c) = (1/(c+1))·Σ_{λ⊢c+1} dim_q(V_λ)`,  `dim_q = [n]_q!/∏_x [h_x]_q` (balanced q-hook).

`binding_selection_rule_tau_closure.py` fixes `τ = (lw(1)+lw(3))/lw(2)` from the **three**
anchors c=1,2,3 and *defines* the odd-partner `a₅ := τ·lw(3) − lw(2)`. **It never checks
that `a₅` equals the independently-computed `lw(4) = (1/5)·Σ_{λ⊢5} dim_q`.** This probe runs
exactly that cross-check at c=4 and c=5:

  predicted `â(c) = τ·lw(c−1) − lw(c−2)`  vs  direct `lw(c)` (canonical dim_q).

## Result (q₀ ≈ 1.10998, 50 dps)

| c | direct `lw(c)` | depth-2 prediction | rel. error |
|---|---------------:|-------------------:|-----------:|
| 1 | 1.0 | (anchor) | — |
| 2 | 1.33697 | (anchor) | — |
| 3 | 2.53278 | (anchor) | — |
| **4** | **5.37614** | 5.35562 | **0.38 %** |
| **5** | **13.55983** | 11.67305 | **13.9 %** |

`τ = 2.64239` (reproduces the corpus `2.6424`). The successive ratios `lw(c+1)/lw(c)` are
**1.89 → 2.12 → 2.52 → 2.52** — *increasing*, not converging to the depth-2 dominant root
`λ₊ = 2.1846`. So `lw(c)` grows **faster than any fixed-τ depth-2 recurrence**; the kernel's
match at c≤3 is automatic (3 anchors fix τ via det=1 + one ratio), and it breaks immediately
at c=4.

## Verdict — (a) scope-limited negative

**The depth-2 *constant* kernel `R=x²−τx+1` does not generate the selection-rule sequence
`lw(c)` beyond its three c≤3 anchors** (misses `lw(4)` by 0.38 %, `lw(5)` by 13.9 %). This is
a **scope-limited (a) negative**, not a structural exclusion:

- It **does not** refute the kernel's qualitative content: the proved `λ₊ > 1`
  extensive-growth property (`BindingRecurrenceSpectral.lean`, PR #2718) **stands** — the
  recurrence *does* have a dominant root > 1; the binding *is* extensive.
- It **does** bound the *constant-kernel reach*: τ is anchor-fitted to c≤3, and the `lw`
  sequence is not a constant-coefficient depth-2 recurrence. This **quantifies**, at the
  selection-rule level, the corpus note that a **constant kernel of depth ≤ 3 is refuted**
  and the true object is a **non-constant / higher-depth kernel**
  ([`2026-06-04-c4-gap-no-constant-kernel-recursion.md`](2026-06-04-c4-gap-no-constant-kernel-recursion.md)).

**Implication for lever 1.** "One selection rule generates the depth-2 kernel" is accurate
only as an anchor statement (c≤3). For the body-order series to be reproduced for A ≥ 4,
the kernel must be **non-constant in n** (τ → τ(n), so that `lw(c+1)/lw(c)` can rise) or of
**higher depth**. The natural candidate, given the increasing ratios, is a kernel whose
coefficient tracks `dim_q` growth — i.e. the q-Plancherel `d_q²` weighting itself, which ties
lever 1 back to the `W_λ` frontier (the SW-period = `lw` identification, owner-gated #2488).

## Discipline

No fit (τ fixed by c≤3; `lw(4)`,`lw(5)` computed from `dim_q`, nothing tuned); `q₀` only as
evaluation point. (a)-scoped per the refutation discipline — the finding bounds the constant
depth-2 reach, it does **not** exclude a non-constant/higher-depth kernel (the open frontier).
Corpus-grep: this *extends* `binding_selection_rule_tau_closure.py` (which checked only c≤3);
it does not re-walk a refuted approach — it **quantifies** the existing depth-≤3 caveat.

## Cross-references

- PR #2718 / `BindingRecurrenceSpectral.lean` — the landed depth-2 kernel + λ₊>1 (stands).
- [`binding_selection_rule_tau_closure.py`](../../computations/binding_selection_rule_tau_closure.py) — the c≤3 anchor closure this probe extends.
- [`2026-06-04-c4-gap-no-constant-kernel-recursion.md`](2026-06-04-c4-gap-no-constant-kernel-recursion.md) — the constant-kernel-depth refutation this quantifies.
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the SW-period = `lw` identification (the non-constant kernel ties here).
