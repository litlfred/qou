import Mathlib.Tactic

/-!
# QOU.MassTheory.TransverseSurfaceCurvature

**Formalize-first (forward, geometric) structure of the transverse
non-abelian-Stokes surface-curvature** — the named surviving carrier of the
deuteron binding *magnitude* after braid-word, scale, level, edge, and
DT-count are all excluded (bean `qou-prjo`;
[`docs/audits/2026-07-24-eunit-magnus-order2.md` §2](../../../../../../docs/audits/2026-07-24-eunit-magnus-order2.md),
[`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md` §4](../../../../../../docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md)).

## What this file IS (and is NOT)

The order-2 Magnus term of the surface-ordered exponential is the transverse
surface-curvature pairing
`Ω₂ = ½ P ∮∮ [𝓕, 𝓕]`, quadratic in the germ commutator q-curvature
`F_q = [δq₁, δq₂]`
([`germ-commutator-q-curvature.md`](../../../quantum-observable-universes/germ-commutator-q-curvature.md)),
where `𝓕(x) = U(x,O)⁻¹ F_q U(x,O)` is the *path-dependent* (parallel-
transported) curvature. It lives **transverse** to the strand ordering — the
two-observer-parallelogram direction — so it survives even on the
single-generator deuteron channel `σ₁³` where every *inter-crossing* (path)
Magnus commutator vanishes identically (`[a,a]=0`; audit §2).

This file formalises, **sorry-free and forward**, the *algebraic structure*
of that transverse pairing plus the *Seifert-surface combinatorics* it is
carried on. It does **NOT** derive the deuteron magnitude:

> **sorry-free ≠ derived; axiomatising the curvature is NOT deriving its
> magnitude** (AGENTS.md). The numerical magnitude requires the actual
> position-dependent transport `U(x,O)` across the Seifert surface — the
> "canonical discretisation of the Yekutieli surface 2-form" that bean
> `qou-prjo` names as the missing corpus data. The **wall** is formalised
> below (`transverse_nonzero_needs_noncommuting_curvature`): a nonzero
> transverse magnitude *forces* the local curvatures to differ across the
> surface, i.e. requires exactly that transport-twist data.

No `q₀`, no AME target, zero free parameters, nothing inverted.

## References
- Ref: [yekutieli2015] https://doi.org/10.1142/9537 — non-abelian
  multiplicative integration and Stokes on surfaces.
- Ref: [leitner2026] germ-commutator-q-curvature (`F_q = [δq₁, δq₂]`).
- Companion discrete-holonomy (boundary / 1-form) layer:
  `QOU.MathlibExt.YekutieliIntegration`.

**Base ring (§7c).** Part B is purely algebraic — a generic non-commutative
`Ring R` (the curvature bracket `a*b - b*a`); no `ℝ`, no ordering. Part A is
`ℤ` combinatorics (Seifert Betti numbers). Only the scalar *magnitude* wrapper
in Part C carries a real `κ² = ‖F_q‖²` (a genuine archimedean norm).
-/

namespace QOU.MassTheory.TransverseSurfaceCurvature

/-! ## Part A — Seifert-surface combinatorics of a braid diagram

Seifert's algorithm on a connected positive-braid diagram `β` on `s` strands
with `c` crossing letters gives a spanning surface `Σ` with `s` Seifert disks
(2-cells) glued by `c` twisted bands (1-cells).  Its Euler characteristic is
`χ(Σ) = s − c`, so the first Betti number (twice the genus, for a one-boundary
knot surface) is `b₁(Σ) = 1 − χ = c − s + 1 = 2g`.  This integer counts the
independent transverse 2-cycles (handles) available to carry surface
curvature. -/

/-- First Betti number `b₁ = c − s + 1 = 2g` of the Seifert surface of a
    connected `s`-strand, `c`-crossing braid diagram. -/
def seifertBettiOne (strands crossings : ℤ) : ℤ := crossings - strands + 1

/-- **Deuteron / trefoil.**  The pn channel word `σ₁³` is `s = 2`, `c = 3`, so
    `b₁ = 2` (genus one).  A concrete, falsifiable value — not a definition. -/
theorem seifertBettiOne_trefoil : seifertBettiOne 2 3 = 2 := by
  unfold seifertBettiOne; norm_num

/-- **Unknot / disk (planar, genus 0) has `b₁ = 0`.**  For `c = s − 1` (a tree
    of bands) the surface is a disk — no transverse handle.  E.g. `s = 2`,
    `c = 1`. -/
theorem seifertBettiOne_disk : seifertBettiOne 2 1 = 0 := by
  unfold seifertBettiOne; norm_num

/-- **Link-additivity (the pairwise cap).**  Adding `k` crossings to a fixed
    strand set (one inter-nucleon link, *no* new strands) increments `b₁` by
    **exactly** `k`.  Hence the Betti/diagonal transverse magnitude is
    *exactly linear* in the number of inter-nucleon links — additive,
    never super-additive.  This is the structural reason the Betti-count
    reading **cannot** be the ≥3-body super-pairwise term the corpus proves
    is required (`deltalambda…additive-term.md` §4): a genuinely 3-body
    enhancement must come from the *off-diagonal* cross-handle pairing
    (Part B), not from `b₁`. -/
theorem seifertBettiOne_link_additive (s c k : ℤ) :
    seifertBettiOne s (c + k) = seifertBettiOne s c + k := by
  unfold seifertBettiOne; ring

/-- **Extensivity.**  With the framework strand count `s = 3A` (each nucleon a
    3-strand Borromean baryon) and crossing density `ρ` per nucleon
    (`c = ρ·A`), the Betti number is `b₁ = (ρ − 3)·A + 1` — **extensive**
    (grows with `A`) precisely when `ρ > 3`, i.e. when the crossing density
    exceeds the strand density.  This is the forward geometric statement that
    the transverse surface curvature *can* carry an `∝ A` (extensive) binding
    term — the shape the corpus's missing additive term must have. -/
theorem seifertBettiOne_extensive (A rho : ℤ) :
    seifertBettiOne (3 * A) (rho * A) = (rho - 3) * A + 1 := by
  unfold seifertBettiOne; ring

/-! ## Part B — the transverse (surface-ordered) curvature pairing

Discretise the Seifert surface into 2-cells `x₀, x₁, …` in surface order, and
record at each cell the *parallel-transported* germ curvature
`𝓕ᵢ = U(xᵢ,O)⁻¹ F_q U(xᵢ,O) ∈ R` (an element of the Hecke-image ring `R`).
The order-2 Magnus / transverse term `½ P ∮∮ [𝓕,𝓕]` discretises to the
**ordered** double sum over cell pairs `(later, earlier)` of the curvature
commutator.  We work over a generic (non-commutative) `Ring R`. -/

variable {R : Type*} [Ring R]

/-- Curvature commutator `⟦a,b⟧ = a·b − b·a` — the discrete `[𝓕,𝓕]` integrand. -/
def curvComm (a b : R) : R := a * b - b * a

@[simp] theorem curvComm_self (a : R) : curvComm a a = 0 := by
  simp only [curvComm, sub_self]

/-- The germ curvature is a genuine antisymmetric 2-form: swapping the two
    observers negates it (`germ-commutator-q-curvature.md` consequence 2).
    `R` is a generic (possibly non-commutative) ring, so `noncomm_ring`
    rather than `ring`. -/
theorem curvComm_antisymm (a b : R) : curvComm a b = - curvComm b a := by
  rw [curvComm, curvComm, neg_sub]

/-- Row contribution: the ordered commutators of every *later* cell curvature
    `y ∈ ys` with a fixed *earlier* one `c`. -/
def rowPairing (c : R) : List R → R
  | [] => 0
  | (y :: ys) => curvComm y c + rowPairing c ys

/-- **Transverse surface-curvature pairing** (discrete `½ P ∮∮ [𝓕,𝓕]`).
    Ordered double sum over the surface cells: each earlier cell `c` paired
    with all later cells, then recurse.  Argument is the list of transported
    local curvatures `[𝓕₀, 𝓕₁, …]` in surface order. -/
def listPairing : List R → R
  | [] => 0
  | (c :: xs) => rowPairing c xs + listPairing xs

@[simp] theorem listPairing_nil : listPairing ([] : List R) = 0 := rfl

@[simp] theorem listPairing_singleton (a : R) : listPairing [a] = 0 := by
  simp [listPairing, rowPairing]

/-- Two cells: the pairing is the single ordered commutator `⟦𝓕₁, 𝓕₀⟧`
    (later with earlier) — manifestly nonzero for non-commuting curvatures,
    so the transverse object is **not vacuously zero**. -/
theorem listPairing_pair (a b : R) : listPairing [a, b] = curvComm b a := by
  simp [listPairing, rowPairing]

/-- If every later curvature commutes with the fixed earlier one, that row
    vanishes. -/
theorem rowPairing_eq_zero (c : R) (l : List R)
    (h : ∀ y ∈ l, curvComm y c = 0) : rowPairing c l = 0 := by
  induction l with
  | nil => rfl
  | cons y ys ih =>
    rw [rowPairing, h y (by simp), ih (fun z hz => h z (by simp [hz])), add_zero]

/-- **Flat / commuting surface ⇒ transverse curvature vanishes.**  If all pairs
    of local curvatures commute (`⟦𝓕ᵢ, 𝓕ⱼ⟧ = 0`) — in particular the
    *flat-transport* case where every `𝓕ᵢ` equals a common `F_q` — the whole
    transverse pairing is zero.  This is the discrete form of the germ-curvature
    dichotomy "agreement ⟺ flatness". -/
theorem listPairing_eq_zero_of_all_comm (l : List R)
    (h : ∀ x ∈ l, ∀ y ∈ l, curvComm x y = 0) : listPairing l = 0 := by
  induction l with
  | nil => rfl
  | cons c xs ih =>
    have hrow : rowPairing c xs = 0 :=
      rowPairing_eq_zero c xs (fun y hy => h y (by simp [hy]) c (by simp))
    have htail : listPairing xs = 0 :=
      ih (fun x hx y hy => h x (by simp [hx]) y (by simp [hy]))
    rw [listPairing, hrow, htail, add_zero]

/-- **Uniform (flat-transport) curvature ⇒ vanishes.**  The special case where
    every cell carries the *same* curvature `c` (trivial transport, no handle
    twist): the transverse pairing is `0`.  A nonzero transverse surface
    curvature therefore cannot arise from a flat surface. -/
theorem listPairing_const (c : R) (l : List R) (h : ∀ y ∈ l, y = c) :
    listPairing l = 0 := by
  apply listPairing_eq_zero_of_all_comm
  intro x hx y hy
  rw [h x hx, h y hy, curvComm_self]

/-- **THE WALL (formalised).**  A *nonzero* transverse surface curvature
    **forces** two cells whose transported curvatures do not commute.  Since
    the germ curvature `F_q` is a single universal substrate element, distinct
    non-commuting `𝓕ᵢ = U(xᵢ)⁻¹ F_q U(xᵢ)` can only arise from *position-
    dependent transport* `U(xᵢ)` across the surface — exactly the canonical
    Yekutieli surface-2-form discretisation that the corpus lacks (bean
    `qou-prjo`).  So the transverse magnitude is unpinned without that data:
    this theorem is the precise statement of why the route is walled, not a
    derivation of the magnitude. -/
theorem transverse_nonzero_needs_noncommuting_curvature (l : List R)
    (h : listPairing l ≠ 0) :
    ∃ x ∈ l, ∃ y ∈ l, curvComm x y ≠ 0 := by
  by_contra hc
  push_neg at hc
  exact h (listPairing_eq_zero_of_all_comm l (fun x hx y hy => hc x hx y hy))

/-! ### Trace/character annihilation — the transverse term is invisible to the
    scalar Markov trace

Any *cyclic* linear functional `τ` (`τ(a·b)=τ(b·a)` — the Markov trace / a
Wedderburn block character `χ^λ`) annihilates every curvature commutator, hence
the whole transverse pairing.  This is the formal reason the transverse
surface curvature **cannot** contribute to binding through the *scalar* trace
channel (why the scalar-trace binding `B = E₀·Δtr_M` saturates); any surviving
contribution must be **operator-valued** (eigenphase-weighted / non-trace) —
the channel independently named in the sibling probes #4619 and
[`2026-07-24-eunit-magnus-order2.md` §2](../../../../../../docs/audits/2026-07-24-eunit-magnus-order2.md). -/

/-- A cyclic linear functional kills the curvature commutator. -/
theorem curvComm_trace_zero {A : Type*} [AddCommGroup A] (τ : R →+ A)
    (hcyc : ∀ a b : R, τ (a * b) = τ (b * a)) (a b : R) :
    τ (curvComm a b) = 0 := by
  rw [curvComm, map_sub, hcyc a b, sub_self]

theorem rowPairing_trace_zero {A : Type*} [AddCommGroup A] (τ : R →+ A)
    (hcyc : ∀ a b : R, τ (a * b) = τ (b * a)) (c : R) (l : List R) :
    τ (rowPairing c l) = 0 := by
  induction l with
  | nil => simp [rowPairing]
  | cons y ys ih =>
    rw [rowPairing, map_add, curvComm_trace_zero τ hcyc, ih, add_zero]

/-- **The whole transverse pairing has vanishing trace/character.**  Under any
    cyclic functional (Markov trace, block character `χ^λ`) the ordered
    transverse pairing evaluates to `0`.  So the transverse surface curvature is
    a purely *operator-valued* object; it leaves no imprint on the scalar Jones/
    Markov trace. -/
theorem listPairing_trace_zero {A : Type*} [AddCommGroup A] (τ : R →+ A)
    (hcyc : ∀ a b : R, τ (a * b) = τ (b * a)) (l : List R) :
    τ (listPairing l) = 0 := by
  induction l with
  | nil => simp [listPairing]
  | cons c xs ih =>
    rw [listPairing, map_add, rowPairing_trace_zero τ hcyc, ih, add_zero]

/-! ## Part C — scalar magnitude envelope (diagonal / additive reading)

The *diagonal* (per-handle) envelope of the transverse magnitude assigns one
unit `κ² = ‖F_q‖²` per independent handle, i.e. `½ · b₁ · κ²`.  This is the
**additive** reading; by `seifertBettiOne_link_additive` it is exactly linear
in the crossing count, hence pairwise-capped and unable to supply the ≥3-body
enhancement.  The genuine (off-diagonal) content is `listPairing` (Part B),
which needs the transport data.  This wrapper exists only to state the additive
envelope explicitly and its trefoil/flat values. -/

/-- Diagonal transverse-magnitude envelope `½ · b₁ · κ²`, `κ² = ‖F_q‖²`. -/
noncomputable def transverseMagnitudeDiagonal (bettiOne : ℤ) (kappaSq : ℝ) : ℝ :=
  (1 / 2) * (bettiOne : ℝ) * kappaSq

/-- Deuteron diagonal envelope is exactly `κ²` (`b₁ = 2`, `½·2·κ² = κ²`). -/
theorem transverseMagnitudeDiagonal_trefoil (kappaSq : ℝ) :
    transverseMagnitudeDiagonal (seifertBettiOne 2 3) kappaSq = kappaSq := by
  rw [seifertBettiOne_trefoil]
  unfold transverseMagnitudeDiagonal
  push_cast; ring

/-- **Flat curvature (`F_q = 0 ⇒ κ² = 0`) ⇒ zero magnitude** — bosonic /
    q-flat / cocommutative case. -/
@[simp] theorem transverseMagnitudeDiagonal_flat (b : ℤ) :
    transverseMagnitudeDiagonal b 0 = 0 := by
  unfold transverseMagnitudeDiagonal; ring

/-- The diagonal envelope inherits exact link-additivity from `b₁`: adding one
    inter-nucleon link (`k` crossings) adds exactly `½ · k · κ²`, independent of
    `A`.  Formal witness that the diagonal reading is additive (pairwise), not
    super-pairwise. -/
theorem transverseMagnitudeDiagonal_link_additive (s c k : ℤ) (kappaSq : ℝ) :
    transverseMagnitudeDiagonal (seifertBettiOne s (c + k)) kappaSq
      = transverseMagnitudeDiagonal (seifertBettiOne s c) kappaSq
        + transverseMagnitudeDiagonal k kappaSq := by
  rw [seifertBettiOne_link_additive]
  unfold transverseMagnitudeDiagonal
  push_cast; ring

end QOU.MassTheory.TransverseSurfaceCurvature
