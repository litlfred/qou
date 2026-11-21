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

    Justification (delegated to references): the recursive
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
    are delegated to the references above. -/
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
    ascending run `σ_0 ⋯ σ_{m-1}` shifted past the separating slot onto
    `σ_{k+1} ⋯ σ_{k+m}`, `tr(α ⊗ β) = tr(α) · tr(β)`.  A genuine special case of
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

/-- **The general disjoint-product law** — `tr(α ⊗ β) = tr(α) tr(β)` for `α`
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

end DisjointProduct

end QOU.BraidKnot
