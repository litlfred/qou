# Borromean χ^λ cross-method agreement — proof-status audit

**Date:** 2026-06-07 · **Branch:** `claude/homfly-borromean-crosscheck-2026-06-07`
· **PR:** #1947 · **Trigger:** owner — *"are these equivalent paths proved in
the paper? … are normalizations documented and proved? in audit docs? in
paper?"*

This audit records, honestly and without overclaim, the proof status of the
Borromean Markov-trace per-representation result and its independent
cross-check — because the cross-check could easily be mis-read as "two proofs"
when it is one narrative proof + one numerical confirmation.

## 1. The result

`prop:borromean-markov-trace-closed-form`
(`content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md`):

```
χ^{(3)}(β_Bor) = χ^{(1³)}(β_Bor) = 1
χ^{(2,1)}(β_Bor) = (−q¹²+3q¹⁰−3q⁸+4q⁶−3q⁴+3q²−1)/q⁶ = 2 − 3h⁴ − h⁶
tr_M(β_Bor)      = (4 + h² − 3h⁴ − h⁶)/(h² + 4),   h = q − q⁻¹
```

with `β_Bor = (σ₁⁻¹σ₂)³`.

## 2. The two methods (NOT two proofs)

> **Correction (2026-06-07, same day).** An earlier version of this audit said
> Path A "has no `.lean` sibling (stub ref)". That was **wrong** — I checked
> only the `.md` sibling path, not the package path (the precise corpus-grep
> failure AGENTS.md "Before declaring open/missing" warns against). The
> declaration exists and is **fully proved** at
> `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanMarkovTrace.lean`.
> The table below is corrected.

| | Path A (main) | Path B (this branch) |
|---|---|---|
| route | R-matrix / Schur-Weyl on V^⊗3 → Jones polynomial of 𝓑₃ → `V/[2]_q²` | signed seminormal Hecke characters (`homfly_ocneanu_trace`), skein-validated |
| where | content `.md` "Proof." + Lean `BorromeanMarkovTrace.lean`; PR #1933 (T17), #1942 | `borromean_chi_independent_crosscheck.py`, PR #1947 |
| **tr_M closed form** | **Lean-proved, sorry-free** (`borromean_markov_trace_closed_form` via `field_simp; ring`) — the *algebraic* core, modulo the two cited topological inputs below | n/a |
| topological inputs | `V(𝓑₃)` = Murasugi Jones poly + `tr_M = V/[2]_q²` — **cited** (`[murasugi1996]`,`[jones1987]`), stated as premises in the `.lean` docstring, not themselves Lean theorems | n/a |
| **per-rep `χ^λ`** (`χ^{(3)}=χ^{(1³)}=1`, `χ^{(2,1)}=2−3h⁴−h⁶`) | **narrative-only** (`.md` lines 93–111) — **NOT** in `BorromeanMarkovTrace.lean` | **numerical** confirmation (χ float64-bounded via `chi_lambda_braid`) |

**What this cross-check actually anchors.** The `.lean` proves the *tr_M
closed form*; the *per-representation `χ^λ` decomposition* is narrative-only.
This script's value is precisely there: it gives an independent **numerical
confirmation** (≤ 4e-50, `borromean-chi-independent-crosscheck.witness.json`)
of the per-rep `χ^λ` forms that are **not** Lean-covered — *not* a theorem of
equivalence, and *not* redundant with the Lean (different layer).

## 3. Are the normalizations documented and proved?

| item | documented? | proved? | where |
|---|---|---|---|
| Markov normalization `Σ_λ y_λ d_λ = 1`, `tr_M = V/[2]_q²` | yes | identity stated; `tr_M` *uniqueness* has Lean `sorry=1` (cheat sheet step 3) | **paper** (content block lines 32–33, 126–132) |
| `y_{(2,1)}(q=1) = 1/4` | yes | "derived" in T18 — an **exploratory probe commit**, within-H₃, *not* a paper proof | commit `b6c23f20` |
| Borromean `tr_M` closed form | yes | **Lean-proved, sorry-free** (algebraic core; topological inputs `V(𝓑₃)`, `tr_M=V/[2]²` cited) | `BorromeanMarkovTrace.lean` + paper |
| per-rep `χ^λ` forms | yes | **narrative only, not in `.lean`**; numerically confirmed by this PR | paper `.md` lines 93–111 |
| HOMFLY weights `w_λ` (this engine) | yes | **numerically** solved + held-out-validated, not symbolically proved | `homfly_ocneanu_trace.py`, convention doc §7 |
| `y_λ` vs `w_λ` non-equivalence | yes | numerically shown (q-dependent ratio) | **repo doc** `homfly-markov-convention-discipline.md §7` (not paper, not previously an audit) |

## 4. Honest gaps (on the record)

1. **tr_M closed form IS Lean-proved** (`BorromeanMarkovTrace.lean`,
   sorry-free, `field_simp; ring`) — modulo the two *cited* topological inputs
   (`V(𝓑₃)` = Murasugi Jones poly; `tr_M = V/[2]²`), which are premises, not
   Lean theorems. The remaining genuine gap is the **per-rep `χ^λ`
   decomposition** (`χ^{(3)}=χ^{(1³)}=1`, `χ^{(2,1)}=2−3h⁴−h⁶`), which is
   **narrative-only**. A tractable next step (coordinate with #1942): a Lean
   lemma proving the q-form↔h-form *algebraic equivalence*
   `(−q¹²+3q¹⁰−…−1)/q⁶ = 2−3h⁴−h⁶` (`field_simp; ring`) — note this proves the
   two *forms* agree, not that the character *equals* them (the latter needs
   the seminormal-rep machinery).
2. **Path B is numerical** and float64-bounded (the `chi_lambda_braid`
   precision ceiling, see `homfly_ocneanu_trace._chi`). It corroborates the
   narrative-only per-rep forms; it does not prove them.
3. The convention reconciliation lives in a **repo doc**, not the paper. If the
   two-thread distinction matters for the paper's exposition, it should be
   surfaced there.

## 5. Cheat-sheet reflection

`docs/canonical-derivation-cheat-sheet.md` treats seminormal (Hoefsmit) and
R-matrix as machinery of the *same* step (step 1 cat-action + step 6 χ^λ via
Hoefsmit seminormal; `tr_M = Σ y_λ χ^λ` step 5). The seminormal-vs-R-matrix
**numerical agreement** is now recorded there as an explicit checkpoint (added
on this branch) with the honest "numerical, not proved" label.
