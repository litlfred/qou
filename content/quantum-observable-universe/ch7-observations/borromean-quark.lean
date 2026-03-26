-- Ref: [manuscript] Ch. 6, §3
-- Borromean quark conjecture: quarks as Borromean-linked unknots.
-- The Borromean link B_3 has the property that no two components
-- are linked, but all three together are inseparable.
-- Vol(S³ \ B_3) = 7.32772...

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
sorry

noncomputable section

/-- The Borromean link of three unknots in color tubes. -/
structure BorromeanBaryon where
  /-- The three color tube assignments -/
  color : Fin 3 → Fin 3
  /-- Crossing orientation: +1 (up) or -1 (down) for each component -/
  orientation : Fin 3 → Int
  /-- The orientations sum to the net Coulomb charge -/
  charge_sum : (Finset.univ.sum orientation) = orientation 0 + orientation 1 + orientation 2

/-- The proton: two up (+1) and one down (-1), net charge +1 -/
def proton_partition : BorromeanBaryon := sorry

/-- The neutron: one up (+1) and two down (-1), net charge 0 -/
def neutron_partition : BorromeanBaryon := sorry

/-- Hyperbolic volume of the Borromean complement -/
def borromean_volume : ℝ := 7.32772

/-- The baryon mass from the topological mass formula -/
def baryon_mass (q : ℝ) (hq : q > 1) : ℝ :=
  borromean_volume / (1 - 1/q)^2

end
