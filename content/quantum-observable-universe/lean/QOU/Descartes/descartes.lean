/-!
# QOU.Descartes.descartes — Bring's surface is terminal in `𝐂_{−6}`

**Proposition** ([`prop:descartes`](../../../quantum-observable-universe/descartes-universe/descartes.md)).

*Let `𝐂_{−6}` denote the category of quantum observable universes
over `R` satisfying the Descartes condition `χ(A) = −6`, with
morphisms given by QOU maps that preserve the Euler characteristic.
Then Bring's surface `Σ₄` is a terminal object in `𝐂_{−6}`: for
every Descartes universe `(𝐂, A, τ)` in `𝐂_{−6}`, there exists a
**unique** morphism to the Bring's QOU.*

The Lean encoding records the universal-property statement: for
every object `X` in `𝐂_{−6}`, the hom-set `Hom(X, Bring's-QOU)` is
a singleton.

-- Ref: [manuscript] quantum-observable-universe/descartes-universe/descartes.md
-/

namespace QOU.Descartes

/-- Abstract context for the `Bring's-Σ₄ is terminal in 𝐂_{−6}` claim. -/
class DescartesTerminalContext where
  /-- Objects of `𝐂_{−6}` (Descartes universes). -/
  DescUniverse : Type
  /-- Morphisms between Descartes universes (Euler-char preserving). -/
  Mor : DescUniverse → DescUniverse → Type
  /-- The terminal object: Bring's quantum-observable-universe. -/
  BringQOU : DescUniverse

/-- **Bring's `Σ₄` is terminal in `𝐂_{−6}`** ([`prop:descartes`]).

    For every Descartes universe `X`, the hom-set `Mor X BringQOU` is
    a singleton (`Unique`). -/
-- Ref: [manuscript] quantum-observable-universe/descartes-universe/descartes.md
theorem descartes
    [ctx : DescartesTerminalContext] (X : ctx.DescUniverse) :
    Nonempty (Unique (ctx.Mor X ctx.BringQOU)) := by
  -- Manuscript proof: existence is by the Bring's QOU's
  -- Euler-characteristic-preserving structure functor; uniqueness
  -- follows from the rigidity of the fibre-functor identification
  -- under the Descartes condition χ(A) = −6.
  -- Ref: [manuscript] quantum-observable-universe/descartes-universe/descartes.md
  sorry

end QOU.Descartes
