/-!
# Leptons as essential separating curves on the aether surface `Σ₄`

Bean `qou-xtcl` (front `8f-gen`, epic `qou-x08k`): the Seifert-genus filter
`g(T(2,n)) ≤ g(Σ₄) = 4` admits the odd windings `n ∈ {3,5,7,9}`, four of them,
and the corpus had no criterion for dropping `9` that was not unrelated to
generation counting (primality, continuant divisibility).

This file records a refinement of that **same** premise, not a new filter.
Filter 1 reads "the lepton's minimal Seifert surface `F` embeds in the aether
surface `Σ_g`".  Such an `F` has one boundary component, so its boundary `∂F` is a
separating simple closed curve on `Σ_g`, splitting it into `F` (genus `k`) and
its complement (genus `g - k`, one boundary component).

**Refinement (labelled premise, not proved here):** a lepton is topologically
stable on the aether only if `∂F` is *essential*, that is, not null-homotopic
on `Σ_g`.  A null-homotopic curve can be contracted to a point inside the
aether and carries no topological charge there.

**Cited pure-math input (not proved here).** A separating simple closed curve on
a closed orientable surface is null-homotopic if and only if it bounds a disk
(Epstein 1966, *Curves on 2-manifolds and isotopies*, Thm 1.7), and a side with
one boundary component is a disk if and only if its genus is `0`
(classification of surfaces; Farb–Margalit, *A Primer on Mapping Class Groups*,
§1.3).  So `∂F` is essential iff `0 < k` and `0 < g - k`.  This file
formalises everything downstream of that equivalence: it takes the
equivalence as the *definition* `IsEssential` of the side-genus data.

**Results (all sorry-free, no empirical input, core Lean only):**

* `euler_additivity`: the two sides glue to `Σ_g` (`χ = 2 - 2g`).
* `lepton_admissible_iff`: for every genus `g`, the admissible windings are
  exactly `n = 2k + 1` with `1 ≤ k ≤ g - 1`; there are `g - 1` of them
  (`lepton_windings_eq`).
* `bring_lepton_ladder`: at `g = 4` they are exactly `n ∈ {3, 5, 7}`.
* `essential_removes_both_ends`: compared with the genus bound alone, the
  refinement removes exactly `n = 1` (the unknot) and `n = 9` (`T(2,9)`),
  by one criterion: in both cases one side of the curve is a disk.
* `complement_involution`: `k ↦ g - k` preserves essentiality; on the
  `Σ₄` ladder it is `n ↦ 10 - n`, pairing `3 ↔ 7` and fixing `5`.
* `torus_knots_essential_in_bring`: over all torus knots `T(m,n)`,
  `1 < m < n`, coprime, the essential ones are
  `T(2,3), T(2,5), T(2,7), T(3,4)` (the genus-only list also has `T(2,9)`
  and `T(3,5)`, both genus `4`).

**What is NOT established.**  (i) The essentiality premise is a modelling
statement about the aether, labelled as such.  (ii) The count `3 = g - 1` is a
count of *sided* curves (the side is the one carrying the minimal Seifert
surface).  Counted up to the complement involution, essential separating curve
types on `Σ₄` number `⌊g/2⌋ = 2` (`unordered_types_bring`): whether the
electron and the tau are distinct or complementary views of one curve type is
not settled here.  (iii) Why leptons are the two-strand ladder `T(2, 2k+1)`
is the dictionary's premise (`prop:lepton-meson-torus-knot-dictionary`), and
`T(3,4)` (genus 3) also passes the criterion.
-/

namespace QOU.BringsSurface.EssentialSeparatingLeptonCount

/-! ## Separating curves recorded by the genus of the Seifert side -/

/-- A separating simple closed curve on a closed orientable genus-`g` surface,
recorded by the genus `k ≤ g` of the side carrying the Seifert surface; the
other side has genus `g - k`.  Both sides have exactly one boundary
component. -/
structure SeparatingSplit (g : Nat) where
  /-- genus of the Seifert side -/
  k : Nat
  le : k ≤ g

/-- Euler characteristic of a genus-`k` surface with one boundary component. -/
def chiOneBoundary (k : Nat) : Int := 1 - 2 * (k : Int)

/-- Gluing the two sides along the curve (a circle, `χ = 0`) gives `Σ_g`. -/
theorem euler_additivity (g : Nat) (s : SeparatingSplit g) :
    chiOneBoundary s.k + chiOneBoundary (g - s.k) = 2 - 2 * (g : Int) := by
  have h := s.le
  unfold chiOneBoundary
  rw [Int.ofNat_sub h]
  omega

/-- **Essential** (via the cited input in the module docstring): neither side
is a disk, i.e. neither side has genus `0`. -/
def IsEssential (g k : Nat) : Prop := k ≠ 0 ∧ g - k ≠ 0

instance (g k : Nat) : Decidable (IsEssential g k) := by
  unfold IsEssential; infer_instance

theorem isEssential_iff (g k : Nat) : IsEssential g k ↔ 0 < k ∧ k < g := by
  unfold IsEssential; omega

/-! ## The two-strand lepton ladder -/

/-- Seifert genus of `T(2, n)` for odd `n`: `(n - 1) / 2`. -/
def seifertGenusT2 (n : Nat) : Nat := (n - 1) / 2

/-- `T(2,n)` (odd `n`, a knot) passes the genus bound of filter 1:
its minimal Seifert surface fits in `Σ_g`. -/
def GenusAdmissible (g n : Nat) : Prop := n % 2 = 1 ∧ seifertGenusT2 n ≤ g

/-- `T(2,n)` passes filter 1 **and** its Seifert boundary is essential. -/
def LeptonAdmissible (g n : Nat) : Prop :=
  GenusAdmissible g n ∧ IsEssential g (seifertGenusT2 n)

instance (g n : Nat) : Decidable (GenusAdmissible g n) := by
  unfold GenusAdmissible; infer_instance

instance (g n : Nat) : Decidable (LeptonAdmissible g n) := by
  unfold LeptonAdmissible; infer_instance

/-- For every genus `g`: the admissible windings are `n = 2k + 1`,
`1 ≤ k ≤ g - 1`. -/
theorem lepton_admissible_iff (g n : Nat) :
    LeptonAdmissible g n ↔ ∃ k, 1 ≤ k ∧ k + 1 ≤ g ∧ n = 2 * k + 1 := by
  unfold LeptonAdmissible GenusAdmissible IsEssential seifertGenusT2
  constructor
  · rintro ⟨⟨h1, h2⟩, h3, h4⟩
    exact ⟨(n - 1) / 2, by omega, by omega, by omega⟩
  · rintro ⟨k, hk1, hk2, rfl⟩
    omega

/-- Admissible windings below a bound `B`, as a list. -/
def leptonWindings (g B : Nat) : List Nat :=
  (List.range B).filter (fun n => decide (LeptonAdmissible g n))

/-- At `Σ₄` the admissible windings are exactly `3, 5, 7`; nothing above `9`
can pass because the genus bound already fails there. -/
theorem bring_lepton_ladder (n : Nat) :
    LeptonAdmissible 4 n ↔ n = 3 ∨ n = 5 ∨ n = 7 := by
  rw [lepton_admissible_iff]
  constructor
  · rintro ⟨k, h1, h2, rfl⟩; omega
  · rintro (rfl | rfl | rfl)
    · exact ⟨1, by omega, by omega, rfl⟩
    · exact ⟨2, by omega, by omega, rfl⟩
    · exact ⟨3, by omega, by omega, rfl⟩

theorem lepton_windings_bring : leptonWindings 4 20 = [3, 5, 7] := by decide

/-- The count is `g - 1` for every genus (checked as an explicit list for
`g ≤ 6`; the general statement is `lepton_admissible_iff`). -/
theorem lepton_windings_eq :
    leptonWindings 1 30 = [] ∧ leptonWindings 2 30 = [3] ∧
    leptonWindings 3 30 = [3, 5] ∧ leptonWindings 4 30 = [3, 5, 7] ∧
    leptonWindings 5 30 = [3, 5, 7, 9] ∧
    leptonWindings 6 30 = [3, 5, 7, 9, 11] := by decide

/-- The genus bound alone admits the unknot `n = 1` and `n = 3, 5, 7, 9`. -/
theorem genus_bound_alone_bring (n : Nat) :
    GenusAdmissible 4 n ↔ n = 1 ∨ n = 3 ∨ n = 5 ∨ n = 7 ∨ n = 9 := by
  unfold GenusAdmissible seifertGenusT2; omega

/-- Essentiality removes exactly the two ends `n = 1` and `n = 9`; in both
cases one side of the curve is a disk (the Seifert side for `n = 1`, the
complement for `n = 9`). -/
theorem essential_removes_both_ends (n : Nat) :
    (GenusAdmissible 4 n ∧ ¬ LeptonAdmissible 4 n) ↔ n = 1 ∨ n = 9 := by
  rw [genus_bound_alone_bring, bring_lepton_ladder]; omega

/-! ## The complement involution -/

theorem complement_involution (g k : Nat) (hk : k ≤ g) :
    IsEssential g k ↔ IsEssential g (g - k) := by
  unfold IsEssential; omega

/-- On the `Σ₄` ladder, passing to the complementary side sends winding `n`
to `10 - n`: electron `3 ↔ 7` tau, muon `5` fixed. -/
theorem complement_on_bring_ladder (n : Nat) (h : LeptonAdmissible 4 n) :
    LeptonAdmissible 4 (10 - n) ∧ seifertGenusT2 (10 - n) = 4 - seifertGenusT2 n := by
  rw [bring_lepton_ladder] at h
  rcases h with rfl | rfl | rfl <;> decide

/-- Essential sided types on `Σ_g` up to `k ~ g - k`: representatives
`1 ≤ k ≤ g/2`.  At `g = 4` there are `2` (`{1|3}` and `{2|2}`). -/
def unorderedTypes (g : Nat) : List Nat :=
  (List.range (g + 1)).filter (fun k => decide (IsEssential g k ∧ k ≤ g - k))

theorem unordered_types_bring : unorderedTypes 4 = [1, 2] := by decide

/-! ## All torus knots on `Σ₄` -/

/-- Seifert genus of `T(m,n)`: `(m-1)(n-1)/2`. -/
def torusGenus (m n : Nat) : Nat := (m - 1) * (n - 1) / 2

/-- The bounded check as a Boolean: every coprime `1 < m < n < 12` with
`0 < g(T(m,n)) < 4` is one of four knots. -/
def boundedCheck : Bool :=
  (List.range 12).all fun m => (List.range 12).all fun n =>
    !(decide (1 < m ∧ m < n ∧ Nat.gcd m n = 1 ∧ IsEssential 4 (torusGenus m n))) ||
      decide ((m, n) = (2, 3) ∨ (m, n) = (2, 5) ∨ (m, n) = (2, 7) ∨ (m, n) = (3, 4))

theorem boundedCheck_eq : boundedCheck = true := by decide

/-- Bounded enumeration: every coprime `1 < m < n < 12` with
`0 < g(T(m,n)) < 4` is one of four knots. -/
theorem torus_knots_essential_bounded (m n : Nat) (hm12 : m < 12) (hn12 : n < 12)
    (h1 : 1 < m) (h2 : m < n) (h3 : Nat.gcd m n = 1)
    (h4 : IsEssential 4 (torusGenus m n)) :
    (m, n) = (2, 3) ∨ (m, n) = (2, 5) ∨ (m, n) = (2, 7) ∨ (m, n) = (3, 4) := by
  have h := boundedCheck_eq
  unfold boundedCheck at h
  rw [List.all_eq_true] at h
  have hm := h m (List.mem_range.mpr hm12)
  rw [List.all_eq_true] at hm
  have hmn := hm n (List.mem_range.mpr hn12)
  simp only [Bool.or_eq_true, Bool.not_eq_true', decide_eq_false_iff_not,
    decide_eq_true_eq] at hmn
  rcases hmn with hmn | hmn
  · exact absurd ⟨h1, h2, h3, h4⟩ hmn
  · exact hmn

/-- **Torus knots with an essential Seifert boundary on `Σ₄`.** -/
theorem torus_knots_essential_in_bring (m n : Nat) (hm : 1 < m) (hmn : m < n)
    (hcop : Nat.gcd m n = 1) (hE : IsEssential 4 (torusGenus m n)) :
    (m, n) = (2, 3) ∨ (m, n) = (2, 5) ∨ (m, n) = (2, 7) ∨ (m, n) = (3, 4) := by
  have hE' := (isEssential_iff 4 _).mp hE
  unfold torusGenus at hE'
  -- `(m-1)(n-1) ≤ 7`, and each factor is at least `1`.
  have hprod : (m - 1) * (n - 1) ≤ 7 := by omega
  have hn : n - 1 ≤ (m - 1) * (n - 1) := Nat.le_mul_of_pos_left _ (by omega)
  have hm' : m - 1 ≤ (m - 1) * (n - 1) := Nat.le_mul_of_pos_right _ (by omega)
  exact torus_knots_essential_bounded m n (by omega) (by omega) hm hmn hcop hE

end QOU.BringsSurface.EssentialSeparatingLeptonCount
