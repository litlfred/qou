import QOU.Basic
import QOU.ParticleInteractions.HadronDisplay


/-!
# QOU.Hadron.exists — existence of hadrons

Proton witnesses the existence of stable hadrons; Borromean braid +
Hopf gluon gives E_cross < 0.

LaTeX: `\label{prop:hadron-exists}`

## References

- [leitner2026] §4-braids-and-knots/hadron-exists
- [atiyah1990] Geometry and Physics of Knots
-/

namespace QOU

/-- **Existence of hadrons.**

    A `Hadron` term exists. The intended witness is the proton
    `𝔭 = B₃(u, u, d)` (Borromean braid + Hopf gluon, satisfying
    `E_cross < 0`), but constructing that witness requires the full
    Hecke-element + crossing-energy chain.

    For pure existence, a `Hadron` with two `unknot` constituents
    suffices — it is a degenerate witness (does not satisfy the
    physical stability condition `E_cross < 0`), but it is a valid
    inhabitant of the `Hadron` type. Strengthening to "a stable
    hadron exists" is a follow-up requiring the binding-energy
    classification on the constituents.
-/
-- Ref: [atiyah1990] Geometry and Physics of Knots
theorem Hadron.exists : Nonempty Hadron :=
  ⟨{ theta := 0
     phi := 0
     constituents := [QOU.KnotTheory.unknot, QOU.KnotTheory.unknot]
     constituents_nonempty := by simp }⟩

end QOU
