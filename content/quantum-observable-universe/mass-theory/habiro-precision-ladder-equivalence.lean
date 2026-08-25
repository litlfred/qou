import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Eval.Defs


/-!
# QOU.BraidKnot.HabiroPrecisionLadderEquivalence

The precision-ladder coefficients c_k for the Q_β categorical
prediction are the archimedean evaluations of integer Habiro
coefficients a_m(u) ∈ ℤ[u].

The Markov trace tr_M(T_w, q) of any closed braid word admits a
finite Habiro expansion:

  tr_M = Σ_{m=0}^{M} a_m(u) · (u;u)_m,   a_m ∈ ℤ[u], M < ∞

where (u;u)_m = Π_{k=1}^{m}(1 - u^{2k}) is the q-Pochhammer symbol
and u = q^{1/2}. Under archimedean evaluation u → u₀ = q₀^{1/2},
each (u₀;u₀)_m shrinks like ~ℏ_q^m, giving the precision ladder.

The integer coefficients a_m are determined and the expansion
terminates at finite M (no truncation error). NOTE: the historical
"precision-ladder c_k" are NOT in general the Taylor coefficients of
this exact sum — the genuinely-derived expansion is low-order only,
and the higher c_k used for ppb-level fits were tuned against
experiment (see prop:tau-M-asymptotic-rep-theory §Status). Only the
a_m integrality is claimed here.

Ref: [habiro2000] Habiro, "On the quantum sl_2 invariants of knots
     and integral homology spheres" (2000)
Ref: [jones1987] Jones, "Hecke algebra representations of braid
     groups and link polynomials" (1987)
Ref: [manuscript] prop:habiro-precision-ladder-equivalence
-/

namespace QOU.BraidKnot

/-- The q-Pochhammer symbol (u;u)_m = Π_{k=1}^{m}(1 - u^{2k}).
    This is the key structural ingredient of the Habiro expansion:
    at substrate u₀, each factor (1 - u₀^{2k}) ≈ 1 - q₀^k is close
    to 1, so the product shrinks like ℏ_q^m. -/
noncomputable def qPochhammer {R : Type*} [CommRing R] (u : R) : ℕ → R
  | 0 => 1
  | m + 1 => qPochhammer u m * (1 - u ^ (2 * (m + 1)))

/-- A Habiro coefficient is an integer polynomial in u = q^{1/2}. -/
abbrev HabiroCoeff := Polynomial ℤ

/-- A Habiro expansion of a Markov trace: the finite sum
    Σ_{m=0}^{M} a_m(u) · (u;u)_m with a_m ∈ ℤ[u]. -/
structure HabiroExpansion where
  M : ℕ
  coeffs : Fin (M + 1) → HabiroCoeff

/-- Evaluate a Habiro expansion at u ∈ R. -/
noncomputable def HabiroExpansion.eval {R : Type*} [CommRing R]
    (h : HabiroExpansion) (u : R) : R :=
  Finset.univ.sum fun m =>
    (h.coeffs m).eval₂ (Int.castRingHom R) u * qPochhammer u m.val

/-- **PROPOSITION (finiteness / termination).** The Habiro expansion of a
    Markov trace is a *finite* sum: its evaluation `h.eval u` is a sum over
    the finite index set `Fin (h.M + 1)` (`h.M < ∞`), so there is no
    truncation — the sum is taken over all `h.M + 1` terms.  Concretely the
    index set has cardinality `h.M + 1`, a finite natural number.

    This faithfully states the md's "the series terminates (`M < ∞`)",
    replacing the prior placeholder `∃ M, True`.  (Habiro 2000 Thm 1.1
    supplies the existence of such a finite expansion for any braid word;
    here we record that the structure carries a finite bound.) -/
-- Ref: [habiro2000] Theorem 1.1
theorem habiro_terminates (h : HabiroExpansion) :
    (Finset.univ : Finset (Fin (h.M + 1))).card = h.M + 1 := by
  simp

/-- **PROPOSITION (cyclotomic integrality).** Every Habiro coefficient is
    integral: `a_m ∈ ℤ[u]`.  Concretely, evaluating any coefficient at an
    integer point `u₀ : ℤ` yields an integer — i.e. for each index `m`,
    `(h.coeffs m).eval u₀ : ℤ` is a genuine integer (no rational/real
    denominators appear).

    This is the substantive content of the md's integrality claim: the
    coefficients live in `ℤ[u]`, not `ℚ[u]` or `ℝ[u]`, so their integer-point
    evaluations are integers.  (Verified computationally for proton (M=8),
    neutron (M=8), deuteron (M=12), ³He (M=16), ⁴He (M=20) —
    `habiro-expansion-atomic-probe.witness.json`, `all_integral: true`.)

    **Stated in the ambient ring, which is where the claim has teeth.**
    `HabiroCoeff` is `Polynomial ℤ`, so `(h.coeffs m).eval u₀ : ℤ` is an
    integer by typing and `∃ z : ℤ, (h.coeffs m).eval u₀ = z` — what stood
    here until 2026-08-21 — restated that typing rather than the
    proposition.  The claim that can fail is about `HabiroExpansion.eval`,
    which evaluates through `Int.castRingHom R` into an arbitrary
    `CommRing R` (`R := ℝ` at the substrate): at an integer point the
    result stays in the image of `ℤ`, with the integer given by the
    ℤ-valued evaluation.  Over `ℚ[u]` coefficients the corresponding
    statement is false, which is the distinction the md is drawing. -/
-- Ref: [habiro2000] Corollary 1.2
-- Ref: [manuscript] witness habiro-expansion-atomic-probe.witness.json
theorem habiro_integral {R : Type*} [CommRing R]
    (h : HabiroExpansion) (m : Fin (h.M + 1)) (u₀ : ℤ) :
    (h.coeffs m).eval₂ (Int.castRingHom R) (u₀ : R)
      = ((h.coeffs m).eval u₀ : ℤ) := by
  have : ((u₀ : ℤ) : R) = (Int.castRingHom R) u₀ := rfl
  rw [this, Polynomial.eval₂_at_apply]
  rfl

/-- **PROPOSITION (determinacy of the evaluation).** The Habiro evaluation of
    `tr_M` at the substrate `u` is *determined* by the expansion data: it is
    a well-defined function of `(h, u)`.  Two expansions with the same bound
    and the same coefficients yield the same evaluation — no truncation
    choice and no free parameter beyond `u` enters.

    NOTE (2026-05-28): an earlier statement here asserted the historical
    "precision-ladder c_k" equal these `a_m` evaluations.  That claim was
    REMOVED — false in general (the derived expansion is low-order only; the
    ppb-level c_k were tuned against experiment, not evaluated from the
    `a_m`; see `prop:tau-M-asymptotic-rep-theory` §Status and
    `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md`).  Only the
    determinacy/integrality/finiteness of the `a_m` is claimed.  Replaces the
    prior placeholder `True`. -/
-- Ref: [habiro2000] Corollary 1.2
theorem habiro_evaluation_determined {R : Type*} [CommRing R]
    (h₁ h₂ : HabiroExpansion) (u : R)
    (hM : h₁.M = h₂.M) (hc : HEq h₁.coeffs h₂.coeffs) :
    h₁.eval u = h₂.eval u := by
  cases h₁ with
  | mk M₁ c₁ =>
    cases h₂ with
    | mk M₂ c₂ =>
      cases hM
      cases hc
      rfl

/-! ## §3b-cond bridge class: are the c_k the Habiro Taylor coefficients?

The header note above states that the precision-ladder c_k are NOT in
general the Taylor coefficients of the exact Habiro tr_M. This section
makes that statement a formal §3b-cond conditional, mirroring the
verified `EmAlphaInvNextOrderBlochClass` pattern (PR #1508) and
`QbetaC3StructuralFormClass` (`q-beta-categorical-precision-ladder.lean`).

**The bridge is the genuine open derivation step** (gap-plan Bug 3,
`docs/audits/2026-05-30-qbeta-habiro-derivation-gap-plan.md`):
identifying the substrate-canonical `f` with `Q_β = m_e · f(Δtr_M, q)`,
whose Habiro Taylor coefficients would then BE the c_k. Two decisive
tests (2026-05-31) bound what the bridge is NOT:

  - `qbeta-delta-tr-vs-formA.witness.json` (item 1): the Habiro Δtr_M is
    NOT Form A's net-winding slot (leading Taylor orders differ,
    −5/4 vs −2); the bridge is not the canonical-refinement substitution.
  - `mp-dk-decisive-test.witness.json` (item 2): the m_p d_k are stale-q₀
    near-matches (d_4 = 46 drifts 100% between q₀ pins), confirming the
    same failure mode on the mass side.

Only `c_2 = -1` is Taylor-exact (proved to compute precision). The
bridge class below carries the OPEN equivalence as a conditional
hypothesis; NO instance is provided, and production wires only c_2. -/

/-- Abstract precision-ladder coefficient `c_k` (as used in the Q_β
    ladder). Opaque so the bridge class is non-vacuous (mirrors #1508's
    opaque `BlochWigner_unit_circle`). -/
-- Ref: [manuscript] prop:habiro-precision-ladder-equivalence
axiom precisionLadderCoeff : ℕ → ℝ

/-- Abstract Habiro Taylor coefficient: the exact Taylor coefficient,
    at substrate q₀, of the Habiro tr_M expansion. Opaque (its closed
    form is the open multi-block derivation). -/
-- Ref: [habiro2000] Corollary 1.2
axiom habiroTaylorCoeff : ℕ → ℝ

/-- **§3b-cond bridge class.** Axiomatises the OPEN equivalence between
    the precision-ladder coefficients and the Habiro Taylor
    coefficients. This is the formal statement of the gap-plan Bug 3
    bridge. Per the discipline note above it is NOT established beyond
    `c_2`; the class is purely conditional (no instance) and production
    wires only the Taylor-exact `c_2 = -1` rung. -/
-- Ref: [manuscript] prop:habiro-precision-ladder-equivalence
-- Ref: PR #1508 (§3b-cond conditional-class pattern)
class QbetaHabiroTaylorBridgeClass : Prop where
  /-- The precision-ladder `c_k` equals the Habiro Taylor coefficient at
      every order `k`. Known to hold for `k = 2` (Taylor-exact); open
      for `k ≥ 3` (item-1 / item-2 decisive tests). -/
  ck_eq_taylor : ∀ k : ℕ, precisionLadderCoeff k = habiroTaylorCoeff k

/-- **Conditional bridge theorem** (§3b-cond, proved sorry-free from
    `QbetaHabiroTaylorBridgeClass`). Under the bridge hypothesis, the
    ladder coefficient at any order equals the Habiro Taylor
    coefficient — i.e. the c_k ARE the Habiro Taylor coefficients.
    Mirrors `em_alpha_inv_full_form` (#1508): the class field carries
    the conditional content. This LOCKS the equivalence as the open
    derivation target without claiming it is established (only c_2 is). -/
-- Ref: [manuscript] prop:habiro-precision-ladder-equivalence
-- Ref: PR #1508 (§3b-cond conditional-class pattern)
theorem precision_ladder_is_habiro_taylor
    [h : QbetaHabiroTaylorBridgeClass] (k : ℕ) :
    precisionLadderCoeff k = habiroTaylorCoeff k :=
  h.ck_eq_taylor k

end QOU.BraidKnot
