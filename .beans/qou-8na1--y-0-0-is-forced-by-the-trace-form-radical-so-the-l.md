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

---

## 2026-08-21 — confirmed against the corpus's own committed numerics

The ℚ(q) analysis above was symbolic. `computations/a-K-via-lp-dual-hecke-basis.witness.json`
is the committed f64 solve of the same LP, and it agrees **exactly**, for both
atoms:

| predicted in ℚ(q) | witness (proton and neutron) |
|---|---|
| `y₀* = 0`, forced by the radical | `y0_star = -0.0` |
| `s = e₀`, the unique non-negative certificate for `q > 0` | `y_star = [1.0, 0, 0, 0, 0, 0]` |
| optimal value `n_target · y₀* = 0` | `primal_obj ≈ -5e-11`, `dual_obj = 0.0` |
| — | `chi_y_sum = 1.0`, `sc_y_sum = 0.0` |

So this is not a symbolic curiosity that numerics might contradict. The numerics
already showed it and were read as a solver artifact.

### The sharper consequence for `prop:mass-coefficient-shadow-price`

Re-reading the block: it claims `c_λ = y_λ* · m_e`, where `y_λ*` is the dual of
the **Frobenius** constraint on Wedderburn block `λ` — *not* the net-constraint
dual `y₀*`. My earlier note conflated the two, which understated the problem.

`y_star = e₀` says **every Frobenius shadow price except index 0 is exactly
zero**, and index 0 is `𝟙`, the identity element — not a partition block at all.
So if mass coefficients are Frobenius shadow prices, then on this LP **all but
one coefficient is zero**. That is a stronger and more direct contradiction of
the block than the `y₀* = 0` observation, and it does not depend on the
NF-index → Wedderburn-block assignment being exact (the script's own comment
calls that assignment "approximate").

### A tension worth flagging, not resolving

`x_star[0] = -1000000.0` in the witness — exactly `-M_bound`. **The box binds at
the solver's optimum.** Bean `qou/0tjt` concluded the box is non-binding at `x*`,
and `operator_selection_lp.lean` drops the box on that basis.

Both can be true without contradiction: the optimal face here is large (I showed
the radical direction `x* = c·v` is also optimal, with every Frobenius constraint
tight and the box slack), so the LP has many optima and the solver landed on a
box vertex while `0tjt` reasoned about a different one. The *value* and the
*duals* — which are what the content claims rest on — agree either way. But
"the box is non-binding at x*" is true of a particular `x*`, not of the LP, and
the Lean's justification for dropping the box should say so.

## Next

- [ ] **Owner ruling** on `prop:mass-coefficient-shadow-price`, now with the
      numerics confirming the symbolics. The options are unchanged — retract /
      restate, move the extraction off the LP, or change where `n_target`
      enters — but the evidence is no longer contestable as a precision artifact.
- [ ] Re-word the box justification in `operator_selection_lp.lean` and in
      `qou/0tjt`: non-binding **at the radical optimum**, not at every optimum.
- [ ] Re-read the `a_K` chain for other divisions by `y₀*` or by a `y_λ*` that
      is now known to be zero.
