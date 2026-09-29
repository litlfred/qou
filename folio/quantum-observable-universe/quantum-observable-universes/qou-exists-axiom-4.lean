import QOU.QuantumObservableUniverse.CategoricalFoundations


/-!
# QOU.QuantumObservableUniverse.exists_axiom_4_volume

Axiom 4 of a quantum observable universe (categorical volume
constraint via the quantum determinant): the fundamental object
`V` of categorical dimension 2 admits a non-degenerate epimorphism
`ε : Λ²V → 𝟙` preserved by the rigid dualities, which forces
`det(g_V) = 1` for all `g ∈ Aut⊗(ω)` — i.e., restricts the gauge
group from `GL(2)` to `SL(2)`.

The Lake module
[`lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean`](../../lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean)
encodes this as the `volumeIso` field of the
`QuantumObservableUniverse R` structure.  This sibling extracts
that field as the named lemma matching the URI's expected decl.

**Changed 2026-08-22 (bean `qou-n1dj`, iso reading).**  The field was
`volumeForm : exteriorSquare ⟶ (𝟙_ C)`, a bare morphism, and this file's
`exists_axiom_4_volume` proved `Nonempty (Q.exteriorSquare ⟶ (𝟙_ Q.C))` by
exhibiting it.  That was worth nothing: `Preadditive C` is in scope, so the
zero morphism inhabits the Hom-set and the "satisfiability" proof would have
gone through for a QOU with no volume form at all.  With the field now an
isomorphism the lemma states the property the manuscript actually claims —
that `ε` is an epimorphism — and it is no longer satisfied by `0`.

LaTeX label: `lem:qou-exists-axiom-4`

## References

- [manuscript] §1 Quantum Observable Universe, Axiom 4
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.QuantumObservableUniverse

-- Pre-existing: both declarations below write `QuantumObservableUniverse.{u, v}`
-- with no `universe` command in scope, so under the build's `autoImplicit=false`
-- this file failed with two `unknown universe level 'v'` errors and had done for
-- as long as it has existed.  Nothing caught it: co-located `.lean` siblings are
-- outside the `globs = ["QOU", "QOU.+"]` of `lean/lakefile.toml`, so `lake build`
-- never sees them, and they have no `.qa.json` compile gate either.
universe u v

/-- **Axiom 4 — categorical volume constraint.**

    Any `QuantumObservableUniverse R` carries the `volumeIso`
    field — an isomorphism `Λ²V ≅ 𝟙` realising the non-degenerate
    epimorphism that pins the categorical determinant.  This is
    the categorical formulation of the `SL(2)` gauge restriction. -/
-- Ref: [manuscript] §1 Quantum Observable Universe, Axiom 4
-- NOTE: `def`, not `theorem` — a Hom-set `Q.exteriorSquare ⟶ (𝟙_ Q.C)`
-- is a `Type _` (morphisms are data, not propositions).  Per Copilot
-- review on PR #794.
def exists_axiom_4_volume_data
    {R : Type*} [CommRing R] (Q : QOU.QuantumObservableUniverse.{u, v} R) :
    letI := Q.catInst
    letI := Q.monInst
    Q.exteriorSquare ⟶ (𝟙_ Q.C) :=
  letI := Q.catInst
  letI := Q.monInst
  Q.volumeIso.hom

/-- **The volume form is an epimorphism** — the "non-degenerate epimorphism"
    of the manuscript's Axiom 4, now stated rather than merely named.

    This replaces `Nonempty (Q.exteriorSquare ⟶ (𝟙_ Q.C))`, which was true of
    every QOU for the wrong reason: the Hom-set contains `0`. -/
lemma exists_axiom_4_volume
    {R : Type*} [CommRing R] (Q : QOU.QuantumObservableUniverse.{u, v} R) :
    letI := Q.catInst
    letI := Q.monInst
    CategoryTheory.Epi (exists_axiom_4_volume_data Q) := by
  letI := Q.catInst
  letI := Q.monInst
  show CategoryTheory.Epi Q.volumeIso.hom
  exact QOU.epi_of_iso_unit Q.volumeIso

end QOU.QuantumObservableUniverse
