import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.ew_charge_spin_from_involution — `thm:ew-triplet-charge-spin-from-involution`

Charge and spin of the electroweak triplet are **not** two independent open
conjectures: both are **proved consequences** of a single physics selection
postulate, through the corpus `def:spin-involution` (`QOU.BraidKnot.SpinInvolution`).

## Two provable ingredients + one physics postulate

**(Task 3 — bar-parity, provable.)** The even-twist carrier `T(2,2k)` sits in
the two-dimensional sym/alt Hecke block with eigenvalues `(q^{2k}, q^{-2k})`,
modelled here as the pair `(↑a, ↑a⁻¹) ∈ R × R` with `a = q^{2k} ∈ Rˣ`. The
`σ`-spin-involution of `def:spin-involution` acts as the **swap**
`swap₂ (x,y) = (y,x)` — exactly `q^{2k} ↦ q^{-2k}` (the bar involution
`q ↦ q⁻¹` on the eigenvalue pair). Its projections give:

* the **bar-even** part `a₊ = ½(m + σm) ∈ A₊`, `σ`-fixed, with neutral trace
  `trSum(a₊) = q^{2k} + q^{-2k}` (`= 2cosh` — the retained, *neutral* channel,
  per `information-theory/vdw-pskew-isolation`);
* the **bar-odd** part `a₋ = ½(m − σm) ∈ A₋`, `σ`-negated, **traceless**
  (`trSum(a₋) = 0`, the `P_skew` / *charged* channel) but with nonzero skew
  `skew(a₋) = q^{2k} − q^{-2k}` (`= 2sinh`).

The Higgs is the bar-even / self-dual / real-volume carrier
(`braids-and-knots/self-dual-higgs-real-volume`); `W±, Z` are bar-odd.

**(Task 4 — sector label and charge computed through `σ`, modulo one
postulate.)** The residual physics input is the hypothesis class
`EWSectorSelection`: the `σ`-sector of each carrier (`A₊` = `σ`-even, `A₋` =
`σ`-odd; both are one-dimensional `ℤ/2`-sectors), the carrier eigenvalues, `W⁻`
as the `σ`-image of `W⁺`, and non-degeneracy `a² ≠ 1`. Given it:

* the sector label `spinDouble` (`2s`; "spin" names this two-valued sector
  label, not a Lorentz spin) is *computed* from whether `σ = swap₂` fixes the
  carrier's sector vector: `H ↦ 0`, `W±, Z ↦ 2` are theorems;
* the charge `ewCharge` is the skew functional of the sector vector: `H` has
  zero charge, `W⁺` nonzero charge, `W⁻` the opposite charge;
* `σ`-parity does **not** make `Z` neutral (`z_not_neutral_by_parity`); the
  `T₃` table `ewT3Double` (`W± ↦ ±1`, `Z, H ↦ 0`) is recorded, not derived. `Z`
  neutrality rests on the `(W³,B) → (Z,γ)` Weinberg mixing
  (`particle-interactions/weinberg-angle-categorical`).

The `SpinInvolution` structure lives in the `def:spin-involution` content
sibling (`mass-theory/spin-involution.lean`, namespace `QOU.BraidKnot`), whose
abstract projection algebra is proved there sorry-free. Content-block sibling
`.lean` files compile standalone (Mathlib-only) and cannot import one another,
so the concrete `swap₂` instance and its projection facts are recomputed here;
the abstract structure is cited, not re-declared.

LaTeX label: `thm:ew-triplet-charge-spin-from-involution`.

## References

- [leitner2026] particle-interactions/electroweak-triplet-charge-spin-from-involution
- `def:spin-involution` (`QOU.BraidKnot.SpinInvolution`; the abstract σ algebra)
- `thm:hoefsmit-ew-cell-content` (sym/alt block, the `tr_pure` bar-even trace)
- `braids-and-knots/self-dual-higgs-real-volume` (H = bar-even carrier)
- `information-theory/vdw-pskew-isolation` (bar-even neutral / bar-odd `P_skew` charged)
- `particle-interactions/weinberg-angle-categorical` (Z neutral via `θ_W` mixing)
-/

namespace QOU.ParticleInteractions

/-! ## Task 3 — concrete bar-parity of the even-twist carriers

The `σ`-spin-involution of `def:spin-involution`, restricted to the
two-dimensional sym/alt Hecke block, is the swap on `R × R`. We recompute the
projection facts (proved abstractly in `QOU.BraidKnot.SpinInvolution`) on this
concrete instance and read off the neutral (bar-even) and charged (bar-odd)
channels of a carrier `(q^{2k}, q^{-2k})`. -/

section BarParity

variable {R : Type*} [Field R] [Invertible (2 : R)]

/-- The concrete spin involution on the sym/alt block: the **swap**
`(x, y) ↦ (y, x)` — the bar involution `q^{2k} ↔ q^{-2k}` on the eigenvalue
pair. -/
def swap₂ (p : R × R) : R × R := (p.2, p.1)

/-- Neutral (Markov-trace) functional: the retained bar-even channel. -/
def trSum (p : R × R) : R := p.1 + p.2

/-- Charge (skew / `P_skew`) functional: the bar-odd channel. -/
def skew (p : R × R) : R := p.1 - p.2

/-- Bar-even projection `a₊ = ½ (p + σ p)` on the block. -/
def plusPart (p : R × R) : R × R := ((2 : R)⁻¹) • (p + swap₂ p)

/-- Bar-odd projection `a₋ = ½ (p − σ p)` on the block. -/
def minusPart (p : R × R) : R × R := ((2 : R)⁻¹) • (p - swap₂ p)

omit [Field R] [Invertible (2 : R)] in
/-- `swap₂` is an involution. -/
theorem swap₂_involutive (p : R × R) : swap₂ (swap₂ p) = p := rfl

/-- The carrier of eigenvalue `a = q^{2k} ∈ Rˣ`: the pair
`(q^{2k}, q^{-2k}) = (↑a, ↑a⁻¹)`. -/
def carrier (a : Rˣ) : R × R := ((a : R), ((a : R)⁻¹))

omit [Invertible (2 : R)] in
@[simp] theorem carrier_fst (a : Rˣ) : (carrier a : R × R).1 = (a : R) := rfl
omit [Invertible (2 : R)] in
@[simp] theorem carrier_snd (a : Rˣ) : (carrier a : R × R).2 = (a : R)⁻¹ := rfl

omit [Invertible (2 : R)] in
/-- `swap₂` sends the carrier `(q^{2k}, q^{-2k})` to `(q^{-2k}, q^{2k})` — the
bar image. -/
theorem swap₂_carrier (a : Rˣ) : swap₂ (carrier a) = ((a : R)⁻¹, (a : R)) := rfl

omit [Invertible (2 : R)] in
/-- The bar-even part is `σ`-fixed (`∈ A₊`). -/
theorem swap₂_plusPart (p : R × R) : swap₂ (plusPart p) = plusPart p := by
  unfold plusPart swap₂
  ext <;>
  · simp only [Prod.smul_fst, Prod.smul_snd, Prod.fst_add, Prod.snd_add,
      smul_eq_mul]
    ring

omit [Invertible (2 : R)] in
/-- The bar-odd part is `σ`-negated (`∈ A₋`). -/
theorem swap₂_minusPart (p : R × R) : swap₂ (minusPart p) = -(minusPart p) := by
  unfold minusPart swap₂
  ext <;>
  · simp only [Prod.smul_fst, Prod.smul_snd, Prod.fst_sub, Prod.snd_sub,
      Prod.fst_neg, Prod.snd_neg, smul_eq_mul]
    ring

/-- The spin decomposition on the block: `p = a₊ + a₋`. -/
theorem plusPart_add_minusPart (p : R × R) : plusPart p + minusPart p = p := by
  unfold plusPart minusPart swap₂
  ext <;>
  · simp only [Prod.fst_add, Prod.snd_add, Prod.smul_fst, Prod.smul_snd,
      Prod.fst_sub, Prod.snd_sub, smul_eq_mul]
    field_simp
    ring

/-- **Bar-even (neutral) value.** The retained Markov trace of the bar-even
part of the carrier is `q^{2k} + q^{-2k}` (`= 2cosh`). -/
theorem trSum_plusPart_carrier (a : Rˣ) :
    trSum (plusPart (carrier a)) = (a : R) + (a : R)⁻¹ := by
  unfold trSum plusPart carrier swap₂
  simp only [Prod.smul_fst, Prod.smul_snd, Prod.fst_add, Prod.snd_add,
    smul_eq_mul]
  field_simp
  ring

omit [Invertible (2 : R)] in
/-- **Bar-odd (charged) channel is traceless.** The charged (`P_skew`) part
carries zero Markov trace — the neutrality of the trace on the charged sector. -/
theorem trSum_minusPart_carrier (a : Rˣ) :
    trSum (minusPart (carrier a)) = 0 := by
  unfold trSum minusPart carrier swap₂
  simp only [Prod.smul_fst, Prod.smul_snd, Prod.fst_sub, Prod.snd_sub,
    smul_eq_mul]
  ring

/-- **Bar-odd (charged) value.** The skew (`P_skew`) functional of the bar-odd
part is `q^{2k} − q^{-2k}` (`= 2sinh`) — nonzero exactly when `a² ≠ 1`, i.e.
the carrier is genuinely charged. -/
theorem skew_minusPart_carrier (a : Rˣ) :
    skew (minusPart (carrier a)) = (a : R) - (a : R)⁻¹ := by
  unfold skew minusPart carrier swap₂
  simp only [Prod.smul_fst, Prod.smul_snd, Prod.fst_sub, Prod.snd_sub,
    smul_eq_mul]
  field_simp
  ring

end BarParity

/-! ## Task 4 — spin and charge computed through `σ` (conditional on one postulate)

The postulate `EWSectorSelection` carries only *inputs*: the `σ`-sector of each
carrier (`A₊` or `A₋`), the carrier eigenvalue `a = q^{2k} ∈ Rˣ`, the statement
that `W⁻` carries the `σ`-image eigenvalue of `W⁺`, and non-degeneracy
`a² ≠ 1`. From these, each carrier is given its **sector vector**: the `σ`-even
projection `plusPart (carrier a)` if it is in `A₊`, the `σ`-odd projection
`minusPart (carrier a)` if it is in `A₋`. Then

* the **sector label** `spinDouble` (`2s`) is *computed* from the action of
  `σ = swap₂` on the sector vector (`0` if `σ` fixes it, `2` otherwise), and
* the **charge** `ewCharge` is the skew (`P_skew`) functional of the sector
  vector.

"Spin" here is the name of this two-valued `σ`-sector label of the model; it is
not a computation of a Lorentz spin. The `T₃` values are **not** derived: see
`ewT3Double`, which records them as a table. -/

/-- The four electroweak carriers. -/
inductive EWCarrier
  | Wp  -- W⁺
  | Wm  -- W⁻
  | Z
  | H
deriving DecidableEq

/-- **The physics selection postulate** (§3b-cond hypothesis class). It carries
the inputs only, never the spin/charge conclusions:

* `isSinglet` — the `σ`-sector of each carrier: `true` = `σ`-even sector `A₊`,
  `false` = `σ`-odd sector `A₋` (both are `ℤ/2`-sectors of the involution, i.e.
  one-dimensional characters; "singlet" is the historical field name);
* the Higgs is in `A₊` (`self-dual-higgs-real-volume`); `W±, Z` are in `A₋`;
* `eig c` — the eigenvalue `q^{2k}` of the even-twist carrier of `c`;
* `wMinus_eig` — `W⁻` carries the `σ`-image (bar image) of the `W⁺` eigenvalue;
* `eig_sq_ne_one` — non-degeneracy `q^{4k} ≠ 1` (genuinely twisted carrier).

No instance is supplied. -/
class EWSectorSelection (R : Type*) [Field R] where
  /-- `true` = `σ`-even sector `A₊`; `false` = `σ`-odd sector `A₋`. -/
  isSinglet : EWCarrier → Bool
  /-- Higgs is in the bar-even sector `A₊`. -/
  higgs_singlet : isSinglet EWCarrier.H = true
  /-- `W⁺` is in the bar-odd sector `A₋`. -/
  wPlus_doublet : isSinglet EWCarrier.Wp = false
  /-- `W⁻` is in the bar-odd sector `A₋`. -/
  wMinus_doublet : isSinglet EWCarrier.Wm = false
  /-- `Z` is in the bar-odd sector `A₋`. -/
  z_doublet : isSinglet EWCarrier.Z = false
  /-- Carrier eigenvalue `q^{2k}` of each electroweak carrier. -/
  eig : EWCarrier → Rˣ
  /-- `W⁻` is the `σ`-image of `W⁺`: its eigenvalue is the bar image `a⁻¹`. -/
  wMinus_eig : eig EWCarrier.Wm = (eig EWCarrier.Wp)⁻¹
  /-- Non-degeneracy: `(q^{2k})² ≠ 1` for every carrier. -/
  eig_sq_ne_one : ∀ c, ((eig c : R)) ^ 2 ≠ 1

variable {R : Type*} [Field R] [EWSectorSelection R]

/-- Sector vector of a carrier: the `σ`-even projection of its block vector if
it is in `A₊`, the `σ`-odd projection if it is in `A₋`. -/
def sectorVec (c : EWCarrier) : R × R :=
  if EWSectorSelection.isSinglet (R := R) c then
    plusPart (carrier (EWSectorSelection.eig c))
  else
    minusPart (carrier (EWSectorSelection.eig c))

open Classical in
/-- **Doubled sector label** `2s`, computed from the action of `σ = swap₂` on the
sector vector: `0` if `σ` fixes it, `2` otherwise. -/
noncomputable def spinDouble (c : EWCarrier) : ℕ :=
  if swap₂ (sectorVec (R := R) c) = sectorVec (R := R) c then 0 else 2

/-- **Charge** of a carrier: the skew (`P_skew`) functional of its sector
vector. -/
def ewCharge (c : EWCarrier) : R := skew (sectorVec (R := R) c)

/-- **Neutrality by parity**: zero skew charge. -/
def isNeutralByParity (c : EWCarrier) : Prop := ewCharge (R := R) c = 0

/-- The isospin table `2·T₃` used by the paper: `W± ↦ ±1`, `Z ↦ 0`, `H ↦ 0`.
This is a **recorded label table, not derived** from `σ`. `Z ↦ 0` rests on the
Weinberg `(W³,B) → (Z,γ)` mixing (`weinberg-angle-categorical`), and `H ↦ 0` is
the model's assignment (the Standard Model gives the neutral Higgs component
`T₃ = −½`). The values `W± ↦ ±1` read as `2·T₃` give `T₃ = ±½`, the doublet
values of `def:spin-involution`, not the triplet values `T₃ = ±1` quoted in the
`.md`; the table is compared with `σ` in `IsospinFromSkew` / `OrderedSign`. -/
def ewT3Double : EWCarrier → ℤ
  | .Wp => 1
  | .Wm => -1
  | .Z => 0
  | .H => 0

omit [EWSectorSelection R] in
/-- `σ` negates the skew functional. -/
theorem skew_swap₂ (p : R × R) : skew (swap₂ p) = - skew p := by
  unfold skew swap₂; ring

omit [EWSectorSelection R] in
/-- A `σ`-even sector vector has zero skew. -/
theorem skew_plusPart (p : R × R) : skew (plusPart p) = 0 := by
  unfold skew plusPart swap₂
  simp only [Prod.smul_fst, Prod.smul_snd, Prod.fst_add, Prod.snd_add, smul_eq_mul]
  ring

omit [EWSectorSelection R] in
/-- For a non-degenerate carrier, the `σ`-odd skew `a − a⁻¹` is nonzero. -/
theorem sub_inv_ne_zero_of_sq_ne_one (a : Rˣ) (h : ((a : R)) ^ 2 ≠ 1) :
    (a : R) - (a : R)⁻¹ ≠ 0 := by
  intro h0
  apply h
  have he : (a : R) = (a : R)⁻¹ := sub_eq_zero.mp h0
  rw [sq]
  nth_rewrite 2 [he]
  exact mul_inv_cancel₀ a.ne_zero

/-- Charge of an `A₊` carrier vanishes. -/
theorem ewCharge_of_singlet {c : EWCarrier}
    (h : EWSectorSelection.isSinglet (R := R) c = true) :
    ewCharge (R := R) c = 0 := by
  unfold ewCharge sectorVec
  rw [if_pos h]
  exact skew_plusPart _

/-- Charge of an `A₋` carrier is `a − a⁻¹` (the bar-odd skew). -/
theorem ewCharge_of_doublet [Invertible (2 : R)] {c : EWCarrier}
    (h : EWSectorSelection.isSinglet (R := R) c = false) :
    ewCharge (R := R) c =
      (EWSectorSelection.eig (R := R) c : R) - (EWSectorSelection.eig (R := R) c : R)⁻¹ := by
  unfold ewCharge sectorVec
  rw [if_neg (by simp [h])]
  exact skew_minusPart_carrier _

/-- **The sector label is computed by `σ`.** With `2 ∈ Rˣ`, `σ` fixes the sector
vector exactly for `A₊` carriers; so `spinDouble` equals the sector-valued
encoding `0` on `A₊`, `2` on `A₋`. Uses `swap₂_plusPart`, `swap₂_minusPart`,
non-degeneracy, and `2 ≠ 0`. -/
theorem spinDouble_eq_sector [Invertible (2 : R)] (c : EWCarrier) :
    spinDouble (R := R) c = if EWSectorSelection.isSinglet (R := R) c then 0 else 2 := by
  unfold spinDouble
  cases hc : EWSectorSelection.isSinglet (R := R) c
  · -- `A₋`: `σ v = -v`, and `-v = v` would force zero skew
    rw [if_neg]
    · rfl
    intro hfix
    have hsk := congrArg skew hfix
    rw [skew_swap₂] at hsk
    have h2 : (2 : R) * ewCharge (R := R) c = 0 := by
      unfold ewCharge; linear_combination -hsk
    have hz : ewCharge (R := R) c = 0 :=
      (mul_eq_zero.mp h2).resolve_left (isUnit_of_invertible (2 : R)).ne_zero
    rw [ewCharge_of_doublet hc] at hz
    exact sub_inv_ne_zero_of_sq_ne_one _ (EWSectorSelection.eig_sq_ne_one c) hz
  · rw [if_pos]
    · rfl
    unfold sectorVec
    rw [if_pos hc]
    exact swap₂_plusPart _

/-- **Higgs: sector label `0`** — computed from `σ` fixing its sector vector. -/
theorem higgs_scalar [Invertible (2 : R)] : spinDouble (R := R) EWCarrier.H = 0 := by
  rw [spinDouble_eq_sector, EWSectorSelection.higgs_singlet]; rfl

/-- **`W⁺`: sector label `2`.** -/
theorem wPlus_vector [Invertible (2 : R)] : spinDouble (R := R) EWCarrier.Wp = 2 := by
  rw [spinDouble_eq_sector, EWSectorSelection.wPlus_doublet]; rfl

/-- **`W⁻`: sector label `2`.** -/
theorem wMinus_vector [Invertible (2 : R)] : spinDouble (R := R) EWCarrier.Wm = 2 := by
  rw [spinDouble_eq_sector, EWSectorSelection.wMinus_doublet]; rfl

/-- **`Z`: sector label `2`.** -/
theorem z_vector [Invertible (2 : R)] : spinDouble (R := R) EWCarrier.Z = 2 := by
  rw [spinDouble_eq_sector, EWSectorSelection.z_doublet]; rfl

/-- **Higgs is neutral** — its `σ`-even sector vector has zero skew. -/
theorem higgs_neutral : isNeutralByParity (R := R) EWCarrier.H :=
  ewCharge_of_singlet EWSectorSelection.higgs_singlet

/-- **`W⁺` is charged** — nonzero skew `a − a⁻¹` of its `σ`-odd sector vector. -/
theorem wPlus_charged [Invertible (2 : R)] : ¬ isNeutralByParity (R := R) EWCarrier.Wp := by
  unfold isNeutralByParity
  rw [ewCharge_of_doublet EWSectorSelection.wPlus_doublet]
  exact sub_inv_ne_zero_of_sq_ne_one _ (EWSectorSelection.eig_sq_ne_one _)

/-- **`W⁻` has the opposite charge to `W⁺`** — its eigenvalue is the `σ`-image,
and the skew changes sign under `a ↦ a⁻¹`. -/
theorem wMinus_charge_neg [Invertible (2 : R)] :
    ewCharge (R := R) EWCarrier.Wm = - ewCharge (R := R) EWCarrier.Wp := by
  rw [ewCharge_of_doublet EWSectorSelection.wMinus_doublet,
    ewCharge_of_doublet EWSectorSelection.wPlus_doublet, EWSectorSelection.wMinus_eig]
  simp only [Units.val_inv_eq_inv_val, inv_inv]
  ring

/-- **Honest negative: `σ`-parity does not make `Z` neutral.** `Z` is in `A₋`, so
its skew charge is nonzero. The neutrality of `Z` (`ewT3Double Z = 0`) is not a
parity consequence; it rests on the Weinberg mixing (cf.
`signed_C_does_not_force_W_slot_but_forces_neutral_mixed`). -/
theorem z_not_neutral_by_parity [Invertible (2 : R)] : ¬ isNeutralByParity (R := R) EWCarrier.Z := by
  unfold isNeutralByParity
  rw [ewCharge_of_doublet EWSectorSelection.z_doublet]
  exact sub_inv_ne_zero_of_sq_ne_one _ (EWSectorSelection.eig_sq_ne_one _)

/-- **Theorem (sector label and charge computed through `σ`).**

    Conditional on the postulate `EWSectorSelection` (sectors, eigenvalues,
    `W⁻` = `σ`-image of `W⁺`, non-degeneracy), the action of `σ = swap₂` on the
    sector vectors gives: `H` has sector label `0` and zero charge; `W±, Z` have
    sector label `2`; `W⁺` has nonzero charge and `W⁻` the opposite charge.
    The `T₃` table `ewT3Double` is not part of this theorem. -/
theorem ew_charge_spin_forced [Invertible (2 : R)] :
    spinDouble (R := R) EWCarrier.H = 0 ∧
    spinDouble (R := R) EWCarrier.Wp = 2 ∧
    spinDouble (R := R) EWCarrier.Wm = 2 ∧
    spinDouble (R := R) EWCarrier.Z = 2 ∧
    ewCharge (R := R) EWCarrier.H = 0 ∧
    ewCharge (R := R) EWCarrier.Wp ≠ 0 ∧
    ewCharge (R := R) EWCarrier.Wm = - ewCharge (R := R) EWCarrier.Wp :=
  ⟨higgs_scalar, wPlus_vector, wMinus_vector, z_vector,
    higgs_neutral, wPlus_charged, wMinus_charge_neg⟩

/-! ## Task 2 — the σ₅⁸ bar-grading is DERIVED from spin (not merely stated)

The sector→spin map `spinDouble` (singlet ↦ 0, doublet ↦ 2) is injective, so it
**inverts**: spin determines the sector. Physically, an object's spin is an
independent measured input — the Higgs boson is a scalar (spin 0), the
hypercharge gauge boson `B` is a vector (spin 1) — and the spin-involution
grading law of `def:spin-involution` (`A₊` = spin-singlet, `A₋` = spin-doublet)
then *forces* the sector. This upgrades the owner-ruled σ₅⁸ H/B bar-grading from
a bare postulate to a spin-derived theorem: the only residual postulate is that
`H` and `B` inhabit the *one* σ₅⁸ slot; the *grading* of that slot is derived. -/

/-- **Spin forces the sector (the injective inverse of `spinDouble`).** A scalar
(`spinDouble c = 0`) must inhabit the singlet `A₊` (`isSinglet = true`); a vector
(`spinDouble c = 2`) must inhabit the doublet `A₋` (`isSinglet = false`). The
sector is *determined* by the spin — it is not an independent free choice once
the spin is fixed. -/
theorem sector_forced_by_spin [Invertible (2 : R)] (c : EWCarrier) :
    (spinDouble (R := R) c = 0 → EWSectorSelection.isSinglet (R := R) c = true) ∧
    (spinDouble (R := R) c = 2 → EWSectorSelection.isSinglet (R := R) c = false) := by
  rw [spinDouble_eq_sector]
  cases EWSectorSelection.isSinglet (R := R) c <;> simp

/-- Bar-sector recovered from the (doubled) spin via the spin-involution grading
law of `def:spin-involution`: `A₊` (bar-even singlet) `⟺ 2s = 0`, `A₋` (bar-odd
doublet) `⟺ 2s = 2`. `true = A₊`, `false = A₋`. -/
def barSectorOfSpin (twoS : ℕ) : Bool := twoS == 0

/-- **`barSectorOfSpin` is a genuine two-sided inverse of the spin grading.** For
every EW carrier it recovers the sector from the spin (`barSectorOfSpin ∘
spinDouble = isSinglet`). This injectivity is what makes "spin forces sector" a
*derivation* rather than a re-postulation. -/
theorem barSectorOfSpin_inverts [Invertible (2 : R)] (c : EWCarrier) :
    barSectorOfSpin (spinDouble (R := R) c) = EWSectorSelection.isSinglet (R := R) c := by
  rw [spinDouble_eq_sector]
  unfold barSectorOfSpin
  cases EWSectorSelection.isSinglet (R := R) c <;> rfl

/-- The two occupants of the Hoefsmit slot `σ₅⁸` (`= T(2,8)`, strands 5–6): the
Higgs boson `H` and the `U(1)_Y` hypercharge gauge boson `B`. The residual
sector postulate is *only* that both inhabit this one slot; their bar-sectors
are DERIVED from spin below. -/
inductive Sigma58
  | higgs   -- the Higgs boson H
  | hyperB  -- the U(1)_Y hypercharge gauge boson B
deriving DecidableEq

/-- Physical (Standard-Model measured) doubled spin of each σ₅⁸ occupant: the
Higgs is a scalar (`2s = 0`), the hypercharge boson `B` is a vector (`2s = 2`).
These are independent physical inputs, **not** sector assignments. -/
def spin58 : Sigma58 → ℕ
  | .higgs  => 0
  | .hyperB => 2

/-- **σ₅⁸ bar-grading FORCED by spin (Task 2 — derived, not stated).** Given only
the physical spins, the Higgs (scalar, `2s = 0`) is forced into `A₊` (bar-even
singlet) and the hypercharge boson `B` (vector, `2s = 2`) into `A₋` (bar-odd
doublet), through the same spin↔sector inversion (`barSectorOfSpin`,
`barSectorOfSpin_inverts`) that governs the whole triplet. The σ₅⁸ H/B grading
is therefore a *consequence* of the two carriers' spins, not an owner postulate;
the single residual postulate is that both `H` and `B` occupy the one σ₅⁸ slot. -/
theorem ew_sigma5_bargrade_forced :
    barSectorOfSpin (spin58 Sigma58.higgs) = true ∧
    barSectorOfSpin (spin58 Sigma58.hyperB) = false := by
  decide

/-! ## Task 1 — is which-slot-is-`W` (σ₁⁴ vs σ₃⁶) forced? (HONEST: no)

The corpus does supply a crossing→charge map — `def:coulomb-charge`,
`Q(𝔥) = ½(n₊ − n₋) = writhe/2`. But on the all-positive even-twist braid
`σ₁^{2k}` it gives `Q(T(2, 2k)) = k > 0` for *every* carrier (`k = 2, 3, 4`), so
it makes `W`, `Z`, `H` all charged and does **not** single out the neutral slot.
The corpus further records `writhe → Q` as FAILED and `writhe → Y` as FALSIFIED
(`docs/audits/2026-06-02-u1-hypercharge-assignment.md`: only `writhe → I₃`
survives, and Gell-Mann–Nishijima `Y = 2(Q − I₃)` needs a *second* independent
crossing/trace charge the framework does not supply). Consequently which
sub-saturating slot hosts the charged carrier is a **free label**. Below:
(i) the *forced* part — the charged carriers are bar-odd `A₋` doublets and the
`A₊` singlet is neutral; and (ii) the *underdetermination* — two distinct
crossing→isospin labelings both satisfy every proved constraint. -/

/-- **Forced part of the charge labeling.** From the sector postulate, computed
through `σ`: a carrier with nonzero skew charge is in the bar-odd sector `A₋`
(contrapositive of `ewCharge_of_singlet`), so the charged `W±` are `A₋` carriers,
and the `A₊` Higgs has zero charge. What is **not** entailed is which crossing
slot the charged pair occupies — that is the free label of `which_slot_is_W_free`. -/
theorem charged_are_doublets_singlet_neutral [Invertible (2 : R)] :
    (∀ c : EWCarrier, ewCharge (R := R) c ≠ 0 →
      EWSectorSelection.isSinglet (R := R) c = false) ∧
    ewCharge (R := R) EWCarrier.Wp ≠ 0 ∧
    ewCharge (R := R) EWCarrier.Wm ≠ 0 ∧
    ewCharge (R := R) EWCarrier.H = 0 := by
  refine ⟨fun c hc => ?_, wPlus_charged, ?_, higgs_neutral⟩
  · cases h : EWSectorSelection.isSinglet (R := R) c
    · rfl
    · exact absurd (ewCharge_of_singlet h) hc
  · rw [wMinus_charge_neg]
    exact neg_ne_zero.mpr wPlus_charged

/-- A crossing→isospin labeling of the two *vector* (`A₋` doublet) electroweak
slots, indexed by their crossing counts. `t3` gives the doubled isospin at each
admissible crossing count `4` (`σ₁⁴`) and `6` (`σ₃⁶`); a valid electroweak
labeling puts the charged carrier (`|t3| = 1`) on exactly one of the two slots
and the neutral carrier (`t3 = 0`) on the other. Nothing in the proved core
distinguishes the two ways of doing this. -/
structure EWVectorLabeling where
  /-- Doubled isospin at each crossing count. -/
  t3 : ℕ → ℤ
  /-- Exactly one of the two vector slots (`4` or `6`) carries the charge. -/
  charged_at_4_xor_6 : (t3 4 = 1 ∧ t3 6 = 0) ∨ (t3 4 = 0 ∧ t3 6 = 1)

/-- The paper's labeling: charged `W` at the 4-crossing slot `σ₁⁴`, neutral `Z`
at the 6-crossing slot `σ₃⁶`. -/
def labelWat4 : EWVectorLabeling where
  t3 := fun k => if k = 4 then 1 else 0
  charged_at_4_xor_6 := Or.inl ⟨by decide, by decide⟩

/-- The mirror labeling: charged `W` at the 6-crossing slot `σ₃⁶`, neutral at
`σ₁⁴`. Equally admissible under the proved constraints. -/
def labelWat6 : EWVectorLabeling where
  t3 := fun k => if k = 6 then 1 else 0
  charged_at_4_xor_6 := Or.inr ⟨by decide, by decide⟩

/-- **Which slot is `W` is UNDETERMINED (a free label).** Both `labelWat4` (the
paper's `W = σ₁⁴`) and `labelWat6` (`W = σ₃⁶`) are valid `EWVectorLabeling`s and
they disagree on the charged slot (`t3 4 = 1` vs `t3 4 = 0`). No *proved*
crossing→charge principle selects between them: the corpus `writhe → Q` map
(`Q = ½·writhe`) makes *every* even-twist carrier charged (`Q = k`), and
`writhe → Y` is falsified. Hence `W = σ₁⁴` is a labeling choice — supported by
the mass ordering `4 < 6 < 8` (necessary, not sufficient) — and **not** a
theorem. What *would* force it is a genuine crossing/linking → `T₃` (or electric
charge) map assigning the neutral label to exactly the `Z` slot; the corpus does
not yet supply one. -/
theorem which_slot_is_W_free :
    labelWat4.t3 4 = 1 ∧ labelWat6.t3 4 = 0 ∧ labelWat4 ≠ labelWat6 := by
  refine ⟨by decide, by decide, ?_⟩
  intro h
  have hne : labelWat4.t3 4 = labelWat6.t3 4 := congrArg (fun L => L.t3 4) h
  revert hne
  decide

/-! ### The one surviving crossing→charge map (`writhe → I₃`) also fails to
select the neutral slot

The corpus U(1)-assignment audit
(`docs/audits/2026-06-02-u1-hypercharge-assignment.md`) found that of the three
crossing→quantum-number maps, `writhe → Q` FAILS and `writhe → Y` is FALSIFIED,
while **`writhe → I₃` survives** — but only as a *sign+ratio* map `2·I₃ = writhe`
keyed on the **crossing sign**. It matched the nucleon doublet because `p` and
`n` differ by the `σ ↔ σ⁻¹` (`u ↔ d`) crossing-sign flip: `w(p) = +1`,
`w(n) = −1`, giving `I₃(p) = +½`, `I₃(n) = −½`.

One might hope this surviving map, evaluated on the even-twist carriers, singles
out the neutral `Z` slot. **It does not.** The carriers `T(2, 2k) = σ₁^{2k}` are
*all-positive* torus links: writhe `n₊ − n₋ = 2k` with *no* negative crossings.
So the surviving map assigns them a uniformly positive, strictly monotone
`2·I₃ = 2k` — a magnitude / twist ladder (the exact analogue of the audit's
`θ_j = q^{j(j+1)}` spin ladder: monotone, no sign change, no zero), **not** an
additive sign charge. It is nonzero on *both* vector slots `σ₁⁴` (`k = 2`) and
`σ₃⁶` (`k = 3`), so it produces no neutral slot and cannot furnish the
`charged_at_4_xor_6` datum of an `EWVectorLabeling`. The reason is structural:
`I₃`'s sign *is* the crossing sign, and the two same-sign vector carriers offer
no crossing-sign flip for the map to act on — exactly the flip that produced the
`p/n` split is absent among the all-positive even-twist links.

Hence admitting the one surviving map **strengthens, rather than closes,**
`which_slot_is_W_free`: the which-slot-is-`W` label remains free. What *would*
force it is a genuinely *signed* crossing/linking → `T₃` invariant (a carrier
realisation with a `σ ↔ σ⁻¹` asymmetry making one vector slot's net writhe zero),
or the second independent baryon/color-trace charge the audit names — neither of
which the framework supplies for the same-sign even-twist triple. -/

/-- Writhe of the all-positive even-twist torus link `T(2, 2k)` = closure of the
positive braid `σ₁^{2k}`: `2k` positive crossings, no negative crossings, so
`w = n₊ − n₋ = 2k`. -/
def evenTwistWrithe (k : ℕ) : ℤ := 2 * (k : ℤ)

/-- Doubled isospin `2·I₃` assigned by the surviving audit map `writhe → I₃`
(`2·I₃ = writhe`) to the even-twist carrier `T(2, 2k)`. Since the carrier is the
all-positive braid `σ₁^{2k}` (writhe `2k`), this equals `2k`. -/
def evenTwistDoubledI3 (k : ℕ) : ℤ := evenTwistWrithe k

@[simp] theorem evenTwistDoubledI3_eq (k : ℕ) : evenTwistDoubledI3 k = 2 * (k : ℤ) := rfl

/-- **The surviving `writhe → I₃` map assigns strictly positive isospin to every
even-twist carrier.** In particular both vector slots `k = 2` (σ₁⁴) and `k = 3`
(σ₃⁶) get `2·I₃ > 0` — neither is neutral. -/
theorem evenTwist_doubledI3_pos {k : ℕ} (hk : 1 ≤ k) : 0 < evenTwistDoubledI3 k := by
  simp only [evenTwistDoubledI3_eq]; omega

/-- **`writhe → I₃` is a monotone twist ladder, not a sign charge.** Across the
carriers it strictly increases (`k = 2 ↦ 4 < k = 3 ↦ 6 < k = 4 ↦ 8`) with no sign
change and no zero — the signature of a magnitude / spin ladder (audit §3), not
of an additive charge. -/
theorem evenTwist_doubledI3_strictMono :
    evenTwistDoubledI3 2 < evenTwistDoubledI3 3 ∧
    evenTwistDoubledI3 3 < evenTwistDoubledI3 4 := by
  constructor <;> decide

/-- **Every valid `EWVectorLabeling` has a neutral vector slot.** The
`charged_at_4_xor_6` datum puts the charge (`t3 = 1`) on exactly one of the two
vector slots, so the *other* slot is neutral (`t3 = 0`) — this is the `Z`. Any
electroweak labeling therefore *requires* one of `{σ₁⁴, σ₃⁶}` to carry `t3 = 0`. -/
theorem EWVectorLabeling.has_neutral_slot (L : EWVectorLabeling) :
    L.t3 4 = 0 ∨ L.t3 6 = 0 := by
  rcases L.charged_at_4_xor_6 with ⟨_, h⟩ | ⟨h, _⟩
  · exact Or.inr h
  · exact Or.inl h

/-- **The surviving `writhe → I₃` map is INCOMPATIBLE with any valid electroweak
labeling** (the non-vacuous negative result). Two facts do the work:

* the writhe-derived doubled isospin is **nonzero on every carrier** — `2·I₃(σ₁⁴)
  = 4 ≠ 0`, `2·I₃(σ₃⁶) = 6 ≠ 0`, `2·I₃(σ₅⁸) = 8 ≠ 0` (the all-positive braids
  have no zero-writhe slot);
* every valid `EWVectorLabeling` **requires** a neutral (`t3 = 0`) vector slot
  (`has_neutral_slot`) — the `Z`.

Since the writhe map never produces the required `0`, **no** valid labeling can
agree with it on the two vector slots. The proof genuinely uses the nonzeroness
of the writhe assignment against the labeling's mandatory neutral slot — it is
*not* true by the `t3 ∈ {0,1}` type constraint alone. Hence the one
crossing→quantum-number map that survives the U(1)-assignment audit assigns
*all* carriers a nonzero isospin and so **cannot select the neutral `Z` slot**;
which-slot-is-`W` remains a **free label**, strengthening rather than closing
`which_slot_is_W_free`. -/
theorem writheI3_does_not_select_neutral_slot :
    evenTwistDoubledI3 2 ≠ 0 ∧ evenTwistDoubledI3 3 ≠ 0 ∧ evenTwistDoubledI3 4 ≠ 0 ∧
    ¬ ∃ L : EWVectorLabeling,
        L.t3 4 = evenTwistDoubledI3 2 ∧ L.t3 6 = evenTwistDoubledI3 3 := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  rintro ⟨L, h4, h6⟩
  -- a valid labeling has a neutral (`t3 = 0`) slot; the writhe map is nonzero there
  rcases L.has_neutral_slot with h | h
  · rw [h4] at h; exact absurd h (by decide)
  · rw [h6] at h; exact absurd h (by decide)

/-! ## Task 1′ — the SIGNED `σ ↔ σ⁻¹` criterion and the C-invariance neutrality
test: which-slot-is-`W` is STILL free, and the neutral slot is forced to be MIXED

`writheI3_does_not_select_neutral_slot` used the *unsigned* surviving map on the
all-positive carriers. The prior result named the two ingredients that *might*
force the label: a **signed** `σ ↔ σ⁻¹` crossing asymmetry, and a second
baryon/color-trace charge. This section tests the signed / charge-conjugation
route and proves the sharper negative honestly.

**Charge conjugation is crossing reversal** (`predicted-spectra/
chirality-trefoil-electron-positron`): `C = σ ↔ σ⁻¹` reverses every crossing, so
it negates the signed writhe and `Q(𝔭^σ) = −Q(𝔭)`. A carrier is **neutral iff it
is a fixed point of `C`** (its own antiparticle) — i.e. **C-invariant**, i.e.
**amphichiral** (`w = −w`). The signed test therefore replaces the all-positive
magnitude ladder with a genuine sign charge; below it is shown to (i) leave ≥ 2
labelings consistent (no forcing), while (ii) *excluding every pure even-twist
slot* from being the neutral member — so the neutral `Z` is necessarily the mixed
`W³/B → Z` (Weinberg) state, not a single slot. -/

section SignedCrossing

/-- Charge conjugation `C` on the signed writhe: crossing reversal `σ ↔ σ⁻¹`
negates every crossing sign, hence negates the writhe (`predicted-spectra/
chirality-trefoil-electron-positron`: `Q(𝔭^σ) = −Q(𝔭)`). -/
def crossingReversal (w : ℤ) : ℤ := -w

/-- `C` is an involution (`σ² = id`), matching the fibre-adjoint involution of
`chirality-trefoil`. -/
theorem crossingReversal_involutive (w : ℤ) :
    crossingReversal (crossingReversal w) = w := by
  unfold crossingReversal; ring

/-- **C-invariance ⟺ amphichirality ⟺ zero signed writhe.** A carrier is a fixed
point of charge conjugation (its own antiparticle — the neutrality criterion of
`chirality-trefoil`) exactly when its signed writhe vanishes. Over `ℤ` the content
is `−w = w ↔ 2w = 0 ↔ w = 0` — the load-bearing step (`omega`), *not* a type
tautology. -/
theorem cInvariant_iff_writhe_zero (w : ℤ) : crossingReversal w = w ↔ w = 0 := by
  unfold crossingReversal; omega

/-- **Signed** writhe of the pure even-twist carrier `T(2,2k) = σ₁^{2k}`: `+2k`
(all crossings positive). Same value as `evenTwistWrithe`, restated in the signed
layer. -/
def evenTwistSignedWrithe (k : ℕ) : ℤ := 2 * (k : ℤ)

/-- **No pure even-twist carrier is C-invariant / amphichiral.** For `k ≥ 1` the
signed writhe `2k ≠ 0`, so `C` never fixes it: the all-positive braid `σ₁^{2k}` is
genuinely chiral. Hence **no pure even-twist slot** can be the neutral (C-fixed)
electroweak member. The proof genuinely runs `cInvariant_iff_writhe_zero` against
`2k ≠ 0` — it is not vacuous. -/
theorem evenTwist_not_cInvariant {k : ℕ} (hk : 1 ≤ k) :
    crossingReversal (evenTwistSignedWrithe k) ≠ evenTwistSignedWrithe k := by
  rw [Ne, cInvariant_iff_writhe_zero]
  unfold evenTwistSignedWrithe; omega

/-- A **signed** crossing→charge labeling of the two vector slots (crossing counts
`4` and `6`): each slot carries a signed writhe, and — by
`cInvariant_iff_writhe_zero` — the **neutral** slot is the C-invariant one
(`sw = 0`) and the **charged** slot the chiral one (`sw ≠ 0`). A valid electroweak
labeling makes exactly one vector slot neutral (the `Z`/`W³`) and the other
charged (the `W`). -/
structure SignedEWLabeling where
  /-- Signed writhe at each vector-slot crossing count. -/
  sw : ℕ → ℤ
  /-- Exactly one vector slot is C-invariant (neutral); the other is chiral. -/
  neutral_at_4_xor_6 :
    (sw 4 = 0 ∧ sw 6 ≠ 0) ∨ (sw 4 ≠ 0 ∧ sw 6 = 0)

/-- The paper's signed labeling: charged `W` (chiral, `sw = 2`) at slot `4`,
neutral `Z`/`W³` (amphichiral, `sw = 0`) at slot `6`. -/
def signedWat4 : SignedEWLabeling where
  sw := fun k => if k = 4 then 2 else 0
  neutral_at_4_xor_6 := Or.inr ⟨by decide, by decide⟩

/-- The mirror signed labeling: neutral at slot `4`, charged `W` (chiral,
`sw = 2`) at slot `6`. Equally C-consistent. -/
def signedWat6 : SignedEWLabeling where
  sw := fun k => if k = 6 then 2 else 0
  neutral_at_4_xor_6 := Or.inl ⟨by decide, by decide⟩

/-- **The signed / C-invariance criterion does NOT force which slot is `W`.** Both
`signedWat4` (paper: `W` chiral at slot 4, `Z` amphichiral at slot 6) and
`signedWat6` (mirror) are valid `SignedEWLabeling`s satisfying the full
charge-conjugation neutrality constraint, yet they disagree on the charged slot
(`sw 4 = 2` vs `sw 4 = 0`). Admitting the *signed* `σ ↔ σ⁻¹` asymmetry — the first
ingredient the prior result named — therefore leaves ≥ 2 labelings consistent: it
constrains the neutral slot to be **amphichiral**, but not **which** slot. -/
theorem signed_which_slot_is_W_free :
    signedWat4.sw 4 = 2 ∧ signedWat6.sw 4 = 0 ∧ signedWat4 ≠ signedWat6 := by
  refine ⟨by decide, by decide, ?_⟩
  intro h
  have hne : signedWat4.sw 4 = signedWat6.sw 4 := congrArg (fun L => L.sw 4) h
  revert hne; decide

/-- **What WOULD force the label: a second charge nonzero on exactly one slot.** If
a hypothetical second (baryon/color-trace) charge `S : ℕ → ℤ` vanishes on one
vector slot and is nonzero on the other — reading "neutral ⟺ `S` vanishes" — it
*determines* the neutral slot uniquely. This is the precise missing object the
prior result and the U(1)-assignment audit named
(`docs/audits/2026-06-02-u1-hypercharge-assignment.md`: "the precise missing
object is a SECOND, independent crossing invariant (a baryon-number / color-trace
charge)"). The corpus does **not** supply such an `S` for the same-sign even-twist
triple; this conditional makes "fixed only by the second-charge / mixing data"
precise. -/
theorem second_charge_would_force_neutral_slot
    (S : ℕ → ℤ) (hS : S 4 = 0 ∧ S 6 ≠ 0) :
    ∀ j : ℕ, (j = 4 ∨ j = 6) → (S j = 0 ↔ j = 4) := by
  obtain ⟨h4, h6⟩ := hS
  intro j hj
  rcases hj with rfl | rfl
  · exact iff_of_true h4 rfl
  · exact iff_of_false h6 (by decide)

/-- **Capstone (honest stronger negative).** Neither ingredient the prior result
named forces which pure even-twist slot hosts the charged `W`:

* the **signed `σ ↔ σ⁻¹` asymmetry** leaves ≥ 2 C-consistent labelings — two
  distinct labelings disagree on the `W` slot (`signedWat4 ≠ signedWat6`, and
  `sw 4` differs);
* the neutrality criterion **is** C-invariance ⟺ amphichirality (`∀ w, −w = w ↔
  w = 0`), and **no pure even-twist carrier is amphichiral** — all three carriers
  `σ₁⁴` (k=2), `σ₃⁶` (k=3), `σ₅⁸` (k=4) are chiral — so the neutral electroweak
  boson is *necessarily not a single even-twist slot* but the **mixed `W³/B → Z`
  (Weinberg) state**.

Hence which-slot-is-`W` is fixed **only by the mixing / combination data**, not by
any single-slot topological invariant — strengthening `which_slot_is_W_free` with
the *reason*: the correct neutrality criterion (charge-conjugation invariance)
excludes every chiral slot from being neutral. The remaining tie-breaker, a second
baryon/color-trace charge (`second_charge_would_force_neutral_slot`), is a missing
corpus object, not supplied. -/
theorem signed_C_does_not_force_W_slot_but_forces_neutral_mixed :
    (signedWat4 ≠ signedWat6 ∧ signedWat4.sw 4 ≠ signedWat6.sw 4) ∧
    (∀ w : ℤ, crossingReversal w = w ↔ w = 0) ∧
    (crossingReversal (evenTwistSignedWrithe 2) ≠ evenTwistSignedWrithe 2 ∧
     crossingReversal (evenTwistSignedWrithe 3) ≠ evenTwistSignedWrithe 3 ∧
     crossingReversal (evenTwistSignedWrithe 4) ≠ evenTwistSignedWrithe 4) := by
  refine ⟨⟨signed_which_slot_is_W_free.2.2, by decide⟩, cInvariant_iff_writhe_zero, ?_, ?_, ?_⟩
  · exact evenTwist_not_cInvariant (by norm_num)
  · exact evenTwist_not_cInvariant (by norm_num)
  · exact evenTwist_not_cInvariant (by norm_num)

/-! ### The NAMED second-charge candidates (linking, triple-linking) also fail

The `second_charge_would_force_neutral_slot` conditional needs a charge that is
nonzero on *exactly one* vector slot. The audit
(`docs/audits/2026-06-02-u1-hypercharge-assignment.md`) names the missing object
as a baryon / color-trace charge; its two natural knot-theoretic realizations are
the pairwise linking number `Lk` and the Milnor triple linking `μ̄(123)`. Below,
neither meets the forcing hypothesis — the negative is sharpened from "no such
charge in the corpus" to "the two natural candidates provably do not force." -/

/-- Pairwise linking number of the even-twist carrier `T(2,2k)`: the two strands
of the `(2,2k)` torus link wind `k` times, so `lk(T(2,2k)) = k`. Models the
categorical linking operation `Lk_R` (`conj:categorical-linking-operation`). -/
def evenTwistLinkingNumber (k : ℕ) : ℤ := k

/-- Milnor triple linking number `μ̄(123)` of the even-twist carrier. `T(2,2k)` is
a **two**-component link, and the triple linking number requires **≥ 3**
components, so it vanishes identically. Models the baryon / color-trace charge the
U(1)-assignment audit names (`docs/audits/2026-06-02-u1-hypercharge-assignment.md`;
cf. the three-strand color structure of `observations/hadron-proton-example`). -/
def evenTwistTripleLinking (_k : ℕ) : ℤ := 0

/-- **The named second-charge candidates do NOT force the label.** The forcing
hypothesis of `second_charge_would_force_neutral_slot` demands a charge that is
zero on one vector slot and nonzero on the other. Neither candidate qualifies:

* the Milnor triple linking `μ̄(123) ≡ 0` on **every** even-twist carrier (a
  2-component link has no triple) — it vanishes on BOTH slots, so it produces no
  charged slot;
* the pairwise linking `Lk(T(2,2k)) = k ≠ 0` on **every** carrier (`k = 2,3,4`) —
  it vanishes on NEITHER slot, so it produces no neutral slot.

Both halves do real work (`rfl`-per-`k` / `decide`), not a vacuous ¬∃: one
exhibits a charge that is identically zero, the other a charge that is nowhere
zero — the two distinct ways of missing the "nonzero on exactly one slot" datum
that `second_charge_would_force_neutral_slot` requires. -/
theorem named_second_charge_candidates_do_not_force_label :
    (∀ k : ℕ, evenTwistTripleLinking k = 0) ∧
    (evenTwistLinkingNumber 2 ≠ 0 ∧ evenTwistLinkingNumber 3 ≠ 0 ∧
     evenTwistLinkingNumber 4 ≠ 0) := by
  refine ⟨fun _ => rfl, ?_, ?_, ?_⟩ <;>
    · unfold evenTwistLinkingNumber; decide

/-! ### The group-structure data DOES force the label (§3b-cond conditional positive)

Topology cannot force which vector slot is the charged `W` (Task 1′ above), but
the `su(2)_L × u(1)_Y` group assignment can. We axiomatise the *genuine* missing
input as an open hypothesis class — the alignment of the two `A₋` vector slots
with the `su(2)_L` Cartan–Weyl basis — and DERIVE the `T₃` label from it. Per
§3b-cond, the class carries the *hypothesis* (which slot is the neutral Cartan
member `W³`), and the theorem *derives* the `T₃` conclusion via the adjoint
zero-weight rule; it does not carry `T₃` as a field. No instance is supplied — the
group assignment stays an open input (exactly the `(W³,B)→(Z,γ)` mixing data of
`conj:weinberg-angle-categorical`). -/

/-- The two `A₋` vector slots (crossing counts `4` and `6`) hosting the charged
`W±` and the neutral `W³/Z`. -/
inductive VectorSlot
  | s4  -- σ₁⁴ = T(2,4)
  | s6  -- σ₃⁶ = T(2,6)
deriving DecidableEq

/-- **The group-assignment datum (open §3b hypothesis class).** The genuine input
the topological invariants cannot supply: the alignment of the two vector slots
with the `su(2)_L` Cartan–Weyl basis. The fields carry WHICH slot is the neutral
`su(2)_L` Cartan generator `W³` (→ `Z`) versus the charged `W±` root member —
a group-theoretic datum, NOT the `T₃` values (those are derived below). The
`cartan_ne_charged` field is the genuine non-degeneracy of the Cartan–Weyl split
of the adjoint triplet (exactly one neutral Cartan direction, complementary root).
No instance is provided; it is the open `(W³,B)→(Z,γ)` mixing input of
`conj:weinberg-angle-categorical`. -/
class EWGroupAssignment where
  /-- Which vector slot hosts the neutral `su(2)_L` Cartan member `W³` (→ `Z`). -/
  cartanSlot : VectorSlot
  /-- Which vector slot hosts the charged `W±` root member. -/
  chargedSlot : VectorSlot
  /-- The Cartan (neutral) and root (charged) slots are distinct — the
  non-degeneracy of the Cartan–Weyl split of the adjoint triplet. -/
  cartan_ne_charged : cartanSlot ≠ chargedSlot

/-- **Derived doubled isospin `2·T₃` from the group assignment.** The neutral
Cartan member `W³` sits in the **zero-weight** space of the `su(2)_L` adjoint, so
`T₃ = 0`; the complementary root member `W±` has `|T₃| = 1` (`2·T₃` magnitude
`2`). These are the adjoint weights `{+1, 0, −1}`, applied to the group datum — a
derivation, not a re-postulation of `T₃`. -/
def derivedDoubledT3 [EWGroupAssignment] (s : VectorSlot) : ℤ :=
  if s = EWGroupAssignment.cartanSlot then 0 else 2

/-- **The W/Z label IS forced, given the group assignment (§3b-cond conditional
positive; answers "can you prove it?").** No single-slot topological invariant
forces which slot is the charged `W`
(`named_second_charge_candidates_do_not_force_label`, `signed_which_slot_is_W_free`),
but the `su(2)_L × u(1)_Y` group datum `EWGroupAssignment` DOES: the neutral
`W³→Z` slot is the Cartan slot (`2·T₃ = 0`), the charged `W±` slot is the
complementary root slot (`2·T₃ = 2`), and a slot is neutral **iff** it is the
Cartan slot — each DERIVED from the group assignment via the adjoint
zero-weight rule (`derivedDoubledT3`), not projected. The label is determined:
the charged slot is exactly the non-Cartan slot. This relocates the postulate
from a bare `T₃` label to the group-structure (mixing) input — it does not
fabricate a topological forcing. -/
theorem label_forced_given_group_assignment [EWGroupAssignment] :
    derivedDoubledT3 EWGroupAssignment.cartanSlot = 0 ∧
    derivedDoubledT3 EWGroupAssignment.chargedSlot = 2 ∧
    (∀ s : VectorSlot, derivedDoubledT3 s = 0 ↔ s = EWGroupAssignment.cartanSlot) := by
  refine ⟨?_, ?_, ?_⟩
  · unfold derivedDoubledT3; rw [if_pos rfl]
  · unfold derivedDoubledT3; rw [if_neg (EWGroupAssignment.cartan_ne_charged).symm]
  · intro s
    unfold derivedDoubledT3
    by_cases h : s = EWGroupAssignment.cartanSlot
    · rw [if_pos h]; exact iff_of_true rfl h
    · rw [if_neg h]; exact iff_of_false (by decide) h

end SignedCrossing


/-! ## Spin-2 no-go for the `Bool`-sector encoding, and its `ℕ`-graded extension

`spinDouble` factors through the two-valued sector `isSinglet : EWCarrier → Bool`
(singlet `↦ 0`, doublet `↦ 2`). It is therefore a `ℤ/2`-valued label in disguise,
and that is enough for the electroweak carriers, which have spin `0` or `1`.

It is *not* enough for the spin-`2` summand `V₂ = Sym²(V₁) ⊖ V₀` of the gauge
`SU(2)` (`QOU.Eightfold.Sym2AdjointSpinTwo.adjoint_sym2_traceless_is_spin_two`).
This section records, precisely, that the existing encoding cannot represent
spin `2`, and gives an extension that can, which restricts to the existing
encoding on the electroweak carriers.

* `spinDouble_ne_four` — no carrier has doubled spin `4`;
* `bool_sector_not_injective_on_spins` — *any* two-valued sector map, whatever
  its values, identifies two of the spins `0, 1, 2`; so the obstruction is the
  `ℤ/2` target, not the particular choice `0 ↦ 0, 1 ↦ 2`;
* `barSectorOfSpin_spinOne_eq_spinTwo` — the existing inverse `barSectorOfSpin`
  sends spin `1` and spin `2` to the same sector;
* `GradedSpin` — doubled spin as an unrestricted natural number (the
  non-negative part of `ℤ`; the same `twice_j` convention as `QOU.SpinLabels`),
  with `GradedSpin.ofSector` / `GradedSpin.toSector` the embedding of the old
  encoding and its retraction. `GradedSpin` is a wrapper around `ℕ`; it adds a
  value range, not new mathematics, and it is linked to
  `QOU.Eightfold.Sym2AdjointSpinTwo.spinTwo` only by the shared `twice_j`
  convention, not by an import.

Nothing in this section says that any electroweak carrier, or any object at all,
*has* spin `2`. -/

section SpinTwoNoGo

/-- The `Bool`-sector encoding that `spinDouble` factors through:
singlet (`true`) `↦ 0`, doublet (`false`) `↦ 2`. -/
def sectorSpinDouble (b : Bool) : ℕ := if b then 0 else 2

/-- The encoding takes only the values `0` and `2`. -/
theorem sectorSpinDouble_mem (b : Bool) :
    sectorSpinDouble b = 0 ∨ sectorSpinDouble b = 2 := by
  cases b <;> decide

/-- The encoding never takes the value `4` (doubled spin of `V₂`). -/
theorem sectorSpinDouble_ne_four (b : Bool) : sectorSpinDouble b ≠ 4 := by
  cases b <;> decide

/-- **No-go (spin 2 is not representable).** For every sector selection, no
electroweak carrier has `spinDouble = 4`, i.e. spin `2`. -/
theorem spinDouble_ne_four [Invertible (2 : R)] (c : EWCarrier) :
    spinDouble (R := R) c ≠ 4 := by
  -- `spinDouble = sectorSpinDouble ∘ isSinglet` by `spinDouble_eq_sector`.
  rw [spinDouble_eq_sector]
  exact sectorSpinDouble_ne_four (EWSectorSelection.isSinglet (R := R) c)

/-- **No-go, independent of the encoding's values.** A map from doubled spin to
a two-valued sector cannot separate the three spins `0, 1, 2` (doubled: `0, 2,
4`): two of them always share a sector (pigeonhole). -/
theorem bool_sector_not_injective_on_spins (f : ℕ → Bool) :
    f 0 = f 2 ∨ f 0 = f 4 ∨ f 2 = f 4 := by
  cases h0 : f 0 <;> cases h2 : f 2 <;> cases h4 : f 4 <;> decide

/-- The existing inverse `barSectorOfSpin` sends spin `1` and spin `2` to the
same (doublet) sector: it inverts `spinDouble` on `{0, 2}` only. -/
theorem barSectorOfSpin_spinOne_eq_spinTwo :
    barSectorOfSpin 2 = barSectorOfSpin 4 := by decide

/-- **`ℕ`-graded spin label**: doubled spin `2s` with no restriction to
`{0, 2}`. Same `twice_j` convention as `QOU.SpinLabels`; the spin-`2` label of
`QOU.Eightfold.Sym2AdjointSpinTwo.spinTwo` is `twoS = 4`. -/
structure GradedSpin where
  /-- Twice the spin. -/
  twoS : ℕ
deriving DecidableEq

/-- Embedding of the old two-valued encoding into the graded label. -/
def GradedSpin.ofSector (b : Bool) : GradedSpin := ⟨sectorSpinDouble b⟩

/-- Projection of a graded label back to the `Bool` sector, via the existing
`barSectorOfSpin` (`true` iff spin `0`). -/
def GradedSpin.toSector (s : GradedSpin) : Bool := barSectorOfSpin s.twoS

/-- The spin-`2` graded label. -/
def GradedSpin.spinTwo : GradedSpin := ⟨4⟩

/-- **Compatibility 1.** `toSector` is a retraction of `ofSector`: no sector
information is lost by passing to the graded label. -/
theorem GradedSpin.toSector_ofSector (b : Bool) :
    (GradedSpin.ofSector b).toSector = b := by
  cases b <;> decide

/-- **Compatibility 2.** Projecting the graded label of a carrier recovers its
sector; this is `barSectorOfSpin_inverts`, read through `GradedSpin`. -/
theorem GradedSpin.toSector_spinDouble [Invertible (2 : R)] (c : EWCarrier) :
    (GradedSpin.mk (spinDouble (R := R) c)).toSector =
      EWSectorSelection.isSinglet (R := R) c :=
  barSectorOfSpin_inverts (R := R) c

/-- **The extension is proper.** The spin-`2` label is not in the image of the
old encoding. -/
theorem GradedSpin.spinTwo_not_ofSector (b : Bool) :
    GradedSpin.ofSector b ≠ GradedSpin.spinTwo := by
  cases b <;> decide

/-- Projecting spin `2` back to the `Bool` sector lands on the doublet, the
same sector as spin `1`; the projection forgets exactly what the extension adds. -/
theorem GradedSpin.spinTwo_toSector :
    GradedSpin.spinTwo.toSector = (GradedSpin.ofSector false).toSector := by
  decide

end SpinTwoNoGo

/-! ## Isospin `T₃` against the skew charge (2026-11-20)

The recorded table `ewT3Double` is compared with what `σ` and the skew
functional compute. Three results:

* **No-go (generic field).** `ewT3Double` is not an affine function `λ·Q + μ` of
  the skew charge. The `H` row forces `μ = 0`, the `Z` row (`Q(Z) ≠ 0`,
  `z_not_neutral_by_parity`) forces `λ = 0`, and the `W⁺` row then reads `1 = 0`.
* **Normalised skew (generic field).** `Q(c)/Q(W⁺)` equals `1, −1, 0` on
  `W⁺, W⁻, H`, and is nonzero on `Z`. It agrees with the table except at `Z`.
* **Sign rule (ordered field).** `def:spin-involution` sets `2T₃ = 0` on `A₊`
  and `2T₃ = ±1` on `A₋`, with the sign an input there (`isospinT3` takes
  `sgn : ℤ`). Reading the sign as the sign of the skew charge gives
  `H ↦ 0`, `W± ↦ ±1`, `Z ↦ +1` when the eigenvalues exceed `1`. It agrees with
  the table on `W±, H` and disagrees at `Z`.

In every reading the obstruction is the same: `Z ∈ A₋` has nonzero skew. -/

section IsospinFromSkew

/-- **No-go: the `T₃` table is not affine in the skew charge.** There are no
`λ μ : R` with `ewT3Double c = λ · Q(c) + μ` for every carrier. -/
theorem ewT3Double_not_affine_in_charge [Invertible (2 : R)] :
    ¬ ∃ lam mu : R, ∀ c : EWCarrier,
      ((ewT3Double c : ℤ) : R) = lam * ewCharge (R := R) c + mu := by
  rintro ⟨lam, mu, h⟩
  have hH := h EWCarrier.H
  have hZ := h EWCarrier.Z
  have hW := h EWCarrier.Wp
  rw [higgs_neutral] at hH
  simp only [ewT3Double, Int.cast_zero, Int.cast_one, mul_zero, zero_add] at hH hZ hW
  rw [← hH, add_zero] at hZ hW
  have hQZ : ewCharge (R := R) EWCarrier.Z ≠ 0 := z_not_neutral_by_parity
  have hlam : lam = 0 := by
    rcases mul_eq_zero.mp hZ.symm with h0 | h0
    · exact h0
    · exact absurd h0 hQZ
  rw [hlam, zero_mul] at hW
  exact one_ne_zero hW

/-- Skew charge normalised by the `W⁺` charge. -/
def t3OfSkew (c : EWCarrier) : R :=
  ewCharge (R := R) c / ewCharge (R := R) EWCarrier.Wp

/-- **Normalised skew on the four carriers.** `W⁺ ↦ 1`, `W⁻ ↦ −1`, `H ↦ 0`,
and `Z ↦` a nonzero value. Agreement with `ewT3Double` on `W±, H`; disagreement
at `Z`. -/
theorem t3OfSkew_values [Invertible (2 : R)] :
    t3OfSkew (R := R) EWCarrier.Wp = 1 ∧
    t3OfSkew (R := R) EWCarrier.Wm = -1 ∧
    t3OfSkew (R := R) EWCarrier.H = 0 ∧
    t3OfSkew (R := R) EWCarrier.Z ≠ 0 := by
  have hW : ewCharge (R := R) EWCarrier.Wp ≠ 0 := wPlus_charged
  refine ⟨div_self hW, ?_, ?_, ?_⟩
  · unfold t3OfSkew; rw [wMinus_charge_neg, neg_div, div_self hW]
  · unfold t3OfSkew; rw [higgs_neutral, zero_div]
  · exact div_ne_zero z_not_neutral_by_parity hW

end IsospinFromSkew

section OrderedSign

variable [LinearOrder R] [IsStrictOrderedRing R]

omit [EWSectorSelection R] in
/-- For `a > 1` the skew `a − a⁻¹` is positive. -/
theorem sub_inv_pos_of_one_lt (a : Rˣ) (h : 1 < (a : R)) : 0 < (a : R) - (a : R)⁻¹ := by
  have ha : (0 : R) < a := lt_trans zero_lt_one h
  have hi : (a : R)⁻¹ < 1 := inv_lt_one_of_one_lt₀ h
  linarith

/-- **Doubled `T₃` by the spin-involution sign rule**: the sign of the skew
charge. It is `0` exactly on the `σ`-even sector (`sgnT3Double_eq_zero_iff`). -/
def sgnT3Double (c : EWCarrier) : ℤ := (SignType.sign (ewCharge (R := R) c) : ℤ)

omit [IsStrictOrderedRing R] in
/-- The sign rule vanishes exactly on `A₊`. -/
theorem sgnT3Double_eq_zero_iff [Invertible (2 : R)] (c : EWCarrier) :
    sgnT3Double (R := R) c = 0 ↔ EWSectorSelection.isSinglet (R := R) c = true := by
  unfold sgnT3Double
  have hcast : ∀ t : SignType, ((t : ℤ) = 0 ↔ t = 0) := by
    intro t; cases t <;> decide
  rw [hcast, sign_eq_zero_iff]
  constructor
  · intro h0
    cases hc : EWSectorSelection.isSinglet (R := R) c
    · rw [ewCharge_of_doublet hc] at h0
      exact absurd h0 (sub_inv_ne_zero_of_sq_ne_one _ (EWSectorSelection.eig_sq_ne_one c))
    · rfl
  · intro hc; exact ewCharge_of_singlet hc

/-- **Sign rule on the four carriers.** With `1 < a_{W⁺}` and `1 < a_Z`
(`a = q^{2k}`, `q > 1`, `k ≥ 1`): `H ↦ 0`, `W⁺ ↦ 1`, `W⁻ ↦ −1`, `Z ↦ 1`. -/
theorem sgnT3Double_values [Invertible (2 : R)]
    (hW : 1 < (EWSectorSelection.eig (R := R) EWCarrier.Wp : R))
    (hZ : 1 < (EWSectorSelection.eig (R := R) EWCarrier.Z : R)) :
    sgnT3Double (R := R) EWCarrier.H = 0 ∧
    sgnT3Double (R := R) EWCarrier.Wp = 1 ∧
    sgnT3Double (R := R) EWCarrier.Wm = -1 ∧
    sgnT3Double (R := R) EWCarrier.Z = 1 := by
  have pW : 0 < ewCharge (R := R) EWCarrier.Wp := by
    rw [ewCharge_of_doublet EWSectorSelection.wPlus_doublet]
    exact sub_inv_pos_of_one_lt _ hW
  have pZ : 0 < ewCharge (R := R) EWCarrier.Z := by
    rw [ewCharge_of_doublet EWSectorSelection.z_doublet]
    exact sub_inv_pos_of_one_lt _ hZ
  have nM : ewCharge (R := R) EWCarrier.Wm < 0 := by
    rw [wMinus_charge_neg]; linarith
  unfold sgnT3Double
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [higgs_neutral, sign_zero]; rfl
  · rw [sign_pos pW]; rfl
  · rw [sign_neg nM]; rfl
  · rw [sign_pos pZ]; rfl

/-- **The sign rule agrees with the recorded table on `W±, H` and disagrees at
`Z`.** -/
theorem sgnT3Double_vs_table [Invertible (2 : R)]
    (hW : 1 < (EWSectorSelection.eig (R := R) EWCarrier.Wp : R))
    (hZ : 1 < (EWSectorSelection.eig (R := R) EWCarrier.Z : R)) :
    sgnT3Double (R := R) EWCarrier.H = ewT3Double EWCarrier.H ∧
    sgnT3Double (R := R) EWCarrier.Wp = ewT3Double EWCarrier.Wp ∧
    sgnT3Double (R := R) EWCarrier.Wm = ewT3Double EWCarrier.Wm ∧
    sgnT3Double (R := R) EWCarrier.Z ≠ ewT3Double EWCarrier.Z := by
  obtain ⟨h1, h2, h3, h4⟩ := sgnT3Double_values (R := R) hW hZ
  refine ⟨h1, h2, h3, ?_⟩
  rw [h4]; decide

end OrderedSign

/-! ## The `(W³, B) → (Z, γ)` rotation and a linear charge (2026-11-20)

`weinberg-angle-categorical` names the rotation but does not formalise it. Here
it is the rotation `Z = c·W³ − s·B`, `γ = s·W³ + c·B` with `c² + s² = 1`, and a
charge functional extended linearly from its values `x = Q(W³)`, `y = Q(B)`.
The rotation preserves `x² + y²`, so it cannot make both `Z` and `γ` neutral
unless `x = y = 0`. At the corpus angle `c = cot θ_W · s`, `Q(Z) = 0` holds iff
`cot θ_W · x = y`. -/

section WeinbergMixing

variable {K : Type*} [Field K]

/-- Linear charge of `Z = c·W³ − s·B`. -/
def mixChargeZ (c s x y : K) : K := c * x - s * y

/-- Linear charge of `γ = s·W³ + c·B`. -/
def mixChargeGamma (c s x y : K) : K := s * x + c * y

/-- The rotation preserves the charge norm `x² + y²`. -/
theorem mixCharge_norm (c s x y : K) (h : c ^ 2 + s ^ 2 = 1) :
    mixChargeZ c s x y ^ 2 + mixChargeGamma c s x y ^ 2 = x ^ 2 + y ^ 2 := by
  unfold mixChargeZ mixChargeGamma
  linear_combination (x ^ 2 + y ^ 2) * h

/-- **No-go: mixing cannot neutralise both `Z` and `γ`.** If both rotated charges
vanish, then `Q(W³) = Q(B) = 0`. -/
theorem mixing_neutral_both_iff (c s x y : K) (h : c ^ 2 + s ^ 2 = 1) :
    (mixChargeZ c s x y = 0 ∧ mixChargeGamma c s x y = 0) ↔ (x = 0 ∧ y = 0) := by
  unfold mixChargeZ mixChargeGamma
  constructor
  · rintro ⟨hZ, hG⟩
    exact ⟨by linear_combination c * hZ + s * hG - x * h,
      by linear_combination (-s) * hZ + c * hG - y * h⟩
  · rintro ⟨rfl, rfl⟩; constructor <;> ring

/-- If `Z` is neutral, the photon carries the whole charge norm:
`Q(γ)² = x² + y²`. -/
theorem mixChargeGamma_sq_of_Z_neutral (c s x y : K) (h : c ^ 2 + s ^ 2 = 1)
    (hZ : mixChargeZ c s x y = 0) :
    mixChargeGamma c s x y ^ 2 = x ^ 2 + y ^ 2 := by
  have := mixCharge_norm c s x y h
  rw [hZ] at this
  linear_combination this

/-- **`Z` is neutral at the corpus angle iff `cot θ_W · Q(W³) = Q(B)`.** With
`c = cot θ_W · s` and `s ≠ 0` (the parametrisation of
`weinberg-angle-categorical`, `cot_identification`). -/
theorem mixChargeZ_eq_zero_iff_cot (cotW s x y : K) (hs : s ≠ 0) :
    mixChargeZ (cotW * s) s x y = 0 ↔ cotW * x = y := by
  unfold mixChargeZ
  have e : cotW * s * x - s * y = s * (cotW * x - y) := by ring
  rw [e, mul_eq_zero, sub_eq_zero]
  exact ⟨fun h => h.resolve_left hs, Or.inr⟩

/-- **In the model, both pre-mixing charges are nonzero.** If `W³` and `B` are
`σ`-odd sector vectors of non-degenerate eigenvalues `a, b` (the `σ₅⁸` grading
puts `B ∈ A₋`), their skew charges `a − a⁻¹`, `b − b⁻¹` are nonzero, so no
rotation makes both `Z` and `γ` neutral. -/
theorem mixing_cannot_neutralise_model [Invertible (2 : K)] (a b : Kˣ)
    (ha : (a : K) ^ 2 ≠ 1) (c s : K) (h : c ^ 2 + s ^ 2 = 1) :
    ¬ (mixChargeZ c s (skew (minusPart (carrier a))) (skew (minusPart (carrier b))) = 0 ∧
       mixChargeGamma c s (skew (minusPart (carrier a))) (skew (minusPart (carrier b))) = 0) := by
  intro hb
  have hx := ((mixing_neutral_both_iff c s _ _ h).mp hb).1
  rw [skew_minusPart_carrier] at hx
  exact sub_inv_ne_zero_of_sq_ne_one a ha hx

end WeinbergMixing

end QOU.ParticleInteractions
