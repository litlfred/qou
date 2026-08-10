---
# qou-y6h7
title: 'LP degenerates under convention D: dual runs to solver bound because det G = 0 -- re-pose on H_n/rad = TL_n'
status: todo
type: task
priority: normal
created_at: 2026-08-10T02:23:24Z
updated_at: 2026-08-10T02:26:27Z
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
