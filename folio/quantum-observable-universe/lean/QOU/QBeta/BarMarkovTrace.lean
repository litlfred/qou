/-
# The bar involution and the Markov trace on `H₃`, and why `z_D` is bar-stable

Bean `qou-hlx8` (epic `qou-qs0e`). Explains, as an identity, the measurement recorded in
`docs/audits/2026-11-15-one-sided-weak-vertex.md` §4: on the Q_β element,
`tr^{z_D(q)}(bar Δ)(q) = tr^{z_D(1/q)}(Δ)(1/q)` to 7e-52.

Work on the NF free module `Fin 6 → R` of `H₃` (`mulNF`, `trM`). The bar involution
`σ ↦ σ⁻¹ = σ − h` is the ring isomorphism `H₃(q⁻¹) → H₃(q)`; on coordinates it is the
`R`-linear map `barNF h` that sends each basis word to the same word in the flipped letters
`σ_g − h` (the scalar substitution `h ↦ −h` is carried by the source algebra being at `−h`).

* `barNF_mul`: `barNF h (u ·₍₋ₕ₎ v) = barNF h u ·₍ₕ₎ barNF h v` — `barNF` is multiplicative
  from the algebra at `−h` to the algebra at `h`.
* `trM_barNF`: `trM z h (barNF h v) = trM (z − h) (−h) v` for EVERY `z`: pulling the Markov
  trace back along bar gives the Markov trace at parameter `z − h` on the algebra at `−h`.
* `zD_bar_stable`: `z_D(q⁻¹) = z_D(q) − (q − q⁻¹)` for `z_D = q³/(q²+1)`. So under convention
  D the pulled-back trace IS the convention-D trace at `q⁻¹` (`trM_barNF_zD`), which is the
  measured identity. (Convention C `√q/(q+1)` is not bar-stable — checked in the probe.)

Base ring (§7c): generic `[CommRing R]` / `[Field K]`. No `ℝ`.

-- Ref: [kazhdan-lusztig1979] https://doi.org/10.1007/BF01390031
-/
import QOU.Machinery.HeckeH3AlgebraLaws
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta.BarMarkov

open QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- `σ₀ − h` as an NF vector. -/
def f0 (h : R) : Fin 6 → R := ![-h, 1, 0, 0, 0, 0]
/-- `σ₁ − h` as an NF vector. -/
def f1 (h : R) : Fin 6 → R := ![-h, 0, 1, 0, 0, 0]

/-- The bar map on coordinates, `v ↦ ∑ⱼ vⱼ · bar(bⱼ)`, written out: column `j` is the basis
word `bⱼ` (`b₃ = σ₁σ₀`, `b₄ = σ₀σ₁`, `b₅ = σ₀σ₁σ₀` in `mulNF`'s product) in the flipped
letters `σ_g − h`. `barNF_gen0/1` and `barNF_one` with `barNF_mul` characterise it as THE
algebra map `H₃(−h) → H₃(h)` sending `σ_g ↦ σ_g − h`. -/
def barNF (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 0 - h * v 1 - h * v 2 + h ^ 2 * v 3 + h ^ 2 * v 4 - h * (h ^ 2 + 1) * v 5,
    v 1 - h * v 3 - h * v 4 + h ^ 2 * v 5,
    v 2 - h * v 3 - h * v 4 + h ^ 2 * v 5,
    v 3 - h * v 5,
    v 4 - h * v 5,
    v 5]

theorem barNF_one (h : R) : barNF h ![1, 0, 0, 0, 0, 0] = ![1, 0, 0, 0, 0, 0] := by
  funext i; fin_cases i <;> simp [barNF]

theorem barNF_gen0 (h : R) : barNF h ![0, 1, 0, 0, 0, 0] = f0 h := by
  funext i; fin_cases i <;> simp [barNF, f0]

theorem barNF_gen1 (h : R) : barNF h ![0, 0, 1, 0, 0, 0] = f1 h := by
  funext i; fin_cases i <;> simp [barNF, f1]

/-- **bar is multiplicative**, from the algebra at `−h` (`q⁻¹`) to the algebra at `h` (`q`). -/
theorem barNF_mul (h : R) (u v : Fin 6 → R) :
    barNF h (mulNF (-h) u v) = mulNF h (barNF h u) (barNF h v) := by
  funext i
  fin_cases i <;> simp [barNF, mulNF, mulσ₀, mulσ₁] <;> ring

/-- **The Markov trace pulled back along bar** is the Markov trace at `z − h` on the
algebra at `−h`, for every `z`. -/
theorem trM_barNF (z h : R) (v : Fin 6 → R) :
    trM z h (barNF h v) = trM (z - h) (-h) v := by
  simp [trM, TRM, barNF, Fin.sum_univ_six]
  ring

/-- **`z_D` is bar-stable**: `z_D(q⁻¹) = z_D(q) − (q − q⁻¹)`. -/
theorem zD_bar_stable {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    q⁻¹ ^ 3 / (q⁻¹ ^ 2 + 1) = q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹) := by
  have hq2' : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  have h1 : q⁻¹ ^ 2 + 1 ≠ 0 := by
    intro h; apply hq2'
    have := congrArg (· * q ^ 2) h
    simp only [add_mul, inv_pow, inv_mul_cancel₀ (pow_ne_zero 2 hq), one_mul, zero_mul] at this
    exact this
  field_simp
  ring

/-- Composite: under convention D the pulled-back trace is the convention-D trace at `q⁻¹`. -/
theorem trM_barNF_zD {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (v : Fin 6 → K) :
    trM (q ^ 3 / (q ^ 2 + 1)) (q - q⁻¹) (barNF (q - q⁻¹) v) =
      trM (q⁻¹ ^ 3 / (q⁻¹ ^ 2 + 1)) (q⁻¹ - q⁻¹⁻¹) v := by
  rw [trM_barNF, zD_bar_stable hq hq2, inv_inv]
  congr 1; ring

end QOU.QBeta.BarMarkov
