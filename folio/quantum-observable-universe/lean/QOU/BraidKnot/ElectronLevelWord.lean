import QOU.MathlibExt.BraidGroup
import Mathlib.Tactic

/-!
# The excited electron word and its writhe

Owner ruling 2026-11-21: the electron is `e⁻ = σ₀σ₁σ₀ ∈ B₃` (closure: the Hopf
link). Under this ruling, photon absorption is the strand-adding curl
(`docs/audits/2026-11-21-photon-excitation-gs-reduction.md` §4a):

    e₁ = σ₀σ₁σ₀ ∈ B₃,   e₂ = σ₀σ₁σ₀σ₂ ∈ B₄,   …,   eₙ = σ₀σ₁σ₀σ₂⋯σₙ ∈ B_{n+2}.

Each step appends the next generator. That is a Markov stabilisation, so the
closure stays the Hopf link. (The Markov theorem is quoted, not formalised
here.) This file proves the bookkeeping:

* `levelWord_one` — `e₁` is the electron word `σ₀σ₁σ₀`;
* `exponentSum_list_prod` — the writhe of a positive word is its length;
* `writhe_levelWord` — `eₙ` has writhe `n + 2`;
* `shell_eq_writhe_sub_two` — so the level is `n = w − 2`.

For comparison, the backup trefoil reading (`σ^{2n+1}` on `B₂`, used by
`prop:hydrogen-shell-writhe` before the ruling) gives `w = 2n + 1`. The two
readings agree at the ground state `w = 3, n = 1` and differ from `n = 2` on.

-- Ref: [kassel2008] Kassel & Turaev, Braid Groups, §2.5 (Markov's theorem)
-- Ref: docs/coordination/owner-rulings.md (electron word, 2026-11-21)
-/

namespace QOU.BraidKnot.ElectronLevelWord

open QOU.MathlibExt.Braid

/-- The appended generators `σ₂, …, σₙ` of the level-`n` word, in `B_{n+2}`
(generators indexed by `Fin (n+1)`). -/
def tailGens : (n : ℕ) → List (Fin (n + 1))
  | 0 => []
  | 1 => []
  | (k + 2) => (tailGens (k + 1)).map Fin.castSucc ++ [Fin.last (k + 2)]

theorem tailGens_length : ∀ n : ℕ, (tailGens n).length = n - 1
  | 0 => rfl
  | 1 => rfl
  | (k + 2) => by
      simp only [tailGens, List.length_append, List.length_map, List.length_singleton,
        tailGens_length (k + 1)]
      omega

/-- The level-`n` word as a list of generators: `[0, 1, 0, 2, …, n]`. -/
def levelList (n : ℕ) : List (Fin (n + 1)) := [0, 1, 0] ++ tailGens n

/-- The level-`n` electron word `eₙ = σ₀σ₁σ₀σ₂⋯σₙ ∈ B_{n+2}`. -/
def levelWord (n : ℕ) : BraidGroup (n + 1) := ((levelList n).map σ).prod

/-- The ground level is the electron word `σ₀σ₁σ₀ ∈ B₃`. -/
theorem levelWord_one : levelWord 1 = σ 0 * σ 1 * σ 0 := by
  simp [levelWord, levelList, tailGens, mul_assoc]

/-- The writhe of a positive word is its length. -/
theorem exponentSum_list_prod {m : ℕ} (l : List (Fin m)) :
    exponentSum m ((l.map σ).prod) = Multiplicative.ofAdd (l.length : ℤ) := by
  induction l with
  | nil => simp
  | cons a l ih =>
      simp only [List.map_cons, List.prod_cons, map_mul, exponentSum_σ, ih,
        List.length_cons]
      rw [← ofAdd_add]
      congr 1
      push_cast
      ring

/-- **The level-`n` electron word has writhe `n + 2`.** -/
theorem writhe_levelWord (n : ℕ) (hn : 1 ≤ n) :
    exponentSum (n + 1) (levelWord n) = Multiplicative.ofAdd ((n : ℤ) + 2) := by
  rw [levelWord, exponentSum_list_prod]
  congr 1
  simp only [levelList, List.length_append, tailGens_length]
  simp only [List.length_cons, List.length_nil]
  push_cast
  omega

/-- **Shell from writhe, under the ruling.** If the writhe of `eₙ` is `w`, then
`n = w − 2`. -/
theorem shell_eq_writhe_sub_two (n : ℕ) (hn : 1 ≤ n) (w : ℤ)
    (hw : exponentSum (n + 1) (levelWord n) = Multiplicative.ofAdd w) :
    (n : ℤ) = w - 2 := by
  rw [writhe_levelWord n hn] at hw
  have := Multiplicative.ofAdd.injective hw
  omega

end QOU.BraidKnot.ElectronLevelWord
