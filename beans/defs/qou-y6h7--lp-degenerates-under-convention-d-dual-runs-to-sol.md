---
# qou-y6h7
title: 'LP degenerates under convention D: dual runs to solver bound because det G = 0 -- re-pose on H_n/rad = TL_n'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T02:23:24Z
updated_at: 2026-10-04T15:21:18Z
parent: qou-cdx1
---


## The premise of this bean was wrong — retitle it

Opened on the belief that `rho-k-h3a-gg-trajectory`'s
`y_star[2] = 999999999999998.8` showed an LP dual running to infinity because
`det G = 0` under convention D. **It does not.**

`rho_k_h3a_gg_trajectory.py` prices the LP as

```python
_yc_floor = 1e-15
t_arr = [1.0 / (dim_q[lam] * max(y_chi_abs[lam], _yc_floor)) for lam in parts]
# "Guard against near-zero |y_λ χ^λ| (set to a large finite cost so the
#  LP naturally avoids that channel)."
```

Under D, `y_(1^3) = 0` exactly. The floor engages, the cost becomes
`1/(dim_q · 1e-15) ≈ 1e15` with `dim_q((1,1,1)) ≈ 1`, and that reproduces
`999999999999998.8` to the digit. The dual of a channel the LP never uses equals
its cost. Ordinary LP behaviour; `feasible: true` is correct.

I mistook a sentinel for a symptom, and the mistake was seductive because a real
theorem predicts something that *sounds* the same — `det G = 0`, so the LP over
all `n!` basis elements really does have a corank-dimensional optimum set. Both
statements involve convention D, the antisymmetric block, and an LP. Only one of
them is about this witness.

## What is actually left to do

Two things, neither of them "fix a degeneracy":

- [ ] **Stop publishing a sentinel as a dual.** A witness carrying `1e15` in a
      field named `y_star` invites the misreading above — I am the existence
      proof. The zero-weight channel should be *excluded* from the program and
      recorded as excluded, not priced at `1/(dim_q · floor)`. Same numerical
      answer for the primal, honest witness.
- [ ] **Check whether the floor is now load-bearing where it was not.** Under C,
      `y_(1^3) = 0.0227` and the floor never engaged; under D it engages on every
      three-row channel at every `n`. A guard written for "near-zero, shouldn't
      happen" is now the normal path, and guards used that way tend to hide
      things. Worth auditing every `_yc_floor`-style guard in the LP/SDP
      producers for the same change of status.

## Still open, and genuinely predicted (separate from this bean)

`prf:operator-selection-lp` is posed at `d = n!` (2, 6, 24, 120) while the rank
under D is `C_n` (2, 5, 14, 42). That claim is corrected in the content and
proved in `MarkovGramDegenerate`, but no producer has yet been re-posed on the
quotient. That is real work; it just is not what this witness shows.

## What a "dead channel" is, and how one got into an LP

### What it is

A **channel** is one Wedderburn block `λ ⊢ n` of `H_n(q)`. The Markov trace
restricted to that block is the scalar multiple `y_λ · χ^λ`, so `y_λ` is exactly
"how much this block contributes to any trace".

A **dead channel** is a block with `y_λ = 0`. The trace cannot see it at all — it
contributes nothing to `tr_M`, to any mass, to any binding. It is not small; it
is absent.

Under convention D they die for a structural reason, stated in
`thm:jones-markov-trace`:

> Under convention D that scalar **vanishes** precisely when `ℓ(λ) ≥ 3`: the
> fibre `V` is the two-dimensional fundamental of `SU_q(2)`, so no partition with
> three or more rows survives Schur–Weyl, and `tr_M` is faithful on the two-row
> stratum and on nothing else.

A two-dimensional fibre cannot antisymmetrise three ways. So every block with
three or more rows is dead, and the dead fraction grows fast:

| n | blocks enumerated | live under D | dead |
|---|---|---|---|
| 3 | 3 | 2 | 1 |
| 4 | 5 | 3 | 2 |
| 5 | 7 | 3 | 4 |
| 6 | 11 | 4 | **7** |

The survivors are what `H_n/rad ≅ TL_n` means, and `Σ dim² = C_n` counts them.

### How one was allowed into an LP

Not a bug anyone introduced — a distinction that did not need to exist under
convention C.

`rho_k_h3a_gg_trajectory.py:205` enumerates its channels as

```python
parts = [(3,), (2, 1), (1, 1, 1)]  # all partitions of 3
```

That is **convention-independent**: it is the block list of `H_3`, and it is
correct as a block list. But *which blocks are observable* is
**convention-dependent**. Under C, `y_(1^3) = 0.0227449…` — small, nonzero,
live. All three blocks were channels, the enumeration was right, and no code
needed to tell "block" and "channel" apart.

Under D the two sets stop coinciding, and nothing in the pipeline notices,
because nothing anywhere expresses the difference.

What absorbed it was a guard written for something else:

```python
_yc_floor = 1e-15   # "Guard against near-zero |y_λ χ^λ| (set to a large finite
                    #  cost so the LP naturally avoids that channel)."
```

Under C that branch never executed. Under D it executes on every three-row
channel at every `n` — at `n = 6`, on 7 of 11. **A numerical safety net silently
became the semantic mechanism for excluding dead channels**, and it excludes them
by pricing them at `1e15` rather than by removing them, which is how a sentinel
ended up published in a field named `y_star`.

### So the honest answer to "how was it allowed"

Three things had to line up:

1. The code enumerates **blocks**, not **channels**, and has no vocabulary for
   the difference.
2. Under C the two coincided, so the missing distinction cost nothing and was
   invisible for as long as C was production.
3. A guard for "near-zero, shouldn't happen" quietly became "this is the normal
   path", which is the failure mode guards are worst at announcing.

### Siblings with the same shape

Two more producers enumerate all partitions and weight by `y_λ`:

- `rho_k_h3a_co_casimir.py:222` — `parts = partitions_of(6)`; **7 of 11 dead**
- `deltalambda/he4_stage2_ranking_seminormal_xcheck.py:117` — `pn.partitions_of(N)`

Neither has the `_yc_floor` guard, so whatever they do with a zero weight is a
*different* behaviour and needs checking on its own — division, a silent zero
term, or a rank-deficient matrix. Not assumed either way here.

- [ ] check `rho_k_h3a_co_casimir.py` behaviour on the 7 dead blocks at n=6
- [ ] check `he4_stage2_ranking_seminormal_xcheck.py` likewise
- [ ] give the pipeline a name for "live channel" so the distinction is
      expressible rather than implicit

---

## Second instance, from the convention-D migration (PR #4928)

`rho_k_h3a_lp_dual.py` and `rho_k_h3a_refinement.py` both exit **2** on every
run of the dependency-ordered cascade, and it is the same family of effect as
the sentinel above — not a crash, and not something the migration broke by
accident.

`rho_k_h3a_lp_dual.py:604`:

```python
return 0 if sw_match and lp_primary["feasible"] else 2
```

with `sw_match = sw_err < mp.mpf("1e-40")` (line 341). The witness **is still
written** (line 595, `WitnessBuilder.wrap_legacy(...).save()`) before the
return, so this is a *gate*, not a failure to produce output — which is why
`rho-k-h3a-lp-dual.witness.json` shows up refreshed and structurally clean while
the producer reports non-zero.

So the finding is: **under convention D a shadow-price identity that held to
`1e-40` under convention C no longer does.** Given `y_(1^3) = 0` exactly under
D, the zero-weight channel is degenerate and a `1e-40` cross-check on the duals
is exactly where that degeneracy would surface first.

That makes the "stop publishing a sentinel as a dual" item above load-bearing
rather than cosmetic: while the zero-weight channel is priced at
`1/(dim_q · 1e-15)` instead of being excluded from the program, the duals it
produces are not the duals of the intended program, and no tolerance on them
means anything.

### Do not "fix" this by loosening the tolerance

Widening `1e-40` would turn the gate green while leaving the degenerate channel
in the program — the LP/SDP analogue of rebaselining a precision ratchet, which
AGENTS.md forbids at the producer level for the same reason. Fix the program
(exclude the zero-weight channel and record it as excluded), then re-run and see
whether the identity returns.

### Open question worth answering before this is closed

Is the `1e-40` identity supposed to hold under D at all? It was established
under C, where `y_(1^3) ≈ 0.0227` and every channel is live. If the correct
convention-D program has one fewer channel, the identity may need restating
rather than re-satisfying.

---

## Third instance — and now it is a class, not three bugs

`rho_k_h3a_counit_canonical_integral.py:61` dies under convention D:

```python
delta = 1 / y          # counit block weight
ZeroDivisionError
```

Same root as the other two: **convention D's defining property is that
`y_λ = 0` exactly for `ℓ(λ) ≥ 3`**, so any code that assumes every Wedderburn
block carries a nonzero weight breaks. Under C every block was live
(`y_(1^3) ≈ 0.0227`), so the assumption was invisible.

The three instances, all one pattern:

| site | shape | outcome |
|---|---|---|
| `rho_k_h3a_gg_trajectory` | `1/(dim_q · max(y, 1e-15))` | sentinel `999999999999998.8` published as a dual |
| `rho_k_h3a_lp_dual` | Schur–Weyl gate at `1e-40` | exits 2 |
| `rho_k_h3a_counit_canonical_integral` | `1 / y`, unguarded | `ZeroDivisionError` |

### The class is SMALL — checked, not assumed

Grepping every `y_lambda` consumer for divisions by the weight finds only three
sites, and two are already fine:

* `probe_binding_measure_search.py:125` — guarded:
  `(1 / y[lam] if y[lam] != 0 else mpf(0))`
* `rho_k_counit_defect_form.py:123` — a *label*, `lambda l: mpf(1)`; no division
* `rho_k_h3a_counit_canonical_integral.py:61` — the one unguarded site

So this is a narrow repair, not a systemic rewrite. Worth stating, because
"convention D breaks reciprocals of block weights" sounds like it should be
everywhere and is not.

### Do NOT fix it by copying the guard

`else mpf(0)` is what the sibling does, and it may well be wrong here. `Δ = 1/y`
is the *counit block weight*; when `y = 0` the block is **absent**, and an
absent block is not the same as a block of weight zero — that is precisely the
sentinel-instead-of-exclusion error this bean was opened about. Deciding
between "exclude the block from the sum" and "contribute 0" is a modelling
question about what the counit integral is over, and it should be answered
rather than defaulted.

Note the sibling's guard has the same latent ambiguity and was presumably
written for the same reason; whichever answer is right probably applies to both.
