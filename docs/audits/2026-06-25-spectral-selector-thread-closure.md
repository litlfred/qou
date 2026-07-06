# Spectral-selector thread — closure (item-1 of the stalled-session menu)

**Date:** 2026-06-25 · **PR:** #2757 · **Bean:** `z2bn` (lever-1 `R(q,x)` FOCUS)

## TL;DR

The "**which partition activates the deuteron binding?**" question — chased in an
earlier session as a *raw spectral selector* on `ρ_λ(β)` — is **closed**, not open.
It evolved into the depth-2 binding kernel `R(q,x) = x² − τx + 1` (sorry-free Lean),
and the **only** remaining open piece is the owner-gated geometric derivation of the
single number `τ = tr B`. This note records the corpus-grep evidence so the thread is
not re-opened against its own deprecated probes.

## Why this note exists

A stalled session's transcript proposed *"rebuild the Φ_q-tower spectral selector and
validate it against [2,2,1,1]"* as an **open** item. Per the STRICT corpus-grep
discipline (AGENTS.md §"Before declaring open"), that declaration is **wrong**: the
thread was already resolved and superseded. Its own commits (`d848b514`, PRs
#2109/#2122) exist in no branch, and its probes are deprecated.

## The thread's evolution (deprecated probe → production selector → kernel → Lean)

| stage | object | status |
|---|---|---|
| 1. raw spectral probe | `max|μ(ρ_λ(β))|` → `[3,3]`; `|y_λ·χ_λ|` → `[6]` | **refuted** — neither is the empirical `[2,2,1,1]`; probes in [`computations/_deprecated/explore_items_1_and_2.py`](https://github.com/litlfred/qou/blob/main/computations/_deprecated/explore_items_1_and_2.py), `brane-tower-per-channel-phi-q-probe.witness.json` |
| 2. selection rule | `lw(c) = (1/(c+1))·Σ_{λ⊢c+1} dim_q` (mean quantum dimension) | **production** — `linking_weight_family_a`, ~5 live importers |
| 3. binding kernel | `R = x² − τx + 1`, `det = 1`, `a_D^(n) = lw(n−1)`, `τ = tr B ≈ 2.6424` | **derived** (no fit), `τ` closed form `3(3[2]_q²+2)/(4([2]_q+2))` (PR #2722) |
| 4. formalization | `λ₊ > 1` (extensive); **q-robust** `0<q ⇒ λ₊(τ([2]_q))>1` (PR #2757) | **Lean, sorry-free** — [`BindingRecurrenceSpectral.lean`](https://github.com/litlfred/qou/blob/claude/happy-edison-b2petg/content/quantum-observable-universe/lean/QOU/Mass/BindingRecurrenceSpectral.lean) |

**Lesson the probes taught (kept):** the activating partition is the **`y_λ`-weighted
spectral contribution**, never a bare eigenvalue max — consistent with binding being
`Σ y_λ χ_λ`. The `lw(c)` mean-quantum-dimension selector is the realized form of that
lesson.

## Corpus-grep evidence (the four STRICT paths)

1. `docs/audits/` — `2026-06-24-lever1-*` (trB-quantum-integer-form, binding-monodromy-
   hyperbolicity, color-eq-monodromy-integrality, lw-depth2-recurrence-falsified,
   lambda-sw-no-shortcut). The thread is **documented as mapped**, not open.
2. `content/` — `prop:binding-recurrence-extensive` (the kernel proposition).
3. `computations/` — `probes/binding_recurrence_spectral_bridge_probe.py` (live);
   `linking_weight_family_a` (production selector); the Φ_q-tower probes are
   **`_deprecated/`**.
4. coordination — bean `z2bn`; [`docs/coordination/s5-so3-keystone.md`](https://github.com/litlfred/qou/blob/main/docs/coordination/s5-so3-keystone.md).

## The single remaining open piece — owner-gated

`τ = tr B` is a q-family Gauss–Manin **monodromy** trace (the abelianised `λ_SW` real
connection holonomy on the color `E_q`, hyperbolic `SL₂(ℝ)`, `θ_binding = 0.7815`).
Its explicit derivation **is** the s5-so3 keystone `M` (residual i) — **owner-gated**
(precision-goals Subgoal-2; narrow owner reversal applies only to the s5-so3 geometric
`W_λ` build). Refuted shortcuts (recorded, not re-litigated): torus (`2.0437`), golden
`τ=3` (−19% on Family-A), const-coeff depth-2 recurrence beyond seed.

## Verdict

The spectral-selector thread is **CLOSED**. Its mathematical content is the
production `lw(c)` selector + the `R(q,x)` kernel + the sorry-free extensivity Lean
(now q-robust). What remains is **one owner-gated number** (`τ`), not a spectral-probe
re-run. Do not revive the deprecated Φ_q-tower probes.
