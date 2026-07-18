# α_EM B2 lift — the τ-functor target specification (2026-07-18)

**Bean:** `qou-tq20`, tranche 8 — the categorical scaffold closing today's
arc, after the numerical program closed
([#4030](https://github.com/litlfred/qou/pull/4030): "irreducibly
categorical").

**Lean (this PR):** [`QOU/Archimedean/TauFunctorTargetSpec.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/TauFunctorTargetSpec.lean)
— sorry-free, `lean`-direct exit 0 with Mathlib.

**Scope guard (STRICT):** nothing asserts the functor exists; the trivial
inhabitant is a labeled *non-sufficiency* demonstration, never progress on
the wall; nothing wired; `1/(8π)` stays phase-4.

## What the module proves

1. **`ArchimedeanTauRealization g w`** — the typed interface the measure
   derivation needs: a loop-weight operator on `H^{1,0} ⊕ H^{0,1}`, real
   (swap-conjugation-commuting), self-adjoint, with `H^{1,0}`-block trace
   `w`.
2. **`discharge`** — any realization yields the `TauRhoHodgeLift` instance
   via the #3999 constructor; **`discharge_equal_split`** — its conjugate
   block carries the same weight (the ½ of `½·a₀`, end to end). So:
   *inhabiting this type with functorial provenance for `w` closes the
   wall.*
3. **`interface_alone_is_trivially_inhabitable`** — machine-checked: a bare
   diagonal matrix satisfies every interface field for any real prescribed
   weight. **This formalizes the tranche-7 verdict**: the wall is not the
   interface, the numerics, or the reality structure (all free/trivial) —
   it is *exclusively* the functorial provenance.

## The target, precisely (what a future session must construct)

The archimedean τ-functor `F` from the framework's braided category, with:

- `F(e₊/e₋ channel pair at the degenerate locus) = (H^{1,0}, H^{0,1})` —
  shadow FORCED (#3960), ℂ-model in place (#3992);
- `F ∘ ρ = Hodge conjugation ∘ F` — the B1 dictionary (#3955), type-exact;
- `F(canonical Markov weight) =` the loop weight's `H^{1,0}`-block — the
  Reality-realization premise (#3999);
- naturality in the categorical data — the part no interface field can
  encode without the category itself (Mathlib `CategoryTheory` reachable
  via the lake-cache restore, #3985).

Constructing `F` and evaluating it into `ArchimedeanTauRealization` is,
by `discharge`, the *entire* remaining content of the α_EM per-loop wall.
