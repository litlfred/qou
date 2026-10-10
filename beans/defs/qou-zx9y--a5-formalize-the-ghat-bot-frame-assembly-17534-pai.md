---
# qou-zx9y
title: 'A5: formalize the Ghat_bot frame assembly — 17,534 pairs measured, 0 proved'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-10T07:03:50Z
updated_at: 2026-10-10T07:03:50Z
parent: qou-3e6w
---

Parent epic `qou-3e6w`.  The arc's Lean debt, split out 2026-10-10.

## What is already Lean (sorry-free, on `main`)

| file | role |
|---|---|
| `folio/quantum-observable-universe/lean/QOU/BraidKnot/SearchCoercivity.lean` | `sub_le_mul_of_antitone_step` — the **discrete** step bound `delta(m) = eps(m) − eps(m+1)`, proved by induction, no derivative and no `Real.log`.  This is why a clean coercivity result is *licensed* rather than merely believed. |
| `.../SupergradientCertificate.lean` | the certificate calculus: `box_mul_sub_le`, `boundary_charge_eq_zero`, `abs_charge_pos`, `sup_le_of_supergradient`, `capped_lt_not_sufficient`, `capped_gt_is_sufficient` |

On the PR branch (#7419) three more, taking the file to **nine** declarations with
`#print axioms` → `propext, Classical.choice, Quot.sound` only:

- `box_charge_eq_zero_of_nonpos` — a padded coordinate with `g ≤ 0` and `w = lo` is charged zero
  in **both** branches.  The hypothesis is `≤`, not `<`, because a padded coordinate may have
  gradient exactly zero and there the `if` takes the opposite branch.
- `sum_charge_extend` — its consequence over a `Sum` index.
- `sum_charge_extend_le` — **the honest form, and the one the measurement needs**: it *bounds* the
  padded block rather than deleting it, because that is what a geometrically decaying tail permits
  and a vanishing one would not.  Added after measuring padded charge **2.4707** at `pe = 2`, which
  refuted the design assumption behind the zero version.

## The open debt

**`Ghat_bot`'s assembly over the frame is verified empirically, not proved.**  The per-*pair* step
is the Lean lemma; the assembly

    Ghat_bot(a) =  eps(b0_a + 1)                               one-body slope
                 + Σ_{j : b0_j < b0_a} delta(b0_a − b0_j)      rows BELOW  (gain)
                 − Σ_{j : b0_j > b0_a} delta(b0_j − b0_a)      rows ABOVE  (loss)

is checked over **17,534 `(profile, pe)` pairs with 0 violations** and is **not formalised**.
Note it is a **difference, not a sum** — deep in the staircase there are ~`k` rows *above* a
displaced row contributing losses, where the top edge sits at a free end with almost nothing
above it.  That asymmetry is the substantive content, so a formalisation must not quietly drop the
negative block.

Second item, smaller: the **geometric tail bound** on `cap_sum` (`+ c · _TAIL_C`) is arithmetic in
the probe and has no Lean counterpart.  It must never be a truncated sum — the guard that refuses
one is what caught the `cap == 0` termination bug.

## Verification recipe for this arc's Lean

`lean`-direct, **never `lake build`** against a restored olean cache (it evicts the restore:
measured 6990 → 334 oleans with zero paper-library progress).  Restore from the `lake-cache/*`
orphan branch, set `LEAN_PATH`, run `lean -DautoImplicit=false -s 65536 <file>`; exit 0 and
`#print axioms` showing no `sorryAx` is the gate.  Prefer the repo's sweep over bare `lean`-direct
where one exists.

**Do not close until the frame assembly is proved or explicitly scoped as unformalised in the
consuming claim.**
