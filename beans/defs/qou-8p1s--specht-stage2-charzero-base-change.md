---
# qou-8p1s
title: 'specht: Stage 2 of specht_form_nondegenerate — general CharZero via Q base change'
status: todo
type: task
created_at: 2026-08-07T09:20:00Z
updated_at: 2026-08-07T09:20:00Z
---

The last `sorry` in `QOU/BraidKnot/SpechtIrreducible.lean`
(`specht_form_nondegenerate`, general `[Field k] [CharZero k]`).

## State

**Stage 1 is DONE** (2026-08-07, sorry-free, `#print axioms` clean):
`bilinM_self_eq_zero_iff`, `specht_form_nondegenerate_ordered`, and the
downstream `specht_isSimple_ordered` cover every ordered field -- so `Q` and
`R`, the archimedean evaluation the framework actually uses.  Over an ordered
field the module has **no residual core**.

What remains is only the case of a characteristic-zero field with no compatible
order -- `C` being the one that matters.  Stage 1 provably cannot reach it: the
form is bilinear, not sesquilinear, so over `C` it has isotropic vectors
(`x = (1, i)` gives `<x, x> = 0` with `x != 0`).

## This is NOT blocked on literature

James's hook-length Gram determinant would suffice but is **not necessary**.
The lighter route is rationality + rank invariance:

1. `S^mu` is spanned by polytabloids, whose tabloid coordinates are `0, +-1`,
   so `S^mu` over `k` is the base change of `S^mu` over `Q`.
2. Over `Q` the restricted form is positive definite by Stage 1, so a Gram
   matrix of a `Q`-basis has full rank.
3. Rank of a fixed `Q`-matrix is invariant under the field extension `Q -> k`,
   so the restricted form stays nondegenerate over `k`.

## What is actually missing

Lean/Mathlib infrastructure, not a citation:

* a base-change lemma identifying `SpechtSubmodule (k := k)` with
  `SpechtSubmodule (k := Q)` extended along `Q -> k` (needs the polytabloid
  coordinates to be visibly `Z`-valued and the span to commute with the
  extension);
* rank invariance under field extension, transported onto that span rather
  than stated for a bare `Matrix`.

## Why it may not be urgent

Check first whether any downstream consumer needs `C` at all.  If the framework
only ever evaluates over `R`, `specht_isSimple_ordered` already discharges the
obligation and this bean is documentation-only.

---

## Route ELIMINATED (2026-08-07): James's dichotomy cannot close this

`bilinM_polytabloid_self` (`<e_t, e_t> = |C_t|`) is now recovered and sorry-free,
along with `specht_not_le_perp` (in char 0 the form does not vanish on `S^mu`).
That was the natural next hope, so record what it does and does not buy.

Feeding the radical `R = S^mu inf (S^mu)-perp` — which IS `S_n`-stable — into
the already-proved `specht_submodule_dichotomy` gives
`S^mu <= R` **or** `R <= (S^mu)-perp`:

* the first branch **is now killed** by `specht_not_le_perp` (it would force
  `|C_t| = 0`, false in char 0);
* the second branch is **vacuous** — it holds by construction.

And the vacuity is structural, not a phrasing artifact. By `kapL_mem_line`,
`kappa_t x = lambda_t(x) . e_t`; by `kapL_selfadjoint` with `<{t}, e_t> = 1`,

    <e_t, x> = <kappa_t {t}, x> = <{t}, kappa_t x> = lambda_t(x)

so the dichotomy's "`kappa_t x = 0` for all `t`" branch says **exactly**
`x in (S^mu)-perp` — literally the hypothesis one already has. **The dichotomy
cannot separate `R = bot` from `R /= bot`, in any characteristic.**

Do not re-attempt a James-theorem route. Stage 2 needs the rank / base-change
input described above and at the `sorry`.
