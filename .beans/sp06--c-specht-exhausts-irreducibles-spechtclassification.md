
## Assessment 2026-08-08 — NOT closed, and here is exactly why

Attempted after closing `spechtIso_imp_dom_both` (qou-6gwx). The cross-shape
machinery does **not** reach this, and I want the reason on record so the next
session does not re-derive the dead end.

### What was delivered instead

`SpechtClassification.dom_of_nonzero_hom` — Sagan Thm 2.4.4 in its general
**hom** form, sorry-free and axiom-clean:

    Hom_{k[S_n]}(S^μ, M^ν) ∋ θ ≠ 0  ⟹  μ ⊵ ν

The previously proved `dom_of_intertwiner` (iso form) is now a corollary: it is
the case `θ = (S^ν ↪ M^ν) ∘ e`. Extracting a surviving polytabloid from `θ ≠ 0`
is a span-induction over `SpechtSubmodule = span (range polytabloid)`.

This is the strongest form of the dominance bound and is what any route to
exhaustion will consume. It is not, by itself, enough.

### The dead end, precisely

`W` simple ⇒ a quotient of the regular module ⇒ (Maschke, char 0) a submodule
of it ⇒ `W ↪ M^{(1ⁿ)}`. Pick `ν` extremal in dominance with `W ↪ M^ν` and apply
`specht_submodule_dichotomy`:

* `S^ν ≤ W` ⇒ `W = S^ν` by simplicity. **Done.**
* `W ≤ (S^ν)ᗮ` ⇒ stuck.

Excluding the second branch needs to know **where the composition factors of
`(S^ν)ᗮ` live** — Young's rule. `dom_of_nonzero_hom` bounds such a factor by
dominance but does not assert one exists, so extremality has nothing to
contradict. Adding a hypothesis to dodge this is assuming the theorem.

### The two honest routes

**(a) Counting** — recommended. `#simples = dim_k Z(k[S_n]) = #conj classes =
#partitions`, then pigeonhole against the `#partitions` pairwise
non-isomorphic Specht modules (`specht_pairwise_noniso`, proved). Three Mathlib
gaps, all checked absent at the pinned revision:

1. `dim_k Z(k[G]) = #conj classes` — class sums are a basis of the centre. No
   centre-of-group-algebra API in Mathlib. ~150–250 lines.
2. `ConjClasses (Perm (Fin n)) ≃ Nat.Partition n` — Mathlib has
   `Equiv.Perm.partition` and `partition_eq_of_isConj`, but not the induced
   bijection, and not surjectivity of `partition`. The cheapest of the three.
3. `#{iso-classes of simple modules} = #Wedderburn blocks ≤ dim_k Z(A)` for
   semisimple `A`. `WedderburnSn.sn_wedderburnArtin` gives the decomposition
   with an **abstract** block count `N`; identifying `N` is the gap. Mathlib's
   `RingTheory/SimpleModule/Isotypic.lean` is the nearest API.

**(b) Young's rule / Specht filtration** of `M^ν`. Larger, and subsumes far
more than is needed.

### Sizing

Route (a) is 2–3 focused sessions and produces three reusable Mathlib-gap
modules. It is not a "finish the file" task. The docstring at the `sorry` site
now carries this analysis so it is not mistaken for a small remaining step.

### Do not

- Do not weaken the statement (e.g. by assuming `W` embeds in some `M^ν` with a
  dominance hypothesis) — that assumes the conclusion.
- Do not try to route it through `dom_of_nonzero_hom` alone; the branch above is
  where it fails.
