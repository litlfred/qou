# Keystone Identity I (A), reduced to six finite sub-identities — the hook-length formula is OFF the critical path (constructive proof)

**Date:** 2026-06-24
**Branch:** `claude/optimistic-meitner-owwu8n`
**Status:** complete arm–leg reduction of the per-partition identity (A); algebraic
core **Lean-proved sorry-free**; the per-partition statement **exhaustively
machine-verified for every partition through `n = 12`** (271 partitions); nothing
archimedean (`q₀` and the 210 ppb target never appear); no fit.
**Lean:** [`IdentityIContentDecomposition.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/IdentityIContentDecomposition.lean)
(`identityA_algebra` sorry-free; `partitions` + `identityA_exhaustive_n12` +
`partitionCounts` sorry-free `native_decide`).

## Context

The keystone `W_λ` defect cubic `144·C(n) = −n(n−1)(2n−13)`
([`2026-06-20-keystone-wlambda-C-n-closed-form.md`](2026-06-20-keystone-wlambda-C-n-closed-form.md))
carries exactly one representation-theoretic input, **Identity I**
`M(n) = (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c} h_c² = n(3n−1)/2`, which the prior audit
([`2026-06-23-keystone-identity-I-content-decomposition.md`](2026-06-23-keystone-identity-I-content-decomposition.md))
factored as `M(n) = binom(n,2) + n²` via

- **(A)** the per-partition `Σ_c h_c² = Σ_c c(c)² + n²` (single Young diagram), and
- **(B)** the Jucys–Murphy Plancherel content-square mean `E_Planch[Σc²] = binom(n,2)`.

This note **constructively reduces (A) itself** — previously carried with one opaque
`sorry` framed as "needs `YoungDiagram` hook/content infrastructure" — to a pure
algebraic combination of **six finite, formula-free sub-identities**, and proves the
algebraic combination sorry-free. The **Frame–Robinson–Thrall hook-length formula is
not among them.**

## The reduction (0-indexed cells, the `List ℕ` computable model)

For a weakly-decreasing `l = (λ_0 ≥ λ_1 ≥ … ≥ λ_{r-1})`, cell `(i,j)` with
`0 ≤ i < r`, `0 ≤ j < λ_i`, has arm `a = λ_i − 1 − j`, leg
`ℓ = colLen_j − 1 − i` (`colLen_j = #{i : λ_i > j}`), hook `h = a + ℓ + 1`, content
`c = j − i`. Write the totals

```
n   = Σλ_i             (size)
p2  = Σ λ_i²            q1 = Σ i·λ_i       q2 = Σ i²·λ_i     s2 = Σ i·λ_i²
a1  = Σ_c a            a2 = Σ_c a²        l1 = Σ_c ℓ        l2 = Σ_c ℓ²
al  = Σ_c a·ℓ          c2 = Σ_c c²        h2 = Σ_c h².
```

Expanding `h² = (a+ℓ+1)² = a² + ℓ² + 1 + 2aℓ + 2a + 2ℓ` and summing gives the
**hook-square expansion**

> **(E)**  `h2 = a2 + l2 + n + 2·al + 2·a1 + 2·l1`.

Six finite sub-identities then collapse everything to single-row data:

| id | statement | nature |
|---|---|---|
| **(E)** | `h2 = a2 + l2 + n + 2·al + 2·a1 + 2·l1` | per-cell square expansion |
| **(Arm)** | `2·a1 = p2 − n` (`Σ_c a = Σ_i binom(λ_i,2)`) | single-row |
| **(Cont)** | `c2 = a2 − s2 + q1 + q2` | single-row (`Σ_{j<λ_i}(j−i)²`) |
| **(Leg1)** | `l1 = q1` (`Σ_c ℓ = Σ_j binom(colLen_j,2) = Σ_i i·λ_i`) | conjugate column-sum |
| **(Leg2)** | `l2 = q2` (`Σ_c ℓ² = Σ_i i²·λ_i`) | conjugate column-sum |
| **(Cross)** | `2·al = n² − p2 − s2 − q1` | **sorted** double-count |

**(Cross) is where weak-decreasingness is used.** The cross term double-counts
"L-triples" (a cell, one strictly to its right, one strictly below):

```
al = Σ_{i<i'} Σ_{j'=0}^{λ_i−1} min(j', λ_{i'}),
```

and **sortedness** (`λ_i ≥ λ_{i'}` for `i < i'`) removes the `min`
(`Σ_{j'} min(j',λ_{i'}) = binom(λ_{i'},2) + λ_{i'}(λ_i − λ_{i'})`), giving the closed
form `2·al = n² − p2 − s2 − q1` — polynomial in the parts, no `min`, no conjugate.

### Algebraic collapse (the Lean-proved core)

Substituting (Leg1), (Leg2), (Cross), (Arm) into (E):

```
h2 = a2 + q2 + n + (n² − p2 − s2 − q1) + (p2 − n) + 2q1
   = a2 − s2 + q1 + q2 + n²,
```

while (Cont) gives `c2 + n² = (a2 − s2 + q1 + q2) + n²`. Hence **`h2 = c2 + n²`** — the
identity (A). This is a pure ℤ identity once the six facts are in hand; it is
Lean-proved sorry-free as

```lean
theorem identityA_algebra
    (n p2 q1 q2 s2 a1 a2 l1 l2 al c2 h2 : ℤ)
    (hHook  : h2 = a2 + l2 + n + 2*al + 2*a1 + 2*l1)
    (hArm   : 2*a1 = p2 - n)
    (hCont  : c2 = a2 - s2 + q1 + q2)
    (hLeg1  : l1 = q1)  (hLeg2 : l2 = q2)
    (hCross : 2*al = n^2 - p2 - s2 - q1) :
    h2 = c2 + n^2 := by subst hLeg1; subst hLeg2; linarith
```

**Non-vacuous.** The hypotheses are genuine intermediate sums (`Σarm`, `Σleg`,
`Σarm·leg`, the content/leg conjugate sums) — *not* the conclusion. The theorem
derives `Σh² = Σc² + n²` from them by algebra; it is not a self-assuming projection
(AGENTS.md §1a).

## What this re-scopes

The residual Lean fill for (A) is now **six precisely-characterized finite
identities**, none of which is the hook-length formula:

- **(E), (Arm), (Cont)** are single-Young-diagram / single-row sums over `List.range`
  — elementary `Finset`/`List` `BigOperators` lemmas (no representation theory).
- **(Leg1), (Leg2)** are the conjugate column-sums `Σ_j f(colLen_j)` — a finite
  double-count over the parts (the `colLen`-filter ↔ part-pair bijection).
- **(Cross)** is the sorted L-triple count — the one place weak-decreasingness enters.

So the corpus framing *"Identity I needs SYT-dimension / hook-length infrastructure"*
is now sharpened: the **hook-length formula is off the critical path entirely**, and
the genuine residual is a self-contained finite-combinatorics fill (still multi-session
in Lean, but no longer gated on an absent Mathlib theorem). The Plancherel half **(B)**
(`E_Planch[Σc²] = binom(n,2)`, via `Σ(dim λ)² = n!` + Jucys–Murphy centrality) remains
the only piece needing genuine `ℂ[S_n]` Wedderburn/JM infrastructure.

## Verification

- **Lean (sorry-free):** `identityA_algebra` (`linarith`); `partitionCounts`
  (`p(n) = 1,2,3,5,7,11,15,22,30,42,56,77` for `n = 1..12`, proving the enumerator is
  complete); `identityA_exhaustive_n12` (the per-partition `Σh² = Σc² + n²` for **every
  partition through `n = 12`**, 271 partitions, `native_decide`). All check via
  lean-direct (`EXIT 0`).
- **Python (exact integer, `n = 1..22`, 4507 partitions):** the six sub-identities
  (E)/(Arm)/(Cont)/(Leg1)/(Leg2)/(Cross) and the assembled `Σh² = Σc² + n²` all hold.

## Discipline

- **No fit.** An exact identity, algebraic core proved + per-partition machine-checked;
  `q₀` / 210 ppb never used. Concerns the `q→1` leading datum `M(n)` of `W_λ`, the one
  carried input to the *falsifiable* `C(n)` sub-target.
- **No correspondence chain.** Pure `S_n` / Young-diagram combinatorics; the
  `2I→E₈→Lawrence–Zagier` chain is never invoked.
- **Owner-gate respected.** Inside the 2026-06-19 narrow reversal for the keystone
  geometric `W_λ` construction; no physical claim, nothing wired to production.
- **Corpus-grep done.** The content/JM eigenbasis (`θ_λ = q^{2c(λ)}`) is in-corpus; the
  *arm–leg six-identity reduction of (A)* (this doc) is new — the corpus framed (A) via
  the hook-length formula or the β-set, not this single-row collapse.

## Cross-references

- [`2026-06-23-keystone-identity-I-content-decomposition.md`](2026-06-23-keystone-identity-I-content-decomposition.md) — the (A)+(B) decomposition this note's (A) reduction refines.
- [`2026-06-20-keystone-wlambda-C-n-closed-form.md`](2026-06-20-keystone-wlambda-C-n-closed-form.md) — the `C(n)` cubic; Identity I as the carried input.
- [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) — the defect file carrying Identity I in `twoM`.
- [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger.
