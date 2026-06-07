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

| | Path A (main) | Path B (this branch) |
|---|---|---|
| route | R-matrix / Schur-Weyl on V^⊗3 → Jones polynomial of 𝓑₃ → `V/[2]_q²` | signed seminormal Hecke characters (`homfly_ocneanu_trace`), skein-validated |
| where | content `.md` "Proof.", PR #1933 (T17), #1942 (content) | `borromean_chi_independent_crosscheck.py`, PR #1947 |
| status | **narrative proof**, *cites* Borromean Jones poly (Murasugi 1996) + polynomial long division | **numerical** computation (χ float64-bounded via `chi_lambda_braid`) |
| Lean | **none** — `.ts` `lean.ref` `QOU.BraidsAndKnots.borromean_markov_trace_closed_form` has **no `.lean` sibling** (stub ref) | n/a (numerical) |
| rigor | rigorous modulo the cited topological input | corroboration only |

**Agreement:** the three `χ^λ` forms match to **≤ 4e-50** at every tested q
(`borromean-chi-independent-crosscheck.witness.json`). This is an independent
**numerical confirmation** of Path A's per-rep decomposition — *not* a theorem
that the two paths are equivalent.

## 3. Are the normalizations documented and proved?

| item | documented? | proved? | where |
|---|---|---|---|
| Markov normalization `Σ_λ y_λ d_λ = 1`, `tr_M = V/[2]_q²` | yes | identity stated; `tr_M` *uniqueness* has Lean `sorry=1` (cheat sheet step 3) | **paper** (content block lines 32–33, 126–132) |
| `y_{(2,1)}(q=1) = 1/4` | yes | "derived" in T18 — an **exploratory probe commit**, within-H₃, *not* a paper proof | commit `b6c23f20` |
| Borromean closed form itself | yes | **narrative only, no Lean** | paper (content block) |
| HOMFLY weights `w_λ` (this engine) | yes | **numerically** solved + held-out-validated, not symbolically proved | `homfly_ocneanu_trace.py`, convention doc §7 |
| `y_λ` vs `w_λ` non-equivalence | yes | numerically shown (q-dependent ratio) | **repo doc** `homfly-markov-convention-discipline.md §7` (not paper, not previously an audit) |

## 4. Honest gaps (on the record)

1. **Path A is not Lean-verified.** The content prop's `lean.ref` is a stub.
   Lean-formalizing the *algebraic* core (given `V(𝓑₃)`, the long division →
   closed form is `field_simp; ring`) is tractable and turns Path A from
   narrative into Lean-verified-modulo-the-cited-`V`. Coordinate with #1942
   (it owns the content block).
2. **Path B is numerical** and float64-bounded (the `chi_lambda_braid`
   precision ceiling, see `homfly_ocneanu_trace._chi`). It corroborates; it
   does not prove.
3. The convention reconciliation lives in a **repo doc**, not the paper. If the
   two-thread distinction matters for the paper's exposition, it should be
   surfaced there.

## 5. Cheat-sheet reflection

`docs/canonical-derivation-cheat-sheet.md` treats seminormal (Hoefsmit) and
R-matrix as machinery of the *same* step (step 1 cat-action + step 6 χ^λ via
Hoefsmit seminormal; `tr_M = Σ y_λ χ^λ` step 5). The seminormal-vs-R-matrix
**numerical agreement** is now recorded there as an explicit checkpoint (added
on this branch) with the honest "numerical, not proved" label.
