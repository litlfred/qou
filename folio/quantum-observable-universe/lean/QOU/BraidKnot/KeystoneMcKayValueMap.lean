import QOU.BraidKnot.KeystoneStandardRepQDim

/-!
# Keystone — the McKay value-map q-dimension identities for the `n = 5` W_λ blocks

The geometric `W_λ` derivation (audit `2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md`,
merged #3685) derives the colour→partition-λ value map via the McKay correspondence
`2I ↔ affine Ê₈` (irrep dims = Coxeter marks) composed with `A₅ ⊂ S₅` branching: the value on each
of the four `bwS0` conjugation classes is `d_q(λ) = [mark]_q`, the `q`-integer of the McKay node's
Coxeter mark. This file **proves the two new members** of that value map (the third, `d_q(4,1)=[4]_q`,
is the standard-representation theorem `qFactorial_standard_hook` of
[`KeystoneStandardRepQDim.lean`](KeystoneStandardRepQDim.lean), #3640):

> * `d_q((3,2)) = [5]_q` — the **mark-5** node (the muon block).
> * `[2]_q · d_q((3,1,1)) = [3]_q · [4]_q` — the **A₅-split** mark-6 electron node
>   (`d_q((3,1,1)) = [3]_q[4]_q/[2]_q`, *not* `[6]_q`; the deviation from `[mark]_q` is the `3⊕3′`
>   split signature).

Both are **convention-independent** pure `q`-factorial hook cancellations (they hold for the corpus
unbalanced `qIntGeo q k = ∑_{i<k} qⁱ` used here, and equally for the balanced convention): the compute
witness records the additional *balanced-only* reading `[3]_q[4]_q/[2]_q = [5]_q + 1`, which is a
separate normalization fact and is **not** formalized here (only the fundamental hook identities are).

## Multiplicative (division-free) form

Matching the `shape_*` / `qFactorial_standard_hook` convention (avoids nonvanishing hypotheses):

* **(3,2)** has hooks `{4,3,1,2,1}`, product `[4]_q·[3]_q·[1]_q·[2]_q·[1]_q = [4]_q!` (as `[1]_q=1`),
  so `[5]_q! = [5]_q · (hook product)`, i.e. `d_q(3,2) = [5]_q!/∏hooks = [5]_q`.
* **(3,1,1)** has hooks `{5,2,1,2,1}`, product `[5]_q·[2]_q·[1]_q·[2]_q·[1]_q`, so
  `[2]_q · [5]_q! = [3]_q · [4]_q · (hook product)`, i.e. `[2]_q · d_q(3,1,1) = [3]_q·[4]_q`.

Each reduces to the `q`-factorial recursion `[n+1]_q! = [n]_q!·[n+1]_q` (`qFactorial_succ`) applied
repeatedly, `[1]_q = 1` (`qIntGeo_one'`), and commutativity (`ring`). Base ring: generic `[Field R]`
(no archimedean construct — §7c). No fit; pure `q`-combinatorics.

-- Ref: [leitner2026] docs/audits/2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md
-- Ref: [macdonald1995] Symmetric Functions and Hall Polynomials, I.3 (q-hook-length formula)
-/

namespace QOU.BraidKnot.Keystone

-- `qIntGeo`, not `qInt`: this file's `qInt` came from
-- `wedderburn_trace_identity` via `KeystoneStandardRepQDim`, which is the
-- GEOMETRIC convention. Renamed in #6257 (bean `qou-qint`) so the
-- convention is in the name; the q-hook-length formula below is geometric.
open QOU.BraidKnot (qIntGeo qFactorial)

variable {R : Type*} [Field R]

/-- **Value map, mark-5 node (muon block `(3,2)`): `d_q(3,2) = [5]_q`** (multiplicative,
division-free). Hooks of `(3,2)` are `{4,3,1,2,1}`, so

  `[5]_q!  =  [5]_q · ([4]_q · [3]_q · [1]_q · [2]_q · [1]_q)`,

the parenthesized factor being the hook-length product; equivalently `d_q(3,2) = [5]_q!/∏hooks
= [5]_q`. Proved from `[5]_q! = [5]_q·[4]_q!` and `[4]_q! = [4]_q·[3]_q·[2]_q·[1]_q` (`qFactorial_succ`
recursion), `[1]_q = 1`, and `ring`. This is the **new exact identity** of the McKay value map
(#3685): the muon block value is the `q`-integer of its McKay Coxeter mark `5`. -/
theorem qFactorial_shape_32 (q : R) :
    qFactorial q 5
      = qIntGeo q 5 * (qIntGeo q 4 * qIntGeo q 3 * qIntGeo q 1 * qIntGeo q 2 * qIntGeo q 1) := by
  simp only [qFactorial, Finset.prod_range_succ, Finset.prod_range_zero, Nat.reduceAdd,
    qIntGeo_one']
  ring

/-- **Value map, A₅-split mark-6 node (electron block `(3,1,1)`): `[2]_q · d_q(3,1,1) = [3]_q·[4]_q`**
(multiplicative, division-free). Hooks of the self-conjugate `(3,1,1)` are `{5,2,1,2,1}`, so

  `[2]_q · [5]_q!  =  [3]_q · [4]_q · ([5]_q · [2]_q · [1]_q · [2]_q · [1]_q)`,

the last factor being the hook-length product; equivalently `d_q(3,1,1) = [5]_q!/∏hooks
= [3]_q·[4]_q/[2]_q`. This is **not** `[6]_q`: the electron block is the McKay node where the
`A₅` irrep `3⊕3′` (dim 6) splits, and the deviation of `d_q` from `[mark]_q = [6]_q` is exactly this
split. Proved from the `qFactorial_succ` recursion, `[1]_q = 1`, and `ring`. -/
theorem qFactorial_shape_311 (q : R) :
    qIntGeo q 2 * qFactorial q 5
      = qIntGeo q 3 * qIntGeo q 4
          * (qIntGeo q 5 * qIntGeo q 2 * qIntGeo q 1 * qIntGeo q 2 * qIntGeo q 1) := by
  simp only [qFactorial, Finset.prod_range_succ, Finset.prod_range_zero, Nat.reduceAdd,
    qIntGeo_one']
  ring

end QOU.BraidKnot.Keystone
