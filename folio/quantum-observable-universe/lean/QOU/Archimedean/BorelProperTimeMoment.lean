/-
# Borel variable ↔ proper time: the provable moment core, the Carleman
# minorant, the conditional reduction class, and the bar-covariance falsifier

Attacks A + E on the conjecture "binding Borel variable = loop proper time"
(the §5/d′ lead of the 2026-07-25 R2-core Schwinger exploration): the
Borel-plane variable of the binding OGF resummation — the C1 carrier of
`QOU.Mass.KeystoneBridgeC1Binding`, whose normalizer `N(n) = (n−1)!` is
PROVED forced by `n·N(n) = n!` — is conjecturally the SAME variable as the
Schwinger proper time `s` of the ζ-regularized photon determinant
`∫₀^∞ (ds/s)·Tr e^{−sΔ}` on Jac(Bring) (`SchwingerMeasureShape.lean`).

PROVED here (sorry-free):

* `moment_eq_factorial` — the moment identity
  `∫₀^∞ s^{n+1}·e^{−s}·ds/s = n!` (index shifted by 1 to keep ℕ-arithmetic
  subtraction-free: the `(n+1)`-st `ds/s`-moment of the unit Schwinger
  kernel is `n! = N(n+2)/(n+1) · (n+1) = N(n+2)`-adjacent; unshifted,
  `∫ s^n e^{−s} ds/s = (n−1)!` for `n ≥ 1`). The keystone-forced binding
  normalizer IS the unit-Schwinger moment.
* `carleman_minorant` + `carleman_divergence` — the Carleman terms of the
  shifted moment sequence `{k!}` dominate `1/k` (via the exact minorant
  `k! ≤ k^{2k}`), hence `Σ_k (k!)^{−1/(2k)} = ∞`: **Carleman's condition
  holds**. By the classical Carleman–Stieltjes determinacy theorem (NOT
  formalized in Mathlib; classical, cited below) the Stieltjes moment
  problem for `{k!}` is DETERMINATE — `e^{−s}·ds` is the unique positive
  measure on `(0,∞)` with these moments. The divergence proved here is the
  exact hypothesis of that theorem.
* `unit_forced` / `half_unit_fails` — with kernel `c·e^{−s}·ds/s` the
  moments are `c·(n−1)!`; the PROVED bridge identity `n·N(n) = n!`
  (`KeystoneBridgeC1Binding.period_carrier_strip`) forces `c = 1`; `c = ½`
  is impossible. Conditional on the identification, the Schwinger unit is
  pinned (the r2core §5 distinguisher, now Lean-carried).
* `kernel_moments_eq_schwinger` — the CONDITIONAL reduction (over the
  content-bearing hypothesis class below, §3b-tax, NO instance): any
  positive kernel whose `ds/s`-moments are the keystone-forced factorials
  is moment-indistinguishable from the unit Schwinger kernel. Combined
  with the (classical, unformalized) determinacy step, such a kernel IS
  `e^{−s}·ds` — which is the identification. The class fields (positivity,
  integrability, representability) are exactly the two OPEN hypotheses the
  conjecture reduces to.
* Attack-E falsifier core (generic field, §7c — pre-archimedean algebra):
  `qint_reflect` / `qfact_reflect` — the one-sided quantum integer and
  q-factorial are bar-COVARIANT with exact monomial weight:
  `[k+1]_q = q^k·[k+1]_{q⁻¹}` and `[m]_q! = q^{C(m,2)}·[m]_{q⁻¹}!`.
  `keystone_normalizer_not_bar_invariant` — for `q^{C(m,2)} ≠ 1` the
  normalizer `N_q(n) = [n−1]_q!` (m = n−1) is NOT bar-invariant, while
  loop proper time (s real) IS: the identification with the unbalanced
  kernel FAILS at `q ≠ 1` (scope-(a): the stated unbalanced form only;
  at `q = 1` the weight is 1 and nothing is refuted).
  `balanced_bar_invariance` — the exact repair: in the doubled variable
  (`q_paper = Q²`, the `BalancedQuantumTwist` convention) the identity
  `[m]_{Q²}! = (Q²)^{C(m,2)}·[m]_{Q⁻²}!` says precisely that the balanced
  normalizer `Q^{−C(m,2)}·[m]_{Q²}!` is bar-invariant — the bar-projection
  caveat under which the identification survives.

CONJECTURAL (NOT proved here — the honest residual):
* the identification itself (`conj:qdifference-kernel-prolongation-symbol`
  geometric leg); the class below names its two open hypotheses and
  carries NO instance — creating one would be laundering (§Axiomatization
  is NOT a Proof).
* the Carleman–Stieltjes determinacy THEOREM (moments + positivity +
  Carleman ⇒ uniqueness) is classical and not in Mathlib; this file
  proves its hypothesis (the divergence minorant), not the theorem.

Base rings (§7c): the moment/Carleman legs are wall-side (`ℝ` — integrals,
`Real.exp`, ordering); the bar-covariance legs are generic `[Field K]`
(algebraic inverses only, no ordering, no `ℝ`).

Probe: computations/probes/borel_propertime_moment_attack_probe.py
(exact sympy verifications of every identity here, n = 1..8, + the
subleading-pattern falsifier quadratic-vs-linear and pin numerics).

-- Ref: [leitner2026] mass-theory, conj:qdifference-kernel-prolongation-symbol;
--      docs/audits/2026-07-25-borel-propertime-attack-a-e.md;
--      docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md §5;
--      classical determinacy: B. Simon, "The classical moment problem as a
--      self-adjoint finite difference operator", Adv. Math. 137 (1998) 82–203
--      (Carleman's criterion, Stieltjes case).
-/

import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Analysis.PSeries
import QOU.Mass.QDifferenceConfluentObstruction

namespace QOU.Archimedean.BorelProperTimeMoment

open MeasureTheory QOU.Mass.QDifferenceConfluentObstruction

/-! ## Attack A — the provable moment core (wall-side, ℝ) -/

/-- **The moment identity.** The `(n+1)`-st `ds/s`-moment of the unit
(`c = 1`) Schwinger kernel is exactly `n!`:
`∫₀^∞ s^{n+1}·e^{−s}·ds/s = Γ(n+1) = n!`. Unshifted this is
`∫ s^n e^{−s} ds/s = (n−1)!` for `n ≥ 1` — the keystone-forced binding
normalizer `N(n) = (n−1)!` (`KeystoneBridgeC1Binding`) IS the moment data
of the loop's proper-time kernel. Index shifted by 1 so ℕ-arithmetic stays
subtraction-free. -/
theorem moment_eq_factorial (n : ℕ) :
    ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Real.exp (-s) / s
      = (n.factorial : ℝ) := by
  have h1 : ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Real.exp (-s) / s
      = ∫ s in Set.Ioi (0:ℝ), Real.exp (-s) * s ^ (((n:ℝ) + 1) - 1) := by
    refine setIntegral_congr_fun measurableSet_Ioi ?_
    intro s hs
    have hs0 : (0:ℝ) < s := hs
    have he : ((n:ℝ) + 1) - 1 = ((n : ℕ) : ℝ) := by ring
    simp only [he, Real.rpow_natCast, pow_succ]
    field_simp [hs0.ne']
  rw [h1, ← Real.Gamma_eq_integral (by positivity : (0:ℝ) < (n:ℝ) + 1)]
  exact_mod_cast Real.Gamma_nat_eq_factorial n

/-- **The Carleman minorant.** The Carleman term of the shifted moment
sequence `{k!}` dominates the harmonic term: `1/k ≤ (k!)^{−1/(2k)}`, from
the exact bound `k! ≤ k^{2k}`. This is the quantitative heart of
Carleman's condition for `{k!}`. -/
theorem carleman_minorant (k : ℕ) (hk : 1 ≤ k) :
    (1 : ℝ) / k ≤ (k.factorial : ℝ) ^ (-(1 / (2 * (k : ℝ)))) := by
  have hk0 : (0:ℝ) < k := by exact_mod_cast hk
  have hfac0 : (0:ℝ) ≤ (k.factorial : ℝ) := by positivity
  have hx : (0:ℝ) ≤ 1 / (2 * (k:ℝ)) := by positivity
  have hnat : k.factorial ≤ k ^ (2 * k) :=
    le_trans (Nat.factorial_le_pow k) (Nat.pow_le_pow_right hk (by omega))
  have hle : (k.factorial : ℝ) ≤ (k:ℝ) ^ (2 * k) := by exact_mod_cast hnat
  have hax : (k.factorial : ℝ) ^ (1 / (2 * (k:ℝ))) ≤ (k:ℝ) := by
    have h1 : (k.factorial : ℝ) ^ (1 / (2 * (k:ℝ)))
        ≤ ((k:ℝ) ^ (2 * k)) ^ (1 / (2 * (k:ℝ))) :=
      Real.rpow_le_rpow hfac0 hle hx
    have h2 : ((k:ℝ) ^ (2 * k) : ℝ) = (k:ℝ) ^ ((2 * k : ℕ) : ℝ) :=
      (Real.rpow_natCast _ _).symm
    have h3 : ((k:ℝ) ^ ((2 * k : ℕ) : ℝ)) ^ (1 / (2 * (k:ℝ)))
        = (k:ℝ) ^ (((2 * k : ℕ) : ℝ) * (1 / (2 * (k:ℝ)))) :=
      (Real.rpow_mul (le_of_lt hk0) _ _).symm
    have h4 : ((2 * k : ℕ) : ℝ) * (1 / (2 * (k:ℝ))) = 1 := by
      have hne : (2 * (k:ℝ)) ≠ 0 := by positivity
      push_cast
      field_simp
    rw [h2, h3, h4, Real.rpow_one] at h1
    exact h1
  have haxpos : (0:ℝ) < (k.factorial : ℝ) ^ (1 / (2 * (k:ℝ))) :=
    Real.rpow_pos_of_pos (by positivity) _
  have hdiv := one_div_le_one_div_of_le haxpos hax
  rw [Real.rpow_neg hfac0, ← one_div]
  exact hdiv

/-- **Carleman divergence.** `Σ_k (k!)^{−1/(2k)} = ∞` (stated as
non-summability): the Carleman condition for the Stieltjes moment problem
of `{k!}` HOLDS. By the classical Carleman–Stieltjes determinacy theorem
(Simon 1998; NOT formalized in Mathlib — this lemma proves its exact
hypothesis) the problem is determinate: `e^{−s}·ds` is the UNIQUE positive
measure on `(0,∞)` with moments `{k!}`. -/
theorem carleman_divergence :
    ¬ Summable (fun k : ℕ => (k.factorial : ℝ) ^ (-(1 / (2 * (k : ℝ))))) := by
  intro hsum
  have h : Summable (fun k : ℕ => (1:ℝ) / k) := by
    refine Summable.of_nonneg_of_le (fun k => by positivity)
      (fun k => ?_) hsum
    rcases Nat.eq_zero_or_pos k with hk | hk
    · subst hk
      simp
    · exact carleman_minorant k hk
  exact Real.not_summable_one_div_natCast h

/-- **Unit forcing.** With kernel `c·e^{−s}·ds/s` the moments are
`c·(n−1)!`; the PROVED keystone identity `n·N(n) = n!` (shifted:
`(n+1)·N(n+1) = (n+1)!` with `N(n+1) = c·n!`) forces `c = 1` exactly.
Conditional on the Borel-variable = proper-time identification, the
Schwinger measure unit is pinned — the r2core §5 distinguisher. -/
theorem unit_forced (c : ℝ) (n : ℕ)
    (h : ((n:ℝ) + 1) * (c * n.factorial) = ((n + 1).factorial : ℝ)) :
    c = 1 := by
  have hf : (((n + 1).factorial : ℕ) : ℝ) = ((n:ℝ) + 1) * n.factorial := by
    rw [Nat.factorial_succ]; push_cast; ring
  have hn : ((n:ℝ) + 1) ≠ 0 := by positivity
  have hfn : (n.factorial : ℝ) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero n
  rw [hf] at h
  have h2 : c * (n.factorial : ℝ) = n.factorial := mul_left_cancel₀ hn h
  have h3 : c * (n.factorial : ℝ) = 1 * n.factorial := by
    rw [h2, one_mul]
  exact mul_right_cancel₀ hfn h3

/-- **The rival unit `c = ½` is impossible** against the proved keystone
identity — the exact `n!/2 ≠ n!` distinguisher, for every `n`. -/
theorem half_unit_fails (n : ℕ) :
    ¬ (((n:ℝ) + 1) * ((1/2 : ℝ) * n.factorial) = ((n + 1).factorial : ℝ)) := by
  intro h
  have := unit_forced (1/2) n h
  norm_num at this

/-! ## The conditional reduction class (§3b-tax; content-bearing; NO
instance — the fields are the conjecture's two open hypotheses) -/

/-- **Conjecture carrier (primary; no instance exists or may be created).**
The binding Borel resummation kernel — the weight `K_b(s)·ds` realizing the
keystone-forced normalizer as `N(n+1) = n! = ∫ s^{n+1}·K_b(s)·ds/s` — is a
positive measure on `(0,∞)` with exactly the factorial `ds/s`-moments.
These fields are the two OPEN hypotheses that Attack A reduces the
conjecture "binding Borel variable = loop proper time" to:

* `positive` + `integrable` — the substrate resummation weight is a genuine
  positive measure (open: no corpus result establishes it; the C1 carrier
  coefficients `I(n)/n!` are NOT themselves a Stieltjes moment sequence —
  log-convexity fails at `m = 2` — so this is a statement about the
  kernel, not the coefficients);
* `moments` — its moments are the keystone-forced factorials (open: the
  keystone forces the NORMALIZER values `(n−1)!`, not that they arise as
  the moments of the substrate's own kernel).

Given both, `kernel_moments_eq_schwinger` below (proved) plus classical
Carleman–Stieltjes determinacy (`carleman_divergence` proves its
hypothesis; the theorem itself is classical, unformalized) force
`K_b(s)·ds = e^{−s}·ds` — the identification. Creating an `instance` of
this class would launder the conjecture (§Axiomatization is NOT a Proof);
none exists. -/
class BindingKernelSchwingerRepresentation (Kb : ℝ → ℝ) : Prop where
  positive : ∀ s : ℝ, 0 < s → 0 ≤ Kb s
  integrable : ∀ n : ℕ,
    IntegrableOn (fun s : ℝ => s ^ (n + 1) * Kb s / s) (Set.Ioi 0)
  moments : ∀ n : ℕ,
    ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Kb s / s = (n.factorial : ℝ)

/-- **The reduction, proved conditionally.** Any kernel satisfying the
hypothesis class is moment-indistinguishable from the unit Schwinger
kernel: every `ds/s`-moment agrees. The remaining gap to
`K_b = e^{−s}` (a.e.) is exactly the classical determinacy step whose
Carleman hypothesis `carleman_divergence` proves — so the conjecture is
reduced to the class's two named hypotheses, nothing else. -/
theorem kernel_moments_eq_schwinger (Kb : ℝ → ℝ)
    [BindingKernelSchwingerRepresentation Kb] (n : ℕ) :
    ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Kb s / s
      = ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Real.exp (-s) / s := by
  rw [BindingKernelSchwingerRepresentation.moments (Kb := Kb) n,
    moment_eq_factorial]

/-! ## Attack E — the bar-covariance falsifier core (generic field, §7c) -/

section BarCovariance

variable {K : Type*} [Field K]

/-- **Bar reflection of the one-sided quantum integer.**
`[k+1]_q = q^k·[k+1]_{q⁻¹}` — the one-sided `[k]_q = 1 + q + … + q^{k−1}`
(the corpus convention, `QDifferenceConfluentObstruction.qint`) is
bar-covariant with monomial weight. Index stated at `k+1` so the exponent
`k` is subtraction-free. -/
theorem qint_reflect (q : K) (hq : q ≠ 0) (k : ℕ) :
    qint q (k + 1) = q ^ k * qint q⁻¹ (k + 1) := by
  have hrefl := Finset.sum_range_reflect (fun j => q ^ j) (k + 1)
  rw [qint, qint, ← hrefl, Finset.mul_sum]
  refine Finset.sum_congr rfl fun i hi => ?_
  have hik : i ≤ k := Nat.lt_succ_iff.mp (Finset.mem_range.mp hi)
  have h1 : k + 1 - 1 - i = k - i := by omega
  rw [h1, inv_pow, eq_mul_inv_iff_mul_eq₀ (pow_ne_zero i hq), ← pow_add]
  congr 1
  omega

/-- **Bar reflection of the q-factorial.**
`[m]_q! = q^{C(m,2)}·[m]_{q⁻¹}!` with `C(m,2) = m(m−1)/2`. Applied to the
keystone normalizer `N_q(n) = [n−1]_q!` (`m = n−1`): the binding q-Borel
normalizer is bar-COVARIANT with exact weight `q^{C(n−1,2)}` — while the
loop proper time (`s` real) is bar-INVARIANT. This is the Attack-E
falsifier: the identification with the unbalanced kernel fails at `q ≠ 1`
(scope-(a); at `q = 1` the weight is 1 and the classical identification is
untouched). -/
theorem qfact_reflect (q : K) (hq : q ≠ 0) (n : ℕ) :
    qfact q n = q ^ n.choose 2 * qfact q⁻¹ n := by
  induction n with
  | zero => simp [qfact]
  | succ m ih =>
    have h1 : qfact q (m + 1) = qint q (m + 1) * qfact q m := rfl
    have h2 : qfact q⁻¹ (m + 1) = qint q⁻¹ (m + 1) * qfact q⁻¹ m := rfl
    have hch : (m + 1).choose 2 = m + m.choose 2 := by
      rw [Nat.choose_succ_succ, Nat.choose_one_right]
    rw [h1, h2, qint_reflect q hq m, ih, hch, pow_add]
    ring

/-- **The falsifier fires.** If the bar weight is nontrivial
(`q^{C(m,2)} ≠ 1`) and the reflected factorial is nonzero, the one-sided
q-factorial is NOT bar-invariant: `[m]_q! ≠ [m]_{q⁻¹}!`. For the keystone
normalizer (`m = n−1`) the weight is nontrivial for every `n ≥ 3` at
generic `q ≠ 1` — the unbalanced-kernel identification is refuted at
`q ≠ 1` (scope-(a): this stated form only). -/
theorem keystone_normalizer_not_bar_invariant (q : K) (hq : q ≠ 0) (m : ℕ)
    (hw : q ^ m.choose 2 ≠ 1) (hf : qfact q⁻¹ m ≠ 0) :
    qfact q m ≠ qfact q⁻¹ m := by
  intro h
  have hr := qfact_reflect q hq m
  rw [h] at hr
  have := (mul_left_eq_self₀).mp hr.symm
  rcases this with h1 | h1
  · exact hw h1
  · exact hf h1

/-- **The balanced repair (the bar-projection caveat, exact).** In the
doubled variable (`q_paper = Q²`, the `BalancedQuantumTwist` convention)
the reflection identity reads `[m]_{Q²}! = (Q²)^{C(m,2)}·[m]_{Q⁻²}!` —
which is precisely the statement that the BALANCED normalizer
`Q^{−C(m,2)}·[m]_{Q²}!` is bar-invariant (`Q ↦ Q⁻¹`): dividing both sides
by `Q^{C(m,2)}` matches term for term. The identification survives iff the
conjecture's kernel is read in this balanced convention — matching the
proper time's reality (bar-invariance), with vanishing first-order
`q`-correction (probe E3). -/
theorem balanced_bar_invariance (q : K) (hq : q ≠ 0) (m : ℕ) :
    qfact (q ^ 2) m = (q ^ 2) ^ m.choose 2 * qfact ((q⁻¹) ^ 2) m := by
  rw [inv_pow]
  exact qfact_reflect (q ^ 2) (pow_ne_zero 2 hq) m

end BarCovariance

end QOU.Archimedean.BorelProperTimeMoment
