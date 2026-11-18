/-
# The Markov bond rule forces pairwise-additivity — so `b₃ = 0` is the TRACE's, not the assembly's

`QOU.Mass.PairwiseCumulantVanishing` proves that every **bond-functional**
assembly `B = Σ_{i<j} f (μ i j)` has identically vanishing connected cumulants
above order two, for every `f`. Its own scope note is careful about what that
leaves open:

> the premises constrain `f` on **disjoint** clusters, and the observable that
> fails is a **connected** quantity

That is the honest limit of the argument as stated there: §10a's multiplicativity
premise is about *independent* subsystems, and a bound state is exactly not one,
so one could still hope the bound atom's trace carries irreducible many-body
content that a smarter assembly would expose.

**It does not, and this file is why.** The corpus separately established the
**bond rule** — bean `qou-g8i1`, `completed`; audit
`docs/audits/2026-08-19-bar-involution-is-isospin-conjugation.md` §4f:

    tr (x * (σ_g + d·I)) = (z + d) · tr x       ⇒     tr_free / tr_atom = Π_b 1/(z + d_b)

verified on 16 nuclei numerically (A = 2..10, to `4.45e-31`) and on 6 symbolically
at `n = 6, 9, 12`, for `d = 0` (pp), `d = -h` (nn) and `d = d_iface` (pn). The
mechanism recorded there is *"the Markov property applied at a **gap**, not at the
last strand"* — the generators are **interior**, with strands above them, so this
is the bound atom word, **not** the disjoint sector that Markov axiom M3 covers
(`computations/probe_inter_knot_decoupling.py` is the M3, unlinked, case).

So the bound atom's trace ratio **is** a product over its bonds. Feed that to any
map `f` carrying products to sums, and the binding is a bond functional — whose
`b₃` vanishes identically. The chain closes:

    bond rule (qou-g8i1)      trace ratio = Π_bonds μ_b        [bound atom, interior gaps]
    + f multiplicative→additive                                [§10a's Cauchy step]
    ⇒ binding is ofBondFunctional
    ⇒ b₃ = b₄ = 0 identically                                  [PairwiseCumulantVanishing]
    vs AME2020  b₃ = +1.426222 MeV ≠ 0.

## What this changes about the open question

`qou-edt7` asks *what replaces the multiplicative assembly*. The answer this
forces is sharper than "a different assembly": **no function of the Markov trace
of the atom word can work.** The bond rule makes the trace a bond product; every
multiplicative-to-additive map of a bond product is a bond sum; every bond sum has
`b₃ = 0`. A replacement must therefore break the bond rule — a trace that is not
Markov, or an object that is not a trace of the atom word — not merely a different
`f`, and not a different edge set.

## Two things this makes cheaper, worth stating

**§10a's uniqueness step is not needed.** The audit's route runs Cauchy →
*continuous solutions are* `c·log` → the log form is forced, and
`binding_functional_extensivity_probe.py` records that the uniqueness half is
**classical and not in Lean**. It is also **irrelevant here**: `IsAdditiveOnProducts`
below assumes only `f (x*y) = f x + f y`, with no continuity, measurability or
regularity of any kind, and the conclusion already follows. A pathological
non-measurable Hamel-basis solution of Cauchy's equation gives `b₃ = 0` too.

**The hypothesis is carried explicitly, not assumed away.** Per AGENTS.md
§"Conditional-proved ≠ premise-established", the bond rule appears as a named
hypothesis `SatisfiesBondRule` rather than as an axiom or a `def` asserting it.
What is proved here is the *implication*. `qou-g8i1` records the premise as
established by measurement plus the gap-Markov mechanism; it is **not** re-proved
here, and this file does not claim it.

## Not contradicted by the nonzero Brunnian deficit `D_A` — different word

A reader arriving from `qou-v7ro` will know that the **Brunnian trace deficit**
`D_A = 1 - qtr(ρ(w_A))/[2]^A` is **nonzero for every `A`** (proved, merged #6217:
`D_{A+1} = -h²(h²+2)·D_A`, with `D_3 = 1.44e-3` at the proton pin). That looks
like a factorisation failure sitting beside a bond rule verified to `4.45e-31`,
and it is worth saying plainly that it is not one: **the two are different
words.**

* The **bond rule** governs the nucleon **atom word** — a product of bond letters
  `σ_g + d·I` at interior gaps (`canonical_braid_crossings`, `qou-g8i1`).
* `w_A` is the **iterated group commutator** `w_n = [w_{n-1}, b]` in the
  Temperley–Lieb / spin-½ setting. A commutator is not a product of independent
  bond letters, which is exactly why its trace does not reduce to one.

So `D_A ≠ 0` does not falsify `SatisfiesBondRule` for the atom word, and this
file's exclusion is not vacuous there.

**Better: `D_A` is the corpus's one known member of the class this file leaves
open.** The conclusion above is that a carrier must *break* the bond rule; a word
whose normalised trace departs from the bond product by a nonzero `D_A` is
precisely such a word. So the search is correctly aimed at non-factorising words
— and `qou-v7ro` has already measured why this particular one does not finish the
job: `|D_A|` **falls** geometrically (`D_3 = 1.44e-3` → `D_8 = 8.2e-9`, factor
`-h²(h²+2) = -0.0893226497` per step) while the empirical binding fraction
**rises** with `A` (`0.767 → 0.954·ℏ_q²`, ⁴He → ⁵⁶Fe). Opposite trends, so `D_A`
is the Milnor order/parity marker, not the magnitude — a scope-**(a)** negative on
that carrier, not on the class.

**Which narrows `qou-edt7`'s positive half to a stated question:** is there a
non-factorising word whose deficit *rises* with `A`? That is a search over words,
not over functionals `f` and not over edge sets — both of which this file rules
out.

## Scope

**(b)** on bindings of the form `f ∘ (trace of the atom word)` where the trace
obeys the bond rule and `f` carries products to sums — invariant named: the bond
rule makes the cluster trace a product over pairs, so the connected part above
order two has nothing to be built from. **(a)** on everything else: this refutes
no physics, excludes no non-trace carrier, and says nothing about whether the bond
rule extends past the nuclei on which it was verified.

Generic base rings throughout (AGENTS.md §7c): a `CommMonoid` for the trace side,
where only products are used, and the `CommRing` `BindingMap` already requires for
the energy side. No `ℝ`, no ordering, no anchor, no `q₀`.
-/
import QOU.Mass.PairwiseCumulantVanishing

namespace QOU.Mass.MarkovBondRuleForcesPairwise

open QOU.Mass.PairwiseCumulantVanishing

variable {R : Type*} [CommMonoid R] {S : Type*} [CommRing S]

/-- The Markov-trace ratios of the clusters of up to four nucleons: one scalar per
cluster. Only the *ratio* `tr_free / tr_atom` matters, so this carries no units
and no anchor. -/
structure ClusterTrace (R : Type*) [CommMonoid R] where
  /-- the two-body cluster `{i, j}`. -/
  pair : Fin 4 → Fin 4 → R
  /-- the three-body cluster `{i, j, k}`. -/
  triple : Fin 4 → Fin 4 → Fin 4 → R
  /-- the four-body cluster. -/
  quad : R

namespace ClusterTrace

/-- **The bond rule** (bean `qou-g8i1`): every cluster's trace ratio is the
product of its bonds' factors. Carried as a hypothesis, not asserted — see the
header. -/
def SatisfiesBondRule (T : ClusterTrace R) (μ : Fin 4 → Fin 4 → R) : Prop :=
  (∀ i j, T.pair i j = μ i j) ∧
    (∀ i j k, T.triple i j k = μ i j * μ i k * μ j k) ∧
      T.quad = μ 0 1 * μ 0 2 * μ 0 3 * μ 1 2 * μ 1 3 * μ 2 3

end ClusterTrace

/-- `f` carries products to sums — §10a's Cauchy condition, and **nothing more**:
no continuity, no measurability, no regularity. The uniqueness step that would
pin `f` to a logarithm is not assumed and is not needed. -/
def IsAdditiveOnProducts (f : R → S) : Prop := ∀ x y : R, f (x * y) = f x + f y

/-- The binding read off the cluster traces by `f`, cluster by cluster. This is
the production shape: `B = -α · ln (tr_atom / tr_free)`. -/
def bindingOfTrace (f : R → S) (T : ClusterTrace R) : BindingMap S where
  pair i j := f (T.pair i j)
  triple i j k := f (T.triple i j k)
  quad := f T.quad

/-- **The composition.** Under the bond rule and the Cauchy condition, a binding
read off the trace is pairwise-additive — the property
`PairwiseCumulantVanishing` shows kills every connected cumulant above two. -/
theorem bindingOfTrace_isPairwise {f : R → S} {T : ClusterTrace R}
    {μ : Fin 4 → Fin 4 → R} (hf : IsAdditiveOnProducts f)
    (hT : T.SatisfiesBondRule μ) : (bindingOfTrace f T).IsPairwise := by
  obtain ⟨hp, ht, hq⟩ := hT
  constructor
  · intro i j k
    show f (T.triple i j k) = f (T.pair i j) + f (T.pair i k) + f (T.pair j k)
    rw [ht i j k, hp i j, hp i k, hp j k, hf, hf]
  · show f T.quad = _
    rw [BindingMap.pairSum]
    show f T.quad
        = f (T.pair 0 1) + f (T.pair 0 2) + f (T.pair 0 3) + f (T.pair 1 2)
            + f (T.pair 1 3) + f (T.pair 2 3)
    rw [hq, hp, hp, hp, hp, hp, hp, hf, hf, hf, hf, hf]

/-- **The conclusion.** The connected three-body cumulant of any trace-derived
binding vanishes identically. Not small — zero, for every `f`, every `μ`, and
every triple. -/
theorem b3_eq_zero_of_bondRule {f : R → S} {T : ClusterTrace R}
    {μ : Fin 4 → Fin 4 → R} (hf : IsAdditiveOnProducts f)
    (hT : T.SatisfiesBondRule μ) (i j k : Fin 4) :
    (bindingOfTrace f T).b3 i j k = 0 :=
  b3_eq_zero_of_isPairwise (bindingOfTrace_isPairwise hf hT) i j k

/-- And the four-body cumulant with it. -/
theorem b4_eq_zero_of_bondRule {f : R → S} {T : ClusterTrace R}
    {μ : Fin 4 → Fin 4 → R} (hf : IsAdditiveOnProducts f)
    (hT : T.SatisfiesBondRule μ) : (bindingOfTrace f T).b4 = 0 :=
  b4_eq_zero_of_isPairwise (bindingOfTrace_isPairwise hf hT)

/-- **The falsifiable form**, and the one AME2020 instantiates: a binding with any
nonzero connected three-body cumulant is not `f ∘ trace` for **any** `f` carrying
products to sums, over **any** bond-rule trace. This excludes the whole family at
once rather than one `f` at a time — which is what makes it an answer to
`qou-edt7` rather than another candidate for it. -/
theorem no_traceFunctional_of_b3_ne_zero {M : BindingMap S} {i j k : Fin 4}
    (h : M.b3 i j k ≠ 0) (f : R → S) (T : ClusterTrace R)
    (μ : Fin 4 → Fin 4 → R) (hf : IsAdditiveOnProducts f)
    (hT : T.SatisfiesBondRule μ) : M ≠ bindingOfTrace f T := by
  intro hEq
  exact h (hEq ▸ b3_eq_zero_of_bondRule hf hT i j k)

/-- **Sum of three-body and four-body cumulants under `SatisfiesBondRule` (`qou-5lsb`).**
When `IsAdditiveOnProducts f` and `T.SatisfiesBondRule μ`,
`(bindingOfTrace f T).b3 i j k + (bindingOfTrace f T).b4 = 0`. -/
theorem b3_add_b4_eq_zero_of_bondRule {f : R → S} {T : ClusterTrace R}
    {μ : Fin 4 → Fin 4 → R} (hf : IsAdditiveOnProducts f)
    (hT : T.SatisfiesBondRule μ) (i j k : Fin 4) :
    (bindingOfTrace f T).b3 i j k + (bindingOfTrace f T).b4 = 0 := by
  rw [b3_eq_zero_of_bondRule hf hT i j k, b4_eq_zero_of_bondRule hf hT, add_zero]

end QOU.Mass.MarkovBondRuleForcesPairwise
