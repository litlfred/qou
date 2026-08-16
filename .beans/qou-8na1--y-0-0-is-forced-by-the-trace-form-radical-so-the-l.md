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

## Likely connection worth checking

`qou/pin3` — "regeneration picks a DIFFERENT optimal LP dual vertex" — is
exactly what a degenerate dual produces: the dual optimum is a face, not a
vertex, so any solver may land anywhere on it. Check whether `pin3` is this
same degeneracy seen from the numerics side before treating them separately.

## Not claimed here

That the physics is wrong. The LP may simply be the wrong instrument for the
attribution it is being asked to make, or `n_target` may need to enter
somewhere other than the net constraint. Deciding that is the owner's, not a
mechanical check's.

## Next

- [ ] Owner decision on `prop:mass-coefficient-shadow-price`
- [ ] Check `qou/pin3` against this — same degeneracy or different?
- [ ] Re-read the `a_K` extraction chain for other divisions by `y₀*`
