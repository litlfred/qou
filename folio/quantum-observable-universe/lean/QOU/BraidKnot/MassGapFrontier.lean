import QOU.BraidKnot.MassGapObstruction
import QOU.BraidKnot.CrossingGradedModel

/-!
# QOU.BraidKnot.MassGapFrontier — the two research gaps, narrowed to typed form

After S1a/S1b/Step-2/Step-3-arm/S1c-constructive (all merged), the
mass-gap three-step program has exactly two research-grade residues.
This module narrows each from a prose hypothesis to a **typed,
machine-checkable interface with a verified consuming pipeline**, so
that discharging either becomes a matter of constructing one instance
— with the precise field signature pinned in Lean rather than in
prose.

## Gap 1 — S1c physical spectral hypothesis, narrowed three ways

The open statement: *every non-vacuum excitation of the physical
`𝒯_q` on `End(Aₙ)` carries at least one crossing's energy.*

1. **Spectral anchor (proved, sorry-free).** The per-crossing energy
   `E_×(q)` is not an ad-hoc constant: it is the **mean of the two
   Hecke crossing eigenvalues** `{q, −q⁻¹}`
   (`crossingEnergy_eq_eigenvalue_mean`), and the eigenvalue
   separation is `[2]_q = q + q⁻¹`
   (`crossing_eigenvalue_separation`).  This anchors the filtration
   hypothesis in the categorical source of `q` (the per-crossing
   weights of `def:crossing-energy` are the eigenvalues of the
   braiding `T` on `S²V ⊕ Λ²V`).

2. **Induction decomposition (proved, sorry-free).** Strategy (i)
   of the workplan — Wenzl/Jones-tower positivity transport — has
   the shape *base case + transport step*.
   `crossingFiltration_of_base_and_transport` proves: filtration at
   the tower base + a `TowerTransport` instance (the inclusion
   `H_n ⊂ H_{n+1}` preserves the per-crossing bound) ⟹ the full
   `CrossingFiltration`.  The universally-quantified hypothesis is
   thereby replaced by two strictly smaller named ones.

3. **What remains** is constructing `FiltrationBase` + `TowerTransport`
   for the physical tower.  **Honest scope note (the base case is NOT a
   near-term `native_decide` win):** the per-crossing Hecke spectrum is
   the *signed* pair `{q, −q⁻¹}`, and for `1 < q` the antisymmetric
   eigenvalue is negative — `−q⁻¹ ∈ (−1, 0) < 0 < E_×(q)`.  The Lean
   `CategoricalTransferMatrix.eigenvalues`, by contrast, is a
   *non-negative, monotone, vacuum-0 energy* spectrum (its structure
   axioms), so the physical energy spectrum is **not** the raw signed
   Hecke spectrum: an energy functional
   `E : (signed Hecke / vertex-volume) → ℝ≥0` sits in between, and
   `FiltrationBase` is a claim about *that* spectrum.  The finite-rank
   check (H₂/H₃) is well-posed only after that functional is fixed —
   and fixing it is itself open content (the crossing-graded model in
   `CrossingGradedModel` sidesteps it by *postulating* `energy = k·E_×`).
   The transport step is where the Wenzl conditional-expectation
   positivity argument lives.

## Gap 2 — Step-3 universality, narrowed to an interface class

The open statement: *any axiomatized Yang–Mills theory with a gap
yields a QOU-type structure* (the Millennium-relevance gate; the
workplan notes it "does not exist").

`AxiomatizedYMWithGap` pins the *minimal* abstract data the transfer
corollary needs (an excitation spectrum and a uniform positive gap —
deliberately free of any QOU-specific structure), and `YMUniversality`
is the gate itself: a map from such theories into obstruction-
reduction contexts with `χ(A) = −6`.  The corollary
`universality_transfers_obstruction` (proved, sorry-free) shows
exactly what one instance would buy: the Kummer persistence at all
primes > 3 transfers to **every** axiomatized gapped YM theory.

**No instance of `YMUniversality` is provided or claimed** —
constructing one is precisely the open research, and per the
workplan's mandatory caveat, until it exists every obstruction
statement is QOU-framework-conditional.
-/

namespace QOU.BraidKnot

open QOU.Torsion QOU.AlgebraicSubstrate

/-! ## Gap 1a — the spectral anchor of `E_×(q)` -/

/-- **The per-crossing energy is the mean of the two Hecke crossing
    eigenvalues.**  The braiding eigenvalues on `S²V ⊕ Λ²V` are
    `q` (symmetric channel) and `−q⁻¹` (antisymmetric channel); their
    mean is exactly `E_×(q) = (q − q⁻¹)/2`.

    This anchors the `CrossingFiltration` hypothesis in the
    categorical source of `q`: the filtration asserts that every
    non-vacuum excitation carries at least the *mean* spectral weight
    of one crossing. -/
-- Ref: [manuscript] braids-and-knots/hecke-algebra-from-braiding.md
theorem crossingEnergy_eq_eigenvalue_mean (q : ℝ) :
    minCrossingEnergy q = (q + (-q⁻¹)) / 2 := by
  unfold minCrossingEnergy
  ring

/-- **The crossing eigenvalue separation is `[2]_q`.**  The distance
    between the symmetric and antisymmetric channel eigenvalues is
    `q − (−q⁻¹) = q + q⁻¹ = [2]_q` — the quantum integer that
    normalises the Markov trace (`tr_M = V/[2]_q^{c−1}`). -/
-- Ref: [manuscript] braids-and-knots/hecke-algebra-from-braiding.md
theorem crossing_eigenvalue_separation (q : ℝ) :
    q - (-q⁻¹) = q + q⁻¹ := by
  ring

/-! ## Gap 1b — strategy (i) as base + transport -/

/-- **Filtration base case**: the per-crossing bound holds at the
    base level of the tower.  For the physical tower this is a fixed
    finite-rank spectral computation (H₂ or H₃) — the
    compute-witness + `native_decide` candidate. -/
class FiltrationBase (q : ℝ) (tms : ℕ → CategoricalTransferMatrix) : Prop where
  base : ∀ k, (tms 0).eigenvalues k ≠ 0 →
    minCrossingEnergy q ≤ (tms 0).eigenvalues k

/-- **Tower transport** (strategy (i), Wenzl/Jones-tower positivity):
    the inclusion `H_n ⊂ H_{n+1}` with conditional expectation
    preserves the per-crossing bound — if every non-vacuum excitation
    at level `n` dominates `E_×(q)`, the same holds at level `n + 1`.

    This is where the research content of S1c now lives: the
    conditional-expectation positivity argument supplies this field. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §1 S1c(i)
class TowerTransport (q : ℝ) (tms : ℕ → CategoricalTransferMatrix) : Prop where
  transport : ∀ n,
    (∀ k, (tms n).eigenvalues k ≠ 0 →
      minCrossingEnergy q ≤ (tms n).eigenvalues k) →
    (∀ k, (tms (n + 1)).eigenvalues k ≠ 0 →
      minCrossingEnergy q ≤ (tms (n + 1)).eigenvalues k)

/-- **Induction decomposition of the S1c hypothesis**: base case +
    tower transport ⟹ the full crossing-energy filtration.  The
    universally-quantified physical hypothesis is replaced by two
    strictly smaller named hypotheses, matching the shape of the
    workplan's preferred strategy (i). -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §1 S1c
theorem crossingFiltration_of_base_and_transport
    {q : ℝ} (tms : ℕ → CategoricalTransferMatrix)
    [hb : FiltrationBase q tms] [ht : TowerTransport q tms] :
    CrossingFiltration q tms where
  per_crossing := by
    intro n
    induction n with
    | zero => exact hb.base
    | succ m ih => exact ht.transport m ih

/-! ## Gap 2 — the universality interface -/

/-- **Minimal abstract axiomatized YM-with-gap data**: an excitation
    spectrum and a uniform positive gap.  Deliberately free of any
    QOU-specific structure — these are the only fields the transfer
    corollary consumes, so the universality gate is stated against
    the weakest meaningful interface. -/
structure AxiomatizedYMWithGap where
  /-- The excitation spectrum (energies of states). -/
  spectrum : Set ℝ
  /-- The mass gap. -/
  gap : ℝ
  /-- The gap is strictly positive. -/
  gap_pos : 0 < gap
  /-- Every non-vacuum excitation energy is bounded below by the gap. -/
  gap_bounds : ∀ E ∈ spectrum, E ≠ 0 → gap ≤ E

/-- **The universality gate** (the Millennium-relevance interface):
    a map sending every axiomatized gapped YM theory to a QOU
    obstruction-reduction context with `χ(A) = −6`.

    **No instance is provided or claimed** — constructing one ("any
    axiomatized YM with a gap yields a QOU-type structure") is the
    open research identified by the workplan, and per its mandatory
    caveat every obstruction statement remains QOU-framework-
    conditional until an instance exists.  This class pins the exact
    field signature such a construction must satisfy. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §3
-- Ref: [jaffe2006] https://www.claymath.org/millennium/yang-mills-the-maths-gap/
class YMUniversality where
  /-- The structure map: axiomatized gapped YM ⟶ obstruction context. -/
  toContext : AxiomatizedYMWithGap → QouObstructionReductionContext
  /-- The image context carries the QOU Euler characteristic. -/
  chi_is_minus_six : ∀ ym, (toContext ym).chi_A = -6

/-- **What one `YMUniversality` instance would buy**: the Kummer
    persistence at all primes > 3 transfers from the QOU framework to
    *every* axiomatized gapped YM theory.  Proved sorry-free against
    the interface; its physical force is exactly conditional on the
    (open) universality instance. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §3
theorem universality_transfers_obstruction [u : YMUniversality]
    (ym : AxiomatizedYMWithGap) {p : ℕ} (hp : Nat.Prime p) (hp3 : 3 < p) :
    ¬ (u.toContext ym).kappa_vanishes p := by
  letI : QouObstructionReductionContext := u.toContext ym
  exact kummer_persists_above_three (u.chi_is_minus_six ym) hp hp3

end QOU.BraidKnot
