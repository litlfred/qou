/-!
# Linking neutrality excludes the climbing family `e₀e₂·Σ₁ᶜ`, `c ≥ 1`

Bean `qou-cds1` (route A, owner choice 2026-11-27). The 2026-11-14 probe
`computations/probes/gg_ntower/gg_scalar_per_step_probe.py` found, exactly over `ℚ(q)`,

    e₀e₂ · Σ₁ = q² · e₀e₂,   Σ₁ = σ₁σ₀σ₂σ₁,   tr_M(e₀e₂ Σ₁ᶜ) = q^{4+2c}/(q²+1)⁴,

with `e_p = (q·1 − σ_p)/(q + q⁻¹)`, and that reading-3 Frobenius positivity passes for every
`c`. So reading 3 cannot fix the magnitude `q^{2c}`. This file asks whether the other half
of the adopted γγ rule, term-by-term **linking neutrality** (owner rulings 2026-11-21 and
2026-11-25), can.

## The argument

Writhe is additive on words, and `Σ₁ᶜ` has writhe `4c`. Expanding
`(q − σ₀)(q − σ₂) = q² − qσ₀ − qσ₂ + σ₀σ₂` gives four words of writhe `0, 1, 1, 2`. So every
braid word in the expansion of `e₀e₂Σ₁ᶜ` has writhe between `4c` and `4c + 2`
(`writhe_support`). A linking-neutral word has writhe `0` (`writhe_eq_zero_of_neutral`: the
writhe is the sum of the ten self-writhe and pairwise crossing counts, all of which vanish).
Hence for `c ≥ 1` no term is neutral (`not_neutral_support`): the term-by-term rule removes
the whole family. The invariant is the writhe homomorphism, so this is a structural
(scope (b)) exclusion.

At `c = 0` the identity word is the only neutral term (`neutral_support_zero`): the rule keeps
only the scalar part `q²·1` of `(q − σ₀)(q − σ₂)`.

## Scope

* Words in the braid group algebra of `B₄`, before any Hecke quotient. The ruling filters
  terms there. In `H₄(q)` the relation `e₀e₂Σ₁ = q²·e₀e₂` makes the excluded element equal
  to a multiple of an admitted one; this file says nothing about the Hecke image. What it
  does say is that the factor `q^{2c}`, `c ≥ 1`, cannot be produced by a neutral braid word.
* Four strands only, with the linking-neutrality definition of
  `QOU.PhotonU1NeutralCut.Neutral` carried from three to four strands.
* The pair-creation vertex `e_p` is not a word of the ruled photon grammar
  `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`; this is a statement about the 2026-11-14 family as
  written, not about that grammar.

Core Lean only, no `sorry`.
-/

namespace QOU.MassTheory.ClimbingFamilyNeutralExclusion

/-- A crossing: generator index (`0`, `1` or `2`) and sign. -/
abbrev Letter := Nat × Int

/-- Swap the strand labels at positions `i` and `i+1`. -/
def swapAt : List Nat → Nat → List Nat
  | a :: b :: r, 0 => b :: a :: r
  | a :: r, i + 1 => a :: swapAt r i
  | p, _ => p

def pairAt (p : List Nat) (i : Nat) : Nat × Nat := (p.getD i 0, p.getD (i + 1) 0)

def finalPos : List Letter → List Nat → List Nat
  | [], p => p
  | (i, _) :: w, p => finalPos w (swapAt p i)

/-- Closure permutation on strand labels. -/
def step (w : List Letter) (x : Nat) : Nat := (finalPos w [0, 1, 2, 3]).idxOf x

/-- Component of the closure containing strand `x`: the least label in its orbit. -/
def comp (w : List Letter) (x : Nat) : Nat :=
  (min x (min (step w x) (min (step w (step w x)) (step w (step w (step w x)))))) % 4

/-- Signed count of crossings between components `C` and `D` (`C = D`: self-writhe). -/
def cnt (w : List Letter) (C D : Nat) : List Letter → List Nat → Int
  | [], _ => 0
  | (i, e) :: v, p =>
      let x := comp w (pairAt p i).1
      let y := comp w (pairAt p i).2
      (if (x = C ∧ y = D) ∨ (x = D ∧ y = C) then e else 0) + cnt w C D v (swapAt p i)

def writhe : List Letter → Int
  | [] => 0
  | (_, e) :: v => e + writhe v

/-- Linking-neutral: every self-writhe and every pairwise crossing count of the closure
vanishes (four strands). -/
def Neutral (w : List Letter) : Prop :=
  ∀ C D : Fin 4, cnt w C D w [0, 1, 2, 3] = 0

instance (w : List Letter) : Decidable (Neutral w) := by unfold Neutral; infer_instance

/-- The ten unordered component pairs. -/
def ten (w v : List Letter) (p : List Nat) : Int :=
  cnt w 0 0 v p + cnt w 0 1 v p + cnt w 0 2 v p + cnt w 0 3 v p +
  cnt w 1 1 v p + cnt w 1 2 v p + cnt w 1 3 v p +
  cnt w 2 2 v p + cnt w 2 3 v p + cnt w 3 3 v p

theorem ind_one (x y : Nat) (hx : x < 4) (hy : y < 4) (e : Int) :
    (if (x = 0 ∧ y = 0) ∨ (x = 0 ∧ y = 0) then e else 0) +
    (if (x = 0 ∧ y = 1) ∨ (x = 1 ∧ y = 0) then e else 0) +
    (if (x = 0 ∧ y = 2) ∨ (x = 2 ∧ y = 0) then e else 0) +
    (if (x = 0 ∧ y = 3) ∨ (x = 3 ∧ y = 0) then e else 0) +
    (if (x = 1 ∧ y = 1) ∨ (x = 1 ∧ y = 1) then e else 0) +
    (if (x = 1 ∧ y = 2) ∨ (x = 2 ∧ y = 1) then e else 0) +
    (if (x = 1 ∧ y = 3) ∨ (x = 3 ∧ y = 1) then e else 0) +
    (if (x = 2 ∧ y = 2) ∨ (x = 2 ∧ y = 2) then e else 0) +
    (if (x = 2 ∧ y = 3) ∨ (x = 3 ∧ y = 2) then e else 0) +
    (if (x = 3 ∧ y = 3) ∨ (x = 3 ∧ y = 3) then e else 0) = e := by
  rcases (by omega : x = 0 ∨ x = 1 ∨ x = 2 ∨ x = 3) with rfl | rfl | rfl | rfl <;>
    rcases (by omega : y = 0 ∨ y = 1 ∨ y = 2 ∨ y = 3) with rfl | rfl | rfl | rfl <;> simp

/-- Every crossing is counted in exactly one of the ten pair counts. -/
theorem writhe_eq_ten (w : List Letter) :
    ∀ (v : List Letter) (p : List Nat), writhe v = ten w v p
  | [], _ => by simp [writhe, ten, cnt]
  | (i, e) :: v, p => by
      have ih := writhe_eq_ten w v (swapAt p i)
      have hx : comp w (pairAt p i).1 < 4 := Nat.mod_lt _ (by decide)
      have hy : comp w (pairAt p i).2 < 4 := Nat.mod_lt _ (by decide)
      have h1 := ind_one _ _ hx hy e
      simp only [ten, cnt, writhe] at *
      omega

/-- **A linking-neutral word has writhe `0`.** -/
theorem writhe_eq_zero_of_neutral (w : List Letter) (h : Neutral w) : writhe w = 0 := by
  rw [writhe_eq_ten w w [0, 1, 2, 3]]
  simp only [ten]
  have := h 0 0; have := h 0 1; have := h 0 2; have := h 0 ⟨3, by decide⟩; have := h 1 1
  have := h 1 2; have := h 1 ⟨3, by decide⟩; have := h 2 2; have := h 2 ⟨3, by decide⟩; have := h ⟨3, by decide⟩ ⟨3, by decide⟩
  simp_all

theorem writhe_append (u v : List Letter) : writhe (u ++ v) = writhe u + writhe v := by
  induction u with
  | nil => simp [writhe]
  | cons a u ih => obtain ⟨i, e⟩ := a; simp [writhe, ih]; omega

/-- `Σ₁ = σ₁σ₀σ₂σ₁`, the cabled crossing exchanging the two singlet pairs. -/
def bigSigma : List Letter := [(1, 1), (0, 1), (2, 1), (1, 1)]

/-- `Σ₁ᶜ` as a word. -/
def climb : Nat → List Letter
  | 0 => []
  | c + 1 => bigSigma ++ climb c

theorem writhe_climb (c : Nat) : writhe (climb c) = 4 * c := by
  induction c with
  | zero => rfl
  | succ c ih => rw [climb, writhe_append, ih]; simp [bigSigma, writhe]; omega

/-- The four words of `(q − σ₀)(q − σ₂) = q² − qσ₀ − qσ₂ + σ₀σ₂`. -/
def jonesWords : List (List Letter) := [[], [(0, 1)], [(2, 1)], [(0, 1), (2, 1)]]

/-- The braid words in the expansion of `e₀e₂·Σ₁ᶜ`. -/
def support (c : Nat) : List (List Letter) := jonesWords.map (· ++ climb c)

theorem writhe_support (c : Nat) :
    ∀ w ∈ support c, 4 * (c : Int) ≤ writhe w ∧ writhe w ≤ 4 * c + 2 := by
  intro w hw
  simp only [support, jonesWords, List.map_cons, List.map_nil, List.mem_cons,
    List.not_mem_nil, or_false] at hw
  rcases hw with rfl | rfl | rfl | rfl <;>
    simp [writhe_climb, writhe] <;> omega

/-- **Route A.** For `c ≥ 1` no braid word in the expansion of `e₀e₂·Σ₁ᶜ` is linking-neutral,
so the term-by-term neutrality rule removes the whole element. -/
theorem not_neutral_support {c : Nat} (hc : 1 ≤ c) : ∀ w ∈ support c, ¬ Neutral w := by
  intro w hw hn
  have h0 := writhe_eq_zero_of_neutral w hn
  have := (writhe_support c w hw).1
  omega

/-- At `c = 0` exactly one term is neutral: the identity word (the scalar `q²`). -/
theorem neutral_support_zero :
    Neutral [] ∧ ¬ Neutral [(0, 1)] ∧ ¬ Neutral [(2, 1)] ∧ ¬ Neutral [(0, 1), (2, 1)] := by
  decide

/-- Control: the neutrality test on four strands does admit a non-trivial neutral word,
`σ₀σ₁⁻¹` (the ruled vertex `V`), and rejects `Σ₁`. -/
theorem controls : Neutral [(0, 1), (1, -1)] ∧ ¬ Neutral bigSigma := by decide

end QOU.MassTheory.ClimbingFamilyNeutralExclusion
