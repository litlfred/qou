---
# sv8b-step5
title: 'GAP: sv8b step 5 — the Garnir annihilation assembly is the ONLY piece left'
status: in-progress
type: task
priority: high
tags:
    - lean
    - specht
    - okounkov-vershik
created_at: 2026-08-08T09:00:00Z
updated_at: 2026-08-08T19:02:41Z
---

## Why this bean exists

After #4702 and #4719 merged (2026-08-08), every ingredient of
`JucysMurphy.seminormalVector_base_exists` is on `main` **except one gluing
lemma**. This bean states that lemma precisely, because the surrounding
write-ups (bean `sv8b`, the two PR bodies) each describe their own half and
none states the residue as a single closed obligation.

`seminormalVector_base_exists` gates **both** `PlancherelSnData` axioms —
axiom (ii) (`ω = Σc²`) as originally filed, and axiom (i) (`Σ_λ dim² = n!`)
since #4710, whose `burnside_proved` residual `sorryAx` traces to
`JucysMurphy:865` and `SnWedderburnPartitionBridge:234`.

## What is already on main

| Piece | Source |
|---|---|
| `jm_polytabloid_split` — the JM action splits into same-column + off-column | pre-existing |
| `sameColumn_count` — same-column count = `row(s)` (the `−i` half) | #4716 |
| `offColumn_sum` — off-column sum = `col(s)·e_{T₀}` (the `+j` half) | #4719, **conditional on the annihilation** |
| `jm_eigen_colSuperstandard` — both halves assembled to the OV eigenvalue | #4719, same hypothesis |
| `colPattern_smul_of_mem_colStab` — `ρ ∈ colStab t ⟹ colPattern (ρ•t) = colPattern t` | #4702 |
| `exists_collision_earlier_col` — for `c < c'`, a label `x ≠ s` in column `c` shares `s`'s row | #4702 |
| `colGarnir_single_column_of_annihilation` — annihilation ⟹ single-column relation | pre-existing |
| `sum_sign_rep_polytabloid_eq_zero_of_family` — `hfam` ⟹ rep-level annihilation | pre-existing |
| `mtab_sum_sign_smul_of_eq_zero` — a sign-reversing row transposition ⟹ tabloid sum is 0 | pre-existing |

## The one remaining obligation

Discharge the `hann` hypothesis carried by `offColumn_sum` /
`jm_eigen_colSuperstandard`: for each `c < (colSuperstandard μ s).2`,

```
∑ σ ∈ permFixingOutside (insert s (colLabels μ c)),
    sgn(σ) • Mtab.rep μ σ (polytabloid (colSuperstandard μ)) = 0
```

Route — every input exists, nothing new is needed mathematically:

1. Apply `sum_sign_rep_polytabloid_eq_zero_of_family` with
   `G := permFixingOutside (insert s (colLabels μ c))`. It reduces the goal to
   `hfam`: for **every** `ρ : colStab T₀`, the tabloid-level sum over `ρ • T₀` vanishes.
2. Fix `ρ`. Apply `exists_collision_earlier_col` at `t := ρ • T₀`, with `c < c_s`.
   Its hypothesis `colPattern (ρ•T₀) s = c_s` comes from
   `colPattern_smul_of_mem_colStab` + `colPattern_colSuperstandard`.
   This yields `x ≠ s` with `colPattern (ρ•T₀) x = c` and
   `rowPattern (ρ•T₀) x = rowPattern (ρ•T₀) s`.
3. Apply `mtab_sum_sign_smul_of_eq_zero` with `τ := Equiv.swap x s`:
   - `hτ2` — `Equiv.swap_mul_self`
   - `hτsign` — `Equiv.Perm.sign_swap` (needs `x ≠ s`, from step 2)
   - `hτrow` — `Specht.mem_rowStab` from the row equality of step 2
   - `hGclosed` — `G` is closed under right-multiplication by `τ` because both
     `x` and `s` lie in `insert s (colLabels μ c)`; `x ∈ colLabels μ c` follows
     from step 2's column equality together with
     `colPattern_smul_of_mem_colStab` (the column-`c` label set is
     `colStab`-invariant, i.e. `colLabels_smul_of_mem_colStab`).

Then feed the discharged `hann` into `jm_eigen_colSuperstandard` and close
`seminormalVector_base_exists` with the two side conjuncts
(`polytabloid_mem_specht`, and `≠ 0` from standard-basis independence).

## Honest scoping

This is stated as a **route, not a completed proof**. It has not been attempted
in Lean. The step that could still bite is (3)'s `hGclosed`: `permFixingOutside`
is defined by "fixes everything outside `D`", and closure under right-multiplication
by `swap x s` needs both points inside `D` — which the route supplies, but the
Lean bookkeeping around `permFixingOutside`'s membership lemma is where an
unexpected obligation would appear. Do not record this bean as "closed pending
typing"; it is open until it elaborates.

Base ring is genuinely `[Field k] [CharZero k]` — the `[CommRing k]` form is
**false** (contents collide mod `p`). Do not "generalize" it.

## Method rule (carry forward)

Verify with `scripts/lean-direct-cone.sh` (recovered on #4730), **not**
`lake build` — the latter evicts the restored `lake-cache` oleans. The script
passes `-DautoImplicit=false` to match the lakefiles; an axiom query is only as
trustworthy as the olean tree under it (bean `qou-4r5y`).
