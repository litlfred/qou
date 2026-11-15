---
# qou-bygw
title: 'Which prime closure carries the many-body cumulants: the all-pairs band routing is not a chain'
status: completed
type: task
priority: normal
created_at: 2026-09-03T20:24:04Z
updated_at: 2026-09-05T06:15:33Z
---


Opened from `qou-m3sh` (2026-09-03), which ended with two theorems that
between them relocate the binding-gap search:

1. **The canonical closure is a chain** (linear connected sum of `(2, odd)`-
   torus knots, `prop:canonical-closure-torus-chain`), so its Markov trace is
   a PRODUCT of two-strand factors `z + d` (checked to 1e-59 at A ≤ 4,
   `the_canonical_mass_trace_factorises_over_the_chain_probe`; factor algebra
   in `QOU.Mass.ChainTraceFactor`). Its `L` is exactly additive over
   interfaces: the canonical closure carries NO many-body binding, by theorem.
2. The many-body cumulants the binding arc measures — `c₃ < 0`, `c₄ < 0`,
   `c₅ > 0`, the order-six datum (`qou-wx83`, `prop:subset-cumulant-recursion`)
   — belong to the ALL-PAIRS bond model, whose band-routed bonds interleave
   generators across blocks and destroy the chain form.

So the question is no longer "which invariant carries the twist" (answered:
none of the knot type, `rem:frenet-framing-is-not-an-invariant`) but **which
prime closure carries the cumulants.** Concretely:

- [ ] Take the all-pairs bond word for A = 3, 4 (both classical branches of
      the averaged letters, as in the chain probe) and decide whether its
      closure is composite. Test: does the Jones/HOMFLY polynomial factor as a
      product of the per-component or per-bond torus-link polynomials? Does
      the linking graph stop being a path? A prime, non-split closure is the
      first thing that COULD carry `c₃`.
- [ ] **BLOCKED on a modelling decision, not on a computation.** Identifying
      the link needs a word, and the model supplies only a multiset. Three ways
      out, none of them mine to take: name a canonical bond ordering and defend
      it physically; symmetrise over orderings (a choice, not a derivation, and
      it does not obviously close under the Markov trace); or drop the
      braid-word presentation, since pairwise bonds applied *simultaneously*
      are not a braid word at all. Once an ordering is fixed this item is a
      short spherogram run.
- [ ] Which cumulant order first fails to factor is a topological statement
      about the closure (a `k`-body term needs a sublink on `k` blocks that
      is not a connected sum); compare with the arc's sign pattern `+ − − + −`.
- [ ] Borromean-type linking (pairwise-unlinked, triple-linked) versus
      chain-type: `atom_closure_milnor_indeterminacy_probe` already showed the
      canonical closure is neither Brunnian nor unknotted per component. Redo
      that census on the all-pairs closure.

Not the question: any new bond model. The all-pairs model is the one whose
cumulants exist; this asks what link it is.

## Two things found on the way that are not about links

**The `3H` all-pairs agreement with AME is an ordering artifact.**
`pairwise_ceiling_is_overstated_probe` reports `AME/allpairs = 1.00418` for
`3H` and hedges it heavily as "one number out of three". There is now a
mechanism: across the six bond orderings the ratio spans **0.9675 … 1.0598**.
The 1.004 belongs to the four-ordering majority class; a single reordering
moves it to 1.060. The hedge was right and the reason is now concrete.

**At A = 2 the model inverts the physics, with no convention in play.**
One bond, one word, no ordering or arrangement to choose:

| system | bond | L | B (MeV) | reality |
|---|---|---|---|---|
| ²He | pp | 0.489899 | 2.0507 | UNBOUND (no bound diproton) |
| ²H  | pn | 0.676822 | 2.8332 | BOUND, 2.22452 MeV |
| 2n  | nn | 0.907262 | 3.7978 | UNBOUND (no bound dineutron) |

The model ranks `nn > pn > pp`; reality binds only `pn`. The sibling's charge
term `−(e/2)log(1−h) = +0.1173 e` raises pp and pn and leaves nn alone, so it
deepens the inversion rather than repairing it. Honest caveat: this arc's `L`
carries no spin, and the real distinction is a spin one — the deuteron binds
in the triplet channel and every ¹S₀ two-body system is unbound — so a
spinless bond constant cannot be expected to separate them. What it can be
expected not to do is rank the unbound `nn` system above the bound `pn` one.
Worth its own bean; it is upstream of every cumulant question.


## Convergence with the sibling arc (2026-09-04)

Merging `main` surfaced `docs/audits/2026-09-04-monotone-word-trace-factorizes-derived-link-map.md`
(beans `qou-kru4`, `qou-5vhf`), which reaches this bean's central finding from
the algebra side and supplies the closed form this bean only measured:

    content_reorder_defect:
    tr(g0 g1 g0 g2 g1) = (product over the same content) + z (z^2 - h z - 1)

"same letters, non-ascending order, cross term" is exactly "the bond multiset
does not determine a word". They also prove the complement — a MONOTONE word
always factorizes — which is the `qou-m3sh` chain form and the control here.

Complementary, not duplicated. Theirs: the exact `n = 4` cross term. Ours: the
link-level consequence (three distinct Jones polynomials, so different links),
the `A = 4` magnitude (15 % of helium-4), and the reconciliation of the corpus's
two published `A = 3` numbers. The cross term is `-0.4612` at `q_0` — negative,
agreeing in sign with `c_3 = -0.34`, though a different word, so the two are not
the same quantity.

**This strengthens the bean's blocked verdict rather than unblocking it.** Two
independent routes now say the all-pairs word's trace depends on ordering. The
open item is still a modelling decision, not a computation.

## RETIRED (owner decision B3, 2026-09-05)

The all-pairs bond model is retired as **ill-posed**, not parked as blocked. The
deciding argument is new and it removes the option that looked cheapest.

### Why "declare a canonical ordering" has no candidate

The sibling arc proves that **monotone** words — ascending, one run per
generator — always factorise
(`docs/audits/2026-09-04-monotone-word-trace-factorizes-derived-link-map.md`).
That is the only ordering class with a factorisation theorem, so it is the only
principled place to declare a convention. But the band generator's own sequence
is

    band(0,2) = [5, 4, 3, 2, 3, 4, 5]

with generators 3, 4 and 5 each appearing **twice, in two separate runs, inside
a single bond**. No reordering of the bonds can merge them, because they belong
to one bond. **The all-pairs word can never be monotone.**

So the principled ordering class is unreachable, and where it IS reachable the
word is the chain — which `qou-m3sh` proved is a connected sum carrying no
many-body binding at all. **The principled choice and the wanted answer exclude
each other.**

### What that means

The ambiguity is not a technicality standing between us and the cumulants. It
is the model telling us that a set of pairwise bonds applied *simultaneously* is
not a braid word, so "the all-pairs closure" does not name an algebra element,
and the cumulants measured from it were artifacts of a non-canonical choice —
33 distinct values across 40 sampled orderings at `A = 4`, spanning 15 % of
helium-4's binding.

### What is retired, and what is not

**Retired:** the all-pairs bond model as a source of many-body binding; the
`c_3 = -0.34` cumulants read off it; the search for "which prime closure carries
the cumulants", which presupposed a closure exists.

**Kept, all independent of this:** the chain closure and its connected-sum
theorem (`qou-m3sh`); the affine interface law and its closed forms
(`QOU.Mass.ChainTraceFactor`, sorry-free); the Fary-Milnor curvature floor
`2 pi (2A+1)` and the Frenet-framing jump; and this bean's own measurements,
which stand as a correct statement about braid words rather than about binding
— three distinct Jones polynomials from one bond multiset is a fact whatever
one thinks of the model.

**Not claimed:** that no algebraic home exists for simultaneous pairwise
bonding. Only that the braid-word presentation is not it, and nobody has a
candidate. If someone finds one, this reopens as a new bean rather than this
one.

## Summary of Changes

Investigated fully and retired on the evidence:

- `the_all_pairs_closure_is_not_one_link_probe` (13/13): six bond orderings give
  three distinct Markov traces and three distinct Jones polynomials at identical
  letter multiset, exponent sum and strand count; a second, independent
  arrangement ambiguity (`ppn` vs `pnp`, worth 0.0699 in `L`); the corpus's two
  published `A = 3` numbers reconciled as two different conventions; and the
  `A = 4` spread of 0.9924 in `L` = 4.15 MeV = 14.7 % of `B_AME(4He)`.
- Convergence with the sibling arc's `content_reorder_defect`, which supplies
  the exact `n = 4` cross term `z(z^2 - hz - 1)` this bean only measured.
- The monotone argument above, which is what turns "blocked" into "retired".
