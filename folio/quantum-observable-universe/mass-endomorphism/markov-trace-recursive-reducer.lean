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
    recursive and so terminating by Lean's own check; that it satisfies the
    `IsMarkovTrace` axioms is not proved.
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
    those axioms, is the trace.

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
check is the termination proof: the evaluator is a total function. What is
NOT proved is that `trWord` satisfies all axioms of `IsMarkovTrace` (proved
below: `normalised`, `stable`, `hecke`, `far_comm`); that is
the existence half (Ocneanu). By `markovTrace_unique`, if it does, it is the
trace. The `example`s below are kernel-checked computations, not proofs of the
axioms: the Hecke quadratic, a braid relation, the product law, and agreement
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
far commutation (`trWord_far_comm`), proved further below. Strip, cyclicity
and the braid relation are not yet proved for `trWord`. -/

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

end Evaluator

end QOU.BraidKnot
