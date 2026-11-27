/-!
# Six strands: a linking-neutral photon term is a word in the vertices `V_i`

Bean `qou-cds1`. The six-strand photon grammar has four photon factors, one per adjacent
pair of generators,

    γ_i = 1 + φ₀·σ_i + φ₁·σ_{i+1} + φ₀₁·σ_iσ_{i+1}⁻¹,    i = 0, 1, 2, 3,

in `B₆` (generators `σ₀ … σ₄`). The fourth term is the chiral vertex
`V_i = σ_iσ_{i+1}⁻¹`, never `σ_iσ_{i+1}` (owner ruling 2026-11-20). Expanding a product
`γ_{i₁} ⋯ γ_{i_m}` gives one braid word per choice of a term in each factor. This file proves:

* `vword_of_neutral`: **if such a term is linking-neutral, every factor contributed `1` or
  `V_i`, so the term is a word in the `V_i`.**

## The argument

Generalises `QOU.Mass.GammaGammaNeutralSelectionAllN.eq_vertexPow_of_writhe_zero` (three
strands) and the four-strand neutrality of `QOU.MassTheory.ClimbingFamilyNeutralExclusion`.

1. Writhe is the sum over the 21 unordered component pairs `{C, D}`, `0 ≤ C ≤ D < 6`, of the
   signed crossing count between them (`writhe_eq_psum`): each crossing lies in exactly one
   pair (`indSum_pairs6`).
2. Linking-neutral means every one of those 21 counts vanishes, so a neutral word has
   writhe `0` (`writhe_eq_zero_of_neutral`).
3. A term's writhe is the number of factors that contributed `σ_i` or `σ_{i+1}`, because `1`
   and `V_i` have writhe `0` (`writhe_termWord`). So writhe `0` forces every choice to be
   `1` or `V_i` (`vword_of_writhe_zero`).

## Scope

* Words, before any Hecke quotient and before free reduction. The coefficients `φ` play no
  role: the statement is about which braid words occur, so it holds over any coefficient
  ring.
* Only the "only if" direction. The converse fails on six strands: `V₀V₁` is a V-word and
  is **not** neutral (`v0v1_not_neutral`), because `σ₁⁻¹σ₁` cancels and leaves `σ₀σ₂⁻¹`,
  whose two components have self-writhe `+1` and `−1`. So neutrality is strictly finer than
  "word in the `V_i`".
* Six strands, with the neutrality test of `QOU.PhotonU1NeutralCut.Neutral` carried from
  three to six strands (orbit minimum over six iterates of the closure permutation).

Core Lean only, no `sorry`.
-/

namespace QOU.MassTheory.SixStrandNeutralVWord

/-- A crossing: generator index (`0 … 4`) and sign. -/
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

/-- The six strand labels. -/
def start : List Nat := [0, 1, 2, 3, 4, 5]

/-- Closure permutation on strand labels. -/
def step (w : List Letter) (x : Nat) : Nat := (finalPos w start).idxOf x

/-- Least label among `x` and its next `k` images under `step`. -/
def orbitMin (w : List Letter) : Nat → Nat → Nat
  | 0, x => x
  | k + 1, x => min x (orbitMin w k (step w x))

/-- Component of the closure containing strand `x`: the least label in its orbit. -/
def comp (w : List Letter) (x : Nat) : Nat := orbitMin w 5 x % 6

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

theorem writhe_append (u v : List Letter) : writhe (u ++ v) = writhe u + writhe v := by
  induction u with
  | nil => simp [writhe]
  | cons a u ih => obtain ⟨i, e⟩ := a; simp [writhe, ih]; omega

/-- Linking-neutral: every self-writhe and every pairwise crossing count of the closure
vanishes (six strands). -/
def Neutral (w : List Letter) : Prop :=
  ∀ C D : Fin 6, cnt w C D w start = 0

instance (w : List Letter) : Decidable (Neutral w) := by unfold Neutral; infer_instance

/-! ## Writhe is the sum of the 21 pair counts -/

/-- The 21 unordered component pairs `C ≤ D < 6`. -/
def pairs6 : List (Nat × Nat) :=
  [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,1),(1,2),(1,3),(1,4),(1,5),
   (2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)]

theorem pairs6_length : pairs6.length = 21 := rfl

/-- Sum of the pair counts over a list of pairs. -/
def psum (w : List Letter) (v : List Letter) (p : List Nat) : List (Nat × Nat) → Int
  | [] => 0
  | (C, D) :: L => cnt w C D v p + psum w v p L

/-- Sum of the crossing indicators over a list of pairs. -/
def indSum (x y : Nat) (e : Int) : List (Nat × Nat) → Int
  | [] => 0
  | (C, D) :: L => (if (x = C ∧ y = D) ∨ (x = D ∧ y = C) then e else 0) + indSum x y e L

/-- Each crossing lies in exactly one of the 21 pairs. -/
theorem indSum_pairs6 (x y : Nat) (hx : x < 6) (hy : y < 6) (e : Int) :
    indSum x y e pairs6 = e := by
  rcases (by omega : x = 0 ∨ x = 1 ∨ x = 2 ∨ x = 3 ∨ x = 4 ∨ x = 5) with
      rfl | rfl | rfl | rfl | rfl | rfl <;>
    rcases (by omega : y = 0 ∨ y = 1 ∨ y = 2 ∨ y = 3 ∨ y = 4 ∨ y = 5) with
      rfl | rfl | rfl | rfl | rfl | rfl <;>
    simp [indSum, pairs6]

theorem psum_cons (w v : List Letter) (i : Nat) (e : Int) (p : List Nat) :
    ∀ L : List (Nat × Nat),
      psum w ((i, e) :: v) p L =
        indSum (comp w (pairAt p i).1) (comp w (pairAt p i).2) e L + psum w v (swapAt p i) L
  | [] => by simp [psum, indSum]
  | (C, D) :: L => by
      have ih := psum_cons w v i e p L
      simp only [psum, indSum, cnt] at *
      omega

theorem psum_nil (w : List Letter) (p : List Nat) :
    ∀ L : List (Nat × Nat), psum w [] p L = 0
  | [] => rfl
  | (C, D) :: L => by simp [psum, cnt, psum_nil w p L]

/-- **Writhe is the sum of the 21 pair counts.** -/
theorem writhe_eq_psum (w : List Letter) :
    ∀ (v : List Letter) (p : List Nat), writhe v = psum w v p pairs6
  | [], p => by rw [psum_nil]; rfl
  | (i, e) :: v, p => by
      have hx : comp w (pairAt p i).1 < 6 := Nat.mod_lt _ (by decide)
      have hy : comp w (pairAt p i).2 < 6 := Nat.mod_lt _ (by decide)
      rw [psum_cons, indSum_pairs6 _ _ hx hy, ← writhe_eq_psum w v (swapAt p i)]
      rfl

theorem psum_eq_zero_of_neutral (w : List Letter) (h : Neutral w) :
    ∀ L : List (Nat × Nat), (∀ cd ∈ L, cd.1 < 6 ∧ cd.2 < 6) → psum w w start L = 0
  | [], _ => rfl
  | (C, D) :: L, hL => by
      have hCD := hL (C, D) (List.mem_cons_self ..)
      have h0 : cnt w C D w start = 0 := h ⟨C, hCD.1⟩ ⟨D, hCD.2⟩
      have ih := psum_eq_zero_of_neutral w h L (fun cd hcd => hL cd (List.mem_cons_of_mem _ hcd))
      simp only [psum, h0, ih]; rfl

/-- **A linking-neutral six-strand word has writhe `0`.** -/
theorem writhe_eq_zero_of_neutral (w : List Letter) (h : Neutral w) : writhe w = 0 := by
  rw [writhe_eq_psum w w start]
  exact psum_eq_zero_of_neutral w h pairs6 (by decide)

/-! ## The six-strand photon grammar -/

/-- Generator `σ_j`. -/
def sig (j : Nat) : List Letter := [(j, 1)]

/-- The vertex `V_i = σ_iσ_{i+1}⁻¹`. -/
def V (i : Nat) : List Letter := [(i, 1), (i + 1, -1)]

/-- The four terms of `γ_i`, in order: `1`, `σ_i`, `σ_{i+1}`, `σ_iσ_{i+1}⁻¹`. -/
def photonTerm (i : Fin 4) : Fin 4 → List Letter
  | 0 => []
  | 1 => sig i
  | 2 => sig (i + 1)
  | 3 => V i

/-- A term of the expansion of `γ_{i₁} ⋯ γ_{i_m}`: a factor index and a term choice per
factor. Its braid word is the concatenation. -/
def termWord : List (Fin 4 × Fin 4) → List Letter
  | [] => []
  | (i, c) :: t => photonTerm i c ++ termWord t

/-- The terms `1` and `V_i` are the writhe-0 choices. -/
def IsVChoice (c : Fin 4) : Prop := c = 0 ∨ c = 3

instance (c : Fin 4) : Decidable (IsVChoice c) := by unfold IsVChoice; infer_instance

/-- Number of factors that contributed `σ_i` or `σ_{i+1}`. -/
def sigCount : List (Fin 4 × Fin 4) → Nat
  | [] => 0
  | (_, c) :: t => (if IsVChoice c then 0 else 1) + sigCount t

theorem writhe_photonTerm (i c : Fin 4) :
    writhe (photonTerm i c) = if IsVChoice c then 0 else 1 := by
  match c with
  | 0 => rfl
  | 1 => simp [photonTerm, sig, writhe, IsVChoice]
  | 2 => simp [photonTerm, sig, writhe, IsVChoice]
  | 3 => simp [photonTerm, V, writhe, IsVChoice]

/-- **The writhe of a photon term counts its `σ` factors.** -/
theorem writhe_termWord (t : List (Fin 4 × Fin 4)) : writhe (termWord t) = sigCount t := by
  induction t with
  | nil => rfl
  | cons a t ih =>
    obtain ⟨i, c⟩ := a
    rw [termWord, writhe_append, ih, writhe_photonTerm, sigCount]
    split <;> simp

/-- The V-word of a list of vertex indices. -/
def vword : List (Fin 4) → List Letter
  | [] => []
  | i :: l => V i ++ vword l

/-- Writhe `0` forces every factor to contribute `1` or `V_i`, and the term is then the
V-word of the factors that contributed `V_i`. -/
theorem vword_of_writhe_zero (t : List (Fin 4 × Fin 4)) (h : writhe (termWord t) = 0) :
    (∀ a ∈ t, IsVChoice a.2) ∧
      termWord t = vword ((t.filter (fun a => a.2 = 3)).map Prod.fst) := by
  rw [writhe_termWord] at h
  have hc : sigCount t = 0 := by exact_mod_cast h
  clear h
  induction t with
  | nil => exact ⟨by simp, rfl⟩
  | cons a t ih =>
    obtain ⟨i, c⟩ := a
    simp only [sigCount] at hc
    have hv : IsVChoice c := by
      refine Decidable.byContradiction fun hn => ?_
      simp [hn] at hc
    have ht : sigCount t = 0 := by simp [hv] at hc; exact hc
    obtain ⟨hall, hw⟩ := ih ht
    refine ⟨?_, ?_⟩
    · intro b hb
      rcases List.mem_cons.1 hb with rfl | hb
      · exact hv
      · exact hall b hb
    · rcases hv with rfl | rfl
      · simp [termWord, photonTerm, hw]
      · simp [termWord, photonTerm, hw, vword]

/-- **Six strands: a linking-neutral term of the photon grammar is a word in the
`V_i = σ_iσ_{i+1}⁻¹`.** Every factor `γ_i` contributed `1` or `V_i`; none contributed
`σ_i` or `σ_{i+1}`. -/
theorem vword_of_neutral (t : List (Fin 4 × Fin 4)) (h : Neutral (termWord t)) :
    (∀ a ∈ t, IsVChoice a.2) ∧
      termWord t = vword ((t.filter (fun a => a.2 = 3)).map Prod.fst) :=
  vword_of_writhe_zero t (writhe_eq_zero_of_neutral _ h)

/-- Existential form. -/
theorem exists_vword_of_neutral (t : List (Fin 4 × Fin 4)) (h : Neutral (termWord t)) :
    ∃ l : List (Fin 4), termWord t = vword l :=
  ⟨_, (vword_of_neutral t h).2⟩

/-! ## Controls -/

/-- Each single vertex `V_i` is neutral, and each single generator is not. -/
theorem controls_single :
    Neutral (V 0) ∧ Neutral (V 1) ∧ Neutral (V 2) ∧ Neutral (V 3) ∧
    ¬ Neutral (sig 0) ∧ ¬ Neutral (sig 1) ∧ ¬ Neutral (sig 2) ∧ ¬ Neutral (sig 3) ∧
    ¬ Neutral (sig 4) := by decide

/-- Disjoint vertices stay neutral; the converse of `vword_of_neutral` fails at `V₀V₁`. -/
theorem v0v3_neutral : Neutral (V 0 ++ V 3) := by decide

theorem v0v1_not_neutral : ¬ Neutral (V 0 ++ V 1) := by decide

/-- The old fourth term `σ_iσ_{i+1}` is not neutral (it has writhe `2`). -/
theorem old_form_not_neutral : ¬ Neutral (sig 0 ++ sig 1) := by decide

end QOU.MassTheory.SixStrandNeutralVWord
