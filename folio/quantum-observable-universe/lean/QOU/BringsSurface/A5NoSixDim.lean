import Mathlib.GroupTheory.SpecificGroups.Alternating
import Mathlib.Tactic.LinearCombination
import QOU.BringsSurface.CharacterBound

open Equiv QOU.BringsSurface.CharacterBound QOU.BringsSurface.IrreducibleH1ForcesGenusFour

/-!
# `QOU.BringsSurface.A5NoSixDim` — `A₅` has no 6-dimensional irreducible representation

Bean `qou-qhcr`, milestone M4c. With it, the genus theorem needs no input about the
representations of `A₅` at all: `genus_eq_four_of_A5_irreducible` below.

## The argument

Let `V` be an irreducible complex representation of `A₅` with character `χ`, and suppose
`dim V = 6`. Write `x, y, u, v` for `χ` on the classes of a double transposition `t`, a 3-cycle
`c`, a 5-cycle `f` and `f²`, of sizes `15, 20, 12, 12`. For a subgroup `H`,
`Σ_{h ∈ H} χ(h) = |H| · dim V^H` is a multiple of `|H|` (`sum_subgroup_char`). Applied to
`{1, t}`, `⟨c⟩`, the dihedral normaliser `D₅` of `⟨f⟩` and `A₅` itself:

* `6 + x = 2n₁`, `6 + 2y = 3n₂`,
* `6 + 5x + 2u + 2v = 10n₄`, `6 + 15x + 20y + 12u + 12v = 60n₀`.

Orthonormality gives `36 + 15|x|² + 20|y|² + 12|u|² + 12|v|² = 60`, so `15x² ≤ 24` and
`20y² ≤ 24`. Then `x = 0` and `y = 0`, and the last two equations give `60(n₄ − n₀) = 30`,
which has no integer solution.

The facts about `A₅` (class representatives, class sizes, the subgroups and their class
counts) are finite checks done by `decide` in the kernel. There is no `native_decide`.
Ref: [fulton-harris1991] Fulton–Harris, *Representation Theory*, §3.1 (the character table
of `A₅`, which this argument avoids computing).
-/

namespace QOU.BringsSurface.A5NoSixDim

abbrev A5 := alternatingGroup (Fin 5)

def t : A5 := ⟨swap 0 1 * swap 2 3, by rw [Perm.mem_alternatingGroup]; decide⟩
def c : A5 := ⟨swap 0 1 * swap 1 2, by rw [Perm.mem_alternatingGroup]; decide⟩
def f : A5 := ⟨swap 0 1 * swap 1 2 * swap 2 3 * swap 3 4, by rw [Perm.mem_alternatingGroup]; decide⟩

def rep (g : A5) : A5 :=
  if g = 1 then 1 else if g ^ 2 = 1 then t else if g ^ 3 = 1 then c
  else if ∃ h : A5, h * f * h⁻¹ = g then f else f ^ 2

set_option maxRecDepth 100000

theorem rep_conj : ∀ g : A5, ∃ h : A5, h * rep g * h⁻¹ = g := by decide
theorem image_rep : Finset.univ.image rep = {1, t, c, f, f ^ 2} := by decide
theorem card1 : (Finset.univ.filter (fun g => rep g = 1)).card = 1 := by decide
theorem card_t : (Finset.univ.filter (fun g => rep g = t)).card = 15 := by decide
theorem card_c : (Finset.univ.filter (fun g => rep g = c)).card = 20 := by decide
theorem card_f : (Finset.univ.filter (fun g => rep g = f)).card = 12 := by decide
theorem card_f2 : (Finset.univ.filter (fun g => rep g = f ^ 2)).card = 12 := by decide
theorem distinct : (1 : A5) ≠ t ∧ (1:A5) ≠ c ∧ (1:A5) ≠ f ∧ (1:A5) ≠ f^2 ∧ t ≠ c ∧ t ≠ f ∧ t ≠ f^2 ∧ c ≠ f ∧ c ≠ f^2 ∧ f ≠ f^2 := by decide

def D5 : Finset A5 := Finset.univ.filter (fun g => g * f * g⁻¹ = f ∨ g * f * g⁻¹ = f⁻¹)
theorem D5_card : D5.card = 10 := by decide
theorem D5_mul : ∀ a ∈ D5, ∀ b ∈ D5, a * b ∈ D5 := by decide
theorem D5_image : D5.image rep = {1, t, f, f ^ 2} := by decide
theorem D5_t : (D5.filter (fun g => rep g = t)).card = 5 := by decide
theorem D5_f : (D5.filter (fun g => rep g = f)).card = 2 := by decide
theorem D5_f2 : (D5.filter (fun g => rep g = f ^ 2)).card = 2 := by decide

def C2 : Finset A5 := {1, t}
def C3 : Finset A5 := {1, c, c ^ 2}
theorem C2_mul : ∀ a ∈ C2, ∀ b ∈ C2, a * b ∈ C2 := by decide
theorem C3_mul : ∀ a ∈ C3, ∀ b ∈ C3, a * b ∈ C3 := by decide
theorem C2_image : C2.image rep = {1, t} := by decide
theorem C3_image : C3.image rep = {1, c} := by decide
theorem C2_1 : (C2.filter (fun g => rep g = 1)).card = 1 := by decide
theorem C2_t : (C2.filter (fun g => rep g = t)).card = 1 := by decide
theorem C3_1 : (C3.filter (fun g => rep g = 1)).card = 1 := by decide
theorem C3_c : (C3.filter (fun g => rep g = c)).card = 2 := by decide
theorem D5_1 : (D5.filter (fun g => rep g = 1)).card = 1 := by decide
theorem card_A5 : Fintype.card A5 = 60 := by decide

/-- A finite subset closed under multiplication and containing `1` and inverses is a subgroup. -/
def ofFinset (S : Finset A5) (h1 : (1 : A5) ∈ S) (hm : ∀ a ∈ S, ∀ b ∈ S, a * b ∈ S)
    (hi : ∀ a ∈ S, a⁻¹ ∈ S) : Subgroup A5 where
  carrier := {g | g ∈ S}
  one_mem' := h1
  mul_mem' := fun ha hb => hm _ ha _ hb
  inv_mem' := fun ha => hi _ ha

theorem sum_subgroup_char {G : Type} [Group G] (V : FDRep ℂ G) (H : Subgroup G) [Fintype H] :
    ∃ n : ℕ, (∑ h : H, V.character h) = (Fintype.card H : ℂ) * n := by
  let W : FDRep ℂ H := FDRep.of (V.ρ.comp H.subtype)
  haveI : Invertible (Fintype.card H : ℂ) := invertibleOfNonzero (by exact_mod_cast Fintype.card_ne_zero)
  have hav := FDRep.average_char_eq_finrank_invariants W
  have hW : ∀ h : H, W.character h = V.character h := fun h => rfl
  refine ⟨Module.finrank ℂ (Representation.invariants W.ρ), ?_⟩
  rw [← hav]
  simp only [hW, smul_eq_mul, ← mul_assoc, mul_invOf_self, one_mul]

variable (V : FDRep ℂ A5)

theorem char_rep (g : A5) : V.character g = V.character (rep g) := by
  obtain ⟨h, hh⟩ := rep_conj g
  conv_lhs => rw [← hh]
  exact FDRep.char_conj V _ _

theorem sum_rep {M : Type} [AddCommMonoid M] (F : A5 → M) (hF : ∀ g, F g = F (rep g))
    (S : Finset A5) :
    ∑ g ∈ S, F g = ∑ b ∈ S.image rep, (S.filter (fun g => rep g = b)).card • F b := by
  rw [← Finset.sum_comp]; exact Finset.sum_congr rfl (fun g _ => hF g)

/-- The average of `χ` over a subset that is a subgroup is a natural number. -/
theorem sum_finset_nat (S : Finset A5) (h1 : (1 : A5) ∈ S) (hm : ∀ a ∈ S, ∀ b ∈ S, a * b ∈ S)
    (hi : ∀ a ∈ S, a⁻¹ ∈ S) : ∃ n : ℕ, ∑ g ∈ S, V.character g = (S.card : ℂ) * n := by
  let H := ofFinset S h1 hm hi
  letI : Fintype H := Fintype.ofFinset S (fun _ => Iff.rfl)
  obtain ⟨n, hn⟩ := sum_subgroup_char V H
  refine ⟨n, ?_⟩
  rw [Finset.sum_subtype (p := fun g => g ∈ H) S (fun _ => Iff.rfl) (fun g => V.character g), hn]
  congr 2
  exact Fintype.card_ofFinset (p := fun g => g ∈ H) S (fun _ => Iff.rfl)

set_option maxHeartbeats 4000000 in
/-- **M4c.** `A₅` has no 6-dimensional irreducible complex representation. -/
theorem finrank_ne_six [CategoryTheory.Simple V] : Module.finrank ℂ V.V ≠ 6 := by
  intro hd
  have hχ1 : V.character 1 = 6 := by rw [FDRep.char_one, hd]; norm_num
  have hrep := char_rep V
  -- subgroup averages
  obtain ⟨n1, h1⟩ := sum_finset_nat V C2 (by decide) C2_mul (by decide)
  obtain ⟨n2, h2⟩ := sum_finset_nat V C3 (by decide) C3_mul (by decide)
  obtain ⟨n4, h4⟩ := sum_finset_nat V D5 (by decide) D5_mul (by decide)
  obtain ⟨n0, h0⟩ := sum_finset_nat V Finset.univ (Finset.mem_univ _)
    (fun _ _ _ _ => Finset.mem_univ _) (fun _ _ => Finset.mem_univ _)
  rw [sum_rep _ hrep, C2_image, Finset.sum_insert (by decide), Finset.sum_singleton, C2_1, C2_t,
    show C2.card = 2 by decide] at h1
  rw [sum_rep _ hrep, C3_image, Finset.sum_insert (by decide), Finset.sum_singleton, C3_1, C3_c,
    show C3.card = 3 by decide] at h2
  rw [sum_rep _ hrep, D5_image, Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_singleton, D5_1, D5_t, D5_f, D5_f2, D5_card] at h4
  rw [sum_rep _ hrep, image_rep, Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton, card1,
    card_t, card_c, card_f, card_f2, Finset.card_univ, card_A5] at h0
  simp only [nsmul_eq_mul, hχ1] at h1 h2 h4 h0
  push_cast at h1 h2 h4 h0
  -- norm identity
  have hn := sum_normSq_character V
  rw [sum_rep (fun g => Complex.normSq (V.character g)) (fun g => by dsimp only; rw [hrep g]) Finset.univ,
    image_rep, Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton, card1,
    card_t, card_c, card_f, card_f2, card_A5, hχ1] at hn
  simp only [nsmul_eq_mul] at hn
  push_cast at hn
  have hu := Complex.normSq_nonneg (V.character f)
  have hv := Complex.normSq_nonneg (V.character (f ^ 2))
  -- x = 2 n1 - 6, y = (3 n2 - 6)/2, both real
  have hx : V.character t = ((2 * (n1 : ℝ) - 6 : ℝ) : ℂ) := by push_cast; linear_combination h1
  have hy : V.character c = (((3 * (n2 : ℝ) - 6) / 2 : ℝ) : ℂ) := by
    push_cast; linear_combination h2 / 2
  have h6 : Complex.normSq (6 : ℂ) = 36 := by
    rw [show (6 : ℂ) = ((6 : ℝ) : ℂ) by norm_num, Complex.normSq_ofReal]; norm_num
  rw [hx, hy, Complex.normSq_ofReal, Complex.normSq_ofReal, h6] at hn
  have hxr : 15 * ((2 * (n1 : ℝ) - 6) * (2 * (n1 : ℝ) - 6)) ≤ 24 := by
    nlinarith [mul_self_nonneg ((3 * (n2 : ℝ) - 6) / 2)]
  have hyr : 5 * ((3 * (n2 : ℝ) - 6) * (3 * (n2 : ℝ) - 6)) ≤ 24 := by
    nlinarith [mul_self_nonneg (2 * (n1 : ℝ) - 6)]
  have hxi : 15 * ((2 * (n1 : ℤ) - 6) * (2 * (n1 : ℤ) - 6)) ≤ 24 := by exact_mod_cast hxr
  have hyi : 5 * ((3 * (n2 : ℤ) - 6) * (3 * (n2 : ℤ) - 6)) ≤ 24 := by exact_mod_cast hyr
  have hn1 : n1 = 3 := by
    have h1a : 2 * (n1 : ℤ) - 6 ≤ 1 := by nlinarith
    have h1b : -1 ≤ 2 * (n1 : ℤ) - 6 := by nlinarith
    omega
  have hn2 : n2 = 2 := by
    have h2a : 3 * (n2 : ℤ) - 6 ≤ 2 := by nlinarith
    have h2b : -2 ≤ 3 * (n2 : ℤ) - 6 := by nlinarith
    omega
  subst hn1 hn2
  have hx0 : V.character t = 0 := by rw [hx]; norm_num
  have hy0 : V.character c = 0 := by rw [hy]; norm_num
  rw [hx0] at h4
  rw [hx0, hy0] at h0
  have key : ((60 * (n4 : ℤ) - 30 : ℤ) : ℂ) = ((60 * (n0 : ℤ) : ℤ) : ℂ) := by
    push_cast; linear_combination h0 - 6 * h4
  have key' := Int.cast_injective key
  omega

/-- **Genus 4 from (H_W), with nothing assumed about `A₅`'s representations.** `A₅` and
`S₅` act on a curve of genus `g ≥ 2`, and `g = dim W` for an irreducible complex
`A₅`-representation `W`. Then `g = 4`. -/
theorem genus_eq_four_of_A5_irreducible
    (W : FDRep ℂ A5) [CategoryTheory.Simple W]
    (g hA hS : Nat) (tsA tsS : List Nat)
    (htsA : ∀ t ∈ tsA, A5Branch t) (hRHA : RH 60 g hA tsA)
    (htsS : ∀ t ∈ tsS, S5Branch t) (hRHS : RH 120 g hS tsS)
    (hgW : Module.finrank ℂ W.V = g) (hg : 2 ≤ g) : g = 4 :=
  genus_eq_four_of_irreducible A5 card_A5 W g hA hS tsA tsS htsA hRHA htsS hRHS hgW hg
    (finrank_ne_six W)

end QOU.BringsSurface.A5NoSixDim
