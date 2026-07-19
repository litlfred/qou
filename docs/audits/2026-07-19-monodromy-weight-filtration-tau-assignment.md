# The monodromy weight filtration + the typed τ-assignment obligation (2026-07-19)

**Bean:** `qou-tasg`. **Lean:** [`QOU/Machinery/HeckeMonodromyWeightFiltration.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeMonodromyWeightFiltration.lean)
— sorry-free, `lean`-direct exit 0.

## The assignment-map brick (`TauRhoHodgeLift` wall, target B)

- **`channel_vectors_collide_at_monodromy`** — at `q = i` the e₊ and e₋
  channel VECTORS (not merely their eigenvalues, #4090) coincide — both
  equal the nilpotent `N v = σv − i·v`. The channel pair collapses onto
  the Jordan weight filtration at the degenerate locus: the precise
  domain datum of `F(channel pair at the degenerate locus) =
  (H^{1,0}, H^{0,1})`.
- **`monodromyN_star`** — conjugation carries the `i`-Jordan nilpotent to
  the `(−i)`-Jordan nilpotent `N̄`: ρ exchanges the two Jordan
  structures — the algebraic twin of T3's deck exchange, now at the
  filtration level.
- **`jordan_sq_zero_bar`** — `N̄² = 0`, DERIVED from the merged
  `jordan_sq_zero` by conjugation transport (not re-proved).
- **`TauAssignmentData`** — the typed assignment obligation: a linear map
  to the `H^{1,0}` model that kills the nilpotent (factors through the
  semisimple quotient — the local-to-global monodromy step), a ρ-partner,
  and the intertwining law. Content-bearing; **no instance declared** —
  inhabiting it with functorial provenance IS the remaining module-side
  wall content. Derived, never restated (§3b-cond rule 5):
  **`bar_kills_nilpotent`** — the partner automatically kills the
  conjugate nilpotent, from the fields plus the exchange.

## Wall state after targets A + B

```
A: general-rank braid/far-comm  ⟸ coset data ⟸ RightExchangeProp (#4091)
   — one textbook theorem (BB 1.4.3) remains; algebra layer complete
B: TauRhoHodgeLift  ⟸ inhabit TauAssignmentData with provenance
   — domain pinned (Jordan #4090, collapse + ρ-filtration exchange: this)
```

Honesty: no instance declared; the derived lemma certifies field
non-degeneracy; nothing wired; `1/(8π)` stays phase-4.
