import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

/-!
# A Weyl-symmetric pair coupling between two nucleon blocks is never Coulomb

Two three-strand blocks `A`, `B`, each strand in `V = C²` with basis `u`, `d`. A block with
`n` strands in state `u` has charge `Q = n − 1` (proton `n = 2`, neutron `n = 1`).

Every `gl(2)`-invariant symmetric bilinear form is `a·tr(XY) + b·tr X·tr Y`. Summed over the
strand pairs `i ∈ A`, `j ∈ B`, its Cartan part on a weight state with `u`-counts `nA`, `nB` is
`a·(nA·nB + dA·dB) + 9b` with `d = 3 − n` (`invCartan`). The off-diagonal part changes the
weight and has zero trace against the sector projectors (probe
`np_gaudin_pair_charge_probe.py`), so this is the whole pair shift of the rational Gaudin
coupling `Ω_AB/(z_A − z_B)`, for `sl(2)` and for `gl(2)`.

The form is symmetric under the Weyl reflection `u ↔ d`, which sends the proton block to the
neutron block. So it gives `pp = nn` (`invCartan_pp_eq_nn`), and a Coulomb shape
`c + κ·Q_A·Q_B` with `pp = nn` has `κ = 0` (`coulomb_kappa_zero_of_pp_eq_nn`). Hence no
invariant Gaudin coupling is Coulomb (`invCartan_not_coulomb`).

The Coulomb coupling itself is `Q ⊗ Q` with strand charge `Q = T₃ + B/2`, `B = 1/3` per strand
(Gell-Mann–Nishijima): `u ↦ 2/3`, `d ↦ −1/3` (`blockCharge_eq`). It is not Weyl symmetric
(`coulombPair_pp_ne_nn`): it needs the mixing of `T₃` with baryon number, which no invariant
form supplies.

Everything is over a generic commutative ring except the Gell-Mann–Nishijima lemmas, which need
`1/3` and are stated over a field.
-/

namespace QOU.QBeta.GaudinPair

section Generic

variable {R : Type*} [CommRing R]

/-- Cartan part of `a·tr(XY) + b·tr X·tr Y`, summed over the nine strand pairs, on blocks with
`u`-counts `nA`, `nB`. -/
def invCartan (a b : R) (nA nB : ℕ) : R :=
  a * ((nA : R) * nB + ((3 : R) - nA) * ((3 : R) - nB)) + 9 * b

/-- The invariant form gives the same value on the proton pair and the neutron pair. -/
theorem invCartan_pp_eq_nn (a b : R) : invCartan a b 2 2 = invCartan a b 1 1 := by
  unfold invCartan; push_cast; ring

/-- Coulomb shape `c + κ·Q_A·Q_B` on the four nucleon sectors, `Q = n − 1`. -/
def CoulombOnNucleons (E : ℕ → ℕ → R) (c κ : R) : Prop :=
  E 2 2 = c + κ ∧ E 2 1 = c ∧ E 1 2 = c ∧ E 1 1 = c

/-- A Coulomb shape with `pp = nn` has no charge-charge term. -/
theorem coulomb_kappa_zero_of_pp_eq_nn (E : ℕ → ℕ → R) (c κ : R) (h : E 2 2 = E 1 1)
    (hc : CoulombOnNucleons E c κ) : κ = 0 := by
  obtain ⟨h1, -, -, h4⟩ := hc
  have : c + κ = c := by rw [← h1, h, h4]
  linear_combination this

/-- No `gl(2)`-invariant pair coupling between the blocks is Coulomb with `κ ≠ 0`. -/
theorem invCartan_not_coulomb (a b c κ : R) (hκ : κ ≠ 0) :
    ¬ CoulombOnNucleons (invCartan a b) c κ := fun hc =>
  hκ (coulomb_kappa_zero_of_pp_eq_nn _ c κ (invCartan_pp_eq_nn a b) hc)

end Generic

section GellMannNishijima

variable {K : Type*} [Field K]

/-- Strand charge `T₃ + B/2` with `B = 1/3`: `u ↦ 1/2 + 1/6`, `d ↦ −1/2 + 1/6`. -/
noncomputable def strandCharge (u : Bool) : K :=
  if u then 1 / 2 + 1 / 6 else -1 / 2 + 1 / 6

/-- A three-strand block with `n` `u`-strands has charge `n − 1`. -/
theorem blockCharge_eq (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (n : K) :
    n * strandCharge true + (3 - n) * strandCharge false = n - 1 := by
  have h6 : (6 : K) ≠ 0 := by
    have : (6 : K) = 2 * 3 := by norm_num
    rw [this]; exact mul_ne_zero h2 h3
  unfold strandCharge; simp only [if_true, Bool.false_eq_true, if_false]
  field_simp; ring

/-- The Coulomb pair coupling `Σ_{i∈A, j∈B} Q_i Q_j = Q_A·Q_B` on `u`-counts. -/
def coulombPair (nA nB : ℕ) : K := ((nA : K) - 1) * ((nB : K) - 1)

theorem coulombPair_pp_ne_nn : (coulombPair 2 2 : K) ≠ coulombPair 1 1 := by
  unfold coulombPair; norm_num

end GellMannNishijima

end QOU.QBeta.GaudinPair
