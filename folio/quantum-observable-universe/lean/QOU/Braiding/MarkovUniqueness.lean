import Mathlib.Algebra.Ring.Defs
/-
# QOU.Braiding.MarkovUniqueness

**The inductive step of Markov-trace uniqueness, proved; and what it reduces
`contact_is_markov` to.**

## Why this file exists

`QOU/Braiding/JonesMobiusDiagonal.lean` proves

    markov_eq_mobius_contact : markovTrace = twoPointReg - mobiusEnergy

from two `class JonesMobiusDiagonal` fields. That conclusion is sorry-free, but
what it derives is `A = B - (B - A)` over a bare `AddCommGroup` — true whatever
the symbols mean. **All of the content sits in one assumed field:**

    contact_is_markov : contact = markovTrace

that the diagonal contact coefficient of the categorical Möbius kernel
`tr(Δ(ϱ(s)) ⊗ Δ(ϱ(t)))` *is* the fundamental Markov trace. Per AGENTS.md
§"Axiomatization is NOT a Proof", assuming that field and consuming it
downstream is not proving it — and it is the whole Hecke↔O'Hara translation.

**This file does not close that gap.** It supplies the lever that makes closing
it a finite task rather than an open-ended one, and it is deliberate that the
lever is a *uniqueness* statement:

> A Markov trace is **determined** by normalisation, cyclicity and the Markov
> relation. So one never has to prove `contact = markovTrace` directly — it is
> enough to prove that `contact` *satisfies those properties*, and uniqueness
> does the rest.

That converts a bespoke, arc-specific assumption into a classical, citable one.

## What is proved here, and what is not

**PROVED (sorry-free, no hypothesis beyond the stated ones):**
`agree_on_stabilised` — the inductive step. If two functionals are cyclic,
satisfy the same Markov relation, and already agree on level `n`, they agree on
every stabilised element `a * σ * b` with `a, b` at level `n`. This is the step
that makes the induction go, and it is where cyclicity is actually used.

`markov_unique_of_spanning` — the uniqueness conclusion, with the spanning fact
as an **explicit hypothesis**.

**NOT PROVED, and named rather than hidden:** the spanning fact itself,
`H_{n+1} = H_n + H_n · σ_n · H_n`. It is classical (Jones 1985, Wenzl 1988) and
the corpus does not carry it: `braids-and-knots/markov-trace-inductive-limit.lean`
is by its own docstring a "Lean scaffold" whose closure is "the open R&D". It is
a hypothesis here, never a conclusion, so §3b-cond item 5 is satisfied — the
theorem *derives* from it rather than projecting it.

**Still missing for `contact_is_markov`, beyond this file** — stated so nobody
reads this as closing the arc:

1. the kernel `K_q(s,t) = tr(Δ(ϱ(s)) ⊗ Δ(ϱ(t)))` as an actual object, not an
   opaque scalar (`contact` is currently a bare `R` field);
2. the Hadamard finite-part residue on `s = t` as a construction — no
   derivative or distributional data exists in `LinkEmbedding` or
   `JonesMobiusDiagonal`;
3. a proof that (2) satisfies cyclicity and the Markov relation, which is what
   this file's uniqueness would then convert into `contact = markovTrace`.

So the honest status is: **the bridge is reduced from one opaque assumption to
one classical assumption plus two property checks.** Bean `qou-bn8e`.

## Base ring

Generic `[CommRing R]` and `[Ring A]` — nothing archimedean is used, per
AGENTS.md §7c. No `Real`, no ordering, no `q > 0`.

## References

- [leitner2026] climax-volume-mass/jones-mobius-diagonal
- [leitner2026] braids-and-knots/jones-markov-trace
-/

namespace QOU.Braiding.MarkovUniqueness

variable {R A : Type*} [CommRing R] [Ring A]

/-- **Markov-functional data**, relative to a level predicate `inH` (read: "lies
    in `H_n`"), a stabiliser `σ` (read: `σ_n`), and the Markov parameter `z`.

    Only the two properties the uniqueness argument actually consumes are
    recorded. Normalisation `tr 1 = 1` is deliberately *not* a field: it fixes
    the base case of the induction, not the step, and including it here would
    suggest the step needs it. -/
structure IsMarkov (inH : A → Prop) (σ : A) (z : R) (tr : A → R) : Prop where
  /-- Cyclicity: `tr (a * b) = tr (b * a)`. -/
  tr_comm : ∀ a b : A, tr (a * b) = tr (b * a)
  /-- The Markov relation: stabilising an element of `H_n` multiplies its trace
      by `z`. -/
  markov : ∀ x : A, inH x → tr (x * σ) = z * tr x

/-- **The inductive step of Markov-trace uniqueness.**

    Two functionals that are cyclic, share the same Markov relation, and already
    agree on level `n` agree on every *stabilised* element `a * σ * b` with
    `a, b` at level `n`.

    This is the whole content of the induction: cyclicity moves `b` to the front
    so that `b * a` is again at level `n`, the Markov relation then peels `σ`
    off, and the level-`n` agreement finishes it. Nothing here is specific to
    Hecke algebras — it holds for any ring and any level predicate closed under
    the product. -/
theorem agree_on_stabilised
    {inH : A → Prop} {σ : A} {z : R} {tr tr' : A → R}
    (h : IsMarkov inH σ z tr) (h' : IsMarkov inH σ z tr')
    (hclosed : ∀ a b : A, inH a → inH b → inH (b * a))
    (hagree : ∀ x : A, inH x → tr x = tr' x)
    {a b : A} (ha : inH a) (hb : inH b) :
    tr (a * σ * b) = tr' (a * σ * b) := by
  have hba : inH (b * a) := hclosed a b ha hb
  calc tr (a * σ * b)
      = tr (b * (a * σ)) := h.tr_comm _ _
    _ = tr (b * a * σ)   := by rw [mul_assoc]
    _ = z * tr (b * a)   := h.markov _ hba
    _ = z * tr' (b * a)  := by rw [hagree _ hba]
    _ = tr' (b * a * σ)  := (h'.markov _ hba).symm
    _ = tr' (b * (a * σ)) := by rw [mul_assoc]
    _ = tr' (a * σ * b)  := h'.tr_comm _ _

/-- **Markov-trace uniqueness, given spanning.**

    If every element of the next level is either at level `n` or stabilised from
    level `n`, then two Markov functionals agreeing on level `n` agree there
    too — so the Markov trace is determined by its defining properties.

    🛑 `hspan` is the classical spanning fact `H_{n+1} = H_n + H_n · σ_n · H_n`
    (Jones 1985, Wenzl 1988) and is an **explicit hypothesis**: this corpus does
    not prove it, and `markov-trace-inductive-limit.lean` records its closure as
    open. Do not cite this theorem as though the spanning fact were established.

    The `∨` form is the single-term case; the general statement needs additivity
    of `tr` across the spanning decomposition, which is why this is stated for a
    decomposition that has already been taken. -/
theorem markov_unique_of_spanning
    {inH : A → Prop} {inH' : A → Prop} {σ : A} {z : R} {tr tr' : A → R}
    (h : IsMarkov inH σ z tr) (h' : IsMarkov inH σ z tr')
    (hclosed : ∀ a b : A, inH a → inH b → inH (b * a))
    (hagree : ∀ x : A, inH x → tr x = tr' x)
    (hspan : ∀ y : A, inH' y →
      inH y ∨ ∃ a b : A, inH a ∧ inH b ∧ y = a * σ * b)
    (y : A) (hy : inH' y) :
    tr y = tr' y := by
  rcases hspan y hy with hlevel | ⟨a, b, ha, hb, rfl⟩
  · exact hagree y hlevel
  · exact agree_on_stabilised h h' hclosed hagree ha hb

/-- **What `contact_is_markov` reduces to.**

    Stated as a theorem rather than prose so the reduction is machine-checked:
    if the contact coefficient is *itself* a Markov functional agreeing with the
    Markov trace at level `n`, then on the spanned level it simply **is** the
    Markov trace — no separate identification is needed.

    This is the payoff of the file. `JonesMobiusDiagonal.contact_is_markov`
    assumes an equation; what actually has to be checked is that the diagonal
    residue satisfies cyclicity and the Markov relation. -/
theorem contact_eq_markov_of_isMarkov
    {inH inH' : A → Prop} {σ : A} {z : R} {contact markovTrace : A → R}
    (hc : IsMarkov inH σ z contact) (hm : IsMarkov inH σ z markovTrace)
    (hclosed : ∀ a b : A, inH a → inH b → inH (b * a))
    (hbase : ∀ x : A, inH x → contact x = markovTrace x)
    (hspan : ∀ y : A, inH' y →
      inH y ∨ ∃ a b : A, inH a ∧ inH b ∧ y = a * σ * b)
    (y : A) (hy : inH' y) :
    contact y = markovTrace y :=
  markov_unique_of_spanning hc hm hclosed hbase hspan y hy

end QOU.Braiding.MarkovUniqueness
