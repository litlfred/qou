/-
Copyright (c) 2026 litlfred. All rights reserved.

# Symmetry-eigenspace selection rules — one engine for the weak (c₃) and strong (Δ_λ) sectors

Two independent QOU dead ends share a single structural cause: a candidate object
built from the **wrong symmetry eigenspace** is excluded from a target that lives in
another eigenspace. Formalizing the obstruction turns a scatter of numerical misses
into a machine-checked *selection rule*, so a re-proposal in the same eigenspace is
dead on arrival (the "no 7th fit-based ansatz" gate, `AGENTS.md §Δ_λ gate`).

Two eigenspaces of two different symmetries recur:

1. **Bar-parity** (the involution `q ↦ q⁻¹`, weak / Q_β sector).
   - The Q_β coefficient `c₃` is the leading datum of the bar-**ODD** decay channel:
     its carrier `Δ(net)_odd = (h/4)·C(y)` flips sign under the bar (`h = q−q⁻¹`
     bar-odd; `QOU.QBeta.HopfCubic`, probe `qbeta_net_bar_odd_projection`).
   - `Vol(4₁)` (the figure-eight / Higgs volume) is bar-**EVEN**: `4₁` is amphichiral,
     `CS(4₁)=0`, `𝔙(4₁)=Vol` real (`self-dual-higgs-real-volume`, #3482) — the corpus
     already proves the bare Higgs knot carries only the even mass face
     ("𝔔_β is not a property of the lone Higgs knot").
   - `odd_ne_even_of_ne_zero` is the *structural* (scope-(b)) reason the Gemini-session
     identification `c₃ = −Vol(4₁)` fails: a bar-even invariant projects to `0` in the
     bar-odd channel, so it can never be the *source* of a nonzero bar-odd coefficient.
     Not merely anchor-blind (scope-(a) probe `qbeta_c3_continuum_vol41_anchor_blind`) —
     wrong eigenspace.

2. **Sign / positivity** (the `Δ_λ` per-isotope binding sector).
   - The `Δ_λ` target is **mixed-sign** (`Δ_λ = sgn(w₀)·dim`, Lean-proved
     `QOU.BraidsAndKnots.deltaSign_mixed`).
   - `nonneg_sum_ne_neg_target` is the common cause of TWO of the six refuted Δ_λ
     ansätze (`QOU.BraidKnot.DeltaLambdaRefutation`): the Frobenius co-Casimir
     `1/dim_q(λ) > 0` (row B, `coCasimir_wrong_sign`) and the crystal-graph KL route
     (row E, KL multiplicities `n^w_λ ≥ 0` — the KL-positivity prune). No non-negative
     combination of non-negative operators can equal a strictly negative target, so on
     the partitions where `Δ_λ < 0` every positive ansatz is excluded *up front*.

**Forward use (necessary condition, not closure).** Both rules are *necessary*
conditions on a source, not derivations. They prune: a Δ_λ source must be
sign-carrying (chiral) — the amphichiral / positive classes are dead on arrival — which
is why chiral torus knots `T(2, odd)` are the parity-*allowed* candidate class. Allowed
≠ derived: the archimedean residue (the c₃ swing / the Δ_λ magnitude) remains open
(Subgoal-2 / Track A). These lemmas justify the gate, they do not lift it.

Generic base ring per §7c — no archimedean structure; the involution is abstract, the
positivity lemma is over any ordered comm ring.
-/
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.LinearCombination

namespace QOU.SelectionRules

/-! ## 1. Bar-parity selection (weak / Q_β sector) -/

/-- A bar-involution: an additive, negation-compatible self-map of the ring
    (the arithmetic shadow of `q ↦ q⁻¹` on the Laurent ring). Only additivity is
    needed for the eigenspace-orthogonality argument, so we ask for no more. -/
structure BarInvolution (R : Type*) [CommRing R] where
  bar : R → R
  bar_add : ∀ a b, bar (a + b) = bar a + bar b
  bar_neg : ∀ a, bar (-a) = -bar a

variable {R : Type*} [CommRing R]

/-- **Parity orthogonality (the exclusion).** In characteristic ≠ 2 (`NoZeroDivisors`
    + `2 ≠ 0`), a nonzero bar-**ODD** element `x` (`bar x = −x`) cannot equal any
    bar-**EVEN** element `v` (`bar v = v`): the odd and even eigenspaces of the
    involution meet only at `0`.

    Applied: the bar-odd `c₃` carrier ≠ the bar-even `−Vol(4₁)`. This is the
    scope-(b) structural reason `c₃ = −Vol(4₁)` fails — wrong bar-parity eigenspace,
    not merely a wrong number. -/
theorem odd_ne_even_of_ne_zero [NoZeroDivisors R] (B : BarInvolution R)
    (x v : R) (hx : B.bar x = -x) (hv : B.bar v = v)
    (h2 : (2 : R) ≠ 0) (hx0 : x ≠ 0) : x ≠ v := by
  intro hxv
  have htwo : (2 : R) * x = 0 := by
    have h1 : B.bar x = B.bar v := congrArg B.bar hxv
    rw [hx, hv] at h1        -- h1 : -x = v
    rw [← hxv] at h1         -- h1 : -x = x
    linear_combination -h1
  exact (mul_eq_zero.mp htwo).elim h2 hx0

/-- A trivial bar-involution (identity) witnesses that the structure is inhabited;
    the load-bearing instance is `q ↦ q⁻¹` on the Laurent ring (built elsewhere). -/
def id (R : Type*) [CommRing R] : BarInvolution R where
  bar := _root_.id
  bar_add _ _ := rfl
  bar_neg _ := rfl

/-! ## 2. Sign / positivity selection (strong / Δ_λ sector) -/

/-- **Positivity exclusion (the common cause of Δ_λ rows B and E).** A non-negative
    linear combination of non-negative operators is non-negative, hence cannot equal a
    strictly negative target.

    Applied to `Δ_λ`: on any partition where the mixed-sign target `Δ_λ < 0`, every
    positive ansatz — Frobenius co-Casimir (`1/dim_q > 0`) and the crystal/KL route
    (`Σ_w n^w_λ · X_w`, `n^w_λ ≥ 0`) — is excluded. One machine-checked selection rule
    unifies the co-Casimir wrong-sign refutation and the KL-positivity prune. -/
theorem nonneg_sum_ne_neg_target {R : Type*} [CommRing R] [PartialOrder R]
    [IsOrderedRing R] {ι : Type*} (s : Finset ι) (n x : ι → R)
    (hn : ∀ i ∈ s, 0 ≤ n i) (hx : ∀ i ∈ s, 0 ≤ x i)
    (t : R) (ht : t < 0) : ∑ i ∈ s, n i * x i ≠ t := by
  have h : 0 ≤ ∑ i ∈ s, n i * x i :=
    Finset.sum_nonneg fun i hi => mul_nonneg (hn i hi) (hx i hi)
  intro heq
  rw [heq] at h
  exact absurd (lt_of_lt_of_le ht h) (lt_irrefl t)

end QOU.SelectionRules
