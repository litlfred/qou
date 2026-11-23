/-
# Letter orientation vs. eigenline (chirality) labelling: two different involutions

Bean `qou-hlx6` (epic `qou-qs0e`). Formalize-first test of a coordinator's working
hypothesis — NOT a finding, NOT adopted:

  the letter orientation `σ ↦ σ⁻¹` (the net-flavour bit of stream 6a, #7827) is the
  same datum as the choice of which eigenline of that letter (`q` vs `−q⁻¹`) is called
  left-handed (the chirality pair of stream 6b, #7825).

## What this file proves

Fix one Hecke letter `s` in any `K`-algebra `A`: `s² = h s + 1`, `h = q − q⁻¹`, with
`q ≠ 0`, `q + q⁻¹ ≠ 0`. Its two eigenprojectors are
`P₊ = (s + q⁻¹)/(q + q⁻¹)` (eigenvalue `q`) and `P₋ = (q − s)/(q + q⁻¹)`
(eigenvalue `−q⁻¹`) — `eigen_plus`, `eigen_minus`, `Pp_add_Pm`, `Pp_mul_Pm`.

Two involutions act on the letter:

* **orientation flip** `s ↦ s⁻¹ = s − h` (`inv_letter`): a Hecke letter at parameter
  `q⁻¹` (`flip_hecke`), with the SAME two projectors (`flip_Pp`, `flip_Pm`) and the
  eigenvalues inverted on BOTH lines (`flip_eigen_plus`, `flip_eigen_minus`);
* **eigenline swap** `s ↦ −s⁻¹ = h − s`: a Hecke letter at the SAME parameter `q`
  (`swap_hecke`) whose projectors are exchanged (`swap_Pp`, `swap_Pm`).

`flip_ne_swap`: whenever `P₊ ≠ 0`, the two involutions do not induce the same labelled
eigenline pair. So the orientation bit is NOT the chirality bit (scope (b); the
invariant is the bar-invariance of the idempotents, `flip_Pp`).

`no_one_sided_letter`: no element acting by an inverted eigenvalue on `P₊` only
(`x P₊ = q⁻¹ P₊`, `x P₋ = −q⁻¹ P₋`) is a Hecke letter at ANY parameter `p`, unless
`q² = 1`. So a chirality-selective flavour flip is not a letter.

**The skein difference is a chirality projector** (bean `qou-hlx7`):
`q·s − q⁻¹·s⁻¹ = (q − q⁻¹)(q + q⁻¹)·P₊` (`skein_asym_eq`). It kills the `(−q⁻¹)`-line
(`skein_asym_mul_Pm`), vanishes at `h = 0` (`skein_asym_zero_of_h`), is bar-odd
(`skein_asym_bar_odd`), and the mirror weighting / the swapped letter give `P₋`
(`skein_mirror_eq`, `skein_asym_swap`). It is a multiple of an idempotent, not a letter.

On the NF algebra `H₃(q)` with formal `h` (6a's `netFlavour`):
`netFlavour` of `σ`, `σ⁻¹`, `−σ⁻¹` is `0`, `−1`, `+1` (`netFlavour_swapLetter`). The two
corpus flavours `σ`, `σ⁻¹` have the same projector pair (`corpus_flavours_same_lines`)
and different net flavour (`netFlavour_letter`, 6a): **net flavour is not a function of
the eigenline labelling.** The photon-level combinations are `pair_id_swap_netFlavour`,
`pair_swap_id_netFlavour`.

Base ring (§7c): generic `[Field K]` (projectors need `(q + q⁻¹)⁻¹`), generic
`[Ring A] [Algebra K A]`; the formal-`h` part is over generic `[CommRing R]`. No `ℝ`.

-- Ref: [kazhdan-lusztig1979] https://doi.org/10.1007/BF01390031
-/
import QOU.QuarkState.PhotonPairNormalForm
import QOU.Machinery.HeckeH3AlgebraInstance
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Module
import Mathlib.Tactic.FieldSimp

namespace QOU.QuarkState.Helicity

/-! ## One Hecke letter in an abstract algebra -/

section Abstract

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]

/-- The Hecke relation at parameter `q`: `x² = (q − q⁻¹) x + 1`. -/
def IsLetter (q : K) (x : A) : Prop := x * x = (q - q⁻¹) • x + 1

/-- The orientation flip `s ↦ s − h` (`= s⁻¹` on a letter). -/
def flip (q : K) (s : A) : A := s - (q - q⁻¹) • (1 : A)

/-- The eigenline swap `s ↦ h − s` (`= −s⁻¹` on a letter). -/
def swap (q : K) (s : A) : A := (q - q⁻¹) • (1 : A) - s

/-- Projector onto the eigenvalue-`q` line. -/
noncomputable def Pp (q : K) (s : A) : A := (q + q⁻¹)⁻¹ • (s + q⁻¹ • (1 : A))

/-- Projector onto the eigenvalue-`(−q⁻¹)` line. -/
noncomputable def Pm (q : K) (s : A) : A := (q + q⁻¹)⁻¹ • (q • (1 : A) - s)

variable {q : K} {s : A}

theorem inv_letter (hs : IsLetter q s) : s * flip q s = 1 ∧ flip q s * s = 1 := by
  unfold IsLetter at hs
  refine ⟨?_, ?_⟩ <;>
    simp only [flip, mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, mul_one, one_mul, hs] <;>
    abel

theorem Pp_add_Pm (hq2 : q + q⁻¹ ≠ 0) : Pp q s + Pm q s = 1 := by
  unfold Pp Pm
  rw [← smul_add]
  have : s + q⁻¹ • (1 : A) + (q • (1 : A) - s) = (q + q⁻¹) • (1 : A) := by
    rw [add_smul]; abel
  rw [this, smul_smul, inv_mul_cancel₀ hq2, one_smul]

theorem eigen_plus (hq : q ≠ 0) (hs : IsLetter q s) : s * Pp q s = q • Pp q s := by
  unfold IsLetter at hs
  unfold Pp
  rw [mul_smul_comm, smul_comm q]
  congr 1
  rw [mul_add, hs, mul_smul_comm, mul_one, smul_add, smul_smul, mul_inv_cancel₀ hq, one_smul,
    sub_smul]
  abel

theorem eigen_minus (hq : q ≠ 0) (hs : IsLetter q s) : s * Pm q s = (-q⁻¹) • Pm q s := by
  unfold IsLetter at hs
  unfold Pm
  rw [mul_smul_comm, smul_comm (-q⁻¹)]
  congr 1
  rw [mul_sub, hs, mul_smul_comm, mul_one, smul_sub, smul_smul, neg_mul, inv_mul_cancel₀ hq,
    neg_smul, one_smul, sub_smul, neg_smul]
  abel

theorem Pp_mul_Pm (hq : q ≠ 0) (hs : IsLetter q s) : Pp q s * Pm q s = 0 := by
  have e := eigen_minus hq hs
  unfold Pp
  rw [smul_mul_assoc, add_mul, e, smul_mul_assoc, one_mul, ← add_smul, neg_add_cancel,
    zero_smul, smul_zero]

theorem Pp_idem (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    Pp q s * Pp q s = Pp q s := by
  have h1 : Pp q s * (Pp q s + Pm q s) = Pp q s := by rw [Pp_add_Pm hq2, mul_one]
  rwa [mul_add, Pp_mul_Pm hq hs, add_zero] at h1

/-! ### The orientation flip -/

theorem flip_hecke (hs : IsLetter q s) : IsLetter q⁻¹ (flip q s) := by
  unfold IsLetter at hs ⊢
  simp only [flip, inv_inv, mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, mul_one, one_mul,
    hs, smul_sub, smul_smul, sub_smul]
  module

/-- **The orientation flip fixes the `q`-line projector** (read at the flipped
parameter `q⁻¹`, where the flipped letter's matching eigenvalue is `q⁻¹`). -/
theorem flip_Pp : Pp q⁻¹ (flip q s) = Pp q s := by
  unfold Pp flip
  rw [inv_inv, add_comm q⁻¹ q]
  congr 1
  rw [sub_smul]; abel

theorem flip_Pm : Pm q⁻¹ (flip q s) = Pm q s := by
  unfold Pm flip
  rw [inv_inv, add_comm q⁻¹ q]
  congr 1
  rw [sub_smul]; abel

/-- The flipped letter inverts the eigenvalue on the `q`-line … -/
theorem flip_eigen_plus (hq : q ≠ 0) (hs : IsLetter q s) :
    flip q s * Pp q s = q⁻¹ • Pp q s := by
  unfold flip
  rw [sub_mul, eigen_plus hq hs, smul_mul_assoc, one_mul, ← sub_smul]
  congr 1; ring

/-- … and on the `(−q⁻¹)`-line (eigenvalue `−q`). The flip acts on BOTH lines. -/
theorem flip_eigen_minus (hq : q ≠ 0) (hs : IsLetter q s) :
    flip q s * Pm q s = (-q) • Pm q s := by
  unfold flip
  rw [sub_mul, eigen_minus hq hs, smul_mul_assoc, one_mul, ← sub_smul]
  congr 1; ring

/-! ### The eigenline swap -/

theorem swap_eq_neg_flip : swap q s = -flip q s := by
  unfold swap flip; abel

theorem swap_hecke (hs : IsLetter q s) : IsLetter q (swap q s) := by
  unfold IsLetter at hs ⊢
  simp only [swap, mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, mul_one, one_mul,
    hs, smul_sub, smul_smul, sub_smul]
  module

theorem swap_Pp : Pp q (swap q s) = Pm q s := by
  unfold Pp Pm swap
  congr 1
  rw [sub_smul]; abel

theorem swap_Pm : Pm q (swap q s) = Pp q s := by
  unfold Pp Pm swap
  congr 1
  rw [sub_smul]; abel

/-- **The orientation flip is not the eigenline swap.** The flip keeps `P₊` as the
projector of its matching eigenvalue; the swap sends it to `P₋`; and `P₊ ≠ P₋`
whenever `P₊ ≠ 0`. -/
theorem flip_ne_swap (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s)
    (hP : Pp q s ≠ 0) : Pp q⁻¹ (flip q s) ≠ Pp q (swap q s) := by
  rw [flip_Pp, swap_Pp]
  intro he
  apply hP
  calc Pp q s = Pp q s * Pp q s := (Pp_idem hq hq2 hs).symm
    _ = Pp q s * Pm q s := by rw [← he]
    _ = 0 := Pp_mul_Pm hq hs

/-- **No one-sided flip is a letter.** An element inverting the eigenvalue on `P₊` only
(acting by `q⁻¹` on `P₊`, unchanged `−q⁻¹` on `P₋`) satisfies a Hecke relation at some
parameter `p` only if `q² = 1`. -/
theorem no_one_sided_letter (h2 : (2 : K) ≠ 0) (hq : q ≠ 0)
    (hPp : Pp q s ≠ 0) (hPm : Pm q s ≠ 0) {x : A} {p : K}
    (hxp : x * Pp q s = q⁻¹ • Pp q s) (hxm : x * Pm q s = (-q⁻¹) • Pm q s)
    (hx : IsLetter p x) : q ^ 2 = 1 := by
  unfold IsLetter at hx
  have ep : (q⁻¹ * q⁻¹ - (p - p⁻¹) * q⁻¹ - 1) • Pp q s = 0 := by
    have := congrArg (· * Pp q s) hx
    simp only [mul_assoc, hxp, mul_smul_comm, smul_mul_assoc, add_mul, one_mul, smul_smul]
      at this
    rw [sub_smul, sub_smul, this]; module
  have em : (q⁻¹ * q⁻¹ + (p - p⁻¹) * q⁻¹ - 1) • Pm q s = 0 := by
    have := congrArg (· * Pm q s) hx
    simp only [mul_assoc, hxm, mul_smul_comm, smul_mul_assoc, add_mul, one_mul, smul_smul,
      neg_mul, mul_neg, neg_neg] at this
    rw [sub_smul, add_smul, this]; module
  have a := (smul_eq_zero.mp ep).resolve_right hPp
  have b := (smul_eq_zero.mp em).resolve_right hPm
  have hqi : q⁻¹ * q⁻¹ = 1 := by
    have : (2 : K) * (q⁻¹ * q⁻¹ - 1) = 0 := by linear_combination a + b
    have := (mul_eq_zero.mp this).resolve_left h2
    linear_combination this
  have : q ^ 2 = (q * q⁻¹) ^ 2 * q ^ 2 := by rw [mul_inv_cancel₀ hq]; ring
  rw [this]; field_simp at hqi ⊢; linear_combination -hqi

/-! ### The `q`-weighted skein difference (bean `qou-hlx7`)

`force-knot-identification.md` locates parity violation in the asymmetry of the
`q`-weighted crossing difference `q[L₊] − q⁻¹[L₋]`. Read in the algebra (before any trace),
with `L₊ = s` and `L₋ = s⁻¹`, this difference is EXACTLY `h·[2]_q` times the eigenvalue-`q`
projector: it kills the other line. The mirror weighting gives the other projector. -/

/-- `q·s − q⁻¹·s⁻¹ = (q − q⁻¹)(q + q⁻¹)·P₊`. -/
theorem skein_asym_eq (hq2 : q + q⁻¹ ≠ 0) :
    q • s - q⁻¹ • flip q s = (q - q⁻¹) • ((q + q⁻¹) • Pp q s) := by
  unfold Pp flip
  rw [smul_smul (q + q⁻¹), mul_inv_cancel₀ hq2, one_smul]
  module

/-- The mirror weighting: `q⁻¹·s − q·s⁻¹ = (q − q⁻¹)(q + q⁻¹)·P₋`. -/
theorem skein_mirror_eq (hq2 : q + q⁻¹ ≠ 0) :
    q⁻¹ • s - q • flip q s = (q - q⁻¹) • ((q + q⁻¹) • Pm q s) := by
  unfold Pm flip
  rw [smul_smul (q + q⁻¹), mul_inv_cancel₀ hq2, one_smul]
  module

/-- **The skein difference annihilates the `(−q⁻¹)`-line.** -/
theorem skein_asym_mul_Pm (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    (q • s - q⁻¹ • flip q s) * Pm q s = 0 := by
  rw [skein_asym_eq hq2, smul_mul_assoc, smul_mul_assoc, Pp_mul_Pm hq hs, smul_zero, smul_zero]

/-- … and acts on the `q`-line by the scalar `(q − q⁻¹)(q + q⁻¹) = q² − q⁻²`. -/
theorem skein_asym_mul_Pp (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    (q • s - q⁻¹ • flip q s) * Pp q s = ((q - q⁻¹) * (q + q⁻¹)) • Pp q s := by
  rw [skein_asym_eq hq2, smul_mul_assoc, smul_mul_assoc, Pp_idem hq hq2 hs, smul_smul]

/-- The eigenline swap exchanges the two weightings: the skein difference of the swapped
letter is the mirror projector `(q − q⁻¹)(q + q⁻¹)·P₋`. -/
theorem skein_asym_swap (hq2 : q + q⁻¹ ≠ 0) :
    q • swap q s - q⁻¹ • flip q (swap q s) = (q - q⁻¹) • ((q + q⁻¹) • Pm q s) := by
  unfold Pm flip swap
  rw [smul_smul (q + q⁻¹), mul_inv_cancel₀ hq2, one_smul]
  module

/-- At `h = q − q⁻¹ = 0` the skein difference vanishes: no asymmetry at `q = ±1`. -/
theorem skein_asym_zero_of_h (hq2 : q + q⁻¹ ≠ 0) (hh : q - q⁻¹ = 0) :
    q • s - q⁻¹ • flip q s = 0 := by
  rw [skein_asym_eq hq2, hh, zero_smul]

/-- **The skein difference is bar-odd**: the orientation flip (`q ↦ q⁻¹`, `s ↦ s⁻¹`) sends
it to its negative, while `P₊` is bar-even (`flip_Pp`) — the sign sits in `h`. -/
theorem skein_asym_bar_odd :
    q⁻¹ • flip q s - q⁻¹⁻¹ • flip q⁻¹ (flip q s) = -(q • s - q⁻¹ • flip q s) := by
  unfold flip
  rw [inv_inv]
  module

/-- The swap is an involution. -/
theorem swap_swap : swap q (swap q s) = s := by
  unfold swap; abel

/-- **On a three-letter word the L↔R relabelling is minus the mirror.** Applying the swap to
every letter of `a·b·a` gives `−(a⁻¹·b⁻¹·a⁻¹)`: the knot mirror times `(−1)^{length}`. -/
theorem swap_word3 (a b : A) :
    swap q a * swap q b * swap q a = -(flip q a * flip q b * flip q a) := by
  simp only [swap_eq_neg_flip, neg_mul, mul_neg, neg_neg]

/-- On a two-letter word the relabelling IS the mirror (even length, no sign). -/
theorem swap_word2 (a b : A) : swap q a * swap q b = flip q a * flip q b := by
  simp only [swap_eq_neg_flip, neg_mul, mul_neg, neg_neg]

/-! ### The three letter-level involutions form a Klein four-group (D-H5, bean `qou-hlx7`)

`flip : s ↦ s⁻¹` and `neg : s ↦ −s` move the Hecke parameter `q ↦ q⁻¹`; `swap : s ↦ −s⁻¹`
keeps it. Each is an involution and the composite of any two is the third. -/

theorem neg_hecke (hs : IsLetter q s) : IsLetter q⁻¹ (-s) := by
  unfold IsLetter at hs ⊢
  rw [neg_mul_neg, hs, inv_inv]
  module

theorem flip_flip : flip q⁻¹ (flip q s) = s := by
  unfold flip; rw [inv_inv]; module

/-- `neg` exchanges the eigenprojectors (read at the moved parameter). -/
theorem neg_Pp : Pp q⁻¹ (-s) = Pm q s := by
  unfold Pp Pm; rw [inv_inv, add_comm q⁻¹ q]; congr 1; abel

theorem neg_Pm : Pm q⁻¹ (-s) = Pp q s := by
  unfold Pp Pm; rw [inv_inv, add_comm q⁻¹ q]; congr 1; abel

/-- Klein relation: `flip ∘ neg = swap`. -/
theorem flip_neg : flip q⁻¹ (-s) = swap q s := by
  unfold flip swap; rw [inv_inv]; module

/-- Klein relation: `flip ∘ swap = neg`. -/
theorem flip_swap : flip q (swap q s) = -s := by
  unfold flip swap; abel

/-- **No `K`-linear algebra map realises the flip.** If an algebra endomorphism sends a
letter to its inverse, then `2(q − q⁻¹) = 0`: impossible for `q² ≠ 1` in char ≠ 2. -/
theorem no_linear_flip [Nontrivial A] (h2 : (2 : K) ≠ 0) (hs : IsLetter q s)
    (φ : A →ₐ[K] A) (hφ : φ s = flip q s) : q - q⁻¹ = 0 := by
  have e := congrArg φ hs
  unfold IsLetter at e
  rw [map_mul, map_add, map_smul, map_one, hφ] at e
  have hf := flip_hecke hs
  unfold IsLetter at hf
  rw [hf, inv_inv] at e
  have hz : ((2 : K) * (q - q⁻¹)) • flip q s = 0 := by
    have : ((q - q⁻¹) - (q⁻¹ - q)) • flip q s = 0 := by
      rw [sub_smul]; exact sub_eq_zero.mpr (add_right_cancel e.symm)
    rw [← this]; congr 1; ring
  have h1 : ((2 : K) * (q - q⁻¹)) • (1 : A) = 0 := by
    rw [← (inv_letter hs).2, ← smul_mul_assoc, hz, zero_mul]
  rcases smul_eq_zero.mp h1 with h | h
  · exact (mul_eq_zero.mp h).resolve_left h2
  · exact absurd h one_ne_zero

/-- **No `K`-linear algebra map realises `neg`** either, unless `q² = 1`. -/
theorem no_linear_neg [Nontrivial A] (h2 : (2 : K) ≠ 0) (hs : IsLetter q s)
    (φ : A →ₐ[K] A) (hφ : φ s = -s) : q - q⁻¹ = 0 := by
  have e := congrArg φ hs
  unfold IsLetter at e
  rw [map_mul, map_add, map_smul, map_one, hφ, neg_mul_neg, hs] at e
  have hz : ((2 : K) * (q - q⁻¹)) • s = 0 := by
    have : (q - q⁻¹) • s - (q - q⁻¹) • (-s) = 0 := sub_eq_zero.mpr (add_right_cancel e)
    rw [← this]; module
  have h1 : ((2 : K) * (q - q⁻¹)) • (1 : A) = 0 := by
    rw [← (inv_letter hs).1, ← smul_mul_assoc, hz, zero_mul]
  rcases smul_eq_zero.mp h1 with h | h
  · exact (mul_eq_zero.mp h).resolve_left h2
  · exact absurd h one_ne_zero

end Abstract

/-! ## On the NF algebra `H₃(q)`: the corpus letters -/

section NF

open QOU.Machinery.H3

variable {K : Type*} [Field K]

/-- `σ₀` as an element of the NF ring at `h = q − q⁻¹`. -/
def sig0 (q : K) : H3A K (q - q⁻¹) := ⟨s0⟩
/-- `σ₁` as an element of the NF ring. -/
def sig1 (q : K) : H3A K (q - q⁻¹) := ⟨s1⟩

theorem sig0_letter (q : K) : IsLetter q (sig0 q) := by
  unfold IsLetter; ext i
  fin_cases i <;> simp [sig0, H3A.mul_v, H3A.add_v, H3A.smul_v, H3A.one_v, mulNF, mulσ₀,
    mulσ₁, s0, unitNF]

theorem sig1_letter (q : K) : IsLetter q (sig1 q) := by
  unfold IsLetter; ext i
  fin_cases i <;> simp [sig1, H3A.mul_v, H3A.add_v, H3A.smul_v, H3A.one_v, mulNF, mulσ₀,
    mulσ₁, s1, unitNF]

/-- **The two corpus flavours of a letter carry the same eigenline pair.** -/
theorem corpus_flavours_same_lines (q : K) :
    (Pp q⁻¹ (flip q (sig0 q)) = Pp q (sig0 q) ∧ Pm q⁻¹ (flip q (sig0 q)) = Pm q (sig0 q)) ∧
    (Pp q⁻¹ (flip q (sig1 q)) = Pp q (sig1 q) ∧ Pm q⁻¹ (flip q (sig1 q)) = Pm q (sig1 q)) :=
  ⟨⟨flip_Pp, flip_Pm⟩, ⟨flip_Pp, flip_Pm⟩⟩

/-! ### The electron and the L↔R relabelling (coordinator question 2, bean `qou-hlx7`)

`breit-wheeler-vertex.md:34-36`: `e⁻ = σ₀σ₁σ₀`, and `e⁺` is the mirror
`σ₀⁻¹σ₁⁻¹σ₀⁻¹`. The L↔R relabelling replaces every letter `σ` by the other Hecke letter at
the SAME parameter, `−σ⁻¹`. -/

/-- The electron `σ₀σ₁σ₀`. -/
def electron (q : K) : H3A K (q - q⁻¹) := sig0 q * sig1 q * sig0 q

/-- The positron, the mirror word `σ₀⁻¹σ₁⁻¹σ₀⁻¹`. -/
def positron (q : K) : H3A K (q - q⁻¹) := flip q (sig0 q) * flip q (sig1 q) * flip q (sig0 q)

theorem flip_sig0_v (q : K) : (flip q (sig0 q)).v = ![-(q - q⁻¹), 1, 0, 0, 0, 0] := by
  funext i; fin_cases i <;> simp [flip, sig0, H3A.smul_v, H3A.one_v, s0, unitNF,
    show ∀ x y : H3A K (q - q⁻¹), (x - y).v = x.v - y.v from fun _ _ => rfl]

theorem flip_sig1_v (q : K) : (flip q (sig1 q)).v = ![-(q - q⁻¹), 0, 1, 0, 0, 0] := by
  funext i; fin_cases i <;> simp [flip, sig1, H3A.smul_v, H3A.one_v, s1, unitNF,
    show ∀ x y : H3A K (q - q⁻¹), (x - y).v = x.v - y.v from fun _ _ => rfl]

/-- The mirrored letters satisfy the braid relation. -/
theorem flip_braid (q : K) :
    flip q (sig0 q) * flip q (sig1 q) * flip q (sig0 q) =
      flip q (sig1 q) * flip q (sig0 q) * flip q (sig1 q) := by
  ext i
  simp only [H3A.mul_v, flip_sig0_v, flip_sig1_v]
  fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁] <;> ring

/-- The relabelled letters still satisfy the braid relation, so relabelling every letter
is a consistent presentation of the same algebra. -/
theorem swap_braid (q : K) :
    swap q (sig0 q) * swap q (sig1 q) * swap q (sig0 q) =
      swap q (sig1 q) * swap q (sig0 q) * swap q (sig1 q) := by
  rw [swap_word3, swap_word3, flip_braid]

/-- **The relabelling sends the electron to MINUS the positron.** -/
theorem swap_electron (q : K) :
    swap q (sig0 q) * swap q (sig1 q) * swap q (sig0 q) = -positron q :=
  swap_word3 _ _

/-- The top coordinate (`σ₀σ₁σ₀`) of the electron is `1`. -/
theorem electron_top (q : K) : (electron q).v 5 = 1 := by
  simp [electron, sig0, sig1, H3A.mul_v, mulNF, mulσ₀, mulσ₁, s0, s1]

/-- … and of the positron also `1`. -/
theorem positron_top (q : K) : (positron q).v 5 = 1 := by
  simp only [positron, H3A.mul_v, flip_sig0_v, flip_sig1_v]
  simp [mulNF, mulσ₀, mulσ₁]

/-- **The relabelling does not fix the electron** (char ≠ 2): the electron is a positive word
in exactly one of the two letter systems at parameter `q`. -/
theorem electron_ne_swap (q : K) (h2 : (2 : K) ≠ 0) :
    electron q ≠ swap q (sig0 q) * swap q (sig1 q) * swap q (sig0 q) := by
  rw [swap_electron]
  intro he
  have := congrArg (fun x => x.v 5) he
  simp only [H3A.neg_v, Pi.neg_apply, electron_top, positron_top] at this
  apply h2; linear_combination this

/-- `neg` sends the electron to MINUS ITSELF (same word, sign `(−1)^3`). -/
theorem neg_electron (q : K) : (-sig0 q) * (-sig1 q) * (-sig0 q) = -electron q := by
  simp only [electron, neg_mul, mul_neg, neg_neg]

/-- The positron's `σ₁σ₀` coordinate is `−h`. -/
theorem positron_v3 (q : K) : (positron q).v 3 = -(q - q⁻¹) := by
  simp only [positron, H3A.mul_v, flip_sig0_v, flip_sig1_v]
  simp [mulNF, mulσ₀, mulσ₁]

/-- **The mirror changes the particle**: `e⁺ ≠ e⁻` whenever `h ≠ 0`. -/
theorem positron_ne_electron (q : K) (hh : q - q⁻¹ ≠ 0) : positron q ≠ electron q := by
  intro he
  have := congrArg (fun x => x.v 3) he
  simp only [positron_v3] at this
  apply hh
  have h3 : (electron q).v 3 = 0 := by
    simp [electron, sig0, sig1, H3A.mul_v, mulNF, mulσ₀, mulσ₁, s0, s1]
  rw [h3] at this; linear_combination -this

end NF

/-! ## Net flavour (6a's `h¹` unit coordinate) of the three letter forms -/

section Flavour

open Polynomial QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- The eigenline-swapped letter `−σ_g⁻¹ = h − σ_g`, with `h` formal. -/
noncomputable def swapLetter (g : Bool) : Fin 6 → R[X] :=
  (X : R[X]) • (e0 : Fin 6 → R[X]) - (if g then s0 else s1)

/-- `netFlavour` of `σ`, `σ⁻¹`, `−σ⁻¹` is `0`, `−1`, `+1`. -/
theorem netFlavour_swapLetter (g : Bool) :
    netFlavour (swapLetter (R := R) g) = 1 ∧
    netFlavour (quarkLetter (R := R) g true) = 0 ∧
    netFlavour (quarkLetter (R := R) g false) = -1 := by
  refine ⟨?_, ?_, ?_⟩
  · cases g <;> simp [netFlavour, hPart, swapLetter, e0, s0, s1, Polynomial.coeff_X]
  · simpa [flavourShift] using netFlavour_letter (R := R) g true
  · simpa [flavourShift] using netFlavour_letter (R := R) g false

/-- **Net flavour is not a function of the eigenline labelling**: the two corpus
flavours of one letter have the same projector pair (`corpus_flavours_same_lines`) and
different net flavour. -/
theorem netFlavour_flavours_differ [Nontrivial R] (g : Bool) :
    netFlavour (quarkLetter (R := R) g true) ≠ netFlavour (quarkLetter (R := R) g false) := by
  rw [(netFlavour_swapLetter (R := R) g).2.1, (netFlavour_swapLetter (R := R) g).2.2]
  exact (neg_ne_zero.mpr one_ne_zero).symm

/-- The photon with eigenline-swapped letters, `1 + φ₀(h−σ₀) + φ₁(h−σ₁) + φ₀₁(h−σ₀)(h−σ₁)`. -/
noncomputable def photonSwap (a0 a1 a2 : R[X]) : Fin 6 → R[X] :=
  e0 + a0 • ((X : R[X]) • e0 - s0) + a1 • ((X : R[X]) • e0 - s1)
    + a2 • mulNF (X : R[X]) ((X : R[X]) • e0 - s0) ((X : R[X]) • e0 - s1)

theorem pair_id_swap_coord0 (a0 a1 a2 b0 b1 b2 : R) :
    mulNF (X : R[X]) (photonStraight X (C a0) (C a1) (C a2)) (photonSwap (C b0) (C b1) (C b2)) 0 =
      C (1 - a0 * b0 - a1 * b1) + C (b0 + b1 - (a0 + a1) * b2) * X + C b2 * X ^ 2 := by
  simp [photonStraight, photonSwap, mulNF, mulσ₀, mulσ₁, e0, s0, s1]
  ring

/-- σ-photon against swap-photon: net flavour `(ψ₀ + ψ₁) − (φ₀ + φ₁)ψ₀₁`
(compare 6a's `pairBar_netFlavour`: `−(ψ₀ + ψ₁) − (φ₀ + φ₁)ψ₀₁`). -/
theorem pair_id_swap_netFlavour (a0 a1 a2 b0 b1 b2 : R) :
    netFlavour (mulNF (X : R[X]) (photonStraight X (C a0) (C a1) (C a2))
      (photonSwap (C b0) (C b1) (C b2))) = b0 + b1 - (a0 + a1) * b2 := by
  simp only [netFlavour, hPart, pair_id_swap_coord0, Polynomial.coeff_add, Polynomial.coeff_C,
    Polynomial.coeff_C_mul, Polynomial.coeff_X_pow, Polynomial.coeff_X]
  simp

theorem pair_swap_id_coord0 (a0 a1 a2 b0 b1 b2 : R) :
    mulNF (X : R[X]) (photonSwap (C a0) (C a1) (C a2)) (photonStraight X (C b0) (C b1) (C b2)) 0 =
      C (1 - a0 * b0 - a1 * b1) + C (a0 + a1 - a2 * (b0 + b1)) * X + C a2 * X ^ 2 := by
  simp [photonStraight, photonSwap, mulNF, mulσ₀, mulσ₁, e0, s0, s1]
  ring

theorem pair_swap_id_netFlavour (a0 a1 a2 b0 b1 b2 : R) :
    netFlavour (mulNF (X : R[X]) (photonSwap (C a0) (C a1) (C a2))
      (photonStraight X (C b0) (C b1) (C b2))) = a0 + a1 - a2 * (b0 + b1) := by
  simp only [netFlavour, hPart, pair_swap_id_coord0, Polynomial.coeff_add, Polynomial.coeff_C,
    Polynomial.coeff_C_mul, Polynomial.coeff_X_pow, Polynomial.coeff_X]
  simp

end Flavour

end QOU.QuarkState.Helicity
