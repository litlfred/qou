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

/-! ## The cited complexity layer and the counting–decision gap

Everything citable about hardness at $q_0$ concerns **counting**:
Jaeger--Vertigan--Welsh give $\#\mathrm{P}$-hardness of exact Jones
evaluation away from the lattice roots of unity, and the textbook
inclusion $\mathrm{NP} \subseteq \mathrm{P}^{\#\mathrm{P}}$ makes
$\mathrm{FP} = \#\mathrm{P} \Rightarrow \mathrm{P} = \mathrm{NP}$.
Lean has no complexity-theory library, so these are carried as a
**cited hypothesis class** — never proved, never instantiated (a
fabricated instance would launder literature into a Lean proof; per
AGENTS.md §Axiomatization is NOT a Proof).  The theorems below are
sorry-free *given* the class, and isolate exactly what a proof of the
conjecture must add. -/

/-- **Cited complexity layer** (hypotheses, not theorems of this
    development).  All four parameters are opaque `Prop`s:
    `semisimple` = $H_n(q_0)$ is semisimple (no radical pruning of the
    resolution tree), `JonesInFP` = exact Jones evaluation at $q_0$ is
    polynomial-time, `FPeqSharpP` = $\mathrm{FP} = \#\mathrm{P}$,
    `PeqNP` = $\mathrm{P} = \mathrm{NP}$.  **No instance is declared**:
    the fields are established literature results that Lean cannot
    currently express, carried honestly in the type. -/
class JonesComplexityCitations
    (semisimple JonesInFP FPeqSharpP PeqNP : Prop) : Prop where
  /-- Jaeger--Vertigan--Welsh: at a semisimple (non-root-of-unity)
      parameter, exact Jones evaluation is $\#\mathrm{P}$-hard — so a
      polynomial-time evaluator collapses $\mathrm{FP} = \#\mathrm{P}$.

      Ref: [jaeger1990] https://doi.org/10.1017/S0305004100068936 -/
  jvw_sharp_p_hard : semisimple → JonesInFP → FPeqSharpP
  /-- $\mathrm{NP} \subseteq \mathrm{P}^{\#\mathrm{P}}$: if counting is
      easy, decision is easy.

      Ref: [arora2009] https://doi.org/10.1017/CBO9780511804090 -/
  counting_dominates_decision : FPeqSharpP → PeqNP

variable {semisimple JonesInFP FPeqSharpP PeqNP : Prop} {r : ℝ}

/-- $\mathrm{FP} \neq \#\mathrm{P}$ is the *weaker* separation:
    it already follows from $\mathrm{P} \neq \mathrm{NP}$ (sorry-free
    given the cited layer). -/
theorem counting_sep_of_decision_sep
    [C : JonesComplexityCitations semisimple JonesInFP FPeqSharpP PeqNP] :
    ¬PeqNP → ¬FPeqSharpP :=
  mt C.counting_dominates_decision

/-- **Composition (sorry-free modulo citations).**  Given the
    residue–semisimplicity bridge (the open front (a), tracked as its
    own epic), a surviving residue makes polynomial-time exact Jones
    evaluation collapse $\mathrm{FP} = \#\mathrm{P}$. -/
theorem intractability_of_residual_ne_zero
    [C : JonesComplexityCitations semisimple JonesInFP FPeqSharpP PeqNP]
    (bridge : r ≠ 0 → semisimple) (hr : r ≠ 0) :
    JonesInFP → FPeqSharpP :=
  C.jvw_sharp_p_hard (bridge hr)

/-- **Companion (counting) faithfulness — provable, unlike the
    $\mathrm{P} \neq \mathrm{NP}$ faithfulness.**  Given
    $\mathrm{FP} \neq \#\mathrm{P}$ and the bridge, a surviving residue
    forces exact Jones evaluation at $q_0$ out of $\mathrm{FP}$. -/
theorem counting_faithfulness
    [C : JonesComplexityCitations semisimple JonesInFP FPeqSharpP PeqNP]
    (bridge : r ≠ 0 → semisimple) (hFP : ¬FPeqSharpP) (hr : r ≠ 0) :
    ¬JonesInFP :=
  fun hJ => hFP (C.jvw_sharp_p_hard (bridge hr) hJ)

/-- **Isolation of the open kernel.**  The conjectured faithfulness
    ($\mathrm{res} \neq 0 \Rightarrow \mathrm{P} \neq \mathrm{NP}$)
    follows from the cited layer + bridge + **two open inputs**, and
    this theorem exists to display them:

    * `hFP` — the counting separation $\mathrm{FP} \neq \#\mathrm{P}$
      itself (open; weaker than $\mathrm{P} \neq \mathrm{NP}$ by
      `counting_sep_of_decision_sep`), and
    * `transfer` — a counting$\to$decision transfer
      ($\text{Jones} \notin \mathrm{FP} \Rightarrow
       \mathrm{P} \neq \mathrm{NP}$), which **no known result
      supplies**: $\#\mathrm{P}$-hardness of one invariant does not
      imply $\mathrm{P} \neq \mathrm{NP}$.

    Discharging these two hypotheses IS proving `conj:qou-p-neq-np`. -/
theorem faithfulness_of_transfer
    [C : JonesComplexityCitations semisimple JonesInFP FPeqSharpP PeqNP]
    (bridge : r ≠ 0 → semisimple)
    (hFP : ¬FPeqSharpP)
    (transfer : ¬JonesInFP → ¬PeqNP)
    (hr : r ≠ 0) : ¬PeqNP :=
  transfer fun hJ => hFP (C.jvw_sharp_p_hard (bridge hr) hJ)

/-! ## The Wenzl bridge (stage 1, bean `qou-f0p8`)

The residue–semisimplicity bridge, parameter side.  Wenzl's criterion
[wenzl1988] characterises semisimplicity of the Iwahori--Hecke algebra
$H_n(q)$ by *genericity of the parameter*: $H_n(q)$ is semisimple iff
$q^k \neq 1$ for every $2 \leq k \leq n$ (equivalently
$[n]_q! \neq 0$).  Stage 1 formalises the parameter-side condition
(`WenzlGeneric`, over a generic monoid per §7c), proves — sorry-free —
that any real $q > 1$ satisfies it at **every** rank, carries the
criterion itself as a cited hypothesis class (`WenzlCriterion`, no
instance: the Hecke radical theory is stage 2, bean `qou-vndn`), and
composes end-to-end: for the substrate $q_0 > 1$ the semisimplicity
hypothesis of `counting_faithfulness` is *discharged*, so the
companion faithfulness needs only the two cited classes plus
$\mathrm{FP} \neq \#\mathrm{P}$.  Notably the residual drops out: the
reachable counting statement is purely about genericity of $q_0$. -/

/-- **Wenzl genericity** (parameter-side semisimplicity condition,
    generic monoid per §7c): `q` is not a `k`-th root of unity for any
    `2 ≤ k ≤ n`.  Equivalent to `[n]_q! ≠ 0` over a field; the form
    here is the one Wenzl's criterion consumes.

    Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 -/
def WenzlGeneric {M : Type*} [Monoid M] (q : M) (n : ℕ) : Prop :=
  ∀ k : ℕ, 2 ≤ k → k ≤ n → q ^ k ≠ 1

/-- Genericity is antitone in the rank (sorry-free). -/
theorem wenzlGeneric_of_le {M : Type*} [Monoid M] {q : M} {m n : ℕ}
    (hmn : m ≤ n) (h : WenzlGeneric q n) : WenzlGeneric q m :=
  fun k h2 hk => h k h2 (hk.trans hmn)

/-- Non-torsion implies Wenzl genericity at every rank (sorry-free). -/
theorem wenzlGeneric_of_nontorsion {M : Type*} [Monoid M] {q : M}
    (h : ∀ k : ℕ, k ≠ 0 → q ^ k ≠ 1) (n : ℕ) : WenzlGeneric q n :=
  fun k h2 _ => h k (by omega)

/-- **The substrate is Wenzl-generic at every rank (sorry-free).**
    Any real $q > 1$ — in particular $q_0 \approx 1.10998$ — satisfies
    the Wenzl genericity condition for all $n$: the semisimplicity
    *hypothesis* is discharged by pure order arithmetic. -/
theorem wenzlGeneric_of_one_lt {q : ℝ} (hq : 1 < q) (n : ℕ) :
    WenzlGeneric q n :=
  fun _ h2 _ => ne_of_gt (one_lt_pow₀ hq (by omega))

/-- **Cited Wenzl criterion** (hypothesis class, not a theorem of this
    development): parameter genericity implies semisimplicity of
    $H_n(q)$.  `semisimple n` is an opaque per-rank `Prop` pending the
    stage-2 Hecke radical formalisation (bean `qou-vndn`).  **No
    instance is declared** — a fabricated instance would launder
    [wenzl1988] into a Lean proof.

    Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 -/
class WenzlCriterion {M : Type*} [Monoid M] (q : M)
    (semisimple : ℕ → Prop) : Prop where
  /-- Wenzl's semisimplicity criterion, carried as a hypothesis. -/
  semisimple_of_generic : ∀ n, WenzlGeneric q n → semisimple n

/-- **Bridge discharged (sorry-free modulo the cited criterion).**
    For real $q > 1$, $H_n(q)$ is semisimple at every rank. -/
theorem semisimple_of_one_lt {q : ℝ} {ss : ℕ → Prop}
    [W : WenzlCriterion q ss] (hq : 1 < q) (n : ℕ) : ss n :=
  W.semisimple_of_generic n (wenzlGeneric_of_one_lt hq n)

/-- **End-to-end companion faithfulness, bridge discharged (sorry-free
    modulo the two cited classes).**  For the real substrate
    $q_0 > 1$: given $\mathrm{FP} \neq \#\mathrm{P}$, exact Jones
    evaluation at $q_0$ is not polynomial-time.  The semisimplicity
    leg is *supplied* (Wenzl genericity from $q_0 > 1$), no longer
    assumed — and the obstruction residual does not appear: the
    reachable counting statement depends only on the genericity of the
    substrate parameter.  What remains open beyond citations is
    exactly the pair displayed by `faithfulness_of_transfer`. -/
theorem counting_faithfulness_of_one_lt {q : ℝ} {ss : ℕ → Prop}
    {JonesInFP FPeqSharpP PeqNP : Prop}
    [C : JonesComplexityCitations (∀ n, ss n) JonesInFP FPeqSharpP PeqNP]
    [WenzlCriterion q ss]
    (hq : 1 < q) (hFP : ¬FPeqSharpP) : ¬JonesInFP :=
  fun hJ => hFP (C.jvw_sharp_p_hard (fun n => semisimple_of_one_lt hq n) hJ)

end QOU.Information
