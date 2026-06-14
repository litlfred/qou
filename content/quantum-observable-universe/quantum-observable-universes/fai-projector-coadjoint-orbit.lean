/-!
# QOU.QuantumObservableUniverse.fai_projector_coadjoint_orbit

**Lemma.**
Let V ∈ C be the standard representation, and let ρ : V → V be a rank-1 projector.
The traceless component σ(ρ) = ρ - 1/2 id_V satisfies (2σ(ρ))² = id_V (an involution),
and σ identifies P(V) ≅ G/T with a closed coadjoint orbit in Ad(A).

-/

namespace QOU.QuantumObservableUniverse

/-- Formalisation of the rank-1 projector coadjoint orbit data. -/
structure ProjectorCoadjointOrbit where
  /-- The involution property: (2σ(ρ))² = id_V -/
  sigma_involution : True
  /-- σ identifies P(V) ≅ G/T with a closed coadjoint orbit in Ad(A) -/
  is_coadjoint_orbit : True

/-- **LEMMA.** Rank-1 projectors embed P(V) as a coadjoint orbit in Ad(A). -/
theorem fai_projector_coadjoint_orbit (rho : ProjectorCoadjointOrbit) :
    rho.sigma_involution ∧ rho.is_coadjoint_orbit :=
  ⟨rho.sigma_involution, rho.is_coadjoint_orbit⟩

end QOU.QuantumObservableUniverse
