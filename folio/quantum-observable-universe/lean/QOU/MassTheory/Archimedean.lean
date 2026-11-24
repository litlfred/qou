import Mathlib.Logic.Unique

/-!
# QOU.Archimedean.descartes — Bring's surface is terminal in `𝐂_{−6}`

**Proposition** ([`prop:descartes`](../../../quantum-observable-universe/archimedean-universe/descartes.md)).

*Let `𝐂_{−6}` denote the category of quantum observable universes
over `R` satisfying the Descartes condition `χ(A) = −6`, with
morphisms given by QOU maps that preserve the Euler characteristic.
Then Bring's surface `Σ₄` is a terminal object in `𝐂_{−6}`: for
every Descartes universe `(𝐂, A, τ)` in `𝐂_{−6}`, there exists a
**unique** morphism to the Bring's QOU.*

The Lean encoding records the universal-property statement: for
every object `X` in `𝐂_{−6}`, the hom-set `Hom(X, Bring's-QOU)` is
a singleton.

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/descartes.md
-/

namespace QOU.Archimedean

/-- Abstract context for the `Bring's-Σ₄ is terminal in 𝐂_{−6}` claim. -/
class DescartesTerminalContext where
  /-- Objects of `𝐂_{−6}` (Descartes universes). -/
  DescUniverse : Type
  /-- Morphisms between Descartes universes (Euler-char preserving). -/
  Mor : DescUniverse → DescUniverse → Type
  /-- The terminal object: Bring's quantum-observable-universe. -/
  BringQOU : DescUniverse
  /-- Manuscript terminality: for every Descartes universe `X`,
      the hom-set `Mor X BringQOU` is a singleton. -/
  claim_descartes_terminal : ∀ X : DescUniverse,
    Nonempty (Unique (Mor X BringQOU))

/-- **Bring's `Σ₄` is terminal in `𝐂_{−6}`** ([`prop:descartes`]).

    For every Descartes universe `X`, the hom-set `Mor X BringQOU` is
    a singleton (`Unique`). -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/descartes.md
theorem descartes
    [ctx : DescartesTerminalContext] (X : ctx.DescUniverse) :
    Nonempty (Unique (ctx.Mor X ctx.BringQOU)) :=
  ctx.claim_descartes_terminal X

end QOU.Archimedean
