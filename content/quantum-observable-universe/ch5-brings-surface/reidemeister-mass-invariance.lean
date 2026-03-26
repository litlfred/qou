-- Ref: [manuscript] Ch. 6, §3
-- The topological mass formula is a knot invariant (R-I, R-II, R-III).
-- The binding energy is an embedding invariant (R-II, R-III but not R-I).
-- Shell transitions are R-I moves on the embedding.

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
sorry

noncomputable section

/-- Reidemeister move type -/
inductive ReidemeisterMove
  | R1 : ReidemeisterMove  -- curl (writhe ±1)
  | R2 : ReidemeisterMove  -- poke (two opposite crossings)
  | R3 : ReidemeisterMove  -- slide (strand past crossing)

/-- Bare mass is invariant under all Reidemeister moves -/
theorem bare_mass_invariant (K : sorry) (r : ReidemeisterMove) :
    sorry := sorry

/-- Binding energy is invariant under R-II and R-III only -/
theorem binding_energy_R2_invariant (L : sorry) :
    sorry := sorry

theorem binding_energy_R3_invariant (L : sorry) :
    sorry := sorry

/-- Shell transition = R-I move that changes binding energy -/
theorem shell_transition_is_R1 (n : ℕ) :
    sorry := sorry

end
