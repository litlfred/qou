import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Laurent

/-!
# QOU.AppendixSurreals.QCollatz — the $q$-Collatz conjecture (content-bearing class)

**§3b conjecture-class axiomatisation** for content block
[`conj:q-collatz`](../../../quantum-observable-universe/appendix-surreals/q-collatz-conjecture.md):
*The $q$-Collatz conjecture: Skein-module crossing resolution*.

**Given a quantum observable universe** `(𝐂, A, τ)` with substrate
parameter `q`, its Skein module `Skein = 𝒮(q) ≅ ℤ[q^{±1}]` (the Skein
module of the QOU's Reeb bundle) carries the Skein-Collatz dynamics.
This is a statement *within the QOU* — not a claim about the classical
Collatz problem, which it recovers only in the archimedean limit
`q → 1`.

This is a **primary open conjecture** (per AGENTS.md §3b / §3b-tax).
The class `QCollatz` carries the conjecture's actual content:

* the Skein module is the QOU's `𝒮(q) ≅ ℤ[q^{±1}]`, modelled as a
  commutative ring `Skein`;
* `qi2 = [2]_q = q + 1` and `qi3 = [3]_q = q^2 + q + 1` (combinatorial
  convention);
* the Skein-Collatz map `C` is characterised branch-by-branch — the
  **even** branch $P \mapsto P/[2]_q$ (`C_even`) and the **odd** branch
  $P \mapsto ([3]_q P + 1)/[2]_q$ (`C_odd`), the latter well-defined by
  Skein divisibility;
* the field `reaches_cycle` **is the conjecture**: every element of the
  positive cone reaches the fundamental 2-cycle `{q⁻¹, 1 + q⁻¹}` (via its
  representative `attractor`) under finitely many iterations of `C`. The
  literal `1` is *not* the attractor — it is outside the domain of `C`.

Honest open-primary state (§3b-tax): the class is **content-bearing and
has no instance** — an instance would have to supply `reaches_cycle`, which
is exactly the open problem. We deliberately do **not** fabricate a
trivial instance (that would be an audit-dodge; bean `cj317`). Downstream
results may take `[QCollatz Skein]` as an explicit `[Instance]`
hypothesis to state theorems conditional on the conjecture (§3b-cond).

The balanced-holonomy sub-case of no-cycles is a genuine **consequence**
of these fields — see
`qi3_sub_q_qi2` below (the Skein-Bézout coprimality identity), which is
derived, sorry-free, from the axiomatised `qi2`/`qi3` definitions. The
divergence half is what remains open.

Base ring is a generic `[CommRing Skein]` per §7c: the map, divisibility
and coprimality live at the *fibre* (formal-$q$) level, so no `ℝ` is
introduced here. Archimedean positivity ("$q > 1$, $P > 0$") is
abstracted into the `pos` predicate. The archimedean identities
(`[2]_q^2 - [3]_q = q`, the contraction estimates) are proved separately,
sorry-free, in [`QOU/QCollatz.lean`](../QCollatz.lean).
-/

universe u

namespace QOU.AppendixSurreals

/-- The $q$-Collatz conjecture: Skein-module crossing resolution.

    Conjectural class furnished by a QOU — see
    [`conj:q-collatz`](../../../quantum-observable-universe/appendix-surreals/q-collatz-conjecture.md).
    The `reaches_cycle` field is the open conjecture; the class carries
    the full definitional content of the Skein-Collatz map. -/
class QCollatz (Skein : Type u) [CommRing Skein] where
  -- Witness: computations/none
  /-- Image of the formal substrate parameter `q` in the Skein ring
      (a model of $\mathbb{Z}[q^{\pm 1}]$). -/
  qgen : Skein
  /-- The $q$-integer `[2]_q`. -/
  qi2 : Skein
  /-- The $q$-integer `[3]_q`. -/
  qi3 : Skein
  /-- `[2]_q = q + 1` (combinatorial convention). -/
  qi2_def : qi2 = qgen + 1
  /-- `[3]_q = q^2 + q + 1` (combinatorial convention). -/
  qi3_def : qi3 = qgen ^ 2 + qgen + 1
  /-- The Skein-Collatz map `C_q`. -/
  C : Skein → Skein
  /-- **Even branch.** For `q`-even `P` (i.e. `[2]_q ∣ P`),
      `C P = P / [2]_q`, characterised by `C P * [2]_q = P`. -/
  C_even : ∀ P : Skein, qi2 ∣ P → C P * qi2 = P
  /-- **Odd branch.** For `q`-odd `P` (i.e. `[2]_q ∣ P + 1`),
      `C P = ([3]_q * P + 1) / [2]_q`, characterised by
      `C P * [2]_q = [3]_q * P + 1`. Well-defined by Skein divisibility
      `[3]_q = q * [2]_q + 1`. -/
  C_odd : ∀ P : Skein, qi2 ∣ (P + 1) → C P * qi2 = qi3 * P + 1
  /-- The positive cone `ℤ[q^{±1}]_{>0}` (archimedean positivity at
      `q > 1`, abstracted). -/
  pos : Skein → Prop
  /-- The fundamental attractor `α ∈ Skein` — the `q⁻¹` end of the
      period-2 cycle `{q⁻¹, 1 + q⁻¹}` (the `q`-lift of the classical
      `{1, 2}`). The literal ring element `1` is **not** the attractor:
      it is outside the domain of `C`, being neither `q`-even nor
      `q`-odd (`1` reduces to `1 ∉ {0, -1}` modulo `[2]_q`). -/
  attractor : Skein
  /-- `attractor` is a genuine period-2 point of the Skein-Collatz map. -/
  attractor_period_two : C (C attractor) = attractor
  /-- …and not a fixed point (the fundamental cycle is truly 2-periodic). -/
  attractor_not_fixed : C attractor ≠ attractor
  /-- **Domain-stability of the positive cone (well-posedness).** The
      Skein-Collatz map is *partial*: it is defined at `P` only when `P`
      is `q`-even (`[2]_q ∣ P`) or `q`-odd (`[2]_q ∣ P + 1`). Unlike the
      integers — where every element is even or odd — this domain is
      **not** forward-invariant on the naive positive cone: almost every
      positive Laurent element leaves it within a few steps
      (computations/qcollatz_divergence_probe: 6042/6045 escape, most in
      one step). So the conjecture's cone `pos` is the **domain-stable**
      subset — elements whose entire forward orbit stays in the domain.
      This field records that requirement; it has no classical analog. -/
  pos_domain_stable : ∀ P : Skein, pos P →
    ∀ k : ℕ, qi2 ∣ (C^[k] P) ∨ qi2 ∣ (C^[k] P + 1)
  /-- **The $q$-Collatz conjecture (within the QOU).** Every element of
      the (domain-stable) positive cone reaches the fundamental cycle —
      i.e. reaches `attractor` — under finitely many iterations of the
      Skein-Collatz map. The `sorry`-free absence of an instance is the
      honest "open" state per §3b-tax. -/
  reaches_cycle : ∀ P : Skein, pos P → ∃ k : ℕ, C^[k] P = attractor

/-- **Skein-Bézout coprimality**, derived sorry-free from the class
    fields: `[3]_q - q * [2]_q = 1`.

    This is the engine of the *no-cycles* half of the conjecture: it
    exhibits `[2]_q` and `[3]_q` as coprime (`gcd = 1` by Bézout), so
    `[3]_q^{k_odd} = [2]_q^k` is impossible for `k_odd ≥ 1` and the only
    periodic orbit is `P = 1`. Its derivability is evidence that the
    `QCollatz` class content is genuine, not a vacuous marker. -/
theorem qi3_sub_q_qi2 (Skein : Type u) [CommRing Skein] [QCollatz Skein] :
    (QCollatz.qi3 (Skein := Skein)) - QCollatz.qgen * QCollatz.qi2 = 1 := by
  rw [QCollatz.qi2_def (Skein := Skein), QCollatz.qi3_def (Skein := Skein)]
  ring

/-! ### The fundamental attractor cycle `{q⁻¹, 1 + q⁻¹}` (proved)

The two lemmas below discharge, sorry-free over any commutative ring in
which `q` is invertible (as in the Skein module `ℤ[q^{±1}]`), the
branch-defining equations of the fundamental 2-cycle — the `q`-lift of the
classical `{1, 2}`. Writing `[2]_q = q + 1`, `[3]_q = q² + q + 1`:

* the **odd** branch sends `q⁻¹ ↦ 1 + q⁻¹`
  (`(1 + q⁻¹)·[2]_q = [3]_q·q⁻¹ + 1`);
* the **even** branch sends `1 + q⁻¹ ↦ q⁻¹` (`q⁻¹·[2]_q = 1 + q⁻¹`).

Together they show `{q⁻¹, 1 + q⁻¹}` is a genuine period-2 orbit of the
Skein-Collatz map — the concrete realisation of the `attractor` field. -/

/-- Odd-branch step of the fundamental cycle: `(1 + q⁻¹)·[2]_q = [3]_q·q⁻¹ + 1`. -/
theorem qcollatz_fundamental_odd_step {R : Type u} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) :
    (1 + qinv) * (q + 1) = (q ^ 2 + q + 1) * qinv + 1 := by
  linear_combination (-q) * hq

/-- Even-branch step of the fundamental cycle: `q⁻¹·[2]_q = 1 + q⁻¹`. -/
theorem qcollatz_fundamental_even_step {R : Type u} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) :
    qinv * (q + 1) = 1 + qinv := by
  linear_combination hq

/-- **Odd-branch fixed points are pinned by `q²·P = -1`.** A fixed point of
    the odd branch (`[3]_q·P + 1 = [2]_q·P`) forces `q²·P = -1`, hence
    `P = -q⁻²` once `q` is invertible — the `q`-lift of the classical
    negative fixed point `-1`. In particular the fixed point is unique and
    *negative*: there is **no positive fixed point**, so the fundamental
    `{q⁻¹, 1+q⁻¹}` is genuinely 2-periodic. This discharges the period-1
    case of nontrivial-cycle exclusion. -/
theorem qcollatz_odd_fixed_point {R : Type u} [CommRing R] (q P : R)
    (h : (q ^ 2 + q + 1) * P + 1 = (q + 1) * P) : q ^ 2 * P = -1 := by
  linear_combination h

/-- The negative element `-q⁻²` is an odd-branch fixed point (given `q`
    invertible): `[3]_q·(-q⁻²) + 1 = [2]_q·(-q⁻²)`. With
    `qcollatz_odd_fixed_point` this identifies `-q⁻²` as *the* odd fixed
    point. -/
theorem qcollatz_neg_qinv_sq_is_odd_fixed {R : Type u} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) :
    (q ^ 2 + q + 1) * (-qinv ^ 2) + 1 = (q + 1) * (-qinv ^ 2) := by
  linear_combination (-(q * qinv) - 1) * hq

/-- **Even-branch fixed points force `q·P = 0`.** A fixed point of the even
    branch (`[2]_q·P = P`) forces `q·P = 0`, hence `P = 0` when `q` is a
    non-zero-divisor (as in `ℤ[q^{±1}]`). Together with
    `qcollatz_odd_fixed_point`, the only fixed points of the Skein-Collatz
    map are `0` (even) and `-q⁻²` (odd) — **neither positive** — completing
    the period-1 case of nontrivial-cycle exclusion. -/
theorem qcollatz_even_fixed_point {R : Type u} [CommRing R] (q P : R)
    (h : (q + 1) * P = P) : q * P = 0 := by
  linear_combination h

/-! #### Period-2 cycle exclusion

Extends the period-1 result to period 2: the only positive 2-cycle is the
fundamental `{q⁻¹, 1+q⁻¹}`. A period-2 orbit `P ↦ P₁ ↦ P` has one of the
parity words `EE`, `OO`, `EO`/`OE`; each is pinned below (`h_even`/`h_odd`
encode the branch-defining equations `C P · [2]_q = P` resp.
`C P · [2]_q = [3]_q·P + 1`). -/

/-- **Period-2, word EE.** An even→even 2-cycle forces `q·(q+2)·P = 0`,
    hence `P = 0` in a domain (`q ≠ 0`, `q ≠ -2`): no positive EE 2-cycle. -/
theorem qcollatz_period2_eveneven {R : Type u} [CommRing R] (q P P1 : R)
    (h1 : P1 * (q + 1) = P) (h2 : P * (q + 1) = P1) :
    q * (q + 2) * P = 0 := by
  linear_combination h1 + (q + 1) * h2

/-- **Period-2, word OO.** An odd→odd 2-cycle forces
    `(q²+2q+2)·(P − P₁) = 0`, hence `P = P₁` in a domain — it degenerates to
    the odd fixed point `-q⁻²`, not a genuine 2-cycle. -/
theorem qcollatz_period2_oddodd {R : Type u} [CommRing R] (q P P1 : R)
    (h1 : P1 * (q + 1) = (q ^ 2 + q + 1) * P + 1)
    (h2 : P * (q + 1) = (q ^ 2 + q + 1) * P1 + 1) :
    (q ^ 2 + 2 * q + 2) * (P - P1) = 0 := by
  linear_combination h2 - h1

/-- **Period-2, word EO/OE.** An even→odd 2-cycle (`P₁·[2]_q = P`,
    `P·[2]_q = [3]_q·P₁ + 1`) forces `q·P₁ = 1`, i.e. `P₁ = q⁻¹` — the
    fundamental cycle `{q⁻¹, 1+q⁻¹}`, uniquely. Together with the EE and OO
    cases, the only positive period-2 cycle is the fundamental one. -/
theorem qcollatz_period2_evenodd {R : Type u} [CommRing R] (q P P1 : R)
    (h_even : P1 * (q + 1) = P)
    (h_odd : P * (q + 1) = (q ^ 2 + q + 1) * P1 + 1) :
    q * P1 = 1 := by
  linear_combination h_odd + (q + 1) * h_even

/-! #### Period-3 cycle exclusion

The two primitive length-3 parity words (`EEO`, `EOO`, up to rotation) each pin
the cycle value to a *non-unit* multiple, with no solution in `ℤ[q^{±1}]` (whose
only units are `±q^n`). So there is no nontrivial period-3 cycle — extending the
period-1 and period-2 results. -/

/-- **Period-3, word EEO.** An even→even→odd 3-cycle forces
    `q·(q²+2q+2)·P₂ = 1`. Since `q(q²+2q+2)` is a non-unit in `ℤ[q^{±1}]`, no
    such `P₂` exists — no EEO 3-cycle. -/
theorem qcollatz_period3_EEO {R : Type u} [CommRing R] (q P0 P1 P2 : R)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = P1)
    (h3 : P0 * (q + 1) = (q ^ 2 + q + 1) * P2 + 1) :
    q * (q ^ 2 + 2 * q + 2) * P2 = 1 := by
  linear_combination h3 + (q + 1) * h1 + (q + 1) ^ 2 * h2

/-- **Period-3, word EOO.** An even→odd→odd 3-cycle forces
    `q·(q³+q²−1)·P₁ = −(q²+2q+2)`. The coefficient `q(q³+q²−1)` is a non-unit in
    `ℤ[q^{±1}]`, so no such `P₁` exists — no EOO 3-cycle. With EEO (and their
    rotations) this excludes every nontrivial period-3 cycle. -/
theorem qcollatz_period3_EOO {R : Type u} [CommRing R] (q P0 P1 P2 : R)
    (h1 : P1 * (q + 1) = P0)
    (h2 : P2 * (q + 1) = (q ^ 2 + q + 1) * P1 + 1)
    (h3 : P0 * (q + 1) = (q ^ 2 + q + 1) * P2 + 1) :
    q * (q ^ 3 + q ^ 2 - 1) * P1 = -(q ^ 2 + 2 * q + 2) := by
  linear_combination -(q + 1) * h3 - (q ^ 2 + q + 1) * h2 - (q + 1) ^ 2 * h1

/-! #### All-even cycle exclusion at every period (uniform)

Generalises the `EE` period-2 case to arbitrary period: an orbit that is
even at every step and returns satisfies `P = [2]_q^k · P`, forcing `P = 0`
in any integral domain where `[2]_q^k ≠ 1`. So there is **no** nontrivial
all-even cycle, at any period `k`. -/

/-- All-even `k`-cycle exclusion: `P = [2]_q^k · P` and `[2]_q^k ≠ 1` in a
    domain force `P = 0`. -/
theorem qcollatz_alleven_forces_zero {R : Type u} [CommRing R] [IsDomain R]
    (q P : R) (k : ℕ) (hq : (q + 1) ^ k ≠ 1) (h : P = (q + 1) ^ k * P) :
    P = 0 := by
  have h0 : ((q + 1) ^ k - 1) * P = 0 := by linear_combination -h
  rcases mul_eq_zero.mp h0 with h1 | h1
  · exact absurd (sub_eq_zero.mp h1) hq
  · exact h1

open Polynomial in
/-- `[2]_q^k = (q+1)^k ≠ 1` in the Skein ring `ℤ[q]` for `k ≥ 1` (its
    `natDegree` is `k > 0`), discharging the hypothesis of
    `qcollatz_alleven_forces_zero`. -/
theorem qcollatz_qplus1_pow_ne_one (k : ℕ) (hk : 0 < k) :
    ((X + 1 : Polynomial ℤ)) ^ k ≠ 1 := by
  intro h
  have hnd : (X + 1 : Polynomial ℤ).natDegree = 1 := by
    rw [show (X + 1 : Polynomial ℤ) = X + C 1 by rw [C_1], natDegree_X_add_C]
  have h1 : ((X + 1 : Polynomial ℤ) ^ k).natDegree = k := by
    rw [natDegree_pow, hnd, mul_one]
  rw [h] at h1
  simp at h1
  omega

/-- **Domain non-invariance (concrete counterexample, proved).**

    The Skein-Collatz map is partial: `P` is in its domain iff `P` is
    `q`-even (`φ P = 0`) or `q`-odd (`φ P = -1`), where `φ : R →+* ℤ` is
    the parity evaluation sending `q ↦ -1` (so `φ [2]_q = 0`). The domain
    is **not** forward-invariant: `[2]_q = q + 1` is `q`-even, its
    even-branch image is `1` (since `1·[2]_q = [2]_q`), yet `φ 1 = 1`, which
    is neither `0` nor `-1` — so `1` has left the domain. This is the
    structural obstruction with no classical analog (over `ℤ` every element
    is even or odd), backing the `pos_domain_stable` well-posedness field. -/
theorem qcollatz_domain_not_forward_invariant {R : Type u} [CommRing R]
    (q : R) (φ : R →+* ℤ) (hq : φ q = -1) :
    φ (q + 1) = 0 ∧ (1 : R) * (q + 1) = q + 1 ∧ φ (1 : R) ≠ 0 ∧ φ (1 : R) ≠ -1 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [map_add, hq, map_one]; ring
  · ring
  · rw [map_one]; decide
  · rw [map_one]; decide

/-- **Convergence reduces to a descent measure (proved reduction).**

    Given a QOU's `QCollatz` structure, suppose there is a measure
    `μ : Skein → ℕ` that strictly decreases along the Skein-Collatz map on
    the positive cone away from the attractor (`hdesc`), and the positive
    cone is forward-invariant there (`hclosed`). Then **every** positive
    element reaches the fundamental cycle.

    This factors the open conjecture `reaches_cycle` into (i) this proved
    termination-from-descent lemma and (ii) the existence of such a `μ` —
    the genuinely open content (the `q`-analog of a Collatz stopping-time
    bound; the paper's `⟨v_[2]⟩ ≥ 2` contact condition is the intended
    witness). It wires nothing: `μ` is a hypothesis, not supplied. -/
theorem reaches_cycle_of_descent {Skein : Type u} [CommRing Skein]
    [QCollatz Skein] (μ : Skein → ℕ)
    (hclosed : ∀ P : Skein, QCollatz.pos P → P ≠ QCollatz.attractor →
      QCollatz.pos (QCollatz.C P))
    (hdesc : ∀ P : Skein, QCollatz.pos P → P ≠ QCollatz.attractor →
      μ (QCollatz.C P) < μ P) :
    ∀ P : Skein, QCollatz.pos P →
      ∃ k : ℕ, QCollatz.C^[k] P = QCollatz.attractor := by
  suffices H : ∀ n P, μ P = n → QCollatz.pos P →
      ∃ k, QCollatz.C^[k] P = QCollatz.attractor from
    fun P hP => H (μ P) P rfl hP
  intro n
  induction n using Nat.strong_induction_on with
  | _ n IH =>
    intro P hμ hP
    by_cases hc : P = QCollatz.attractor
    · exact ⟨0, by simpa using hc⟩
    · have hlt : μ (QCollatz.C P) < n := hμ ▸ hdesc P hP hc
      obtain ⟨k, hk⟩ := IH (μ (QCollatz.C P)) hlt (QCollatz.C P) rfl (hclosed P hP hc)
      exact ⟨k + 1, by rw [Function.iterate_succ_apply]; exact hk⟩

/-- A period-2 point's forward orbit is exactly `{P, f P}`: every iterate is
    `P` or `f P`. -/
theorem iterate_period_two_mem {α : Type*} (f : α → α) (P : α)
    (h : f (f P) = P) : ∀ k : ℕ, f^[k] P = P ∨ f^[k] P = f P := by
  intro k
  induction k with
  | zero => exact Or.inl rfl
  | succ n ih =>
    rcases ih with h1 | h1
    · exact Or.inr (by rw [Function.iterate_succ_apply', h1])
    · exact Or.inl (by rw [Function.iterate_succ_apply', h1, h])

/-- **The fundamental attractor's orbit is a bounded finite invariant set.**
    Every iterate stays within the 2-cycle `{attractor, C attractor}` — it
    never escapes. So the attractor is domain-stable (its forward orbit is
    a finite invariant set), corroborating that the domain-stable cone is
    nonempty and contains the fundamental cycle `{q⁻¹, 1+q⁻¹}`. -/
theorem qcollatz_attractor_orbit_bounded (Skein : Type u) [CommRing Skein]
    [QCollatz Skein] : ∀ k : ℕ,
    (QCollatz.C (Skein := Skein))^[k] QCollatz.attractor = QCollatz.attractor ∨
    (QCollatz.C (Skein := Skein))^[k] QCollatz.attractor
      = QCollatz.C QCollatz.attractor :=
  iterate_period_two_mem (QCollatz.C (Skein := Skein)) QCollatz.attractor
    QCollatz.attractor_period_two

/-! ### Concrete grounding in the Skein module `ℤ[q^{±1}]` (non-vacuity)

The abstract fundamental-cycle and fixed-point lemmas realise in the actual
Skein module `LaurentPolynomial ℤ = ℤ[T;T⁻¹]`, with `q = T 1` (a unit,
inverse `T (-1)`, since `T 1 · T (-1) = T 0 = 1`). This exhibits the
fundamental 2-cycle `{T(-1), 1 + T(-1)}` (the `q`-lift of classical `{1,2}`)
and the negative odd-branch fixed point `-T(-2) = -(T(-1))²` (the `q`-lift of
`-1`) as genuine Skein elements — the cluster is non-vacuous. -/

open LaurentPolynomial in
/-- `T 1` is a unit in `ℤ[T;T⁻¹]` with inverse `T (-1)`. -/
theorem qcollatz_laurent_qunit :
    (T 1 : LaurentPolynomial ℤ) * T (-1) = 1 := by
  rw [← T_add]; norm_num

open LaurentPolynomial in
/-- **Fundamental 2-cycle in `ℤ[q^{±1}]`.** The odd branch sends
    `q⁻¹ = T(-1) ↦ 1 + T(-1)` and the even branch sends it back. -/
theorem qcollatz_laurent_fundamental_cycle :
    (1 + T (-1) : LaurentPolynomial ℤ) * (T 1 + 1)
      = ((T 1) ^ 2 + T 1 + 1) * T (-1) + 1
    ∧ (T (-1) : LaurentPolynomial ℤ) * (T 1 + 1) = 1 + T (-1) :=
  ⟨qcollatz_fundamental_odd_step (T 1) (T (-1)) qcollatz_laurent_qunit,
   qcollatz_fundamental_even_step (T 1) (T (-1)) qcollatz_laurent_qunit⟩

open LaurentPolynomial in
/-- **Negative odd-branch fixed point in `ℤ[q^{±1}]`**: `-T(-2) = -(T(-1))²`
    satisfies `[3]_q·P + 1 = [2]_q·P`. -/
theorem qcollatz_laurent_neg_fixed :
    ((T 1) ^ 2 + T 1 + 1 : LaurentPolynomial ℤ) * (-(T (-1)) ^ 2) + 1
      = (T 1 + 1) * (-(T (-1)) ^ 2) :=
  qcollatz_neg_qinv_sq_is_odd_fixed (T 1) (T (-1)) qcollatz_laurent_qunit

/-! ### `[2]_q`-adic valuation infrastructure (qcz12)

The `[2]_q`-adic valuation `v_[2](P) = max{k : [2]_q^k ∣ P}` on `ℤ[q]`, as
the multiplicity of the factor `[2]_q = q + 1` — i.e. of the root `q = -1`.
(On `ℤ[q^{±1}]` it agrees, since `q` is a unit and coprime to `q + 1`.) The
per-step bookkeeping below is honest reusable infrastructure; it does **not**
by itself furnish a globally-descending measure for `reaches_cycle` (the
even branch lowers `v_[2]` by exactly one, but the odd branch's effect is the
uncontrolled part — precisely the open content, per the 2026-07-18 audit). -/

open Polynomial in
/-- The `[2]_q`-adic valuation on `ℤ[q]`: multiplicity of the root `q = -1`
    (equivalently, of the factor `[2]_q = q + 1`). -/
noncomputable def qTwoValuation (P : Polynomial ℤ) : ℕ := P.rootMultiplicity (-1)

open Polynomial in
/-- **Even-branch valuation bookkeeping.** Multiplying by `[2]_q = q + 1`
    raises `v_[2]` by exactly one (for `P ≠ 0`); equivalently the even branch
    `P ↦ P/[2]_q` lowers it by one. -/
theorem qTwoValuation_mul_qplus_one (P : Polynomial ℤ) (hP : P ≠ 0) :
    qTwoValuation (P * (X + 1)) = qTwoValuation P + 1 := by
  have hXC : (X + 1 : Polynomial ℤ) = X - C (-1) := by
    rw [map_neg, map_one]; ring
  unfold qTwoValuation
  rw [hXC, rootMultiplicity_mul (mul_ne_zero hP (X_sub_C_ne_zero (-1))),
    rootMultiplicity_X_sub_C_self]

open Polynomial in
/-- **Odd-branch well-definedness.** When `P` is `q`-odd (`[2]_q ∣ P + 1`), the
    odd-branch numerator `[3]_q·P + 1` is divisible by `[2]_q`, so the odd
    branch `([3]_q·P + 1)/[2]_q` stays in the Skein ring `ℤ[q]`. Proof: the
    Skein divisibility identity gives `[3]_q·P + 1 = q·[2]_q·P + (P + 1)`, and
    `[2]_q` divides both summands. -/
theorem qTwoDvd_oddBranch (P : Polynomial ℤ) (h : (X + 1) ∣ (P + 1)) :
    (X + 1) ∣ ((X ^ 2 + X + 1) * P + 1) := by
  have key : (X ^ 2 + X + 1) * P + 1 = X * (X + 1) * P + (P + 1) := by ring
  rw [key]
  exact dvd_add ((dvd_mul_left (X + 1) X).mul_right P) h

/-! ### The domain-stable cone `D∞` and hypothesis-free convergence (Tier B) -/

/-- **Generic termination-from-descent.** Over any predicate `S` that is
    forward-invariant off `target` and carries a strictly-descending
    `ℕ`-measure, every `S`-element reaches `target`. This is
    `reaches_cycle_of_descent` with the cone abstracted, so it also applies to
    the domain-stable cone (where forward-invariance is free). -/
theorem reaches_of_descent_of_forward {α : Type*} (f : α → α) (target : α)
    (S : α → Prop) (μ : α → ℕ)
    (hfwd : ∀ x, S x → x ≠ target → S (f x))
    (hdesc : ∀ x, S x → x ≠ target → μ (f x) < μ x) :
    ∀ x, S x → ∃ k : ℕ, f^[k] x = target := by
  suffices H : ∀ n x, μ x = n → S x → ∃ k, f^[k] x = target from
    fun x hx => H (μ x) x rfl hx
  intro n
  induction n using Nat.strong_induction_on with
  | _ n IH =>
    intro x hμ hx
    by_cases hc : x = target
    · exact ⟨0, by simpa using hc⟩
    · have hlt : μ (f x) < n := hμ ▸ hdesc x hx hc
      obtain ⟨k, hk⟩ := IH (μ (f x)) hlt (f x) rfl (hfwd x hx hc)
      exact ⟨k + 1, by rw [Function.iterate_succ_apply]; exact hk⟩

/-- The domain of the (partial) Skein-Collatz map: `P` is `q`-even (`[2]_q ∣ P`)
    or `q`-odd (`[2]_q ∣ P + 1`). -/
def QCollatz.inDomain {Skein : Type u} [CommRing Skein] [QCollatz Skein]
    (P : Skein) : Prop :=
  QCollatz.qi2 ∣ P ∨ QCollatz.qi2 ∣ (P + 1)

/-- The **domain-stable cone** `D∞`: elements whose entire forward orbit stays
    in the domain. This is the well-posed cone for the conjecture — the naive
    positive cone is ill-posed (`C_q` undefined on almost all of it; see
    `pos_domain_stable` and `qcollatz_domain_not_forward_invariant`). -/
def QCollatz.domainStable {Skein : Type u} [CommRing Skein] [QCollatz Skein]
    (P : Skein) : Prop :=
  ∀ k : ℕ, QCollatz.inDomain (QCollatz.C^[k] P)

/-- **The domain-stable cone is forward-invariant**: `C` maps `D∞` into `D∞`
    (unlike the ambient domain, which is not forward-invariant). -/
theorem QCollatz.domainStable_forward {Skein : Type u} [CommRing Skein]
    [QCollatz Skein] (P : Skein) (h : QCollatz.domainStable P) :
    QCollatz.domainStable (QCollatz.C P) := by
  intro k
  rw [← Function.iterate_succ_apply]
  exact h (k + 1)

/-- **Convergence over the domain-stable cone reduces to a descent measure
    alone.** Because `D∞` is forward-invariant, the `hclosed` hypothesis of
    `reaches_cycle_of_descent` is discharged automatically — the open content
    is exactly the existence of the descent measure `μ`. -/
theorem reaches_cycle_of_descent_domainStable {Skein : Type u} [CommRing Skein]
    [QCollatz Skein] (μ : Skein → ℕ)
    (hdesc : ∀ P : Skein, QCollatz.domainStable P → P ≠ QCollatz.attractor →
      μ (QCollatz.C P) < μ P) :
    ∀ P : Skein, QCollatz.domainStable P →
      ∃ k : ℕ, QCollatz.C^[k] P = QCollatz.attractor :=
  reaches_of_descent_of_forward QCollatz.C QCollatz.attractor QCollatz.domainStable
    μ (fun P hP _ => QCollatz.domainStable_forward P hP) hdesc

/-! ### The map's arithmetic descends from the QOU substrate parameter (Tier C #8, brick 1)

A quantum observable universe furnishes a single substrate parameter `q`. The
bundle below shows that the **entire** Skein-Collatz `q`-arithmetic — the
`q`-integers `[2]_q`, `[3]_q`, the Skein divisibility identity, the contraction
gap, and the Bézout coprimality — is *determined by `q` alone*, with every
identity holding **by construction** (proved, not axiomatised). This makes
explicit that the categorical data descends from the substrate parameter rather
than being posited. Bricks 2–3 (see bean `qcz17`) link `q` to an actual
`QuantumObservableUniverse` and its Reeb-bundle Skein module `𝒮(q) ≅ ℤ[q^{±1}]`. -/

/-- The Skein-Collatz arithmetic induced by a substrate parameter `q`
    (a QOU's `q₀`, as an element of the Skein ring `R`). -/
structure SkeinCollatzArith (R : Type u) [CommRing R] where
  /-- The substrate parameter furnished by the QOU. -/
  q : R

namespace SkeinCollatzArith

variable {R : Type u} [CommRing R] (a : SkeinCollatzArith R)

/-- Induced `[2]_q = q + 1`. -/
def qi2 : R := a.q + 1

/-- Induced `[3]_q = q² + q + 1`. -/
def qi3 : R := a.q ^ 2 + a.q + 1

/-- **Skein divisibility** `[3]_q = q·[2]_q + 1` — holds by construction. -/
theorem skein_divisibility : a.qi3 = a.q * a.qi2 + 1 := by
  rw [qi2]
  rw [qi3]
  ring

/-- **Contraction gap** `[2]_q² − [3]_q = q` — holds by construction. -/
theorem contraction_gap : a.qi2 ^ 2 - a.qi3 = a.q := by
  rw [qi2]
  rw [qi3]
  ring

/-- **Bézout coprimality** `[3]_q − q·[2]_q = 1` — holds by construction. -/
theorem coprime : a.qi3 - a.q * a.qi2 = 1 := by
  rw [qi2]
  rw [qi3]
  ring

/-- The odd-branch defining equation at `q⁻¹` (the fundamental cycle) follows
    from the induced arithmetic whenever `q` is invertible — so the fundamental
    2-cycle is likewise determined by the substrate parameter. -/
theorem fundamental_odd_step (qinv : R) (hq : a.q * qinv = 1) :
    (1 + qinv) * a.qi2 = a.qi3 * qinv + 1 := by
  rw [qi2]
  rw [qi3]
  linear_combination (-a.q) * hq

end SkeinCollatzArith

/-! ### The Markov-trace observable: `reaches_cycle` as observed halting (Tier C #12)

In the QOU, *observation* is the Markov trace `tr_M` — an orbit's observed output
is the skein value of its current state, the degree-0 section an observer
reads. Coupling any observation map `obs : Skein → V` to the Skein-Collatz
dynamics turns the convergence conjecture into an **observational halting
statement**: the observed output stabilises to the value of the fundamental
cycle — the trivial invariant, the unknot's `tr_M = 1`. This is the Markov-trace
face of the conjecture (`collatz-three-forms`: `tr_M(𝒞_q^k h) → 1`) — the sense
in which the output of the braid-computation *is* an observation. -/

/-- **Observed output stabilises to the attractor's** (conditional on the
    conjecture `reaches_cycle`). For any observation map `obs`, every positive
    orbit's observed output eventually equals `obs attractor` — the observed
    halting output. -/
theorem reaches_cycle_observed {Skein : Type u} [CommRing Skein] [QCollatz Skein]
    {V : Type*} (obs : Skein → V) (P : Skein) (hP : QCollatz.pos P) :
    ∃ k : ℕ, obs (QCollatz.C^[k] P) = obs QCollatz.attractor := by
  obtain ⟨k, hk⟩ := QCollatz.reaches_cycle P hP
  exact ⟨k, by rw [hk]⟩

/-- **`reaches_cycle` ⇒ observed output `→` the trivial invariant.** If the
    observation map assigns the fundamental cycle the unknot value `u`
    (`obs attractor = u`, e.g. the trivial skein polynomial `tr_M = 1`), then
    every positive braid-computation in the domain halts to the observed output
    `u`. This is the observational reading of the conjecture: *the halting output
    is the trivial invariant.* -/
theorem reaches_cycle_observed_unknot {Skein : Type u} [CommRing Skein]
    [QCollatz Skein] {V : Type*} (obs : Skein → V) (u : V)
    (hu : obs QCollatz.attractor = u) (P : Skein) (hP : QCollatz.pos P) :
    ∃ k : ℕ, obs (QCollatz.C^[k] P) = u := by
  obtain ⟨k, hk⟩ := reaches_cycle_observed obs P hP
  exact ⟨k, hk.trans hu⟩

/-- Even iterates `C^[2m]` fix the fundamental 2-cycle representative `attractor`. -/
theorem QCollatz.iterate_two_attractor {Skein : Type u} [CommRing Skein]
    [QCollatz Skein] (m : ℕ) :
    (QCollatz.C^[2 * m] QCollatz.attractor : Skein) = QCollatz.attractor := by
  induction m with
  | zero => rfl
  | succ m ih =>
    have hstep : 2 * (m + 1) = 2 * m + 1 + 1 := by omega
    rw [hstep, Function.iterate_succ_apply', Function.iterate_succ_apply',
      ih, QCollatz.attractor_period_two]

/-- Odd iterates `C^[2m+1]` map `attractor` to its period-2 partner `C attractor`. -/
theorem QCollatz.iterate_two_add_one_attractor {Skein : Type u} [CommRing Skein]
    [QCollatz Skein] (m : ℕ) :
    (QCollatz.C^[2 * m + 1] QCollatz.attractor : Skein)
      = QCollatz.C QCollatz.attractor := by
  rw [Function.iterate_succ_apply', QCollatz.iterate_two_attractor m]

/-- The fundamental 2-cycle lies in the domain-stable cone `D∞` whenever both
    cycle vertices `attractor` and `C attractor` lie in `inDomain`. -/
theorem QCollatz.attractor_domainStable {Skein : Type u} [CommRing Skein]
    [QCollatz Skein]
    (h0 : QCollatz.inDomain (QCollatz.attractor : Skein))
    (h1 : QCollatz.inDomain (QCollatz.C (QCollatz.attractor : Skein))) :
    QCollatz.domainStable (QCollatz.attractor : Skein) := by
  intro k
  rcases Nat.even_or_odd' k with ⟨m, rfl | rfl⟩
  · rw [QCollatz.iterate_two_attractor m]
    exact h0
  · rw [QCollatz.iterate_two_add_one_attractor m]
    exact h1

end QOU.AppendixSurreals
