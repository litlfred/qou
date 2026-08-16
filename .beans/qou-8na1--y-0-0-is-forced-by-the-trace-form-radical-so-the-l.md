---
# qou-8na1
title: y_0* = 0 is forced by the trace-form radical, so the LP shadow price prices nothing
status: todo
type: task
created_at: 2026-08-16T13:18:20Z
updated_at: 2026-08-16T13:18:20Z
---


Split out of `qou/k4f8` (#5239), which established the fact. This bean carries
the **content** consequence, which is not a Lean question and needs an owner
decision.

## The fact

Exact in ℚ(q), 18/18 checks, no floating point —
`computations/operator_selection_lp_symbolic_qq.py`. For `H₃(q)`, `d = 6`:

- `t` is row 0 of `G`, structurally: `tⱼ = tr_M(bⱼ) = tr_M(b₀bⱼ) = G₀ⱼ`.
- `det G = 0` **identically**; rank 5; radical `v = (−q³, q², q², −q, −q, 1)`,
  the q-antisymmetriser.
- Pairing the dual equation with `v` gives `0 = ⟨t,v⟩ = y₀⟨𝟙,v⟩`, and
  `⟨𝟙,v⟩ = −(q−1)(q²−q+1)`. So **`y₀ = 0` for every dual-feasible `(y₀,s)` at
  every `q ≠ 1`** — no `s ≥ 0`, no symmetry, no primal feasibility needed.

Lean: `y_0_eq_zero_of_radical` in `operator_selection_lp.lean` (holds over any
commutative ring without zero divisors).

## Why it is a content problem

The dual objective is `n_target · y₀`. With `y₀ ≡ 0` the LP's optimal value is
`0` **for every `n_target`** — the quantity meant to price the net constraint
cannot respond to it. Consequences to adjudicate:

1. `a_K^{dual_ratio} = y₀*_atom / y₀*_free` is `0/0` symbolically.
   `aK_via_lp_dual_hecke_basis.py` guards `abs(u0) > 1e-12` and records
   `a_K^chi_active` as undefined when it trips. **The guard is firing on an
   identity, not on noise** — it is reporting the structure correctly while
   describing it as a numerical edge case.
2. The header of that script says the *previous* Wedderburn-block LP "gave
   degenerate duals (y_0^* = 0 for A ≥ 2)" and moved to the full Hecke basis
   to escape it. The full basis has the same property. `H₂` does **not**
   (`det G = (q⁴+q²+1)/(q²+1)² ≠ 0`), so this is an `H₃` fact, not a
   formulation artifact — the move could not have helped.
3. `prop:mass-coefficient-shadow-price` is the block that reads `y₀*` as a
   shadow price. That reading is what is in question, not the LP algebra.

## `qou/pin3` is NOT this — checked, and my guess was wrong

When this bean was filed I flagged `pin3` ("regeneration picks a DIFFERENT
optimal LP dual vertex") as plausibly the same degeneracy seen from the
numerics side. **It is not**, and the reasoning that suggested it does not
transfer. Checked in `computations/alpha_5_lp_dual_crystal_closed_form.py`:

`alpha_5_lp_dual_crystal.py` builds `G = diag(|weight_λ|)` — a *diagonal*
matrix, not a trace form — and its `t` is `q`-content of shapes, unrelated to
`G`. Neither hypothesis of `y_0_eq_zero_of_radical` holds there: no weight is
zero (min `|w|` = 2.2e-06), so there is **no radical at all**, and `t` is not
a row of `G`, so `⟨t,v⟩ = 0` would fail even if there were one.

That LP is in fact solvable in closed form — `x* = n_target·e_argmin(t)`,
`y₀* = min_j t_j`, `s*_j = (t_j − min t)/|w_j|` — verified against every field
of every stratum of the committed witness. Its dual optimum is a **unique
point**, so `pin3`'s own "different vertex" diagnosis is wrong too. The real
cause there is that `s*` divides by `|w| ~ 1e-06`, amplifying a
solver-tolerance error in `y₀*` by ~1e+05. Written up in `pin3`.

Keep the two separate. The only thing they share is the word "degenerate".

## Not claimed here

That the physics is wrong. The LP may simply be the wrong instrument for the
attribution it is being asked to make, or `n_target` may need to enter
somewhere other than the net constraint. Deciding that is the owner's, not a
mechanical check's.

## Next

- [ ] Owner decision on `prop:mass-coefficient-shadow-price`
- [x] Check `qou/pin3` against this — **different**, see above
- [ ] Re-read the `a_K` extraction chain for other divisions by `y₀*`
