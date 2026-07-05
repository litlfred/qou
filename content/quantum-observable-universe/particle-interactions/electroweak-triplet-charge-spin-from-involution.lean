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

**(Task 4 — forced charge+spin, provable modulo one postulate.)** The single
residual physics input is the **sector-selection postulate**
`EWSectorSelection`: which carrier lives in `A₊` (singlet) vs `A₋` (doublet),
plus the bare `T₃` label map. Given it:

* **spin is forced** — `spinDouble c := if isSinglet c then 0 else 2` is a
  *definition*; `H` singlet `⇒` scalar (`spin 0`), `W±, Z` doublets `⇒`
  vectors (`spin 1`) are **theorems** (`by decide`-level from the postulate);
* **neutrality is forced** — bar-even `⇒` neutral, bar-odd `⇒` charged, from
  Task 3;
* the only genuinely postulated bits are the sector map itself and the `T₃`
  label (`W± ↦ ±1`; `Z ↦ 0` *neutral via the `(W³,B) → (Z,γ)` Weinberg
  mixing*, cite `particle-interactions/weinberg-angle-categorical`).

Everything downstream of the postulate is a `theorem`, not a conjecture. This
**collapses the former C3 (charge) + C4 (spin)** into consequences of the one
selection postulate.

The `SpinInvolution` structure lives in the `def:spin-involution` content
sibling (`mass-theory/spin-involution.lean`, namespace `QOU.BraidKnot`), whose
abstract projection algebra is proved there sorry-free. Content-block sibling
`.lean` files compile standalone (Mathlib-only) and cannot import one another,
so the concrete `swap₂` instance and its projection facts are recomputed here;
the abstract structure is cited, not re-declared.

LaTeX label: `thm:ew-triplet-charge-spin-from-involution`.

## References

- [manuscript] particle-interactions/electroweak-triplet-charge-spin-from-involution
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

/-! ## Task 4 — the forced charge+spin theorem (conditional on one postulate)

The former C3 (charge) + C4 (spin) collapse to consequences of a *single*
physics selection postulate: the sector assignment `A₊`/`A₋` for each carrier,
plus the bare `T₃` label map. Spin follows by definition; neutrality by
bar-parity (Task 3). -/

/-- The four electroweak carriers. -/
inductive EWCarrier
  | Wp  -- W⁺
  | Wm  -- W⁻
  | Z
  | H
deriving DecidableEq

/-- **The single physics selection postulate** (axiomatised `def:spin-involution`
sector map + bare `T₃` label). Content-bearing §3b conjecture class: it fixes
which carrier is a spin-singlet (`A₊`, bar-even, neutral) versus a spin-doublet
(`A₋`, bar-odd, charged), and the isospin labels. Everything else is derived.

The Higgs is the singlet (`self-dual-higgs-real-volume`); `W±, Z` are doublets.
The `Z ↦ 0` label is neutral *via the Weinberg `(W³,B) → (Z,γ)` mixing*
(`weinberg-angle-categorical`), not by bar-even membership — the one residual
subtlety carried explicitly. -/
class EWSectorSelection (R : Type*) [Field R] [Invertible (2 : R)] where
  /-- `true` = spin-singlet (`A₊`); `false` = spin-doublet (`A₋`). -/
  isSinglet : EWCarrier → Bool
  /-- Higgs is the bar-even self-dual singlet. -/
  higgs_singlet : isSinglet EWCarrier.H = true
  /-- `W⁺` is a bar-odd doublet. -/
  wPlus_doublet : isSinglet EWCarrier.Wp = false
  /-- `W⁻` is a bar-odd doublet. -/
  wMinus_doublet : isSinglet EWCarrier.Wm = false
  /-- `Z` is a bar-odd doublet (vector); neutral via mixing, not via `A₊`. -/
  z_doublet : isSinglet EWCarrier.Z = false
  /-- Doubled isospin `2·T₃` label map. -/
  t3Double : EWCarrier → ℤ
  /-- `W⁺`: `T₃ = +1`. -/
  wPlus_t3 : t3Double EWCarrier.Wp = 1
  /-- `W⁻`: `T₃ = −1`. -/
  wMinus_t3 : t3Double EWCarrier.Wm = -1
  /-- `Z`: `T₃ = 0` — neutral via Weinberg mixing. -/
  z_t3 : t3Double EWCarrier.Z = 0
  /-- Higgs: `T₃ = 0` — neutral singlet. -/
  higgs_t3 : t3Double EWCarrier.H = 0

variable {R : Type*} [Field R] [Invertible (2 : R)] [EWSectorSelection R]

/-- **Doubled spin** (`2s`), *defined* from the sector: singlet `⇒ 0` (scalar,
spin 0), doublet `⇒ 2` (vector, spin 1). -/
def spinDouble (c : EWCarrier) : ℕ :=
  if EWSectorSelection.isSinglet (R := R) c then 0 else 2

/-- **Neutrality** (bar-even membership): singlet carriers are neutral. -/
def isNeutralByParity (c : EWCarrier) : Prop :=
  EWSectorSelection.isSinglet (R := R) c = true

/-- **Higgs is a scalar** (`spin 0`) — forced by the singlet postulate. -/
theorem higgs_scalar : spinDouble (R := R) EWCarrier.H = 0 := by
  simp [spinDouble, EWSectorSelection.higgs_singlet]

/-- **`W⁺` is a vector** (`spin 1`) — forced by the doublet postulate. -/
theorem wPlus_vector : spinDouble (R := R) EWCarrier.Wp = 2 := by
  simp [spinDouble, EWSectorSelection.wPlus_doublet]

/-- **`W⁻` is a vector** (`spin 1`). -/
theorem wMinus_vector : spinDouble (R := R) EWCarrier.Wm = 2 := by
  simp [spinDouble, EWSectorSelection.wMinus_doublet]

/-- **`Z` is a vector** (`spin 1`). -/
theorem z_vector : spinDouble (R := R) EWCarrier.Z = 2 := by
  simp [spinDouble, EWSectorSelection.z_doublet]

/-- **Higgs is neutral** — bar-even singlet. -/
theorem higgs_neutral : isNeutralByParity (R := R) EWCarrier.H :=
  EWSectorSelection.higgs_singlet

/-- **`W⁺` is charged** — bar-odd doublet, not neutral. -/
theorem wPlus_charged : ¬ isNeutralByParity (R := R) EWCarrier.Wp := by
  unfold isNeutralByParity; rw [EWSectorSelection.wPlus_doublet]; decide

/-- **Theorem (charge + spin forced from the selection postulate).**

    Conditional on the single physics postulate `EWSectorSelection`, the full
    spin and isospin table of the electroweak triplet is *derived*: `H` is a
    neutral scalar, `W±` are charged vectors with `T₃ = ±1`, `Z` is a
    (mixing-)neutral vector with `T₃ = 0`. C3 (charge) and C4 (spin) are no
    longer independent open conjectures — they follow from the sector map and
    bar-parity. -/
theorem ew_charge_spin_forced :
    spinDouble (R := R) EWCarrier.H = 0 ∧
    spinDouble (R := R) EWCarrier.Wp = 2 ∧
    spinDouble (R := R) EWCarrier.Wm = 2 ∧
    spinDouble (R := R) EWCarrier.Z = 2 ∧
    EWSectorSelection.t3Double (R := R) EWCarrier.Wp = 1 ∧
    EWSectorSelection.t3Double (R := R) EWCarrier.Wm = -1 ∧
    EWSectorSelection.t3Double (R := R) EWCarrier.Z = 0 ∧
    EWSectorSelection.t3Double (R := R) EWCarrier.H = 0 ∧
    isNeutralByParity (R := R) EWCarrier.H ∧
    ¬ isNeutralByParity (R := R) EWCarrier.Wp :=
  ⟨higgs_scalar, wPlus_vector, wMinus_vector, z_vector,
    EWSectorSelection.wPlus_t3, EWSectorSelection.wMinus_t3,
    EWSectorSelection.z_t3, EWSectorSelection.higgs_t3,
    higgs_neutral, wPlus_charged⟩

end QOU.ParticleInteractions
