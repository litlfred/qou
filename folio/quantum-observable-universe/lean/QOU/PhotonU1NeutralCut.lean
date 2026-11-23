/-!
# U(1)-neutral words of the ruled photon product

The ruled photon is `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (`QOU.Photon`, owner ruling
2026-11-20). Expanding `γ(φ)γ(ψ)` gives twelve non-identity braid words in `B₃`.
This file decides, for each of them, whether it is **U(1)-neutral** in the sense of the
central U(1) colouring of `QEDHigherOrderCovariance` §U: every component's self-writhe
and every pairwise crossing count of its closure vanishes.

Results (all by `decide`, core Lean only, no `sorry`):

* `table`: of the twelve terms, only `V = σ₀σ₁⁻¹` and `V²` are neutral; `σ₀`, `σ₁` and
  the eight mixed bilinears are not. `V³` (the canonical nucleon word `β_Bor`) is neutral.
* `writhe_eq_zero_of_neutral`: a neutral word has total writhe `0`. This is the writhe
  premise that the twist argument needs, obtained here from neutrality rather than
  from a choice of letters.

Scope. This is a statement about braid words and their closures. It does not decide
whether neutrality should be imposed term by term or on the whole product braid;
`QEDHigherOrderCovariance` §P applies the colouring to the braid, not term by term.
Probe: `computations/probes/gg_photon_cut/u1_neutral_cut_probe.py`. Bean `qou-99qc`.
-/

namespace QOU.PhotonU1NeutralCut

/-- A crossing: generator index (0 or 1) and sign. -/
abbrev Letter := Nat × Int

def swapAt (p : List Nat) (i : Nat) : List Nat :=
  match i with
  | 0 => match p with | a :: b :: r => b :: a :: r | _ => p
  | 1 => match p with | a :: b :: c :: r => a :: c :: b :: r | _ => p
  | _ => p

def pairAt (p : List Nat) (i : Nat) : Nat × Nat := (p.getD i 0, p.getD (i+1) 0)

def finalPos : List Letter → List Nat → List Nat
  | [], p => p
  | (i, _) :: w, p => finalPos w (swapAt p i)

/-- Closure permutation on strand labels: the position the label `x` ends at. -/
def step (w : List Letter) (x : Nat) : Nat :=
  ((finalPos w [0,1,2]).idxOf x)

/-- Component of the closure containing strand `x`: the least label in its orbit. -/
def comp (w : List Letter) (x : Nat) : Nat :=
  (min x (min (step w x) (step w (step w x)))) % 3

/-- signed count of crossings whose two strands lie in components {C, D} (C = D: self-writhe). -/
def cnt (w : List Letter) (C D : Nat) : List Letter → List Nat → Int
  | [], _ => 0
  | (i, e) :: v, p =>
      let x := comp w (pairAt p i).1
      let y := comp w (pairAt p i).2
      (if (x = C ∧ y = D) ∨ (x = D ∧ y = C) then e else 0) + cnt w C D v (swapAt p i)

def writhe : List Letter → Int
  | [] => 0
  | (_, e) :: v => e + writhe v

/-- U(1)-neutral: every self-writhe and every pairwise crossing count vanishes. -/
def Neutral (w : List Letter) : Prop :=
  ∀ C D : Fin 3, cnt w C D w [0,1,2] = 0

instance (w : List Letter) : Decidable (Neutral w) := by unfold Neutral; infer_instance

def s0 : List Letter := [(0,1)]
def s1 : List Letter := [(1,1)]
def V : List Letter := [(0,1),(1,-1)]

/-- The twelve non-identity terms of γ(φ)γ(ψ) for the ruled photon. -/
theorem table :
    ¬ Neutral s0 ∧ ¬ Neutral s1 ∧ Neutral V ∧
    ¬ Neutral (s0 ++ s0) ∧ ¬ Neutral (s0 ++ s1) ∧ ¬ Neutral (s1 ++ s0) ∧ ¬ Neutral (s1 ++ s1) ∧
    ¬ Neutral (s0 ++ V) ∧ ¬ Neutral (V ++ s0) ∧ ¬ Neutral (s1 ++ V) ∧ ¬ Neutral (V ++ s1) ∧
    Neutral (V ++ V) ∧ Neutral (V ++ V ++ V) := by decide

/-- Control: the Hopf word σ₀² is not neutral (its two components link). -/
theorem hopf_not_neutral : ¬ Neutral (s0 ++ s0) := by decide

/-- The six unordered component pairs. -/
def six (w : List Letter) (v : List Letter) (p : List Nat) : Int :=
  cnt w 0 0 v p + cnt w 0 1 v p + cnt w 0 2 v p + cnt w 1 1 v p + cnt w 1 2 v p + cnt w 2 2 v p

theorem ind_one (x y : Nat) (hx : x < 3) (hy : y < 3) (e : Int) :
    (if (x = 0 ∧ y = 0) ∨ (x = 0 ∧ y = 0) then e else 0) +
    (if (x = 0 ∧ y = 1) ∨ (x = 1 ∧ y = 0) then e else 0) +
    (if (x = 0 ∧ y = 2) ∨ (x = 2 ∧ y = 0) then e else 0) +
    (if (x = 1 ∧ y = 1) ∨ (x = 1 ∧ y = 1) then e else 0) +
    (if (x = 1 ∧ y = 2) ∨ (x = 2 ∧ y = 1) then e else 0) +
    (if (x = 2 ∧ y = 2) ∨ (x = 2 ∧ y = 2) then e else 0) = e := by
  rcases (by omega : x = 0 ∨ x = 1 ∨ x = 2) with rfl | rfl | rfl <;>
    rcases (by omega : y = 0 ∨ y = 1 ∨ y = 2) with rfl | rfl | rfl <;> simp

/-- Every crossing is counted in exactly one of the six pair counts, so they sum to the writhe. -/
theorem writhe_eq_six (w : List Letter) : ∀ (v : List Letter) (p : List Nat), writhe v = six w v p
  | [], _ => by simp [writhe, six, cnt]
  | (i, e) :: v, p => by
      have ih := writhe_eq_six w v (swapAt p i)
      have hx : comp w (pairAt p i).1 < 3 := Nat.mod_lt _ (by decide)
      have hy : comp w (pairAt p i).2 < 3 := Nat.mod_lt _ (by decide)
      have h1 := ind_one _ _ hx hy e
      simp only [six, cnt, writhe] at *
      omega

/-- **A U(1)-neutral word has writhe 0.** -/
theorem writhe_eq_zero_of_neutral (w : List Letter) (h : Neutral w) : writhe w = 0 := by
  rw [writhe_eq_six w w [0,1,2]]
  simp only [six]
  have := h 0 0; have := h 0 1; have := h 0 2; have := h 1 1; have := h 1 2; have := h 2 2
  simp_all

end QOU.PhotonU1NeutralCut
