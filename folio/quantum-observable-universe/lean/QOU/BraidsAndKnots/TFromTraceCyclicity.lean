import QOU.MathlibExt.MarkovTrace

/-!
# QOU.BraidsAndKnots.TFromTraceCyclicity — time reversal as word reversal

Formalisation of [`conj:t-from-trace-cyclicity`]: time reversal `T` acts on
braid words by **word reversal**,

`T : σ_{i₁}^{ε₁} ⋯ σ_{i_ℓ}^{ε_ℓ} ↦ σ_{i_ℓ}^{ε_ℓ} ⋯ σ_{i₁}^{ε₁}`,

and the Markov trace is invariant under it.

## What is proved here, and what is assumed

The block's structural claims about `T` itself — that it is an involution,
that it preserves `q`, the colour-sheet flavours, the Hecke generator signs,
and acts purely on the ordering of crossings — are **unconditional
theorems** below (`timeReversal_involutive`, `timeReversal_crossings`,
`timeReversal_perm`). They need no hypothesis: on
`BraidWord n = List (Fin (n-1) × Bool)` reversal is `List.reverse`, which
keeps every `(generator, sign)` pair and only permutes their order.

The **trace invariance** `tr_M(β) = tr_M(β^T)` is the genuinely conjectural
content and is carried by the class field `trace_reversal_invariant`.

### It does not follow from cyclicity

The `.md` derives trace invariance "by the Markov trace cyclicity axiom
`tr_M(ab) = tr_M(ba)`". That step does not go through. Cyclicity — available
here as `QOU.markovTrace_append_comm` — gives invariance under *rotation* of
a word, `tr(vw) = tr(wv)`; reversal is a different operation, and for
non-commuting matrices `tr(ABC) ≠ tr(CBA)` in general. The claim is
plausible for Hecke characters by a *different* route (the anti-automorphism
fixing each generator, under which characters are invariant), but that route
is not formalised here and the corpus does not carry it. Hence the class
field rather than a proof.

-- Ref: [leitner2026] conj:t-from-trace-cyclicity
-- Ref: [jones1987] Hecke Algebra Representations of Braid Groups
-/

namespace QOU.BraidsAndKnots

/-! ### Symbol-collision note

`BraidWord` is **overloaded** in this corpus: `QOU.BraidWord` is the
`structure` in `QOU/PhotonThreading.lean`, while the braid word carried by
the Hecke representation machinery is the indexed abbreviation
`QOU.Archimedean.BraidWord (n : ℕ) := List (Fin (n-1) × Bool)`. A bare
`open QOU` resolves the name to the former and this file will not elaborate.
Everything below is therefore fully qualified. -/

variable {n d : ℕ}

/-- **Time reversal** on braid words: reverse the order of the crossings,
    keeping each generator index and each sign. -/
def timeReversal (w : Archimedean.BraidWord n) : Archimedean.BraidWord n :=
  w.reverse

@[simp] theorem timeReversal_nil :
    timeReversal ([] : Archimedean.BraidWord n) = [] := rfl

/-- **`T` is an involution**, `T² = id` — unconditional. -/
@[simp] theorem timeReversal_involutive (w : Archimedean.BraidWord n) :
    timeReversal (timeReversal w) = w :=
  List.reverse_reverse w

/-- **`T` preserves the crossing count** (it only reorders crossings). -/
@[simp] theorem timeReversal_crossings (w : Archimedean.BraidWord n) :
    (timeReversal w).length = w.length :=
  List.length_reverse

/-- **`T` preserves generator indices and signs**: the reversed word is a
    permutation of the original as a multiset of `(generator, sign)` pairs.
    This is the precise sense in which `T` "acts purely on the ordering of
    crossings" and "preserves Hecke generator signs". -/
theorem timeReversal_perm (w : Archimedean.BraidWord n) :
    (timeReversal w).Perm w :=
  List.reverse_perm w

/-- `T` reverses concatenation: `(v ++ w)^T = w^T ++ v^T`. -/
theorem timeReversal_append (v w : Archimedean.BraidWord n) :
    timeReversal (v ++ w) = timeReversal w ++ timeReversal v :=
  List.reverse_append

/-- **Time-reversal closure (conjecture).**

    The one unproved input: the Markov trace does not see word reversal.

    Axiomatised as a class per AGENTS.md §3b — providing an instance
    asserts the conjecture. The field is parameter-quantified over every
    representation and every braid word, i.e. it is stated in the shape of
    the claim rather than as an opaque `Prop`. -/
class TFromTraceCyclicity (n d : ℕ) where
  /-- **The conjecture**: the Markov trace of a braid word equals that of
      its time reversal, for every representation and every word. -/
  trace_reversal_invariant :
    ∀ (ρ : Archimedean.HeckeRep n d) (w : Archimedean.BraidWord n),
      MathlibExt.MarkovTrace.markovTrace ρ (timeReversal w)
        = MathlibExt.MarkovTrace.markovTrace ρ w

namespace TFromTraceCyclicity

/-- Conditional consequence: assuming the conjecture, a word and its time
    reversal are Markov-trace indistinguishable. -/
theorem markovTrace_timeReversal_eq [T : TFromTraceCyclicity n d]
    (ρ : Archimedean.HeckeRep n d) (w : Archimedean.BraidWord n) :
    MathlibExt.MarkovTrace.markovTrace ρ (timeReversal w)
      = MathlibExt.MarkovTrace.markovTrace ρ w :=
  T.trace_reversal_invariant ρ w

/-- Conditional: the same invariance stated in the other direction. -/
theorem markovTrace_eq_timeReversal [TFromTraceCyclicity n d]
    (ρ : Archimedean.HeckeRep n d) (w : Archimedean.BraidWord n) :
    MathlibExt.MarkovTrace.markovTrace ρ w
      = MathlibExt.MarkovTrace.markovTrace ρ (timeReversal w) :=
  (markovTrace_timeReversal_eq ρ w).symm

end TFromTraceCyclicity

end QOU.BraidsAndKnots
