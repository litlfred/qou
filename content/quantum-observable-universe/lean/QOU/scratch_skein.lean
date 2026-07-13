import Mathlib.Algebra.Algebra.Basic
import Mathlib.RingTheory.Adjoin.Basic
import Mathlib.Data.Set.Basic

open Set

/-!
# QOU.Torsion.skein_generation
-/

namespace QOU.Torsion

class SkeinGenerationContext (R Skein FundamentalKnotIndex : Type*)
    [CommRing R] [Ring Skein] [Algebra R Skein] where
  fundamentalKnot : FundamentalKnotIndex → Skein
  hopfLink : Skein
  Hadron : Skein → Prop
  hadron_is_polynomial : ∀ (h : Skein), Hadron h →
    h ∈ Algebra.adjoin R (range fundamentalKnot ∪ {hopfLink})

theorem skein_generation {R Skein FundamentalKnotIndex : Type*}
    [CommRing R] [Ring Skein] [Algebra R Skein]
    [ctx : SkeinGenerationContext R Skein FundamentalKnotIndex]
    (h : Skein) (h_hadron : ctx.Hadron h) :
    h ∈ Algebra.adjoin R (range ctx.fundamentalKnot ∪ {ctx.hopfLink}) :=
  ctx.hadron_is_polynomial h h_hadron

end QOU.Torsion

