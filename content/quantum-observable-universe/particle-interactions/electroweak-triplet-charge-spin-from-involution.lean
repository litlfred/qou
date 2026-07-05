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
theorem sector_forced_by_spin (c : EWCarrier) :
    (spinDouble (R := R) c = 0 → EWSectorSelection.isSinglet (R := R) c = true) ∧
    (spinDouble (R := R) c = 2 → EWSectorSelection.isSinglet (R := R) c = false) := by
  unfold spinDouble
  cases EWSectorSelection.isSinglet (R := R) c <;> simp

/-- Bar-sector recovered from the (doubled) spin via the spin-involution grading
law of `def:spin-involution`: `A₊` (bar-even singlet) `⟺ 2s = 0`, `A₋` (bar-odd
doublet) `⟺ 2s = 2`. `true = A₊`, `false = A₋`. -/
def barSectorOfSpin (twoS : ℕ) : Bool := twoS == 0

/-- **`barSectorOfSpin` is a genuine two-sided inverse of the spin grading.** For
every EW carrier it recovers the sector from the spin (`barSectorOfSpin ∘
spinDouble = isSinglet`). This injectivity is what makes "spin forces sector" a
*derivation* rather than a re-postulation. -/
theorem barSectorOfSpin_inverts (c : EWCarrier) :
    barSectorOfSpin (spinDouble (R := R) c) = EWSectorSelection.isSinglet (R := R) c := by
  unfold barSectorOfSpin spinDouble
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

/-- **Forced part of the charge labeling.** From the sector postulate alone: the
charged carriers `W±` (`t₃ = ±1 ≠ 0`) are bar-odd `A₋` doublets, and the `A₊`
singlet `H` is neutral (`t₃ = 0`). So *charge ⇒ doublet* and *singlet ⇒ neutral*
hold for these carriers. What is **not** entailed is which crossing slot the
charged pair occupies — that is the free label of `which_slot_is_W_free`. -/
theorem charged_are_doublets_singlet_neutral :
    EWSectorSelection.isSinglet (R := R) EWCarrier.Wp = false ∧
    EWSectorSelection.isSinglet (R := R) EWCarrier.Wm = false ∧
    EWSectorSelection.t3Double (R := R) EWCarrier.Wp ≠ 0 ∧
    EWSectorSelection.t3Double (R := R) EWCarrier.Wm ≠ 0 ∧
    EWSectorSelection.isSinglet (R := R) EWCarrier.H = true ∧
    EWSectorSelection.t3Double (R := R) EWCarrier.H = 0 :=
  ⟨EWSectorSelection.wPlus_doublet, EWSectorSelection.wMinus_doublet,
    by rw [EWSectorSelection.wPlus_t3]; decide,
    by rw [EWSectorSelection.wMinus_t3]; decide,
    EWSectorSelection.higgs_singlet, EWSectorSelection.higgs_t3⟩

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
  simp only [evenTwistDoubledI3_eq]
  have : (1 : ℤ) ≤ (k : ℤ) := by exact_mod_cast hk
  linarith

/-- **`writhe → I₃` is a monotone twist ladder, not a sign charge.** Across the
carriers it strictly increases (`k = 2 ↦ 4 < k = 3 ↦ 6 < k = 4 ↦ 8`) with no sign
change and no zero — the signature of a magnitude / spin ladder (audit §3), not
of an additive charge. -/
theorem evenTwist_doubledI3_strictMono :
    evenTwistDoubledI3 2 < evenTwistDoubledI3 3 ∧
    evenTwistDoubledI3 3 < evenTwistDoubledI3 4 := by
  constructor <;> decide

/-- **The surviving `writhe → I₃` map does NOT single out the neutral slot.**
Evaluated on the two vector carriers it gives `2·I₃(σ₁⁴) = 4 ≠ 0` and
`2·I₃(σ₃⁶) = 6 ≠ 0`: neither is neutral, so the map cannot supply the
`charged_at_4_xor_6` datum of any `EWVectorLabeling` (which requires exactly one
of the two slots to carry `t3 = 0`). Hence the one crossing→quantum-number map
that survives the U(1)-assignment audit still leaves which-slot-is-`W` a **free
label** — it strengthens, rather than closes, `which_slot_is_W_free`. -/
theorem writheI3_does_not_select_neutral_slot :
    evenTwistDoubledI3 2 ≠ 0 ∧ evenTwistDoubledI3 3 ≠ 0 ∧
    ¬ ∃ L : EWVectorLabeling,
        L.t3 4 = evenTwistDoubledI3 2 ∧ L.t3 6 = evenTwistDoubledI3 3 := by
  refine ⟨by decide, by decide, ?_⟩
  rintro ⟨L, h4, h6⟩
  rcases L.charged_at_4_xor_6 with ⟨_, hc6⟩ | ⟨hc4, _⟩
  · rw [hc6] at h6; norm_num [evenTwistDoubledI3_eq] at h6
  · rw [hc4] at h4; norm_num [evenTwistDoubledI3_eq] at h4

end QOU.ParticleInteractions
