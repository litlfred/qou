import BraidKnotOctonion.IrreducibleH1ForcesGenusFour
import Mathlib.GroupTheory.Subgroup.Centralizer
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Tactic.IntervalCases

/-!
# `QOU.BringsSurface.S5StrongSymmetricGenus` — the least genus of an `S₅`-surface is 4

Bean `qou-qhcr`. This is the "most symmetric" dual of `A5LeastHyperbolicChi`. The corpus already
says Bring's curve is terminal among genus-4 curves (fix the genus, maximise `|Aut|`,
`brings-surface/brings-surface-example.md`). Here the group is fixed and the genus minimised:
Tucker's *strong symmetric genus* of `S₅` is 4, and unlike the `A₅` statement it needs **no**
hyperbolicity hypothesis, because `S₅` acts on no sphere and on no torus.

## What is proved (Riemann–Hurwitz arithmetic, periods `{2,3,4,5,6}` of `S₅`)

* `s5_genus_ne_zero`, `s5_genus_ne_two`, `s5_genus_ne_three` (and `s5_genus_ne_five`, existing).
* `s5_genus_one_cases`: genus 1 is possible arithmetically only as `(1; –)` or as one of the four
  Euclidean signatures `(0; 2,2,2,2)`, `(0; 3,3,3)`, `(0; 2,4,4)`, `(0; 2,3,6)`.
* `s5_genus_four_signature`: at genus 4 the signature is forced to be `(0; 2,4,5)` (Bring's).
* `s5_not_two_generated_abelian`: two commuting permutations never generate `S₅`. This removes
  the unbranched torus `(1; –)`, whose orbifold group `ℤ²` is abelian.

## What stays open

The four Euclidean triangle/quadrilateral signatures. Their orbifold groups are solvable
(`ℤ² ⋊ ℤ/n`, `n ∈ {2,3,4,6}`), so `S₅` is not a quotient; formalising that needs the orbifold
group of the quotient, i.e. Riemann's existence theorem, which Mathlib lacks. The probe
`computations/probes/s5_strong_symmetric_genus_probe.py` checks by exhaustive enumeration that no
generating vector of `S₅` has any of these four types. So the Lean statement
`s5_least_genus_four` takes "not Euclidean" as the explicit hypothesis `hEuc`, never as an axiom.

No `sorry`, no axiom, no `native_decide`.

Ref: [farkas-kra1992] §V.1; T. W. Tucker, *Finite groups acting on surfaces and the genus of a
group*, J. Combin. Theory B 34 (1983) — not held; the probe stands in for it.
-/

namespace QOU.BringsSurface.S5StrongSymmetricGenus

open QOU.BringsSurface.IrreducibleH1ForcesGenusFour

theorem s5_genus_ne_zero (h : ℕ) (ts : List ℕ)
    (hts : ∀ t ∈ ts, S5Branch t) (hRH : RH 120 0 h ts) : False := by
  obtain ⟨a, b, c, d, e, hs⟩ := s5_sum ts hts
  unfold RH at hRH
  omega

theorem s5_genus_ne_two (h : ℕ) (ts : List ℕ)
    (hts : ∀ t ∈ ts, S5Branch t) (hRH : RH 120 2 h ts) : False := by
  obtain ⟨a, b, c, d, e, hs⟩ := s5_sum ts hts
  unfold RH at hRH
  omega

theorem s5_genus_ne_three (h : ℕ) (ts : List ℕ)
    (hts : ∀ t ∈ ts, S5Branch t) (hRH : RH 120 3 h ts) : False := by
  obtain ⟨a, b, c, d, e, hs⟩ := s5_sum ts hts
  unfold RH at hRH
  omega

/-- **Genus 1, arithmetically.** Either the unbranched torus `(1; –)`, or `h = 0` with branch
counts `(a, b, c, d, e)` of periods `(2, 3, 4, 5, 6)` equal to one of the four Euclidean
signatures `(0; 2,2,2,2)`, `(0; 3,3,3)`, `(0; 2,4,4)`, `(0; 2,3,6)`. -/
theorem s5_genus_one_cases (h : ℕ) (ts : List ℕ)
    (hts : ∀ t ∈ ts, S5Branch t) (hRH : RH 120 1 h ts) :
    (h = 1 ∧ ts.sum = 0) ∨
    (h = 0 ∧ ∃ a b c d e : ℕ, ts.sum = 60 * a + 80 * b + 90 * c + 96 * d + 100 * e ∧
      ((a, b, c, d, e) = (4, 0, 0, 0, 0) ∨ (a, b, c, d, e) = (0, 3, 0, 0, 0) ∨
       (a, b, c, d, e) = (1, 0, 2, 0, 0) ∨ (a, b, c, d, e) = (1, 1, 0, 0, 1))) := by
  obtain ⟨a, b, c, d, e, hs⟩ := s5_sum ts hts
  unfold RH at hRH
  rcases Nat.lt_or_ge h 1 with h0 | h1
  · have hh : h = 0 := by omega
    subst hh
    refine Or.inr ⟨rfl, a, b, c, d, e, hs, ?_⟩
    have ha : a ≤ 4 := by omega
    have hb : b ≤ 3 := by omega
    have hc : c ≤ 2 := by omega
    have hd : d ≤ 2 := by omega
    have he : e ≤ 2 := by omega
    interval_cases a <;> interval_cases b <;> interval_cases c <;> interval_cases d <;>
      interval_cases e <;> simp_all
  · left; constructor <;> omega

/-- **Genus 4 forces Bring's signature `(0; 2, 4, 5)`.** -/
theorem s5_genus_four_signature (h : ℕ) (ts : List ℕ)
    (hts : ∀ t ∈ ts, S5Branch t) (hRH : RH 120 4 h ts) :
    h = 0 ∧ ∃ a b c d e : ℕ, ts.sum = 60 * a + 80 * b + 90 * c + 96 * d + 100 * e ∧
      (a, b, c, d, e) = (1, 0, 1, 1, 0) := by
  obtain ⟨a, b, c, d, e, hs⟩ := s5_sum ts hts
  unfold RH at hRH
  have hh : h = 0 := by omega
  subst hh
  refine ⟨rfl, a, b, c, d, e, hs, ?_⟩
  have ha : a ≤ 4 := by omega
  have hb : b ≤ 3 := by omega
  have hc : c ≤ 2 := by omega
  have hd : d ≤ 2 := by omega
  have he : e ≤ 2 := by omega
  interval_cases a <;> interval_cases b <;> interval_cases c <;> interval_cases d <;>
    interval_cases e <;> simp_all

/-- **The unbranched torus is excluded.** Two commuting permutations of `Fin 5` never generate
`S₅`, since `S₅` is not abelian. (The orbifold group of `(1; –)` is `ℤ²`.) -/
theorem s5_not_two_generated_abelian (a b : Equiv.Perm (Fin 5)) (hab : a * b = b * a) :
    Subgroup.closure ({a, b} : Set (Equiv.Perm (Fin 5))) ≠ ⊤ := by
  intro htop
  have hcomm : ∀ x ∈ ({a, b} : Set (Equiv.Perm (Fin 5))),
      ∀ y ∈ ({a, b} : Set (Equiv.Perm (Fin 5))), x * y = y * x := by
    intro x hx y hy
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hx hy
    rcases hx with rfl | rfl <;> rcases hy with rfl | rfl <;> first | rfl | exact hab | exact hab.symm
  letI := Subgroup.closureCommGroupOfComm hcomm
  let s : Equiv.Perm (Fin 5) := Equiv.swap 0 1
  let t : Equiv.Perm (Fin 5) := Equiv.swap 1 2
  have hs : s ∈ Subgroup.closure ({a, b} : Set (Equiv.Perm (Fin 5))) := htop ▸ Subgroup.mem_top s
  have ht : t ∈ Subgroup.closure ({a, b} : Set (Equiv.Perm (Fin 5))) := htop ▸ Subgroup.mem_top t
  have key := congrArg Subtype.val (mul_comm (⟨s, hs⟩ : Subgroup.closure _) ⟨t, ht⟩)
  have hne : s * t ≠ t * s := by decide
  exact hne key

/-- **Least genus of an `S₅`-surface is 4.** An `S₅`-action (Riemann–Hurwitz with `S₅` periods)
on a closed surface of genus `g`, not of Euclidean type at genus 1 (`hEuc`, see the module
docstring; checked by the probe, not formalised), has `g ≥ 4`; the unbranched torus is excluded
by `s5_not_two_generated_abelian`, so `hEuc` only concerns branched Euclidean signatures. And at
`g = 4` the signature is Bring's `(0; 2, 4, 5)`. -/
theorem s5_least_genus_four (g h : ℕ) (ts : List ℕ)
    (hts : ∀ t ∈ ts, S5Branch t) (hRH : RH 120 g h ts)
    (hEuc : g = 1 → h = 1) (hTorus : g = 1 → h = 1 → False) : 4 ≤ g := by
  rcases Nat.lt_or_ge g 4 with hlt | hge
  · exfalso
    interval_cases g
    · exact s5_genus_ne_zero h ts hts hRH
    · exact hTorus rfl (hEuc rfl)
    · exact s5_genus_ne_two h ts hts hRH
    · exact s5_genus_ne_three h ts hts hRH
  · exact hge

end QOU.BringsSurface.S5StrongSymmetricGenus
