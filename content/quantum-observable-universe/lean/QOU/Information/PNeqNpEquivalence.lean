import Mathlib.Tactic

/-!
# QOU.Information.PNeqNpEquivalence — chipping the conjectured equivalence

Structural companion to [`QouPNeqNp`](QouPNeqNp.lean) /
[`conj:qou-p-neq-np`](../../../quantum-observable-universe/information-theory/qou-p-neq-np.md).
The conjecture asserts an *equivalence*
$\mathrm{P} \neq \mathrm{NP} \iff \mathrm{res}_{\mathcal{R}}(\chi(A)) \neq 0$
at the non-torsion substrate point $q_0$.  This module decomposes the
equivalence into its two directions and proves — **sorry-free** —
everything that is not the irreducible open kernel:

* `equivalence_collapse` — pure propositional logic: once the
  non-vanishing leg is established, asserting the equivalence is
  *exactly* asserting $\mathrm{P} \neq \mathrm{NP}$.  Since the corpus
  derives $\chi(A) = -6$ (`ex:chi-minus-six-derivation`,
  `prf:qou-obstruction-reduction`) with no computational-complexity
  input, this is the machine-checked form of the collapse observation
  in the `.md`.
* `ResidueFaithfulness.sound_of_ne_zero` — the soundness direction
  ($\mathrm{P} \neq \mathrm{NP} \Rightarrow \mathrm{res} \neq 0$) is
  automatic given the derived non-vanishing: it carries no content.
* `conclusion_of_faithful` — faithfulness alone, plus the derived
  non-vanishing, already yields the conclusion; the equivalence adds
  nothing beyond its faithful direction.
* `chi_mod_vanishes_iff` — the Kummer filtration arithmetic of the
  derived value: $-6 \bmod n = 0 \iff n \mid 6$, i.e. the classically
  transparent torsion levels are exactly the
  Jaeger--Vertigan--Welsh tractable set $n \mid 6$.
* `nontorsion_of_one_lt` — any real $q > 1$ (in particular the
  substrate $q_0 \approx 1.10998$) is non-torsion in
  $\mathbb{G}_m(\mathbb{R})$: no positive power returns to $1$, so no
  finite Kummer level applies.

What deliberately remains open: the **faithfulness** direction
$\mathrm{res} \neq 0 \Rightarrow \mathrm{P} \neq \mathrm{NP}$ — that
*is* the conjecture (the `sorry` on `QouPNeqNp`).  $\mathrm{P}$ and
$\mathrm{NP}$ themselves are kept as an opaque `Prop` parameter:
Mathlib has no standard P/NP formalisation, and axiomatising one here
would add fake precision without content (per the anti-laundering
rule, AGENTS.md §Axiomatization is NOT a Proof).
-/

namespace QOU.Information

/-- **Collapse of a conditioned equivalence (sorry-free).**  If `a`
    already holds, then the assertion `a ↔ b` is equivalent to the bare
    assertion `b`.  Instantiated with `a := res ≠ 0` (derived, the
    $\chi(A) = -6$ chain) and `b := P ≠ NP`, this says: the conjectured
    equivalence carries exactly the content $\mathrm{P} \neq \mathrm{NP}$
    — no more, no less. -/
theorem equivalence_collapse {a b : Prop} (ha : a) : (a ↔ b) ↔ b :=
  ⟨fun h => h.mp ha, fun hb => ⟨fun _ => hb, fun _ => ha⟩⟩

/-- The two directions of the conjectured equivalence as separate named
    hypotheses (§3b-cond non-degenerate decomposition: the class carries
    the genuine sub-claims, and the equivalence is *derived* from them
    by `Iff.intro`, never carried as a monolithic field).
    `PneqNP` is an opaque `Prop` pending a formal P/NP. -/
class ResidueFaithfulness (PneqNP : Prop) (residual : ℝ) : Prop where
  /-- Soundness: separation forces the obstruction residue to survive. -/
  sound : PneqNP → residual ≠ 0
  /-- Faithfulness: a surviving residue forces the separation.  This
      direction is the irreducible open kernel of `conj:qou-p-neq-np`. -/
  faithful : residual ≠ 0 → PneqNP

/-- The conjectured equivalence, *derived* from the two directions
    (sorry-free given the class hypotheses). -/
theorem equivalence_of_faithfulness {P : Prop} {r : ℝ}
    [ResidueFaithfulness P r] : r ≠ 0 ↔ P :=
  ⟨ResidueFaithfulness.faithful, ResidueFaithfulness.sound⟩

/-- **The soundness direction is free (sorry-free).**  Given the derived
    non-vanishing, `P → r ≠ 0` holds for *any* proposition `P` — it
    carries no information about computation.  The chippable half of
    the equivalence chips to nothing. -/
theorem sound_of_residual_ne_zero {P : Prop} {r : ℝ} (hr : r ≠ 0) :
    P → r ≠ 0 :=
  fun _ => hr

/-- **Faithfulness is the whole conjecture (sorry-free reduction).**
    Given the derived non-vanishing, the faithful direction alone
    already yields the conclusion.  Together with
    `sound_of_residual_ne_zero` and `equivalence_collapse`, this locates
    the entire open content of `conj:qou-p-neq-np` in the single
    implication `faithful`. -/
theorem conclusion_of_faithful {P : Prop} {r : ℝ} (hr : r ≠ 0)
    (hf : r ≠ 0 → P) : P :=
  hf hr

/-- **Kummer arithmetic of the derived value (sorry-free).**  With
    $\chi(A) = -6$, the mod-$n$ reduction of the obstruction vanishes
    exactly at the Jaeger--Vertigan--Welsh classically tractable
    torsion levels $n \mid 6$. -/
theorem chi_mod_vanishes_iff (n : ℤ) : (-6 : ℤ) % n = 0 ↔ n ∣ 6 := by
  rw [← Int.dvd_iff_emod_eq_zero, dvd_neg]

/-- **The substrate point is non-torsion (sorry-free).**  Any real
    $q > 1$ — in particular $q_0 \approx 1.10998$ — has no positive
    power equal to $1$, so no finite Kummer level applies to it:
    $q_0$ sits permanently outside the transparent set. -/
theorem nontorsion_of_one_lt {q : ℝ} (hq : 1 < q) :
    ∀ n : ℕ, n ≠ 0 → q ^ n ≠ 1 := by
  intro n hn
  exact ne_of_gt (one_lt_pow₀ hq hn)

end QOU.Information
