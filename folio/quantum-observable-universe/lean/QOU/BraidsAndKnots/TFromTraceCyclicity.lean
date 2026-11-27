import QOU.Core.MarkovTrace
import HeckeTemperleyLieb.HeckeH3AlgebraInstance

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
fixing each generator, under which characters are invariant). Hence the class
field rather than a proof.

**Status (2026-11-27): proved.** The class has an instance for every `n`
and `d`, `QOU.BraidsAndKnots.TFromTraceCyclicityAll.tFromTraceCyclicity`.
The proof (`QOU.IwahoriHecke.HeckeTraceReversal`) shows every cyclic
functional on a type-`A` Hecke algebra is invariant under the anti-involution
fixing the generators, by induction along `H₁ ⊂ H₂ ⊂ ⋯` using only the
double-coset decomposition `H_{k+1} = H_k + H_k s_k H_k`. For Markov traces a
second proof goes through uniqueness
(`QOU.IwahoriHecke.MarkovTraceSymmetries.markov_reverse`), and
`TFromTraceCyclicityH3` has an elementary `n = 3` argument.

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

/-! ## Unconditional Anti-Involution Word Reversal & Markov-Trace Invariance on `H_3(R, h)` -/

section H3WordReversalTraceInvariance

open QOU.Machinery.H3

/-- Generic word-reversal anti-homomorphism law `(u ++ v).reverse = v.reverse ++ u.reverse`. -/
theorem reverse_append_anti {α : Type*} (u v : List α) :
    (u ++ v).reverse = v.reverse ++ u.reverse :=
  List.reverse_append

/-- Word-reversal linear map on the 6-dimensional normal-form coordinates
    `[1, σ₀, σ₁, L₊, L₋, e⁻]` of `H_3(R, h)`: fixes `1, σ₀, σ₁, e⁻ = σ₀σ₁σ₀` and
    swaps `L₊ = σ₁σ₀ ↔ L₋ = σ₀σ₁`. -/
def revNF {R : Type*} (v : Fin 6 → R) : Fin 6 → R :=
  ![v 0, v 1, v 2, v 4, v 3, v 5]

/-- Word-reversal operator `rev` on `H3A R h` over any `[CommRing R]`. -/
def revH3 {R : Type*} [CommRing R] {h : R} (x : H3A R h) : H3A R h :=
  ⟨revNF x.v⟩

@[simp]
theorem revNF_involutive {R : Type*} (v : Fin 6 → R) :
    revNF (revNF v) = v := by
  funext i
  fin_cases i <;> simp [revNF]

/-- **`revH3` is an involution** (`rev² = id`) on `H3A R h`. -/
@[simp]
theorem revH3_involutive {R : Type*} [CommRing R] {h : R} (x : H3A R h) :
    revH3 (revH3 x) = x :=
  H3A.ext (revNF_involutive x.v)

@[simp]
theorem revH3_one {R : Type*} [CommRing R] {h : R} :
    revH3 (1 : H3A R h) = 1 := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [revH3, revNF, unitNF]

theorem revH3_add {R : Type*} [CommRing R] {h : R} (x y : H3A R h) :
    revH3 (x + y) = revH3 x + revH3 y := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [revH3, revNF, Pi.add_apply]

theorem revH3_smul {R : Type*} [CommRing R] {h : R} (c : R) (x : H3A R h) :
    revH3 (c • x) = c • revH3 x := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [revH3, revNF, Pi.smul_apply]

/-- Explicit action of `revH3` on the 6 GB normal-form basis vectors:
    fixes `1`, `σ₀`, `σ₁`, `e⁻` and swaps `L₊ ↔ L₋`. -/
theorem revH3_basis_action {R : Type*} [CommRing R] {h : R} :
    revH3 (1 : H3A R h) = 1 ∧
    revH3 (⟨![0, 1, 0, 0, 0, 0]⟩ : H3A R h) = ⟨![0, 1, 0, 0, 0, 0]⟩ ∧
    revH3 (⟨![0, 0, 1, 0, 0, 0]⟩ : H3A R h) = ⟨![0, 0, 1, 0, 0, 0]⟩ ∧
    revH3 (⟨![0, 0, 0, 1, 0, 0]⟩ : H3A R h) = ⟨![0, 0, 0, 0, 1, 0]⟩ ∧
    revH3 (⟨![0, 0, 0, 0, 1, 0]⟩ : H3A R h) = ⟨![0, 0, 0, 1, 0, 0]⟩ ∧
    revH3 (⟨![0, 0, 0, 0, 0, 1]⟩ : H3A R h) = ⟨![0, 0, 0, 0, 0, 1]⟩ := by
  refine ⟨revH3_one, ?_, ?_, ?_, ?_, ?_⟩ <;>
    apply H3A.ext <;> funext i <;> fin_cases i <;> simp [revH3, revNF]

/-- **Anti-automorphism law on `H_3(R, h)`** over any `[CommRing R]`:
    `revH3 (x * y) = revH3 y * revH3 x`. -/
theorem revH3_mul {R : Type*} [CommRing R] {h : R} (x y : H3A R h) :
    revH3 (x * y) = revH3 y * revH3 x := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [revH3, revNF, mulNF, mulσ₀, mulσ₁] <;> ring

/-- **Unconditional Markov-trace invariance under word reversal on `H_3(R, h)`**
    over any `[CommRing R]`: `tr_M (rev x) = tr_M x`, because `rev` fixes `1, σ₀, σ₁, e⁻`
    and swaps `L₊ ↔ L₋`, both of which have Markov trace `z²`! -/
theorem trM_revNF {R : Type*} [CommRing R] (z h : R) (v : Fin 6 → R) :
    trM z h (revNF v) = trM z h v := by
  simp only [trM, TRM, revNF, Fin.sum_univ_six, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val]
  ring

theorem trace_revH3 {R : Type*} [CommRing R] (z h : R) (x : H3A R h) :
    H3A.trace z (revH3 x) = H3A.trace z x :=
  trM_revNF z h x.v

/-- Evaluation of a single 3-strand signed crossing `(i, b)` in `H3A R h`
    (`σ_i` for `b = true`, `σ_i⁻¹ = σ_i - h • 1` for `b = false`). -/
def evalH3Letter {R : Type*} [CommRing R] (h : R) (p : Fin 2 × Bool) : H3A R h :=
  let gen : H3A R h := if p.1.val = 0 then ⟨![0, 1, 0, 0, 0, 0]⟩ else ⟨![0, 0, 1, 0, 0, 0]⟩
  if p.2 then gen else gen - h • (1 : H3A R h)

theorem revH3_evalH3Letter {R : Type*} [CommRing R] (h : R) (p : Fin 2 × Bool) :
    revH3 (evalH3Letter h p) = evalH3Letter h p := by
  obtain ⟨i, b⟩ := p
  fin_cases i <;> cases b <;>
    apply H3A.ext <;> funext k <;> fin_cases k <;>
    simp [evalH3Letter, sub_eq_add_neg, revH3, revNF, unitNF]

/-- Evaluation of any 3-strand signed braid word `w : Archimedean.BraidWord 3` in `H3A R h`. -/
def evalH3Word {R : Type*} [CommRing R] (h : R) : Archimedean.BraidWord 3 → H3A R h
  | [] => 1
  | p :: rest => evalH3Letter h p * evalH3Word h rest

theorem evalH3Word_append {R : Type*} [CommRing R] (h : R)
    (u v : Archimedean.BraidWord 3) :
    evalH3Word h (u ++ v) = evalH3Word h u * evalH3Word h v := by
  induction u with
  | nil => simp [evalH3Word]
  | cons p tl ih => simp [evalH3Word, ih, mul_assoc]

/-- Word reversal on `Archimedean.BraidWord 3` intertwines directly with `revH3` on `H3A R h`. -/
theorem evalH3Word_timeReversal {R : Type*} [CommRing R] (h : R)
    (w : Archimedean.BraidWord 3) :
    evalH3Word h (timeReversal w) = revH3 (evalH3Word h w) := by
  induction w with
  | nil => simp [timeReversal, evalH3Word]
  | cons p tl ih =>
    have hrev : timeReversal (p :: tl) = timeReversal tl ++ [p] := List.reverse_cons
    rw [hrev, evalH3Word_append, ih]
    have hsingle : evalH3Word h [p] = evalH3Letter h p := by simp [evalH3Word]
    rw [hsingle, ← revH3_evalH3Letter h p, ← revH3_mul]
    rfl

/-- **Unconditional Markov-trace invariance under `timeReversal`** for every 3-strand
    signed braid word `w : Archimedean.BraidWord 3` over any `[CommRing R]`. -/
theorem trace_evalH3Word_timeReversal {R : Type*} [CommRing R] (z h : R)
    (w : Archimedean.BraidWord 3) :
    H3A.trace z (evalH3Word h (timeReversal w)) = H3A.trace z (evalH3Word h w) := by
  rw [evalH3Word_timeReversal, trace_revH3]

end H3WordReversalTraceInvariance

end QOU.BraidsAndKnots
