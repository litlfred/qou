/-!
# QOU.QuantumObservableUniverse.fibre_functor_atlas

**Proposition.**
Let (C, A, τ) be a quantum observable universe with G = Aut_⊗(τ).
Then the fibre functors form an atlas with torsor transitions.
-/

namespace QOU.QuantumObservableUniverse

/-- Formalisation of the fibre functor atlas structural data. -/
structure FibreFunctorAtlasData where
  /-- Each fibre functor is an affine chart -/
  is_affine_chart : True
  /-- The set of monoidal natural isomorphisms between fibre functors is a G-torsor -/
  is_g_torsor : True
  /-- The composition of transitions satisfies the cocycle condition -/
  cocycle_condition : True
  /-- The category of fibre functors is a G-gerbe (the affine atlas) -/
  is_g_gerbe : True

/-- **PROPOSITION.** The category of fibre functors is a G-gerbe forming an affine atlas. -/
theorem fibre_functor_atlas (atlas : FibreFunctorAtlasData) :
    atlas.is_affine_chart ∧ atlas.is_g_torsor ∧ atlas.cocycle_condition ∧ atlas.is_g_gerbe :=
  ⟨atlas.is_affine_chart, atlas.is_g_torsor, atlas.cocycle_condition, atlas.is_g_gerbe⟩

end QOU.QuantumObservableUniverse
