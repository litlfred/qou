import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import QOU.BraidsAndKnots.ClosureUnseen

/-!
# QOU.FluidDynamics.helicity_conservation — categorical helicity conservation

The categorical helicity `ℋ_q` of a vortex configuration is conserved
under the quantum Euler equation (`dℋ_q/dt = 0`) and decomposes into
writhe, twist, and linking contributions, with the writhe and twist of
each filament obeying the Călugăreanu–White–Fuller relation
`Wr_q + Tw_q = Lk_q`.

LaTeX label: `prop:helicity-conservation`

## What the load-bearing claim is

The md states (1) conservation `dℋ_q/dt = 0`, (2) the three-way topological
decomposition `ℋ_q = writhe + twist + linking` with `Wr_q + Tw_q = Lk_q`,
(3) a Jones-polynomial refinement, and (4) the classical `q → 1` limit.

## 2026-08-31 — the decomposition is DERIVED; it used to be a class field

This file used to hold `HelicityContext`, a class carrying `Hq`, `writhe`,
`twist`, `linking`, `Wr`, `Tw`, `Lk` **and** the three claims as its own
fields, with `helicity_conservation`, `helicity_decomposition` and
`helicity_cwf_relation` each handing one field straight back.  Because the
data were fields rather than parameters, the instance chose them: `Hq := fun
_ => 0` and every scalar `0` satisfies all three fields, so a
`[HelicityContext]` binder assumed nothing and the three declarations
asserted nothing (AGENTS.md §3b-cond item 5; bean `qou-z9ws`).

The repair is not a demotion.  Reading the `.md`, the decomposition is a
**consequence**, not an axiom: `ℋ_q` is *defined* there as
`Σ_i ∮_{ϱ_i} v·ω ds + 2 Σ_{i<j} lk_q(ϱ_i,ϱ_j) Γ_i Γ_j`, and part (2) claims
the self-helicity term splits as writhe + twist.  Given the two standard
per-filament identities — Călugăreanu–White–Fuller `Wr_q + Tw_q = Lk_q` and
the Moffatt–Ricca self-helicity `∮ v·ω ds = Lk_q · Γ²` — the split follows
by summation, and *time-independence follows from the decomposition* rather
than being assumed alongside it.  So `helicity_conservation` below derives
**both** of its conjuncts from hypotheses about caller-supplied data, and
neither is a field of anything.

## What is still NOT encoded, stated rather than implied

- The two per-filament identities are **hypotheses**, not theorems here.
  CWF is classical (Călugăreanu 1961, White 1969, Fuller 1971) and its
  `q`-deformation is what the manuscript asserts; Moffatt–Ricca is the
  helicity/self-linking identity.  Neither is proved in this development.
- The hypothesis `hdef` — that `ℋ_q(t)` equals the same filament data at
  every `t` — is where the quantum Euler equation would enter.  That the
  flow preserves the linking numbers and quantised circulations is the
  physical content of md part (1) and is **not** established here.
- md part (3) (Jones-polynomial refinement) is encoded in the section `Closure` below
  (2026-11-16, issue #8133): `jones_normalised_conserved` (general isotopy, via Markov moves),
  `annular_class_conserved` / `closure_invariants_conserved` (fixed-axis case, conjugation only),
  and `reconnection_jump` (exact jump across a reconnection). The physical input — frozen-in
  vortex lines give an isotopy, and isotopy gives a Markov path — is cited, **not** proved here.
- md part (4) (the `q → 1` classical Moffatt limit) has **no encoding** in this file.

## References
- [leitner2026] §Fluid dynamics / Categorical helicity conservation,
  prop:helicity-conservation
-/

namespace QOU.FluidDynamics

/-- Helicity data of a single vortex filament `ϱ`: its `q`-deformed writhe,
twist and self-linking, its quantised circulation `Γ^{(q)} = [j]_q [j+1]_q`,
and its self-helicity `∮_ϱ v·ω ds`. -/
structure FilamentHelicity where
  /-- `q`-deformed writhe `Wr_q(ϱ)`. -/
  Wr : ℝ
  /-- `q`-deformed twist `Tw_q(ϱ)`. -/
  Tw : ℝ
  /-- `q`-deformed self-linking `Lk_q(ϱ)`. -/
  Lk : ℝ
  /-- Quantised circulation `Γ^{(q)} = [j]_q [j+1]_q` at intensity level `j`. -/
  Gamma : ℝ
  /-- Self-helicity `∮_ϱ v·ω ds` of this filament. -/
  selfHelicity : ℝ

/-- **Călugăreanu–White–Fuller relation** `Wr_q + Tw_q = Lk_q`, as a
proposition about one caller-supplied filament.  Classical for the
undeformed invariants; its `q`-deformation is asserted by the manuscript and
is **not** proved here. -/
-- Ref: [leitner2026] prop:helicity-conservation
def CWFHolds (f : FilamentHelicity) : Prop := f.Wr + f.Tw = f.Lk

/-- **Moffatt–Ricca self-helicity identity** `∮_ϱ v·ω ds = Lk_q(ϱ)·(Γ^{(q)})²`,
as a proposition about one caller-supplied filament.  Not proved here. -/
-- Ref: [leitner2026] prop:helicity-conservation
def SelfHelicityIsLinking (f : FilamentHelicity) : Prop :=
  f.selfHelicity = f.Lk * f.Gamma ^ 2

/-- The self-helicity term `Σ_i ∮_{ϱ_i} v·ω ds` of the md's definition of
`ℋ_q`. -/
def selfHelicitySum (fs : List FilamentHelicity) : ℝ :=
  (fs.map (fun f => f.selfHelicity)).sum

/-- The writhe term `Σ_i Wr_q(ϱ_i)·(Γ_i^{(q)})²` of md part (2). -/
def writheTerm (fs : List FilamentHelicity) : ℝ :=
  (fs.map (fun f => f.Wr * f.Gamma ^ 2)).sum

/-- The twist term `Σ_i Tw_q(ϱ_i)·(Γ_i^{(q)})²` of md part (2). -/
def twistTerm (fs : List FilamentHelicity) : ℝ :=
  (fs.map (fun f => f.Tw * f.Gamma ^ 2)).sum

/-- **`ℋ_q` is conserved**: constant in time, the integrated form of
`dℋ_q/dt = 0`.  Named here; establishing it for the quantum Euler flow is md
part (1) and is not done in this development. -/
def HelicityConserved (Hq : ℝ → ℝ) : Prop := ∀ t s, Hq t = Hq s

/-- **The writhe/twist split of the self-helicity term** (md part (2)).

Derived, not assumed: summing `∮ = Lk·Γ²` and `Wr + Tw = Lk` over the
filaments gives `Σ ∮ = Σ Wr·Γ² + Σ Tw·Γ²`.  Both inputs are hypotheses on
caller-supplied filaments; neither is a field of anything, and the
conclusion is neither. -/
-- Ref: [leitner2026] prop:helicity-conservation
theorem selfSum_eq_writhe_add_twist (fs : List FilamentHelicity)
    (hCWF : ∀ f ∈ fs, CWFHolds f)
    (hSelf : ∀ f ∈ fs, SelfHelicityIsLinking f) :
    selfHelicitySum fs = writheTerm fs + twistTerm fs := by
  induction fs with
  | nil => simp [selfHelicitySum, writheTerm, twistTerm]
  | cons f fs ih =>
      have hf1 : f.Wr + f.Tw = f.Lk := hCWF f (by simp)
      have hf2 : f.selfHelicity = f.Lk * f.Gamma ^ 2 := hSelf f (by simp)
      have ih' := ih (fun g hg => hCWF g (by simp [hg]))
        (fun g hg => hSelf g (by simp [hg]))
      simp only [selfHelicitySum, writheTerm, twistTerm, List.map_cons,
        List.sum_cons] at ih' ⊢
      rw [hf2, ih', ← hf1]
      ring

/-- **Categorical helicity conservation** ([`prop:helicity-conservation`]).

Let `ℋ_q(t)` be given at every time by the md's definition over a fixed
filament family `fs` and mutual-linking term `mutualLk` (hypothesis `hdef`),
and let each filament satisfy Călugăreanu–White–Fuller and the
Moffatt–Ricca self-helicity identity.  Then

* `ℋ_q` is **conserved** — md part (1); and
* `ℋ_q = writhe + twist + linking` at every time — md part (2).

**Both conjuncts are derived.**  Conservation is not a separate assumption:
it follows from `ℋ_q(t)` being equal, at every `t`, to one time-independent
expression.  The decomposition is `selfSum_eq_writhe_add_twist`.

What the hypotheses cost is stated in the module docstring: `hdef` is where
the quantum Euler equation would enter and is not established here, and the
two per-filament identities are cited rather than proved. -/
-- Ref: [leitner2026] prop:helicity-conservation
theorem helicity_conservation
    (Hq : ℝ → ℝ) (fs : List FilamentHelicity) (mutualLk : ℝ)
    (hdef : ∀ t, Hq t = selfHelicitySum fs + mutualLk)
    (hCWF : ∀ f ∈ fs, CWFHolds f)
    (hSelf : ∀ f ∈ fs, SelfHelicityIsLinking f) :
    HelicityConserved Hq ∧
      ∀ t, Hq t = writheTerm fs + twistTerm fs + mutualLk := by
  constructor
  · intro t s
    rw [hdef t, hdef s]
  · intro t
    rw [hdef t, selfSum_eq_writhe_add_twist fs hCWF hSelf]

/-- **Reeb-derived categorical linking magnitude.**
The sub-ceiling magnitude `g` extracted via the Reeb-flow helicity for a
2-strand `pn` bond obeys the eigenvalue bound `g < 1/√5`.

The `[HelicityContext]` binder this carried until 2026-08-31 was decorative —
the proof never used it, and the class it named is gone. -/
-- Ref: [leitner2026] docs/audits/2026-07-05-reeb-linking-operation-attack.md
theorem reeb_linking_magnitude_bound (q : ℝ) (hq : q > 1) :
    let g := 1 / Real.sqrt (5 + (q - 1) ^ 2 / q)
    g < 1 / Real.sqrt 5 := by
  intro g
  have hq_pos : q > 0 := by linarith
  have hq_sub : q - 1 > 0 := sub_pos.mpr hq
  have h_num : (q - 1) ^ 2 > 0 := by nlinarith
  have h_pos : (q - 1) ^ 2 / q > 0 := div_pos h_num hq_pos
  have h_denom : Real.sqrt (5 + (q - 1) ^ 2 / q) > Real.sqrt 5 := by
    apply Real.sqrt_lt_sqrt (by norm_num)
    linarith
  exact one_div_lt_one_div_of_lt (Real.sqrt_pos.mpr (by norm_num)) h_denom

section Closure

open QOU.BraidsAndKnots.ClosureUnseen

/-! ### md part (3): what is conserved, and under which hypothesis

The physical input, in its correct form (corrected 2026-11-16; the previous version assumed the
flow acts on the braid word by conjugation, which is too narrow):

1. A smooth ideal flow carries vortex lines with it (Helmholtz–Kelvin, `[moffatt1969]`), so the
   closed vortex link at time `t` is the image of the link at time `0` under the flow map: the two
   are **isotopic**.
2. By the Alexander and Markov theorems (`[alexander1923]`, `[markov1936]`, `[birman1974]`), two
   closed braids give isotopic links iff their words are joined by a path of **Markov moves**:
   conjugation, stabilisation `x ↦ x σₙ^{±1}`, and the inverses.

Step 1 is analytic and is not proved here; step 2 is classical topology and is not proved here
either. Given them, the algebra below is proved:

* `jones_normalised_conserved`: along any Markov path a Markov trace changes only by the recorded
  stabilisation factors, so the normalised trace (the Jones value) is conserved.
* `annular_class_conserved`: the finer annular class in `HH₀` (every sector separately) is
  conserved only when the path uses **conjugation alone**, i.e. when the tangle stays a closed
  braid on a fixed number of strands around a fixed axis.
* `reconnection_jump`: a reconnection flips one crossing, which breaks isotopy; the Jones value
  then jumps by exactly `h` times its value on the smoothed word. -/

section Generic

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- **Fixed-axis case.** If the flow acts on the tangle's word by conjugation,
`β (s+1) = g s * β s * (g s)⁻¹` — the tangle stays a closed braid on the same strands around a
fixed axis — then the class of `β s` in `HH₀(A) = A ⧸ [A, A]`, which keeps every sector character
separately, is the same at every time. -/
-- Ref: [leitner2026] prop:helicity-conservation; prop:closure-unseen-subword
theorem annular_class_conserved (β : ℕ → A) (g : ℕ → Aˣ)
    (hstep : ∀ s, β (s + 1) = (g s : A) * β s * (↑(g s)⁻¹ : A)) :
    ∀ s, univTrace (R := R) (β s) = univTrace (R := R) (β 0) :=
  trace_conserved_of_conj univTrace_isTrace β g hstep

/-- **Fixed-axis case: every closure invariant is conserved**, read off the conserved annular
class through `t = f ∘ univTrace` (`trace_factors`). -/
-- Ref: [leitner2026] prop:helicity-conservation; prop:closure-unseen-subword
theorem closure_invariants_conserved {M : Type*} [AddCommGroup M] [Module R M]
    {t : A →ₗ[R] M} (ht : IsTrace t) (β : ℕ → A) (g : ℕ → Aˣ)
    (hstep : ∀ s, β (s + 1) = (g s : A) * β s * (↑(g s)⁻¹ : A)) :
    ∀ s, t (β s) = t (β 0) := by
  intro s
  rw [trace_factors ht, LinearMap.comp_apply, LinearMap.comp_apply,
    annular_class_conserved (R := R) β g hstep s]

/-- **Reconnection jump.** A reconnection replaces one crossing `σ` by `σ⁻¹` inside the word
`u σ v`. With the skein relation `σ - σ⁻¹ = h` (`h = q - q⁻¹`), any closure invariant `t` jumps by
exactly `h` times its value on the smoothed word `u v`. -/
-- Ref: [leitner2026] prop:helicity-conservation; prop:closure-unseen-subword
theorem reconnection_jump {M : Type*} [AddCommGroup M] [Module R M] (t : A →ₗ[R] M)
    (σ : Aˣ) (h : R) (hskein : (σ : A) - (↑σ⁻¹ : A) = algebraMap R A h) (u v : A) :
    t (u * (↑σ⁻¹ : A) * v) = t (u * σ * v) - h • t (u * v) := by
  rw [← crossing_change_jump t σ h hskein u v, sub_sub_cancel]

end Generic

section Isotopy

variable {R : Type*} [Field R] {A : ℕ → Type*} [∀ n, Ring (A n)] [∀ n, Algebra R (A n)]
  {T : BraidTower (R := R) A} (M : MarkovTraceOn T)

/-- **General case: the normalised Jones value is conserved under isotopy.** Let the tangle's
braid words `p 0, p 1, …` be joined by Markov moves and their inverses (what isotopy of the closed
vortex link gives, by Markov's theorem), with recorded factors `e k`, none zero. Then the Markov
trace divided by the accumulated factor is the same at every time. -/
-- Ref: [leitner2026] prop:helicity-conservation; [markov1936]; [birman1974]
theorem jones_normalised_conserved (p : ℕ → Σ n, A n) (e : ℕ → R)
    (hstep : ∀ k, PathStep M (p k) (p (k + 1)) (e k)) (he : ∀ k, e k ≠ 0) :
    ∀ k, (∏ i ∈ Finset.range k, e i)⁻¹ * M.val (p k) = M.val (p 0) := by
  intro k
  rw [val_along_path M p e hstep k, ← mul_assoc,
    inv_mul_cancel₀ (Finset.prod_ne_zero_iff.2 (fun i _ => he i)), one_mul]

end Isotopy

end Closure

end QOU.FluidDynamics
