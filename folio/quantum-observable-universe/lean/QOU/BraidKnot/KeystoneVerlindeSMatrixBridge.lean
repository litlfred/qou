import QOU.BraidKnot.WLambdaMTCLocalizationObligation
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# Keystone residual (i): the DG bridge — Beasley–Witten localization ⇒ Verlinde S-matrix measure

`WLambdaMTCLocalizationObligation.lean` carries the residual-(i) obligation as a single raw field
`loc_matches : loc λ = d_q(λ)²/D²`. That field is opaque: it asserts the gauge-theory output *equals*
the Hecke Plancherel measure, without exhibiting the gauge object that produces it. This file does the
**formalize-first DG step**: it factors `loc_matches` through the actual differential-geometric output
of the construction — the **modular S-matrix** of the Beasley–Witten Chern–Simons localization on the
Seifert manifold `S³/2I` (the Poincaré homology sphere; Reeb = Seifert `S¹`).

## What the bridge buys (and what it does NOT)

The Beasley–Witten non-abelian localization of Chern–Simons theory on a Seifert 3-manifold outputs a
**modular tensor category** `𝒞` whose **vacuum S-matrix row** `S_{0λ}` weights the Verlinde measure
`μ(λ) = S_{0λ}²`. In *any* modular tensor category the vacuum row is the published structural identity
`S_{0λ} = d_λ / D`, `D² = Σ_λ d_λ²` (Bakalov–Kirillov / EGNO; *not* a fit). So:

* **DG side (gauge output):** the localization measure is `μ(λ) = S_{0λ}²` — the squared vacuum
  S-matrix row, the genuine TQFT/DG datum.
* **Bridge (this file, sorry-free):** `μ(λ) = S_{0λ}² = (d_λ/D)² = d_λ²/D²` — so `μ` **is** the
  Hecke Plancherel measure, discharging `BeasleyWittenLocalization.loc_matches` (`toBeasleyWitten`).

This **reduces** residual (i)'s open content from the raw measure assertion to the precise, citable
modular-data inputs `VerlindeModularData` carries. It does **not** *close* residual (i): the genuine
open content is a **category-identification / physics claim** — that the BW localization of `S³/2I`,
on the **full-Hecke side**, is a modular category whose simple objects are the Hecke blocks with
quantum dimension the *Hecke* `d_q(λ)`. That identification is owner-gated (narrow Subgoal-2 reversal,
#2503/#2524) and is **foreclosed on the SU(2)`_k` sub-route** (`Su2SchurWeylForeclosure.lean`,
#2717/#2727: `[2j+1]_q ≠ d_q(λ)` off the standard rep, electron block outside the GL₂ image). So
constructing a `VerlindeModularData` whose `qDim` is the Hecke `d_q` remains the open, multi-session
research step — the bridge states it in gauge-theoretic language and proves everything downstream of
it. **Honest scope:** a formalization cannot *prove* the physics that the localization yields this
category; it can only factor the assertion and verify its arithmetic (the n=5 witness +
`heckeVerlindeData` below show the Hecke side realizes the bridge once the identification is granted).

Base ring: generic `{R : Type*} [Field R]` for the bridge (§7c — the S-matrix identity is algebraic);
the non-vacuity model and `heckeVerlindeData` specialise to `ℝ` (the substrate `q₀`, `Real.sqrt` for
`D`).
-/

namespace QOU.BraidKnot.Keystone

open scoped BigOperators

/-- **Modular data of the Beasley–Witten / RT localization category** (the gauge-theory side,
sharpened). The localization on `S³/2I` outputs a modular tensor category whose vacuum S-matrix row
`S0` weights the Verlinde measure. This class carries that modular data: the Hecke blocks, the
categorical quantum dimension `qDim`, the global dimension `D` (`D² = Σ qDim²`), and the vacuum
S-matrix row `S0`. In *any* modular category the vacuum row is `S_{0λ} = d_λ/D` (`S0_eq`) — a
**published structural fact** (Bakalov–Kirillov / EGNO), carried here as the modular-data input, *not*
a fit. The single physics content — that this category's `qDim` is the *Hecke* `d_q` — lives in
*constructing an instance*, not in these fields.

-- Ref: [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (S-matrix vacuum row).
-- Ref: [beasleywitten2005] https://doi.org/10.4310/jdg/1143593746 — non-abelian CS localization. -/
class VerlindeModularData (R : Type*) [Field R] where
  /-- Partition index for the Hecke block `λ ⊢ n`. -/
  Part : Type*
  /-- The finite set of Hecke partition blocks. -/
  parts : Finset Part
  /-- The transpose involution `λ ↦ λ′`. -/
  conj : Part → Part
  /-- Blocks closed under transpose. -/
  conj_mem : ∀ p ∈ parts, conj p ∈ parts
  /-- The categorical quantum dimension `d_q(λ)` (the *Hecke* q-dimension on an instance). -/
  qDim : Part → R
  /-- `d_q(λ′) = d_q(λ)` (corpus-proved, `KeystoneC2QDimTranspose.qDim_conj`). -/
  qDim_conj : ∀ p ∈ parts, qDim (conj p) = qDim p
  /-- The global quantum dimension `D` (total dimension of the modular category). -/
  D : R
  /-- `D² = Σ_λ d_q(λ)²` — the defining global-dimension relation. -/
  D_sq : D ^ 2 = ∑ p ∈ parts, qDim p ^ 2
  /-- `D ≠ 0`. -/
  D_ne : D ≠ 0
  /-- The **vacuum S-matrix row** `S_{0λ}` — the Beasley–Witten / Verlinde localization output. -/
  S0 : Part → R
  /-- **Published modular-data identity** `S_{0λ} = d_λ/D` (vacuum row of the S-matrix in any
  modular tensor category). The gauge output, now a structural fact rather than a raw measure. -/
  S0_eq : ∀ p ∈ parts, S0 p = qDim p / D

namespace VerlindeModularData

variable {R : Type*} [Field R]

/-- **The Verlinde measure** `μ(λ) = S_{0λ}²` — the squared vacuum S-matrix row, i.e. the genuine
Beasley–Witten localization weight on the blocks. -/
def verlindeMeasure (h : VerlindeModularData R) (p : h.Part) : R := h.S0 p ^ 2

/-- **The DG bridge (sorry-free): the localization measure IS the Hecke Plancherel measure.**
`μ(λ) = S_{0λ}² = (d_λ/D)² = d_λ²/D²`. The gauge-theory output (squared vacuum S-matrix row) equals
`d_q²/D²` purely from the published modular-data identity `S_{0λ} = d_λ/D` — no fit, no extra input. -/
theorem verlindeMeasure_eq_plancherel (h : VerlindeModularData R) (p : h.Part) (hp : p ∈ h.parts) :
    h.verlindeMeasure p = h.qDim p ^ 2 / (∑ m ∈ h.parts, h.qDim m ^ 2) := by
  rw [verlindeMeasure, h.S0_eq p hp, div_pow, h.D_sq]

/-- `Σ qDim² ≠ 0` — from `D² = Σ qDim²` and `D ≠ 0`. -/
theorem sum_qDimSq_ne (h : VerlindeModularData R) : (∑ m ∈ h.parts, h.qDim m ^ 2) ≠ 0 := by
  rw [← h.D_sq]; exact pow_ne_zero 2 h.D_ne

/-- **The bridge discharges the residual-(i) obligation.** Any `VerlindeModularData` (a modular
category produced by the localization, with vacuum row `S_{0λ}=d_λ/D`) yields a
`BeasleyWittenLocalization` whose `loc` is the squared vacuum S-matrix row — and `loc_matches` is the
bridge `verlindeMeasure_eq_plancherel`. So once the localization is identified as *this* modular
category, residual (i)'s C1/C2/C6 consequences all follow. -/
def toBeasleyWitten (h : VerlindeModularData R) : BeasleyWittenLocalization R where
  Part := h.Part
  parts := h.parts
  conj := h.conj
  conj_mem := h.conj_mem
  qDim := h.qDim
  qDim_conj := h.qDim_conj
  globalDim_ne := h.sum_qDimSq_ne
  loc := h.verlindeMeasure
  loc_matches := h.verlindeMeasure_eq_plancherel

end VerlindeModularData

/-! ## Non-vacuity: the bridge is realized (not conditional-on-`False`) -/

/-- **Non-vacuity model — the `n = 2` modular category over `ℝ`.** Two blocks `[2],[1,1]`, both of
quantum dimension `1`, `D = √2` (`D² = 2 = Σ d²`), vacuum row `S_{00} = 1/√2`. Confirms
`VerlindeModularData` is inhabited, so the bridge and `toBeasleyWitten` are not vacuous. -/
noncomputable instance verlindeData_two : VerlindeModularData ℝ where
  Part := Bool
  parts := {false, true}
  conj := not
  conj_mem := by decide
  qDim := fun _ => 1
  qDim_conj := fun _ _ => rfl
  D := Real.sqrt 2
  D_sq := by
    rw [Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)]
    rw [Finset.sum_pair (by decide : (false : Bool) ≠ true)]; norm_num
  D_ne := by positivity
  S0 := fun _ => 1 / Real.sqrt 2
  S0_eq := fun _ _ => rfl

/-! ## The Hecke side realizes the bridge (once the category identification is granted) -/

open QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.IdentityI

/-- **The Hecke q-dimensions realize `VerlindeModularData`** for `q > 1` on any conjugate-closed,
nonempty block set `P`: take `qDim := d_q`, `D := √(Σ d_q²)`, `S0 := d_q/D`. Then `S0_eq` is `rfl`
and the modular-data fields are discharged from positivity (`qDim_pos`, `sum_qDimSq_pos`) and the
corpus `qDim_conj`. The **only** thing this does *not* establish is the physics — that the BW
localization of `S³/2I` actually *is* this category; that owner-gated identification is the open
residual. Given it, `toBeasleyWitten ∘ heckeVerlindeData` reproduces `heckeLocalizationOfPos` with
the S-matrix made explicit. -/
noncomputable def heckeVerlindeData
    (q : ℝ) (hq : 1 < q) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hP : P.Nonempty) :
    VerlindeModularData ℝ where
  Part := List ℕ
  parts := P
  conj := Partition.conjugate
  conj_mem := hconj
  qDim := qDim q
  qDim_conj := fun p hp => qDim_conj q p (hsorted p hp)
  D := Real.sqrt (∑ m ∈ P, qDim q m ^ 2)
  D_sq := Real.sq_sqrt (le_of_lt (sum_qDimSq_pos hq hP))
  D_ne := ne_of_gt (Real.sqrt_pos.mpr (sum_qDimSq_pos hq hP))
  S0 := fun p => qDim q p / Real.sqrt (∑ m ∈ P, qDim q m ^ 2)
  S0_eq := fun _ _ => rfl

/-- **The Hecke Verlinde data reproduces the residual-(i) localization with the S-matrix explicit.**
`(heckeVerlindeData …).toBeasleyWitten` has `loc = (d_q/D)²` and matches `d_q²/D²` — the same measure
as `heckeLocalizationOfPos`, now exhibited as the squared vacuum S-matrix row of the (conjectured)
localization category. -/
theorem heckeVerlindeData_loc
    (q : ℝ) (hq : 1 < q) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hP : P.Nonempty) (p : List ℕ) (hp : p ∈ P) :
    ((heckeVerlindeData q hq P hsorted hconj hP).toBeasleyWitten).loc p
      = qDim q p ^ 2 / (∑ m ∈ P, qDim q m ^ 2) :=
  (heckeVerlindeData q hq P hsorted hconj hP).verlindeMeasure_eq_plancherel p hp

/-! ## Residual (i), reduced to ONE precisely-stated open piece -/

/-- **The single open content of residual (i), precisely stated — the category identification.**

Introduce the Beasley–Witten localization's vacuum S-matrix row `bwS0` as an **abstract gauge
datum**: the Chern–Simons path-integral output on `S³/2I`, carried as an opaque field — **not**
defined as `d_q/D`. The lone open conjecture is `bwS0_eq_hecke`: that the gauge-defined vacuum row
equals the Hecke modular datum `d_q(λ)/√(Σ d_q²)`. This is the *one* thing the published, owner-gated
localization must deliver; everything else in residual (i) — the Verlinde measure `= d_q²/D²`, C1
(`Σ=1`), C2 (chirality), C6 (full support) — is **derived** from it (`bwLocalization`,
`bwLocalization_loc`).

No global instance is supplied: residual (i) is genuinely conditional on this identification, which is
owner-gated (the narrow Subgoal-2 reversal, #2503/#2524) and **foreclosed on the SU(2)`_k` sub-route**
(`Su2SchurWeylForeclosure.lean`, #2717/#2727 — `[2j+1]_q ≠ d_q(λ)` off the standard rep, so the index
must live full-Hecke side). The class field `bwS0_eq_hecke` is a content-bearing,
parameter-quantified identity (AGENTS.md §3b-tax — primary conjecture, not `True`); the inhabiting
`example` below is the *fiat* realization (`bwS0 := d_q/D`), present only to show the conditional
results are not conditional-on-`False`. The genuinely open content is the *physical* instance, where
`bwS0` is the actual path-integral output. -/
class BWVacuumRowIsHecke (q : ℝ) (P : Finset (List ℕ)) where
  /-- Substrate regime `q > 1` (positivity of the Hecke q-dimensions). -/
  hq : 1 < q
  /-- The blocks are weakly-decreasing partitions. -/
  hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·)
  /-- The blocks are closed under transpose. -/
  hconj : ∀ l ∈ P, Partition.conjugate l ∈ P
  /-- The block set is nonempty. -/
  hP : P.Nonempty
  /-- **The gauge datum** — the BW localization's vacuum S-matrix row on the blocks, abstract (the
  path-integral output on `S³/2I`, NOT defined as `d_q/D`). -/
  bwS0 : List ℕ → ℝ
  /-- **THE single open conjecture (owner-gated):** the gauge-defined vacuum S-matrix row equals the
  Hecke modular datum `d_q(λ)/√(Σ d_q²)`. What the published localization must deliver; foreclosed on
  the SU(2)`_k` sub-route, so full-Hecke.

  **Realized at the fibre root** (PR #4365): the LR/WRT amplitude satisfies `|A_m(α)| = 2·[mark]/D`
  exactly at the root of unity `ζ = e^{iπ/5}` (`KeystoneLRAmplitudeReal.amplitude_first` /
  `colored_modulus_phi_node`), i.e. `bwS0 = d_ζ/D` for the *actual* gauge datum (the WRT amplitude),
  not the fiat. So the residual open content is precisely the **archimedean continuation of `bwS0`
  from `ζ` to real `q₀`** — and the value-map side of that continuation is polynomial evaluation
  (`KeystoneWLambdaContinuation`), so the wall is the continuation of the *gauge row*, not the
  Plancherel structure (proved here) nor the value map (proved). -/
  bwS0_eq_hecke : ∀ l ∈ P, bwS0 l = qDim q l / Real.sqrt (∑ m ∈ P, qDim q m ^ 2)

namespace BWVacuumRowIsHecke

variable {q : ℝ} {P : Finset (List ℕ)}

/-- The modular tensor category built from the (conjectured) BW vacuum-row identification: the gauge
row `bwS0` is the S-matrix vacuum row, the q-dimensions are the Hecke `d_q`. -/
noncomputable def toVerlindeModularData (h : BWVacuumRowIsHecke q P) : VerlindeModularData ℝ where
  Part := List ℕ
  parts := P
  conj := Partition.conjugate
  conj_mem := h.hconj
  qDim := qDim q
  qDim_conj := fun p hp => qDim_conj q p (h.hsorted p hp)
  D := Real.sqrt (∑ m ∈ P, qDim q m ^ 2)
  D_sq := Real.sq_sqrt (le_of_lt (sum_qDimSq_pos h.hq h.hP))
  D_ne := ne_of_gt (Real.sqrt_pos.mpr (sum_qDimSq_pos h.hq h.hP))
  S0 := h.bwS0
  S0_eq := h.bwS0_eq_hecke

/-- **Residual (i) holds given the identification.** The BW localization (squared gauge vacuum row)
is a `BeasleyWittenLocalization` whose measure is the Hecke Plancherel measure `d_q²/D²` — so C1
(`Σ=1`), C2 (chirality), C6 (full support) all follow from the single conjecture `bwS0_eq_hecke`. -/
noncomputable def bwLocalization (h : BWVacuumRowIsHecke q P) : BeasleyWittenLocalization ℝ :=
  h.toVerlindeModularData.toBeasleyWitten

/-- The BW localization measure equals the Hecke Plancherel measure `d_q²/D²` (the discharged
residual-(i) obligation, conditional on the identification). -/
theorem bwLocalization_loc (h : BWVacuumRowIsHecke q P) (l : List ℕ) (hl : l ∈ P) :
    h.bwLocalization.loc l = qDim q l ^ 2 / (∑ m ∈ P, qDim q m ^ 2) :=
  h.toVerlindeModularData.verlindeMeasure_eq_plancherel l hl

/-- **Non-vacuity — `BWVacuumRowIsHecke` is inhabitable** (the *fiat* realization `bwS0 := d_q/D` on
the single block `[1]`), so the conditional results above are not conditional-on-`False`. The OPEN
content is the *physical* instance where `bwS0` is the genuine path-integral output, not this fiat. -/
noncomputable example : BWVacuumRowIsHecke (3 / 2) {[1]} where
  hq := by norm_num
  hsorted := by decide
  hconj := by decide
  hP := ⟨[1], by decide⟩
  bwS0 := fun l => qDim (3 / 2) l / Real.sqrt (∑ m ∈ ({[1]} : Finset (List ℕ)), qDim (3 / 2) m ^ 2)
  bwS0_eq_hecke := fun _ _ => rfl

end BWVacuumRowIsHecke

end QOU.BraidKnot.Keystone
