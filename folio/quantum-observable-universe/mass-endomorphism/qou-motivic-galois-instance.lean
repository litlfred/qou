import QOU.LiftingDescent.MotivicGaloisCharacter
import QOU.BringsSurface.MotivicSubstrateTrivial
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
# The QOU Motivic Galois Character on the Habiro Ring (`qou-motivic-galois-instance`)

Per remediation standard §3b-cond (`conj:qou-motivic-galois-instance`), this module formalises
the conditional structure of the QOU Motivic Galois Character conjecture together with
its unconditional Habiro cyclotomic-truncation foundation:

1. **Unconditional Habiro Pochhammer Vanishing & Truncation
   (`qPochhammer_eq_zero_of_pow_eq_one`, `habiro_pochhammer_truncation_sum_eq`)**:
   In the Habiro ring $\widehat{\mathbb{Z}[u]} = \varprojlim_n \mathbb{Z}[u]/((u;u)_n)$,
   the $q$-Pochhammer product $(u; u)_m = \prod_{k=1}^m (1 - u^k)$ vanishes at any
   $2p$-th root of unity $\zeta$ ($\zeta^{2p} = 1$) whenever $m \ge 2p > 0$. Consequently,
   for any series term sequence `term : ℕ → R` satisfying `∀ m ≥ 2 * p, term m = 0`, every
   partial sum `∑ m ∈ Finset.range N, term m` with `N ≥ 2 * p` stabilizes identically to
   the finite truncation `∑ m ∈ Finset.range (2 * p), term m`.

2. **§3b Conditional Hypothesis Class (`HabiroMotivicCoherenceHypothesis`)**:
   Encodes the open conjectural input of `conj:qou-motivic-galois-instance` relative to a
   `MotivicSubstrate K0 Mhat Target`:
   - at each prime `p : Nat.Primes`, a sequence of Habiro expansion terms
     `habiro_terms p : ℕ → Target (Place.finite p)` satisfying the Pochhammer vanishing
     condition `∀ m ≥ 2 * p.val, habiro_terms p m = 0`,
   - a cross-prime Habiro lift `frob_lift : Nat.Primes → Mhat` whose realization
     `sub.realize (Place.finite p) (frob_lift p)` agrees with the finite `2p`-term Habiro sum
     `(Finset.range (2 * p.val)).sum (habiro_terms p)`, and
   - local tower non-degeneracy: whenever `Target (Place.finite p)` is nontrivial, the
     finite `2p`-term Habiro evaluation is non-zero.

3. **Derived Motivic Galois Character (`qouMotivicGaloisCharacterOfCoherence`)**:
   Under `[HabiroMotivicCoherenceHypothesis K0 Mhat Target motiveA]`, constructs a canonical
   `MotivicGaloisCharacter K0 Mhat Target motiveA`, proves its Frobenius realization at every
   prime `p` agrees with any cutoff `N ≥ 2p` of the Habiro series
   (`qouMotivicGaloisCharacter_realize_eq_finite_sum`), and establishes non-degeneracy across
   the prime tower (`qouMotivicGaloisCharacter_nondegenerate`).

4. **Non-Vacuity / Satisfiability Witness (`habiroMotivicCoherenceTrivialWitness`)**:
   Provides a concrete inhabited `def` witness over `(ℤ, ℤ, trivialTarget)` (deliberately a
   `def`, not an `instance`, so downstream hypotheses are never silently discharged).
-/

namespace QOU.LiftingDescent

open QOU.AlgebraicSubstrate

/-- Concrete polynomial model of the $q$-Pochhammer factor $(1 - \zeta^{2p})$ vanishing at
    any $2p$-th root of unity $\zeta$ satisfying $\zeta^{2p} = 1$. -/
theorem qPochhammer_top_factor_zero_at_root_of_unity
    {R : Type*} [CommRing R] (ζ : R) (p : ℕ) (hζ : ζ ^ (2 * p) = 1) :
    1 - ζ ^ (2 * p) = 0 := by
  rw [hζ, sub_self]

/-- **Unconditional $q$-Pochhammer Cyclotomic Vanishing**:
    For any $2p$-th root of unity $\zeta$ ($\zeta^{2p} = 1$) with $p \ge 1$ and any $m \ge 2p$,
    the $q$-Pochhammer product $(\zeta; \zeta)_m = \prod_{k \in [1, m]} (1 - \zeta^k)$ vanishes
    in any commutative ring `R`. -/
theorem qPochhammer_eq_zero_of_pow_eq_one
    {R : Type*} [CommRing R] (ζ : R) {p m : ℕ} (hp : 1 ≤ p) (hm : 2 * p ≤ m)
    (hζ : ζ ^ (2 * p) = 1) :
    (Finset.Icc 1 m).prod (fun k => 1 - ζ ^ k) = 0 := by
  refine Finset.prod_eq_zero (i := 2 * p) ?_ (qPochhammer_top_factor_zero_at_root_of_unity ζ p hζ)
  rw [Finset.mem_Icc]
  omega

/-- **Unconditional Habiro Pochhammer Truncation Identity**:
    Whenever `term m = 0` for all `m ≥ 2 * p`, any partial sum of length `N ≥ 2 * p` reduces
    unconditionally to the finite sum over `Finset.range (2 * p)`. -/
theorem habiro_pochhammer_truncation_sum_eq
    {R : Type*} [AddCommMonoid R]
    (p N : ℕ) (hN : 2 * p ≤ N)
    (term : ℕ → R) (hvanish : ∀ m : ℕ, 2 * p ≤ m → term m = 0) :
    (Finset.range N).sum term = (Finset.range (2 * p)).sum term := by
  symm
  apply Finset.sum_subset (Finset.range_mono hN)
  intro m _ hm2p
  rw [Finset.mem_range, not_lt] at hm2p
  exact hvanish m hm2p

/-- **§3b Conditional Hypothesis Class (`HabiroMotivicCoherenceHypothesis`)**:
    Packages the open arithmetic coherence hypothesis of `conj:qou-motivic-galois-instance`:
    there exists a Habiro-lift Frobenius character across `Nat.Primes` whose realization
    at each finite place `Place.finite p` is computed by the finite `2p`-term Habiro
    cyclotomic specialization and is non-zero whenever `Target (Place.finite p)` is nontrivial. -/
class HabiroMotivicCoherenceHypothesis
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (Target : Place → Type*) [∀ v, CommRing (Target v)]
    [sub : MotivicSubstrate K0 Mhat Target]
    (motiveA : Mhat) where
  /-- The sequence of Habiro expansion terms $a_m(\zeta_{2p}) (\zeta_{2p}; \zeta_{2p})_m$
      evaluated in `Target (Place.finite p)` for each prime $p$. -/
  habiro_terms : (p : Nat.Primes) → ℕ → Target (Place.finite p)
  /-- Pochhammer truncation: for every $m \ge 2p$, the $m$-th Habiro term vanishes at $\zeta_{2p}$. -/
  habiro_terms_vanish :
    ∀ (p : Nat.Primes) (m : ℕ), 2 * p.val ≤ m → habiro_terms p m = 0
  /-- Cross-prime lift of the Frobenius character into the completed motivic ring `Mhat`. -/
  frob_lift : Nat.Primes → Mhat
  /-- Compatibility of `sub.realize (Place.finite p) (frob_lift p)` with the finite `2p`-term
      Habiro specialization. -/
  frob_lift_spec :
    ∀ p : Nat.Primes,
      sub.realize (Place.finite p) (frob_lift p) =
        (Finset.range (2 * p.val)).sum (habiro_terms p)
  /-- Local realization non-degeneracy of the finite `2p`-term Habiro specialization. -/
  habiro_sum_ne_zero :
    ∀ p : Nat.Primes, Nontrivial (Target (Place.finite p)) →
      (Finset.range (2 * p.val)).sum (habiro_terms p) ≠ 0

/-- **Main §3b Conditional Construction (`qouMotivicGaloisCharacterOfCoherence`)**:
    Under `HabiroMotivicCoherenceHypothesis`, the Habiro-lifted Frobenius tower defines
    a valid `MotivicGaloisCharacter K0 Mhat Target motiveA`. -/
def qouMotivicGaloisCharacterOfCoherence
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (Target : Place → Type*) [∀ v, CommRing (Target v)]
    [sub : MotivicSubstrate K0 Mhat Target]
    (motiveA : Mhat)
    [H : HabiroMotivicCoherenceHypothesis K0 Mhat Target motiveA] :
    MotivicGaloisCharacter K0 Mhat Target motiveA where
  frobenius_at := H.frob_lift
  frobenius_realize_ne_zero := by
    intro p hnt
    rw [H.frob_lift_spec p]
    exact H.habiro_sum_ne_zero p hnt

/-- **Theorem (`qouMotivicGaloisCharacter_realize_eq_finite_sum`)**:
    Under `HabiroMotivicCoherenceHypothesis`, for every prime $p$ and every cutoff $N \ge 2p$,
    the finite-place realization of the motivic Frobenius character equals the $N$-term Habiro sum
    and stabilizes at the finite $2p$-term cyclotomic truncation. -/
theorem qouMotivicGaloisCharacter_realize_eq_finite_sum
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (Target : Place → Type*) [∀ v, CommRing (Target v)]
    [sub : MotivicSubstrate K0 Mhat Target]
    (motiveA : Mhat)
    [H : HabiroMotivicCoherenceHypothesis K0 Mhat Target motiveA]
    (p : Nat.Primes) (N : ℕ) (hN : 2 * p.val ≤ N) :
    sub.realize (Place.finite p)
      ((qouMotivicGaloisCharacterOfCoherence K0 Mhat Target motiveA).frobenius_at p) =
      (Finset.range N).sum (H.habiro_terms p) := by
  change sub.realize (Place.finite p) (H.frob_lift p) =
    (Finset.range N).sum (H.habiro_terms p)
  rw [H.frob_lift_spec p]
  symm
  exact habiro_pochhammer_truncation_sum_eq p.val N hN (H.habiro_terms p) (H.habiro_terms_vanish p)

/-- **Theorem (`qouMotivicGaloisCharacter_nondegenerate`)**:
    Under `HabiroMotivicCoherenceHypothesis`, the motivic Galois character is not identically
    zero across the prime tower. -/
theorem qouMotivicGaloisCharacter_nondegenerate
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (Target : Place → Type*) [∀ v, CommRing (Target v)]
    [sub : MotivicSubstrate K0 Mhat Target]
    (motiveA : Mhat)
    [H : HabiroMotivicCoherenceHypothesis K0 Mhat Target motiveA] :
    ¬ (∀ p : Nat.Primes,
        (qouMotivicGaloisCharacterOfCoherence K0 Mhat Target motiveA).frobenius_at p = 0) :=
  not_forall_frobenius_eq_zero (qouMotivicGaloisCharacterOfCoherence K0 Mhat Target motiveA)

/-- **Non-Vacuity / Satisfiability Witness (`habiroMotivicCoherenceTrivialWitness`)**:
    Concrete inhabited `def` witness of `HabiroMotivicCoherenceHypothesis` over the trivial
    motivic substrate `(ℤ, ℤ, trivialTarget)`, where at each prime $p$ the $m = 0$ Habiro
    term is `(p.val : ℤ)` and all higher terms $m \ge 1$ vanish. Deliberately a `def` rather
    than an `instance` so typeclass search never silently discharges the hypothesis. -/
def habiroMotivicCoherenceTrivialWitness :
    HabiroMotivicCoherenceHypothesis ℤ ℤ trivialTarget (1 : ℤ) where
  habiro_terms := fun p m => if m = 0 then (p.val : ℤ) else 0
  habiro_terms_vanish := by
    intro p m hm
    have hp2 : 2 ≤ p.val := Nat.Prime.two_le p.prop
    have hm_pos : m ≠ 0 := by omega
    simp [hm_pos]
  frob_lift := fun p => (p.val : ℤ)
  frob_lift_spec := by
    intro p
    have hp2 : 2 ≤ p.val := Nat.Prime.two_le p.prop
    have h2p_pos : 0 < 2 * p.val := by omega
    have hsum :
        (Finset.range (2 * p.val)).sum (fun m => if m = 0 then (p.val : ℤ) else 0) =
          (p.val : ℤ) := by
      rw [Finset.sum_ite_eq' (Finset.range (2 * p.val)) 0 (fun _ => (p.val : ℤ))]
      simp [Finset.mem_range, h2p_pos]
    exact hsum.symm
  habiro_sum_ne_zero := by
    intro p _
    have hp2 : 2 ≤ p.val := Nat.Prime.two_le p.prop
    have h2p_pos : 0 < 2 * p.val := by omega
    have hsum :
        (Finset.range (2 * p.val)).sum (fun m => if m = 0 then (p.val : ℤ) else 0) =
          (p.val : ℤ) := by
      rw [Finset.sum_ite_eq' (Finset.range (2 * p.val)) 0 (fun _ => (p.val : ℤ))]
      simp [Finset.mem_range, h2p_pos]
    rw [hsum]
    show ((p : ℕ) : ℤ) ≠ 0
    exact_mod_cast p.property.pos.ne'

end QOU.LiftingDescent
