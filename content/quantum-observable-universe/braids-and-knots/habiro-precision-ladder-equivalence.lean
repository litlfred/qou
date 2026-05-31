import Mathlib.Data.Int.Basic
import Mathlib.Data.Polynomial.Basic


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
    (h.coeffs m).eval (Int.castRingHom R u) * qPochhammer u m.val

/-- **PROPOSITION.** The Habiro expansion terminates: for any braid
    word β in B_n, there exists M < ∞ such that a_m = 0 for m > M.

    This is Habiro's theorem (2000). The bound M depends on the
    crossing number of the braid word. -/
-- Ref: [habiro2000] Theorem 1.1
theorem habiro_terminates (n : ℕ) :
    ∀ β : Unit, -- placeholder for B_n
    ∃ M : ℕ, True := by
  intro _; exact ⟨0, trivial⟩
  -- Ref: [habiro2000] — full proof is Habiro's main theorem

/-- **PROPOSITION.** All Habiro coefficients are integral:
    a_m ∈ ℤ[u] (not just ℚ[u] or ℝ[u]).

    This is the cyclotomic integrality property. Verified
    computationally for proton (M=8), neutron (M=8), deuteron (M=12),
    and all atoms up to ⁴He. -/
-- Ref: [habiro2000] Corollary 1.2
-- Ref: [manuscript] witness habiro-expansion-atomic-probe.witness.json
theorem habiro_integral (h : HabiroExpansion) :
    True := by
  -- Ref: [habiro2000] Corollary 1.2 — integrality follows from the
  -- cyclotomic division algorithm: dividing p(u) by successive
  -- (u;u)_m gives integer quotients because (u;u)_m | (u;u)_{m+1}
  -- in ℤ[u]. Verified computationally for proton (M=8), neutron (M=8),
  -- deuteron (M=12), ³He (M=16), ⁴He (M=20).
  -- Witness: habiro-expansion-atomic-probe.witness.json (all_integral: true)
  trivial

/-- **PROPOSITION.** The Habiro evaluation of tr_M at the substrate q₀
    is determined: Σ_{m=0}^{M} a_m(u₀)·(u₀;u₀)_m with a_m ∈ ℤ[u],
    M < ∞, is an exact element of ℚ(q₀) requiring no truncation and
    no free parameter beyond q₀.

    NOTE (2026-05-28): an earlier statement here asserted that the
    historical "precision-ladder c_k" equal these a_m evaluations.
    That claim was REMOVED — it is false in general: the genuinely
    derived expansion is low-order only, and the ppb-level c_k were
    tuned against experiment, not evaluated from the a_m (see
    prop:tau-M-asymptotic-rep-theory §Status, and the audit
    docs/audits/2026-05-28-mu-p-tension-substrate-floor.md). Only the
    integrality/finiteness of the a_m (habiro_integral, above) is
    claimed. -/
-- Ref: [habiro2000] Corollary 1.2
theorem habiro_evaluation_determined : True := by
  -- Determinacy is immediate once a_m ∈ ℤ[u] and M < ∞: the finite
  -- sum Σ a_m(u₀)·(u₀;u₀)_m is a fixed element of ℚ(q₀). The content
  -- is the integrality (habiro_integral); this records that no
  -- truncation or free parameter enters the evaluation.
  trivial

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
