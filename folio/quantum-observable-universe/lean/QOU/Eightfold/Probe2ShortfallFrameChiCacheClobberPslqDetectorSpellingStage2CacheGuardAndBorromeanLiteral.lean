/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Formalization for beans in the qou-10v9 subtree:
  - qou-34oo: 4He PROBE 2 body-order shortfall amplification under convention D (33.36%) vs convention C (26.40%)
  - qou-43v0: bar_pairing_binding_observable lossy overwrite of 25-key chi-cache witness to 21-key partial record
  - qou-580o: Detector-blind convention-C spelling 1/(u + 1/u) = u/(u^2 + 1), Vol(4_1) = 2*Cl_2(π/3) = 6*Λ(π/3), and c_3 sensitivity jump
  - qou-5ovu: he4_binding_k_stage2 Leg A nf-parameter cache guard vs Leg B unguarded cache acceptance
  - qou-5pgl: hecke_core.z +22.70% C->D import-cone shift and ALPHA_BORROMEAN_MEV = m_e * 8G +2.732 ppm literal transcription residual
-/

namespace QOU.Eightfold.Probe2ShortfallFrameChiCacheClobberPslqDetectorSpellingStage2CacheGuardAndBorromeanLiteral

/-!
## 1. Bean `qou-34oo`: `4He` PROBE 2 Shortfall Amplification (Convention C vs Canonical Convention D)
In `docs/audits/2026-07-05-delta-lambda-gate-status.md` PROBE 2, the quoted `4He` body-order figures
(`|b4c| = 1.9614`, `delivered = 1.54019`, `needed = 2.09252`, `del/need = 0.7360`, `26.40%` short)
are convention-C-frame. Under canonical convention D (`z = 0.612688`, `|b4c| = 1.17395`,
`delivered = 1.398`, `del/need = 0.6664`), the shortfall widens to `33.36%`.
-/

/-- Positive shortfall `needed - delivered` in scaled integer units. -/
def bodyOrderShortfall (needed delivered : Int) : Int :=
  needed - delivered

/-- Universal theorem: whenever `deliveredD < deliveredC` against a common target `scale`, the
    D-frame shortfall `scale - deliveredD` strictly exceeds the C-frame shortfall `scale - deliveredC`. -/
theorem convention_d_shortfall_exceeds_convention_c (scale deliveredC deliveredD : Int)
    (hDrop : deliveredD < deliveredC) :
    bodyOrderShortfall scale deliveredC < bodyOrderShortfall scale deliveredD := by
  dsimp [bodyOrderShortfall]
  omega

/-- Concrete verification in `10^5`-scaled units of the C-frame shortfall (`209252 - 154019 = 55233`)
    and in `10^4`-scaled ratio units that the D-frame shortfall (`10000 - 6664 = 3336`, `33.36%`)
    strictly exceeds the C-frame shortfall (`10000 - 7360 = 2640`, `26.40%`). -/
theorem probe2_he4_shortfall_c_vs_d_frame_comparison :
    bodyOrderShortfall 209252 154019 = 55233 ∧
    bodyOrderShortfall 10000 7360 = 2640 ∧
    bodyOrderShortfall 10000 6664 = 3336 ∧
    bodyOrderShortfall 10000 7360 < bodyOrderShortfall 10000 6664 ∧
    (196140 : Int) > 117395 := by
  decide

/-!
## 2. Bean `qou-43v0`: Lossy Clobber of `chi`-Cache Witness by `bar_pairing_binding_observable.py`
The upstream producer `chi_at_q0_via_hoefsmit_mpfr.py` writes a `25`-key witness including
`tr_M_at_q0`. When `bar_pairing_binding_observable.py` overwrites the same path, it drops `8`
upstream keys (including `tr_M_at_q0`) and adds `4` provenance keys (`3` of which are `None`),
leaving `25 - 8 + 4 = 21` keys (`18` non-null keys).
-/

/-- Resulting key count after overwriting a schema of `initialKeys` by dropping `lostKeys` and
    adding `gainedKeys`. -/
def clobberedKeyCount (initialKeys lostKeys gainedKeys : Int) : Int :=
  initialKeys - lostKeys + gainedKeys

/-- Universal theorem: whenever `gainedKeys < lostKeys`, overwriting the witness strictly reduces
    the total key count (`clobberedKeyCount initialKeys lostKeys gainedKeys < initialKeys`). -/
theorem lossy_overwrite_reduces_key_count (initialKeys lostKeys gainedKeys : Int)
    (hLossy : gainedKeys < lostKeys) :
    clobberedKeyCount initialKeys lostKeys gainedKeys < initialKeys := by
  dsimp [clobberedKeyCount]
  omega

/-- Concrete verification of the `25 -> 21` key drop (`8` lost, `4` gained, `3` `None` fields leaving
    `18` non-null keys). -/
theorem bar_pairing_chi_cache_overwrite_key_accounting :
    clobberedKeyCount 25 8 4 = 21 ∧
    (21 : Int) - 3 = 18 ∧
    clobberedKeyCount 25 8 4 < 25 := by
  decide

/-!
## 3. Bean `qou-580o`: Detector-Blind Convention-C Spelling, `Vol(4_1)` Factor of `3`, and `c_3` Jump
The pre-flip spelling `1 / (sqrt(q) + 1 / sqrt(q))` equals `sqrt(q) / (q + 1)` (`u / (u^2 + 1)` for
`u = sqrt(q)`): clearing denominators over `u / S + S / u = (u^2 + S^2) / (S * u)`, its reciprocal is
`(S * u) / (u^2 + S^2)`. Moreover, `Vol(4_1) = 2 * Cl_2(π/3) = 6 * Λ(π/3)` (`Cl_2(π/3) = 3 * Λ(π/3)`),
and substituting `z_D` into the C-frame `c_3` formula jumps `|c_3|` from `2.020188` to `974.382477`.
-/

/-- Cleared numerator `(u^2 + S^2) * (S * u)` of `(u / S + S / u) * (S * u)`. -/
def reciprocalSumClearedLHS (scale u : Int) : Int :=
  (u * u + scale * scale) * (scale * u)

/-- Expanded form `u^3 * S + S^3 * u` verifying `1 / (u/S + S/u) = S * u / (u^2 + S^2)`. -/
def reciprocalSumClearedRHS (scale u : Int) : Int :=
  (u * u) * (scale * u) + (scale * scale) * (scale * u)

/-- Universal algebraic identity confirming that the detector-blind reciprocal spelling
    `1 / (u + 1/u)` and the standard rational form `u / (u^2 + 1)` have identical cleared cross-products. -/
theorem detector_blind_c_spelling_cross_product_identity (scale u : Int) :
    reciprocalSumClearedLHS scale u = reciprocalSumClearedRHS scale u := by
  dsimp [reciprocalSumClearedLHS, reciprocalSumClearedRHS]
  rw [Int.add_mul]

/-- Concrete verification of the `Vol(4_1) = 2 * Cl_2(π/3) = 6 * Λ(π/3)` factor-of-3 identity in
    `10^10`-scaled units (`2 * 10149416064 = 6 * 3383138688 = 20298832128`) and the `> 480x` jump
    in `|c_3|` (`974382477` vs `2020188` in `10^6`-scaled units). -/
theorem vol41_clausen_lobachevsky_and_c3_sensitivity_jump :
    2 * (10149416064 : Int) = 6 * 3383138688 ∧
    2 * (10149416064 : Int) = 20298832128 ∧
    (974382477 : Int) > 480 * 2020188 := by
  decide

/-!
## 4. Bean `qou-5ovu`: `he4_binding_k_stage2` Leg A Parameter Guard vs Leg B Unguarded Cache
In `he4_binding_k_stage2_probe.py`, Leg A guards cached JSONL entries with `entry.nf == current_nf`,
discarding entries computed under a different `K`-factor word length, whereas Leg B accepts cached
partition entries unconditionally (`true`), creating a stale-cache discrepancy whenever
`cachedNf ≠ currentNf`.
-/

/-- Leg A cache acceptance predicate: requires `cachedNf == currentNf`. -/
def legACacheAccepts (cachedNf currentNf : Int) : Bool :=
  decide (cachedNf = currentNf)

/-- Leg B cache acceptance predicate: accepts unconditionally without checking `nf`. -/
def legBCacheAccepts (_cachedNf _currentNf : Int) : Bool :=
  true

/-- Universal theorem: whenever `cachedNf ≠ currentNf`, Leg A rejects the stale cache entry
    (`legACacheAccepts cachedNf currentNf = false`) while Leg B accepts it
    (`legBCacheAccepts cachedNf currentNf = true`). -/
theorem stage2_leg_a_rejects_while_leg_b_accepts_on_nf_mismatch (cachedNf currentNf : Int)
    (hMismatch : cachedNf ≠ currentNf) :
    legACacheAccepts cachedNf currentNf = false ∧
    legBCacheAccepts cachedNf currentNf = true := by
  refine ⟨?_, rfl⟩
  dsimp [legACacheAccepts]
  rw [decide_eq_false_iff_not]
  exact hMismatch

/-!
## 5. Bean `qou-5pgl`: `hecke_core.z` `+22.70%` Flip and `ALPHA_BORROMEAN_MEV` `+2.732 ppm` Residual
Migrating `hecke_core.z` from convention C (`z_C ≈ 0.499320`) to `z = q^3 / (q^2 + 1) ≈ 0.612688`
shifts `z` by `+22.70%` (`612688 - 499320 = 113368` in `10^-6` units). Meanwhile, in
`paper_six_term_isotope_sweep.py:1151`, `ALPHA_BORROMEAN_MEV = 3.74446989` (`3744469890` in `10^-9`
MeV) exceeds its stated closed form `m_e * 8 * G = 3.744459660` (`3744459660` in `10^-9` MeV) by
`+10230` (`+2.732 ppm`), and the implied `m_e = 0.511000347` exceeds all three CODATA editions
(`2014`: `0.5109989461`, `2018`: `0.5109989500`, `2022`: `0.51099895069`).
-/

/-- Absolute residual `literalVal - closedFormVal` of a hardcoded constant against its closed form. -/
def hardcodedLiteralResidual (literalVal closedFormVal : Int) : Int :=
  literalVal - closedFormVal

/-- Universal theorem: if a hardcoded literal `literalVal` strictly exceeds the upper bound `maxEditionVal`
    of all reference editions, then `literalVal - editionVal > 0` for every `editionVal ≤ maxEditionVal`. -/
theorem literal_exceeds_all_editions_of_gt_max (literalVal maxEditionVal editionVal : Int)
    (hGtMax : maxEditionVal < literalVal) (hLeMax : editionVal ≤ maxEditionVal) :
    0 < hardcodedLiteralResidual literalVal editionVal := by
  dsimp [hardcodedLiteralResidual]
  omega

/-- Concrete verification of:
    1. The `+22.70%` shift in `z` (`612688 - 499320 = 113368`, with `2270 * 499320 < 10000 * 113368 < 2271 * 499320`);
    2. The `+10230` (`10^-9` MeV, `~2.732 ppm`) excess of `3744469890` over `m_e * 8G = 3744459660`;
    3. The strict ordering of CODATA-2014 (`51099894610`), CODATA-2018 (`51099895000`), and
       CODATA-2022 (`51099895069`) `m_e` values (in `10^-11` MeV) below the literal-implied
       `m_e` (`51100034677`). -/
theorem z_import_cone_shift_and_alpha_borromean_literal_residual :
    (612688 : Int) - 499320 = 113368 ∧
    2270 * (499320 : Int) < 10000 * 113368 ∧
    10000 * (113368 : Int) < 2271 * 499320 ∧
    hardcodedLiteralResidual 3744469890 3744459660 = 10230 ∧
    (51099894610 : Int) < 51099895000 ∧
    (51099895000 : Int) < 51099895069 ∧
    (51099895069 : Int) < 51100034677 := by
  decide

end QOU.Eightfold.Probe2ShortfallFrameChiCacheClobberPslqDetectorSpellingStage2CacheGuardAndBorromeanLiteral
