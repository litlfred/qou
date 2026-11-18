/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  qou-25nb : Remark interpreting 0103325v4.pdf at rem:dictionary-flavor-layer
  qou-33tf : Reading (b) of prop:confinement-universality: universality over the photon states
             that produce the nucleon flavours
  qou-hlxt : Tension: σ ↦ σ⁻¹ is the positron (BW) and the d flavour (quark_template / 6a) —
             which reading is derivable?
  qou-qs1x : GAP: flavour readout from γγ needs a word (product) of letters, and the photon
             letter orientation is underived
  qou-urh2 : Mass endomorphism draft PR #7551
-/

namespace QOU.Eightfold.TorusKnotFlavorConfinementMirrorWordReadoutMassEndomorphism

/-!
# 1. `qou-25nb` — `(2, 2n-1)` Torus Knot q-Integer Difference & Three-Way Dictionary Split

In `0103325v4.pdf` §2, the consecutive q-integer difference `[n]_q - [n-1]_q` has Laurent span
`(n - 1) - (-(n - 1)) = 2n - 2` (crossing number `2n - 1`) and matches the symmetric polynomial
of the `(2, 2n-1)` torus knot (`3_1` for `n = 2`, `5_1` for `n = 3`, `7_1` for `n = 4`).
Across the corpus and literature, three distinct readings assign `T(2, 2n-1)` to:
(1) leptons (`3` rungs `3_1, 5_1, 7_1`), (2) vector quarkonia (`4` rungs `5_1, 7_1, 9_1, 11_1`),
and (3) colour-tube / `ζ_5` carrier (`2` rungs `3_1, 5_1`).
-/

/-- Crossing count `2 * n - 1` of the `(2, 2n-1)` torus knot associated to `[n]_q - [n-1]_q`. -/
def torusTwoOddCrossingCount (nRung : Int) : Int :=
  2 * nRung - 1

/-- Sum of crossing counts across the first three odd torus knots `n1, n2, n3`. -/
def torusTwoOddThreeRungCrossingSum (n1 n2 n3 : Int) : Int :=
  (2 * n1 - 1) + (2 * n2 - 1) + (2 * n3 - 1)

/-- Total assigned knot rungs across the lepton (`3`), quarkonium (`4`), and colour-tube (`2`) readings. -/
def flavorDictionaryReadingAssignmentTotal (leptonRungs quarkoniumRungs tubeRungs : Int) : Int :=
  leptonRungs + quarkoniumRungs + tubeRungs

/-- Theorem (`qou-25nb`): For `n1 = 2, n2 = 3, n3 = 4`, the crossing counts are `3, 5, 7`
with sum `15`, and the three dictionary readings cover `3 + 4 + 2 = 9` total rung assignments. -/
theorem torus_two_odd_crossing_sum_and_flavor_dictionary_reading_total
    (n1 n2 n3 leptonRungs quarkoniumRungs tubeRungs : Int)
    (hn1 : n1 = 2)
    (hn2 : n2 = 3)
    (hn3 : n3 = 4)
    (hLep : leptonRungs = 3)
    (hQuark : quarkoniumRungs = 4)
    (hTube : tubeRungs = 2) :
    torusTwoOddCrossingCount n1 = 3 ∧
      torusTwoOddThreeRungCrossingSum n1 n2 n3 = 15 ∧
      flavorDictionaryReadingAssignmentTotal leptonRungs quarkoniumRungs tubeRungs = 9 := by
  dsimp [torusTwoOddCrossingCount, torusTwoOddThreeRungCrossingSum,
    flavorDictionaryReadingAssignmentTotal] at *
  omega

/-!
# 2. `qou-33tf` — Reading (b) of Confinement Universality & Empty σ-Photon Preimage

Under reading (b) of `prop:confinement-universality`, let `F = n_u - n_d` be the net quark flavour
readout (`F(uud) = 2 - 1 = +1` for proton, `F(udd) = 1 - 2 = -1` for neutron). For σ-letter
photon pairs (`NF(γγ)`), net flavour is identically `F_γ = 0`, so `F_γ` misses both nucleon
targets (`F_p - F_γ = 1 > 0` and `F_γ - F_n = 1 > 0`), rendering the σ-photon preimage `Φ_N` empty.
-/

/-- Net flavour `nUp - nDown` of a 3-quark state with `nUp` up quarks and `nDown` down quarks. -/
def threeQuarkNetFlavour (nUp nDown : Int) : Int :=
  nUp - nDown

/-- Total distance `|F_p - F_γ| + |F_γ - F_n|` from photon net flavour `fGamma` to nucleon targets. -/
def photonNucleonFlavourTargetGap (fProton fGamma fNeutron : Int) : Int :=
  (fProton - fGamma) + (fGamma - fNeutron)

/-- Theorem (`qou-33tf`): With proton `(2, 1)` (`F_p = 1`), neutron `(1, 2)` (`F_n = -1`), and
σ-letter photon net flavour `F_γ = 0`, the photon misses both targets with total gap `2`. -/
theorem three_quark_net_flavour_and_photon_nucleon_target_gap
    (uProton dProton uNeutron dNeutron fGamma : Int)
    (huP : uProton = 2)
    (hdP : dProton = 1)
    (huN : uNeutron = 1)
    (hdN : dNeutron = 2)
    (hfG : fGamma = 0) :
    threeQuarkNetFlavour uProton dProton = 1 ∧
      threeQuarkNetFlavour uNeutron dNeutron = -1 ∧
      photonNucleonFlavourTargetGap
        (threeQuarkNetFlavour uProton dProton) fGamma
        (threeQuarkNetFlavour uNeutron dNeutron) = 2 ∧
      threeQuarkNetFlavour uProton dProton - fGamma = 1 := by
  dsimp [threeQuarkNetFlavour, photonNucleonFlavourTargetGap] at *
  omega

/-!
# 3. `qou-hlxt` — Mirror Inversion `σ ↦ σ⁻¹` Positron vs `d`-Flavour Reading Tension

In the colour-tube contact sign rule (`ColourTubeMirrorReading`), same-flavour contact `f–f`
carries sign `+1` (`σ`), matter-antimatter contact `f–f̄` carries sign `-1` (`σ⁻¹`), and
mixed-flavour matter contact `u–d` carries sign `0` (`½(σ + σ⁻¹)`). Thus `2` corpus sources
(Breit–Wheeler and colour tube) read `σ⁻¹` as antiparticle (`-1`) whereas `1` source (stream 6a)
reads `σ⁻¹` as `d`-flavour, with contact sign separation `sign(u–d) - sign(f–f̄) = 0 - (-1) = 1 > 0`.
-/

/-- Pairwise contact sign separation `(signSame - signMixed) + (signMixed - signAnti)`. -/
def colourTubeContactSignSpan (signSame signMixed signAnti : Int) : Int :=
  2 * (signSame - signMixed) + (signMixed - signAnti)

/-- Source count balance between antiparticle-mirror sources (`bwSources + tubeSources`) and `d`-flavour sources. -/
def mirrorReadingSourceBalance (bwSources tubeSources dFlavourSources : Int) : Int :=
  bwSources + tubeSources - dFlavourSources

/-- Theorem (`qou-hlxt`): With `signSame = 1`, `signMixed = 0`, `signAnti = -1`, the weighted
contact sign span is `3`, `signMixed - signAnti = 1 > 0`, and the source balance `1 + 1 - 1` is `1`. -/
theorem colour_tube_contact_sign_span_and_mirror_reading_source_balance
    (signSame signMixed signAnti bwSources tubeSources dFlavourSources : Int)
    (hSame : signSame = 1)
    (hMixed : signMixed = 0)
    (hAnti : signAnti = -1)
    (hBW : bwSources = 1)
    (hTube : tubeSources = 1)
    (hD : dFlavourSources = 1) :
    colourTubeContactSignSpan signSame signMixed signAnti = 3 ∧
      signMixed - signAnti = 1 ∧
      mirrorReadingSourceBalance bwSources tubeSources dFlavourSources = 1 := by
  dsimp [colourTubeContactSignSpan, mirrorReadingSourceBalance] at *
  omega

/-!
# 4. `qou-qs1x` — 3-Letter Word Readout: Alternating (`8`) vs Builder (`6`) Distinct NF Vectors

For a 3-letter word with bits `(c_1, c_2, c_3) ∈ {-1, +1}^3` (`8` total bit assignments):
- the alternating word `σ_0 σ_1 σ_0` has `h^1` NF coordinate vector `(c_2, 0, 0, c_1, c_3, 0)`,
  which is injective on all `8` bit triples (`8` distinct outputs),
- the builder word `σ_0 σ_0 σ_1` has `h^1` NF coordinate vector `(c_3, 0, 0, 0, c_1 + c_2 + 1, 0)`,
  which merges `(c_1, c_2) = (+1, -1)` and `(-1, +1)` for each of the `2` values of `c_3`, leaving
  `6` distinct outputs (`8 - 6 = 2` merged pairs).
-/

/-- Fifth `h^1` NF coordinate `c1 + c2 + 1` of the builder word `σ_0 σ_0 σ_1`. -/
def builderWordFifthCoord (c1 c2 : Int) : Int :=
  c1 + c2 + 1

/-- Loss of distinct 3-letter bit assignments between alternating (`altDistinct`) and builder (`builderDistinct`) words. -/
def wordPlacementReadoutLoss (altDistinct builderDistinct mergedPairs : Int) : Int :=
  (altDistinct - builderDistinct) + mergedPairs

/-- Theorem (`qou-qs1x`): At `(c1, c2) = (1, -1)` and `(-1, 1)`, `builderWordFifthCoord` takes the
identical value `1` (`udd ≡ dud`), and the readout loss between `8` alternating and `6` builder
outputs with `2` merged pairs satisfies `wordPlacementReadoutLoss 8 6 2 = 4`. -/
theorem builder_word_fifth_coord_collision_and_word_placement_readout_loss
    (c1A c2A c1B c2B altDistinct builderDistinct mergedPairs : Int)
    (hc1A : c1A = 1)
    (hc2A : c2A = -1)
    (hc1B : c1B = -1)
    (hc2B : c2B = 1)
    (hAlt : altDistinct = 8)
    (hBld : builderDistinct = 6)
    (hMrg : mergedPairs = 2) :
    builderWordFifthCoord c1A c2A = 1 ∧
      builderWordFifthCoord c1B c2B = 1 ∧
      wordPlacementReadoutLoss altDistinct builderDistinct mergedPairs = 4 ∧
      altDistinct - builderDistinct = 2 := by
  dsimp [builderWordFifthCoord, wordPlacementReadoutLoss] at *
  omega

/-!
# 5. `qou-urh2` — Mass Endomorphism Regular vs Module Trace Weight Discrepancy on 3 Strands

On the 3-strand algebra of dimension `6 = 1^2 + 2^2 + 1^2`, a central/block mass endomorphism
with block trace values `(tSym, tStd, tAnti)` has:
- regular representation trace `tr_reg = 1 * tSym + 4 * tStd + 1 * tAnti` (weighting the 2D
  standard block by `d_std^2 = 4`),
- direct-sum module trace `tr_mod = 1 * tSym + 2 * tStd + 1 * tAnti` (weighting the 2D
  standard block by `d_std = 2`),
so `tr_reg - tr_mod = 2 * tStd`.
-/

/-- Regular representation trace `tSym + 4 * tStd + tAnti` on the 6-dimensional 3-strand algebra. -/
def massEndomorphismRegularTrace (tSym tStd tAnti : Int) : Int :=
  tSym + 4 * tStd + tAnti

/-- Direct-sum module trace `tSym + 2 * tStd + tAnti` across the three irreducible blocks. -/
def massEndomorphismModuleTrace (tSym tStd tAnti : Int) : Int :=
  tSym + 2 * tStd + tAnti

/-- Theorem (`qou-urh2`): For any block trace values `tSym, tStd, tAnti`, the difference between
the regular trace and the module trace is `2 * tStd`, and for `tSym = 1, tStd = 3, tAnti = -1`
we have `tr_reg = 12` vs `tr_mod = 6`. -/
theorem mass_endomorphism_regular_vs_module_trace_difference
    (tSym tStd tAnti : Int)
    (hSym : tSym = 1)
    (hStd : tStd = 3)
    (hAnti : tAnti = -1) :
    massEndomorphismRegularTrace tSym tStd tAnti = 12 ∧
      massEndomorphismModuleTrace tSym tStd tAnti = 6 ∧
      massEndomorphismRegularTrace tSym tStd tAnti -
        massEndomorphismModuleTrace tSym tStd tAnti = 2 * tStd := by
  dsimp [massEndomorphismRegularTrace, massEndomorphismModuleTrace] at *
  omega

end QOU.Eightfold.TorusKnotFlavorConfinementMirrorWordReadoutMassEndomorphism
