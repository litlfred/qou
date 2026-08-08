/-
# One named premise decides the Borromean trace convention

**What this file does, and what it deliberately does not.** Bean `qou-n1dj`
asks a single categorical question: does the fibre functor for the **mass**
channel land in `Rep(SU_q(2)) ≃ TL₃`, or in the full `H₃(q)`? The answer
selects between two normalised Markov traces on `H₃(q)` that sit `195 ppm`
apart on the Borromean braid — convention **D** (Jones / Temperley–Lieb, what
production consumes) and convention **C** (full-Hecke Ocneanu / Wenzl
`z`-trace, what the scope note of `prop:h3-markov-wenzl-weights` asserts).

This file **does not answer that question.** What it does is collapse it to
*one* premise, with every other link machine-checked, so that what remains
open is crisp, named, and auditable:

> **The premise (open).** The mass channel's trace is the **categorical trace
> of the fibre action** on `V^{⊗3}`, rather than an abstract Ocneanu trace
> posited on all of `H₃(q)`.

Granting that premise — and nothing else beyond results already proved
sorry-free in this repository — convention D follows. "Conditional-proved ≠
premise-established" (AGENTS.md): this is an implication, and the antecedent
is exactly the thing bean `qou-n1dj` is open on.

## The chain, and where each link comes from

| link | statement | status |
|---|---|---|
| 1 | `dim V = 2` — the gauge group of tensor automorphisms is `SU(2)`, fibre `ℂ²` | `thm:su2-emergence` (corpus); enters here as the **explicit hypothesis** `hN : N = 2` |
| 2 | at `N = 2` the alternating Schur–Weyl channel `λ = (1³)` is **absent** from `V^{⊗3}` | **proved**, `QOU.Eightfold.RowCapObstruction.weyl_dim_alt_eq_zero_iff` (`C(N,3) = 0 ↔ N < 3`) |
| 3 | a trace that is the categorical trace of the fibre action puts **no weight** on an absent channel, and **does** carry a present one | **the premise** — `MassTraceIsFibreCategorical` below |
| 4 | `y_(1³) = 0` together with faithfulness on `TL₃` forces `y = ([4]_q/[2]_q³, 1/[2]_q², 0)` and `z·[2]_q = q²` | **proved**, `QOU.BraidsAndKnots.markovWeights_eq_jones_of_threeRow_eq_zero` |

Links 2 and 4 are sorry-free theorems; link 1 is a corpus theorem carried as a
visible hypothesis; link 3 is the class. Composing them is
`markovWeights_eq_jones_of_fibre_categorical`.

## Why the class is honest about being partial

`MassTraceIsFibreCategorical` does **not** attempt to formalise quantum
Schur–Weyl duality (no such development exists in this tree). It axiomatises
only the two *support* consequences of the premise that the forcing argument
actually consumes:

* **row-cap support** — a channel whose Weyl module is `0`-dimensional receives
  weight `0`;
* **non-degeneracy** — a channel the fibre genuinely supplies receives a
  **nonzero** weight (this is faithfulness on `TL₃`, and it is what kills the
  degenerate root `z = q` of the Temperley–Lieb condition).

Both are `q`-independent, which is the point: the row cap constrains `dim V`,
and Drinfeld–Jimbo quantisation does not change dimensions. Deliberately
*absent* from the class are the weight **magnitudes**: at `q ≠ 1` those are
quantum dimensions, not the classical Weyl dimensions, and asserting the
classical values would be a *false* premise. Because the class assumes strictly
less than the physical premise it names, the conditional theorem is
correspondingly **stronger** — a full formalisation of the premise would
*imply* these fields, not conflict with them.

## Non-degeneracy of the conditional (AGENTS §3b-cond item 5)

The class carries **hypotheses**, never the conclusion. Nothing in it mentions
`q`, the Ocneanu parameter `z`, the Jones weight vector, or convention D; the
conclusion `[2]_q²·y_(2,1) = 1 ∧ y_(3) = 1 − 2y_(2,1) ∧ z·[2]_q = q²` is
**derived** from the class fields plus the three Markov equations, via the
proved uniqueness theorem. It is not a projection `:= ctx.weights_eq_D`.

Both class fields are load-bearing, and both are exercised:

* `fibre_ne_zero_of_zero_dimensional` — with `N = 0` the row-cap fields kill
  *all three* weights, contradicting normalisation. So the class plus
  normalisation already forces a nonempty fibre.
* `weightAlt_ne_zero_at_three` — the class **alone** does not force
  `y_(1³) = 0`: at `N = 3` it admits an instance with a nonzero alternating
  weight. The vanishing comes from `hN : N = 2`, i.e. from `thm:su2-emergence`,
  which is therefore genuinely used and not decoration.

## §3b-cond items 3 and 4

This is a standalone library file with no `.ts`/`.md` content-block siblings, so
the narrative conditional banner (item 3) and the manifest `uses[]` entry
(item 4) attach to whichever content block later wraps it; the conditionality
is stated in this docstring in the meantime. Items 1 (class axiomatisation),
2 (explicit class hypothesis on the Lean side) and 5 (non-degeneracy) are
satisfied here.

## Base ring (§7c)

Generic `{R : Type*} [CommRing R]`, with `[IsDomain R]` only where the proved
uniqueness theorem needs to cancel a nonzero factor. `q⁻¹` is carried as a
separate element `qi` constrained by `q * qi = 1`, so everything is
division-free. No `ℝ`, no ordering, no numerical `q₀` — this is the fibre
(formal `q`) side of the substrate/archimedean wall.

## Scope

A **scope-(a)** result in the sense of AGENTS §"Before declaring 'refuted'":
it constrains which trace can feed the mass channel *given* the premise. It
does not establish the premise, does not show convention C is mathematically
illegitimate (it is a genuine member of the Ocneanu family), and does not
resolve the corpus self-contradiction catalogued in bean `qou-n1dj`.
-/
import QOU.BraidsAndKnots.MarkovTraceTLUniqueness
import QOU.Eightfold.RowCapObstruction

namespace QOU.BraidsAndKnots

open QOU.Eightfold.RowCapObstruction

variable {R : Type*} [CommRing R]

/-- **The one open premise, axiomatised: the mass-channel trace is the
categorical trace of the fibre action on `V^{⊗3}`.**

An instance records the three Frobenius weights `(y_(3), y_(2,1), y_(1³))` of
the mass-channel trace on `H₃(q)`, together with the two support properties
that follow from its being the categorical trace of the action of a fibre of
dimension `N`:

* `weight*_eq_zero_of_dim_eq_zero` — **row-cap support.** Quantum Schur–Weyl
  duality decomposes `V^{⊗3} = ⊕_{λ ⊢ 3} S^λ ⊗ V_λ` with the row cap
  `ℓ(λ) ≤ N`; a partition violating the cap has `dim V_λ = 0` and therefore
  contributes no summand at all. A trace computed *from the fibre action* can
  put no weight on a channel that is absent from the module it acts on.

* `weightMixed_ne_zero_of_dim_ne_zero` — **non-degeneracy / faithfulness.**
  Conversely a channel the fibre genuinely supplies is genuinely seen: its
  weight is nonzero. This is faithfulness on the surviving (Temperley–Lieb)
  part, and it is what excludes the degenerate root `z = q` of the
  Temperley–Lieb condition (`markovWeights_degenerate_root`).

Both properties are independent of the deformation parameter, because the row
cap constrains `dim V` and quantisation does not change dimensions.

**What is not asserted.** The weight *magnitudes*. At `q ≠ 1` these are quantum
dimensions rather than the classical Weyl dimensions `weylDim*`, so pinning
them to the classical values would be false. Nothing here mentions `q`, the
Ocneanu parameter, or the Jones weight vector — those appear only in the
*conclusions* of the theorems below.

An instance of this class is not a proof of the premise; it is the premise,
named. Bean `qou-n1dj` is open on whether the mass channel admits one. -/
class MassTraceIsFibreCategorical (R : Type*) [CommRing R] (N : ℕ) where
  /-- Frobenius weight of the symmetric channel `λ = (3)`. -/
  weightSym : R
  /-- Frobenius weight of the mixed channel `λ = (2,1)`; this is the
  Temperley–Lieb / two-row block. -/
  weightMixed : R
  /-- Frobenius weight of the alternating channel `λ = (1³)`; this is the block
  the row cap kills at `N = 2`. -/
  weightAlt : R
  /-- Row-cap support in the symmetric channel. -/
  weightSym_eq_zero_of_dim_eq_zero : weylDimSym N = 0 → weightSym = 0
  /-- Row-cap support in the mixed channel. -/
  weightMixed_eq_zero_of_dim_eq_zero : weylDimMixed N = 0 → weightMixed = 0
  /-- Row-cap support in the alternating channel — the field that, at `N = 2`,
  supplies the Temperley–Lieb condition `y_(1³) = 0`. -/
  weightAlt_eq_zero_of_dim_eq_zero : weylDimAlt N = 0 → weightAlt = 0
  /-- Non-degeneracy: a mixed channel the fibre supplies is genuinely carried.
  Equivalently, faithfulness on `TL₃`. -/
  weightMixed_ne_zero_of_dim_ne_zero : weylDimMixed N ≠ 0 → weightMixed ≠ 0

namespace MassTraceIsFibreCategorical

/-- **The Temperley–Lieb condition, derived from the premise at `dim V = 2`.**

At `N = 2` the alternating Schur–Weyl channel is absent
(`weylDimAlt 2 = C(2,3) = 0`, `weyl_dim_alt_eq_zero_iff`), so the row-cap field
of the premise forces its Frobenius weight to vanish. This is the link that
turns `thm:su2-emergence` into the Temperley–Lieb condition. -/
theorem weightAlt_eq_zero_at_two (ctx : MassTraceIsFibreCategorical R 2) :
    ctx.weightAlt = 0 :=
  ctx.weightAlt_eq_zero_of_dim_eq_zero (no_singlet_of_lt_three (by norm_num))

/-- **Faithfulness on `TL₃`, derived from the premise at `dim V = 2`.**

At `N = 2` the mixed channel *is* present (`weylDimMixed 2 = 2`, the spin-`1/2`
doublet), so the non-degeneracy field forces its weight to be nonzero. This is
the link that excludes the degenerate root `z = q`. -/
theorem weightMixed_ne_zero_at_two (ctx : MassTraceIsFibreCategorical R 2) :
    ctx.weightMixed ≠ 0 :=
  ctx.weightMixed_ne_zero_of_dim_ne_zero (by decide)

end MassTraceIsFibreCategorical

/-- **Conditional theorem — the fibre-categorical premise plus `dim V = 2`
forces convention D.**

Let the mass-channel trace satisfy the premise `MassTraceIsFibreCategorical`
(the categorical trace of the fibre action on `V^{⊗3}`; the one open input),
let the fibre be two-dimensional (`hN : N = 2`, supplied by
`thm:su2-emergence`), and let the three Markov equations hold against the
`H₃(q)` `q`-character table on the class representatives `1`, `σ₀`, `σ₀σ₁`,

  `tr 1 = 1`,   `tr σ₀ = z`,   `tr σ₀σ₁ = z²`

(hypotheses `hnorm`, `hsigma`, `hsigmasigma`; `qi` is `q⁻¹`, constrained by
`hqi : q * qi = 1`, so the statement is division-free).

Then the weight vector and the Ocneanu parameter are completely determined:

  `[2]_q² · y_(2,1) = 1`,   `y_(3) = 1 − 2 y_(2,1)`,   `z · [2]_q = q²`,

with `[2]_q = q + qi`. Solving the first gives `y = ([4]_q/[2]_q³, 1/[2]_q², 0)`
— the Jones / Temperley–Lieb closure, **convention D**. Convention C, whose
Ocneanu parameter satisfies `z·[2]_q ≠ q²`, is thereby excluded.

**This is an implication, not a resolution.** The conclusion is derived — from
the class fields (which mention neither `q` nor `z` nor D), the proved row-cap
obstruction, and the proved Markov-trace uniqueness theorem. What it buys is
that the D-vs-C question now rests on exactly one named, unproved premise
instead of on a numerical coincidence with CODATA. Whether the mass channel
satisfies that premise is bean `qou-n1dj`, and it is open. -/
theorem markovWeights_eq_jones_of_fibre_categorical [IsDomain R] {N : ℕ}
    (ctx : MassTraceIsFibreCategorical R N) (hN : N = 2)
    (q qi z : R)
    (hqi : q * qi = 1)
    (hnorm : ctx.weightSym + 2 * ctx.weightMixed + ctx.weightAlt = 1)
    (hsigma : q * ctx.weightSym + (q - qi) * ctx.weightMixed
      + (-qi) * ctx.weightAlt = z)
    (hsigmasigma : q ^ 2 * ctx.weightSym + (-1) * ctx.weightMixed
      + qi ^ 2 * ctx.weightAlt = z ^ 2) :
    (q + qi) ^ 2 * ctx.weightMixed = 1
      ∧ ctx.weightSym = 1 - 2 * ctx.weightMixed
      ∧ z * (q + qi) = q ^ 2 := by
  subst hN
  exact markovWeights_eq_jones_of_threeRow_eq_zero q qi z
    ctx.weightSym ctx.weightMixed ctx.weightAlt hqi hnorm hsigma hsigmasigma
    ctx.weightAlt_eq_zero_at_two ctx.weightMixed_ne_zero_at_two

/-- **Convention C is excluded under the premise.**

Contrapositive of the conditional theorem in the form that separates the two
production conventions: a mass-channel trace satisfying the fibre-categorical
premise at `dim V = 2` **cannot** have an Ocneanu parameter with
`z·[2]_q ≠ q²`. Applied to the Wenzl `z`-trace at
`z = 1/(q^{1/2} + q^{-1/2})` (convention C), this says C is not the categorical
trace of a two-dimensional fibre action on `V^{⊗3}`.

Again conditional: it excludes C *given* the premise, not absolutely. -/
theorem ocneanu_eq_jones_of_fibre_categorical [IsDomain R] {N : ℕ}
    (ctx : MassTraceIsFibreCategorical R N) (hN : N = 2)
    (q qi z : R)
    (hqi : q * qi = 1)
    (hnorm : ctx.weightSym + 2 * ctx.weightMixed + ctx.weightAlt = 1)
    (hsigma : q * ctx.weightSym + (q - qi) * ctx.weightMixed
      + (-qi) * ctx.weightAlt = z)
    (hsigmasigma : q ^ 2 * ctx.weightSym + (-1) * ctx.weightMixed
      + qi ^ 2 * ctx.weightAlt = z ^ 2)
    (hC : z * (q + qi) ≠ q ^ 2) : False :=
  hC (markovWeights_eq_jones_of_fibre_categorical ctx hN q qi z hqi hnorm hsigma
    hsigmasigma).2.2

/-! ## Both class fields are load-bearing

Two lemmas showing the premise is neither vacuous nor doing the whole job by
itself — the `N = 2` input from `thm:su2-emergence` is genuinely used. -/

/-- **The premise plus normalisation forces a nonempty fibre.**

At `N = 0` every Weyl dimension vanishes (`C(2,3) = C(1,3) = C(0,3) = 0`), so
all three row-cap fields fire and the trace is identically zero — contradicting
`tr 1 = 1`. Hence the row-cap fields have genuine content: they are strong
enough to be *refutable* against normalisation. -/
theorem fibre_ne_zero_of_zero_dimensional [Nontrivial R]
    (ctx : MassTraceIsFibreCategorical R 0)
    (hnorm : ctx.weightSym + 2 * ctx.weightMixed + ctx.weightAlt = 1) :
    False := by
  have hs : ctx.weightSym = 0 :=
    ctx.weightSym_eq_zero_of_dim_eq_zero (by decide)
  have hm : ctx.weightMixed = 0 :=
    ctx.weightMixed_eq_zero_of_dim_eq_zero (by decide)
  have ha : ctx.weightAlt = 0 :=
    ctx.weightAlt_eq_zero_of_dim_eq_zero (by decide)
  rw [hs, hm, ha] at hnorm
  simp at hnorm

/-- Witness instance at `N = 3`: all three Weyl dimensions are nonzero there
(`10`, `8`, `1`), so every row-cap implication is vacuously satisfied and the
alternating weight is free to be nonzero. Used only by
`weightAlt_ne_zero_at_three` to show `hN : N = 2` is load-bearing. -/
def fibreCategoricalAtThree (R : Type*) [CommRing R] [Nontrivial R] :
    MassTraceIsFibreCategorical R 3 where
  weightSym := 1
  weightMixed := 1
  weightAlt := 1
  weightSym_eq_zero_of_dim_eq_zero h := absurd h (by decide)
  weightMixed_eq_zero_of_dim_eq_zero h := absurd h (by decide)
  weightAlt_eq_zero_of_dim_eq_zero h := absurd h (by decide)
  weightMixed_ne_zero_of_dim_ne_zero _ := one_ne_zero

/-! ### The conditional is not vacuous — convention D is a model

A conditional theorem whose antecedent is unsatisfiable proves nothing. The
next two declarations rule that out: at `N = 2` the premise **is** satisfiable
*together with* all three Markov equations, and the model realising it is
convention D itself. `t` plays the role of `[2]_q⁻¹ = 1/(q + q⁻¹)`, carried as
an element constrained by `h2 : (q + qi) * t = 1` so the construction stays
division-free (§7c). -/

/-- Convention D as a model of the premise at `N = 2`: weights
`(1 − 2t², t², 0)` with `t = [2]_q⁻¹`, i.e. `y_(2,1) = 1/[2]_q²` and
`y_(1³) = 0` — the Jones / Temperley–Lieb closure.

The row-cap fields hold because at `N = 2` the alternating weight is `0` by
construction while the symmetric and mixed channels are present
(`weylDimSym 2 = 4`, `weylDimMixed 2 = 2`), and non-degeneracy holds because
`[2]_q²·t² = 1` makes `t² ≠ 0` in any nontrivial ring. -/
def fibreCategoricalJones [Nontrivial R] (q qi t : R) (_hqi : q * qi = 1)
    (h2 : (q + qi) * t = 1) : MassTraceIsFibreCategorical R 2 where
  weightSym := 1 - 2 * t ^ 2
  weightMixed := t ^ 2
  weightAlt := 0
  weightSym_eq_zero_of_dim_eq_zero h := absurd h (by decide)
  weightMixed_eq_zero_of_dim_eq_zero h := absurd h (by decide)
  weightAlt_eq_zero_of_dim_eq_zero _ := rfl
  weightMixed_ne_zero_of_dim_ne_zero _ := fun h => by
    have hone : (q + qi) ^ 2 * t ^ 2 = 1 := by
      linear_combination ((q + qi) * t + 1) * h2
    rw [h, mul_zero] at hone
    exact zero_ne_one hone

/-- **The premise is satisfiable at `dim V = 2`, and convention D realises it.**

There exists a trace satisfying the fibre-categorical premise at `N = 2`
*together with* all three Markov equations — namely the Jones weight vector
`(1 − 2t², t², 0)` at Ocneanu parameter `z = q − t`, `t = [2]_q⁻¹`. Its
parameter satisfies `z·[2]_q = q²`, exactly the conclusion of
`markovWeights_eq_jones_of_fibre_categorical`.

So the conditional theorem is **not** vacuously true: its antecedent has a
model, and the model is the convention production already uses. What remains
open is not whether such a trace exists but whether the *mass channel's* trace
is one — bean `qou-n1dj`. -/
theorem exists_fibre_categorical_markov_trace [Nontrivial R] (q qi t : R)
    (hqi : q * qi = 1) (h2 : (q + qi) * t = 1) :
    ∃ (ctx : MassTraceIsFibreCategorical R 2) (z : R),
      ctx.weightSym + 2 * ctx.weightMixed + ctx.weightAlt = 1
      ∧ q * ctx.weightSym + (q - qi) * ctx.weightMixed
          + (-qi) * ctx.weightAlt = z
      ∧ q ^ 2 * ctx.weightSym + (-1) * ctx.weightMixed
          + qi ^ 2 * ctx.weightAlt = z ^ 2
      ∧ z * (q + qi) = q ^ 2 := by
  refine ⟨fibreCategoricalJones q qi t hqi h2, q - t, ?_, ?_, ?_, ?_⟩
  · show (1 - 2 * t ^ 2) + 2 * t ^ 2 + (0 : R) = 1
    ring
  · show q * (1 - 2 * t ^ 2) + (q - qi) * t ^ 2 + (-qi) * (0 : R) = q - t
    linear_combination (-t) * h2
  · show q ^ 2 * (1 - 2 * t ^ 2) + (-1) * t ^ 2 + qi ^ 2 * (0 : R) = (q - t) ^ 2
    linear_combination (-2 * q * t) * h2 + 2 * t ^ 2 * hqi
  · linear_combination hqi - h2

/-- **`hN : N = 2` is load-bearing: the premise alone does not give
Temperley–Lieb.**

At `N = 3` the class admits an instance whose alternating weight is nonzero, so
`weightAlt_eq_zero_at_two` really consumes the two-dimensionality of the fibre
— i.e. `thm:su2-emergence` is used, not decorative. Equivalently: were the mass
fibre three-dimensional, the fibre-categorical premise would be compatible with
a nonzero `(1³)` weight, hence with convention C. -/
theorem weightAlt_ne_zero_at_three (R : Type*) [CommRing R] [Nontrivial R] :
    (fibreCategoricalAtThree R).weightAlt ≠ 0 := one_ne_zero

end QOU.BraidsAndKnots
