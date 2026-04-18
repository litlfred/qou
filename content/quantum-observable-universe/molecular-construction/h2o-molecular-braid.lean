-- Ref: [manuscript] Ch. 12, §h2o-molecular-braid
-- Water H₂O as a molecular braid in H₂₈(q)

/-- **Water H₂O** as a molecular braid with 28 strands.

    Two single O–H σ bonds share 2 electron pairs. Oxygen retains
    2 core electrons (1s²) and 2 lone pairs (4 non-bonding
    electrons in the 2s / 2p channels). The 2 lone pairs on O
    push the bonding pairs together, producing the bent
    ∠HOH ≈ 104.5° geometry (see `rem:h2o-bent-geometry`). -/
structure H2OBraid where
  /-- Total strand count = 28 (2·H + O = 2·2 + 24). -/
  totalStrands : Nat := 28
  /-- Number of bonds = 2 (two single O–H σ bonds). -/
  numBonds : Nat := 2
  /-- Bond order of each O–H bond = 1. -/
  bondOrderPerBond : Nat := 1
  /-- Total shared electrons = 4 (2 pairs). -/
  sharedElectrons : Nat := 4
  /-- Lone pairs on oxygen = 2 (4 non-bonding valence electrons). -/
  oxygenLonePairs : Nat := 2

/-- H₂O strand count: 2·H(2) + O(24) = 28. -/
-- Hydrogen: Z=1, N=0, so 1+0+1 = 2 per atom
-- Oxygen:   Z=8, N=8, so 8+8+8 = 24
theorem h2o_strands : 2 + 2 + 24 = 28 := by norm_num

/-- Valence electron accounting for H₂O: 2 bonded pairs + 2 lone
    pairs on O = 4 valence pairs = 8 valence electrons
    (6 from O's n=2 shell + 2 from the two H atoms). -/
theorem h2o_valence_count : 2 * 2 + 2 * 2 = 8 := by norm_num
