import QOU.MassTheory.RaLDeterminant

/-!
# A positive angle structure on the `RᵃL` layered triangulation, every `a ≥ 3`

`NeumannZagierBloch` writes the gluing of the layered triangulation of the
once-punctured-torus bundle of `RᵃL` as rows `∏ⱼ zⱼ^{A_kj} (1 − zⱼ)^{B_kj} = 1`. Taking
arguments, with `arg zⱼ = π αⱼ` and `arg(1 − zⱼ) = −π βⱼ`, a shape vector in the upper
half plane gives angles with

* `αⱼ > 0`, `βⱼ > 0`, `αⱼ + βⱼ < 1` (the third dihedral angle `1 − αⱼ − βⱼ` is positive),
* `∑ⱼ (A_kj αⱼ − B_kj βⱼ) = 0` for every row `k`.

(For the geometric solution every row's argument sum is `0`, not a nonzero multiple of
`2π`; checked numerically for `a = 3, …, 12` in
`computations/probes/lepton_bundle_nahm_probe.py`.) A solution of these linear
conditions is a **positive angle structure**. Its existence is the hypothesis of the
Casson–Rivin / Guéritaud route to the geometric solution: the volume functional is
strictly concave on the polytope of angle structures, and its interior maximum is the
complete hyperbolic structure.

**Theorem** (`ra_angleStructure`). For every `a ≥ 3` there is an explicit positive angle
structure, with angles in units of `π / N`, `N = 128(a² + 1)`:

* layered tetrahedra `j = 0, …, a − 2`: `α = 8`, `β = 32(a² + 1) − 2(2j − a + 2)²`;
* the last two tetrahedra: `α = 15a² − 4a + 24`, `β = 16(a² + 1) + 4 − (a − 2)²`.

All integer arithmetic. The step from an angle structure to shapes in the upper half
plane (the volume maximization) is not proved here.

-- Ref: [futer-gueritaud-angled] D. Futer, F. Guéritaud, From angled triangulations to hyperbolic structures
-/

namespace QOU.Archimedean.RaLAngleStructure

open QOU.Archimedean.NeumannZagierBloch QOU.Archimedean.RaLSymplectic
open QOU.Archimedean.RaLDeterminant Matrix

/-- The `β` angle of layered tetrahedron `j`. -/
def bet (a : ℕ) (j : ℤ) : ℤ := 32 * ((a : ℤ) ^ 2 + 1) - 2 * (2 * j - a + 2) ^ 2

/-- The `β` angle of the last two tetrahedra. -/
def qB (a : ℕ) : ℤ := 16 * ((a : ℤ) ^ 2 + 1) + 4 - ((a : ℤ) - 2) ^ 2

/-- The `α` angle of the last two tetrahedra. -/
def pA (a : ℕ) : ℤ := 15 * (a : ℤ) ^ 2 - 4 * a + 24

/-- The `α` angles, as a function of the tetrahedron index. -/
def angA (a : ℕ) (j : ℤ) : ℤ := if j < (a : ℤ) - 1 then 8 else pA a

/-- The `β` angles, as a function of the tetrahedron index. -/
def angB (a : ℕ) (j : ℤ) : ℤ := if j < (a : ℤ) - 1 then bet a j else qB a

/-- The unit: `π = N`. -/
def unitN (a : ℕ) : ℤ := 128 * ((a : ℤ) ^ 2 + 1)

theorem ev_rows {a : ℕ} (h3 : 3 ≤ a) {k : ℕ} (hk : k ≤ a) :
    evA a k (angA a) - evB a k (angB a) = 0 := by
  unfold evA evB angA angB bet pA qB
  split_ifs <;> first | omega | ring1 |
    (have hka : (k : ℤ) = a := by omega
     rw [hka]; ring1)

/-- **The `RᵃL` triangulation carries a positive angle structure**, every `a ≥ 3`. -/
theorem ra_angleStructure {a : ℕ} (h3 : 3 ≤ a) :
    ∃ (N : ℤ) (α β : Fin (a + 1) → ℤ),
      (∀ j, 0 < α j ∧ 0 < β j ∧ α j + β j < N) ∧
      ∀ k, ∑ j, (raA a k j * α j - raB a k j * β j) = 0 := by
  refine ⟨unitN a, fun j => angA a (j : ℕ), fun j => angB a (j : ℕ), ?_, ?_⟩
  · intro j
    have hj := j.isLt
    have ha : (3 : ℤ) ≤ a := by exact_mod_cast h3
    dsimp only
    unfold angA angB bet pA qB unitN
    split_ifs with h
    · have hj0 : (0 : ℤ) ≤ (j : ℕ) := by positivity
      refine ⟨by norm_num, ?_, ?_⟩ <;> nlinarith
    · refine ⟨?_, ?_, ?_⟩ <;> nlinarith
  · intro k
    have hk := Nat.lt_succ_iff.1 k.isLt
    have h2 : 2 ≤ a := by omega
    simp only [Finset.sum_sub_distrib, raA_apply h2, raB_apply h2]
    rw [sum_rowA_mul (by omega) hk, sum_rowB_mul (by omega) hk]
    exact ev_rows h3 hk

end QOU.Archimedean.RaLAngleStructure
