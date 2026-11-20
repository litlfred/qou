/-
# The γγ normal form, its two gradings, and the quark-state hypothesis

Bean `qou-qs1d` (epic `qou-qs0e`). Formalize-first test of the agent working
hypothesis — NOT a finding, and NOT adopted —

  quark state := the degree ≥ 1 part of `NF(γ(φ)·γ(ψ))` in `H₃(q)`,
                 projected to the `(2,1)` Wedderburn channel,

with `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁` (`rem:knot-basis-color-content`).

The hypothesis needs three things to be non-vacuous. This file proves what
holds and records, as theorems, where it fails.

## Two gradings, which the hypothesis conflates

* **word degree** — length of the Gröbner–Shirshov normal-form word
  (`1` : 0; `σ₀, σ₁` : 1; `σ₁σ₀, σ₀σ₁` : 2; `σ₀σ₁σ₀` : 3);
* **order in the tower** — the power of `h = q − q⁻¹ = 2t + O(t²)`, `t = q − 1`.

`results.md:9-13` (`computations/probes/quark_template/`) is a statement about
the SECOND grading. The hypothesis is phrased in the FIRST. They agree on the
γγ product itself and disagree as soon as a flavour flip is applied:

* `pairNF_affine` : `NF(γγ)` is EXACTLY affine in `h`, `NF = NF|_{h=0} + h·N₁`;
* `N₁_deg0`, `N₁_bilin_*` : the `h`-coefficient `N₁` lives in word degree ≥ 1
  and is homogeneous bilinear in `(φ, ψ)` — so on `γγ` the order-1 part
  satisfies all three non-vacuity requirements;
* `pairNF_deg0_h_free` : the word-degree-0 coordinate `1 + φ₀ψ₀ + φ₁ψ₁` is
  `h`-free;
* **but** `flavour_reaches_deg0` : under the flavour flip of
  `results.md` (`σᵢ ↦ σᵢ⁻¹ = σᵢ − h`), the word-degree-0 coordinate moves at
  order `h¹` (by exactly `−h` on the witness `flavour_reaches_deg0_witness`).
  So requirement (1), "the degree-0 part carries no flavour", holds only
  modulo `h` (scope (a)); it is FALSE at order `t¹` in the word-degree reading.
* `degPos_not_bilinear` : requirement (3) FAILS as stated — the degree ≥ 1
  part contains the pass-through terms `φ₀ + ψ₀`, `φ₁ + ψ₁`, `φ₀₁ + ψ₀₁`, so it
  is affine-bilinear, not bilinear. The connected part
  `NF((γ(φ)−1)(γ(ψ)−1))` IS bilinear (`pairNF_eq_connected`).

## Re-derivation of `results.md:9-13` (the `(2,1)` channel)

With the reduced-Burau `(2,1)` representation `ρ` of the probe
(`rho_mul` : `ρ` is multiplicative on the NF algebra at `h = q − q⁻¹`):

* `template_order_zero` : at `q = 1` the `(2,1)` character of the nucleon word
  is `0` for EVERY choice of quark shifts — flavour is invisible at `t⁰`;
* `template_S0_zero` : the flavour-blind template's character is identically 0;
* `template_SplusAVG_proton` : the corpus template's character is
  `(q − 1)·g(q)` with `g(1) = −1` — flavour is decided at order `t¹`.

## Owner decisions 2026-11-15 (D1–D3), implemented

* **D1** — the quark state is the `h¹` part of a SINGLE LETTER, with `h` a
  formal variable (`R[X]`, `h := X`): `quarkState g ε := hPart 1 (quarkLetter g ε)`.
  It equals `flavourShift ε • 1` (`quarkState_eq`), separates the flavours
  (`quarkState_flavour_ne`), has `h⁰` part = the bare generator for both flavours
  (`quarkLetter_order_zero`), and the letter has no `h^{≥2}` part. On γγ the `h¹`
  part is `N₁` (`hPart_one_pairNF`).
* **D2** — the `(2,1)` projection is the NUCLEON state (`nucleonState`,
  `nucleonStateOfQuarks`), built from three single letters; `rho_letter` identifies
  each letter's `(2,1)` image with the word's factor. The γγ projection is renamed
  `pairChannelState` and retired as "quark state".
* **D3** — the `L₊` orientation trap is documented on `mulNF`
  (`MarkovTraceOnHecke.lean`) and `H3A.v`.

Base ring (§7c): the NF algebra is over generic `[CommRing R]`; the `(2,1)`
representation needs `q⁻¹` and is over `[Field R]` with `q ≠ 0`. No `ℝ`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-/
import QOU.Machinery.MarkovTraceOnHecke
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Algebra.Polynomial.Coeff

namespace QOU.QuarkState

open QOU.Machinery.H3

/-! ## The normal-form algebra over a generic commutative ring -/

section Generic

variable {R : Type*} [CommRing R]

/-- The unit `1` as an NF vector (local copy of `HeckeH3AlgebraLaws.unitNF`,
kept local so this file's import cone is `MarkovTraceOnHecke` + Mathlib). -/
def e0 : Fin 6 → R := ![1, 0, 0, 0, 0, 0]

/-- `σ₀` as an NF vector on the basis `[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`. -/
def s0 : Fin 6 → R := ![0, 1, 0, 0, 0, 0]
/-- `σ₁` as an NF vector. -/
def s1 : Fin 6 → R := ![0, 0, 1, 0, 0, 0]

/-- The basis labels are DERIVED, not asserted: `σ₀·σ₁` is coordinate 4.
(Trap: `MarkovTraceOnHecke` labels coordinate 3 `L₊` although it is `σ₁σ₀`,
while `rem:knot-basis-color-content` writes `L₊ = σ₀σ₁`, i.e. coordinate 4.) -/
theorem s0_mul_s1 (h : R) : mulNF h s0 s1 = ![0, 0, 0, 0, 1, 0] := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1]

theorem s1_mul_s0 (h : R) : mulNF h s1 s0 = ![0, 0, 0, 1, 0, 0] := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1]

/-- The photon in the **straight chart** `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁`, built with
the algebra product (no basis label is trusted).

This was the corpus photon until the owner ruling of 2026-11-18 (bean `qou-99qc`,
confirmed 2026-11-20). `def:photon` is now `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` — `photon`
below — and `photon h a0 a1 a2 = photonStraight h (a0 − h·a2) a1 a2`
(`photon_eq_photonStraight`). Every theorem of this file stated on
`photonStraight` / `pairNF` is a statement in the straight chart; the canonical
chart's pair product is `pairNFChiral`. -/
def photonStraight (h a0 a1 a2 : R) : Fin 6 → R :=
  e0 + a0 • s0 + a1 • s1 + a2 • mulNF h s0 s1

theorem photonStraight_eq (h a0 a1 a2 : R) : photonStraight h a0 a1 a2 = ![1, a0, a1, 0, a2, 0] := by
  rw [photonStraight, s0_mul_s1]
  funext i; fin_cases i <;> simp [e0, s0, s1]

/-- The flavour-flipped photon: every letter `σᵢ` replaced by
`σᵢ⁻¹ = σᵢ − h` (the sign bit of `quark_template`). -/
def photonBar (h a0 a1 a2 : R) : Fin 6 → R :=
  e0 + a0 • (s0 - h • e0) + a1 • (s1 - h • e0)
    + a2 • mulNF h (s0 - h • e0) (s1 - h • e0)

/-- `NF(γ(φ)·γ(ψ))`. -/
def pairNF (h a0 a1 a2 b0 b1 b2 : R) : Fin 6 → R :=
  mulNF h (photonStraight h a0 a1 a2) (photonStraight h b0 b1 b2)

/-- **The γγ normal form** — reproduces table 5 of
`trivial-knot-photon-interpretation` coordinate by coordinate (with
`L₋ = σ₁σ₀` at index 3 and `L₊ = σ₀σ₁` at index 4). -/
theorem pairNF_eq (h a0 a1 a2 b0 b1 b2 : R) :
    pairNF h a0 a1 a2 b0 b1 b2 =
      ![1 + a0 * b0 + a1 * b1,
        a0 + b0 + h * a0 * b0 + a2 * b1,
        a1 + b1 + h * a1 * b1 + a0 * b2,
        a2 * b2 + a1 * b0,
        a2 + b2 + a0 * b1 + h * (a0 * b2 + a2 * b1),
        a2 * b0 + a1 * b2 + h * a2 * b2] := by
  funext i
  fin_cases i <;>
    simp [pairNF, photonStraight, mulNF, mulσ₀, mulσ₁, e0, s0, s1] <;> ring

/-! ### The canonical photon: chiral vertex `σ₀σ₁⁻¹` (`def:photon`, ruling 2026-11-18) -/

/-- `σ₁ − h` is the inverse of `σ₁` in the NF algebra. -/
theorem s1_mul_s1inv (h : R) : mulNF h s1 (s1 - h • e0) = e0 := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1, e0]

theorem s1inv_mul_s1 (h : R) : mulNF h (s1 - h • e0) s1 = e0 := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1, e0]

/-- **`def:photon`**: `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`, `σ₁⁻¹ = σ₁ − h`. -/
def photon (h a0 a1 a2 : R) : Fin 6 → R :=
  e0 + a0 • s0 + a1 • s1 + a2 • mulNF h s0 (s1 - h • e0)

theorem photon_eq (h a0 a1 a2 : R) :
    photon h a0 a1 a2 = ![1, a0 - h * a2, a1, 0, a2, 0] := by
  funext i; fin_cases i <;> simp [photon, mulNF, mulσ₀, mulσ₁, e0, s0, s1] <;> ring

/-- Same element, straight coordinates: the `σ₀`-weight moves by `−h·φ₀₁`. -/
theorem photon_eq_photonStraight (h a0 a1 a2 : R) :
    photon h a0 a1 a2 = photonStraight h (a0 - h * a2) a1 a2 := by
  rw [photon_eq, photonStraight_eq]

/-- `NF(γ(φ)·γ(ψ))` for the canonical photon. -/
def pairNFChiral (h a0 a1 a2 b0 b1 b2 : R) : Fin 6 → R :=
  mulNF h (photon h a0 a1 a2) (photon h b0 b1 b2)

theorem pairNFChiral_eq_pairNF (h a0 a1 a2 b0 b1 b2 : R) :
    pairNFChiral h a0 a1 a2 b0 b1 b2 = pairNF h (a0 - h * a2) a1 a2 (b0 - h * b2) b1 b2 := by
  simp only [pairNFChiral, pairNF, photon_eq_photonStraight]

/-- **The γγ normal form of `def:photon`** (basis `1, σ₀, σ₁, L₋ = σ₁σ₀,
`L₊ = σ₀σ₁, e⁻ = σ₀σ₁σ₀`). Recomputed independently in
`computations/probes/gamma_gamma_pair_nf_h3_probe.py`. -/
theorem pairNFChiral_eq (h a0 a1 a2 b0 b1 b2 : R) :
    pairNFChiral h a0 a1 a2 b0 b1 b2 =
      ![1 + a0 * b0 + a1 * b1 - h * (a0 * b2 + a2 * b0) + h ^ 2 * (a2 * b2),
        a0 + b0 + h * a0 * b0 + a2 * b1 - h * (a2 + b2) - h ^ 2 * (a0 * b2 + a2 * b0)
          + h ^ 3 * (a2 * b2),
        a1 + b1 + h * a1 * b1 + a0 * b2 - h * (a2 * b2),
        a1 * b0 + a2 * b2 - h * (a1 * b2),
        a2 + b2 + a0 * b1 + h * (a0 * b2) - h ^ 2 * (a2 * b2),
        a2 * b0 + a1 * b2] := by
  rw [pairNFChiral_eq_pairNF, pairNF_eq]
  funext i; fin_cases i <;> simp <;> ring

/-- **`pairNF_affine` is a statement about the straight chart only.** In the
canonical chart the identity coordinate of `γ(0,0,1)·γ(0,0,1)` is `1 + h²`. -/
theorem pairNFChiral_deg0_quadratic (h : R) :
    pairNFChiral h 0 0 1 0 0 1 0 = 1 + h ^ 2 := by
  rw [pairNFChiral_eq]; simp

/-- The order-`h¹` coefficient of `NF(γγ)`. -/
def N1 (a0 a1 a2 b0 b1 b2 : R) : Fin 6 → R :=
  ![0, a0 * b0, a1 * b1, 0, a0 * b2 + a2 * b1, a2 * b2]

/-- **`NF(γγ)` is exactly affine in `h`**: no `h²` term. -/
theorem pairNF_affine (h a0 a1 a2 b0 b1 b2 : R) :
    pairNF h a0 a1 a2 b0 b1 b2 =
      pairNF 0 a0 a1 a2 b0 b1 b2 + h • N1 a0 a1 a2 b0 b1 b2 := by
  rw [pairNF_eq, pairNF_eq]
  funext i; fin_cases i <;> simp [N1] <;> ring

/-- The order-1 part lies in word degree ≥ 1. -/
theorem N1_deg0 (a0 a1 a2 b0 b1 b2 : R) : N1 a0 a1 a2 b0 b1 b2 0 = 0 := rfl

/-- The order-1 part is additive in `φ` … -/
theorem N1_bilin_left (a0 a1 a2 a0' a1' a2' b0 b1 b2 : R) :
    N1 (a0 + a0') (a1 + a1') (a2 + a2') b0 b1 b2 =
      N1 a0 a1 a2 b0 b1 b2 + N1 a0' a1' a2' b0 b1 b2 := by
  funext i; fin_cases i <;> simp [N1] <;> ring

/-- … additive in `ψ` … -/
theorem N1_bilin_right (a0 a1 a2 b0 b1 b2 b0' b1' b2' : R) :
    N1 a0 a1 a2 (b0 + b0') (b1 + b1') (b2 + b2') =
      N1 a0 a1 a2 b0 b1 b2 + N1 a0 a1 a2 b0' b1' b2' := by
  funext i; fin_cases i <;> simp [N1] <;> ring

/-- … and homogeneous in each slot. -/
theorem N1_smul (c a0 a1 a2 b0 b1 b2 : R) :
    N1 (c * a0) (c * a1) (c * a2) b0 b1 b2 = c • N1 a0 a1 a2 b0 b1 b2 ∧
    N1 a0 a1 a2 (c * b0) (c * b1) (c * b2) = c • N1 a0 a1 a2 b0 b1 b2 := by
  constructor <;> (funext i; fin_cases i <;> simp [N1] <;> ring)

/-- The order-1 part is not zero (two horizontal polarizations). -/
theorem N1_nonzero [Nontrivial R] : N1 (1 : R) 0 0 1 0 0 ≠ 0 := by
  intro h; have := congrFun h 1; simp [N1] at this

/-- **Word degree 0 is `h`-free** on the γγ product. -/
theorem pairNF_deg0_h_free (h h' a0 a1 a2 b0 b1 b2 : R) :
    pairNF h a0 a1 a2 b0 b1 b2 0 = pairNF h' a0 a1 a2 b0 b1 b2 0 := by
  simp [pairNF_eq]

/-- Flavour is invisible at order zero: at `h = 0` the flipped photon IS the
photon. -/
theorem photonBar_order_zero (a0 a1 a2 : R) :
    photonBar 0 a0 a1 a2 = photonStraight 0 a0 a1 a2 := by
  simp [photonBar, photonStraight]

/-- **Flavour reaches word degree 0 at order `h¹`.** Flipping `ψ`'s letters
moves the degree-0 coordinate by `h·(h ψ₀₁ − φ₀ψ₀₁ − φ₁ψ₀₁ − ψ₀ − ψ₁)`. -/
theorem flavour_reaches_deg0 (h a0 a1 a2 b0 b1 b2 : R) :
    mulNF h (photonStraight h a0 a1 a2) (photonBar h b0 b1 b2) 0
      - pairNF h a0 a1 a2 b0 b1 b2 0
      = h * (h * b2 - a0 * b2 - a1 * b2 - b0 - b1) := by
  simp [pairNF, photonStraight, photonBar, mulNF, mulσ₀, mulσ₁, e0, s0, s1]; ring

/-- The witness: a horizontal photon `ψ = σ₀` against the bare core. The
degree-0 coordinate moves by exactly `−h`, so "word degree 0 carries no
flavour" fails whenever `h ≠ 0` (scope (a): true only modulo `h`). -/
theorem flavour_reaches_deg0_witness (h : R) :
    mulNF h (photonStraight h 0 0 0) (photonBar h 1 0 0) 0 - pairNF h 0 0 0 1 0 0 0 = -h := by
  rw [flavour_reaches_deg0]; ring

/-- The word-degree ≥ 1 part. -/
def degPos (v : Fin 6 → R) : Fin 6 → R := v - v 0 • e0

/-- **Requirement (3) fails as stated**: with `φ = 0` the degree ≥ 1 part of
`NF(γγ)` is `ψ`'s own polarization, not `0`; a bilinear form vanishes at
`φ = 0`. -/
theorem degPos_not_bilinear [Nontrivial R] (h : R) :
    degPos (pairNF h 0 0 0 1 0 0) 1 ≠ 0 := by
  simp [degPos, pairNF_eq, e0]

/-- The connected part `NF((γ(φ)−1)(γ(ψ)−1))` — explicit, homogeneous
bilinear in `(φ, ψ)` — and `NF(γγ) = γ(φ) + γ(ψ) − 1 + connected`. -/
def connected (h a0 a1 a2 b0 b1 b2 : R) : Fin 6 → R :=
  ![a0 * b0 + a1 * b1, h * a0 * b0 + a2 * b1, h * a1 * b1 + a0 * b2,
    a2 * b2 + a1 * b0, a0 * b1 + h * (a0 * b2 + a2 * b1), a2 * b0 + a1 * b2 + h * a2 * b2]

theorem pairNF_eq_connected (h a0 a1 a2 b0 b1 b2 : R) :
    pairNF h a0 a1 a2 b0 b1 b2 =
      photonStraight h a0 a1 a2 + photonStraight h b0 b1 b2 - e0 + connected h a0 a1 a2 b0 b1 b2 := by
  rw [pairNF_eq, photonStraight_eq, photonStraight_eq]
  funext i; fin_cases i <;> simp [e0, connected] <;> ring

theorem connected_eq_mulNF (h a0 a1 a2 b0 b1 b2 : R) :
    connected h a0 a1 a2 b0 b1 b2 =
      mulNF h (photonStraight h a0 a1 a2 - e0) (photonStraight h b0 b1 b2 - e0) := by
  rw [photonStraight_eq, photonStraight_eq]
  funext i; fin_cases i <;>
    simp [connected, mulNF, mulσ₀, mulσ₁, e0] <;> ring


open Polynomial

/-! ## The quark state (owner decision D1, 2026-11-15): the `h¹` part of a letter

`h` is a formal variable: we work in `Fin 6 → R[X]` with `h := X`. The Hecke
relation `σ² = hσ + 1` involves only `h`, so every normal-form coefficient is a
polynomial in `h` whose coefficients are `q`-independent labels. The order-`k`
part is the coefficient of `X^k`, read off BEFORE any value of `q` is inserted.
A single letter is `σ_g` (flavour bit `true`) or `σ_g⁻¹ = σ_g − h`
(`false`). -/

/-- A single-letter quark: generator `g` (`true` = `σ₀`, `false` = `σ₁`) and
flavour bit `ε` (`true` = `σ`, `false` = `σ⁻¹ = σ − h`), with `h` formal. -/
noncomputable def quarkLetter (g ε : Bool) : Fin 6 → R[X] :=
  (if g then s0 else s1) + (if ε then (0 : R[X]) else -X) • e0

/-- The order-`h^k` part of an NF vector with polynomial coefficients. -/
noncomputable def hPart (k : ℕ) (v : Fin 6 → R[X]) : Fin 6 → R := fun i => (v i).coeff k

/-- **The quark state**: the `h¹` part of a single letter. -/
noncomputable def quarkState (g ε : Bool) : Fin 6 → R := hPart 1 (quarkLetter (R := R) g ε)

/-- The flavour shift: `0` for `σ`, `−1` for `σ⁻¹`. -/
def flavourShift (ε : Bool) : R := if ε then 0 else -1

/-- `σ⁻¹ = σ − h` holds in the NF algebra over `R[X]`: the two flavours of a
letter are mutually inverse. -/
theorem quarkLetter_inverse (g : Bool) :
    mulNF (X : R[X]) (quarkLetter g true) (quarkLetter g false) = (e0 : Fin 6 → R[X]) := by
  cases g <;> (funext i; fin_cases i <;> simp [quarkLetter, mulNF, mulσ₀, mulσ₁, e0, s0, s1])

/-- Order 0: a letter's `h⁰` part is its bare generator, the same for both
flavours (flavour is invisible). -/
theorem quarkLetter_order_zero (g ε : Bool) :
    hPart 0 (quarkLetter (R := R) g ε) = (if g then s0 else s1) := by
  cases g <;> cases ε <;> (funext i; fin_cases i <;> simp [hPart, quarkLetter, e0, s0, s1])

/-- The quark state is the flavour shift on the unit. NOTE: it sits in word
degree 0. -/
theorem quarkState_eq (g ε : Bool) :
    quarkState (R := R) g ε = flavourShift (R := R) ε • (e0 : Fin 6 → R) := by
  cases g <;> cases ε <;>
    (funext i; fin_cases i <;> simp [quarkState, hPart, quarkLetter, flavourShift, e0, s0, s1, Polynomial.coeff_one])

/-- Orders `≥ 2` vanish: a letter is exactly affine in `h`. -/
theorem quarkLetter_order_ge_two (g ε : Bool) (k : ℕ) (hk : 2 ≤ k) :
    hPart k (quarkLetter (R := R) g ε) = 0 := by
  have h1 : k ≠ 1 := by omega
  have h0 : k ≠ 0 := by omega
  cases g <;> cases ε <;>
    (funext i; fin_cases i <;>
      simp [hPart, quarkLetter, e0, s0, s1, Polynomial.coeff_X, Polynomial.coeff_one, h0, h1,
        Ne.symm h1, Ne.symm h0])

/-- The quark state distinguishes the flavours (non-vacuity). -/
theorem quarkState_flavour_ne [Nontrivial R] (g : Bool) :
    quarkState (R := R) g true ≠ quarkState g false := by
  rw [quarkState_eq, quarkState_eq]
  intro h; have := congrFun h 0; simp [flavourShift, e0] at this

/-- The two flavours of a letter differ by exactly `−h·1`: `σ⁻¹ − σ = −h`. The
difference is purely order `h¹` and sits in word degree 0. (The bar involution
`q ↦ q⁻¹` sends `h ↦ −h`; a bar-parity statement about the quark state is NOT
proved here.) -/
theorem quarkLetter_flavour_difference (g : Bool) :
    quarkLetter (R := R) g false - quarkLetter g true = (-X : R[X]) • (e0 : Fin 6 → R[X]) := by
  cases g <;> (funext i; fin_cases i <;> simp [quarkLetter, e0, s0, s1])

/-- The `h¹` part of the photon pair product is `N₁`, now as a statement about
the formal variable (labels are constants `C aᵢ`). -/
theorem pairNF_formal (a0 a1 a2 b0 b1 b2 : R) (i : Fin 6) :
    pairNF (X : R[X]) (C a0) (C a1) (C a2) (C b0) (C b1) (C b2) i =
      C (pairNF 0 a0 a1 a2 b0 b1 b2 i) + C (N1 a0 a1 a2 b0 b1 b2 i) * X := by
  rw [pairNF_eq, pairNF_eq]
  fin_cases i <;> simp only [N1, map_add, map_mul, map_one, map_zero] <;> simp <;> ring

/-- The `h¹` part of the photon pair product is `N₁`, now as a statement about
the formal variable (the labels are constants `C aᵢ`). -/
theorem hPart_one_pairNF (a0 a1 a2 b0 b1 b2 : R) :
    hPart 1 (pairNF (X : R[X]) (C a0) (C a1) (C a2) (C b0) (C b1) (C b2)) =
      N1 a0 a1 a2 b0 b1 b2 := by
  funext i
  simp [hPart, pairNF_formal, Polynomial.coeff_C]

/-! ## Flavour extraction from the photon pair (bean `qou-usxh`, exploration)

Question: can the D1 definition read a flavour bit off `NF(γγ)` WITHOUT a chosen
map? The only flavour-sensitive datum D1 provides is the `h¹` coefficient on the
unit (`quarkState_eq`). Call it the **net flavour**. It is additive, so on a sum
of letters it returns the sum of their flavour shifts, and nothing finer. -/

/-- Net flavour: the `h¹` coefficient on the unit. -/
noncomputable def netFlavour (v : Fin 6 → R[X]) : R := hPart 1 v 0

theorem netFlavour_add (u v : Fin 6 → R[X]) :
    netFlavour (u + v) = netFlavour u + netFlavour v := by
  simp [netFlavour, hPart]

theorem netFlavour_letter (g ε : Bool) :
    netFlavour (quarkLetter (R := R) g ε) = flavourShift ε := by
  have := congrFun (quarkState_eq (R := R) g ε) 0
  simpa [netFlavour, quarkState, e0] using this

/-- **(Q3) Residual freedom.** Per-letter flavour is NOT recoverable from a sum
of letters: `u` on `σ₀` plus `d` on `σ₁` is the same element as `d` on `σ₀`
plus `u` on `σ₁`. Only the net flavour is determined. -/
theorem letter_sum_flavour_swap :
    quarkLetter (R := R) true true + quarkLetter false false =
      quarkLetter true false + quarkLetter false true := by
  funext i; fin_cases i <;> simp [quarkLetter, e0, s0, s1]

/-- The photon pair (both photons built from `σ` letters, `q`-independent labels)
has net flavour zero, for EVERY colour content. -/
theorem pairNF_netFlavour (a0 a1 a2 b0 b1 b2 : R) :
    netFlavour (pairNF (X : R[X]) (C a0) (C a1) (C a2) (C b0) (C b1) (C b2)) = 0 := by
  simp only [netFlavour, hPart_one_pairNF]; rfl

/-- **(Q2) The nucleon flavours are not extractable from one photon pair.**
Write `NF(γγ)` as three letters plus any remainder of zero net flavour. Then all
three letters are `u`; `uud` and `udd` are impossible for every `(φ, ψ)`, so the
set asked for is EMPTY. `CharZero` is used only to separate `−1, −2, −3` from `0`. -/
theorem pairNF_three_letters_all_up [CharZero R] (a0 a1 a2 b0 b1 b2 : R)
    (g1 g2 g3 e1 e2 e3 : Bool) (r : Fin 6 → R[X]) (hr : netFlavour r = 0)
    (h : pairNF (X : R[X]) (C a0) (C a1) (C a2) (C b0) (C b1) (C b2) =
      quarkLetter g1 e1 + quarkLetter g2 e2 + quarkLetter g3 e3 + r) :
    e1 = true ∧ e2 = true ∧ e3 = true := by
  have key := congrArg netFlavour h
  rw [pairNF_netFlavour, netFlavour_add, netFlavour_add, netFlavour_add, hr,
    netFlavour_letter, netFlavour_letter, netFlavour_letter] at key
  cases e1 <;> cases e2 <;> cases e3 <;> simp [flavourShift] at key ⊢ <;> norm_num at key

/-- With the second photon flavour-flipped (`σ ↦ σ⁻¹` on its letters), the net
flavour is `−(ψ₀ + ψ₁ + (φ₀ + φ₁)ψ₀₁)`. The flavour comes from the photon's own
letters: it is an INPUT, not produced by the collision. -/
theorem pairBar_netFlavour (a0 a1 a2 b0 b1 b2 : R) :
    netFlavour (mulNF (X : R[X]) (photonStraight X (C a0) (C a1) (C a2))
      (photonBar X (C b0) (C b1) (C b2))) = -(b0 + b1 + (a0 + a1) * b2) := by
  have hd := flavour_reaches_deg0 (R := R[X]) X (C a0) (C a1) (C a2) (C b0) (C b1) (C b2)
  have h0 := pairNF_formal a0 a1 a2 b0 b1 b2 0
  have hv : mulNF (X : R[X]) (photonStraight X (C a0) (C a1) (C a2))
      (photonBar X (C b0) (C b1) (C b2)) 0 =
      C (pairNF 0 a0 a1 a2 b0 b1 b2 0) + C (-(b0 + b1 + (a0 + a1) * b2)) * X
        + C b2 * X ^ 2 := by
    rw [sub_eq_iff_eq_add] at hd
    rw [hd, h0]
    simp only [N1, map_add, map_mul, map_neg, map_zero]
    simp
    ring
  simp only [netFlavour, hPart, hv, Polynomial.coeff_add, Polynomial.coeff_C,
    Polynomial.coeff_C_mul, Polynomial.coeff_X_pow, Polynomial.coeff_X]
  simp

/-! ## Flavour readout from a WORD of letters (bean `qou-qs1x`)

A sum of letters loses which letter carries which bit (`letter_sum_flavour_swap`).
A PRODUCT keeps it, except inside a run of consecutive letters on the SAME
generator, because those commute (`sameGen_letters_commute`). The `h¹` part of the
word reads the bits off directly (`word010_hPart_one`); a same-generator run
leaves only the sum of its bits (`word001_hPart_one`). Measured over all
placements and flavour assignments, exactly, by
`computations/probes/quark_state/flavour_readout_word_probe.py`. -/

/-- A letter with a general shift: `σ_g + c·h·1`. -/
def letterH (h c : R) (g : Bool) : Fin 6 → R :=
  (if g then s0 else s1) + (c * h) • e0

/-- Letters on the same generator commute: they lie in the commutative
subalgebra generated by `σ_g`. So flavour bits inside a same-generator run can
only be read as a multiset. -/
theorem sameGen_letters_commute (h a b : R) (g : Bool) :
    mulNF h (letterH h a g) (letterH h b g) = mulNF h (letterH h b g) (letterH h a g) := by
  cases g <;> (funext i; fin_cases i <;> simp [letterH, mulNF, mulσ₀, mulσ₁, e0, s0, s1] <;> ring)

/-- The alternating word `ℓ₀(c₁)ℓ₁(c₂)ℓ₀(c₃)`. -/
def word010 (h c1 c2 c3 : R) : Fin 6 → R :=
  mulNF h (mulNF h (letterH h c1 true) (letterH h c2 false)) (letterH h c3 true)

theorem word010_eq (h c1 c2 c3 : R) :
    word010 h c1 c2 c3 =
      ![c1 * c2 * c3 * h ^ 3 + c2 * h, h ^ 2 * (c1 * c2 + c2 * c3 + c2), c1 * c3 * h ^ 2,
        c1 * h, c3 * h, 1] := by
  funext i; fin_cases i <;> simp [word010, letterH, mulNF, mulσ₀, mulσ₁, e0, s0, s1] <;> ring

/-- The builder-placement word `ℓ₀(c₁)ℓ₀(c₂)ℓ₁(c₃)`. -/
def word001 (h c1 c2 c3 : R) : Fin 6 → R :=
  mulNF h (mulNF h (letterH h c1 true) (letterH h c2 true)) (letterH h c3 false)

theorem word001_eq (h c1 c2 c3 : R) :
    word001 h c1 c2 c3 =
      ![c1 * c2 * c3 * h ^ 3 + c3 * h, h ^ 2 * (c1 * c3 + c2 * c3 + c3), c1 * c2 * h ^ 2 + 1,
        0, h * (c1 + c2 + 1), 0] := by
  funext i; fin_cases i <;> simp [word001, letterH, mulNF, mulσ₀, mulσ₁, e0, s0, s1] <;> ring

theorem word010_formal (c1 c2 c3 : R) :
    word010 (X : R[X]) (C c1) (C c2) (C c3) =
      ![C (c1 * c2 * c3) * X ^ 3 + C c2 * X, C (c1 * c2 + c2 * c3 + c2) * X ^ 2,
        C (c1 * c3) * X ^ 2, C c1 * X, C c3 * X, 1] := by
  rw [word010_eq]
  funext i; fin_cases i <;> simp only [map_mul, map_add, map_one] <;> simp <;> ring

/-- **Per-letter readout on the alternating word.** With `h` formal, the `h¹`
part is `(c₂, 0, 0, c₁, c₃, 0)`: each letter's bit sits on its own coordinate
(the word with that letter deleted). -/
theorem word010_hPart_one (c1 c2 c3 : R) :
    hPart 1 (word010 (X : R[X]) (C c1) (C c2) (C c3)) = ![c2, 0, 0, c1, c3, 0] := by
  rw [word010_formal]
  funext i
  fin_cases i <;>
    simp [hPart, Polynomial.coeff_C_mul_X_pow, Polynomial.coeff_C_mul_X, Polynomial.coeff_one,
      Polynomial.coeff_add, Polynomial.coeff_mul_X_pow']

theorem word001_formal (c1 c2 c3 : R) :
    word001 (X : R[X]) (C c1) (C c2) (C c3) =
      ![C (c1 * c2 * c3) * X ^ 3 + C c3 * X, C (c1 * c3 + c2 * c3 + c3) * X ^ 2,
        C (c1 * c2) * X ^ 2 + 1, 0, C (c1 + c2 + 1) * X, 0] := by
  rw [word001_eq]
  funext i; fin_cases i <;> simp only [map_mul, map_add, map_one] <;> simp <;> ring

/-- **The same-generator run on the builder word leaves only `c₁ + c₂`.** -/
theorem word001_hPart_one (c1 c2 c3 : R) :
    hPart 1 (word001 (X : R[X]) (C c1) (C c2) (C c3)) = ![c3, 0, 0, 0, c1 + c2 + 1, 0] := by
  rw [word001_formal]
  funext i
  fin_cases i <;>
    simp [hPart, Polynomial.coeff_C_mul_X_pow, Polynomial.coeff_C_mul_X, Polynomial.coeff_one,
      Polynomial.coeff_add, Polynomial.coeff_mul_X_pow']

end Generic

/-! ## The `(2,1)` channel -/

section Rep

variable {R : Type*} [Field R]

/-- `ρ(σ₀)` in the reduced-Burau `(2,1)` representation of the probe. -/
def rA (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, -q⁻¹; 0, -q⁻¹]
/-- `ρ(σ₁)`. -/
def rB (q : R) : Matrix (Fin 2) (Fin 2) R := !![-q⁻¹, 0; -q, q]

/-- `ρ` on the NF module, basis images `1, A, B, BA, AB, ABA`. -/
def rho (q : R) (v : Fin 6 → R) : Matrix (Fin 2) (Fin 2) R :=
  v 0 • 1 + v 1 • rA q + v 2 • rB q + v 3 • (rB q * rA q) + v 4 • (rA q * rB q)
    + v 5 • (rA q * rB q * rA q)

/-- **`ρ` is multiplicative** on the NF algebra at `h = q − q⁻¹`, so the
`(2,1)` projection of a normal form is well defined. -/
theorem rho_mul (q : R) (hq : q ≠ 0) (u v : Fin 6 → R) :
    rho q (mulNF (q - q⁻¹) u v) = rho q u * rho q v := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rho, rA, rB, mulNF, mulσ₀, mulσ₁, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

theorem rho_unit (q : R) : rho q e0 = 1 := by simp [rho, e0]

/-- The `(2,1)` projection of the word-degree ≥ 1 part of `NF(γ(φ)γ(ψ))`.
This was the agent's original "quark state" hypothesis. The owner RETIRED it as
the quark state on 2026-11-15 (D1/D2): at level 2 the `(2,1)` channel is a
three-strand, isospin-½, nucleon-type channel. It is kept under a neutral name
because the theorems about it still hold. -/
def pairChannelState (q a0 a1 a2 b0 b1 b2 : R) : Matrix (Fin 2) (Fin 2) R :=
  rho q (degPos (pairNF (q - q⁻¹) a0 a1 a2 b0 b1 b2))

/-- The γγ product's `(2,1)` image splits as the degree-0 scalar plus the
quark state. -/
theorem rho_pairNF_split (q a0 a1 a2 b0 b1 b2 : R) :
    rho q (pairNF (q - q⁻¹) a0 a1 a2 b0 b1 b2) =
      (1 + a0 * b0 + a1 * b1) • 1 + pairChannelState q a0 a1 a2 b0 b1 b2 := by
  have : pairNF (q - q⁻¹) a0 a1 a2 b0 b1 b2 0 = 1 + a0 * b0 + a1 * b1 := by
    simp [pairNF_eq]
  simp only [pairChannelState, degPos, this]
  ext i j; fin_cases i <;> fin_cases j <;> simp [rho, e0] <;> ring

/-! ### `results.md:9-13` as theorems

A template letter is `ρ(σ_g) + c·h·1` (every `σ^{±1}` and every averaged pair
is of this form, since `σ⁻¹ = σ − h`). The nucleon word is the Borromean core
`(σ₀σ₁⁻¹)³` followed by three quark letters on generators `0, 0, 1`. -/

/-- Template letters, written out entrywise: `ρ(σ₀) + c·h·1` and
`ρ(σ₁) + c·h·1` with `h = q − q⁻¹`. -/
def lA (q c : R) : Matrix (Fin 2) (Fin 2) R :=
  !![q + c * (q - q⁻¹), -q⁻¹; 0, -q⁻¹ + c * (q - q⁻¹)]
def lB (q c : R) : Matrix (Fin 2) (Fin 2) R :=
  !![-q⁻¹ + c * (q - q⁻¹), 0; -q, q + c * (q - q⁻¹)]

theorem lA_eq (q c : R) : lA q c = rA q + (c * (q - q⁻¹)) • 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [lA, rA]
theorem lB_eq (q c : R) : lB q c = rB q + (c * (q - q⁻¹)) • 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [lB, rB]

/-- **The nucleon state** (owner decision D2, 2026-11-15): the `(2,1)` image of
the core-plus-quarks word `(σ₀σ₁⁻¹)³ · ℓ₀(c₁) ℓ₀(c₂) ℓ₁(c₃)`. With
`cᵢ = flavourShift εᵢ` it is built from three single-letter quark states
(`nucleonStateOfQuarks`). The corpus `AVG` pair rule gives `c = −½`, which is
a pair AVERAGE and NOT a single letter. -/
def nucleonState (q c1 c2 c3 : R) : Matrix (Fin 2) (Fin 2) R :=
  lA q 0 * lB q (-1) * lA q 0 * lB q (-1) * lA q 0 * lB q (-1)
    * lA q c1 * lA q c2 * lB q c3

/-- The nucleon state built from three single-letter quark states. -/
def nucleonStateOfQuarks (q : R) (ε₁ ε₂ ε₃ : Bool) : Matrix (Fin 2) (Fin 2) R :=
  nucleonState q (flavourShift ε₁) (flavourShift ε₂) (flavourShift ε₃)

/-- A letter's `(2,1)` image IS the nucleon-word factor: evaluating `h` at
`q − q⁻¹` and applying `ρ` to `σ_g + c·h·1` gives `lA`/`lB`. -/
theorem rho_letter (q c : R) :
    rho q (s0 + (c * (q - q⁻¹)) • e0) = lA q c ∧
    rho q (s1 + (c * (q - q⁻¹)) • e0) = lB q c := by
  constructor <;>
    (ext i j; fin_cases i <;> fin_cases j <;> simp [rho, rA, rB, lA, lB, s0, s1, e0] <;> ring)

/-- **Order `t⁰`: flavour is invisible.** At `q = 1` the `(2,1)` character of
the nucleon word is `0` for EVERY choice of quark shifts. -/
theorem template_order_zero (c1 c2 c3 : R) :
    (nucleonState (1 : R) c1 c2 c3).trace = 0 := by
  simp only [nucleonState, lA, lB, Matrix.mul_fin_two, Matrix.trace_fin_two,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.head_cons, Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_fin_const,
    inv_one]
  ring

set_option maxHeartbeats 4000000 in
/-- The flavour-blind template `S0` (all quark letters `σ`): character
identically `0`. -/
theorem template_S0_zero (q : R) (hq : q ≠ 0) :
    (nucleonState q 0 0 0).trace = 0 := by
  simp only [nucleonState, lA, lB, Matrix.mul_fin_two, Matrix.trace_fin_two,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.head_cons, Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_fin_const]
  field_simp
  ring

/-- The cofactor `g(q) = (q+1)(q⁴+1)P(q)/(4q⁹)` of the corpus template. -/
noncomputable def gSplus (q : R) : R :=
  (q + 1) * (q ^ 4 + 1)
    * (q ^ 12 - 2 * q ^ 10 + 2 * q ^ 8 - 3 * q ^ 6 + 2 * q ^ 4 - 2 * q ^ 2 + 1)
    / (4 * q ^ 9)

set_option maxHeartbeats 4000000 in
/-- **Order `t¹`: flavour is decided.** For the corpus template `S+ AVG` on the
proton (shifts `0, −½, −½`) the `(2,1)` character is `(q − 1)·g(q)`. -/
theorem template_SplusAVG_proton (q : R) (hq : q ≠ 0) (h2 : (2 : R) ≠ 0) :
    (nucleonState q 0 (-1 / 2) (-1 / 2)).trace = (q - 1) * gSplus q := by
  have h4 : (4 : R) ≠ 0 := by
    have : (4 : R) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  simp only [nucleonState, lA, lB, gSplus, Matrix.mul_fin_two, Matrix.trace_fin_two,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.head_cons, Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_fin_const]
  field_simp
  ring

/-- …and the `t¹` coefficient is nonzero: `g(1) = −1`. -/
theorem gSplus_one (h2 : (2 : R) ≠ 0) : gSplus (1 : R) = -1 := by
  have h4 : (4 : R) ≠ 0 := by
    have : (4 : R) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  simp [gSplus]
  field_simp
  norm_num

/-- **The `(2,1)` channel cannot see a global flavour flip of `Δ = σ₀σ₁σ₀`.**
`ρ(Δ⁻¹) = ρ(Δ)`, equivalently the full twist `Δ²` acts as `1` on `(2,1)`. So on
the alternating word, `uuu` and `ddd` have the same nucleon state, although the
full normal forms differ (`word010_hPart_one`). -/
theorem rho_delta_inv (q : R) (hq : q ≠ 0) :
    lA q (-1) * lB q (-1) * lA q (-1) = rA q * rB q * rA q := by
  simp only [lA, lB, rA, rB, Matrix.mul_fin_two]
  ext i j; fin_cases i <;> fin_cases j <;> simp <;> field_simp <;> ring

theorem rho_delta_sq (q : R) (hq : q ≠ 0) :
    rA q * rB q * rA q * (rA q * rB q * rA q) = 1 := by
  simp only [rA, rB, Matrix.mul_fin_two]
  ext i j; fin_cases i <;> fin_cases j <;> simp
  all_goals (try field_simp)
  all_goals (try ring_nf)
  all_goals (try simp)

end Rep

end QOU.QuarkState
