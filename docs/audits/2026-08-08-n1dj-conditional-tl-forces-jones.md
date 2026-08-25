# The `qou-n1dj` question, collapsed to one named premise

**Date.** 2026-08-08
**Branch.** `claude/n1dj-conditional-tl-forces-d-2026-08-08`
**Bean.** [`qou-n1dj`](../../.beans/qou-n1dj--gap-does-the-mass-fibre-functor-land-in-repsu-q2tl.md) — still **open**
**Artifact.** [`QOU/BraidsAndKnots/FibreCategoricalTraceForcesJones.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/FibreCategoricalTraceForcesJones.lean)

## What this does — and what it does not

Bean `qou-n1dj` is open on one categorical question: does the fibre functor for
the **mass** channel land in `Rep(SU_q(2)) ≃ TL₃`, or in the full `H₃(q)`? The
answer selects between two normalised Markov traces sitting `195 ppm` apart on
the Borromean braid — convention **D** (Jones / Temperley–Lieb, what
`canonical_mass.py` consumes) and convention **C** (full-Hecke Ocneanu / Wenzl
`z`-trace, what the scope note of `prop:h3-markov-wenzl-weights` asserts).

**This work does not answer that question.** It reduces it to *one* premise,
with every other link machine-checked, so what remains open is crisp, named and
auditable:

> **The premise (open).** The mass channel's trace is the **categorical trace of
> the fibre action** on `V^{⊗3}`, rather than an abstract Ocneanu trace posited
> on all of `H₃(q)`.

Granting that premise — and nothing else beyond results already sorry-free in
this repository — convention D follows. Per AGENTS §"Conditional-proved ≠
premise-established", this is an implication; the antecedent is exactly what the
bean is open on. It is **not** evidence that D is correct, and **not** a claim
that the corpus self-contradiction is resolved.

## The chain

| link | statement | status |
|---|---|---|
| 1 | `dim V = 2` — gauge group of tensor automorphisms is `SU(2)`, fibre `ℂ²` | `thm:su2-emergence` (corpus); enters as the **explicit hypothesis** `hN : N = 2` |
| 2 | at `N = 2` the alternating channel `λ = (1³)` is **absent** from `V^{⊗3}` | **proved** — `RowCapObstruction.weyl_dim_alt_eq_zero_iff` (`C(N,3) = 0 ↔ N < 3`) |
| 3 | a categorical trace of the fibre action puts **no** weight on an absent channel and **does** carry a present one | **the premise** — `MassTraceIsFibreCategorical` |
| 4 | `y_(1³) = 0` + faithfulness on `TL₃` ⟹ `y = ([4]_q/[2]_q³, 1/[2]_q², 0)`, `z·[2]_q = q²` | **proved** — `markovWeights_eq_jones_of_threeRow_eq_zero` |

Composition: `markovWeights_eq_jones_of_fibre_categorical`. Corollary
`ocneanu_eq_jones_of_fibre_categorical` excludes convention C *under the
premise* — C's parameter fails `z·[2]_q = q²`, so C is not the categorical trace
of a two-dimensional fibre action on `V^{⊗3}`.

## What the class does and does not assume

`MassTraceIsFibreCategorical R N` carries three weight fields and four Prop
fields. It axiomatises only the two **support** consequences of the premise that
the forcing argument consumes:

* **row-cap support** — `weylDim_λ N = 0 → y_λ = 0`, per channel;
* **non-degeneracy** — `weylDimMixed N ≠ 0 → y_(2,1) ≠ 0`, i.e. faithfulness on
  `TL₃`, which is what kills the degenerate root `z = q`.

Both are `q`-independent: the row cap constrains `dim V`, and Drinfeld–Jimbo
quantisation does not change dimensions.

**Deliberately not assumed: the weight magnitudes.** At `q ≠ 1` the weights are
*quantum* dimensions, not the classical Weyl dimensions `weylDim*`; asserting
the classical values would be a **false** premise (D at `q₀` has
`y_(3)/y_(2,1) = 2.0437`, not `2`). Because the class assumes strictly less than
the physical premise it names, the conditional theorem is correspondingly
**stronger** — a full formalisation of quantum Schur–Weyl would *imply* these
fields, not conflict with them. This is a partial axiomatisation, and the
docstring says so.

## Non-degeneracy audit (AGENTS §3b-cond item 5)

The failure mode the rule targets is a class that carries the block's own
conclusion as a field with a "theorem" that projects it
(`:= ctx.weights_eq_D`). That is not what happens here:

* The class mentions **neither** `q`, **nor** the Ocneanu parameter `z`, **nor**
  the Jones weight vector, **nor** convention D. It is stated purely in terms of
  Weyl-module dimensions and weight vanishing.
* The conclusion `[2]_q²·y_(2,1) = 1 ∧ y_(3) = 1 − 2y_(2,1) ∧ z·[2]_q = q²` is
  **derived** — from the class fields, the proved row-cap obstruction, and the
  proved Markov-trace uniqueness theorem, against the three Markov equations
  carried as hypotheses.

Three further declarations were added specifically to close the vacuity
objections a reviewer would raise:

| objection | answer | declaration |
|---|---|---|
| "the antecedent may be unsatisfiable, so the conditional is vacuous" | at `N = 2` the premise **has a model** satisfying all three Markov equations — convention D itself, at `z = q − t`, `t = [2]_q⁻¹` | `exists_fibre_categorical_markov_trace` |
| "the class alone might already force `y_(1³) = 0`, making `hN` decoration" | at `N = 3` the class admits an instance with **nonzero** alternating weight; the vanishing genuinely comes from `dim V = 2`, i.e. `thm:su2-emergence` is used | `weightAlt_ne_zero_at_three` |
| "the row-cap fields might be too weak to say anything" | premise + normalisation is already **refutable**: at `N = 0` all three weights vanish, contradicting `tr 1 = 1` | `fibre_ne_zero_of_zero_dimensional` |

## Verification

* `scripts/lean-verify.sh` (`lean`-direct against restored oleans; **no**
  `lake build`) → **exit 0**.
* **Zero `sorry` terms.** `grep -c sorry` returns `2`, but both hits are the
  prose phrase *"sorry-free"* in the docstring (lines 21, 34); a word-bounded
  search for `sorry` as a term returns **0**, as does
  `sorryAx|admit|native_decide`. Recorded explicitly because `lean-verify.sh`
  exit 0 is *not* by itself evidence of sorry-freeness — a `sorry` is a warning,
  not an error.
* `#print axioms` on all **10** new declarations: no `sorryAx`. Four depend on
  no axioms at all (`MassTraceIsFibreCategorical`,
  `weightMixed_ne_zero_at_two`, `fibreCategoricalAtThree`,
  `weightAlt_ne_zero_at_three`); six on `[propext, Classical.choice, Quot.sound]`
  only.
* §7c: generic `{R : Type*} [CommRing R]`, with `[IsDomain R]` only where the
  uniqueness theorem cancels a nonzero factor and `[Nontrivial R]` only for the
  witness instances. `q⁻¹` carried as `qi` under `q * qi = 1`, so everything is
  division-free. No `ℝ`, no ordering, no numerical `q₀`.

## §3b-cond items 3 and 4

This is a standalone library file with no `.ts`/`.md` siblings, so the narrative
conditional banner (item 3) and the manifest `uses[]` entry (item 4) attach to
whichever content block later wraps it. Items 1, 2 and 5 are satisfied in the
Lean; the conditionality is stated in the module docstring meanwhile.

## Scope

**Scope-(a)** per AGENTS §"Before declaring 'refuted'". It constrains which
trace can feed the mass channel *given* the premise. It does **not**:

* establish the premise (that is bean `qou-n1dj`, still open);
* show convention C is mathematically illegitimate — C is a genuine member of
  the Ocneanu one-parameter family;
* resolve the corpus self-contradiction between the closed-form proof block and
  `h3-markov-wenzl-weights-context.md` §Scope (bean sub-task 2);
* touch the false sensitivity claim in that scope note (bean sub-task 3).

## What remains open

Unchanged in substance, sharper in form. The open item is now a single
categorical question about the mass fibre functor, with the downstream
implication machine-checked:

> Does the mass channel's trace arise as the categorical trace of the fibre
> action on `V^{⊗3}` (an instance of `MassTraceIsFibreCategorical R 2`), or is
> it an Ocneanu trace posited on all of `H₃(q)`?

Unchased in-tree hooks, from the bean: `QOU/Knots/KauffmanTL3.lean`,
`conj:s5-so3-fiber-action`, `QOU/MathlibExt/WenzlSchurElement.lean`.
