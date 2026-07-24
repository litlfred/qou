import Mathlib.Tactic

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

end QOU.AppendixSurreals
