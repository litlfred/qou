---
# qou-gmfz
title: 'Kazhdan-Lusztig classical limit: the KL-basis identification and monoidality are still unstated'
status: todo
type: task
priority: normal
created_at: 2026-08-24T19:39:51Z
updated_at: 2026-08-24T19:39:51Z
---

`QOU/BraidKnot/KazhdanLusztigClassicalLimit.lean`. Follow-up to the repair
landed 2026-08-24 on `claude/mt7r-archimedean-eval-2026-08-24`; this bean is the
**remainder**, and the file's own docstring already names it.

## What was repaired (do not redo)

- `statSign` retyped from `Z` to the ground ring `R`, so a root of unity can
  live there and the collapse can fail;
- the sibling axiom `statSign_pm_one : forall b, statSign b = 1 \/ statSign b = -1`
  **deleted** — it axiomatised the very collapse the conjecture claims, making
  `kl_compatible_with_tau` derivable in every model;
- `kl_compatible_with_tau` guarded by `q = 1`, so it asserts nothing away from
  the classical point;
- `canonical` demoted `instance` -> `def` (it was `KLBasisElt := PUnit`,
  `statSign _ := 1`, discharging by `Or.inl rfl` — and its docstring had claimed
  it "carries the conjecture as a sorry", which was false; no `sorry` existed).

## What is still owed

The module docstring states the conjecture as three claims:

> as `q -> 1`, the KLR canonical basis `{b_w}` of `H_n(R,q)` **flattens to the
> Kazhdan-Lusztig basis** `{C_w}` of `Z[S_n]`, and the resulting classical-limit
> functor **is monoidal** and **compatible with the observation functor tau**.

The class states one of them, weakly:

```
class KazhdanLusztigClassicalLimit (R) [CommRing R] (q : R) [H : ...] [C : ...] where
  KLBasisElt : Type u                       -- an ARBITRARY type
  klMap : H.NormalForm -> KLBasisElt        -- an ARBITRARY function
  statSign : KLBasisElt -> R
  kl_compatible_with_tau : q = 1 -> forall T, statSign (klMap T) = 1 \/ statSign (klMap T) = -1
```

- **The KL basis is not there.** `KLBasisElt` is an opaque type with no
  Kazhdan-Lusztig structure — no Hecke algebra of `S_n`, no bar involution, no
  KL polynomials, no defining property. So "flattens to the KL basis" is not
  stated; any type at all satisfies the signature.
- **Monoidality is not there.** No tensor structure on either side, no
  comparison morphism, nothing to be monoidal about.
- **`tau` is not there.** The field is *named* `kl_compatible_with_tau` and
  `tau` appears nowhere in the class. What the field says is that a phase is
  `+-1` at `q = 1`. That is a consequence one might want *from* tau-compatibility,
  not tau-compatibility.

## What it costs

Both missing claims need `tau` and the KL basis as **independent data** — the
whole point being that `klMap`'s target is not free to be chosen. Concretely:

1. a `KLBasis` structure over `Z[S_n]` carrying the bar involution and the
   defining self-duality, so `KLBasisElt` can be *required* to be it rather than
   permitted to be anything;
2. `tau` as a field (the observation functor already exists upstream in
   `HeckeAnyonicSubstrate` / `CrystalGraphRealization` — check before
   re-declaring), and `kl_compatible_with_tau` restated as a square that
   commutes, with the `+-1` statement demoted to a corollary;
3. monoidal structure on the source and target and a `klMap`-is-monoidal field.

(1) is the useful one and is independently valuable — nothing else in the corpus
has a Kazhdan-Lusztig basis. (3) is the largest and the least load-bearing for
anything downstream today.

## State

`statSign_klMap_pm_one` and `statSign_sq_eq_one` are the only consumers, both in
this file, both now correctly conditional on `q = 1`. No instance exists outside
`canonical` (a `def`). Nothing breaks while this is open; the risk is only that
the module docstring keeps promising three things the Lean states one of.
Consider trimming that docstring in the same change so the gap is visible from
the top of the file, not just from this bean.
