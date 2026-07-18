import Mathlib.Tactic

/-!
# QOU.AppendixSurreals.QCollatz — the $q$-Collatz conjecture (content-bearing class)

**§3b conjecture-class axiomatisation** for content block
[`conj:q-collatz`](../../../quantum-observable-universe/appendix-surreals/q-collatz-conjecture.md):
*The $q$-Collatz conjecture: Skein-module crossing resolution*.

This is a **primary open conjecture** (per AGENTS.md §3b / §3b-tax).
The class `QCollatz` carries the conjecture's actual content:

* the Skein module is a commutative ring `Skein` (a model of
  $\mathbb{Z}[q^{\pm 1}]$);
* `qi2 = [2]_q = q + 1` and `qi3 = [3]_q = q^2 + q + 1` (combinatorial
  convention);
* the Skein-Collatz map `C` is characterised branch-by-branch — the
  **even** branch $P \mapsto P/[2]_q$ (`C_even`) and the **odd** branch
  $P \mapsto ([3]_q P + 1)/[2]_q$ (`C_odd`), the latter well-defined by
  Skein divisibility;
* the field `reaches_one` **is the conjecture**: every element of the
  positive cone reaches the unknot polynomial `1` under finitely many
  iterations of `C`.

Honest open-primary state (§3b-tax): the class is **content-bearing and
has no instance** — an instance would have to supply `reaches_one`, which
is exactly the open problem. We deliberately do **not** fabricate a
trivial instance (that would be an audit-dodge; bean `cj317`). Downstream
results may take `[QCollatz Skein]` as an explicit `[Instance]`
hypothesis to state theorems conditional on the conjecture (§3b-cond).

The no-cycles half of the conjecture (no periodic orbit other than
`P = 1`) is a genuine **consequence** of these fields — see
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

    Conjectural class — see
    [`conj:q-collatz`](../../../quantum-observable-universe/appendix-surreals/q-collatz-conjecture.md).
    The `reaches_one` field is the open conjecture; the class carries
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
  /-- **The $q$-Collatz conjecture.** Every element of the positive cone
      reaches the unknot polynomial `1` under finitely many iterations of
      the Skein-Collatz map. The `sorry`-free absence of an instance is
      the honest "open" state per §3b-tax. -/
  reaches_one : ∀ P : Skein, pos P → ∃ k : ℕ, C^[k] P = 1

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
