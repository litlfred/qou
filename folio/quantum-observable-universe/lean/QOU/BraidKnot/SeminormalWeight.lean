/-
# Seminormal weights — the `a_ρ = h/(1 − q^{−2ρ})` sum infrastructure

Foundational Mathlib-gap infra for the **Young seminormal character sum** that the
corpus repeatedly cites as *"not in Mathlib"* (e.g. `symbolic_character_table`,
`QHeckeSeminormalCharacterClosure`). Mathlib carries `YoungDiagram` and
`SemistandardTableau` but **no** standard-tableau seminormal representation, so
the single-generator character

  χ_λ(σ) = Σ_{T ∈ SYT(λ)}  a_{ρ(T)},        a_ρ = h / (1 − q^{−2ρ}),  h = q − q⁻¹

has no home. This file supplies the **weight layer** (bean `qou-mcbf`, Infra 2):
the reduced weight `g_ρ = 1/(1 − q^{−2ρ})`, the factorisation `a_ρ = h · g_ρ`
(the algebraic *source* of the `· h` in the closed form `χ_λ(σ) = c_λ · h`), and
the **pairing identity** `g_ρ + g_{−ρ} = 1` — the structural fact that makes a sum
of reduced weights over a ρ ↔ −ρ symmetric tableau set an **integer** `c_λ`.

Base ring (§7c): pure algebra over a generic `[Field R]` with `q ≠ 0` — no
archimedean structure (`Real.sqrt`, ordering) is used, so this is *not* `ℝ`-locked.
The `q₀`-evaluation lives downstream, past the substrate→archimedean wall.

-- Ref: [sagan2001] The Symmetric Group, §3.3 (Young's seminormal form)
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/symbolic-character-table.md
-/
import Mathlib.Tactic

namespace QOU.BraidKnot.SeminormalWeight

variable {R : Type*} [Field R]

/-- **Reduced seminormal weight** `g_ρ = 1/(1 − q^{−2ρ})` — the dimensionless part
    of the axial-distance weight, `ρ : ℤ` the axial distance between the boxes
    holding `i` and `i+1` in a standard tableau. -/
noncomputable def reducedWeight (q : R) (ρ : ℤ) : R := (1 - q ^ (-2 * ρ))⁻¹

/-- **Seminormal weight** `a_ρ = h / (1 − q^{−2ρ})`, `h = q − q⁻¹` the Hecke
    parameter (AGENTS.md §7a). -/
noncomputable def seminormalWeight (q h : R) (ρ : ℤ) : R := h * reducedWeight q ρ

/-- **The `h` factors out.** `a_ρ = h · g_ρ`. This is the algebraic source of the
    `· h` in the character closed form `χ_λ(σ) = c_λ · h`: every summand carries a
    single factor of `h`, so the whole character does. -/
theorem seminormalWeight_eq_h_mul (q h : R) (ρ : ℤ) :
    seminormalWeight q h ρ = h * reducedWeight q ρ := rfl

/-- **Character sum factors out `h`.** The single-generator seminormal character
    is a sum of weights `Σ_{t ∈ S} a_{ρ(t)}` over the standard-tableau index set
    `S`; `h` pulls out of the whole sum: `χ_λ(σ) = h · Σ_t g_{ρ(t)}`. Together with
    `Σ_t g_{ρ(t)} = c_λ ∈ ℤ` (the reduced-weight sum over the swap-symmetric SYT
    set — an integer by the pairing identity `reducedWeight_add_neg`) this is the
    closed form `χ_λ(σ) = c_λ · h`. The `h`-linearity of the whole table is thus
    reduced to a purely *integer* combinatorial statement about the reduced sum. -/
theorem characterSum_eq_h_mul {ι : Type*} (q h : R) (S : Finset ι) (ρ : ι → ℤ) :
    (∑ t ∈ S, seminormalWeight q h (ρ t)) = h * ∑ t ∈ S, reducedWeight q (ρ t) := by
  simp only [seminormalWeight, Finset.mul_sum]

/-- Rewriting `q^{−2ρ}` as `(q^{2ρ})⁻¹`. -/
theorem reducedWeight_eq (q : R) (ρ : ℤ) :
    reducedWeight q ρ = (1 - (q ^ (2 * ρ))⁻¹)⁻¹ := by
  unfold reducedWeight
  rw [show (-2 * ρ) = -(2 * ρ) by ring, zpow_neg]

/-- **The pairing identity** `g_ρ + g_{−ρ} = 1`.

    With `x = q^{2ρ}`: `g_ρ = (1 − x⁻¹)⁻¹ = x/(x−1)` and `g_{−ρ} = (1 − x)⁻¹ =
    −1/(x−1)`, so the sum telescopes to `1`. This is *why* a reduced-weight sum
    over a ρ ↔ −ρ symmetric standard-tableau set is an **integer** `c_λ`: the
    off-diagonal boxes pair up, each pair contributing `1`. Hypotheses: `q ≠ 0`
    (so `zpow` inverts) and `q^{2ρ} ≠ 1` (so no box sits on the diagonal, i.e.
    `i, i+1` are neither same-row nor same-column). -/
theorem reducedWeight_add_neg (q : R) (ρ : ℤ) (hq : q ≠ 0)
    (hx : q ^ (2 * ρ) ≠ 1) :
    reducedWeight q ρ + reducedWeight q (-ρ) = 1 := by
  rw [reducedWeight_eq, show reducedWeight q (-ρ) = (1 - q ^ (2 * ρ))⁻¹ by
        unfold reducedWeight; rw [show (-2 * -ρ) = 2 * ρ by ring]]
  set x := q ^ (2 * ρ) with hxdef
  have hx0 : x ≠ 0 := zpow_ne_zero _ hq
  clear_value x
  have hxinv : x⁻¹ ≠ 1 := fun h => hx (inv_eq_one.mp h)
  have h2 : (1 : R) - x⁻¹ ≠ 0 := sub_ne_zero.mpr (Ne.symm hxinv)
  have hx1 : x - 1 ≠ 0 := sub_ne_zero.mpr hx
  have A : (1 - x⁻¹)⁻¹ = x / (x - 1) := by
    have hnum : 1 - x⁻¹ = (x - 1) / x := by field_simp
    rw [hnum, inv_div]
  have B : (1 - x)⁻¹ = -(1 / (x - 1)) := by
    rw [show (1 : R) - x = -(x - 1) by ring, ← neg_inv, one_div]
  rw [A, B]
  field_simp
  ring

/-- **Integer content `c_λ = 1` — the two-tableau base case.** When the SYT set is
    a single swap-pair `{a, b}` with `ρ(b) = −ρ(a)` (one off-diagonal box pair, the
    boxes exchanged by the `i ↔ i+1` transposition), the reduced-weight sum is `1`.
    The base case of `Σ g_ρ = c_λ ∈ ℤ`, provable directly from the pairing identity
    (no general involution reindex). -/
theorem reducedSum_pair {ι : Type*} [DecidableEq ι] (q : R) (a b : ι) (hab : a ≠ b)
    (ρ : ι → ℤ) (hρ : ρ b = -ρ a) (hq : q ≠ 0) (hnd : q ^ (2 * ρ a) ≠ 1) :
    ∑ t ∈ ({a, b} : Finset ι), reducedWeight q (ρ t) = 1 := by
  rw [Finset.sum_pair hab, hρ]
  exact reducedWeight_add_neg q (ρ a) hq hnd

/-- **`χ_λ(σ) = c_λ · h` end-to-end for a two-tableau partition (`c_λ = 1`).**
    Composes `characterSum_eq_h_mul` (h factors out) with `reducedSum_pair`
    (the reduced sum is the integer `1`): the single-generator seminormal character
    over a one-pair SYT set is exactly `h`. This is the full closed form realised on
    the base case — the weight + geometry layers deliver `χ = c_λ·h` with no
    outstanding `sorry`. -/
theorem characterSum_pair {ι : Type*} [DecidableEq ι] (q h : R) (a b : ι) (hab : a ≠ b)
    (ρ : ι → ℤ) (hρ : ρ b = -ρ a) (hq : q ≠ 0) (hnd : q ^ (2 * ρ a) ≠ 1) :
    ∑ t ∈ ({a, b} : Finset ι), seminormalWeight q h (ρ t) = h := by
  rw [characterSum_eq_h_mul, reducedSum_pair q a b hab ρ hρ hq hnd, mul_one]

/-- **The reduced-weight sum is `|S|/2` — the integer content `c_λ` (general).**
    If the SYT index set `S` carries a fixed-point-free involution `τ` that negates
    the axial distance (`ρ(τ t) = −ρ t` — the `i ↔ i+1` transposition swapping the
    two boxes, which negates `ρ` by `TableauContent.axialDistance_antisymm`), then
    `2·Σ_t g_{ρ(t)} = |S|`: each τ-pair contributes `g_ρ + g_{−ρ} = 1`, so the sum
    is the pair count `|S|/2 ∈ ℤ`. The proof reindexes `∑ g_{−ρ t}` by `τ` (via
    `Finset.sum_image` over the involution) into `∑ g_{ρ t}`, then applies the
    pairing identity termwise. This is the **integer content** `c_λ`. -/
theorem two_mul_reducedSum_eq_card {ι : Type*} [DecidableEq ι] (q : R) (S : Finset ι)
    (ρ : ι → ℤ) (τ : ι → ι) (hτS : ∀ t ∈ S, τ t ∈ S) (hττ : ∀ t ∈ S, τ (τ t) = t)
    (hρτ : ∀ t ∈ S, ρ (τ t) = -ρ t) (hq : q ≠ 0)
    (hnd : ∀ t ∈ S, q ^ (2 * ρ t) ≠ 1) :
    (2 : R) * ∑ t ∈ S, reducedWeight q (ρ t) = (S.card : R) := by
  have reindex : (∑ t ∈ S, reducedWeight q (-ρ t)) = ∑ t ∈ S, reducedWeight q (ρ t) := by
    have hinj : ∀ x ∈ S, ∀ y ∈ S, τ x = τ y → x = y := by
      intro x hx y hy h
      have h2 := congrArg τ h; rwa [hττ x hx, hττ y hy] at h2
    have himg : S.image τ = S := by
      apply Finset.Subset.antisymm
      · intro b hb; rw [Finset.mem_image] at hb; obtain ⟨a, ha, rfl⟩ := hb; exact hτS a ha
      · intro b hb; rw [Finset.mem_image]; exact ⟨τ b, hτS b hb, hττ b hb⟩
    calc (∑ t ∈ S, reducedWeight q (-ρ t))
        = ∑ t ∈ S, reducedWeight q (ρ (τ t)) :=
          Finset.sum_congr rfl (fun t ht => by rw [hρτ t ht])
      _ = ∑ t ∈ S.image τ, reducedWeight q (ρ t) :=
          (Finset.sum_image (f := fun t => reducedWeight q (ρ t)) hinj).symm
      _ = ∑ t ∈ S, reducedWeight q (ρ t) := by rw [himg]
  have pair : ∀ t ∈ S, reducedWeight q (ρ t) + reducedWeight q (-ρ t) = 1 :=
    fun t ht => reducedWeight_add_neg q (ρ t) hq (hnd t ht)
  calc (2 : R) * ∑ t ∈ S, reducedWeight q (ρ t)
      = (∑ t ∈ S, reducedWeight q (ρ t)) + ∑ t ∈ S, reducedWeight q (ρ t) := by ring
    _ = (∑ t ∈ S, reducedWeight q (ρ t)) + ∑ t ∈ S, reducedWeight q (-ρ t) := by rw [reindex]
    _ = ∑ t ∈ S, (reducedWeight q (ρ t) + reducedWeight q (-ρ t)) := by
          rw [Finset.sum_add_distrib]
    _ = ∑ _t ∈ S, (1 : R) := Finset.sum_congr rfl pair
    _ = (S.card : R) := by rw [Finset.sum_const, nsmul_eq_mul, mul_one]

/-- **`2·χ_λ(σ) = |S|·h` — the general closed form `χ_λ(σ) = c_λ·h`, `c_λ = |S|/2`.**
    The single-generator seminormal character over a standard-tableau set `S`
    carrying the `i ↔ i+1` swap involution is `c_λ·h` with `c_λ = |S|/2 ∈ ℤ`.
    Composes `characterSum_eq_h_mul` (h factors out) with `two_mul_reducedSum_eq_card`
    (the reduced sum is the integer `|S|/2`). No `sorry`. -/
theorem two_mul_characterSum_eq {ι : Type*} [DecidableEq ι] (q h : R) (S : Finset ι)
    (ρ : ι → ℤ) (τ : ι → ι) (hτS : ∀ t ∈ S, τ t ∈ S) (hττ : ∀ t ∈ S, τ (τ t) = t)
    (hρτ : ∀ t ∈ S, ρ (τ t) = -ρ t) (hq : q ≠ 0)
    (hnd : ∀ t ∈ S, q ^ (2 * ρ t) ≠ 1) :
    (2 : R) * ∑ t ∈ S, seminormalWeight q h (ρ t) = (S.card : R) * h := by
  rw [characterSum_eq_h_mul]
  have hkey := two_mul_reducedSum_eq_card q S ρ τ hτS hττ hρτ hq hnd
  linear_combination h * hkey

/-- **Full single-generator character `χ_λ(σ) = c_λ·h` (all three tableau
    classes).** The seminormal character of `σ` on `S^λ` splits the standard
    tableaux into three classes by where `1, 2` sit: **same-row** (diagonal
    eigenvalue `q`), **same-column** (diagonal eigenvalue `−q⁻¹`), and
    **off-diagonal** (weight `a_ρ`). The two Hecke eigenvalues satisfy
    `q + (−q⁻¹) = q − q⁻¹ = h`, so the same-column eigenvalue is `−q⁻¹ = h − q`
    (stated that way here to keep the identity inverse-free). For a
    **self-conjugate** `λ` the same-row and same-column counts are equal
    (`Rrow.card = Rcol.card`, conjugation symmetry), so the diagonal contribution
    `r·q + r·(h − q) = r·h` is an integer multiple of `h`; the off-diagonal part is
    `(|Soff|/2)·h` by `two_mul_characterSum_eq`. Hence

      2·χ_λ(σ) = (2·|Rrow| + |Soff|)·h,   i.e.  χ_λ(σ) = c_λ·h,  c_λ = |Rrow| + |Soff|/2 ∈ ℤ.

    This is the complete abstract form of `symbolic_character_table` — sorry-free,
    reducing that block to supplying the concrete tableau partition + the swap
    involution `τ` on the off-diagonal class (bean `qou-9vvr` / `qou-tqab`). -/
theorem fullCharacter_two_mul {ι : Type*} [DecidableEq ι] (q h : R)
    (Rrow Rcol Soff : Finset ι) (ρ : ι → ℤ) (τ : ι → ι)
    (hcard : Rrow.card = Rcol.card)
    (hτS : ∀ t ∈ Soff, τ t ∈ Soff) (hττ : ∀ t ∈ Soff, τ (τ t) = t)
    (hρτ : ∀ t ∈ Soff, ρ (τ t) = -ρ t) (hq : q ≠ 0)
    (hnd : ∀ t ∈ Soff, q ^ (2 * ρ t) ≠ 1) :
    (2 : R) * ((Rrow.card : R) * q + (Rcol.card : R) * (h - q)
          + ∑ t ∈ Soff, seminormalWeight q h (ρ t))
      = ((2 * Rrow.card + Soff.card : ℕ) : R) * h := by
  have hoff := two_mul_characterSum_eq q h Soff ρ τ hτS hττ hρτ hq hnd
  set Q := ∑ t ∈ Soff, seminormalWeight q h (ρ t) with hQ
  rw [hcard]
  push_cast
  linear_combination hoff

end QOU.BraidKnot.SeminormalWeight