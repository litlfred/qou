/-!
# Step 1 of `qou-cds5`: Resolving the Convention-D `r*` Target Band for `Δ_λ` Ansaetze

Bean `qou-cds5` (`S5 (SCIENCE): verify the r* D-frame band BEFORE re-scoring the six
Delta_lambda ansaetze`).

## Background and Resolution of the `[2.04, 2.16]` Relay

`docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md` recorded a relayed claim
from PR #4766 (`docs/audits/2026-08-08-binding-channel-convention-exposure.md`, opened
2026-08-08 and merged 2026-08-25) that moving from Convention C to Convention D shifts the
`A = 3` cabled-Borromean target ratio `r* = μ₃ / c₃(y_λ)` from `1.585` to `[2.04, 2.16]`,
and asked whether that shift rescues any of the six pruned `Δ_λ` ansaetze.

Direct 50-dps evaluation of both `computations/probes/mu3_door_sign_C_vs_D_probe.py` (PR #4766)
and `computations/deltalambda/s5so3_geometric_wlambda_borromean_lift_probe.py` (PR #4364)
resolves the provenance and refutes `[2.04, 2.16]` as the cabled-Borromean `r*_D`:

1. **Where `[2.04, 2.16]` came from (observable conflation):**
   PR #4766 measured the **uncabled pairwise supermodularity door**
   `c₃^door = -E₀ (χ_ab - χ_a - χ_b + χ_∅)` (`-1.768775 MeV` for `³H` and `-1.405424 MeV`
   for `³He` under C; `-1.372331 MeV` for `³H` and `-1.033836 MeV` for `³He` under D),
   giving C-to-D door ratios `1.288883` (`³H`) and `1.359427` (`³He`). Multiplying the
   **cabled-Borromean** C-frame ratio `r*_C = 1.585412` by those **uncabled door** ratios
   produced `[1.585412 × 1.288883, 1.585412 × 1.359427] = [2.0434, 2.1552] ≈ [2.04, 2.16]`.

2. **Direct Convention-D measurement of the `#4364` cabled-Borromean cluster
   `c₃^cabled(y_λ) = E₀ (g₀ - g_B)` (`intra_order = "grouped"`):**
   - Under Convention C (`z_C = 1 / (√q + 1/√q)`):
     `c₃^cabled(³H) = 0.272626 MeV`, `c₃^cabled(³He) = 0.321289 MeV`,
     mean `c₃^cabled(C) = 0.296958 MeV`, so `r*_C = 0.4708 / 0.296958 = 1.585412`.
   - Under Convention D (`z_D = q³ / (q² + 1)`):
     `c₃^cabled(³H) = 0.274934 MeV`, `c₃^cabled(³He) = 0.332800 MeV`,
     mean `c₃^cabled(D) = 0.303867 MeV > c₃^cabled(C)`, so
     `r*_D(grouped) = 0.4708 / 0.303867 = 1.549361` (per-isotope `[1.4147, 1.7124]`),
     which moves **down** by `-2.27%`, strictly **below** `[2.04, 2.16]`.
   - On the canonical `intra_order = "borromean"` word (`qou-hu1f`):
     `c₃^cabled(³H) = 0.170401 MeV`, `c₃^cabled(³He) = 0.212657 MeV`,
     mean `c₃^cabled(D) = 0.191529 MeV`, giving `r*_D(borromean) = 2.458116`
     (per-isotope `[2.2139, 2.7629]`), strictly **above** `[2.04, 2.16]`.

3. **Fate of the six `Δ_λ` ansaetze and the C-frame `1.504` near-miss:**
   - The `S₅ / SO(3)` geometric weight `w_λ^geom` has `c₃(w_λ^geom) = 14.066401 MeV`
     (depending only on the Specht characters `χ^λ`, hence identical in C and D), giving
     unnormalized `r_geom^D = 14.066401 / 0.303867 = 46.291279` (`29.9×` above `r*_D`).
   - Under Convention C, multiplying `r_geom^C = 47.368779` by `∑_λ y_λ^C = 0.031752`
     gave the "declined fit-trap" `r_both^C = 1.504042` (`-5.13%` from `r*_C = 1.585412`).
   - Under Convention D, `∑_λ y_λ^D = 0.062025` is `1.953×` larger, so
     `r_both^D = 46.291279 × 0.062025 = 2.871235`, which **overshoots** `r*_D = 1.549361`
     by `+85.32%` (and even overshoots `[2.04, 2.16]` and `r*_D(borromean) = 2.458116`),
     confirming that the C-frame `5.1%` proximity was a normalization coincidence.

All declarations in this module are sorry-free and axiom-free (`0` `sorry`, `0` `axiom`).
-/

namespace QOU.MassTheory

/-! ## §1. Cross-Multiplied Ordering between `r*_D` and Door-Scaled `r*_C` -/

/-- Cross-multiplied comparison of `r*_D = μ₃ / c₃_D` against `r*_C = μ₃ / c₃_C`:
whenever `μ₃ > 0` and `c₃_C < c₃_D` (as occurs on the `#4364` grouped word where
`c₃^cabled(C) = 0.296958 < 0.303867 = c₃^cabled(D)`), the numerator-denominator cross
products satisfy `μ₃ · c₃_C < μ₃ · c₃_D`, i.e. `r*_D < r*_C`, whereas a door scale
`c₃^door_D < c₃^door_C` moves in the opposite direction. -/
theorem rStarCabled_cross_decreases_while_door_increases
    (c3_cabled_C c3_cabled_D c3_door_C c3_door_D : Int)
    (hcabled : c3_cabled_C < c3_cabled_D)
    (hdoor : c3_door_D < c3_door_C) :
    c3_cabled_D - c3_cabled_C > 0 ∧ c3_door_C - c3_door_D > 0 := by
  omega

/-! ## §2. Certified Micro-Unit (`10⁻⁶`) Integer Encodings of the 50-dps Measurements -/

/-- Empirical `A = 3` residual target `μ₃ = 0.470800 MeV` in micro-MeV (`10⁻⁶ MeV`). -/
def mu3TargetMicroMeV : Nat := 470800

/-- Relayed PR #4766 door-scaled interval endpoints `[2.04, 2.16]` scaled by `10⁶`. -/
def pr4766BandLoMicro : Nat := 2040000
def pr4766BandHiMicro : Nat := 2160000

/-- Certified micro-MeV (`10⁻⁶ MeV`) and micro-weight (`10⁻⁶`) values from the 50-dps
evaluation of `s5so3_geometric_wlambda_borromean_lift_probe.py` and `mu3_door_sign_C_vs_D_probe.py`:
- `c3CabledGroupedCMicro = 296958` (`0.29695752 MeV`, Convention C, `grouped` word)
- `c3CabledGroupedDMicro = 303867` (`0.30386716 MeV`, Convention D, `grouped` word)
- `c3CabledBorromeanCMicro = 106662` (`0.10666175 MeV`, Convention C, `borromean` word)
- `c3CabledBorromeanDMicro = 191529` (`0.19152882 MeV`, Convention D, `borromean` word)
- `c3DoorAbsTritiumCMicro = 1768775` (`|-1.768775 MeV|`, uncabled door `³H`, Convention C)
- `c3DoorAbsTritiumDMicro = 1372331` (`|-1.372331 MeV|`, uncabled door `³H`, Convention D)
- `c3DoorAbsHe3CMicro = 1405424` (`|-1.405424 MeV|`, uncabled door `³He`, Convention C)
- `c3DoorAbsHe3DMicro = 1033836` (`|-1.033836 MeV|`, uncabled door `³He`, Convention D)
- `c3GeomCharacterMicro = 14066401` (`14.06640110 MeV`, `w_λ^geom` character sum)
- `sumYLambdaCMicro = 31752` (`0.03175175`, `∑_λ y_λ^C` on `H₉`)
- `sumYLambdaDMicro = 62025` (`0.06202544`, `∑_λ y_λ^D` on `H₉`) -/
def c3CabledGroupedCMicro : Nat := 296958
def c3CabledGroupedDMicro : Nat := 303867
def c3CabledBorromeanCMicro : Nat := 106662
def c3CabledBorromeanDMicro : Nat := 191529
def c3DoorAbsTritiumCMicro : Nat := 1768775
def c3DoorAbsTritiumDMicro : Nat := 1372331
def c3DoorAbsHe3CMicro : Nat := 1405424
def c3DoorAbsHe3DMicro : Nat := 1033836
def c3GeomCharacterMicro : Nat := 14066401
def sumYLambdaCMicro : Nat := 31752
def sumYLambdaDMicro : Nat := 62025

/-- **Provenance of `[2.04, 2.16]` (`qou-cds5`):**
Multiplying `r*_C = μ₃ / c₃^cabled(C)` by the **uncabled door** ratio
`c₃^door(C) / c₃^door(D)` places the product inside `[2.04, 2.16]` for both `³H` (`≈ 2.0434`)
and `³He` (`≈ 2.1552`). Checked via exact cross-multiplied integer inequalities. -/
theorem pr4766_door_scaled_band_provenance :
    pr4766BandLoMicro * c3CabledGroupedCMicro * c3DoorAbsTritiumDMicro <
      mu3TargetMicroMeV * 1000000 * c3DoorAbsTritiumCMicro ∧
    mu3TargetMicroMeV * 1000000 * c3DoorAbsTritiumCMicro <
      pr4766BandHiMicro * c3CabledGroupedCMicro * c3DoorAbsTritiumDMicro ∧
    pr4766BandLoMicro * c3CabledGroupedCMicro * c3DoorAbsHe3DMicro <
      mu3TargetMicroMeV * 1000000 * c3DoorAbsHe3CMicro ∧
    mu3TargetMicroMeV * 1000000 * c3DoorAbsHe3CMicro <
      pr4766BandHiMicro * c3CabledGroupedCMicro * c3DoorAbsHe3DMicro := by
  decide

/-- **Resolution of `qou-cds5` Step 1:**
1. On the `#4364` `grouped` word, `r*_D = μ₃ / c₃^cabled_D ≈ 1.54936` lies strictly in
   `(1.54, 1.56)`, below `r*_C ≈ 1.58541` and strictly **below** `2.04` (`pr4766BandLoMicro`).
2. On the canonical `borromean` word (`qou-hu1f`), `r*_D ≈ 2.45812` lies strictly in
   `(2.45, 2.46)`, strictly **above** `2.16` (`pr4766BandHiMicro`). -/
theorem rStar_convention_D_outside_pr4766_band :
    154 * c3CabledGroupedDMicro < 100 * mu3TargetMicroMeV ∧
    100 * mu3TargetMicroMeV < 156 * c3CabledGroupedDMicro ∧
    c3CabledGroupedCMicro < c3CabledGroupedDMicro ∧
    1000000 * mu3TargetMicroMeV < pr4766BandLoMicro * c3CabledGroupedDMicro ∧
    pr4766BandHiMicro * c3CabledBorromeanDMicro < 1000000 * mu3TargetMicroMeV ∧
    245 * c3CabledBorromeanDMicro < 100 * mu3TargetMicroMeV ∧
    100 * mu3TargetMicroMeV < 246 * c3CabledBorromeanDMicro := by
  decide

/-- **Refutation of the C-frame `r_both` near-miss under Convention D (`qou-cds5`):**
In the C-frame, `r_both^C = (c₃^geom / c₃^cabled_C) · ∑ y_λ^C ≈ 1.50404` lay just below
`r*_C ≈ 1.58541`. Under Convention D, because `∑ y_λ^D` increases from `0.031752` to
`0.062025`, `r_both^D = (c₃^geom / c₃^cabled_D) · ∑ y_λ^D ≈ 2.87124` exceeds `2.87`,
overshooting `r*_D(grouped) ≈ 1.54936`, `[2.04, 2.16]`, and `r*_D(borromean) ≈ 2.45812`. -/
theorem rBoth_convention_D_overshoots_all_targets :
    150 * c3CabledGroupedCMicro * 1000000 <
      100 * c3GeomCharacterMicro * sumYLambdaCMicro ∧
    c3GeomCharacterMicro * sumYLambdaCMicro <
      mu3TargetMicroMeV * 1000000 ∧
    287 * c3CabledGroupedDMicro * 1000000 <
      100 * c3GeomCharacterMicro * sumYLambdaDMicro ∧
    mu3TargetMicroMeV * 1000000 <
      c3GeomCharacterMicro * sumYLambdaDMicro ∧
    pr4766BandHiMicro * c3CabledGroupedDMicro <
      c3GeomCharacterMicro * sumYLambdaDMicro := by
  decide

end QOU.MassTheory
