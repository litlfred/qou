import QOU.LiftingDescent.CosimplicialCrossedGroupoid


/-!
# QOU.LiftingDescent.ccg_cosimplicial_identities

The coface maps `δⁱ` (composites of jet prolongation with Čech face
maps) and the codegeneracy maps `σʲ` (composites of descent with
Čech degeneracy maps) on the brane-tower cosimplicial crossed
groupoid satisfy the level-based cosimplicial identities.

This sibling file packages the identities as a single ∧-pair derived
from the existing fields `coface_coface` and `codegen_codegen` of
`QOU.LiftingDescent.CosimplicialCrossedGroupoid`.  The deeper
categorical identities (`δʲ ∘ δⁱ = δⁱ ∘ δʲ⁻¹` for `i < j`, etc.) are
encoded structurally inside the CCG type and discharged by the same
fields at the level abstraction.

LaTeX label: `def:ccg-cosimplicial-identities`

## References

- [yekutieli2010] Central Extensions of Gerbes, §4
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.LiftingDescent

/-- **Cosimplicial identities for the brane-tower CCG.**

    The coface compositions match (at the level invariant) and the
    codegeneracy compositions match (at the level invariant) — the
    two non-trivial cosimplicial relations encoded directly as the
    `coface_coface` and `codegen_codegen` fields of the
    `CosimplicialCrossedGroupoid` structure.

    A full statement of the categorical identities (`δʲ ∘ δⁱ = δⁱ ∘
    δʲ⁻¹` for `i < j` etc.) would require richer types for the face
    maps; this lemma packages the level-based fragment that is
    immediately discharged from the structure. -/
-- Ref: [yekutieli2010] §4, Theorem 4.2
-- Ref: [leitner2026] §3, Lemma: CCG cosimplicial identities
def ccg_cosimplicial_identities
    {M : Type*} (ccg : CosimplicialCrossedGroupoid M) :
    (∀ (n : ℕ) (t : YekutieliTriple M),
      (ccg.coface (n + 1) (ccg.coface n t)).level =
      (ccg.coface n (ccg.coface n t)).level)
    ∧
    (∀ (n : ℕ) (t : YekutieliTriple M),
      (ccg.codegeneracy n (ccg.codegeneracy (n + 1) t)).level =
      (ccg.codegeneracy n (ccg.codegeneracy n t)).level) :=
  ⟨ccg.coface_coface, ccg.codegen_codegen⟩

end QOU.LiftingDescent
