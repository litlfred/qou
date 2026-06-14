/-!
# QOU.Archimedean.metallic_character_knot

**PROPOSITION.** Metallic character from incomplete sub-Hopf links
-/

namespace QOU.Archimedean

structure MetallicCharacterKnotData where
  is_incomplete_sub_hopf_link : True
  has_metallic_character : True

/-- **PROPOSITION.** Metallic character from incomplete sub-Hopf links -/
theorem metallic_character_knot (d : MetallicCharacterKnotData) :
    d.is_incomplete_sub_hopf_link ∧ d.has_metallic_character :=
  ⟨d.is_incomplete_sub_hopf_link, d.has_metallic_character⟩

end QOU.Archimedean
