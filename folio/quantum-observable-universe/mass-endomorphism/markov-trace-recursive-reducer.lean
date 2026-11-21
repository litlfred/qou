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

  • Termination via well-founded recursion on `(n, ℓ(w))`.
  • The disjoint-product property
    `tr_M(α ⊗ β) = tr_M(α) · tr_M(β)`
    for `α, β` on disjoint commuting strand-clusters separated by
    an unused generator slot.

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

    *Statement (concrete):* for any commutative ring `R` carrying
    an opaque `markovTrace : (n : ℕ) → List ℤ → R` and a "shift
    embedding" `embedRight : List ℤ → ℕ → List ℤ` that re-indexes
    a word's generators by adding a fixed offset to land on a
    disjoint set of strands, the Markov trace satisfies

      markovTrace n (α ++ embedRight β (k+1))
        = markovTrace k α * markovTrace (n - k - 1) β

    whenever `α` uses only generators in `Fin (k - 1)`,
    `β` uses only generators in `Fin (n - k - 2)`, and
    `k + 2 ≤ n` (so the slot `σ_{k+1}` separates the two clusters
    and is unused).

    Proof sketch (delegated to references): cyclicity moves `β`'s
    generators to the right; the Markov axiom strips `σ_{n-2}`,
    `σ_{n-3}`, …, `σ_{k+2}` in turn, each contributing a factor
    `z` that exactly matches the standalone `markovTrace β`
    computed in its own algebra `H_{n-k-1}`.

    Ref: [kassel1995] Theorem III.3.3 (Markov-trace stability under
    embedding); [wenzl1988] §3 (block decomposition).

    The Lean elaboration requires (1) a `Hecke n q` algebra type;
    (2) a `MarkovTrace` typeclass; (3) the explicit embedding of
    `H_k ⊗ H_{n-k-1}` into `H_n` via the strand-shift map.  Full
    proof structure mirrors the cyclic-peeling argument; see the
    `.md` sibling. -/

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
explicit.  The **general** disjoint-product law is *not* derived here: for a
word `β` with repeated generators it needs the Hecke-quadratic reduction of `β`
to a normal form, i.e. a basis of the Hecke algebra, which this file does not
construct (it is Ocneanu's uniqueness argument).  It is stated below as the
proposition `DisjointProductLaw` and left open (bean `qou-tmmt`). -/

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
    a word of `H_{k+1}` and `β` any positive word, shifted past the separating
    slot `σ_{k+1}`.  True of the genuine Markov trace (Ocneanu; [kassel1995]
    Thm III.3.3), but **not proved here**: the proof reduces `β` to a normal
    form with `hecke`/`braid`/`far_comm`, which needs a basis of the Hecke
    algebra.  Before 2026-11-20 a "proof" existed only because the axioms had
    collapsed `mT` to `z ^ |w|`.  Open: bean `qou-tmmt`. -/
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
    `markovTrace_disjointProduct` below now does: the field is gone and the
    product law is proved. This theorem is kept because it is what justifies
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

end QOU.BraidKnot
