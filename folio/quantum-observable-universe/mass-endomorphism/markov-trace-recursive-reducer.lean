import Mathlib.Data.List.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

-- `u` is the level of the coefficient ring `R` in the signatures below;
-- naming it is required once auto-bound universes are off.
universe u

/-!
# Recursive symbolic Markov-trace reducer for `H_n(q)`

This file formalises the *signature* of the recursive symbolic
Markov-trace reducer for arbitrary braid words in `H_n(q)`.

The algorithm:

  1. Expand the braid word into the canonical Hecke basis
     `{T_w : w ∈ S_n}` via iterated Hecke quadratic.
  2. For each basis element `T_w`, recursively compute `tr_M(T_w)`:
     • base case: `w = id` ⇒ `tr_M = 1`;
     • if `w` doesn't use the highest generator `σ_{n-2}` (0-indexed),
       truncate to `S_{n-1}` and recurse with smaller ambient `n`;
     • otherwise peel one `σ_{n-2}` via cyclic + Markov axiom,
       gaining a factor of `z`, and reduce the remainder back into
       the `H_n` basis (which may invoke the Hecke quadratic on
       remaining `σ_{n-2}` occurrences).
  3. Sum the contributions weighted by the basis-expansion coefficients.

We formalise:

  • A computable evaluator `trWord` (section `Evaluator`), structurally
    recursive and so terminating by Lean's own check. It satisfies every
    `IsMarkovTrace` axiom (`trWord_isMarkovTrace`), so a Markov trace exists
    for every `z, h` (Ocneanu existence, `exists_isMarkovTrace`).
  • A terminating *shape* only (`markovTraceRecursiveReducer_terminates`):
    it is met by a constant tracer, so it says nothing about the actual
    reducer. Termination of the algorithm is proved in the `.md` sibling,
    not here.
  • The disjoint-product law `markovTrace_disjointProduct`, proved from
    the axioms of `IsMarkovTrace`: `tr(α · β↑) = tr(α) · tr(β)` with `α` on
    `σ_0, …, σ_k` and `β↑` on `σ_{k+1}, …` (0-indexed). The two clusters
    share one strand. The split form, with an unused slot between them,
    additionally needs shift invariance of the trace, which is not
    formalised.
  • Uniqueness `markovTrace_unique`: the axioms of `IsMarkovTrace` fix the
    trace on every positive word, so the reducer's output, which uses only
    those axioms, is the trace. With existence, every Markov trace equals the
    evaluator (`isMarkovTrace_eq_trWord`).

Ref: [jones1987] Hecke algebra representations of braid groups,
Annals of Math. 126, 335-388.
Ref: [kassel1995] Quantum Groups, Springer GTM 155, Ch. III §3.
Ref: [wenzl1988] Hecke algebras of type A_n and subfactors,
Inventiones Math. 92, 349-383.
LaTeX label: `prop:markov-trace-recursive-reducer`.
-/

namespace QOU.BraidKnot

/-- 0-indexed reduced word: a list of generator indices in
    `Fin (n - 1)` (= `{0, ..., n - 2}`) representing a braid in
    `H_n(q)`.  Empty list = identity. -/
abbrev ReducedWord (n : ℕ) := List (Fin (n - 1))

/-- Coxeter length of a permutation, abstracted by its reduced-word
    representation.  Concrete `S_n` instantiation defers to Mathlib's
    `Equiv.Perm.coxeterLength` (when needed). -/
abbrev coxeterLength {n : ℕ} (w : ReducedWord n) : ℕ := w.length

/-- Statement-level reducer signature: given a braid word in `B_n`
    (encoded as a list of signed generator indices), produces a
    symbolic value `R` representing `tr_M` in the chosen base ring.

    The concrete implementation lives in `markov_trace_recursive.py`
    via sympy.  This Lean signature captures the algorithmic
    interface and termination properties. -/
abbrev MarkovTraceReducerSig (R : Type u) : Type u :=
  ∀ (_n : ℕ), List ℤ → R

/-- A fueled tracer: signature of a recursive function that returns
    `none` when fuel is exhausted, and `some (r, fuel')` when it
    successfully produces a result `r` with leftover fuel `fuel'`.

    Used to express termination as "with fuel ≥ ℓ(β) + n, the tracer
    always returns `some _`". -/
abbrev FueledTracer (R : Type u) : Type u :=
  ℕ → (n : ℕ) → List ℤ → Option R

/-- **Termination of the recursive Markov-trace reducer.**

    *Statement (concrete):* there exists a fueled implementation
    `tracer` such that for every input `(n, β)` and every fuel
    bound `fuel ≥ β.length + n`, the tracer returns `some _`.

    Justification (not formalised; proved in prose in the `.md`
    sibling, section Correctness): the recursive
    algorithm has well-founded structure on the lex order
    `(n, ℓ(w))`. Each peeling step removes exactly one `σ_{n-2}`
    factor (decreasing ℓ by 1); each truncation decreases the
    ambient algebra's index `n`. The lex order has no infinite
    descending chain, so the algorithm halts in finitely many
    steps. A constructive fuel bound is `β.length + n` (an
    upper bound on the number of peel/truncate steps along any
    branch).

    Ref: [jones1987] §5 (recursive structure of the Markov trace);
    [kassel1995] Lemma III.3.5 (well-foundedness of the Hecke-basis
    descent).

    NOTE (honest scope): this lemma asserts only the *terminating-shape*
    property — there exists a total fueled tracer returning `some` for
    every sufficiently-fuelled input (`(tracer fuel n β).isSome`). The
    witness is the constant `some default` tracer, which discharges the
    shape but is not the canonical `tr_M` reducer; the added
    `[Inhabited R]` hypothesis only inhabits the return type. The
    concrete tracer corresponding to `markov_trace_recursive.py`, and the
    well-founded-recursion argument on `(n, ℓ(w))` that it terminates,
    are given in prose in the `.md` sibling and are not formalised. -/
theorem markovTraceRecursiveReducer_terminates {R : Type*} [Inhabited R] :
    ∃ (tracer : FueledTracer R),
      ∀ (n : ℕ) (β : List ℤ) (fuel : ℕ),
        β.length + n ≤ fuel → (tracer fuel n β).isSome := by
  refine ⟨fun _ _ _ => some default, ?_⟩
  intro n β fuel _
  rfl

/-! ## Disjoint-product property of the Markov trace

    The statement is `DisjointProductLaw` below, and the proof is
    `markovTrace_disjointProduct` at the end of the file. The argument is
    Ocneanu's reduction (`HeckeRel.reduce`), not iterated stripping:
    stripping alone handles only words in which each generator occurs once
    (`markovTrace_disjointProduct_ascendingRun`). For general words the
    proof inducts on the number of generators of `β` and uses the Hecke,
    braid and far-commutation relations to bring every word down to one
    that uses the top generator at most once.

    Ref: [kassel1995] Theorem III.3.3 (Markov-trace stability under
    embedding); [jones1987] §5 (Ocneanu trace). -/

/-- `w` is a **positive word on the first `n` generators**: every letter is an
    index `c` with `0 ≤ c < n`.  `mT n` is only constrained on such words; the
    level-`n` algebra of the tower is spanned by them (the generators are
    invertible through the quadratic relation, `σ⁻¹ = σ - h`). -/
def Supp (n : ℕ) (w : List ℤ) : Prop := ∀ c ∈ w, 0 ≤ c ∧ c < n

theorem Supp.mono {n m : ℕ} {w : List ℤ} (h : Supp n w) (hnm : n ≤ m) : Supp m w :=
  fun c hc => ⟨(h c hc).1, lt_of_lt_of_le (h c hc).2 (by exact_mod_cast hnm)⟩

theorem Supp.append {n : ℕ} {u v : List ℤ} (hu : Supp n u) (hv : Supp n v) :
    Supp n (u ++ v) := by
  intro c hc
  rcases List.mem_append.mp hc with h | h
  · exact hu c h
  · exact hv c h

/-- **Axioms of a Markov (Ocneanu) trace, read on positive braid words**
    (repaired 2026-11-20, bean `qou-dx7g`; previously flagged in `qou-n2un`).

    `mT n w` is the trace of the image of the positive word `w` in the level-`n`
    algebra `H_{n+1}(q)` (generators `σ_0, …, σ_{n-1}`), `h = q - q⁻¹`.  The
    fields are the defining relations of the Hecke tower (quadratic, braid, far
    commutation — read inside an arbitrary context `u · _ · v`, so that `mT`
    factors through the algebra) together with Ocneanu's axioms (cyclicity,
    normalisation, stability under the trivial embedding, Markov stabilisation
    `tr(x σ_n) = z tr(x)` for `x ∈ H_n`).  By Ocneanu's uniqueness theorem
    ([jones1987] §5) such an `mT` is *the* Markov trace with parameter `z`.

    **What changed.**  Before this repair `strip`, `cyclic` and `stable` were
    quantified over every word with no support condition, and there was no
    Hecke relation.  That forced `mT n w = z ^ |w|` for every non-negative word
    (the old `IsMarkovTrace.eq_pow_length`), so `tr(σ₁²) = z²` instead of
    `h z + 1`, and the "derived" disjoint-product law was the product law of
    `z ^ |w|`.  Now `strip`/`stable`/`cyclic` carry the support hypothesis
    `Supp`, and `hecke` forces `tr(σ_i²) = h z + 1`; the length-power model
    survives only at the degenerate root `z² = h z + 1` (the trivial character,
    which is a genuine Markov trace — `lengthPow_isMarkovTrace`) and is
    excluded elsewhere (`not_isMarkovTrace_two_pow_length`). -/
structure IsMarkovTrace {R : Type*} [CommRing R]
    (mT : ℕ → List ℤ → R) (embedRight : List ℤ → ℕ → List ℤ) (z h : R) :
    Prop where
  /-- Markov stabilisation: for `w ∈ H_n`, appending the new generator `σ_n`
      peels with the fixed factor `z`. -/
  strip : ∀ (n : ℕ) (w : List ℤ), Supp n w →
    mT (n + 1) (w ++ [Int.ofNat n]) = z * mT n w
  /-- Cyclicity of the trace, on words of the level-`n` algebra. -/
  cyclic : ∀ (n : ℕ) (u v : List ℤ), Supp n u → Supp n v →
    mT n (u ++ v) = mT n (v ++ u)
  /-- The shift embedding re-indexes `β`'s generators onto a disjoint
      strand cluster (right of the separating slot). -/
  embed_disjoint : ∀ (β : List ℤ) (j : ℕ),
    embedRight β j = β.map (· + Int.ofNat j)
  /-- **Normalisation.** The empty word has trace `1`. -/
  normalised : ∀ n : ℕ, mT n [] = 1
  /-- **Stability under the trivial embedding** `H_n ⊆ H_{n+1}`, for words that
      do not use the new generator. -/
  stable : ∀ (n : ℕ) (w : List ℤ), Supp n w → mT (n + 1) w = mT n w
  /-- **Hecke quadratic relation** `σ_i² = h σ_i + 1`, in context. -/
  hecke : ∀ (n : ℕ) (u v : List ℤ) (i : ℤ), Supp n (u ++ [i] ++ v) →
    mT n (u ++ [i, i] ++ v) = h * mT n (u ++ [i] ++ v) + mT n (u ++ v)
  /-- **Braid relation** `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`, in context. -/
  braid : ∀ (n : ℕ) (u v : List ℤ) (i : ℤ), Supp n (u ++ [i, i + 1] ++ v) →
    mT n (u ++ [i, i + 1, i] ++ v) = mT n (u ++ [i + 1, i, i + 1] ++ v)
  /-- **Far commutation** `σ_i σ_j = σ_j σ_i` for `|i - j| ≥ 2`, in context. -/
  far_comm : ∀ (n : ℕ) (u v : List ℤ) (i j : ℤ), 2 ≤ |i - j| →
    Supp n (u ++ [i, j] ++ v) →
    mT n (u ++ [i, j] ++ v) = mT n (u ++ [j, i] ++ v)

/-! ## What the axioms buy, derived

Peeling an *ascending* run `σ_n σ_{n+1} ⋯ σ_{n+m-1}` off a word of `H_n` costs
exactly `z^m`; this is `strip` iterated, and the support bookkeeping is now
explicit.  The **general** disjoint-product law, for a word `β` with repeated
generators, needs Ocneanu's reduction of `β` modulo the Hecke relations.  It is
stated below as the proposition `DisjointProductLaw` and proved at the end of
the file (`markovTrace_disjointProduct`, via `HeckeRel.reduce`). -/

/-- The ascending run of generator indices `[n, n+1, …, n+m-1]`, written so
    that the *last* letter is exposed — the form `IsMarkovTrace.strip`
    consumes. -/
def ascendingRun (n : ℕ) : ℕ → List ℤ
  | 0 => []
  | m + 1 => ascendingRun n m ++ [Int.ofNat (n + m)]

/-- **Stripping an ascending run costs exactly `z^m`.** Derived from `strip`
    by induction on the run length, for `w` a word of `H_n`. -/
theorem markovTrace_strip_ascendingRun {R : Type*} [CommRing R]
    {mT : ℕ → List ℤ → R} {embedRight : List ℤ → ℕ → List ℤ} {z h : R}
    (hmT : IsMarkovTrace mT embedRight z h) (n : ℕ) (w : List ℤ) (hw : Supp n w) :
    ∀ m : ℕ, mT (n + m) (w ++ ascendingRun n m) = z ^ m * mT n w := by
  intro m
  induction m with
  | zero => simp [ascendingRun]
  | succ m ih =>
    have hsupp : Supp (n + m) (w ++ ascendingRun n m) := by
      refine Supp.append (hw.mono (Nat.le_add_right n m)) ?_
      clear ih
      induction m with
      | zero => intro c hc; simp [ascendingRun] at hc
      | succ m ih2 =>
        intro c hc
        simp only [ascendingRun, List.mem_append, List.mem_singleton] at hc
        rcases hc with hc | rfl
        · have := ih2 c hc; exact ⟨this.1, by omega⟩
        · exact ⟨by simp; omega, by simp⟩
    have hstep := hmT.strip (n + m) (w ++ ascendingRun n m) hsupp
    calc mT (n + (m + 1)) (w ++ ascendingRun n (m + 1))
        = mT (n + m + 1) ((w ++ ascendingRun n m) ++ [Int.ofNat (n + m)]) := by
          simp [ascendingRun, List.append_assoc, Nat.add_assoc]
      _ = z * mT (n + m) (w ++ ascendingRun n m) := hstep
      _ = z * (z ^ m * mT n w) := by rw [ih]
      _ = z ^ (m + 1) * mT n w := by ring

/-- **The trace of an ascending run is `z^m`** (`w = []` above). -/
theorem markovTrace_ascendingRun {R : Type*} [CommRing R]
    {mT : ℕ → List ℤ → R} {embedRight : List ℤ → ℕ → List ℤ} {z h : R}
    (hmT : IsMarkovTrace mT embedRight z h) (n m : ℕ) :
    mT (n + m) (ascendingRun n m) = z ^ m := by
  have := markovTrace_strip_ascendingRun hmT n [] (fun c hc => by simp at hc) m
  simpa [hmT.normalised n] using this

/-- `σ_i² = h σ_i + 1` evaluated: `tr(σ_n²) = h z + 1` on the level above `n`.
    This is the value the pre-repair structure got wrong (it forced `z²`). -/
theorem markovTrace_sq_gen {R : Type*} [CommRing R]
    {mT : ℕ → List ℤ → R} {embedRight : List ℤ → ℕ → List ℤ} {z h : R}
    (hmT : IsMarkovTrace mT embedRight z h) (n : ℕ) :
    mT (n + 1) [Int.ofNat n, Int.ofNat n] = h * z + 1 := by
  have hs : Supp (n + 1) ([] ++ [Int.ofNat n] ++ []) := by
    intro c hc; simp at hc; subst hc; constructor <;> simp
  have := hmT.hecke (n + 1) [] [] (Int.ofNat n) hs
  simp only [List.nil_append, List.append_nil] at this
  rw [this, hmT.normalised]
  have h1 := hmT.strip n [] (fun c hc => by simp at hc)
  simp only [List.nil_append] at h1
  rw [h1, hmT.normalised]; ring

/-- **Disjoint product for an ascending run.** For `α ∈ H_{k+1}` and `β` the
    ascending run `σ_0 ⋯ σ_{m-1}` shifted onto `σ_{k+1} ⋯ σ_{k+m}`
    (so the two clusters share one strand), `tr(α · β↑) = tr(α) · tr(β)`.  A genuine special case of
    the disjoint-product law, proved from the axioms. -/
theorem markovTrace_disjointProduct_ascendingRun {R : Type*} [CommRing R]
    {mT : ℕ → List ℤ → R} {embedRight : List ℤ → ℕ → List ℤ} {z h : R}
    (hmT : IsMarkovTrace mT embedRight z h) (k m : ℕ) (α : List ℤ)
    (hα : Supp (k + 1) α) :
    mT (k + 1 + m) (α ++ embedRight (ascendingRun 0 m) (k + 1))
      = mT (k + 1) α * mT m (ascendingRun 0 m) := by
  have hrun : embedRight (ascendingRun 0 m) (k + 1) = ascendingRun (k + 1) m := by
    rw [hmT.embed_disjoint]
    clear hα
    induction m with
    | zero => rfl
    | succ m ih =>
      simp only [ascendingRun, List.map_append, ih, List.map_singleton]
      congr 2
      simp only [Int.ofNat_eq_coe]; push_cast; ring
  rw [hrun, markovTrace_strip_ascendingRun hmT (k + 1) α hα m]
  have := markovTrace_ascendingRun hmT 0 m
  rw [Nat.zero_add] at this
  rw [this, mul_comm]

/-- **The general disjoint-product law** — `tr(α · β↑) = tr(α) tr(β)` for `α`
    a word on the generators `σ_0, …, σ_k` and `β` any positive word, shifted
    by `k + 1`, so that its lowest generator lands on `σ_{k+1}`.  Proved from
    the axioms below (`markovTrace_disjointProduct`, 2026-11-21).  Before
    2026-11-20 a "proof" existed only because the axioms had collapsed `mT` to
    `z ^ |w|`; the present proof uses the Hecke, braid and far-commutation
    relations essentially. -/
def DisjointProductLaw {R : Type*} [CommRing R]
    (mT : ℕ → List ℤ → R) (embedRight : List ℤ → ℕ → List ℤ) : Prop :=
  ∀ (k m : ℕ) (α β : List ℤ), Supp (k + 1) α → Supp m β →
    mT (k + 1 + m) (α ++ embedRight β (k + 1)) = mT (k + 1) α * mT m β

/-- **Non-vacuity.** The trivial character `σ_i ↦ q` of the Hecke tower,
    `mT n w = q ^ |w|`, with `z = q` and `h = q - q⁻¹`, satisfies every axiom.
    It is a genuine (degenerate) Markov trace: `q² = h q + 1`. -/
theorem lengthPow_isMarkovTrace {R : Type*} [CommRing R] (q : Rˣ) :
    IsMarkovTrace (fun _ w => (q : R) ^ w.length)
      (fun β j => β.map (· + Int.ofNat j)) (q : R) ((q : R) - (q⁻¹ : Rˣ)) where
  strip _ w _ := by simp [pow_succ]; ring
  cyclic _ u v _ _ := by simp [Nat.add_comm]
  embed_disjoint _ _ := rfl
  normalised _ := by simp
  stable _ _ _ := rfl
  hecke _ u v _ _ := by
    simp only [List.length_append, List.length_cons, List.length_nil]
    have hq : (q : R) * (q⁻¹ : Rˣ) = 1 := by simp
    have : (q : R) ^ (u.length + 2 + v.length)
        = ((q : R) - (q⁻¹ : Rˣ)) * (q : R) ^ (u.length + 1 + v.length)
          + (q : R) ^ (u.length + v.length) := by
      have e1 : u.length + 2 + v.length = (u.length + v.length) + 2 := by omega
      have e2 : u.length + 1 + v.length = (u.length + v.length) + 1 := by omega
      rw [e1, e2, pow_add, pow_add]
      linear_combination (q : R) ^ (u.length + v.length) * hq
    simpa using this
  braid _ u v _ _ := by simp
  far_comm _ u v _ _ _ _ := by simp

/-- **The old trivial inhabitant is gone.** `mT n w = 2 ^ |w|` with `z = 2`
    satisfied every pre-repair field; with `h = 0` it fails the Hecke relation
    (`tr(σ₀²) = 4 ≠ 1 = h z + 1`). -/
theorem not_isMarkovTrace_two_pow_length :
    ¬ IsMarkovTrace (R := ℤ) (fun _ w => (2 : ℤ) ^ w.length)
      (fun β j => β.map (· + Int.ofNat j)) 2 0 := by
  intro hmT
  have := markovTrace_sq_gen hmT 0
  norm_num at this

/-- **`disjoint_product` is genuinely independent of the other three axioms.**

    A structure field that could be derived from its siblings would be an
    axiom too many; this shows it cannot. The witness is
    `mT n w := 2 ^ n` — a "trace" that ignores the word entirely — with
    `z := 2` over `ℤ`. It satisfies `strip` (`2^(n+1) = 2 · 2^n`), `cyclic`
    (both sides ignore the word) and `embed_disjoint` (by definition), and it
    refutes the product law already at `k = 0`, `n = 2`, `α = β = []`, where
    the left side is `4` and the right is `2^0 · 2^1 = 2`.

    What the counter-model exposes is the missing ingredient: `IsMarkovTrace`
    states no **normalisation** (`mT n [] = 1`) and no **stability under the
    trivial embedding** (`mT (n+1) w = mT n w` for `w` off the top strand).
    Without those, `mT` may grow with the ambient index alone, and no amount of
    stripping or cyclic rearrangement can force a product law. So keeping
    `disjoint_product` as an axiom would be correct rather than lazy — but the
    counter-model also says exactly what to add, so the better move is to add
    the two axioms and re-attempt the derivation. That is what
    `markovTrace_disjointProduct` below now does, together with the Hecke,
    braid and far-commutation relations (normalisation and stability alone,
    quantified over all words, collapse the trace to `z ^ |w|`): the field is
    gone and the product law is proved. This theorem is kept because it is what justifies
    the axiom set being the size it is — three of these axioms genuinely do not
    suffice. Bean `qou-tmmt`. -/
theorem disjointProduct_independent_of_strip_cyclic_embed :
    ∃ (mT : ℕ → List ℤ → ℤ) (embedRight : List ℤ → ℕ → List ℤ) (z : ℤ),
      (∀ (n : ℕ) (w : List ℤ),
          mT (n + 1) (w ++ [Int.ofNat n]) = z * mT n w) ∧
      (∀ (n : ℕ) (u v : List ℤ), mT n (u ++ v) = mT n (v ++ u)) ∧
      (∀ (β : List ℤ) (j : ℕ), embedRight β j = β.map (· + Int.ofNat j)) ∧
      ¬ (∀ (k n : ℕ), k + 2 ≤ n → ∀ α β : List ℤ,
          mT n (α ++ embedRight β (k + 1)) = mT k α * mT (n - k - 1) β) := by
  refine ⟨fun n _ => 2 ^ n, fun β j => β.map (· + Int.ofNat j), 2, ?_, ?_, ?_, ?_⟩
  · intro n _; ring
  · intro _ _ _; rfl
  · intro _ _; rfl
  · intro h
    have hcontra := h 0 2 (by norm_num) [] []
    exact absurd hcontra (by norm_num)


/-! ## The general disjoint-product law, derived (bean `qou-tmmt`)

The proof is Ocneanu's reduction.  Any function `G` on positive words that
satisfies the three in-context relations of the Hecke tower (`HeckeRel`) and
vanishes on words using the top generator at most once vanishes everywhere
(`HeckeRel.reduce`): two consecutive top letters `σ_T x σ_T` are either pushed
together through `x` and merged by the quadratic relation (when `x` avoids
`σ_{T-1}`), or turned by one braid move into a word with one top letter fewer
(when `x` uses `σ_{T-1}` once); otherwise `x` is first reduced one level down.
The difference of the two sides of the product law is such a `G`, and it
vanishes on words using the top generator at most once by stability, cyclicity
and Markov stabilisation. -/

section DisjointProduct

variable {R : Type*} [CommRing R]

theorem supp_append_iff {n : ℕ} {u v : List ℤ} :
    Supp n (u ++ v) ↔ Supp n u ∧ Supp n v := List.forall_mem_append

theorem supp_cons_iff {n : ℕ} {a : ℤ} {w : List ℤ} :
    Supp n (a :: w) ↔ (0 ≤ a ∧ a < n) ∧ Supp n w := List.forall_mem_cons

theorem supp_nil {n : ℕ} : Supp n [] := fun _ h => by simp at h

/-- The in-context relations of the Hecke tower `H_{n+1}(q)` (generators
    `σ_0, …, σ_{n-1}`), for a function `G` on positive words. -/
def HeckeRel (n : ℕ) (h : R) (G : List ℤ → R) : Prop :=
  (∀ (u v : List ℤ) (i : ℤ), Supp n (u ++ [i] ++ v) →
      G (u ++ [i, i] ++ v) = h * G (u ++ [i] ++ v) + G (u ++ v)) ∧
  (∀ (u v : List ℤ) (i : ℤ), Supp n (u ++ [i, i + 1] ++ v) →
      G (u ++ [i, i + 1, i] ++ v) = G (u ++ [i + 1, i, i + 1] ++ v)) ∧
  (∀ (u v : List ℤ) (i j : ℤ), 2 ≤ |i - j| → Supp n (u ++ [i, j] ++ v) →
      G (u ++ [i, j] ++ v) = G (u ++ [j, i] ++ v))

/-- Split a word at the first occurrence of a letter. -/
theorem exists_split_first (a : ℤ) :
    ∀ w : List ℤ, a ∈ w → ∃ p s, w = p ++ a :: s ∧ a ∉ p
  | [], h => by simp at h
  | b :: w, h => by
    by_cases hb : b = a
    · exact ⟨[], w, by simp [hb], by simp⟩
    · have hw : a ∈ w := by
        rcases List.mem_cons.mp h with h | h
        · exact absurd h.symm hb
        · exact h
      obtain ⟨p, s, rfl, hp⟩ := exists_split_first a w hw
      exact ⟨b :: p, s, rfl, by simp [Ne.symm hb, hp]⟩

/-- A letter far from every letter of `y` moves through `y`. -/
theorem HeckeRel.move {n : ℕ} {h : R} {G : List ℤ → R} (hG : HeckeRel n h G)
    (T : ℤ) : ∀ (y u v : List ℤ), (∀ c ∈ y, 2 ≤ |T - c|) →
      Supp n (u ++ [T] ++ y ++ v) →
      G (u ++ [T] ++ y ++ v) = G (u ++ y ++ [T] ++ v)
  | [], u, v, _, _ => by simp
  | c :: y, u, v, hy, hs => by
    have hs' : Supp n (u ++ [T, c] ++ (y ++ v)) := by
      simp only [supp_append_iff, supp_cons_iff] at hs ⊢; tauto
    have h1 := hG.2.2 u (y ++ v) T c (hy c (by simp)) hs'
    have hs2 : Supp n ((u ++ [c]) ++ [T] ++ y ++ v) := by
      simp only [supp_append_iff, supp_cons_iff] at hs ⊢; tauto
    have h2 := HeckeRel.move hG T y (u ++ [c]) v
      (fun d hd => hy d (by simp [hd])) hs2
    simp only [List.append_assoc, List.cons_append, List.singleton_append,
      List.nil_append] at h1 h2 ⊢
    rw [h1, h2]

theorem count_eq_zero_of_supp {n : ℕ} {y : List ℤ} (hy : Supp n y) :
    y.count (n : ℤ) = 0 :=
  List.count_eq_zero_of_not_mem (fun hm => by have := hy _ hm; omega)

/-- **Ocneanu's reduction.** A function on the positive words of `H_{n+1}(q)`
    satisfying the in-context Hecke-tower relations, and vanishing on words
    that use the top generator `σ_{n-1}` at most once, vanishes on every
    word (up to any length bound `L`). -/
theorem HeckeRel.reduce (h : R) : ∀ (n : ℕ) (G : List ℤ → R), HeckeRel n h G →
    ∀ L : ℕ, (∀ w, Supp n w → w.length ≤ L → w.count ((n : ℤ) - 1) ≤ 1 → G w = 0) →
    ∀ w, Supp n w → w.length ≤ L → G w = 0
  | 0, G, _, L, h0, w, hw, hL => by
    have hwnil : w = [] := by
      cases w with
      | nil => rfl
      | cons c w => have := hw c (by simp); push_cast at this; omega
    subst hwnil; exact h0 [] hw hL (by simp)
  | n + 1, G, hG, L, h0, w, hw, hL => by
    have hcnt : ((n + 1 : ℕ) : ℤ) - 1 = (n : ℤ) := by push_cast; ring
    have key : ∀ K : ℕ, ∀ w, Supp (n + 1) w → w.length ≤ L →
        w.length + w.count (n : ℤ) < K → G w = 0 := by
      intro K
      induction K with
      | zero => intro w _ _ hk; omega
      | succ K ih =>
        intro w hw hL hk
        by_cases hc : w.count (n : ℤ) ≤ 1
        · exact h0 w hw hL (by rw [hcnt]; exact hc)
        push_neg at hc
        obtain ⟨p, r, rfl, hp⟩ :=
          exists_split_first (n : ℤ) w (List.count_pos_iff.mp (by omega))
        have hp0 : p.count (n : ℤ) = 0 := List.count_eq_zero_of_not_mem hp
        have hcr : 1 ≤ r.count (n : ℤ) := by
          simp only [List.count_append, List.count_cons, beq_self_eq_true,
            if_true] at hc
          omega
        obtain ⟨x, s, rfl, hx⟩ :=
          exists_split_first (n : ℤ) r (List.count_pos_iff.mp (by omega))
        have hx0 : x.count (n : ℤ) = 0 := List.count_eq_zero_of_not_mem hx
        have hwsplit := hw
        simp only [supp_append_iff, supp_cons_iff] at hwsplit
        obtain ⟨hP, ⟨-, hX, -, hS⟩⟩ := hwsplit
        have hTn : (0 : ℤ) ≤ n ∧ (n : ℤ) < ((n + 1 : ℕ) : ℤ) := by
          constructor <;> push_cast <;> omega
        have hXn : Supp n x := fun c hc => by
          have := hX c hc
          have hne : c ≠ (n : ℤ) := fun e => hx (e ▸ hc)
          push_cast at this; omega
        -- `G' y = G (p ++ σ_n y σ_n ++ s)`, reduced one level down
        let G' : List ℤ → R := fun y => G (p ++ [(n : ℤ)] ++ y ++ [(n : ℤ)] ++ s)
        have hctx : ∀ y, Supp n y →
            Supp (n + 1) (p ++ [(n : ℤ)] ++ y ++ [(n : ℤ)] ++ s) := by
          intro y hy
          simp only [supp_append_iff, supp_cons_iff]
          exact ⟨⟨⟨⟨hP, hTn, supp_nil⟩, hy.mono (Nat.le_succ n)⟩, hTn, supp_nil⟩, hS⟩
        have hG' : HeckeRel n h G' := by
          refine ⟨?_, ?_, ?_⟩
          · intro u v i hs
            have := hG.1 (p ++ [(n : ℤ)] ++ u) (v ++ [(n : ℤ)] ++ s) i (by
              have := hctx _ hs
              simp only [supp_append_iff, supp_cons_iff] at this ⊢; tauto)
            simp only [G', List.append_assoc, List.cons_append,
              List.singleton_append, List.nil_append] at this ⊢
            exact this
          · intro u v i hs
            have := hG.2.1 (p ++ [(n : ℤ)] ++ u) (v ++ [(n : ℤ)] ++ s) i (by
              have := hctx _ hs
              simp only [supp_append_iff, supp_cons_iff] at this ⊢; tauto)
            simp only [G', List.append_assoc, List.cons_append,
              List.singleton_append, List.nil_append] at this ⊢
            exact this
          · intro u v i j hij hs
            have := hG.2.2 (p ++ [(n : ℤ)] ++ u) (v ++ [(n : ℤ)] ++ s) i j hij (by
              have := hctx _ hs
              simp only [supp_append_iff, supp_cons_iff] at this ⊢; tauto)
            simp only [G', List.append_assoc, List.cons_append,
              List.singleton_append, List.nil_append] at this ⊢
            exact this
        have hlenw : (p ++ (n : ℤ) :: (x ++ (n : ℤ) :: s)).length
            = p.length + x.length + s.length + 2 := by simp; omega
        have hcw : (p ++ (n : ℤ) :: (x ++ (n : ℤ) :: s)).count (n : ℤ)
            = s.count (n : ℤ) + 2 := by
          simp only [List.count_append, List.count_cons, beq_self_eq_true, if_true]
          omega
        rw [hlenw] at hL
        rw [hlenw, hcw] at hk
        have h0' : ∀ y, Supp n y → y.length ≤ x.length →
            y.count ((n : ℤ) - 1) ≤ 1 → G' y = 0 := by
          intro y hy hyl hyc
          have hy0 : y.count (n : ℤ) = 0 := count_eq_zero_of_supp hy
          have hfar : ∀ c ∈ y, c ≠ (n : ℤ) - 1 → 2 ≤ |(n : ℤ) - c| := by
            intro c hc hne
            have := hy c hc
            exact le_trans (by omega) (le_abs_self _)
          rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hyc with hyc | hyc
          · -- `y` avoids `σ_{n-1}`: push the two top letters together
            have hnot : ∀ c ∈ y, 2 ≤ |(n : ℤ) - c| := fun c hc =>
              hfar c hc (fun e => by
                have : 0 < y.count ((n : ℤ) - 1) := List.count_pos_iff.mpr (e ▸ hc)
                omega)
            have hm := HeckeRel.move hG (n : ℤ) y p ([(n : ℤ)] ++ s) hnot (by
              have := hctx y hy
              simp only [supp_append_iff, supp_cons_iff] at this ⊢; tauto)
            have hq := hG.1 (p ++ y) s (n : ℤ) (by
              have := hctx y hy
              simp only [supp_append_iff, supp_cons_iff] at this ⊢; tauto)
            have e1 : G (p ++ y ++ [(n : ℤ)] ++ s) = 0 := by
              apply ih
              · have := hctx y hy
                simp only [supp_append_iff, supp_cons_iff] at this ⊢; tauto
              · simp; omega
              · simp only [List.length_append, List.length_cons, List.length_nil,
                  List.count_append, List.count_cons, beq_self_eq_true, if_true,
                  List.count_nil]
                omega
            have e2 : G (p ++ y ++ s) = 0 := by
              apply ih
              · have := hctx y hy
                simp only [supp_append_iff, supp_cons_iff] at this ⊢; tauto
              · simp; omega
              · simp only [List.length_append, List.count_append]
                omega
            simp only [G', List.append_assoc, List.cons_append,
              List.singleton_append, List.nil_append] at hm hq e1 e2 ⊢
            rw [hm, hq, e1, e2]; ring
          · -- `y` uses `σ_{n-1}` once: one braid move removes a top letter
            obtain ⟨a, b, rfl, ha⟩ := exists_split_first ((n : ℤ) - 1) y
              (List.count_pos_iff.mp (by omega))
            have hb : (n : ℤ) - 1 ∉ b := by
              intro hm
              have h1 : 0 < b.count ((n : ℤ) - 1) := List.count_pos_iff.mpr hm
              have h2 : a.count ((n : ℤ) - 1) = 0 := List.count_eq_zero_of_not_mem ha
              simp only [List.count_append, List.count_cons, beq_self_eq_true,
                if_true] at hyc
              omega
            have hya := hy
            simp only [supp_append_iff, supp_cons_iff] at hya
            obtain ⟨hA, hτ, hB⟩ := hya
            have hfa : ∀ c ∈ a, 2 ≤ |(n : ℤ) - c| := fun c hc =>
              hfar c (by simp [hc]) (fun e => ha (e ▸ hc))
            have hfb : ∀ c ∈ b, 2 ≤ |(n : ℤ) - c| := fun c hc =>
              hfar c (by simp [hc]) (fun e => hb (e ▸ hc))
            have hfull := hctx _ hy
            have m1 := HeckeRel.move hG (n : ℤ) a p
              ([(n : ℤ) - 1] ++ b ++ [(n : ℤ)] ++ s) hfa (by
                simp only [supp_append_iff, supp_cons_iff] at hfull ⊢; tauto)
            have m2 := HeckeRel.move hG (n : ℤ) b
              (p ++ a ++ [(n : ℤ), (n : ℤ) - 1]) s hfb (by
                simp only [supp_append_iff, supp_cons_iff] at hfull ⊢; tauto)
            have br := hG.2.1 (p ++ a) (b ++ s) ((n : ℤ) - 1) (by
              simp only [sub_add_cancel]
              simp only [supp_append_iff, supp_cons_iff] at hfull ⊢; tauto)
            simp only [sub_add_cancel] at br
            have e1 : G (p ++ a ++ [(n : ℤ) - 1, (n : ℤ), (n : ℤ) - 1] ++ b ++ s) = 0 := by
              apply ih
              · simp only [supp_append_iff, supp_cons_iff] at hfull ⊢; tauto
              · simp only [List.length_append, List.length_cons, List.length_nil] at hyl ⊢
                omega
              · have ha0 : a.count (n : ℤ) = 0 := count_eq_zero_of_supp hA
                have hb0 : b.count (n : ℤ) = 0 := count_eq_zero_of_supp hB
                have hne : ((n : ℤ) - 1 == (n : ℤ)) = false := by simp
                simp only [List.length_append, List.length_cons, List.length_nil,
                  List.count_append, List.count_cons, beq_self_eq_true, if_true,
                  List.count_nil, hne, Bool.false_eq_true, if_false] at ⊢
                simp only [List.length_append, List.length_cons] at hyl
                omega
            simp only [G', List.append_assoc, List.cons_append,
              List.singleton_append, List.nil_append] at m1 m2 br e1 ⊢
            rw [m1, ← m2, ← br, e1]
        have := HeckeRel.reduce h n G' hG' x.length h0' x hXn le_rfl
        simp only [G', List.append_assoc, List.cons_append,
          List.singleton_append, List.nil_append] at this ⊢
        exact this
    exact key _ w hw hL (Nat.lt_succ_self _)

/-- **The general disjoint-product law, proved** (bean `qou-tmmt`).  For a
    word `α` of `H_{k+2}` (generators `σ_0, …, σ_k`) and any positive word `β`
    on `σ_0, …, σ_{m-1}` shifted onto `σ_{k+1}, …, σ_{k+m}`,
    `tr(α · β↑) = tr(α) · tr(β)`.  Induction on `m`; inside a level, the
    difference of the two sides satisfies the Hecke-tower relations and
    vanishes on words using the top generator at most once, so it vanishes
    by `HeckeRel.reduce`. -/
theorem markovTrace_disjointProduct {mT : ℕ → List ℤ → R}
    {embedRight : List ℤ → ℕ → List ℤ} {z h : R}
    (hmT : IsMarkovTrace mT embedRight z h) : DisjointProductLaw mT embedRight := by
  intro k m
  induction m with
  | zero =>
    intro α β _ hβ
    have hβnil : β = [] := by
      cases β with
      | nil => rfl
      | cons c β => have := hβ c (by simp); push_cast at this; omega
    subst hβnil
    rw [hmT.embed_disjoint]
    simp [hmT.normalised]
  | succ m ih =>
    intro α β hα hβ
    set c : ℤ := ((k + 1 : ℕ) : ℤ) with hc
    have hemb : ∀ γ : List ℤ, embedRight γ (k + 1) = γ.map (· + c) := by
      intro γ; rw [hmT.embed_disjoint]; simp [hc]
    simp only [hemb] at ih ⊢
    have hN : k + 1 + (m + 1) = k + 1 + m + 1 := by ring
    have hαN : ∀ j, Supp (k + 1 + j) α := fun j => hα.mono (Nat.le_add_right _ _)
    have hsh : ∀ j (γ : List ℤ), Supp j γ → Supp (k + 1 + j) (γ.map (· + c)) := by
      intro j γ hγ d hd
      obtain ⟨e, he, rfl⟩ := List.mem_map.mp hd
      have := hγ e he
      simp only [hc] at *
      push_cast at this ⊢
      omega
    -- the difference of the two sides, as a function of `β`
    let F : List ℤ → R := fun γ =>
      mT (k + 1 + (m + 1)) (α ++ γ.map (· + c)) - mT (k + 1) α * mT (m + 1) γ
    have hF : HeckeRel (m + 1) h F := by
      refine ⟨?_, ?_, ?_⟩
      · intro u v i hs
        have h1 := hmT.hecke (k + 1 + (m + 1)) (α ++ u.map (· + c)) (v.map (· + c))
          (i + c) (by
            have := hsh _ _ hs
            simp only [List.map_append, List.map_cons, List.map_nil] at this
            simp only [supp_append_iff, supp_cons_iff] at this ⊢
            exact ⟨⟨⟨hαN _, this.1.1⟩, this.1.2⟩, this.2⟩)
        have h2 := hmT.hecke (m + 1) u v i hs
        simp only [F, List.map_append, List.map_cons, List.map_nil,
          List.append_assoc, List.cons_append, List.singleton_append,
          List.nil_append] at h1 h2 ⊢
        rw [h1, h2]; ring
      · intro u v i hs
        have h1 := hmT.braid (k + 1 + (m + 1)) (α ++ u.map (· + c)) (v.map (· + c))
          (i + c) (by
            have := hsh _ _ hs
            simp only [List.map_append, List.map_cons, List.map_nil] at this
            have e : i + 1 + c = i + c + 1 := by ring
            rw [e] at this
            simp only [supp_append_iff, supp_cons_iff] at this ⊢
            exact ⟨⟨⟨hαN _, this.1.1⟩, this.1.2⟩, this.2⟩)
        have h2 := hmT.braid (m + 1) u v i hs
        have e : i + 1 + c = i + c + 1 := by ring
        simp only [F, List.map_append, List.map_cons, List.map_nil, e,
          List.append_assoc, List.cons_append, List.singleton_append,
          List.nil_append] at h1 h2 ⊢
        rw [h1, h2]
      · intro u v i j hij hs
        have h1 := hmT.far_comm (k + 1 + (m + 1)) (α ++ u.map (· + c)) (v.map (· + c))
          (i + c) (j + c) (by rw [show i + c - (j + c) = i - j by ring]; exact hij) (by
            have := hsh _ _ hs
            simp only [List.map_append, List.map_cons, List.map_nil] at this
            simp only [supp_append_iff, supp_cons_iff] at this ⊢
            exact ⟨⟨⟨hαN _, this.1.1⟩, this.1.2⟩, this.2⟩)
        have h2 := hmT.far_comm (m + 1) u v i j hij hs
        simp only [F, List.map_append, List.map_cons, List.map_nil,
          List.append_assoc, List.cons_append, List.singleton_append,
          List.nil_append] at h1 h2 ⊢
        rw [h1, h2]
    have hcm : ((m + 1 : ℕ) : ℤ) - 1 = (m : ℤ) := by push_cast; ring
    have h0 : ∀ γ, Supp (m + 1) γ → γ.length ≤ β.length →
        γ.count (((m + 1 : ℕ) : ℤ) - 1) ≤ 1 → F γ = 0 := by
      intro γ hγ _ hγc
      rw [hcm] at hγc
      rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hγc with hγc | hγc
      · -- `γ` avoids the top generator: stability on both sides
        have hγm : Supp m γ := fun d hd => by
          have := hγ d hd
          have hne : d ≠ (m : ℤ) := fun e => by
            have : 0 < γ.count (m : ℤ) := List.count_pos_iff.mpr (e ▸ hd)
            omega
          push_cast at this; omega
        have s1 := hmT.stable (k + 1 + m) (α ++ γ.map (· + c))
          (supp_append_iff.mpr ⟨hαN _, hsh _ _ hγm⟩)
        have s2 := hmT.stable m γ hγm
        simp only [F]
        rw [hN, s1, s2, ih α γ hα hγm]; ring
      · -- `γ` uses the top generator once: cyclicity and stabilisation
        obtain ⟨a, b, rfl, ha⟩ := exists_split_first (m : ℤ) γ
          (List.count_pos_iff.mp (by omega))
        have hγ' := hγ
        simp only [supp_append_iff, supp_cons_iff] at hγ'
        obtain ⟨hA, -, hB⟩ := hγ'
        have hb : (m : ℤ) ∉ b := by
          intro hm
          have h1 : 0 < b.count (m : ℤ) := List.count_pos_iff.mpr hm
          have h2 : a.count (m : ℤ) = 0 := List.count_eq_zero_of_not_mem ha
          simp only [List.count_append, List.count_cons, beq_self_eq_true,
            if_true] at hγc
          omega
        have low : ∀ (l : List ℤ), Supp (m + 1) l → (m : ℤ) ∉ l → Supp m l := by
          intro l hl hn d hd
          have := hl d hd
          have hne : d ≠ (m : ℤ) := fun e => hn (e ▸ hd)
          push_cast at this; omega
        have hAm := low a hA ha
        have hBm := low b hB hb
        have hshA := hsh m a hAm
        have hshB := hsh m b hBm
        have htop : (m : ℤ) + c = ((k + 1 + m : ℕ) : ℤ) := by
          simp only [hc]; push_cast; ring
        -- left side
        have c1 := hmT.cyclic (k + 1 + m + 1)
          (α ++ a.map (· + c) ++ [((k + 1 + m : ℕ) : ℤ)]) (b.map (· + c))
          (by
            simp only [supp_append_iff, supp_cons_iff]
            refine ⟨⟨(hαN _).mono (Nat.le_succ _), hshA.mono (Nat.le_succ _)⟩,
              ⟨by omega, by push_cast; omega⟩, supp_nil⟩)
          (hshB.mono (Nat.le_succ _))
        have st := hmT.strip (k + 1 + m) (b.map (· + c) ++ α ++ a.map (· + c))
          (supp_append_iff.mpr ⟨supp_append_iff.mpr ⟨hshB, hαN _⟩, hshA⟩)
        have c2 := hmT.cyclic (k + 1 + m) (b.map (· + c)) (α ++ a.map (· + c))
          hshB (supp_append_iff.mpr ⟨hαN _, hshA⟩)
        have ihab := ih α (a ++ b) hα (supp_append_iff.mpr ⟨hAm, hBm⟩)
        -- right side
        have d1 := hmT.cyclic (m + 1) (a ++ [(m : ℤ)]) b
          (supp_append_iff.mpr ⟨hAm.mono (Nat.le_succ _),
            supp_cons_iff.mpr ⟨⟨by omega, by push_cast; omega⟩, supp_nil⟩⟩)
          (hBm.mono (Nat.le_succ _))
        have st2 := hmT.strip m (b ++ a) (supp_append_iff.mpr ⟨hBm, hAm⟩)
        have d2 := hmT.cyclic m b a hBm hAm
        simp only [Int.ofNat_eq_coe] at st st2
        simp only [F, List.map_append, List.map_cons, List.map_nil, htop,
          List.append_assoc, List.cons_append, List.singleton_append,
          List.nil_append] at c1 st c2 ihab d1 st2 d2 ⊢
        rw [hN, c1, st, c2, ihab, d1, st2, d2]; ring
    have := HeckeRel.reduce h (m + 1) F hF β.length h0 β hβ le_rfl
    simp only [F] at this
    exact sub_eq_zero.mp this

/-- **Uniqueness: the axioms determine the trace.** Two functions satisfying
    `IsMarkovTrace` with the same parameters `z` and `h` agree on every
    positive word of every level. So any procedure that evaluates a word using
    only these axioms, as the reducer does, returns the one value they force.
    Induction on the level; inside a level the difference of the two traces
    satisfies the Hecke-tower relations and vanishes on words using the top
    generator at most once (stability, or cyclicity and stripping), so it
    vanishes by `HeckeRel.reduce`. -/
theorem markovTrace_unique {mT₁ mT₂ : ℕ → List ℤ → R}
    {e₁ e₂ : List ℤ → ℕ → List ℤ} {z h : R}
    (h₁ : IsMarkovTrace mT₁ e₁ z h) (h₂ : IsMarkovTrace mT₂ e₂ z h) :
    ∀ (n : ℕ) (w : List ℤ), Supp n w → mT₁ n w = mT₂ n w := by
  intro n
  induction n with
  | zero =>
    intro w hw
    have hwnil : w = [] := by
      cases w with
      | nil => rfl
      | cons c w => have := hw c (by simp); push_cast at this; omega
    subst hwnil
    rw [h₁.normalised, h₂.normalised]
  | succ n ih =>
    intro w hw
    let F : List ℤ → R := fun γ => mT₁ (n + 1) γ - mT₂ (n + 1) γ
    have hF : HeckeRel (n + 1) h F := by
      refine ⟨?_, ?_, ?_⟩
      · intro u v i hs
        simp only [F, h₁.hecke (n + 1) u v i hs, h₂.hecke (n + 1) u v i hs]; ring
      · intro u v i hs
        simp only [F, h₁.braid (n + 1) u v i hs, h₂.braid (n + 1) u v i hs]
      · intro u v i j hij hs
        simp only [F, h₁.far_comm (n + 1) u v i j hij hs,
          h₂.far_comm (n + 1) u v i j hij hs]
    have hcn : ((n + 1 : ℕ) : ℤ) - 1 = (n : ℤ) := by push_cast; ring
    have low : ∀ (l : List ℤ), Supp (n + 1) l → (n : ℤ) ∉ l → Supp n l := by
      intro l hl hm d hd
      have := hl d hd
      have hne : d ≠ (n : ℤ) := fun e => hm (e ▸ hd)
      push_cast at this; omega
    have h0 : ∀ γ, Supp (n + 1) γ → γ.length ≤ w.length →
        γ.count (((n + 1 : ℕ) : ℤ) - 1) ≤ 1 → F γ = 0 := by
      intro γ hγ _ hγc
      rw [hcn] at hγc
      rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hγc with hγc | hγc
      · have hγn : Supp n γ := low γ hγ (fun hm => by
          have : 0 < γ.count (n : ℤ) := List.count_pos_iff.mpr hm
          omega)
        simp only [F, h₁.stable n γ hγn, h₂.stable n γ hγn, ih γ hγn, sub_self]
      · obtain ⟨a, b, rfl, ha⟩ := exists_split_first (n : ℤ) γ
          (List.count_pos_iff.mp (by omega))
        have hγ' := hγ
        simp only [supp_append_iff, supp_cons_iff] at hγ'
        obtain ⟨hA, -, hB⟩ := hγ'
        have hb : (n : ℤ) ∉ b := by
          intro hm
          have e1 : 0 < b.count (n : ℤ) := List.count_pos_iff.mpr hm
          have e2 : a.count (n : ℤ) = 0 := List.count_eq_zero_of_not_mem ha
          simp only [List.count_append, List.count_cons, beq_self_eq_true,
            if_true] at hγc
          omega
        have hAn := low a hA ha
        have hBn := low b hB hb
        have htop : Supp (n + 1) (a ++ [(n : ℤ)]) :=
          supp_append_iff.mpr ⟨hAn.mono (Nat.le_succ _),
            supp_cons_iff.mpr ⟨⟨by omega, by push_cast; omega⟩, supp_nil⟩⟩
        have hBs : Supp (n + 1) b := hBn.mono (Nat.le_succ _)
        have hba : Supp n (b ++ a) := supp_append_iff.mpr ⟨hBn, hAn⟩
        have c₁ := h₁.cyclic (n + 1) (a ++ [(n : ℤ)]) b htop hBs
        have c₂ := h₂.cyclic (n + 1) (a ++ [(n : ℤ)]) b htop hBs
        have s₁ := h₁.strip n (b ++ a) hba
        have s₂ := h₂.strip n (b ++ a) hba
        simp only [Int.ofNat_eq_coe, List.append_assoc, List.singleton_append,
          List.cons_append, List.nil_append] at c₁ c₂ s₁ s₂
        simp only [F, List.append_assoc, List.singleton_append, List.cons_append,
          List.nil_append]
        rw [c₁, c₂, s₁, s₂, ih (b ++ a) hba, sub_self]
    exact sub_eq_zero.mp (HeckeRel.reduce h (n + 1) F hF w.length h0 w hw le_rfl)

end DisjointProduct

/-! ## A computable evaluator

`trWord z h n w` computes the trace of a positive word `w` on `σ_0, …, σ_{n-1}`
in `H_{n+1}(q)`, by the reducer's own algorithm: expand `w` in the standard
basis `T_x` (`x ∈ S_{n+1}`, one-line notation), then peel each `T_x` with the
Markov property. Writing `b` for the position of the top value, `x = x' · s_b ⋯ s_{m-1}`
with `x'` fixing the top point and lengths adding, so
`T_x = T_{x'} T_{s_{m-1}} T_c` with `c = s_{m-2} ⋯ s_b`, and
`tr(T_x) = z · tr(T_{x'} T_c)` one level down.

Every definition here is structurally recursive, so Lean's own termination
check is the termination proof: the evaluator is a total function. Below,
`trWord` is proved to satisfy every axiom of `IsMarkovTrace`
(`trWord_isMarkovTrace`); that is the existence half (Ocneanu), and with
`markovTrace_unique` it is the trace. The `example`s below are kernel-checked
computations, independent of those proofs: the Hecke quadratic, a braid relation, the product law, and agreement
with the length-power trace `(-1)^{|w|}` at `q = -1`. -/

section Evaluator

/-- Swap the entries at positions `i` and `i+1` (right multiplication by `s_i`). -/
def swapAt (w : List ℕ) (i : ℕ) : List ℕ :=
  (w.set i (w.getD (i + 1) 0)).set (i + 1) (w.getD i 0)

/-- Right multiplication of a formal sum of basis elements `T_w` by `T_{s_i}`. -/
def mulGen {R : Type*} [Mul R] (h : R) (e : List (R × List ℕ)) (i : ℕ) :
    List (R × List ℕ) :=
  e.flatMap fun p =>
    if p.2.getD i 0 < p.2.getD (i + 1) 0 then [(p.1, swapAt p.2 i)]
    else [(p.1 * h, p.2), (p.1, swapAt p.2 i)]

def mulGens {R : Type*} [Mul R] (h : R) (e : List (R × List ℕ)) (l : List ℕ) :
    List (R × List ℕ) := l.foldl (mulGen h) e

/-- Trace of a basis element `T_w`, `w` a permutation of `{0,…,m-1}` in one-line
    notation. Peels the top letter: `T_w = T_{w'} T_{s_{m-2}} T_c`. -/
def trBasis {R : Type*} [CommRing R] (z h : R) : ℕ → List ℕ → R
  | 0, _ => 1
  | m + 1, w =>
    if w.getD m 0 = m then trBasis z h m (w.take m)
    else
      let b := w.idxOf m
      let w' := (List.range' b (m - b)).foldl swapAt w
      let c := (List.range' b (m - 1 - b)).reverse
      z * ((mulGens h [(1, w'.take m)] c).map fun p => p.1 * trBasis z h m p.2).sum

/-- The evaluator: trace of a positive word on `σ_0,…,σ_{n-1}` in `H_{n+1}`. -/
def trWord {R : Type*} [CommRing R] (z h : R) (n : ℕ) (w : List ℤ) : R :=
  ((mulGens h [(1, List.range (n + 1))] (w.map Int.toNat)).map
    fun p => p.1 * trBasis z h (n + 1) p.2).sum


example : trWord (5 : ℤ) 3 1 [0, 0] = 3 * 5 + 1 := by decide
example : trWord (5 : ℤ) 3 2 [0, 1, 0] = trWord (5 : ℤ) 3 2 [1, 0, 1] := by decide
example : trWord (-1 : ℤ) 0 3 [0, 2, 1, 1, 0] = (-1) ^ 5 := by decide
example : trWord (5 : ℤ) 3 3 [0, 0, 2, 2] = trWord (5 : ℤ) 3 1 [0, 0] * trWord (5 : ℤ) 3 1 [0, 0] := by decide

/-! ### Proved properties of the evaluator

`trWord` is normalised (`trWord_nil`) and stable under adding a strand
(`trWord_stable`); it also satisfies the Hecke relation (`trWord_hecke`) and
far commutation (`trWord_far_comm`), the braid relation (`trWord_braid`) and
Markov stabilisation (`trWord_strip`), proved further below. Cyclicity is not
yet proved for `trWord`. -/

theorem trBasis_range {R : Type*} [CommRing R] (z h : R) :
    ∀ m : ℕ, trBasis z h m (List.range m) = 1
  | 0 => rfl
  | m + 1 => by
    have e1 : (List.range (m + 1)).getD m 0 = m := by simp
    have e2 : (List.range (m + 1)).take m = List.range m := by
      simp [List.range_succ]
    simp only [trBasis, e1, if_true, e2, trBasis_range z h m]

theorem trWord_nil {R : Type*} [CommRing R] (z h : R) (n : ℕ) :
    trWord z h n [] = 1 := by
  simp [trWord, mulGens, trBasis_range]

theorem swapAt_length (w : List ℕ) (i : ℕ) : (swapAt w i).length = w.length := by
  simp [swapAt]

theorem swapAt_append (w : List ℕ) (x i : ℕ) (hi : i + 1 < w.length) :
    swapAt (w ++ [x]) i = swapAt w i ++ [x] := by
  have h0 : i < w.length := by omega
  simp only [swapAt, List.getD_eq_getElem?_getD, List.getElem?_append_left h0,
    List.getElem?_append_left hi]
  rw [List.set_append_left _ _ h0, List.set_append_left _ _ (by simpa using hi)]

def appTop {R : Type*} (x : ℕ) (p : R × List ℕ) : R × List ℕ := (p.1, p.2 ++ [x])

theorem mulGen_append {R : Type*} [Mul R] (h : R) (x L i : ℕ) (hi : i + 1 < L) :
    ∀ e : List (R × List ℕ), (∀ p ∈ e, p.2.length = L) →
      mulGen h (e.map (appTop x)) i = (mulGen h e i).map (appTop x) ∧
      ∀ p ∈ mulGen h e i, p.2.length = L
  | [], _ => by simp [mulGen]
  | q :: e, he => by
    have hq : q.2.length = L := he q (by simp)
    obtain ⟨ih1, ih2⟩ := mulGen_append h x L i hi e (fun p hp => he p (by simp [hp]))
    have h0 : i < q.2.length := by omega
    have h1 : i + 1 < q.2.length := by omega
    have g0 : (q.2 ++ [x]).getD i 0 = q.2.getD i 0 := by
      simp [List.getD_eq_getElem?_getD, List.getElem?_append_left h0]
    have g1 : (q.2 ++ [x]).getD (i + 1) 0 = q.2.getD (i + 1) 0 := by
      simp [List.getD_eq_getElem?_getD, List.getElem?_append_left h1]
    have sw := swapAt_append q.2 x i h1
    simp only [mulGen, List.map_cons, List.flatMap_cons] at ih1 ih2 ⊢
    refine ⟨?_, ?_⟩
    · rw [List.map_append, ← ih1]
      simp only [appTop, g0, g1]
      split_ifs <;> simp [appTop, sw]
    · intro p hp
      rcases List.mem_append.mp hp with hp | hp
      · split_ifs at hp <;> simp at hp <;>
          rcases hp with rfl | rfl <;> simp [swapAt_length, hq]
      · exact ih2 p hp

theorem mulGens_append {R : Type*} [Mul R] (h : R) (x L : ℕ) :
    ∀ (l : List ℕ) (e : List (R × List ℕ)), (∀ i ∈ l, i + 1 < L) →
      (∀ p ∈ e, p.2.length = L) →
      mulGens h (e.map (appTop x)) l = (mulGens h e l).map (appTop x) ∧
      ∀ p ∈ mulGens h e l, p.2.length = L
  | [], e, _, he => ⟨rfl, he⟩
  | i :: l, e, hl, he => by
    obtain ⟨m1, m2⟩ := mulGen_append h x L i (hl i (by simp)) e he
    have := mulGens_append h x L l (mulGen h e i) (fun j hj => hl j (by simp [hj])) m2
    simp only [mulGens, List.foldl_cons] at this ⊢
    rw [m1]; exact this

theorem trBasis_append {R : Type*} [CommRing R] (z h : R) (m : ℕ) (p : List ℕ)
    (hp : p.length = m) : trBasis z h (m + 1) (p ++ [m]) = trBasis z h m p := by
  subst hp
  have e1 : (p ++ [p.length]).getD p.length 0 = p.length := by
    simp [List.getD_eq_getElem?_getD]
  have e2 : (p ++ [p.length]).take p.length = p := by simp
  simp only [trBasis, e1, if_true, e2]

theorem trWord_stable {R : Type*} [CommRing R] (z h : R) (n : ℕ) (w : List ℤ)
    (hw : Supp n w) : trWord z h (n + 1) w = trWord z h n w := by
  have hl : ∀ i ∈ w.map Int.toNat, i + 1 < n + 1 := by
    intro i hi
    obtain ⟨c, hc, rfl⟩ := List.mem_map.mp hi
    have := hw c hc; omega
  have hr : List.range (n + 1 + 1) = List.range (n + 1) ++ [n + 1] := List.range_succ
  have h0 : [((1 : R), List.range (n + 1 + 1))]
      = [((1 : R), List.range (n + 1))].map (appTop (n + 1)) := by
    simp [appTop, hr]
  obtain ⟨m1, m2⟩ := mulGens_append h (n + 1) (n + 1) (w.map Int.toNat)
    [((1 : R), List.range (n + 1))] hl (by simp)
  unfold trWord
  rw [h0, m1, List.map_map]
  congr 1
  apply List.map_congr_left
  intro p hp
  simp only [Function.comp, appTop]
  rw [trBasis_append z h (n + 1) p.2 (m2 p hp)]


/-! ### The Hecke and far-commutation relations for the evaluator

`trComb` evaluates a formal combination of basis permutations. Pushing a
combination through `mulGens` is linear (`trComb_mulGens`), so each relation
reduces to a single basis permutation, where it is a finite case check.
`PermInv` records that the permutations stay duplicate-free, which rules out
the degenerate case `w(i) = w(i+1)` in the Hecke relation. -/

section HeckeProof
variable {R : Type*} [CommRing R] (z h : R)

def trComb (m : ℕ) (e : List (R × List ℕ)) : R := (e.map fun p => p.1 * trBasis z h m p.2).sum

def scaleTerm (c : R) (p : R × List ℕ) : R × List ℕ := (c * p.1, p.2)

theorem mulGen_app (e₁ e₂ : List (R × List ℕ)) (i : ℕ) :
    mulGen h (e₁ ++ e₂) i = mulGen h e₁ i ++ mulGen h e₂ i := by
  simp [mulGen, List.flatMap_append]

theorem mulGens_app : ∀ (v : List ℕ) (e₁ e₂ : List (R × List ℕ)),
    mulGens h (e₁ ++ e₂) v = mulGens h e₁ v ++ mulGens h e₂ v
  | [], _, _ => rfl
  | i :: v, e₁, e₂ => by
    simp only [mulGens, List.foldl_cons] at *
    rw [mulGen_app]; exact mulGens_app v _ _

theorem mulGen_sc (c : R) (i : ℕ) : ∀ e : List (R × List ℕ),
    mulGen h (e.map (scaleTerm c)) i = (mulGen h e i).map (scaleTerm c)
  | [] => rfl
  | p :: e => by
    have ih := mulGen_sc c i e
    simp only [mulGen, List.map_cons, List.flatMap_cons] at ih ⊢
    rw [ih, List.map_append]
    congr 1
    simp only [scaleTerm]; split_ifs <;> simp_all [scaleTerm, mul_assoc]

theorem mulGens_sc (c : R) : ∀ (v : List ℕ) (e : List (R × List ℕ)),
    mulGens h (e.map (scaleTerm c)) v = (mulGens h e v).map (scaleTerm c)
  | [], _ => rfl
  | i :: v, e => by
    simp only [mulGens, List.foldl_cons] at *
    rw [mulGen_sc]; exact mulGens_sc c v _

theorem evalC_app (m : ℕ) (e₁ e₂ : List (R × List ℕ)) :
    trComb z h m (e₁ ++ e₂) = trComb z h m e₁ + trComb z h m e₂ := by
  induction e₁ with
  | nil => simp [trComb]
  | cons p e ih =>
    simp only [trComb, List.cons_append, List.map_cons, List.sum_cons] at ih ⊢
    rw [ih]; ring

theorem evalC_sc (m : ℕ) (c : R) (e : List (R × List ℕ)) :
    trComb z h m (e.map (scaleTerm c)) = c * trComb z h m e := by
  induction e with
  | nil => simp [trComb]
  | cons p e ih =>
    simp only [trComb, List.map_cons, List.sum_cons] at ih ⊢
    rw [ih]; simp [scaleTerm]; ring

theorem mulGens_nil_left : ∀ v : List ℕ, mulGens h ([] : List (R × List ℕ)) v = []
  | [] => rfl
  | i :: v => by simp only [mulGens, List.foldl_cons] at *; exact mulGens_nil_left v

/-- The value of a single basis element pushed through the word `v`. -/
def trCombOne (v : List ℕ) (m : ℕ) (x : List ℕ) : R := trComb z h m (mulGens h [((1 : R), x)] v)

theorem evalC_mulGens (v : List ℕ) (m : ℕ) : ∀ e : List (R × List ℕ),
    trComb z h m (mulGens h e v) = (e.map fun p => p.1 * trCombOne z h v m p.2).sum
  | [] => by
    simp [trComb, mulGens_nil_left]
  | p :: e => by
    have hp : [p] = [((1 : R), p.2)].map (scaleTerm p.1) := by simp [scaleTerm]
    rw [show p :: e = [p] ++ e from rfl, mulGens_app, evalC_app, evalC_mulGens v m e, hp,
      mulGens_sc, evalC_sc]
    simp [trCombOne, scaleTerm]

end HeckeProof

theorem swapAt_eq (w : List ℕ) (i : ℕ) (hi : i + 1 < w.length) :
    swapAt w i = (w.set i w[i + 1]).set (i + 1) w[i] := by
  have h0 : i < w.length := by omega
  simp [swapAt, List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi,
    List.getElem?_eq_getElem h0]

theorem swapAt_perm (w : List ℕ) (i : ℕ) (hi : i + 1 < w.length) : (swapAt w i).Perm w := by
  rw [swapAt_eq w i hi]; exact List.set_set_perm _ _

theorem swapAt_getD_fst (w : List ℕ) (i : ℕ) (hi : i + 1 < w.length) :
    (swapAt w i).getD i 0 = w.getD (i + 1) 0 := by
  have h0 : i < w.length := by omega
  simp [swapAt, List.getD_eq_getElem?_getD, List.getElem?_set, List.getElem?_eq_getElem hi,
    List.getElem?_eq_getElem h0, h0]

theorem swapAt_getD_snd (w : List ℕ) (i : ℕ) (hi : i + 1 < w.length) :
    (swapAt w i).getD (i + 1) 0 = w.getD i 0 := by
  have h0 : i < w.length := by omega
  simp [swapAt, List.getD_eq_getElem?_getD, List.getElem?_set, List.getElem?_eq_getElem hi,
    List.getElem?_eq_getElem h0, hi]

theorem swapAt_swapAt (w : List ℕ) (i : ℕ) (hi : i + 1 < w.length) :
    swapAt (swapAt w i) i = w := by
  have h0 : i < w.length := by omega
  apply List.ext_getElem?
  intro k
  simp only [swapAt, List.getD_eq_getElem?_getD, List.getElem?_set]
  by_cases a : k = i + 1
  · subst a; simp [hi, h0, List.getElem?_eq_getElem hi, List.getElem?_eq_getElem h0]
  · by_cases b : k = i
    · subst b; simp [hi, h0, List.getElem?_eq_getElem hi, List.getElem?_eq_getElem h0]
    · simp [Ne.symm a, Ne.symm b]

theorem nodup_getD_ne (w : List ℕ) (i : ℕ) (hi : i + 1 < w.length) (hw : w.Nodup) :
    w.getD i 0 ≠ w.getD (i + 1) 0 := by
  have h0 : i < w.length := by omega
  simp only [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi,
    List.getElem?_eq_getElem h0, Option.getD_some]
  intro heq
  have := (List.Nodup.getElem_inj_iff hw).mp heq
  omega

section HeckeRelProof
variable {R : Type*} [CommRing R] (z h : R)

def PermInv (L : ℕ) (e : List (R × List ℕ)) : Prop := ∀ p ∈ e, p.2.length = L ∧ p.2.Nodup

theorem mulGen_inv (L i : ℕ) (hi : i + 1 < L) (e : List (R × List ℕ)) (he : PermInv L e) :
    PermInv L (mulGen h e i) := by
  intro p hp
  simp only [mulGen, List.mem_flatMap] at hp
  obtain ⟨q, hq, hp⟩ := hp
  obtain ⟨hl, hn⟩ := he q hq
  have hpm := swapAt_perm q.2 i (by omega)
  split_ifs at hp <;> simp at hp <;>
    rcases hp with rfl | rfl <;> simp_all [swapAt_length, hpm.nodup_iff]

theorem mulGens_inv (L : ℕ) : ∀ (v : List ℕ) (e : List (R × List ℕ)), (∀ i ∈ v, i + 1 < L) →
    PermInv L e → PermInv L (mulGens h e v)
  | [], _, _, he => he
  | i :: v, e, hv, he => by
    simp only [mulGens, List.foldl_cons] at *
    exact mulGens_inv L v _ (fun j hj => hv j (by simp [hj]))
      (mulGen_inv h L i (hv i (by simp)) e he)

theorem hecke_single (v : List ℕ) (m i : ℕ) (a : R) (w : List ℕ) (hi : i + 1 < w.length)
    (hw : w.Nodup) :
    trComb z h m (mulGens h (mulGen h (mulGen h [(a, w)] i) i) v)
      = h * trComb z h m (mulGens h (mulGen h [(a, w)] i) v)
        + trComb z h m (mulGens h [(a, w)] v) := by
  have hne := nodup_getD_ne w i hi hw
  have g1 := swapAt_getD_fst w i hi
  have g2 := swapAt_getD_snd w i hi
  have ss := swapAt_swapAt w i hi
  rw [evalC_mulGens, evalC_mulGens, evalC_mulGens]
  by_cases hlt : w.getD i 0 < w.getD (i + 1) 0
  · have hn : ¬ (swapAt w i).getD i 0 < (swapAt w i).getD (i + 1) 0 := by omega
    have m1 : mulGen h [(a, w)] i = [(a, swapAt w i)] := by
      simp only [mulGen, List.flatMap_cons, List.flatMap_nil, List.append_nil]; rw [if_pos hlt]
    have m2 : mulGen h [(a, swapAt w i)] i = [(a * h, swapAt w i), (a, w)] := by
      simp only [mulGen, List.flatMap_cons, List.flatMap_nil, List.append_nil]; rw [if_neg hn, ss]
    rw [m1, m2]; simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; ring
  · have hp : (swapAt w i).getD i 0 < (swapAt w i).getD (i + 1) 0 := by omega
    have m1 : mulGen h [(a, w)] i = [(a * h, w), (a, swapAt w i)] := by
      simp only [mulGen, List.flatMap_cons, List.flatMap_nil, List.append_nil]; rw [if_neg hlt]
    have m2 : mulGen h [(a * h, w), (a, swapAt w i)] i
        = [(a * h * h, w), (a * h, swapAt w i), (a, w)] := by
      simp only [mulGen, List.flatMap_cons, List.flatMap_nil, List.append_nil]
      rw [if_neg hlt, if_pos hp, ss]; rfl
    rw [m1, m2]; simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; ring

theorem hecke_comb (v : List ℕ) (m L i : ℕ) (hi : i + 1 < L) : ∀ e : List (R × List ℕ),
    PermInv L e →
    trComb z h m (mulGens h (mulGen h (mulGen h e i) i) v)
      = h * trComb z h m (mulGens h (mulGen h e i) v) + trComb z h m (mulGens h e v)
  | [], _ => by simp [mulGen, mulGens_nil_left, trComb]
  | p :: e, he => by
    have ih := hecke_comb v m L i hi e (fun q hq => he q (by simp [hq]))
    obtain ⟨hl, hn⟩ := he p (by simp)
    have hs := hecke_single z h v m i p.1 p.2 (by omega) hn
    rw [show p :: e = [(p.1, p.2)] ++ e by simp]
    simp only [mulGen_app, mulGens_app, evalC_app]
    rw [hs, ih]; ring

theorem mulGens_cat (e : List (R × List ℕ)) (a b : List ℕ) :
    mulGens h e (a ++ b) = mulGens h (mulGens h e a) b := by
  simp [mulGens, List.foldl_append]

theorem trWord_hecke (n : ℕ) (u v : List ℤ) (i : ℤ) (hs : Supp n (u ++ [i] ++ v)) :
    trWord z h n (u ++ [i, i] ++ v) = h * trWord z h n (u ++ [i] ++ v) + trWord z h n (u ++ v) := by
  have hu : ∀ j ∈ u.map Int.toNat, j + 1 < n + 1 := by
    intro j hj
    obtain ⟨c, hc, rfl⟩ := List.mem_map.mp hj
    have := hs c (by simp [hc]); omega
  have hi : i.toNat + 1 < n + 1 := by have := hs i (by simp); omega
  have h0 : PermInv (n + 1) [((1 : R), List.range (n + 1))] := by
    intro p hp; simp at hp; subst hp; exact ⟨by simp, List.nodup_range⟩
  have hE := mulGens_inv h (n + 1) _ _ hu h0
  have key := hecke_comb z h (v.map Int.toNat) (n + 1) (n + 1) i.toNat hi _ hE
  unfold trWord
  simp only [List.map_append, List.map_cons, List.map_nil, mulGens_cat]
  exact key

end HeckeRelProof

theorem swapAt_getD_other (w : List ℕ) (i k : ℕ) (h1 : k ≠ i) (h2 : k ≠ i + 1) :
    (swapAt w i).getD k 0 = w.getD k 0 := by
  simp [swapAt, List.getD_eq_getElem?_getD, List.getElem?_set, Ne.symm h1, Ne.symm h2]

theorem swapAt_getElem? (w : List ℕ) (i : ℕ) (hi : i + 1 < w.length) (k : ℕ) :
    (swapAt w i)[k]? = if k = i then w[i + 1]? else if k = i + 1 then w[i]? else w[k]? := by
  have h0 : i < w.length := by omega
  rw [swapAt_eq w i hi]
  by_cases a : k = i + 1
  · subst a; simp [List.getElem?_set, hi]
  · by_cases b : k = i
    · subst b; simp [List.getElem?_set, h0, a]
    · simp [List.getElem?_set, Ne.symm a, Ne.symm b, a, b]

theorem swapAt_comm (w : List ℕ) (i j : ℕ) (hij : i + 1 < j ∨ j + 1 < i)
    (hi : i + 1 < w.length) (hj : j + 1 < w.length) :
    swapAt (swapAt w i) j = swapAt (swapAt w j) i := by
  apply List.ext_getElem?
  intro k
  have l1 : j + 1 < (swapAt w i).length := by rw [swapAt_length]; exact hj
  have l2 : i + 1 < (swapAt w j).length := by rw [swapAt_length]; exact hi
  rw [swapAt_getElem? _ j l1, swapAt_getElem? _ i l2]
  simp only [swapAt_getElem? w i hi, swapAt_getElem? w j hj]
  split_ifs <;> first | rfl | omega

section FarCommProof
variable {R : Type*} [CommRing R] (z h : R)

theorem far_single (v : List ℕ) (m i j : ℕ) (a : R) (w : List ℕ) (hij : i + 1 < j ∨ j + 1 < i)
    (hi : i + 1 < w.length) (hj : j + 1 < w.length) :
    trComb z h m (mulGens h (mulGen h (mulGen h [(a, w)] i) j) v)
      = trComb z h m (mulGens h (mulGen h (mulGen h [(a, w)] j) i) v) := by
  have gi1 := swapAt_getD_other w j i (by omega) (by omega)
  have gi2 := swapAt_getD_other w j (i + 1) (by omega) (by omega)
  have gj1 := swapAt_getD_other w i j (by omega) (by omega)
  have gj2 := swapAt_getD_other w i (j + 1) (by omega) (by omega)
  have cm := swapAt_comm w i j hij hi hj
  rw [evalC_mulGens, evalC_mulGens]
  by_cases ci : w.getD i 0 < w.getD (i + 1) 0 <;> by_cases cj : w.getD j 0 < w.getD (j + 1) 0 <;>
    simp only [mulGen, List.flatMap_cons, List.flatMap_nil, List.append_nil, List.cons_append,
      List.nil_append, gi1, gi2, gj1, gj2, ci, cj, if_true, if_false, cm, List.map_cons,
      List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem far_comb (v : List ℕ) (m L i j : ℕ) (hij : i + 1 < j ∨ j + 1 < i)
    (hi : i + 1 < L) (hj : j + 1 < L) :
    ∀ e : List (R × List ℕ), PermInv L e →
    trComb z h m (mulGens h (mulGen h (mulGen h e i) j) v)
      = trComb z h m (mulGens h (mulGen h (mulGen h e j) i) v)
  | [], _ => by simp [mulGen, mulGens_nil_left, trComb]
  | p :: e, he => by
    have ih := far_comb v m L i j hij hi hj e (fun q hq => he q (by simp [hq]))
    obtain ⟨hl, -⟩ := he p (by simp)
    have hs := far_single z h v m i j p.1 p.2 hij (by omega) (by omega)
    rw [show p :: e = [(p.1, p.2)] ++ e by simp]
    simp only [mulGen_app, mulGens_app, evalC_app]
    rw [hs, ih]

theorem trWord_far_comm (n : ℕ) (u v : List ℤ) (i j : ℤ) (hd : 2 ≤ |i - j|)
    (hs : Supp n (u ++ [i, j] ++ v)) :
    trWord z h n (u ++ [i, j] ++ v) = trWord z h n (u ++ [j, i] ++ v) := by
  have hi := hs i (by simp)
  have hj := hs j (by simp)
  have hij : i.toNat + 1 < j.toNat ∨ j.toNat + 1 < i.toNat := by
    rcases le_abs.mp hd with h1 | h1 <;> omega
  have hu : ∀ c ∈ u.map Int.toNat, c + 1 < n + 1 := by
    intro c hc
    obtain ⟨d, hd, rfl⟩ := List.mem_map.mp hc
    have := hs d (by simp [hd]); omega
  have h0 : PermInv (n + 1) [((1 : R), List.range (n + 1))] := by
    intro p hp; simp at hp; subst hp; exact ⟨by simp, List.nodup_range⟩
  have key := far_comb z h (v.map Int.toNat) (n + 1) (n + 1) i.toNat j.toNat hij
    (by omega) (by omega) _ (mulGens_inv h (n + 1) _ _ hu h0)
  unfold trWord
  simp only [List.map_append, List.map_cons, List.map_nil, mulGens_cat]
  exact key

end FarCommProof


/-! ### The braid relation for the evaluator

Same reduction as for the Hecke relation: by linearity it suffices to check one
basis permutation, written as `pre ++ p :: q :: r :: rest`. The six relative
orders of `p, q, r` are checked by case split. -/

theorem swapAt_mid (pre rest : List ℕ) (x y : ℕ) :
    swapAt (pre ++ x :: y :: rest) pre.length = pre ++ y :: x :: rest := by
  apply List.ext_getElem?
  intro k
  rw [swapAt_getElem? _ _ (by simp)]
  by_cases a : k = pre.length
  · subst a; simp
  · by_cases b : k = pre.length + 1
    · subst b; simp
    · simp only [a, b, if_false]
      rcases Nat.lt_or_gt_of_ne a with c | c
      · simp [List.getElem?_append_left c]
      · rw [List.getElem?_append_right (by omega), List.getElem?_append_right (by omega)]
        obtain ⟨d, rfl⟩ : ∃ d, k = pre.length + 2 + d := ⟨k - pre.length - 2, by omega⟩
        simp [show pre.length + 2 + d - pre.length = d + 2 by omega]

theorem getD_mid (pre rest : List ℕ) (x : ℕ) : (pre ++ x :: rest).getD pre.length 0 = x := by
  simp [List.getD_eq_getElem?_getD]

section BraidProof
variable {R : Type*} [CommRing R] (z h : R)

theorem braid_single (v : List ℕ) (m : ℕ) (a : R) (pre rest : List ℕ) (p q r : ℕ)
    (hpq : p ≠ q) (hqr : q ≠ r) (hpr : p ≠ r) :
    trComb z h m (mulGens h (mulGen h (mulGen h (mulGen h [(a, pre ++ p :: q :: r :: rest)]
      pre.length) (pre.length + 1)) pre.length) v)
    = trComb z h m (mulGens h (mulGen h (mulGen h (mulGen h [(a, pre ++ p :: q :: r :: rest)]
      (pre.length + 1)) pre.length) (pre.length + 1)) v) := by
  have s0 : ∀ x y z' : ℕ, swapAt (pre ++ x :: y :: z' :: rest) pre.length
      = pre ++ y :: x :: z' :: rest := fun x y z' => swapAt_mid pre (z' :: rest) x y
  have s1 : ∀ x y z' : ℕ, swapAt (pre ++ x :: y :: z' :: rest) (pre.length + 1)
      = pre ++ x :: z' :: y :: rest := by
    intro x y z'
    have := swapAt_mid (pre ++ [x]) rest y z'
    simpa using this
  have g0 : ∀ x y z' : ℕ, (pre ++ x :: y :: z' :: rest).getD pre.length 0 = x :=
    fun x y z' => getD_mid pre _ x
  have g1 : ∀ x y z' : ℕ, (pre ++ x :: y :: z' :: rest).getD (pre.length + 1) 0 = y := by
    intro x y z'; have := getD_mid (pre ++ [x]) (z' :: rest) y; simpa using this
  have g2 : ∀ x y z' : ℕ, (pre ++ x :: y :: z' :: rest).getD (pre.length + 2) 0 = z' := by
    intro x y z'; have := getD_mid (pre ++ [x, y]) rest z'; simpa using this
  rw [evalC_mulGens, evalC_mulGens]
  rcases Nat.lt_or_gt_of_ne hpq with h1 | h1 <;> rcases Nat.lt_or_gt_of_ne hqr with h2 | h2 <;>
    rcases Nat.lt_or_gt_of_ne hpr with h3 | h3 <;>
    first
    | (exfalso; omega)
    | (simp (disch := omega) only [mulGen, List.flatMap_cons, List.flatMap_nil, List.append_nil,
          List.cons_append, List.nil_append, s0, s1, g0, g1, g2, if_pos, if_neg,
          List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
       all_goals ring)

theorem braid_single' (v : List ℕ) (m i : ℕ) (a : R) (w : List ℕ) (hi : i + 2 < w.length)
    (hw : w.Nodup) :
    trComb z h m (mulGens h (mulGen h (mulGen h (mulGen h [(a, w)] i) (i + 1)) i) v)
    = trComb z h m (mulGens h (mulGen h (mulGen h (mulGen h [(a, w)] (i + 1)) i) (i + 1)) v) := by
  obtain ⟨p, q, r, rest, hd⟩ : ∃ p q r rest, w.drop i = p :: q :: r :: rest := by
    match hm : w.drop i with
    | p :: q :: r :: rest => exact ⟨p, q, r, rest, rfl⟩
    | [] => have := congrArg List.length hm; simp at this; omega
    | [_] => have := congrArg List.length hm; simp at this; omega
    | [_, _] => have := congrArg List.length hm; simp at this; omega
  have hw' : w = w.take i ++ p :: q :: r :: rest := by rw [← hd, List.take_append_drop]
  have hl : (w.take i).length = i := by simp; omega
  rw [hw'] at hw ⊢
  have hn := hw
  simp only [List.nodup_append, List.nodup_cons, List.mem_cons, not_or] at hn
  obtain ⟨-, ⟨⟨hpq, hpr, -⟩, ⟨hqr, -⟩, -⟩, -⟩ := hn
  have := braid_single z h v m a (w.take i) rest p q r hpq hqr hpr
  rw [hl] at this
  exact this

theorem braid_comb (v : List ℕ) (m L i : ℕ) (hi : i + 2 < L) : ∀ e : List (R × List ℕ),
    PermInv L e →
    trComb z h m (mulGens h (mulGen h (mulGen h (mulGen h e i) (i + 1)) i) v)
    = trComb z h m (mulGens h (mulGen h (mulGen h (mulGen h e (i + 1)) i) (i + 1)) v)
  | [], _ => by simp [mulGen, mulGens_nil_left, trComb]
  | p :: e, he => by
    have ih := braid_comb v m L i hi e (fun q hq => he q (by simp [hq]))
    obtain ⟨hl, hn⟩ := he p (by simp)
    have hs := braid_single' z h v m i p.1 p.2 (by omega) hn
    rw [show p :: e = [(p.1, p.2)] ++ e by simp]
    simp only [mulGen_app, mulGens_app, evalC_app]
    rw [hs, ih]

theorem trWord_braid (n : ℕ) (u v : List ℤ) (i : ℤ) (hs : Supp n (u ++ [i, i + 1] ++ v)) :
    trWord z h n (u ++ [i, i + 1, i] ++ v) = trWord z h n (u ++ [i + 1, i, i + 1] ++ v) := by
  have hi := hs i (by simp)
  have hi1 := hs (i + 1) (by simp)
  have e1 : (i + 1).toNat = i.toNat + 1 := by omega
  have hu : ∀ c ∈ u.map Int.toNat, c + 1 < n + 1 := by
    intro c hc
    obtain ⟨d, hd, rfl⟩ := List.mem_map.mp hc
    have := hs d (by simp [hd]); omega
  have h0 : PermInv (n + 1) [((1 : R), List.range (n + 1))] := by
    intro p hp; simp at hp; subst hp; exact ⟨by simp, List.nodup_range⟩
  have key := braid_comb z h (v.map Int.toNat) (n + 1) (n + 1) i.toNat (by omega) _
    (mulGens_inv h (n + 1) _ _ hu h0)
  unfold trWord
  simp only [List.map_append, List.map_cons, List.map_nil, mulGens_cat, e1]
  exact key

end BraidProof


/-! ### Markov stabilisation (`strip`) for the evaluator

Appending the new generator `σ_n` to a word of `H_{n+1}`: every basis
permutation `p ++ [n+1]` is ascending at position `n`, so `σ_n` just swaps, and
one peel of `trBasis` returns `z` times the trace of `p`. `PermR` records that
the permutations stay permutations of `range L`. -/

section StripProof
variable {R : Type*} [CommRing R] (z h : R)

theorem trBasis_strip (n : ℕ) (q : List ℕ) (x : ℕ) (hq : q.length = n)
    (hx : x < n + 1) (hqv : ∀ y ∈ q, y < n + 1) :
    trBasis z h (n + 2) (swapAt (q ++ [x] ++ [n + 1]) n) = z * trBasis z h (n + 1) (q ++ [x]) := by
  have e0 : swapAt (q ++ [x] ++ [n + 1]) n = q ++ [n + 1, x] := by
    have := swapAt_mid q [] x (n + 1); rw [hq] at this; simpa using this
  have hnm : (n + 1) ∉ q := fun hm => by have := hqv _ hm; omega
  have e1 : (q ++ [n + 1, x]).getD (n + 1) 0 = x := by
    have := getD_mid (q ++ [n + 1]) [] x; simp only [List.length_append, hq] at this; simpa using this
  have e2 : (q ++ [n + 1, x]).idxOf (n + 1) = n := by
    rw [List.idxOf_append, if_neg hnm, hq]; simp
  have e3 : swapAt (q ++ [n + 1, x]) n = q ++ [x, n + 1] := by
    have := swapAt_mid q [] (n + 1) x; rw [hq] at this; simpa using this
  have e4 : (q ++ [x, n + 1]).take (n + 1) = q ++ [x] := by
    rw [List.take_append, hq, List.take_of_length_le (by omega)]; simp
  rw [e0]
  show trBasis z h (n + 1 + 1) (q ++ [n + 1, x]) = _
  simp only [trBasis, e1, show x ≠ n + 1 by omega, if_false, e2,
    show n + 1 - n = 1 by omega, show n + 1 - 1 - n = 0 by omega]
  simp [e3, e4, mulGens]

def PermR (L : ℕ) (e : List (R × List ℕ)) : Prop := ∀ p ∈ e, p.2.Perm (List.range L)

theorem mulGen_permR (L i : ℕ) (hi : i + 1 < L) (e : List (R × List ℕ)) (he : PermR L e) :
    PermR L (mulGen h e i) := by
  intro p hp
  simp only [mulGen, List.mem_flatMap] at hp
  obtain ⟨q, hq, hp⟩ := hp
  have hql := (he q hq).length_eq
  simp only [List.length_range] at hql
  split_ifs at hp <;> simp only [List.mem_cons, List.not_mem_nil, or_false] at hp
  · subst hp; exact (swapAt_perm q.2 i (by omega)).trans (he q hq)
  · rcases hp with rfl | rfl
    · exact he q hq
    · exact (swapAt_perm q.2 i (by omega)).trans (he q hq)

theorem mulGens_permR (L : ℕ) : ∀ (v : List ℕ) (e : List (R × List ℕ)), (∀ i ∈ v, i + 1 < L) →
    PermR L e → PermR L (mulGens h e v)
  | [], _, _, he => he
  | i :: v, e, hv, he => by
    simp only [mulGens, List.foldl_cons] at *
    exact mulGens_permR L v _ (fun j hj => hv j (by simp [hj]))
      (mulGen_permR h L i (hv i (by simp)) e he)

theorem strip_comb (n : ℕ) : ∀ e : List (R × List ℕ), PermR (n + 1) e →
    trComb z h (n + 2) (mulGen h (e.map (appTop (n + 1))) n) = z * trComb z h (n + 1) e
  | [], _ => by simp [mulGen, trComb]
  | p :: e, he => by
    have ih := strip_comb n e (fun q hq => he q (by simp [hq]))
    have hp := he p (by simp)
    have hl : p.2.length = n + 1 := by simpa using hp.length_eq
    have hv : ∀ y ∈ p.2, y < n + 1 := fun y hy => by simpa using hp.subset hy
    obtain ⟨q, x, hqx⟩ : ∃ q x, p.2 = q ++ [x] := by
      rcases List.eq_nil_or_concat p.2 with h0 | ⟨q, x, h0⟩
      · rw [h0] at hl; simp at hl
      · exact ⟨q, x, by simpa using h0⟩
    have hq : q.length = n := by rw [hqx] at hl; simpa using hl
    have hx : x < n + 1 := hv x (by rw [hqx]; simp)
    have hqv : ∀ y ∈ q, y < n + 1 := fun y hy => hv y (by rw [hqx]; simp [hy])
    have g0 : (q ++ [x] ++ [n + 1]).getD n 0 = x := by
      have := getD_mid q [n + 1] x; rw [hq] at this; simpa using this
    have g1 : (q ++ [x] ++ [n + 1]).getD (n + 1) 0 = n + 1 := by
      have := getD_mid (q ++ [x]) [] (n + 1); simp only [List.length_append, hq] at this
      simpa using this
    have hs := trBasis_strip z h n q x hq hx hqv
    rw [show p :: e = [p] ++ e by simp, List.map_append, mulGen_app, evalC_app, ih]
    simp only [List.map_cons, List.map_nil, appTop, hqx, mulGen, List.flatMap_cons,
      List.flatMap_nil, List.append_nil, g0, g1, show x < n + 1 from hx, if_true]
    simp only [trComb, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, hs,
      List.singleton_append, hqx]
    ring

theorem trWord_strip (n : ℕ) (w : List ℤ) (hw : Supp n w) :
    trWord z h (n + 1) (w ++ [Int.ofNat n]) = z * trWord z h n w := by
  have hl : ∀ i ∈ w.map Int.toNat, i + 1 < n + 1 := by
    intro i hi
    obtain ⟨c, hc, rfl⟩ := List.mem_map.mp hi
    have := hw c hc; omega
  have hr : List.range (n + 1 + 1) = List.range (n + 1) ++ [n + 1] := List.range_succ
  have h0 : [((1 : R), List.range (n + 1 + 1))]
      = [((1 : R), List.range (n + 1))].map (appTop (n + 1)) := by
    simp [appTop, hr]
  obtain ⟨m1, -⟩ := mulGens_append h (n + 1) (n + 1) (w.map Int.toNat)
    [((1 : R), List.range (n + 1))] hl (by simp)
  have hP : PermR (n + 1) (mulGens h [((1 : R), List.range (n + 1))] (w.map Int.toNat)) :=
    mulGens_permR h (n + 1) _ _ hl (by intro p hp; simp at hp; subst hp; exact List.Perm.refl _)
  have key := strip_comb z h n _ hP
  unfold trWord
  rw [List.map_append, mulGens_cat, h0, m1]
  simp only [List.map_cons, List.map_nil, Int.toNat_natCast]
  show trComb z h (n + 2) (mulGens h _ [n]) = _
  exact key

end StripProof


/-! ### The chain Markov property for the evaluator

`trWord_chain`: appending the descending chain `σ_n σ_{n-1} ⋯ σ_k` to a word of
`H_{n+1}` multiplies the trace by `z` and drops `σ_n`. This is the step of
`trBasis` read backwards, and it is what the cyclicity proof uses. -/

section ChainProof
variable {R : Type*} [CommRing R] (z h : R)

theorem chain_mulGens (c : R) (M : ℕ) : ∀ (d : ℕ) (A B T : List ℕ), B.length = d →
    (∀ x ∈ B, x < M) →
    mulGens h [(c, A ++ B ++ [M] ++ T)] (List.range' A.length d).reverse
      = [(c, A ++ [M] ++ B ++ T)]
  | 0, A, B, T, hB, _ => by
    rw [List.length_eq_zero_iff.mp hB]; simp [mulGens]
  | d + 1, A, B, T, hB, hv => by
    obtain ⟨B', b, rfl⟩ : ∃ B' b, B = B' ++ [b] := by
      rcases List.eq_nil_or_concat B with h0 | ⟨B', b, h0⟩
      · subst h0; simp at hB
      · exact ⟨B', b, by simpa using h0⟩
    have hB' : B'.length = d := by simpa using hB
    have hb : b < M := hv b (by simp)
    rw [List.range'_concat, List.reverse_append]
    simp only [List.reverse_cons, List.reverse_nil, List.nil_append, List.singleton_append]
    have g0 : (A ++ (B' ++ [b]) ++ [M] ++ T).getD (A.length + d) 0 = b := by
      have := getD_mid (A ++ B') (M :: T) b; simp only [List.length_append, hB'] at this
      simpa using this
    have g1 : (A ++ (B' ++ [b]) ++ [M] ++ T).getD (A.length + d + 1) 0 = M := by
      have := getD_mid (A ++ B' ++ [b]) T M; simp only [List.length_append, hB'] at this
      simpa [Nat.add_assoc] using this
    have sw : swapAt (A ++ (B' ++ [b]) ++ [M] ++ T) (A.length + d)
        = A ++ B' ++ [M] ++ (b :: T) := by
      have := swapAt_mid (A ++ B') T b M; simp only [List.length_append, hB'] at this
      simpa using this
    have step : mulGen h [(c, A ++ (B' ++ [b]) ++ [M] ++ T)] (A.length + d)
        = [(c, A ++ B' ++ [M] ++ (b :: T))] := by
      simp only [mulGen, List.flatMap_cons, List.flatMap_nil, List.append_nil, g0, g1,
        if_pos hb, sw]
    rw [Nat.one_mul, show ∀ (e : List (R × List ℕ)) (a : ℕ) (l : List ℕ),
      mulGens h e (a :: l) = mulGens h (mulGen h e a) l from fun _ _ _ => rfl, step]
    rw [chain_mulGens c M d A B' (b :: T) hB' (fun x hx => hv x (by simp [hx]))]
    simp

theorem chain_foldl (M : ℕ) : ∀ (d : ℕ) (A B T : List ℕ), B.length = d →
    (List.range' A.length d).foldl swapAt (A ++ [M] ++ B ++ T) = A ++ B ++ [M] ++ T
  | 0, A, B, T, hB => by rw [List.length_eq_zero_iff.mp hB]; simp
  | d + 1, A, b :: B, T, hB => by
    have hB' : B.length = d := by simpa using hB
    rw [List.range'_succ, List.foldl_cons]
    have sw : swapAt (A ++ [M] ++ b :: B ++ T) A.length = (A ++ [b]) ++ [M] ++ B ++ T := by
      have := swapAt_mid A (B ++ T) M b; simpa using this
    rw [sw]
    have := chain_foldl M d (A ++ [b]) B T hB'
    simp only [List.length_append, List.length_singleton] at this
    rw [this]; simp

theorem trBasis_chain (n k : ℕ) (hk : k ≤ n) (p : List ℕ) (hl : p.length = n + 1)
    (hv : ∀ y ∈ p, y < n + 1) :
    trBasis z h (n + 2) (p.take k ++ [n + 1] ++ p.drop k)
      = z * trComb z h (n + 1) (mulGens h [((1 : R), p)] (List.range' k (n - k)).reverse) := by
  have hA : (p.take k).length = k := by simp; omega
  have hB : (p.drop k).length = n + 1 - k := by simp [hl]
  obtain ⟨B', x, hBx⟩ : ∃ B' x, p.drop k = B' ++ [x] := by
    rcases List.eq_nil_or_concat (p.drop k) with h0 | ⟨B', x, h0⟩
    · rw [h0] at hB; simp at hB; omega
    · exact ⟨B', x, by simpa using h0⟩
  have hB' : B'.length = n - k := by rw [hBx] at hB; simp at hB; omega
  have hx : x < n + 1 := by
    have hm : x ∈ p.drop k := by rw [hBx]; simp
    exact hv x (List.mem_of_mem_drop hm)
  have hnA : (n + 1) ∉ p.take k := fun hm => by
    have := hv _ (List.mem_of_mem_take hm); omega
  have e1 : (p.take k ++ [n + 1] ++ p.drop k).getD (n + 1) 0 = x := by
    rw [hBx]
    have := getD_mid (p.take k ++ [n + 1] ++ B') [] x
    simp only [List.length_append, hA, hB', List.length_singleton] at this
    rw [show k + 1 + (n - k) = n + 1 by omega] at this
    simpa using this
  have e2 : (p.take k ++ [n + 1] ++ p.drop k).idxOf (n + 1) = k := by
    rw [List.append_assoc, List.idxOf_append, if_neg hnA, hA]; simp
  have e3 : (List.range' k (n + 1 - k)).foldl swapAt (p.take k ++ [n + 1] ++ p.drop k)
      = p ++ [n + 1] := by
    have := chain_foldl (n + 1) (n + 1 - k) (p.take k) (p.drop k) [] hB
    rw [hA] at this; simpa using this
  have e4 : (p ++ [n + 1]).take (n + 1) = p := by
    rw [List.take_append, hl, List.take_of_length_le (by omega)]; simp
  show trBasis z h (n + 1 + 1) _ = _
  simp only [trBasis, e1, show x ≠ n + 1 by omega, if_false, e2, e3, e4,
    show n + 1 - 1 - k = n - k by omega]
  rfl

theorem chain_comb (n k : ℕ) (hk : k ≤ n) : ∀ E : List (R × List ℕ), PermR (n + 1) E →
    trComb z h (n + 2) (mulGens h (E.map (appTop (n + 1))) (List.range' k (n + 1 - k)).reverse)
      = z * trComb z h (n + 1) (mulGens h E (List.range' k (n - k)).reverse)
  | [], _ => by simp [mulGens_nil_left, trComb]
  | p :: E, hE => by
    have ih := chain_comb n k hk E (fun q hq => hE q (by simp [hq]))
    have hp := hE p (by simp)
    have hl : p.2.length = n + 1 := by simpa using hp.length_eq
    have hv : ∀ y ∈ p.2, y < n + 1 := fun y hy => by simpa using hp.subset hy
    have hA : (p.2.take k).length = k := by simp; omega
    have hB : (p.2.drop k).length = n + 1 - k := by simp [hl]
    have cm := chain_mulGens h p.1 (n + 1) (n + 1 - k) (p.2.take k) (p.2.drop k) []
      hB (fun y hy => hv y (List.mem_of_mem_drop hy))
    rw [hA] at cm
    have hs := trBasis_chain z h n k hk p.2 hl hv
    have hp1 : [p] = [((1 : R), p.2)].map (scaleTerm p.1) := by simp [scaleTerm]
    rw [show p :: E = [p] ++ E from rfl, List.map_append, mulGens_app, mulGens_app,
      evalC_app, evalC_app, ih]
    rw [hp1, mulGens_sc, evalC_sc]
    simp only [List.map_cons, List.map_nil, scaleTerm, appTop, mul_one]
    rw [show p.2 ++ [n + 1] = p.2.take k ++ p.2.drop k ++ [n + 1] ++ [] by simp, cm]
    simp only [trComb, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, List.append_nil]
    rw [hs]; simp only [trComb]; ring

theorem trWord_chain (n k : ℕ) (hk : k ≤ n) (x : List ℤ) (hx : Supp n x) :
    trWord z h (n + 1) (x ++ ((List.range' k (n + 1 - k)).reverse.map Int.ofNat))
      = z * trWord z h n (x ++ ((List.range' k (n - k)).reverse.map Int.ofNat)) := by
  have hl : ∀ i ∈ x.map Int.toNat, i + 1 < n + 1 := by
    intro i hi
    obtain ⟨c, hc, rfl⟩ := List.mem_map.mp hi
    have := hx c hc; omega
  have hr : List.range (n + 1 + 1) = List.range (n + 1) ++ [n + 1] := List.range_succ
  have h0 : [((1 : R), List.range (n + 1 + 1))]
      = [((1 : R), List.range (n + 1))].map (appTop (n + 1)) := by
    simp [appTop, hr]
  obtain ⟨m1, -⟩ := mulGens_append h (n + 1) (n + 1) (x.map Int.toNat)
    [((1 : R), List.range (n + 1))] hl (by simp)
  have hP : PermR (n + 1) (mulGens h [((1 : R), List.range (n + 1))] (x.map Int.toNat)) :=
    mulGens_permR h (n + 1) _ _ hl (by intro p hp; simp at hp; subst hp; exact List.Perm.refl _)
  have key := chain_comb z h n k hk _ hP
  unfold trWord
  simp only [List.map_append, List.map_map, mulGens_cat, h0, m1]
  have e : ∀ l : List ℕ, List.map (Int.toNat ∘ Int.ofNat) l = l := by
    intro l; simp [Function.comp_def]
  rw [e, e]
  exact key

end ChainProof


/-! ### Cyclicity (Ocneanu existence)

The proof follows Ocneanu, by induction on the level `n`.

* `trWord_chain_ctx`: the chain Markov property in context; its `k = n` case is
  `trWord_markov`, `tr(x σ_n y) = z · tr(x y)` for `x, y` on lower letters.
* A function of a word that satisfies the in-context Hecke, braid and
  far-commutation relations is determined by its values on words using the top
  generator at most once (`HeckeRel.reduce`). Both sides of every identity
  below are such functions.
* `symAll`: `tr(a σ b σ) = tr(b σ a σ)` for `σ = σ_{m+1}`, from cyclicity one
  level down (`F_low`, `F_mid` compute both sides once `a`, `b` use `σ_m` at
  most once).
* `trWord_cyc1`: rotating one letter, by induction on the level; letters below
  the top use the Markov property and the induction hypothesis, the top letter
  uses `symAll`. `trWord_cyclic` rotates blocks letter by letter. -/

section CyclicProof
variable {R : Type*} [CommRing R] (z h : R)

/-- `trWord` in a fixed context satisfies the in-context Hecke-tower relations. -/
theorem trWord_heckeRel_ctx (N k : ℕ) (hk : k ≤ N) (pre suf : List ℤ) (hpre : Supp N pre)
    (hsuf : Supp N suf) : HeckeRel k h (fun y => trWord z h N (pre ++ y ++ suf)) := by
  refine ⟨?_, ?_, ?_⟩
  · intro u v i hs
    have hs' : Supp N ((pre ++ u) ++ [i] ++ (v ++ suf)) := by
      have := hs.mono hk
      simp only [supp_append_iff] at this hpre hsuf ⊢; tauto
    have := trWord_hecke z h N (pre ++ u) (v ++ suf) i hs'
    simp only [List.append_assoc, List.cons_append, List.singleton_append, List.nil_append]
      at this ⊢
    exact this
  · intro u v i hs
    have hs' : Supp N ((pre ++ u) ++ [i, i + 1] ++ (v ++ suf)) := by
      have := hs.mono hk
      simp only [supp_append_iff] at this hpre hsuf ⊢; tauto
    have := trWord_braid z h N (pre ++ u) (v ++ suf) i hs'
    simp only [List.append_assoc, List.cons_append, List.singleton_append, List.nil_append]
      at this ⊢
    exact this
  · intro u v i j hij hs
    have hs' : Supp N ((pre ++ u) ++ [i, j] ++ (v ++ suf)) := by
      have := hs.mono hk
      simp only [supp_append_iff] at this hpre hsuf ⊢; tauto
    have := trWord_far_comm z h N (pre ++ u) (v ++ suf) i j hij hs'
    simp only [List.append_assoc, List.cons_append, List.singleton_append, List.nil_append]
      at this ⊢
    exact this

theorem HeckeRel.congr {k : ℕ} {G G' : List ℤ → R} (hG : HeckeRel k h G)
    (e : ∀ y, G y = G' y) : HeckeRel k h G' := by
  have : G = G' := funext e
  exact this ▸ hG

theorem HeckeRel.sub_smul {k : ℕ} {G₁ G₂ : List ℤ → R} (c : R) (h₁ : HeckeRel k h G₁)
    (h₂ : HeckeRel k h G₂) : HeckeRel k h (fun y => G₁ y - c * G₂ y) := by
  refine ⟨?_, ?_, ?_⟩
  · intro u v i hs
    simp only [h₁.1 u v i hs, h₂.1 u v i hs]; ring
  · intro u v i hs
    simp only [h₁.2.1 u v i hs, h₂.2.1 u v i hs]
  · intro u v i j hij hs
    simp only [h₁.2.2 u v i j hij hs, h₂.2.2 u v i j hij hs]

/-- A block `c` all of whose letters are far from all letters of `y` commutes past `y`. -/
theorem HeckeRel.block {N : ℕ} {G : List ℤ → R} (hG : HeckeRel N h G) :
    ∀ (c y u v : List ℤ), (∀ a ∈ c, ∀ b ∈ y, 2 ≤ |a - b|) →
      Supp N (u ++ c ++ y ++ v) → G (u ++ c ++ y ++ v) = G (u ++ y ++ c ++ v)
  | [], y, u, v, _, _ => by simp
  | T :: c, y, u, v, hcy, hs => by
    have ih := HeckeRel.block hG c y (u ++ [T]) v (fun a ha b hb => hcy a (by simp [ha]) b hb)
      (by simpa using hs)
    have hm := HeckeRel.move hG T y u (c ++ v) (fun b hb => hcy T (by simp) b hb)
      (by
        have : Supp N (u ++ (T :: c) ++ y ++ v) := hs
        simp only [supp_append_iff, supp_cons_iff] at this ⊢; tauto)
    simp only [List.append_assoc, List.cons_append, List.singleton_append, List.nil_append]
      at ih hm ⊢
    rw [ih, hm]

/-- The descending chain `σ_n ⋯ σ_k`, as integer letters. -/
def chainZ (n k : ℕ) : List ℤ := (List.range' k (n + 1 - k)).reverse.map Int.ofNat

theorem chainZ_split (n k : ℕ) (hk : k ≤ n) :
    chainZ n k = chainZ n (k + 1) ++ [(k : ℤ)] := by
  unfold chainZ
  rw [show n + 1 - k = (n + 1 - (k + 1)) + 1 by omega, List.range'_succ]
  simp

theorem chainZ'_split (n k : ℕ) (hk : k + 1 ≤ n) :
    (List.range' k (n - k)).reverse.map Int.ofNat
      = (List.range' (k + 1) (n - (k + 1))).reverse.map Int.ofNat ++ [(k : ℤ)] := by
  rw [show n - k = (n - (k + 1)) + 1 by omega, List.range'_succ]
  simp

theorem mem_chainZ {n k : ℕ} {a : ℤ} (ha : a ∈ chainZ n k) : (k : ℤ) ≤ a ∧ a ≤ n := by
  unfold chainZ at ha
  simp only [List.mem_map, List.mem_reverse, List.mem_range'_1] at ha
  obtain ⟨b, hb, rfl⟩ := ha
  simp only [Int.ofNat_eq_coe]; omega

theorem mem_chainZ' {n k : ℕ} {a : ℤ} (ha : a ∈ (List.range' k (n - k)).reverse.map Int.ofNat) :
    (k : ℤ) ≤ a ∧ a + 1 ≤ n := by
  simp only [List.mem_map, List.mem_reverse, List.mem_range'_1] at ha
  obtain ⟨b, hb, rfl⟩ := ha
  simp only [Int.ofNat_eq_coe]; omega

theorem supp_split_low {k : ℕ} {l : List ℤ} (hl : Supp (k + 1) l) (hm : (k : ℤ) ∉ l) :
    Supp k l := by
  intro d hd
  have := hl d hd
  have hne : d ≠ (k : ℤ) := fun e => hm (e ▸ hd)
  push_cast at this; omega

/-- **Generalised chain Markov property.** -/
theorem trWord_chain_ctx (n : ℕ) : ∀ k : ℕ, k ≤ n → ∀ x y : List ℤ, Supp n x → Supp k y →
    trWord z h (n + 1) (x ++ chainZ n k ++ y)
      = z * trWord z h n (x ++ (List.range' k (n - k)).reverse.map Int.ofNat ++ y)
  | 0, _, x, y, hx, hy => by
    have hy0 : y = [] := by
      cases y with
      | nil => rfl
      | cons c y => have := hy c (by simp); push_cast at this; omega
    subst hy0
    simpa [chainZ] using trWord_chain z h n 0 (Nat.zero_le _) x hx
  | k + 1, hk, x, y, hx, hy => by
    let G : List ℤ → R := fun y => trWord z h (n + 1) (x ++ chainZ n (k + 1) ++ y)
      - z * trWord z h n (x ++ (List.range' (k + 1) (n - (k + 1))).reverse.map Int.ofNat ++ y)
    have hch : Supp (n + 1) (chainZ n (k + 1)) := by
      intro a ha
      obtain ⟨h1, h2⟩ := mem_chainZ ha
      push_cast at h1 h2 ⊢
      exact ⟨by omega, by omega⟩
    have hch' : Supp n ((List.range' (k + 1) (n - (k + 1))).reverse.map Int.ofNat) := by
      intro a ha
      obtain ⟨h1, h2⟩ := mem_chainZ' ha
      push_cast at h1 h2 ⊢
      exact ⟨by omega, by omega⟩
    have hxs : Supp (n + 1) x := hx.mono (Nat.le_succ _)
    have hG : HeckeRel (k + 1) h G := by
      have A := trWord_heckeRel_ctx z h (n + 1) (k + 1) (by omega) (x ++ chainZ n (k + 1)) []
        (supp_append_iff.mpr ⟨hxs, hch⟩) supp_nil
      have B := trWord_heckeRel_ctx z h n (k + 1) hk
        (x ++ (List.range' (k + 1) (n - (k + 1))).reverse.map Int.ofNat) []
        (supp_append_iff.mpr ⟨hx, hch'⟩) supp_nil
      exact (HeckeRel.sub_smul h z A B).congr h (fun y => by
        simp only [G, List.append_nil])
    have hT1 : HeckeRel (n + 1) h (trWord z h (n + 1)) := by
      simpa using trWord_heckeRel_ctx z h (n + 1) (n + 1) le_rfl [] [] supp_nil supp_nil
    have hT0 : HeckeRel n h (trWord z h n) := by
      simpa using trWord_heckeRel_ctx z h n n le_rfl [] [] supp_nil supp_nil
    have hcn : ((k + 1 : ℕ) : ℤ) - 1 = (k : ℤ) := by push_cast; ring
    have h0 : ∀ γ, Supp (k + 1) γ → γ.length ≤ y.length →
        γ.count (((k + 1 : ℕ) : ℤ) - 1) ≤ 1 → G γ = 0 := by
      intro γ hγ _ hγc
      rw [hcn] at hγc
      rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hγc with hγc | hγc
      · -- no σ_k: γ commutes past both chains
        have hγk : Supp k γ := supp_split_low hγ (fun hm => by
          have : 0 < γ.count (k : ℤ) := List.count_pos_iff.mpr hm; omega)
        have far1 : ∀ a ∈ chainZ n (k + 1), ∀ b ∈ γ, 2 ≤ |a - b| := by
          intro a ha b hb
          have := mem_chainZ ha; have := hγk b hb
          rw [abs_of_nonneg (by push_cast at *; omega)]; push_cast at *; omega
        have far0 : ∀ a ∈ (List.range' (k + 1) (n - (k + 1))).reverse.map Int.ofNat,
            ∀ b ∈ γ, 2 ≤ |a - b| := by
          intro a ha b hb
          have := mem_chainZ' ha; have := hγk b hb
          rw [abs_of_nonneg (by omega)]; omega
        have hγn : Supp n γ := hγk.mono (by omega)
        have e1 := hT1.block h _ γ x [] far1
          (by simpa using supp_append_iff.mpr ⟨supp_append_iff.mpr ⟨hxs, hch⟩,
            hγn.mono (Nat.le_succ _)⟩)
        have e0 := hT0.block h _ γ x [] far0
          (by simpa using supp_append_iff.mpr ⟨supp_append_iff.mpr ⟨hx, hch'⟩, hγn⟩)
        have st := trWord_chain z h n (k + 1) hk (x ++ γ) (supp_append_iff.mpr ⟨hx, hγn⟩)
        simp only [List.append_nil] at e1 e0
        simp only [G, e1, e0]
        simp only [chainZ, List.append_assoc] at st ⊢
        rw [st]; ring
      · obtain ⟨p, q, rfl, hp⟩ := exists_split_first (k : ℤ) γ
          (List.count_pos_iff.mp (by omega))
        have hγ' := hγ
        simp only [supp_append_iff, supp_cons_iff] at hγ'
        obtain ⟨hP, -, hQ⟩ := hγ'
        have hq : (k : ℤ) ∉ q := by
          intro hm
          have e1 : 0 < q.count (k : ℤ) := List.count_pos_iff.mpr hm
          have e2 : p.count (k : ℤ) = 0 := List.count_eq_zero_of_not_mem hp
          simp only [List.count_append, List.count_cons, beq_self_eq_true, if_true] at hγc
          omega
        have hPk := supp_split_low hP hp
        have hQk := supp_split_low hQ hq
        have hPn : Supp n p := hPk.mono (by omega)
        have far1 : ∀ a ∈ chainZ n (k + 1), ∀ b ∈ p, 2 ≤ |a - b| := by
          intro a ha b hb
          have := mem_chainZ ha; have := hPk b hb
          rw [abs_of_nonneg (by push_cast at *; omega)]; push_cast at *; omega
        have far0 : ∀ a ∈ (List.range' (k + 1) (n - (k + 1))).reverse.map Int.ofNat,
            ∀ b ∈ p, 2 ≤ |a - b| := by
          intro a ha b hb
          have := mem_chainZ' ha; have := hPk b hb
          rw [abs_of_nonneg (by omega)]; omega
        have hkq : Supp (n + 1) ((k : ℤ) :: q) := supp_cons_iff.mpr
          ⟨⟨by omega, by push_cast; omega⟩, (hQk.mono (by omega))⟩
        have hkq0 : Supp n ((k : ℤ) :: q) := supp_cons_iff.mpr
          ⟨⟨by omega, by omega⟩, (hQk.mono (by omega))⟩
        have e1 := hT1.block h _ p x ((k : ℤ) :: q) far1
          (by simpa using supp_append_iff.mpr ⟨supp_append_iff.mpr ⟨supp_append_iff.mpr
            ⟨hxs, hch⟩, hPn.mono (Nat.le_succ _)⟩, hkq⟩)
        have e0 := hT0.block h _ p x ((k : ℤ) :: q) far0
          (by simpa using supp_append_iff.mpr ⟨supp_append_iff.mpr ⟨supp_append_iff.mpr
            ⟨hx, hch'⟩, hPn⟩, hkq0⟩)
        have ih := trWord_chain_ctx n k (by omega) (x ++ p) q (supp_append_iff.mpr ⟨hx, hPn⟩) hQk
        rw [chainZ_split n k (by omega), chainZ'_split n k hk] at ih
        simp only [G]
        simp only [List.append_assoc, List.cons_append, List.singleton_append,
          List.nil_append] at e1 e0 ih ⊢
        rw [e1, e0, ih]; ring
    exact sub_eq_zero.mp (HeckeRel.reduce h (k + 1) G hG y.length h0 y hy le_rfl)

theorem trWord_heckeRel (N : ℕ) : HeckeRel N h (trWord z h N) :=
  (trWord_heckeRel_ctx z h N N le_rfl [] [] supp_nil supp_nil).congr h (fun y => by simp)

/-- **Markov property in context.** -/
theorem trWord_markov (n : ℕ) (x y : List ℤ) (hx : Supp n x) (hy : Supp n y) :
    trWord z h (n + 1) (x ++ [(n : ℤ)] ++ y) = z * trWord z h n (x ++ y) := by
  have := trWord_chain_ctx z h n n le_rfl x y hx hy
  simpa [chainZ] using this

theorem supp_one {n : ℕ} {c : ℤ} (h0 : 0 ≤ c) (h1 : c < n) : Supp n [c] := by
  intro d hd
  simp only [List.mem_singleton] at hd
  subst hd; exact ⟨h0, h1⟩

theorem suppN (m : ℕ) : Supp (m + 1 + 1) [((m + 1 : ℕ) : ℤ)] :=
  supp_one (by omega) (by push_cast; omega)

theorem suppM {m k : ℕ} (hk : m < k) : Supp k [(m : ℤ)] :=
  supp_one (by omega) (by exact_mod_cast hk)

theorem split_top (m : ℕ) (γ : List ℤ) (hγ : Supp (m + 1) γ)
    (hc : γ.count (((m + 1 : ℕ) : ℤ) - 1) ≤ 1) :
    Supp m γ ∨ ∃ p q, γ = p ++ [(m : ℤ)] ++ q ∧ Supp m p ∧ Supp m q := by
  have hcn : ((m + 1 : ℕ) : ℤ) - 1 = (m : ℤ) := by push_cast; ring
  rw [hcn] at hc
  by_cases hm : (m : ℤ) ∈ γ
  · right
    obtain ⟨p, q, rfl, hp⟩ := exists_split_first (m : ℤ) γ hm
    have hγ' := hγ
    simp only [supp_append_iff, supp_cons_iff] at hγ'
    obtain ⟨hP, -, hQ⟩ := hγ'
    have hq : (m : ℤ) ∉ q := by
      intro hmq
      have e1 : 0 < q.count (m : ℤ) := List.count_pos_iff.mpr hmq
      have e2 : p.count (m : ℤ) = 0 := List.count_eq_zero_of_not_mem hp
      simp [List.count_append] at hc
      omega
    exact ⟨p, q, by simp, supp_split_low hP hp, supp_split_low hQ hq⟩
  · left; exact supp_split_low hγ hm

theorem far_top {m : ℕ} {y : List ℤ} (hy : Supp m y) :
    ∀ a ∈ [((m + 1 : ℕ) : ℤ)], ∀ b ∈ y, 2 ≤ |a - b| := by
  intro a ha b hb
  simp only [List.mem_singleton] at ha; subst ha
  have := hy b hb
  rw [abs_of_nonneg (by push_cast; omega)]; push_cast; omega

theorem far_top' {m : ℕ} {y : List ℤ} (hy : Supp m y) :
    ∀ a ∈ y, ∀ b ∈ [((m + 1 : ℕ) : ℤ)], 2 ≤ |a - b| := by
  intro a ha b hb
  simp only [List.mem_singleton] at hb; subst hb
  have := hy a ha
  rw [abs_of_nonpos (by push_cast; omega)]; push_cast; omega

/-- `tr(a σ_{m+1} b σ_{m+1})` when `b` avoids `σ_m`. -/
theorem F_low (m : ℕ) (a b : List ℤ) (ha : Supp (m + 1) a) (hb : Supp m b) :
    trWord z h (m + 1 + 1) (a ++ [((m + 1 : ℕ) : ℤ)] ++ b ++ [((m + 1 : ℕ) : ℤ)])
      = h * z * trWord z h (m + 1) (a ++ b) + trWord z h (m + 1) (a ++ b) := by
  have hT := trWord_heckeRel z h (m + 1 + 1)
  have hab : Supp (m + 1) (a ++ b) := ha.append (hb.mono (Nat.le_succ _))
  have e1 := hT.block h [((m + 1 : ℕ) : ℤ)] b a [((m + 1 : ℕ) : ℤ)] (far_top hb)
    ((((ha.mono (by omega)).append (suppN m)).append (hb.mono (by omega))).append (suppN m))
  have e2 := hT.1 (a ++ b) [] ((m + 1 : ℕ) : ℤ)
    (((hab.mono (Nat.le_succ _)).append (suppN m)).append supp_nil)
  have e3 := trWord_strip z h (m + 1) (a ++ b) hab
  have e4 := trWord_stable z h (m + 1) (a ++ b) hab
  simp only [Int.ofNat_eq_coe, List.append_nil, List.append_assoc, List.cons_append,
    List.singleton_append, List.nil_append] at e1 e2 e3 e4 ⊢
  rw [e1, e2, e3, e4]; ring

/-- `tr(a σ_{m+1} b σ_{m+1})` when `b = b₁ σ_m b₂`. -/
theorem F_mid (m : ℕ) (a b1 b2 : List ℤ) (ha : Supp (m + 1) a) (hb1 : Supp m b1)
    (hb2 : Supp m b2) :
    trWord z h (m + 1 + 1)
        (a ++ [((m + 1 : ℕ) : ℤ)] ++ (b1 ++ [(m : ℤ)] ++ b2) ++ [((m + 1 : ℕ) : ℤ)])
      = z * h * trWord z h (m + 1) (a ++ (b1 ++ [(m : ℤ)] ++ b2))
        + z * trWord z h (m + 1) (a ++ b1 ++ b2) := by
  have hT := trWord_heckeRel z h (m + 1 + 1)
  have hT0 := trWord_heckeRel z h (m + 1)
  have hs1 : Supp (m + 1) b1 := hb1.mono (Nat.le_succ _)
  have hs2 : Supp (m + 1) b2 := hb2.mono (Nat.le_succ _)
  have hm : Supp (m + 1) [(m : ℤ)] := suppM (Nat.lt_succ_self m)
  have hm2 : Supp (m + 1 + 1) [(m : ℤ)] := suppM (by omega)
  have e1 := hT.block h [((m + 1 : ℕ) : ℤ)] b1 a ([(m : ℤ)] ++ b2 ++ [((m + 1 : ℕ) : ℤ)])
    (far_top hb1)
    ((((ha.mono (by omega)).append (suppN m)).append (hb1.mono (by omega))).append
      ((hm2.append (hb2.mono (by omega))).append (suppN m)))
  have e2 := hT.block h b2 [((m + 1 : ℕ) : ℤ)]
    (a ++ b1 ++ [((m + 1 : ℕ) : ℤ)] ++ [(m : ℤ)]) [] (far_top' hb2)
    ((((((ha.mono (by omega)).append (hb1.mono (by omega))).append (suppN m)).append hm2).append
      (hb2.mono (by omega))).append (suppN m) |>.append supp_nil)
  have hcast : ((m + 1 : ℕ) : ℤ) = (m : ℤ) + 1 := by push_cast; ring
  have e3 := hT.2.1 (a ++ b1) b2 (m : ℤ)
    ((((ha.mono (by omega)).append (hb1.mono (by omega))).append
      (supp_cons_iff.mpr ⟨⟨by omega, by push_cast; omega⟩, supp_one (by omega)
        (by push_cast; omega)⟩)).append (hb2.mono (by omega)))
  have e4 := trWord_markov z h (m + 1) (a ++ b1 ++ [(m : ℤ)]) ([(m : ℤ)] ++ b2)
    ((ha.append hs1).append hm) (hm.append hs2)
  have e5 := hT0.1 (a ++ b1) b2 (m : ℤ) (((ha.append hs1).append hm).append hs2)
  rw [← hcast] at e3
  simp only [List.append_nil, List.append_assoc, List.cons_append,
    List.singleton_append, List.nil_append] at e1 e2 e3 e4 e5 ⊢
  rw [e1, e2, ← e3, e4, e5]; ring

/-- Symmetry `tr(a σ b σ) = tr(b σ a σ)` (`σ = σ_{m+1}`) when `b` avoids `σ_m`. -/
theorem symB (m : ℕ)
    (hFC : ∀ u v, Supp (m + 1) u → Supp (m + 1) v →
      trWord z h (m + 1) (u ++ v) = trWord z h (m + 1) (v ++ u))
    (b : List ℤ) (hb : Supp m b) (a : List ℤ) (ha : Supp (m + 1) a) :
    trWord z h (m + 1 + 1) (a ++ [((m + 1 : ℕ) : ℤ)] ++ b ++ [((m + 1 : ℕ) : ℤ)])
      = trWord z h (m + 1 + 1) (b ++ [((m + 1 : ℕ) : ℤ)] ++ a ++ [((m + 1 : ℕ) : ℤ)]) := by
  let G : List ℤ → R := fun y =>
    trWord z h (m + 1 + 1) (y ++ [((m + 1 : ℕ) : ℤ)] ++ b ++ [((m + 1 : ℕ) : ℤ)])
      - trWord z h (m + 1 + 1) (b ++ [((m + 1 : ℕ) : ℤ)] ++ y ++ [((m + 1 : ℕ) : ℤ)])
  have hbs : Supp (m + 1 + 1) b := hb.mono (by omega)
  have hb1 : Supp (m + 1) b := hb.mono (Nat.le_succ _)
  have hG : HeckeRel (m + 1) h G := by
    have A := trWord_heckeRel_ctx z h (m + 1 + 1) (m + 1) (by omega) []
      ([((m + 1 : ℕ) : ℤ)] ++ b ++ [((m + 1 : ℕ) : ℤ)]) supp_nil
      (((suppN m).append hbs).append (suppN m))
    have B := trWord_heckeRel_ctx z h (m + 1 + 1) (m + 1) (by omega)
      (b ++ [((m + 1 : ℕ) : ℤ)]) [((m + 1 : ℕ) : ℤ)] (hbs.append (suppN m)) (suppN m)
    exact (HeckeRel.sub_smul h 1 A B).congr h (fun y => by
      simp only [G, one_mul, List.nil_append, List.append_assoc])
  have h0 : ∀ γ, Supp (m + 1) γ → γ.length ≤ a.length →
      γ.count (((m + 1 : ℕ) : ℤ) - 1) ≤ 1 → G γ = 0 := by
    intro γ hγ _ hc
    rcases split_top m γ hγ hc with hγm | ⟨p, q, rfl, hp, hq⟩
    · simp only [G]
      rw [F_low z h m γ b hγ hb, F_low z h m b γ hb1 hγm, hFC γ b hγ hb1]
      ring
    · simp only [G]
      rw [F_low z h m _ b hγ hb, F_mid z h m b p q hb1 hp hq]
      have e1 := hFC (p ++ [(m : ℤ)] ++ q) b hγ hb1
      have e2 := trWord_markov z h m p (q ++ b) hp (hq.append hb)
      have e3 := hFC b (p ++ q) hb1 ((hp.append hq).mono (Nat.le_succ _))
      have e4 := trWord_stable z h m (p ++ q ++ b) ((hp.append hq).append hb)
      simp only [List.append_assoc, List.cons_append, List.nil_append] at e1 e2 e3 e4 ⊢
      rw [← e1, e2, e3, e4]; ring
  exact sub_eq_zero.mp (HeckeRel.reduce h (m + 1) G hG a.length h0 a ha le_rfl)

/-- Symmetry when `b = b₁ σ_m b₂`. -/
theorem symMid (m : ℕ)
    (hFC : ∀ u v, Supp (m + 1) u → Supp (m + 1) v →
      trWord z h (m + 1) (u ++ v) = trWord z h (m + 1) (v ++ u))
    (b1 b2 : List ℤ) (hb1 : Supp m b1) (hb2 : Supp m b2) (a : List ℤ) (ha : Supp (m + 1) a) :
    trWord z h (m + 1 + 1)
        (a ++ [((m + 1 : ℕ) : ℤ)] ++ (b1 ++ [(m : ℤ)] ++ b2) ++ [((m + 1 : ℕ) : ℤ)])
      = trWord z h (m + 1 + 1)
        ((b1 ++ [(m : ℤ)] ++ b2) ++ [((m + 1 : ℕ) : ℤ)] ++ a ++ [((m + 1 : ℕ) : ℤ)]) := by
  have hb : Supp (m + 1) (b1 ++ [(m : ℤ)] ++ b2) :=
    ((hb1.mono (Nat.le_succ _)).append (suppM (Nat.lt_succ_self m))).append
      (hb2.mono (Nat.le_succ _))
  let G : List ℤ → R := fun y =>
    trWord z h (m + 1 + 1)
        (y ++ [((m + 1 : ℕ) : ℤ)] ++ (b1 ++ [(m : ℤ)] ++ b2) ++ [((m + 1 : ℕ) : ℤ)])
      - trWord z h (m + 1 + 1)
        ((b1 ++ [(m : ℤ)] ++ b2) ++ [((m + 1 : ℕ) : ℤ)] ++ y ++ [((m + 1 : ℕ) : ℤ)])
  have hbs : Supp (m + 1 + 1) (b1 ++ [(m : ℤ)] ++ b2) := hb.mono (by omega)
  have hG : HeckeRel (m + 1) h G := by
    have A := trWord_heckeRel_ctx z h (m + 1 + 1) (m + 1) (by omega) []
      ([((m + 1 : ℕ) : ℤ)] ++ (b1 ++ [(m : ℤ)] ++ b2) ++ [((m + 1 : ℕ) : ℤ)]) supp_nil
      (((suppN m).append hbs).append (suppN m))
    have B := trWord_heckeRel_ctx z h (m + 1 + 1) (m + 1) (by omega)
      ((b1 ++ [(m : ℤ)] ++ b2) ++ [((m + 1 : ℕ) : ℤ)]) [((m + 1 : ℕ) : ℤ)]
      (hbs.append (suppN m)) (suppN m)
    exact (HeckeRel.sub_smul h 1 A B).congr h (fun y => by
      simp only [G, one_mul, List.nil_append, List.append_assoc])
  have h0 : ∀ γ, Supp (m + 1) γ → γ.length ≤ a.length →
      γ.count (((m + 1 : ℕ) : ℤ) - 1) ≤ 1 → G γ = 0 := by
    intro γ hγ _ hc
    rcases split_top m γ hγ hc with hγm | ⟨p, q, rfl, hp, hq⟩
    · simp only [G]
      rw [symB z h m hFC γ hγm _ hb]; ring
    · simp only [G]
      rw [F_mid z h m _ b1 b2 hγ hb1 hb2, F_mid z h m _ p q hb hp hq]
      have e1 := hFC (p ++ [(m : ℤ)] ++ q) _ hγ hb
      have e2 := trWord_markov z h m p (q ++ b1 ++ b2) hp ((hq.append hb1).append hb2)
      have e3 := trWord_markov z h m b1 (b2 ++ p ++ q) hb1 ((hb2.append hp).append hq)
      have e4 := trWord_stable z h m (p ++ q ++ (b1 ++ b2)) ((hp.append hq).append (hb1.append hb2))
      have e5 := trWord_stable z h m (b1 ++ b2 ++ (p ++ q)) ((hb1.append hb2).append (hp.append hq))
      have e6 := hFC (p ++ q) (b1 ++ b2) ((hp.append hq).mono (Nat.le_succ _))
        ((hb1.append hb2).mono (Nat.le_succ _))
      simp only [List.append_assoc, List.cons_append, List.nil_append] at e1 e2 e3 e4 e5 e6 ⊢
      rw [← e1, e2, e3, ← e4, ← e5, e6]; ring
  exact sub_eq_zero.mp (HeckeRel.reduce h (m + 1) G hG a.length h0 a ha le_rfl)

/-- **Two-crossing symmetry** `tr(a σ b σ) = tr(b σ a σ)`, `σ = σ_{m+1}`,
    `a, b ∈ H_{m+2}`, given full cyclicity one level down. -/
theorem symAll (m : ℕ)
    (hFC : ∀ u v, Supp (m + 1) u → Supp (m + 1) v →
      trWord z h (m + 1) (u ++ v) = trWord z h (m + 1) (v ++ u))
    (a : List ℤ) (ha : Supp (m + 1) a) (b : List ℤ) (hb : Supp (m + 1) b) :
    trWord z h (m + 1 + 1) (a ++ [((m + 1 : ℕ) : ℤ)] ++ b ++ [((m + 1 : ℕ) : ℤ)])
      = trWord z h (m + 1 + 1) (b ++ [((m + 1 : ℕ) : ℤ)] ++ a ++ [((m + 1 : ℕ) : ℤ)]) := by
  let G : List ℤ → R := fun y =>
    trWord z h (m + 1 + 1) (a ++ [((m + 1 : ℕ) : ℤ)] ++ y ++ [((m + 1 : ℕ) : ℤ)])
      - trWord z h (m + 1 + 1) (y ++ [((m + 1 : ℕ) : ℤ)] ++ a ++ [((m + 1 : ℕ) : ℤ)])
  have has : Supp (m + 1 + 1) a := ha.mono (by omega)
  have hG : HeckeRel (m + 1) h G := by
    have A := trWord_heckeRel_ctx z h (m + 1 + 1) (m + 1) (by omega)
      (a ++ [((m + 1 : ℕ) : ℤ)]) [((m + 1 : ℕ) : ℤ)] (has.append (suppN m)) (suppN m)
    have B := trWord_heckeRel_ctx z h (m + 1 + 1) (m + 1) (by omega) []
      ([((m + 1 : ℕ) : ℤ)] ++ a ++ [((m + 1 : ℕ) : ℤ)]) supp_nil
      (((suppN m).append has).append (suppN m))
    exact (HeckeRel.sub_smul h 1 A B).congr h (fun y => by
      simp only [G, one_mul, List.nil_append, List.append_assoc])
  have h0 : ∀ γ, Supp (m + 1) γ → γ.length ≤ b.length →
      γ.count (((m + 1 : ℕ) : ℤ) - 1) ≤ 1 → G γ = 0 := by
    intro γ hγ _ hc
    rcases split_top m γ hγ hc with hγm | ⟨p, q, rfl, hp, hq⟩
    · simp only [G]; rw [symB z h m hFC γ hγm a ha]; ring
    · simp only [G]; rw [symMid z h m hFC p q hp hq a ha]; ring
  exact sub_eq_zero.mp (HeckeRel.reduce h (m + 1) G hG b.length h0 b hb le_rfl)

/-- Rotating a block of letters that each rotate singly. -/
theorem rot_of_single (N : ℕ) (S : ℤ → Prop)
    (hS : ∀ c w, S c → Supp N (c :: w) → trWord z h N (w ++ [c]) = trWord z h N (c :: w)) :
    ∀ u v, (∀ c ∈ u, S c) → Supp N (u ++ v) → trWord z h N (u ++ v) = trWord z h N (v ++ u)
  | [], v, _, _ => by simp
  | c :: u, v, hu, hs => by
    have h1 := hS c (u ++ v) (hu c (by simp)) (by simpa using hs)
    have h2 := rot_of_single N S hS u (v ++ [c]) (fun d hd => hu d (by simp [hd])) (by
      intro d hd; apply hs d; simp only [List.mem_append, List.mem_cons, List.mem_singleton,
        List.cons_append] at hd ⊢; tauto)
    simp only [List.cons_append, List.append_assoc, List.singleton_append, List.nil_append]
      at h1 h2 ⊢
    rw [← h1, h2]

/-- **Single-letter cyclicity** of the evaluator at every level. -/
theorem trWord_cyc1 : ∀ n : ℕ, ∀ c w, Supp n (c :: w) →
    trWord z h n (w ++ [c]) = trWord z h n (c :: w)
  | 0, c, w, hs => by
    have := hs c (by simp); push_cast at this; omega
  | n + 1, c, w, hs => by
    have IH := trWord_cyc1 n
    have hFC : ∀ u v, Supp n u → Supp n v → trWord z h n (u ++ v) = trWord z h n (v ++ u) :=
      fun u v hu hv => rot_of_single z h n (fun _ => True) (fun c w _ hs => IH c w hs) u v
        (fun _ _ => trivial) (hu.append hv)
    -- the generic reduction, for any letter `c`
    have core : ∀ c, 0 ≤ c → c < (n : ℤ) + 1 →
        (∀ γ, Supp n γ → trWord z h (n + 1) (γ ++ [c]) = trWord z h (n + 1) (c :: γ)) →
        (∀ p q, Supp n p → Supp n q →
          trWord z h (n + 1) (p ++ [(n : ℤ)] ++ q ++ [c])
            = trWord z h (n + 1) (c :: (p ++ [(n : ℤ)] ++ q))) →
        ∀ w, Supp (n + 1) w → trWord z h (n + 1) (w ++ [c]) = trWord z h (n + 1) (c :: w) := by
      intro c hc0 hc1 hA hB w hw
      have hcs : Supp (n + 1) [c] := supp_one hc0 (by push_cast; omega)
      let G : List ℤ → R := fun y =>
        trWord z h (n + 1) (y ++ [c]) - trWord z h (n + 1) (c :: y)
      have hG : HeckeRel (n + 1) h G := by
        have A := trWord_heckeRel_ctx z h (n + 1) (n + 1) le_rfl [] [c] supp_nil hcs
        have B := trWord_heckeRel_ctx z h (n + 1) (n + 1) le_rfl [c] [] hcs supp_nil
        exact (HeckeRel.sub_smul h 1 A B).congr h (fun y => by
          simp only [G, one_mul, List.nil_append, List.append_nil, List.singleton_append])
      have h0 : ∀ γ, Supp (n + 1) γ → γ.length ≤ w.length →
          γ.count (((n + 1 : ℕ) : ℤ) - 1) ≤ 1 → G γ = 0 := by
        intro γ hγ _ hcnt
        rcases split_top n γ hγ hcnt with hγn | ⟨p, q, rfl, hp, hq⟩
        · simp only [G]; rw [hA γ hγn]; ring
        · simp only [G]; rw [hB p q hp hq]; ring
      exact sub_eq_zero.mp (HeckeRel.reduce h (n + 1) G hG w.length h0 w hw le_rfl)
    -- letters below the top
    have low : ∀ c, 0 ≤ c → c < (n : ℤ) →
        ∀ w, Supp (n + 1) w → trWord z h (n + 1) (w ++ [c]) = trWord z h (n + 1) (c :: w) := by
      intro c hc0 hc1
      have hcn : Supp n [c] := supp_one hc0 hc1
      refine core c hc0 (by omega) ?_ ?_
      · intro γ hγ
        rw [trWord_stable z h n _ (hγ.append hcn),
          trWord_stable z h n _ (by simpa using hcn.append hγ)]
        exact IH c γ (by simpa using hcn.append hγ)
      · intro p q hp hq
        have e1 := trWord_markov z h n p (q ++ [c]) hp (hq.append hcn)
        have e2 := trWord_markov z h n (c :: p) q (by simpa using hcn.append hp) hq
        have e3 := IH c (p ++ q) (by simpa using hcn.append (hp.append hq))
        simp only [List.append_assoc, List.cons_append, List.singleton_append] at e1 e2 e3 ⊢
        rw [e1, e2, e3]
    obtain ⟨hc0, hc1⟩ := (supp_cons_iff.mp hs).1
    have hw : Supp (n + 1) w := (supp_cons_iff.mp hs).2
    by_cases hcl : c < (n : ℤ)
    · exact low c hc0 hcl w hw
    have hcn : c = (n : ℤ) := by push_cast at hc1; omega
    subst hcn
    have rotLow := rot_of_single z h (n + 1) (fun c => 0 ≤ c ∧ c < (n : ℤ))
      (fun c w hc hs => low c hc.1 hc.2 w (supp_cons_iff.mp hs).2)
    refine core (n : ℤ) hc0 (by omega) ?_ ?_ w hw
    · intro γ hγ
      have e1 := trWord_strip z h n γ hγ
      have e2 := trWord_markov z h n [] γ supp_nil hγ
      simp only [Int.ofNat_eq_coe, List.nil_append, List.singleton_append] at e1 e2
      rw [e1, e2]
    · intro p q hp hq
      have hpqs : Supp (n + 1) ([(n : ℤ)] ++ p ++ [(n : ℤ)]) :=
        ((suppM (Nat.lt_succ_self n)).append (hp.mono (Nat.le_succ _))).append
          (suppM (Nat.lt_succ_self n))
      have e1 := rotLow q ([(n : ℤ)] ++ p ++ [(n : ℤ)]) (fun d hd => hq d hd)
        ((hq.mono (Nat.le_succ _)).append hpqs)
      cases n with
      | zero =>
        have hp0 : p = [] := List.eq_nil_iff_forall_not_mem.mpr (fun d hd => by
          have := hp d hd; push_cast at this; omega)
        have hq0 : q = [] := List.eq_nil_iff_forall_not_mem.mpr (fun d hd => by
          have := hq d hd; push_cast at this; omega)
        subst hp0; subst hq0; rfl
      | succ m =>
        have hFC' : ∀ u v, Supp (m + 1) u → Supp (m + 1) v →
            trWord z h (m + 1) (u ++ v) = trWord z h (m + 1) (v ++ u) := hFC
        have e2 := symAll z h m hFC' p hp q hq
        simp only [List.append_assoc, List.cons_append, List.singleton_append,
          List.nil_append] at e1 e2 ⊢
        rw [e2, ← e1]

/-- **Cyclicity** of the evaluator: `tr(uv) = tr(vu)`. -/
theorem trWord_cyclic (n : ℕ) (u v : List ℤ) (hu : Supp n u) (hv : Supp n v) :
    trWord z h n (u ++ v) = trWord z h n (v ++ u) :=
  rot_of_single z h n (fun _ => True) (fun c w _ hs => trWord_cyc1 z h n c w hs) u v
    (fun _ _ => trivial) (hu.append hv)

/-- **Ocneanu existence.** The recursive evaluator satisfies every axiom of
    `IsMarkovTrace`, for every commutative ring `R` and every `z, h : R`. -/
theorem trWord_isMarkovTrace :
    IsMarkovTrace (fun n w => trWord z h n w) (fun β j => β.map (· + Int.ofNat j)) z h where
  strip := trWord_strip z h
  cyclic := trWord_cyclic z h
  embed_disjoint := fun _ _ => rfl
  normalised := trWord_nil z h
  stable := trWord_stable z h
  hecke := trWord_hecke z h
  braid := trWord_braid z h
  far_comm := trWord_far_comm z h

/-- A Markov trace exists for every `z, h`. -/
theorem exists_isMarkovTrace :
    ∃ (mT : ℕ → List ℤ → R) (e : List ℤ → ℕ → List ℤ), IsMarkovTrace mT e z h :=
  ⟨_, _, trWord_isMarkovTrace z h⟩

/-- Every Markov trace is the evaluator (existence + `markovTrace_unique`). -/
theorem isMarkovTrace_eq_trWord {mT : ℕ → List ℤ → R} {e : List ℤ → ℕ → List ℤ}
    (hmT : IsMarkovTrace mT e z h) (n : ℕ) (w : List ℤ) (hw : Supp n w) :
    mT n w = trWord z h n w :=
  markovTrace_unique hmT (trWord_isMarkovTrace z h) n w hw

end CyclicProof

end Evaluator

end QOU.BraidKnot
