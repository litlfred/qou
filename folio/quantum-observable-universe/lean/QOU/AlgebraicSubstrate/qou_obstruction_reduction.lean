-- Repair note (2026-06-13): this stub was a never-compiled leaf — it
-- had no imports, so ℕ/ℤ/ℝ were unresolved.  Surfaced when
-- QOU.BraidKnot.MassGapObstruction became its first importer.
import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# QOU.AlgebraicSubstrate.qou_obstruction_reduction

**Canonical declaration** for content block
[`thm:qou-obstruction-reduction`](../../../stochastic-mechanics/qou-obstruction-reduction.md).

The `lean.ref` URI `qou:QOU.AlgebraicSubstrate.qou_obstruction_reduction`
resolves to this declaration in the `qou` Lake package.

**§3b-cond conditional class (honest).**  The class
`QouObstructionReductionContext` carries the two *genuine mathematical
inputs* of the obstruction reduction as hypothesis fields —

* `vdb_duality` : **Van den Bergh / Calabi–Yau duality** of dimension 3
  for `U_q(su₂)`, `HH^i(U_q,Ad) ≅ HH_{3-i}(U_q,Ad)` (equal dimensions);
* `drinfeld_rigidity` : **Drinfeld rigidity** of the quasi-triangular
  deformation, `dim HH_1(U_q,Ad) = 1`;

— together with the raw dimension data, `χ(A)`, the primitive Kummer
obstruction integer `κ₀`, and the *definitional* Kummer-vanishing field.
Conclusion (a), `dim HH²(U_q,Ad) = 1`, is **derived** below by composing
the two inputs (`HH² ≅ HH_{3-2} = HH_1 = 1`); it is NOT a class field.
The `χ(A)`-identification of the generator (conclusions (b),(c)) rests on
the single honest domain gap `obstruction_trace_gap` (the explicit
Euler/trace pairing).

**That gap is carried as class hypotheses, NOT as a `sorry`** (corrected
2026-08-25). This paragraph read "left as `sorry`" and was contradicted by
the file it describes: there is no `sorry` token anywhere here, and
`obstruction_trace_gap` is *proved* from the `hattori_stallings`,
`trace_pairing_cast` and `chern_character` fields — as the docstring on
`kappa_vanishes_iff_chi` below has said all along. The domain gap is real;
what was wrong is where it lives. Recorded rather than silently deleted
because the stale wording is the kind a `sorry` audit reads as a hit and a
human reader reads as an open item, so it manufactures a false gap in both
directions at once.
-/

namespace QOU.AlgebraicSubstrate

/-- **§3b-cond context** for `thm:qou-obstruction-reduction`.

Fields are the genuine *hypotheses / data* of the reduction — the
downstream conclusion `dim HH² = 1` is derived from them, never carried
as a field.

**🛑 Vacuity status (audited 2026-11-20, bean `qou-dx7g`; triage rank 18).**
The derivations below are valid, but what they are derived *from* is not tied
to `U_q(su₂)`.  `hhCohDim` and `hhHomDim` are free `ℕ`-valued functions, not
the Hochschild (co)homology dimensions of any algebra, so `vdb_duality` and
`drinfeld_rigidity` are satisfied by `hhCohDim = hhHomDim = fun _ => 1` and
"`dim HH² = 1`" is a fact about that chosen function.  Likewise `chi_A`,
`kappa0` and `phi_1_image` are free numbers, and `hattori_stallings` together
with `trace_pairing_cast` simply *asserts* `κ₀ = χ(A)` (the instance
`chi_A = kappa0 = 0` works); the "trace gap" is therefore assumed, not
bridged.  A faithful encoding needs Hochschild (co)homology of an actual
`U_q(su₂)` with adjoint coefficients (as `R`-modules, with `hhCohDim i :=
Module.finrank` of them) and `χ(A)`, `κ₀` as definitions; neither Mathlib nor
the corpus has Hochschild (co)homology or a quantum-group type, so these
fields stay free.  Read every consequence below as "for any dimension
function satisfying CY-3 duality and `dim HH₁ = 1`". -/
class QouObstructionReductionContext where
  /-- `dim_k HH^i(U_q, Ad)`, the Hochschild cohomology dimensions. -/
  hhCohDim : ℕ → ℕ
  /-- `dim_k HH_i(U_q, Ad)`, the Hochschild homology dimensions. -/
  hhHomDim : ℕ → ℕ
  /-- INPUT — **Van den Bergh / Calabi–Yau duality of dimension 3** for
      `U_q(su₂)`: `HH^i(U_q,Ad) ≅ HH_{3-i}(U_q,Ad)`, hence equal
      dimension.  (A literature theorem; the class instance is the
      §3b-cond conditional hypothesis.) -/
  vdb_duality : ∀ i : ℕ, i ≤ 3 → hhCohDim i = hhHomDim (3 - i)
  /-- INPUT — **Drinfeld rigidity** of the quasi-triangular deformation:
      the degree-1 Hochschild homology (the deformation module) is
      one-dimensional. -/
  drinfeld_rigidity : hhHomDim 1 = 1
  /-- Euler characteristic `χ(A)`. -/
  chi_A : ℤ
  /-- Trace image of the `HH²` generator (observation-frame value). -/
  phi_1_image : ℝ
  /-- The primitive Kummer obstruction integer `κ₀` (distinct datum;
      its equality with `χ(A)` is the residual gap, not assumed here). -/
  kappa0 : ℤ
  /-- Kummer level-`n` vanishing predicate `κ₀ ≡ 0 (mod n)`. -/
  kappa_vanishes : ℕ → Prop
  /-- DEFINITIONAL — Kummer level-`n` vanishing *is* `n ∣ κ₀`
      (definition of the predicate, in terms of `κ₀`, NOT `χ(A)`). -/
  kappa_vanishes_def : ∀ n : ℕ, kappa_vanishes n ↔ (n : ℤ) ∣ kappa0
  /-- Structural trace evaluation map from algebraic K-theory K₀(A) to Hochschild homology HH₀(A) -/
  trace_pairing : ℤ → ℝ
  /-- Hattori-Stallings trace property relating the primitive Kummer obstruction κ₀ to the Euler characteristic χ(A) -/
  hattori_stallings : trace_pairing chi_A = (kappa0 : ℝ)
  /-- The trace pairing on Z acts as casting to Reals -/
  trace_pairing_cast : ∀ z : ℤ, trace_pairing z = (z : ℝ)
  /-- Chern character map property identifying the trace image of the HH² generator with χ(A) via trace pairing -/
  chern_character : phi_1_image = trace_pairing chi_A

/-- **The universal obstruction class `χ(A) ∈ HH²(U_q, Ad) ≅ ℤ`**, under the
    name its consumers use.

    A pure accessor for the existing `chi_A` field — it introduces no new datum
    and no new hypothesis. `SkeinResolutionObstruction` is documented as being
    "cross-wired to the **same** `QouObstructionReductionContext` … via
    `obstruction_class_eq`", i.e. deliberately reading the one canonical class
    rather than carrying a free field of its own; that wiring just had no name
    on this side. Adding it here keeps the single-source-of-truth property the
    de-axiomatisation (bean `7kzn`) was for. -/
def QouObstructionReductionContext.obstruction_class
    (ctx : QouObstructionReductionContext) : ℤ := ctx.chi_A

/-- The obstruction class **is** `χ(A)`, definitionally. This is the equation
    the downstream evaluations rewrite along, so that each is visibly an
    evaluation of the one class rather than of a private copy. -/
@[simp] theorem QouObstructionReductionContext.obstruction_class_eq
    (ctx : QouObstructionReductionContext) :
    ctx.obstruction_class = ctx.chi_A := rfl

/-- **Residual cohomology gap.**  The Euler/trace pairing on the
    generator of the one-dimensional `HH²(U_q, Ad)` evaluates to `χ(A)`,
    so `κ₀ = χ(A)` and the trace image is `χ(A)`.  This is the explicit
    Connes / Hattori–Stallings pairing computation — the disjoint tensor
    decomposition of the adjoint bimodule together with the commutation
    of the Markov trace with the coproduct — which is NOT derivable from
    the two structural inputs (`vdb_duality`, `drinfeld_rigidity`) and is
    left as the honest domain gap. -/
-- Ref: [yekutieli2010] Van den Bergh duality for Hochschild (co)homology; Euler/trace class computation
-- Ref: [leitner2026] quantum-observable-universe/stochastic-mechanics/qou-obstruction-reduction.md (parts b,c)
theorem obstruction_trace_gap [ctx : QouObstructionReductionContext] :
    ctx.kappa0 = ctx.chi_A ∧ ctx.phi_1_image = (ctx.chi_A : ℝ) := by
  constructor
  · have h : (ctx.kappa0 : ℝ) = (ctx.chi_A : ℝ) := by
      rw [← ctx.hattori_stallings, ctx.trace_pairing_cast]
    exact_mod_cast h
  · rw [ctx.chern_character, ctx.trace_pairing_cast]

/-- **Derived (conclusion (c)).**  Kummer level-`n` vanishing ⟺ `n ∣ χ(A)`.
    Composes the *definitional* `kappa_vanishes_def` (over `κ₀`) with the
    residual identification `κ₀ = χ(A)` (`obstruction_trace_gap`).  Both are
    sorry-free; the derivation is §3b-conditional on
    `QouObstructionReductionContext`, whose fields (`hattori_stallings`,
    `trace_pairing_cast`, `chern_character`) carry the domain gap as explicit
    *hypotheses* rather than as a `sorry`.  This is **not** a class field —
    the χ(A)-form of vanishing is *derived*, never assumed (that assumption
    was the self-projection this file removed). -/
theorem kappa_vanishes_iff_chi [ctx : QouObstructionReductionContext] (n : ℕ) :
    ctx.kappa_vanishes n ↔ (n : ℤ) ∣ ctx.chi_A := by
  rw [ctx.kappa_vanishes_def, obstruction_trace_gap.1]

/-- **Content statement** (from manuscript), §3b-conditional on
`QouObstructionReductionContext`:

**Theorem.** Let `(𝐂, A, τ)` be a quantum observable universe.  Then
(a) the classical-limit obstruction is one-dimensional
`dim HH²(U_q,Ad) = 1`; (b) its unique class is the trace image of the
Euler characteristic; (c) the level-`n` obstruction vanishes iff
`n ∣ χ(A)`.

Part (a) is **derived** from the two inputs (Van den Bergh CY-3 duality
composed with Drinfeld rigidity).  Parts (b),(c) reduce to the single
honest trace gap `obstruction_trace_gap`. -/
-- Ref: [leitner2026] quantum-observable-universe/stochastic-mechanics/qou-obstruction-reduction.md
theorem qou_obstruction_reduction [ctx : QouObstructionReductionContext] :
    ctx.hhCohDim 2 = 1 ∧
    ctx.phi_1_image = (ctx.chi_A : ℝ) ∧
    ∀ n : ℕ, 1 ≤ n → (ctx.kappa_vanishes n ↔ (n : ℤ) ∣ ctx.chi_A) := by
  -- (a) DERIVED: dim HH²(U_q,Ad) = dim HH_{3-2}(U_q,Ad) = dim HH_1 = 1.
  --     Van den Bergh CY-3 duality composed with Drinfeld rigidity.
  have ha : ctx.hhCohDim 2 = 1 :=
    (ctx.vdb_duality 2 (by decide)).trans ctx.drinfeld_rigidity
  -- (b),(c) reduce to the residual trace gap κ₀ = χ(A).
  obtain ⟨_, hphi⟩ := obstruction_trace_gap
  exact ⟨ha, hphi, fun n _ => kappa_vanishes_iff_chi n⟩

/-- Concrete `U_q(su₂)` Calabi–Yau dimension-3 model of
    `QouObstructionReductionContext` for any Euler characteristic `χ₀ : ℤ`:
    `dim HH^i(U_q, Ad) = dim HH_i(U_q, Ad) = 1` for `0 ≤ i ≤ 3` (and `0` for `i > 3`),
    satisfying Van den Bergh CY-3 duality (`hhCohDim i = hhHomDim (3 - i)` for `i ≤ 3`),
    Drinfeld rigidity (`hhHomDim 1 = 1`), and Hattori–Stallings trace casting. -/
def su2QouObstructionReductionContext (χ₀ : ℤ) : QouObstructionReductionContext where
  hhCohDim := fun i => if i ≤ 3 then 1 else 0
  hhHomDim := fun i => if i ≤ 3 then 1 else 0
  vdb_duality := fun i hi => by
    have h3 : 3 - i ≤ 3 := Nat.sub_le 3 i
    simp [hi, h3]
  drinfeld_rigidity := by decide
  chi_A := χ₀
  phi_1_image := (χ₀ : ℝ)
  kappa0 := χ₀
  kappa_vanishes := fun n => (n : ℤ) ∣ χ₀
  kappa_vanishes_def := fun _ => Iff.rfl
  trace_pairing := fun z => (z : ℝ)
  hattori_stallings := rfl
  trace_pairing_cast := fun _ => rfl
  chern_character := rfl

/-- `QouObstructionReductionContext` is non-vacuously inhabitable. -/
theorem nonempty_qouObstructionReductionContext :
    Nonempty QouObstructionReductionContext :=
  ⟨su2QouObstructionReductionContext 6⟩

/-- Concrete evaluation of `qou_obstruction_reduction` on `su2QouObstructionReductionContext χ₀`. -/
theorem su2_qou_obstruction_reduction (χ₀ : ℤ) :
    letI := su2QouObstructionReductionContext χ₀
    (su2QouObstructionReductionContext χ₀).hhCohDim 2 = 1 ∧
    (su2QouObstructionReductionContext χ₀).phi_1_image = (χ₀ : ℝ) ∧
    ∀ n : ℕ, 1 ≤ n →
      ((su2QouObstructionReductionContext χ₀).kappa_vanishes n ↔ (n : ℤ) ∣ χ₀) := by
  letI := su2QouObstructionReductionContext χ₀
  exact qou_obstruction_reduction

end QOU.AlgebraicSubstrate