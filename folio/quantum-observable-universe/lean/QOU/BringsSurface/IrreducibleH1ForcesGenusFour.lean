/-!
# `QOU.BringsSurface.IrreducibleH1ForcesGenusFour` — the arithmetic step of the "real route"

Bean `qou-qhcr`. Audit:
`docs/audits/2026-11-17-bring-foundations-trace-sites-and-genus-attack.md` §3.

## The route

Hypothesis (H_W): the icosahedral group `A₅` acts faithfully on the base curve `M₀`, and
`H¹(M₀) ⊗ ℂ = 2W` with `W` an irreducible `A₅`-representation. Then `g = dim W`.
If the action extends to `S₅`, then `g = 4`, and the curve is Bring's.

## What this file proves, and what it takes as hypotheses

It proves the **arithmetic step only**. Three classical inputs are not in Mathlib, so they
enter as explicit hypotheses, never as axioms or `sorry`:

* **Riemann–Hurwitz.** A group of order `n` acting with quotient genus `h` and branch
  orders `mᵢ` gives `2g − 2 = n(2h − 2) + Σᵢ (n − n/mᵢ)`. It is carried as `RH n g h ts`,
  where `ts` lists the integers `n − n/mᵢ`. The branch orders are element orders of the
  group: `{2,3,5}` for `A₅`, giving `ts ⊆ {30,40,48}`, and `{2,3,4,5,6}` for `S₅`,
  giving `ts ⊆ {60,80,90,96,100}`.
  Classical (Farkas–Kra, *Riemann Surfaces*, §V.1); no bibliography entry is held yet.
* **Irreducible dimensions of `A₅`** are `1, 3, 3, 4, 5`. This enters as `hdim`.
  Ref: [fulton-harris1991] Fulton–Harris, *Representation Theory*, §5.1.
* **`g = dim W`** follows from `H¹ ⊗ ℂ = H^{1,0} ⊕ H^{0,1}` of equal dimension `g`.

The audit also computes the whole `H¹` character table for every `A₅` and `S₅` action
(Lefschetz, exact). That finer statement, that `g = 4` and `g = 5` are actually *attained*
with `W` irreducible, is not formalised here. This file only needs the dimensions.

## What remains open

The gaps G2 (lift the `A₅` action from the fibre `CP¹` to the base `M₀`) and G3 (derive
the irreducibility of `H¹`) are untouched. This file shows only that, granted (H_W) and
the `S₅` extension, the genus is 4.
-/

namespace QOU.BringsSurface.IrreducibleH1ForcesGenusFour

/-- Riemann–Hurwitz in `ℕ`, with no subtraction:
`2g − 2 = n(2h − 2) + Σ ts` rearranged as `2g + 2n = 2nh + 2 + Σ ts`. -/
def RH (n g h : Nat) (ts : List Nat) : Prop :=
  2 * g + 2 * n = 2 * n * h + 2 + ts.sum

/-- Branch contributions `n − n/m` of `A₅` (`n = 60`, `m ∈ {2,3,5}`). -/
def A5Branch (t : Nat) : Prop := t = 30 ∨ t = 40 ∨ t = 48

/-- Branch contributions `n − n/m` of `S₅` (`n = 120`, `m ∈ {2,3,4,5,6}`). -/
def S5Branch (t : Nat) : Prop := t = 60 ∨ t = 80 ∨ t = 90 ∨ t = 96 ∨ t = 100

theorem a5_sum (ts : List Nat) (h : ∀ t ∈ ts, A5Branch t) :
    ∃ a b c : Nat, ts.sum = 30 * a + 40 * b + 48 * c := by
  induction ts with
  | nil => exact ⟨0, 0, 0, by simp⟩
  | cons x xs ih =>
    obtain ⟨a, b, c, hs⟩ := ih (fun t ht => h t (by simp [ht]))
    have hx : A5Branch x := h x (by simp)
    rcases hx with rfl | rfl | rfl
    · exact ⟨a + 1, b, c, by simp [List.sum_cons, hs]; omega⟩
    · exact ⟨a, b + 1, c, by simp [List.sum_cons, hs]; omega⟩
    · exact ⟨a, b, c + 1, by simp [List.sum_cons, hs]; omega⟩

theorem s5_sum (ts : List Nat) (h : ∀ t ∈ ts, S5Branch t) :
    ∃ a b c d e : Nat, ts.sum = 60 * a + 80 * b + 90 * c + 96 * d + 100 * e := by
  induction ts with
  | nil => exact ⟨0, 0, 0, 0, 0, by simp⟩
  | cons x xs ih =>
    obtain ⟨a, b, c, d, e, hs⟩ := ih (fun t ht => h t (by simp [ht]))
    have hx : S5Branch x := h x (by simp)
    rcases hx with rfl | rfl | rfl | rfl | rfl
    · exact ⟨a + 1, b, c, d, e, by simp [List.sum_cons, hs]; omega⟩
    · exact ⟨a, b + 1, c, d, e, by simp [List.sum_cons, hs]; omega⟩
    · exact ⟨a, b, c + 1, d, e, by simp [List.sum_cons, hs]; omega⟩
    · exact ⟨a, b, c, d + 1, e, by simp [List.sum_cons, hs]; omega⟩
    · exact ⟨a, b, c, d, e + 1, by simp [List.sum_cons, hs]; omega⟩

/-- `A₅` acts on no curve of genus 2 or 3 (Riemann–Hurwitz arithmetic). -/
theorem a5_genus_ne_two_three (g h : Nat) (ts : List Nat)
    (hts : ∀ t ∈ ts, A5Branch t) (hRH : RH 60 g h ts) : g ≠ 2 ∧ g ≠ 3 := by
  obtain ⟨a, b, c, hs⟩ := a5_sum ts hts
  unfold RH at hRH
  constructor <;> intro hg <;> subst hg <;> omega

/-- `S₅` acts on no curve of genus 5 (Riemann–Hurwitz arithmetic). -/
theorem s5_genus_ne_five (h : Nat) (ts : List Nat)
    (hts : ∀ t ∈ ts, S5Branch t) (hRH : RH 120 5 h ts) : False := by
  obtain ⟨a, b, c, d, e, hs⟩ := s5_sum ts hts
  unfold RH at hRH
  omega

/-- **(H_W) gives `g ∈ {4, 5}`.** `A₅` acts on a curve of genus `g ≥ 2`, and
`H¹ ⊗ ℂ = 2W` with `W` irreducible, so `g = dim W ∈ {1,3,4,5}`. -/
theorem genus_four_or_five_of_A5_irreducible (g h : Nat) (ts : List Nat)
    (hts : ∀ t ∈ ts, A5Branch t) (hRH : RH 60 g h ts) (hg : 2 ≤ g)
    (hdim : g = 1 ∨ g = 3 ∨ g = 4 ∨ g = 5) : g = 4 ∨ g = 5 := by
  have h23 := a5_genus_ne_two_three g h ts hts hRH
  omega

/-- **(H_W) plus an `S₅` action gives `g = 4`.** -/
theorem genus_eq_four_of_A5_irreducible_and_S5
    (g hA hS : Nat) (tsA tsS : List Nat)
    (htsA : ∀ t ∈ tsA, A5Branch t) (hRHA : RH 60 g hA tsA)
    (htsS : ∀ t ∈ tsS, S5Branch t) (hRHS : RH 120 g hS tsS)
    (hg : 2 ≤ g) (hdim : g = 1 ∨ g = 3 ∨ g = 4 ∨ g = 5) : g = 4 := by
  rcases genus_four_or_five_of_A5_irreducible g hA tsA htsA hRHA hg hdim with h4 | h5
  · exact h4
  · subst h5; exact (s5_genus_ne_five hS tsS htsS hRHS).elim

/-- The hypotheses are satisfiable at `g = 4`: `A₅` with signature `(0; 2,5,5)` and `S₅`
with signature `(0; 2,4,5)` (Bring's curve). So the conclusion is not vacuous. -/
theorem genus_four_attained :
    RH 60 4 0 [30, 48, 48] ∧ RH 120 4 0 [60, 90, 96] := by
  unfold RH; decide

end QOU.BringsSurface.IrreducibleH1ForcesGenusFour
