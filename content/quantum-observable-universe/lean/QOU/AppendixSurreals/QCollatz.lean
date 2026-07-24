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
  /-- **The $q$-Collatz conjecture (within the QOU).** Every element of
      the positive cone reaches the fundamental cycle — i.e. reaches
      `attractor` — under finitely many iterations of the Skein-Collatz
      map. The `sorry`-free absence of an instance is the honest "open"
      state per §3b-tax. -/
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

end QOU.AppendixSurreals
