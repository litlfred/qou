# The W_λ-producing structure is the non-compact E_q(2) contraction, not a compact MTC — identification settled

**Date:** 2026-06-22
**Branch:** `claude/keystone-modular-category-id-2026-06-22`
**Status:** Positive identification — the modular-category question is settled by a regime check;
it unifies the keystone with the corpus's existing q-Bessel / Reeb-phase identification. No fit.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Follows:** [`2026-06-22-keystone-geometric-angles-preflight.md`](2026-06-22-keystone-geometric-angles-preflight.md) §2 (the WRT reframing)
**Script:** [`scripts/keystone_modular_category_id_probe.py`](scripts/keystone_modular_category_id_probe.py)

## The question

The WRT reframing reduced `index = W_λ` to: **`W_λ` are the block weights `d_λ²/D²` of a modular
tensor category** — and pinning the open object to *which* category. This probe settles it by a
regime check on the substrate `q_0`.

## The settling observation — `q_0` is real > 1 (growth regime)

| check | result | consequence |
|-------|--------|-------------|
| `\|q_0\|` | 1.10998 ≠ 1 | **not** on the unit circle ⇒ **not** a root of unity ⇒ **no** compact SU(2)_k MTC has these quantum dims |
| `η = log q_0` | 0.10434, **real** | the **growth** (arccosh, `I_ν`) regime, not rotation (arccos, `J_ν`) |
| `[m]_q` | `= sinh(mη)/sinh(η)` to 1e-40 | the `I_ν`/`cosh` branch exactly — the Reeb-phase doc's arccosh regime |

A unitary compact modular tensor category SU(2)_k requires `q = e^{iπ/(k+2)}` with `|q| = 1` (η
imaginary). The substrate has `|q_0| = 1.10998 ≠ 1`, so it lies in the **non-compact** regime for
*every* level k. The compact-MTC arena is therefore the **wrong** home for `W_λ`.

## The identification (type-correct)

- `q_0` real > 1 ⇒ the substrate ribbon category is **non-compact**: `Rep` at generic real `q_0`, the
  **`SU_q(2) → E_q(2)` contraction** regime, whose matrix coefficients are the **Hahn–Exton q-Bessel
  functions** (Vaksman–Korogodsky 1989; Koelink 1994). This is **already identified in the corpus**
  ([`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md)).
- So `W_λ = d_q²/[n]_q!` are the **generic-q (growth-regime) Hecke–Markov block weights** of this
  non-compact structure — **not** a finite compact MTC (root of unity), and **not** a finite Sasakian
  manifold (already ruled out, #2398/#2406).
- The **WRT(S³/2I) / Habiro-ring** object reconciles the two ends: the Habiro ring evaluates at *both*
  roots of unity *and* generic `q`, so the generic-`q_0` evaluation is the well-defined bridge.

## What this resolves, and the residual frontier

This **collapses three separate "open geometric" framings into one already-identified object.** The
keystone's `W_λ`-origin question, the WRT/Lawrence–Zagier redirect, and the modular-category question
all resolve to the **same** non-compact `E_q(2)` contraction at generic real `q_0` that the corpus's
Reeb-phase / qbk2 work already named. The progression of the keystone's "single owner-gated object":

1. *(originally)* build a finite Sasakian on the Wu manifold + equivariant index → **arena ruled out** (#2398/#2406);
2. *(WRT reframe)* `W_λ` = modular block weights `d²/D²`, S³/2I the icosahedral selector → **representation-theoretic, not geometric**;
3. *(here)* the category is the **non-compact `E_q(2)` contraction** (real `q_0`, growth regime) — the **Hahn–Exton q-Bessel structure already in the corpus**.

**Residual frontier (sharply located):** the explicit **Habiro-ring WRT(S³/2I) q-series, evaluated at
`q_0`, reproducing `W_λ`**. This is now a concrete q-series computation in a structure the corpus has
infrastructure for (Habiro / Reeb-phase / q-Bessel), not differential geometry. It is the genuine
remaining research step — well-posed, finitely stated, no longer "geometer-grade Sasakian existence".

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-22-keystone-geometric-angles-preflight.md`](2026-06-22-keystone-geometric-angles-preflight.md) — the WRT reframing (§2) this settles.
- [`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md) — the `SU_q(2)→E_q(2)` / Hahn–Exton q-Bessel identification (the now-unified home).
- [`2026-06-16-keystone-wu-manifold-reeb-obstruction.md`](2026-06-16-keystone-wu-manifold-reeb-obstruction.md) — the finite-Sasakian arena ruled out.
- [`2026-06-16-s5so3-markov-weighting-sasakian-scope.md`](2026-06-16-s5so3-markov-weighting-sasakian-scope.md) — the forced `W_λ` target + the WRT/Habiro redirect.
