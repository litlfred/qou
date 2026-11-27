import QOU.Core.QuantaleCut
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# QOU.Core.MassInRing — the canonical nucleon mass as a ring element

Bean `qou-5o1v` (constructive item 2.1), owner ruling 2026-11-27: *mass is valued in the
ring*. Absolute values, norms and logarithms enter only at the comparison step.

The canonical muon-anchored identity (`computations/canonical_mass.py`) in units of `m_e` is

  `m_μ/m_e = v / ℏ_q²`,  `ℏ_q = 1 − q⁻¹`,
  `F_Bor = tr_M(β_Bor) · [3]_q! / q³`,
  `m_p/m_e = 2 (m_μ/m_e · F_Bor − 6)`.

Here `v` is the hyperbolic volume `Vol(4₁)` and `tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h² + 4)`,
with `h = q − q⁻¹` (convention D, `BraidKnotOctonion/BorromeanMarkovTrace.lean`).

This file states all of it over an **arbitrary field** `F` containing `q` and a symbol `v`.
The intended instance is `F = ℚ(q, v)`. There are three results.

* `massProton_eq_affine`: `m_p/m_e = A(q)·v − 12`, where the slope `A(q) ∈ ℚ(q)` is explicit.
  All `q`-dependence is rational, and the one transcendental constant `v` enters linearly.
* `map_massProton`: any ring hom `φ : F →+* K` of fields (evaluation at a point, an embedding
  into `ℝ`, reduction, …) commutes with the mass. So evaluating is applying a ring hom, and a
  comparison with data is a cut on the image.
* `trBor_bar`: `tr_M(β_Bor)` is invariant under `q ↦ q⁻¹`.

**Alignment with the cut core (`QOU.Core.QuantaleCut`).** `NearMap` is a map of near systems,
and `LCut.map` pushes a cut along it, so `ev` and located `coev` are carried over.
* Ordered instance (Dedekind, surreal): `massCut a c` pushes a cut `c` for the volume through
  `x ↦ a·x − 12`, where `a = φ(A(q))` is the evaluated slope. It is located whenever `c` is
  (`massCut_locatedAt`).
* Adic instance (`h`-adic, Habiro, `p`-adic): `ringHomNearMap` pushes a tower cut along any
  ring hom that respects the ideal towers, so stagewise mass comparisons are maps of `LCut`s.

**The absolute value is dropped.** The Python facade writes `|tr_M|`. In the ring there is no
absolute value, so the sign is decided at comparison time. That is the point of the ruling.

**No numerical value appears**: no CODATA constant and no value of `q₀` or of `Vol(4₁)`. This
supersedes `QOU.Substrate.ProtonMassSubstrateIdentity`, which declares `F_Bor` as an `opaque`
real and proves a residual against CODATA values inside a theorem.
-/

namespace QOU.Core.MassInRing

variable {F : Type*} [Field F]

/-- `h = q − q⁻¹`. -/
def hQ (q : F) : F := q - q⁻¹

/-- `ℏ_q = 1 − q⁻¹`. -/
def hbarQ (q : F) : F := 1 - q⁻¹

/-- `[3]_q! = [3]_q [2]_q [1]_q` with balanced `q`-integers `[2] = q + q⁻¹`, `[3] = q² + 1 + q⁻²`. -/
def qFact3 (q : F) : F := (q ^ 2 + 1 + q⁻¹ ^ 2) * (q + q⁻¹)

/-- `tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h² + 4)`. -/
def trBor (q : F) : F :=
  (4 + hQ q ^ 2 - 3 * hQ q ^ 4 - hQ q ^ 6) / (hQ q ^ 2 + 4)

/-- `F_Bor = tr_M(β_Bor) · [3]_q! / q³`, with no absolute value. -/
def fBor (q : F) : F := trBor q * qFact3 q / q ^ 3

/-- `m_μ / m_e = v / ℏ_q²`. -/
def massMuon (q v : F) : F := v / hbarQ q ^ 2

/-- `m_p / m_e = 2 (m_μ/m_e · F_Bor − 6)`. -/
def massProton (q v : F) : F := 2 * (massMuon q v * fBor q - 6)

/-- The slope `A(q) = 2 · tr_M(β_Bor) · [3]_q! / (q³ ℏ_q²)`, an element of `ℚ(q)`. -/
def protonSlope (q : F) : F := 2 * trBor q * qFact3 q / (q ^ 3 * hbarQ q ^ 2)

/-- **Mass is affine in the volume, with rational slope.** `m_p/m_e = A(q)·v − 12`. -/
theorem massProton_eq_affine (q v : F) : massProton q v = protonSlope q * v - 12 := by
  unfold massProton massMuon fBor protonSlope
  ring

/-- `h(q⁻¹) = −h(q)`. -/
theorem hQ_inv (q : F) : hQ q⁻¹ = -hQ q := by
  unfold hQ
  rw [inv_inv]
  ring

/-- **Bar symmetry.** `tr_M(β_Bor)` is invariant under `q ↦ q⁻¹` (it is even in `h`). -/
theorem trBor_bar (q : F) : trBor q⁻¹ = trBor q := by
  unfold trBor
  rw [hQ_inv]
  ring

/-- `[3]_q!` is bar-invariant. -/
theorem qFact3_bar (q : F) : qFact3 q⁻¹ = qFact3 q := by
  unfold qFact3
  rw [inv_inv]
  ring

section Evaluation

variable {K : Type*} [Field K]

/-- **Evaluation is a ring hom.** Any `φ : F →+* K` sends the ring-valued mass to the mass
computed from `φ q` and `φ v`. -/
theorem map_massProton (φ : F →+* K) (q v : F) :
    φ (massProton q v) = massProton (φ q) (φ v) := by
  simp only [massProton, massMuon, fBor, trBor, qFact3, hbarQ, hQ, map_mul, map_sub, map_add,
    map_div₀, map_inv₀, map_pow, map_one, map_ofNat]

theorem map_protonSlope (φ : F →+* K) (q : F) :
    φ (protonSlope q) = protonSlope (φ q) := by
  simp only [protonSlope, trBor, qFact3, hbarQ, hQ, map_mul, map_sub, map_add,
    map_div₀, map_inv₀, map_pow, map_one, map_ofNat]

end Evaluation

/-! ### Alignment with the quantale cut core -/

open QOU.Core.LawvereCut

section Transport

variable {V W X Y : Type*} [Preorder V] [Resolution V] [Preorder W] [Resolution W]

/-- A map of near systems: a point map `f` and a resolution map `g` that send `near ε` to
`near (g ε)`, with `g` sub-multiplicative for `comb`. -/
structure NearMap (N : NearSystem V X) (M : NearSystem W Y) where
  f : X → Y
  g : V → W
  near_map : ∀ {ε : V} {x y : X}, N.near ε x y → M.near (g ε) (f x) (f y)
  g_comb : ∀ ε δ : V, g (Resolution.comb ε δ) ≤ Resolution.comb (g ε) (g δ)

/-- Push a Lawvere cut along a map of near systems. -/
def _root_.QOU.Core.LawvereCut.LCut.map {N : NearSystem V X} {M : NearSystem W Y}
    (Φ : NearMap N M) (c : LCut N) :
    LCut M where
  approx w y := ∃ ε x, c.approx ε x ∧ Φ.f x = y ∧ Φ.g ε ≤ w
  ev := by
    rintro w w' a b ⟨ε, x, hx, rfl, hε⟩ ⟨δ, z, hz, rfl, hδ⟩
    exact M.mono ((Φ.g_comb ε δ).trans (Resolution.comb_mono hε hδ)) (Φ.near_map (c.ev hx hz))

/-- Locatedness transfers whenever every admissible target resolution dominates the image of an
admissible source resolution. -/
theorem _root_.QOU.Core.LawvereCut.LCut.map_locatedAt {N : NearSystem V X}
    {M : NearSystem W Y} (Φ : NearMap N M)
    {c : LCut N} {pos : V → Prop} {pos' : W → Prop} (hc : c.LocatedAt pos)
    (hg : ∀ w, pos' w → ∃ ε, pos ε ∧ Φ.g ε ≤ w) : (c.map Φ).LocatedAt pos' := by
  intro w hw
  obtain ⟨ε, hε, hle⟩ := hg w hw
  obtain ⟨x, hx⟩ := hc ε hε
  exact ⟨Φ.f x, ε, x, hx, rfl, hle⟩

end Transport

section OrderedMass

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The affine map `x ↦ a·x + b` is `|a|`-Lipschitz for `ordNear`. -/
def affineNearMap (a b : K) : NearMap (ordNear K) (ordNear K) where
  f x := a * x + b
  g ε := |a| * ε
  near_map {ε x y} h := by
    show |a * x + b - (a * y + b)| ≤ |a| * ε
    rw [show a * x + b - (a * y + b) = a * (x - y) by ring, abs_mul]
    exact mul_le_mul_of_nonneg_left h (abs_nonneg a)
  g_comb ε δ := le_of_eq (mul_add _ _ _)

/-- **The mass as a Dedekind/surreal cut.** With `a = φ(A(q))` the evaluated slope and `c` a
cut for the volume, `m_p/m_e = a·v − 12` is the pushed cut. -/
def massCut (a : K) (c : LCut (ordNear K)) : LCut (ordNear K) :=
  c.map (affineNearMap a (-12))

/-- The mass cut is located whenever the volume cut is. -/
theorem massCut_locatedAt (a : K) {c : LCut (ordNear K)}
    (hc : c.LocatedAt (fun ε => 0 < ε)) : (massCut a c).LocatedAt (fun ε => 0 < ε) := by
  refine LCut.map_locatedAt (affineNearMap a (-12)) hc ?_
  intro w hw
  rcases eq_or_ne a 0 with ha | ha
  · exact ⟨1, one_pos, by simp [affineNearMap, ha, hw.le]⟩
  · have h' : |a| ≠ 0 := abs_ne_zero.mpr ha
    refine ⟨w / |a|, div_pos hw (abs_pos.mpr ha), le_of_eq ?_⟩
    show |a| * (w / |a|) = w
    field_simp

end OrderedMass

section AdicMass

variable {R S : Type*} [CommRing R] [CommRing S]

/-- A ring hom respecting ideal towers is a map of adic near systems (resolution unchanged). -/
def ringHomNearMap (ψ : R →+* S) (I : ℕ → Ideal R) (hI : Antitone I)
    (J : ℕ → Ideal S) (hJ : Antitone J) (hIJ : ∀ n, I n ≤ Ideal.comap ψ (J n)) :
    NearMap (adicNear I hI) (adicNear J hJ) where
  f := ψ
  g := id
  near_map {ε x y} h := by
    show ψ x - ψ y ∈ J ε.n
    have h' : ψ (x - y) ∈ J ε.n := hIJ ε.n h
    simpa only [map_sub] using h'
  g_comb _ _ := le_refl _

end AdicMass

end QOU.Core.MassInRing
