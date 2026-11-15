/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.Tactic

/-!
# QOU.QBeta.BirkhoffAmplitudeWellPosed — is the A=3 amplitude `E` a gauge-invariant of the Birkhoff connection matrix, or does it require the full (frame-dependent) monodromy? A WELL-POSEDNESS result.

**Scope (read this first).**  Two merged results pinned the A=3 anti-self-adjoint amplitude
`E` to the GLOBAL `0↔∞` Birkhoff connection matrix `P = (X^∞)⁻¹ X^0` of the DM q-cubic
carrier C1:

* `QOU.QBeta.A3AntiSelfAdjointLift` (#4611) bracketed the A=3 lift `r* = μ₃/c₃ ≈ 1.585` to
  **one** free real DOF — the anti-self-adjoint amplitude `E := C + σ B` — and proved
  `E ↦ factor` is an affine **bijection** (`amplitude_surjective`/`amplitude_injective`),
  with any genuine lift forcing `E ≠ 0` (`amplitude_nonzero`).
* `QOU.QBeta.StokesAmplitudeE` (#4811) walled the LOCAL Stokes route: a single-slope carrier
  gives `E = 0`, a multi-slope carrier leaves `E` free — its value living in the **global**
  Birkhoff matrix, not local Stokes data (`stokesAmplitude_surjective_of_dim_pos` + the §3b
  `GlobalBirkhoffSuppliesAmplitude` carrier).

Before anyone reads a value off `P`, this file answers the **well-posedness** question — the
mirror of the μ₃-target-robustness audits (`2026-08-01-mu3-target-{frame-robustness,robustness}`):
**is `E` a single entry of `P`, or does the anti-self-adjoint amplitude require the FULL
monodromy representation (a gauge-dependent combination)?**  Establish what is frame-free
BEFORE a value is extracted, so the sibling's explicit construction (they own
`BirkhoffAmplitudeE.lean`) targets the right invariant.

**The residual gauge freedom (a CITED structural fact, not a fit).**  By
`QOU.MathlibExt.QCharacter`, the canonical local solutions `X^{(0)} = M^{(0)} e_{q,A(0)}`,
`X^{(∞)} = M^{(∞)} e_{q,A(∞)}` are built from q-characters `e_{q,c}` — and a q-character is
unique only **up to multiplication by a `q`-invariant (elliptic / theta) unit**
(`IsQChar.ratio_qInvariant`: two solutions with the same multiplier differ by a q-invariant
ratio).  Choosing the normalisation of the two local bases is therefore a residual **gauge
freedom**: `X^{(0)} ↦ X^{(0)} D_0`, `X^{(∞)} ↦ X^{(∞)} D_∞` with `D_0, D_∞` q-invariant
diagonal matrices, under which the connection matrix transforms

  `P  ↦  D_∞⁻¹ · P · D_0`,   entrywise   `P_{ij} ↦ (d_∞,i)⁻¹ · P_{ij} · (d_0,j)`.

C1 is rank 2 (its two exponents `λ₊, λ₋` at `0`, `C1ModuleExponents`), so `P` is `2×2`.  This
file models that `2×2` gauge action over a generic field and proves exactly what is, and is
not, frame-free.

**Net verdict — MIXED, both branches proved sorry-free.**

* **(a) There IS a specific gauge-invariant functional — the cross-ratio.**  The functional
  `crossRatio P := P₀₁·P₁₀ / (P₀₀·P₁₁)` is invariant under the full residual gauge action
  (`crossRatio_gauge_invariant`).  Moreover it is essentially the **unique** invariant: the
  gauge group `(K^×)⁴` fixes a generic `P` only on its 1-parameter global-scale subgroup
  (`gauge_fixes_all_iff` ⇒ stabiliser `≅ K^×`), leaving `4 − 3 = 1` independent invariant on
  the four entries.  **This is what the sibling must compute** — a frame-free scalar.

* **(b) A single entry is NOT gauge-invariant — it carries a residual elliptic-unit freedom.**
  Any off-diagonal entry `P₀₁` is only defined up to multiplication by an **arbitrary
  `q`-invariant unit** `u = (d_∞,0)⁻¹ d_0,1` (`entry_gauge_orbit_surjective`: every `u·P₀₁` is
  reachable; `entry_not_gauge_invariant`: a nontrivial gauge changes it).  So reading `E` off a
  single entry is **ill-posed**: it needs an extra normalisation datum to pin the gauge — a
  scope-(a) well-posedness caveat.  The residual freedom is the full multiplicative group of
  q-invariant (elliptic) units, i.e. the two diagonal gauges `D_0, D_∞` modulo their common
  scale: `dim = 2·2 − 1 = 3` scalar gauges on the matrix, of which a single entry sees the
  quotient `1`-parameter elliptic unit as pure ambiguity.

**Consequence for `E` (the honest identification, recorded as an OPEN §3b carrier).**  `E` is a
**physical amplitude** — the A=3 mass lift `r*` is a frame-free observable
(`A3AntiSelfAdjointLift.amplitude_injective` makes it a well-defined function of the factor), so
whatever functional of `P` supplies `E` must be gauge-invariant.  By (b) it therefore **cannot**
be a single entry of `P`; by (a) it must be the gauge-invariant cross-ratio (the unique
invariant).  We record `E = crossRatio(P)`, `E ≠ 0`, as the §3b dependent conjecture
`AmplitudeIsGaugeInvariantCrossRatio` with **NO instance** — building `P` and evaluating its
cross-ratio is the open successor; *choosing* `crossRatio` to hit `r*` would be the forbidden
fit (`amplitude_surjective`) and is not done.

**Honesty (STRICT).**  Five sorry-free structural theorems (a cross-ratio invariance identity,
an entry-orbit surjectivity, an entry non-invariance witness, a stabiliser characterisation, and
their composition), no `native_decide`, no trivial-true, no axiom.  The gauge action is a CITED
model (RSZ/Sauloy q-character normalisation freedom), stated as the residual gauge, never a
derivation of `E`.  Nothing fitted, nothing wired; `r*`/`μ₃`/`c₃`/AME/CODATA/`q₀` never inverted;
`q₀`-derivation not routed through.

**Base ring (§7c).**  Generic `{K : Type*} [Field K]` throughout — the gauge scalars are
q-invariant units (inverses `d⁻¹` genuinely required, §7c `[Field K]` carve-out), and the
connection-matrix entries live in the elliptic function field.  No `ℝ`, no `Real.*`; the numerics
`r* ≈ 1.585` live only in the Python witness / audit, downstream of the substrate→archimedean
wall.  The bar involution `σ` (which makes `E` bar-odd, `DTIndexAmplitudeE.amplitude_barOdd`) is
not needed for the gauge algebra; the bar-oddness of `crossRatio(P)` is a *consistency check* the
sibling's `P` must satisfy, noted here, not proved (no concrete `σ` on `P`'s entries yet).

## References

- [leitner2026] `QOU.MathlibExt.QCharacter` (`IsQChar.ratio_qInvariant` — the elliptic
  normalisation freedom that IS the residual gauge; `c1_det_character`);
  `QOU.QBeta.A3AntiSelfAdjointLift` (`amplitude_surjective`/`amplitude_injective`/`amplitude_nonzero`
  — `E` is the single free/unique/forced DOF);
  `QOU.QBeta.StokesAmplitudeE` (`GlobalBirkhoffSuppliesAmplitude` — `E`'s value lives in the
  global Birkhoff matrix, the object this file tests for well-posedness);
  `docs/audits/2026-08-01-branch-selection-birkhoff-connection-matrix.md` (the `P = (X^∞)⁻¹X^0`
  recipe); `docs/audits/2026-08-01-mu3-target-frame-robustness.md` (the frame-free-before-extract
  discipline this mirrors); bean `qou-wiub` (the A=3 magnitude keystone); `qou-jqof`.
- [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (the Birkhoff connection matrix of a
  q-difference module and its q-invariant normalisation gauge).
-/

noncomputable section

namespace QOU.QBeta.BirkhoffAmplitudeWellPosed

/-! ### The residual gauge action on a `2×2` Birkhoff connection matrix.

`P = (X^∞)⁻¹ X^0` is defined only up to the normalisation of the two local solution bases,
each a `q`-invariant (elliptic) diagonal matrix.  The row index `i` is the `∞`-side, the column
index `j` the `0`-side; the residual gauge acts entrywise by `P_{ij} ↦ (d_∞,i)⁻¹ · P_{ij} · d_0,j`. -/

/-- **Gauge action on one connection-matrix entry.**  `d_∞,i` is the `∞`-side (row) normalisation,
    `d_0,j` the `0`-side (column) normalisation — both `q`-invariant (elliptic) units. -/
def gaugeEntry {K : Type*} [Field K] (dinf_i d0_j Pij : K) : K := dinf_i⁻¹ * Pij * d0_j

/-- **The candidate frame-free functional: the cross-ratio** `P₀₁·P₁₀ / (P₀₀·P₁₁)`.  This is the
    off-diagonal-over-diagonal product ratio — the natural invariant of a `2×2` matrix under the
    diagonal×diagonal gauge. -/
def crossRatio {K : Type*} [Field K] (P00 P01 P10 P11 : K) : K := P01 * P10 / (P00 * P11)

/-! ### (a) The cross-ratio is GAUGE-INVARIANT (frame-free). -/

/-- **The cross-ratio is invariant under the full residual gauge (sorry-free).**  Under
    `P_{ij} ↦ (d_∞,i)⁻¹ P_{ij} d_0,j` the four gauge units `d_∞,0, d_∞,1, d_0,0, d_0,1` each cancel
    between numerator and denominator of `P₀₁·P₁₀/(P₀₀·P₁₁)`.  So the cross-ratio is a
    **frame-free** functional of the Birkhoff matrix — the well-posed target for reading `E`. -/
theorem crossRatio_gauge_invariant {K : Type*} [Field K]
    (P00 P01 P10 P11 dinf0 dinf1 d00 d01 : K)
    (hi0 : dinf0 ≠ 0) (hi1 : dinf1 ≠ 0) (h00 : d00 ≠ 0) (h01 : d01 ≠ 0)
    (hP00 : P00 ≠ 0) (hP11 : P11 ≠ 0) :
    crossRatio (gaugeEntry dinf0 d00 P00) (gaugeEntry dinf0 d01 P01)
               (gaugeEntry dinf1 d00 P10) (gaugeEntry dinf1 d01 P11)
      = crossRatio P00 P01 P10 P11 := by
  unfold crossRatio gaugeEntry
  field_simp

/-! ### (b) A single entry is NOT gauge-invariant — the residual elliptic-unit freedom. -/

/-- **A single off-diagonal entry carries a full elliptic-unit gauge freedom (sorry-free).**  For
    ANY nonzero target unit `u` there is a genuine gauge (`d ≠ 0`) realising `P₀₁ ↦ u · P₀₁`
    (witness `d_∞,0 = 1`, `d_0,1 = u`).  So a single connection-matrix entry is defined only up to
    multiplication by an arbitrary `q`-invariant (elliptic) unit: reading `E` off one entry is
    **ill-posed**, needing an extra normalisation datum to pin the gauge.  The residual freedom is
    the whole multiplicative group of q-invariant units. -/
theorem entry_gauge_orbit_surjective {K : Type*} [Field K] (P01 u : K) (hu : u ≠ 0) :
    ∃ dinf0 d01 : K, dinf0 ≠ 0 ∧ d01 ≠ 0 ∧ gaugeEntry dinf0 d01 P01 = u * P01 :=
  ⟨1, u, one_ne_zero, hu, by unfold gaugeEntry; rw [inv_one]; ring⟩

/-- **The gauge fixes an entry iff the two normalisations match on it (sorry-free).**  For a
    nonzero entry, `gaugeEntry d_∞ d_0 P = P ↔ d_0 = d_∞`.  The row/column normalisations must
    coincide to leave the entry untouched — the atom of the stabiliser count. -/
theorem gaugeEntry_fix_iff {K : Type*} [Field K] (dinf d0 P : K)
    (hinf : dinf ≠ 0) (hP : P ≠ 0) : gaugeEntry dinf d0 P = P ↔ d0 = dinf := by
  unfold gaugeEntry
  constructor
  · intro h
    have h2 : dinf * (dinf⁻¹ * P * d0) = dinf * P := by rw [h]
    rw [← mul_assoc, ← mul_assoc, mul_inv_cancel₀ hinf, one_mul] at h2
    -- h2 : P * d0 = dinf * P
    have h3 : P * d0 = P * dinf := by rw [h2]; exact mul_comm dinf P
    exact mul_left_cancel₀ hP h3
  · intro h
    rw [h, mul_comm dinf⁻¹ P, mul_assoc, inv_mul_cancel₀ hinf, mul_one]

/-- **A nontrivial gauge genuinely moves a single entry (sorry-free).**  If the two
    normalisations differ (`d_0 ≠ d_∞`) then the entry changes: `gaugeEntry d_∞ d_0 P ≠ P`.  A
    single entry is therefore NOT gauge-invariant — the direct contrapositive of
    `gaugeEntry_fix_iff`, exhibited as the (b) non-invariance. -/
theorem entry_not_gauge_invariant {K : Type*} [Field K] (dinf d0 P : K)
    (hinf : dinf ≠ 0) (hP : P ≠ 0) (hne : d0 ≠ dinf) : gaugeEntry dinf d0 P ≠ P := by
  rw [ne_eq, gaugeEntry_fix_iff dinf d0 P hinf hP]; exact hne

/-! ### The residual-freedom dimension: the gauge stabiliser is the 1-parameter global scale. -/

/-- **The gauge fixes ALL four entries iff it is a global scale (sorry-free).**  With every entry
    nonzero, `P` is fixed by the gauge `(d_∞,0, d_∞,1, d_0,0, d_0,1)` iff
    `d_0,0 = d_∞,0`, `d_0,1 = d_∞,0`, and `d_∞,1 = d_∞,0` — i.e. all four normalisations are equal
    (the global scale `t·I`).  So the stabiliser of a generic `2×2` connection matrix is the
    1-parameter subgroup `K^×`; the gauge group `(K^×)⁴` acts with `4 − 1 = 3` effective scalar
    DOF on the four entries, leaving exactly `4 − 3 = 1` independent invariant — the cross-ratio.
    This is the rigorous **dimension count** behind the well-posedness verdict. -/
theorem gauge_fixes_all_iff {K : Type*} [Field K]
    (P00 P01 P10 P11 dinf0 dinf1 d00 d01 : K)
    (hi0 : dinf0 ≠ 0) (hi1 : dinf1 ≠ 0)
    (hP00 : P00 ≠ 0) (hP01 : P01 ≠ 0) (hP10 : P10 ≠ 0) (hP11 : P11 ≠ 0) :
    (gaugeEntry dinf0 d00 P00 = P00 ∧ gaugeEntry dinf0 d01 P01 = P01 ∧
     gaugeEntry dinf1 d00 P10 = P10 ∧ gaugeEntry dinf1 d01 P11 = P11)
      ↔ (d00 = dinf0 ∧ d01 = dinf0 ∧ dinf1 = dinf0) := by
  rw [gaugeEntry_fix_iff dinf0 d00 P00 hi0 hP00,
      gaugeEntry_fix_iff dinf0 d01 P01 hi0 hP01,
      gaugeEntry_fix_iff dinf1 d00 P10 hi1 hP10,
      gaugeEntry_fix_iff dinf1 d01 P11 hi1 hP11]
  constructor
  · rintro ⟨h00, h01, h10, h11⟩
    -- h00 : d00 = dinf0, h01 : d01 = dinf0, h10 : d00 = dinf1, h11 : d01 = dinf1
    refine ⟨h00, h01, ?_⟩
    -- dinf1 = dinf0 from d00 = dinf0 and d00 = dinf1
    rw [← h10, h00]
  · rintro ⟨h00, h01, hi⟩
    exact ⟨h00, h01, by rw [hi, h00], by rw [hi, h01]⟩

/-! ### The well-posedness dichotomy for `E`, and the OPEN §3b carrier (no instance).

`E` is a physical amplitude: the A=3 mass lift `r*` is a frame-free observable
(`A3AntiSelfAdjointLift.amplitude_injective` makes it a well-defined function of the even-face
factor), so whatever functional of the global Birkhoff matrix `P` supplies `E` must be
gauge-invariant.  By `entry_not_gauge_invariant` it cannot be a single entry of `P`; by
`crossRatio_gauge_invariant` + `gauge_fixes_all_iff` (unique invariant) it must be the cross-ratio.
We record that identification as an open §3b dependent conjecture with **no instance**. -/

/-- **§3b dependent conjecture — the amplitude `E` is the GAUGE-INVARIANT cross-ratio of the global
    Birkhoff matrix, not a single (frame-dependent) entry.**

    `@conjecture: dependent` (its content depends on the open construction of the global `0↔∞`
    Birkhoff connection matrix `P` of C1 — theta-valued, un-started;
    `docs/audits/2026-08-01-branch-selection-birkhoff-connection-matrix.md`, bean `qou-wiub`, the
    sibling's `BirkhoffAmplitudeE.lean`).

    The claim: the anti-self-adjoint amplitude `E` equals the **gauge-invariant** cross-ratio
    `crossRatio P₀₀ P₀₁ P₁₀ P₁₁` of the global Birkhoff matrix (frame-free, by
    `crossRatio_gauge_invariant`), and is nonzero (the bar-odd amplitude a genuine lift forces,
    `A3AntiSelfAdjointLift.amplitude_nonzero`).  This is the **well-posed** target: it is NOT any
    single entry (`entry_not_gauge_invariant`), and the cross-ratio is the unique invariant
    (`gauge_fixes_all_iff`).

    **Content-bearing, not self-assuming.**  `is_cross_ratio` ties `E` to a SPECIFIC frame-free
    functional of the (open) matrix `P` — a falsifiable identification the sibling's construction
    must satisfy, false for a generic assignment; `nonzero` is the forced bar-odd amplitude.  **No
    instance is supplied**: building `P` and evaluating its cross-ratio is the open successor;
    discharging this by *choosing* `crossRatio P` to hit `r*` (`amplitude_surjective`) would be the
    forbidden fit and is not done. -/
class AmplitudeIsGaugeInvariantCrossRatio {K : Type*} [Field K]
    (P00 P01 P10 P11 E : K) : Prop where
  /-- `E` is the frame-free cross-ratio of the global Birkhoff matrix — the gauge-invariant
      functional (`crossRatio_gauge_invariant`), not a single (gauge-dependent) entry. -/
  is_cross_ratio : E = crossRatio P00 P01 P10 P11
  /-- and it is the nonzero (bar-odd) amplitude a genuine A=3 lift forces
      (`A3AntiSelfAdjointLift.amplitude_nonzero`). -/
  nonzero : E ≠ 0

end QOU.QBeta.BirkhoffAmplitudeWellPosed
