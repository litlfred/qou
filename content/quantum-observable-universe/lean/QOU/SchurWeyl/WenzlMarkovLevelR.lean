import QOU.SchurWeyl.MarkovAssembly
import QOU.SchurWeyl.WenzlMarkovCorner

/-!
# QOU.SchurWeyl.WenzlMarkovLevelR — the Markov condition at every integer level

`MarkovAssembly.markov_of_corner_identity` reduces the Markov condition to the per-corner identity;
`WenzlMarkovCorner.wenzlWeight_markov_corner` proves that identity at every level `r`.  This file is
the composition, and it is the statement bean `qou-j7ln` set out to reach:

`∑_{|L| = m+2} w_L · tr(ι y · σ_{m+1})|_L = z_r · ∑_{|ν| = m+1} w_ν · tr(y)|_ν`,

for `w = wenzlWeight r (q²)` and `z_r = Q^r/(q·[r]_Q)`.

| | |
|---|---|
| `markov_wenzlWeight` | **the Markov condition at every integer level `r`** |
| `markov_wenzlWeight_two` | conservativity: `r = 2` reproduces `markov_conventionD` |

The merged convention-D chain (#5575) is the `r = 2` case: `z_2 = q⁴/(q(1+q²)) = q³/(q²+1) = z_D`,
and `markov_wenzlWeight_two` derives that statement from this one rather than restating it.

## Scope

`r` is the Wenzl level — the number of variables in the principal specialisation — and is a positive
integer by construction.  This is a statement about **every point of the Wenzl lattice**, not about
arbitrary `z`, which is off it.

## Base ring (§7c)

`ℝ`, forced by `seminormalParam` and by `Hecke ℝ q q⁻¹`.

LaTeX label: `thm:wenzl-markov-level-r`
-/

namespace QOU.SchurWeyl
namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.Seminormal QOU.SchurWeyl.HeckeInclusion

/-- **The Markov condition for `wenzlWeight r (q²)`, at every integer level `r`.**

The `w`-weighted seminormal trace of `ι y · σ_{m+1}` over the diagrams of size `m + 2` is `z_r` times
the `w`-weighted trace of `y` over those of size `m + 1`, with

`z_r = Q^r / (q · [r]_Q)`,  `Q = q²`.

`hgen` — `Q` is not a root of unity — is the single genericity hypothesis the whole level-`r` chain
runs on; `hq2` is what `seminormalRep` itself needs, and is implied by `hgen` but has to be named
because it appears in the statement. -/
theorem markov_wenzlWeight (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1) {r : ℕ} (hr : r ≠ 0) {m : ℕ}
    (y : Hecke ℝ q q⁻¹ m) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        wenzlWeight r (q ^ 2) L.1
          * ((seminormalRep q hq hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y))
              * genMat q (m + 1) (by omega) L.2.ge).trace
      = (q ^ 2) ^ r / (q * levelBracket r (q ^ 2))
        * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
            wenzlWeight r (q ^ 2) ν.1 * (seminormalRep q hq hq2 m ν.2 y).trace :=
  markov_of_corner_identity hq hq2 (wenzlWeight r (q ^ 2))
    (fun ν _ _c hc => wenzlWeight_markov_corner q hq hgen hr ν hc) y

/-- **Conservativity: at `r = 2` this *is* the merged convention-D statement.**

`z_2 = (q²)²/(q·[2]_{q²}) = q³/(q²+1) = z_D` and `wenzlWeight 2 (q²) = ocneanuWeight q z_D`, so
`markov_wenzlWeight` at `r = 2` reproduces `MarkovConventionD.markov_conventionD` on the nose — the
general-level theorem specialises back to what #5575 proved, rather than merely resembling it. -/
theorem markov_wenzlWeight_two (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1) {m : ℕ} (y : Hecke ℝ q q⁻¹ m) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) L.1
          * ((seminormalRep q hq hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y))
              * genMat q (m + 1) (by omega) L.2.ge).trace
      = (q ^ 3 / (q ^ 2 + 1)) * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 * (seminormalRep q hq hq2 m ν.2 y).trace := by
  have hq21 : (q : ℝ) ^ 2 + 1 ≠ 0 := by positivity
  have hz : (q ^ 2 : ℝ) ^ 2 / (q * levelBracket 2 (q ^ 2)) = q ^ 3 / (q ^ 2 + 1) := by
    rw [levelBracket_two]
    field_simp
    ring
  have hmain := markov_wenzlWeight q hq hq2 hgen (r := 2) (by norm_num) y
  rw [hz] at hmain
  simpa only [wenzlWeight_two_eq_ocneanuWeight q hq hq21] using hmain

end SeminormalRep
end QOU.SchurWeyl
