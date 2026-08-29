# The addable-box hook identity (B): proof-structure map, one-row brick landed

**Date:** 2026-08-29 · **Beans:** `qou-ognw` (this), `qou-x4zl` / `qou-3quc` (the gap it feeds) ·
**Lean:** [`QOU/MathlibExt/AddableBoxHookOneRow.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/AddableBoxHookOneRow.lean)
(sorry-free) · **Probe:** [`fake_degree_addable_box_recursion_probe.py`](../../computations/qbeta/fake_degree_addable_box_recursion_probe.py)
(B exact `|μ|≤6`).

## The target

The general-`n` fake-degree identity was reduced (PR #5948, `MolienFakeDegreeInduction`, sorry-free)
by induction to the one-step recursion `normalizedSum(n+1)=normalizedSum(n)`, which follows from SYT
branching (A, corpus infra) + the **addable-box hook identity (B)**:

  `Σ_{b addable to μ} q^{−c(b)} · hookProd(μ)/hookProd(μ+b) = 1`  (B′)

(`c(b)=j−i` the added box's content; `hookProd(μ)=∏_{x∈μ}[h_x]_q`).

## What is proved (one-row brick)

For `μ=(n)` the two addable boxes are `(0,n)` (content `n` → `(n+1)`) and `(1,0)` (content `−1` →
`(n,1)`), with `hookProd((n))=[n]_q!`, `hookProd((n+1))=[n+1]_q!`, `hookProd((n,1))=[n+1]_q[n−1]_q!`.
(B′) collapses to the balanced q-integer recurrence

  `[n+1]_q = q·[n]_q + q^{−n}`

which is **`oneRow_addable_hook_recurrence`** (sorry-free), equivalently the existing
`QPartitionCombinatorics.qBracket_add` at `(a,b)=(n,1)`. **So the one-row case is not the open
content** — it is already corpus infrastructure; the brick records it as the induction's base.

## What is NOT proved — and the honest reason (B) is hard

**(B) does not decompose by row count.** The obstruction is concrete: adding the *new-row* box to a
two-row `μ=(a,b)` yields a **three-row** `(a,b,1)` shape, so even the two-row case of (B) requires a
three-row hook product. The relevant closed forms (derived, probe-verified):

  `hookProd((a,b)) = [a+1]_q!·[b]_q! / [a−b+1]_q`,
  `hookProd((a,b,1)) = [a+2]_q[b+1]_q·[a]_q!·[b−1]_q! / [a−b+1]_q`.

So two-row (B) is a rational q-bracket identity in `(a,b)` — provable, but through several hook-product
closed-form lemmas, not one `ring` step.

**The clean general route is contents / partial fractions.** The addable- and removable-box contents
of `μ` **interlace**, and (B) is the residue expansion of a rational function over the content
variable whose poles sit at the removable-box contents. `QOU.SchurWeyl.QJucysMurphyEigen` provides the
contents as q-Jucys–Murphy eigenvalues — the natural tool. This is the same "sum over addable boxes =
1" that underlies the q-Plancherel transition, and formalising it is a genuine multi-lemma project:
(i) the addable/removable-box API over `Nat.Partition` (`YoungDiagramAddCell.cornerAddEquiv` is the
seed), (ii) content interlacing, (iii) the partial-fraction identity.

## Status

One-row brick sorry-free; full (B) is a multi-session hook-length-formula formalisation (`qou-ognw`).
This is honest partial progress on `qou-x4zl`, not a closure. Convergence with #5970's Macdonald
telescope (which may close the whole `normalizedSum=1` residual by a different route) is still open —
see [`docs/coordination/molien-fake-degree-generaln.md`](../coordination/molien-fake-degree-generaln.md).
