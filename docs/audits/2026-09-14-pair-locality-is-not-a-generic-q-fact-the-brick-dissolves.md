# The `qou-ix0x` FIRST BRICK dissolves — pair-locality is not a generic-`q` fact, because it is not a corpus fact at all

Bean `qou-ix0x`. Measured 2026-09-14 on `main` `db8d3cefd9`. **No compute; this is a
corpus-status result**, which is what the brick asked for ("a Lean-readable question about one
hypothesis, needs no probe, and either answer is progress").

## The question as the bean posed it

> Does the corpus's `b3 = 0` proof survive at a root of unity? `b3_eq_zero_of_pairLocal`
> derives `b3 = 0` from pair-locality as a **hypothesis**. So the question is not whether the
> theorem holds — it does — but whether **pair-locality itself** is derivable at a root of
> unity, where `HH^k ≠ 0`. **If pair-locality is genuinely a generic-`q` fact**, the theorem
> simply has no hypothesis to stand on there, and `b3` is unconstrained by it.

The conditional is the load-bearing part, and **its antecedent is false as a description of
the corpus**. Pair-locality is not a generic-`q` fact. It is not a fact at any `q`. Nothing in
the corpus derives it, and the one thing the corpus *does* prove about it runs the other way.

## What is actually on `main`

**1. `PairLocal` contains no `q`.** Its definition is two equalities among a crossing model's
own weight fields, over a generic ring
([`QOU/Mass/CrossingModelPairLocality.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/CrossingModelPairLocality.lean)):

```lean
def PairLocal : Prop :=
  (∀ i j k, C.w3 i j k = C.w2 i j) ∧ (∀ i j, C.w4 i j = C.w2 i j)
```

`{R : Type*}`, no `q`, no order, no semisimplicity. So *"pair-locality at a root of unity"* is
not a well-posed specialisation of this predicate — there is nothing in it for a root of unity
to act on. Whether it holds depends entirely on how a given model *populates* `w2`, `w3`, `w4`,
which is a fact about the carrier's word, not about the fibre `H_n(q)`.

**2. The proved direction is the refutation, and it too is `q`-free.**
`not_pairLocal_of_b3_ne_zero` takes the measured AME cumulant `b₃ = +1.4262225` MeV
(`QOU.MassTheory.AmeBindingNotPairwise.ame_b3_eq`) and concludes `¬ C.PairLocal` — with no `q`
hypothesis and, in that file's own words, *"from data with no unsatisfied hypothesis at all"*.
Its header calls this *"the load-bearing direction"*.

**3. The bridge the bean treats as established is explicitly flagged as a conjecture — in the
very audit the bean cites for it.**
[`2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md`](2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md)
§2 argues semisimplicity ⇒ formality ⇒ nowhere to put a 3-body term, and then says, in its own
sentence:

> §2 states this as a **conjecture to prove, not a theorem** — the bridge from "formal" to
> "pair-local" is the thing to formalise first.

Its §2.1 "What is proved / recorded in the corpus" lists `HH^{k≥1} = 0` under semisimplicity,
and lists *"pair-locality ⇒ `b₃ = 0`"* and *"measured `b₃ ≠ 0` ⇒ not pair-local"*. It does
**not** list "pair-locality holds". There is no such entry because there is no such result.

## Consequence — the brick dissolves, for a better reason than it anticipated

The bean's two branches were: *pair-locality is generic-`q`* (⇒ go to a root of unity and the
hypothesis lapses), or *it is not* (⇒ the theorem constrains `b₃` there too). **Neither obtains.**

- `b₃` is **already** unconstrained by `b3_eq_zero_of_pairLocal` at every `q`, `q₀` included,
  because that theorem's hypothesis is nowhere established and is in fact refuted by AME.
- So **a root of unity buys nothing on this lever** — the lever was never locked. An agent who
  set out to prove "pair-locality fails at roots of unity" would be proving the negation of
  something nobody proved, against a predicate with no `q` in it.

**This does not weaken the Habiro/root-of-unity route. It re-aims it.** The thing that *is*
proved to hold at generic `q` and to fail at a root of unity is **semisimplicity**, and with it
`HH^{k≥1} = 0` — the audit's own "higher structure" row, whose status it records as *"absent:
`HH^{≥1} = 0` at generic `q`"* and whose visibility to the trace it records as **no**, since
`tr_M` is the Euler characteristic. That is the real target, and it is a statement about where
a 3-body datum can be *stored*, not about whether a crossing model happens to be pair-local.

So the sharpened brick is:

> Does `tr_M` — a cyclic 0-cocycle, the Euler characteristic of the Hochschild complex — acquire
> anything to see when `H_n(q)` is evaluated where it is **not** semisimple? Degree 0 of a
> complex does not change when higher degrees become non-zero; an Euler characteristic does.
> Which of those two is `tr_M`, and does the difference reach an evaluation at `q₀`?

That question is well-posed, is not about `PairLocal`, and is where the bean's own ROAST item 4
already pointed: *"the non-semisimplicity is at roots of unity; the substrate `q₀ ≈ 1.11` is not
one … a cyclotomic route has to explain how root-of-unity data reaches an evaluation at a
non-root-of-unity point."*

## What this does NOT claim

- **Not** that `b₃ = 0` is wrong in the model. It is `0` in the production model for reasons that
  have nothing to do with this file — the γγ assembly is exactly affine (#7287), the chain's
  `φᵀ₃` is a product (`B3SignOneRoot.b3corpus_chain`), and `b₃ = −φᵀ₃` with `φᵀ₃ > 0` by Ursell
  alternation (#7198). Those are independent and untouched.
- **Not** that the formality argument of §2 is wrong. It is an argument, correctly labelled a
  conjecture by its author; this note only records that it has not been promoted since.
- **Not** a derivation of `b₃ = +1.4262 MeV`, or of anything. It is a negative that stops one
  session being spent on a lever that is already open.
- **Not** a claim that `PairLocal` is a badly-chosen predicate. It is exactly right for what it
  does — it isolates the one hypothesis separating a crossing sum from a pairwise-additive
  binding, and the corpus uses it to *refute*, which is its strongest use.

## Method note, worth more than the result

The bean asserted *"pair-locality explained by `HH^k = 0` at generic `q`"* as background. Checking
it cost one `grep` of the cited audit, and the audit's own next sentence said it was conjectural.
**A bean is not a primary source** — the standing rule (AGENTS.md, on `qou-q7lf`) applies to one's
own beans as well as to siblings'. This one was mine.
