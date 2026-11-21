import QOU.Mass.GammaGammaWordSelection

/-!
# The H₂ bond over the photon's term alphabet: γγ and U(1)-neutral bonds (issue #8879)

The ruled photon `γ_s(φ) = 1 + φ₀σ_s + φ₁σ_{s+1} + φ₀₁·σ_sσ_{s+1}⁻¹` (owner ruling
2026-11-20) absorbed at the two junction windows `s ∈ {4, 5}` of the twelve-strand `H₂`
word contributes one of five letters: `σ₄, σ₅, σ₆, V₄ = σ₄σ₅⁻¹, V₅ = σ₅σ₆⁻¹`
(`computations/probes/h2_ruled_electron`). This file records two facts about bonds
built from those letters.

**§1. The γγ grammar.** A bond is a γγ-produced word (`GammaGammaWord`) exactly when it
uses only the letters `V₄, V₅` (`bondWord_gammaGamma_iff`). The invariant that excludes the
others is the writhe: every γγ-word has writhe `0` (`writhe_eq_zero`), and a bond's
writhe is its number of `σ` letters (`writhe_bondWord`). In particular `σ₅²`, the cheapest
bond that passes reading 3, is not γγ-produced (`sigma5_sq_not_gammaGamma`).

**§2. U(1) neutrality of the bond alone.** The central U(1) colouring of
`QOU.PhotonU1NeutralCut` (PR #8835), extended to the four junction strands `4…7`: every
component's self-writhe and every pairwise crossing count of the bond's closure vanishes.
The table (`neutral_table`) decides it for the bonds that matter: `V_s`, `V_s²`, `V_s³` are
neutral at both sites; `σ₅²`, `V₅V₄` and `V₅²V₄` are not.

Which of these bonds pass reading 3 is a computation at the proton pin, recorded in the
probe's witness, not here. No numerical value enters this file.

-- Ref: [leitner2026] prop:ilp-covalent-bond; issue #8879; PR #8835
-/

namespace QOU.Molecular.H2BondSelection

open QOU.Mass.GammaGammaWordSelection

/-! ## 1. Bond letters and the γγ grammar -/

/-- The five junction letters (generator indices are those of the twelve-strand word). -/
inductive BondLetter
  | s4 | s5 | s6 | v4 | v5
  deriving DecidableEq, Repr

/-- `true` for the single-crossing letters `σ₄, σ₅, σ₆`. -/
def BondLetter.isSigma : BondLetter → Bool
  | .s4 | .s5 | .s6 => true
  | .v4 | .v5 => false

/-- The braid word of a letter. -/
def BondLetter.word : BondLetter → Word
  | .s4 => [⟨4, true⟩]
  | .s5 => [⟨5, true⟩]
  | .s6 => [⟨6, true⟩]
  | .v4 => vertex 4
  | .v5 => vertex 5

/-- The braid word of a bond: the concatenation of its letters. -/
def bondWord : List BondLetter → Word
  | [] => []
  | x :: l => x.word ++ bondWord l

theorem writhe_letter (x : BondLetter) : writhe x.word = if x.isSigma then 1 else 0 := by
  cases x <;> simp [BondLetter.word, BondLetter.isSigma, writhe, vertex, sign]

/-- **A bond's writhe is its number of `σ` letters.** -/
theorem writhe_bondWord (l : List BondLetter) :
    writhe (bondWord l) = ((l.filter BondLetter.isSigma).length : ℤ) := by
  induction l with
  | nil => simp [bondWord, writhe]
  | cons x l ih =>
      rw [bondWord, writhe_append, ih, writhe_letter]
      cases h : x.isSigma <;> simp [h] <;> ring

/-- **A bond is γγ-produced iff it uses only `V₄` and `V₅`.** -/
theorem bondWord_gammaGamma_iff (l : List BondLetter) :
    GammaGammaWord (bondWord l) ↔ ∀ x ∈ l, x.isSigma = false := by
  constructor
  · intro h x hx
    have hw := writhe_eq_zero h
    rw [writhe_bondWord] at hw
    have hlen : (l.filter BondLetter.isSigma).length = 0 := by exact_mod_cast hw
    rw [List.length_eq_zero_iff, List.filter_eq_nil_iff] at hlen
    simpa using hlen x hx
  · intro h
    induction l with
    | nil => exact GammaGammaWord.nil
    | cons x l ih =>
        have hl : ∀ y ∈ l, y.isSigma = false := fun y hy => h y (List.mem_cons_of_mem _ hy)
        have hx := h x List.mem_cons_self
        cases x <;> simp [BondLetter.isSigma] at hx
        · exact GammaGammaWord.cons 4 (ih hl)
        · exact GammaGammaWord.cons 5 (ih hl)

/-- **`σ₅²` is not a γγ-produced bond** (its writhe is `2`). -/
theorem sigma5_sq_not_gammaGamma : ¬ GammaGammaWord (bondWord [.s5, .s5]) := by
  rw [bondWord_gammaGamma_iff]
  intro h
  simpa [BondLetter.isSigma] using h .s5 List.mem_cons_self

/-! ## 2. U(1) neutrality of the bond on the four junction strands -/

/-- A crossing on the junction strands `4…7`, with local generator index `0, 1, 2`
(`σ₄ ↦ 0`, `σ₅ ↦ 1`, `σ₆ ↦ 2`) and sign `±1`. -/
abbrev Letter := Nat × Int

/-- Swap the labels at positions `i, i+1`. -/
def swapAt (p : List Nat) (i : Nat) : List Nat :=
  (p.set i (p.getD (i + 1) 0)).set (i + 1) (p.getD i 0)

/-- Strand labels after the whole word. -/
def finalPos : List Letter → List Nat → List Nat
  | [], p => p
  | (i, _) :: w, p => finalPos w (swapAt p i)

/-- The closure permutation: the position label `x` ends at. -/
def step (w : List Letter) (x : Nat) : Nat := (finalPos w [0, 1, 2, 3]).idxOf x

/-- The component of the closure containing strand `x`: the least label in its orbit. -/
def comp (w : List Letter) (x : Nat) : Nat :=
  min x (min (step w x) (min (step w (step w x)) (step w (step w (step w x)))))

/-- Signed count of crossings between components `C` and `D` (`C = D`: self-writhe). -/
def cnt (w : List Letter) (C D : Nat) : List Letter → List Nat → Int
  | [], _ => 0
  | (i, e) :: v, p =>
      let x := comp w (p.getD i 0)
      let y := comp w (p.getD (i + 1) 0)
      (if (x = C ∧ y = D) ∨ (x = D ∧ y = C) then e else 0) + cnt w C D v (swapAt p i)

/-- **U(1)-neutral** on four strands: every self-writhe and pairwise crossing count is `0`. -/
def Neutral (w : List Letter) : Prop :=
  ∀ C D : Fin 4, cnt w C D w [0, 1, 2, 3] = 0

instance (w : List Letter) : Decidable (Neutral w) := by unfold Neutral; infer_instance

/-- The local word of a bond letter. -/
def BondLetter.local : BondLetter → List Letter
  | .s4 => [(0, 1)]
  | .s5 => [(1, 1)]
  | .s6 => [(2, 1)]
  | .v4 => [(0, 1), (1, -1)]
  | .v5 => [(1, 1), (2, -1)]

/-- The local word of a bond. -/
def localWord : List BondLetter → List Letter
  | [] => []
  | x :: l => x.local ++ localWord l

/-- **Neutrality table.** `V_s, V_s², V_s³` are neutral at both sites; `σ₅²` (a Hopf clasp),
`V₅V₄` and `V₅²V₄` are not. -/
theorem neutral_table :
    Neutral (localWord [.v4]) ∧ Neutral (localWord [.v5]) ∧
    Neutral (localWord [.v4, .v4]) ∧ Neutral (localWord [.v5, .v5]) ∧
    Neutral (localWord [.v4, .v4, .v4]) ∧ Neutral (localWord [.v5, .v5, .v5]) ∧
    ¬ Neutral (localWord [.s5, .s5]) ∧ ¬ Neutral (localWord [.v5, .v4]) ∧
    ¬ Neutral (localWord [.v5, .v5, .v4]) := by
  decide

end QOU.Molecular.H2BondSelection

