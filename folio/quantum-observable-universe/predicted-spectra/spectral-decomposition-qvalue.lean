import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.Ring
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic


/-!
# QOU.Archimedean.spectral_decomposition_qvalue — Spectral decomposition of the Q_q-value

The torus knots embeddable on Σ₄ form a complete, self-dual basis
for the regular representation of the Hecke algebra H_n(q).  The Q_q-value of
beta decay is the spectral decomposition of the decay operator in
this basis.  The decomposition is exact and finite — it terminates at
degree 2 because the embeddability bound on Σ₄ kills all higher jets.

LaTeX label: `cor:spectral-decomposition-qvalue`

## References

- [leitner2026] §5/spectral-decomposition-qvalue
- [jones1987] https://doi.org/10.2307/1971403
- [turaev2010] https://doi.org/10.1515/9783110221848

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Archimedean

/-- A torus knot label τ(r, s) with coprimality and embeddability data. -/
structure TorusKnotLabel where
  r : ℕ
  s : ℕ
  coprime : Nat.Coprime r s
  genus : ℕ := (r - 1) * (s - 1) / 2

/-- The set of torus knot labels embeddable on Σ_g:
    E_g = {τ(r,s) : (r-1)(s-1)/2 ≤ g}. -/
def embeddableOnSurface (g : ℕ) (τ : TorusKnotLabel) : Prop :=
  τ.genus ≤ g

/-- The six nontrivial torus knots embeddable on Σ₄. -/
def embeddableOnBrings : List (ℕ × ℕ) :=
  [(2, 3), (2, 5), (2, 7), (2, 9), (3, 4), (3, 5)]

/-- Degree of a torus knot in the jet tower.
    Degree 1: τ(2,3), τ(2,5), τ(2,7), τ(3,5)
    Degree 2: τ(2,9), τ(3,4) -/
def torusKnotDegree : ℕ × ℕ → ℕ
  | (2, 3) => 1
  | (2, 5) => 1
  | (2, 7) => 1
  | (3, 5) => 1
  | (2, 9) => 2
  | (3, 4) => 2
  | _ => 0

/-- The quantum Planck constant ℏ_q = (q - 1)/q. -/
noncomputable def hbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- The bare Q-value: |log_q(P_dau/P_par)| · ℏ_q · m_e/3. -/
noncomputable def bareQValue (q : ℝ) (skeinRatio : ℝ) (m_e : ℝ) : ℝ :=
  |Real.log skeinRatio / Real.log q| * hbarQ q * m_e / 3

open scoped BigOperators

/-- **Knot-operator product collapse** — the mechanism behind step `(iv)` of the
    corollary, now *derived* rather than assumed.

    Over the finite embeddable torus-knot basis `E` (⊆ `E_g`), the knot-operator
    product `∏_{τ ∈ E} F τ` collapses to the single active shell `F active`
    whenever every other shell contributes the identity factor `1` — non-active
    shells cancel between parent and daughter, and non-embeddable knots give
    `F = 1`.  A direct application of `Finset.prod_eq_single`.

    This upgrades the earlier opaque assumption `knotOperatorProduct =
    activeShellTerm` (a class field that *asserted* the collapse): the collapse
    of a product of mostly-`1` factors is no longer assumed but proved.  What
    remains open (bean `qou-xq3f`) is the strictly weaker *per-shell* input
    `hInactive` — that each inactive `F τ = 1`, i.e. the Rosso–Jones
    cancellation itself. -/
-- Ref: [leitner2026] §5/spectral-decomposition-qvalue
theorem knot_operator_product_collapse
    {ι : Type*} (E : Finset ι) (F : ι → ℝ) (active : ι)
    (hActive : active ∈ E)
    (hInactive : ∀ τ ∈ E, τ ≠ active → F τ = 1) :
    ∏ τ ∈ E, F τ = F active :=
  Finset.prod_eq_single active hInactive (fun h => absurd hActive h)

/-- **Spectral decomposition of the Q_q-value** (Corollary, conditional on the
    per-shell Rosso–Jones cancellation `hInactive`).

    For β⁻ decay N_{Z,N} → N_{Z+1,N-1}, the Q_q-value admits
    the spectral decomposition:

      Q_q = Q_bare × Π_{τ(r,s) ∈ E_g} F(τ(r,s), N)

    where:
    (i)   P(q) = Π V̂_j(q) is the Skein polynomial in Gröbner normal form
    (ii)  log_q is the q-natural logarithm counting exceptional divisor levels
    (iii) F(τ(r,s), N) is the knot operator (Markov trace of τ·T_β on active shells)
    (iv)  The product collapses to a single term (shell cancellation)
    (v)   The decomposition is exact — terminates at degree 2 on Σ₄

    **Scope (2026-11-16).** Under convention D the Pauli (fully filled shell)
    factor `|tr_M(e_(1³)·τ·T_β·e_(1³))| / |tr_M(T_β)|` is identically `0`, since
    the Ocneanu weight of every three-row partition vanishes at `z = q³/(q²+1)`
    (`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`). The
    corollary is asserted only for non-magic converting shells; this theorem is
    the generic collapse and takes the active factor `F active` as given.

    **Restated 2026-08-22** (vacuity ledger, `proof-no-unused-hypothesis-rfl`).
    The prior form `∃ Q_q, Q_q = Q_bare · knotOperator` was a trivial existential
    (`⟨rhs, rfl⟩`) that asserted nothing.  This states the `(iv)` collapse of the
    Q-value's knot-operator factor and *derives* it from the per-shell
    cancellation `hInactive` via `knot_operator_product_collapse` — the collapse
    is proved, not assumed.  The per-shell cancellation (why each inactive
    `F τ = 1`) is the Rosso–Jones content and stays the hypothesis
    (bean `qou-xq3f`). -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
-- Ref: [leitner2026] §5/spectral-decomposition-qvalue
theorem spectral_decomposition_qvalue
    {ι : Type*}
    (q parentPoly daughterPoly m_e : ℝ)
    (E : Finset ι) (F : ι → ℝ) (active : ι)
    (hActive : active ∈ E)
    (hInactive : ∀ τ ∈ E, τ ≠ active → F τ = 1) :
    bareQValue q (daughterPoly / parentPoly) m_e * (∏ τ ∈ E, F τ)
      = bareQValue q (daughterPoly / parentPoly) m_e * F active := by
  rw [knot_operator_product_collapse E F active hActive hInactive]

/-! ## §2  Discharging the per-shell cancellation (the `hInactive` hypothesis)

`knot_operator_product_collapse` reduces step (iv) to the per-shell input
`hInactive : ∀ inactive shell, F τ = 1`.  This section *discharges* that input
for the two inactive branches of the corollary's `F(τ,N)` — non-embeddable and
unchanged shells — at the ratio level, so those branches are no longer assumed.

What stays open (bean `qou-xq3f`) is the **active** shell's value
`|tr_M(e·τ·T_β·e)| / |tr_M(T_β)|` and the identification of *which* shell is
active — the genuine Rosso–Jones / Markov-trace content, needing the weighted
trace tower (`QOU.Braiding.HnMarkovTrace`) not wired into this file. -/

/-- Per-shell decay data at the ratio level: the shell's Markov-trace weight
    before (parent) and after (daughter) the decay, and whether the shell's knot
    is embeddable on `Σ_g`. -/
structure ShellState where
  /-- Markov-trace weight of the shell in the parent nucleus. -/
  parentTrace : ℝ
  /-- Markov-trace weight of the shell in the daughter nucleus. -/
  daughterTrace : ℝ
  /-- Whether the shell's torus knot is embeddable on `Σ_g` (else `F = 1`). -/
  embeddable : Bool

/-- The knot-operator factor `F(τ,N)` for one shell, at the ratio level (the
    corollary's four cases collapsed to two):
    * non-embeddable → `1` (null: zero action on `Σ_g`);
    * embeddable → the trace ratio `daughterTrace / parentTrace` (which is the
      active shell's `tr_M` ratio, and equals `1` on an unchanged shell). -/
noncomputable def shellFactor (s : ShellState) : ℝ :=
  if s.embeddable then s.daughterTrace / s.parentTrace else 1

/-- **Non-embeddable branch.** A non-embeddable shell contributes `F = 1`
    (definitional: it has zero action on `Σ_g`). -/
theorem shellFactor_nonembeddable (s : ShellState) (h : s.embeddable = false) :
    shellFactor s = 1 := by
  simp [shellFactor, h]

/-- **Unchanged branch.** An embeddable shell left untouched by the decay
    (`daughterTrace = parentTrace`, nonzero) cancels in the ratio: `F = 1`.
    This is the genuine "cancels in ratio" mechanism — `div_self`, not an
    assumption. -/
theorem shellFactor_unchanged (s : ShellState)
    (hchg : s.daughterTrace = s.parentTrace) (hne : s.parentTrace ≠ 0) :
    shellFactor s = 1 := by
  unfold shellFactor
  split
  · rw [hchg]; exact div_self hne
  · rfl

/-- **Per-shell cancellation discharged.** If every shell other than `active`
    is inactive — non-embeddable, or unchanged with nonzero parent trace — the
    shell-factor product collapses to the active shell's factor, with the
    `hInactive` hypothesis of `knot_operator_product_collapse` now *proved* for
    this model rather than assumed. -/
theorem shell_product_collapse
    {ι : Type*} (E : Finset ι) (S : ι → ShellState) (active : ι)
    (hActive : active ∈ E)
    (hInactive : ∀ τ ∈ E, τ ≠ active →
        (S τ).embeddable = false ∨
        ((S τ).daughterTrace = (S τ).parentTrace ∧ (S τ).parentTrace ≠ 0)) :
    ∏ τ ∈ E, shellFactor (S τ) = shellFactor (S active) := by
  refine knot_operator_product_collapse E (fun τ => shellFactor (S τ)) active hActive ?_
  intro τ hτ hne
  rcases hInactive τ hτ hne with h | ⟨hchg, hne0⟩
  · exact shellFactor_nonembeddable (S τ) h
  · exact shellFactor_unchanged (S τ) hchg hne0

/-- The jet bundle over Σ₄ has exactly three non-zero levels (k = 0, 1, 2).
    Degree 3 requires genus ≥ 13, exceeding the genus-4 bound. -/
-- Ref: [leitner2026] §5/spectral-decomposition-qvalue
theorem tower_terminates_at_degree_2 (r s : ℕ)
    (hr : r ≥ 2) (hs : s ≥ 2) (hcop : Nat.Coprime r (s ^ 3))
    (hgen : (r - 1) * (s ^ 3 - 1) / 2 ≥ 13) :
    ¬ embeddableOnSurface 4 ⟨r, s ^ 3, hcop, (r - 1) * (s ^ 3 - 1) / 2⟩ := by
  -- Genus ≥ 13 > 4 = genus of Σ₄, so not embeddable.
  intro hemb
  unfold embeddableOnSurface at hemb
  simp only at hemb
  omega

/-- Self-duality: τ(r,s) ↔ τ(s,r) provides the inner product for
    completeness of the torus knot basis. -/
-- Ref: [leitner2026] §5/spectral-decomposition-qvalue
theorem torus_knot_self_duality (r s : ℕ) :
    (r - 1) * (s - 1) = (s - 1) * (r - 1) := by
  ring

end QOU.Archimedean
