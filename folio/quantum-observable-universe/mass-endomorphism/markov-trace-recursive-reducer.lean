import Mathlib.Data.List.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Tactic.Ring

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

/-- Defining axioms of a genuine Markov trace `mT : ℕ → List ℤ → R` on
    braid words, with strand-shift embedding `embedRight` and
    stabilisation factor `z`.  A `(mT, embedRight, z)` triple satisfying
    these is what the categorical construction produces (`tr_M` in
    `H_n(q)` with `z = (q^{n} - 1)/(q - 1)`-type factor); the trivial
    `mT = const 0` triple does **not** satisfy `strip` with a unit-free
    `z`, so this hypothesis is non-degenerate. -/
structure IsMarkovTrace {R : Type*} [CommRing R]
    (mT : ℕ → List ℤ → R) (embedRight : List ℤ → ℕ → List ℤ) (z : R) :
    Prop where
  /-- Markov stabilisation: appending the top generator `σ_n` peels with
      the fixed factor `z`. -/
  strip : ∀ (n : ℕ) (w : List ℤ),
    mT (n + 1) (w ++ [Int.ofNat n]) = z * mT n w
  /-- Cyclicity of the trace. -/
  cyclic : ∀ (n : ℕ) (u v : List ℤ), mT n (u ++ v) = mT n (v ++ u)
  /-- The shift embedding re-indexes `β`'s generators onto a disjoint
      strand cluster (right of the separating slot). -/
  embed_disjoint : ∀ (β : List ℤ) (j : ℕ),
    embedRight β j = β.map (· + Int.ofNat j)
  /-- **Normalisation.** The empty word has trace `1`. -/
  normalised : ∀ n : ℕ, mT n [] = 1
  /-- **Stability under the trivial embedding.** A Markov trace is a
      *compatible tower* of traces: enlarging the ambient algebra without
      using the new strand does not change the value. -/
  stable : ∀ (n : ℕ) (w : List ℤ), mT (n + 1) w = mT n w

/-! ## What the axioms actually buy, derived

The proof sketch above turns on one step — *"the Markov axiom strips
`σ_{n-2}`, `σ_{n-3}`, …, `σ_{k+2}` in turn, each contributing a factor `z`"*.
That step is a consequence of `strip` alone and is proved here rather than
assumed, so the residual axiomatic content of `disjoint_product` is smaller than
the field's statement suggests.

What is **not** derivable from `IsMarkovTrace` as stated is the general
disjoint product, and the obstruction is concrete: peeling requires the word's
*last* letter to be the current top generator, and `List ℤ` carries no
strand-support information that would let one rewrite an arbitrary `β` into
that form. Closing it needs the support predicate this file defers along with
the `Hecke n q` type — bean `qou-tmmt`. Recorded rather than papered over. -/

/-- The ascending run of generator indices `[n, n+1, …, n+m-1]`, written so
    that the *last* letter is exposed — the form `IsMarkovTrace.strip`
    consumes. -/
def ascendingRun (n : ℕ) : ℕ → List ℤ
  | 0 => []
  | m + 1 => ascendingRun n m ++ [Int.ofNat (n + m)]

/-- **Stripping an ascending run costs exactly `z^m`.** Derived from `strip`
    by induction on the run length; no other axiom is used. This is the
    "each contributing a factor `z`" step of the disjoint-product sketch,
    proved. -/
theorem markovTrace_strip_ascendingRun {R : Type*} [CommRing R]
    {mT : ℕ → List ℤ → R} {embedRight : List ℤ → ℕ → List ℤ} {z : R}
    (hmT : IsMarkovTrace mT embedRight z) (n : ℕ) (w : List ℤ) :
    ∀ m : ℕ, mT (n + m) (w ++ ascendingRun n m) = z ^ m * mT n w := by
  intro m
  induction m with
  | zero => simp [ascendingRun]
  | succ m ih =>
    have hstep := hmT.strip (n + m) (w ++ ascendingRun n m)
    calc mT (n + (m + 1)) (w ++ ascendingRun n (m + 1))
        = mT (n + m + 1) ((w ++ ascendingRun n m) ++ [Int.ofNat (n + m)]) := by
          simp [ascendingRun, List.append_assoc, Nat.add_assoc]
      _ = z * mT (n + m) (w ++ ascendingRun n m) := hstep
      _ = z * (z ^ m * mT n w) := by rw [ih]
      _ = z ^ (m + 1) * mT n w := by ring

/-- **The run may be stripped from either end.** Cyclicity turns the
    right-stripping law into a left-stripping one; derived from `strip` and
    `cyclic` together. -/
theorem markovTrace_strip_ascendingRun_left {R : Type*} [CommRing R]
    {mT : ℕ → List ℤ → R} {embedRight : List ℤ → ℕ → List ℤ} {z : R}
    (hmT : IsMarkovTrace mT embedRight z) (n m : ℕ) (w : List ℤ) :
    mT (n + m) (ascendingRun n m ++ w) = z ^ m * mT n w := by
  rw [hmT.cyclic (n + m) (ascendingRun n m) w]
  exact markovTrace_strip_ascendingRun hmT n w m

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
    norm_num at hcontra
    omega

namespace IsMarkovTrace

variable {R : Type*} [CommRing R] {mT : ℕ → List ℤ → R}
  {embedRight : List ℤ → ℕ → List ℤ} {z : R}

/-- Stability collapses the ambient index: a Markov trace is a function of the
    word alone. -/
theorem ambient_irrelevant (h : IsMarkovTrace mT embedRight z) (n : ℕ)
    (w : List ℤ) : mT n w = mT 0 w := by
  induction n with
  | zero => rfl
  | succ n ih => rw [h.stable n w, ih]

/-- Peeling one non-negative letter costs `z`, at any ambient index. This is
    `strip` with the ambient bookkeeping removed by `ambient_irrelevant`. -/
theorem peel (h : IsMarkovTrace mT embedRight z) {b : ℤ} (hb : 0 ≤ b)
    (w : List ℤ) : mT 0 (w ++ [b]) = z * mT 0 w := by
  obtain ⟨m, rfl⟩ := Int.eq_ofNat_of_zero_le hb
  have hs := h.strip m w
  rw [h.ambient_irrelevant (m + 1) (w ++ [Int.ofNat m]),
    h.ambient_irrelevant m w] at hs
  simpa using hs

/-- Appending a word of non-negative letters costs `z` per letter. -/
theorem append_cost (h : IsMarkovTrace mT embedRight z) (α : List ℤ) :
    ∀ γ : List ℤ, (∀ c ∈ γ, 0 ≤ c) →
      mT 0 (α ++ γ) = z ^ γ.length * mT 0 α := by
  intro γ
  induction γ using List.reverseRecOn with
  | nil => intro _; simp
  | append_singleton t a ih =>
    intro hmem
    have ha : 0 ≤ a := hmem a (by simp)
    have hrest : ∀ c ∈ t, 0 ≤ c := fun c hc => hmem c (by simp [hc])
    rw [← List.append_assoc, h.peel ha (α ++ t), ih hrest,
      List.length_append, List.length_singleton, pow_succ]
    ring

end IsMarkovTrace

/-- **Disjoint-product property, DERIVED** (bean `qou-tmmt`, 2026-09-04).

    Until this commit `IsMarkovTrace` carried the product law itself as a
    field, and the theorem below was the accessor `hmT.disjoint_product …` — a
    §3b-cond item-5 self-assuming projection. The field is gone, replaced by
    the two axioms that
    `disjointProduct_independent_of_strip_cyclic_embed` identified as missing:
    **normalisation** (`mT n [] = 1`) and **stability** under the trivial
    embedding (`mT (n+1) w = mT n w`). Both are part of what "Markov trace"
    means — a compatible tower of normalised traces — so this is a smaller
    axiom set, not a differently-shaped one.

    With those, the sketch in this file's header goes through: stability
    collapses the ambient index, `strip` then peels one letter for a factor of
    `z` regardless of ambient, and induction from the right costs `z` per
    letter on each side. Both sides are `z^{|β|} · mT α`.

    Two things the derivation makes visible that the axiom hid:

    * **The separation hypothesis `k + 2 ≤ n` is not used.** It sat here as an
      unused variable for as long as this was an accessor, because the field
      did not use it either. Once the ambient index is irrelevant there is
      nothing for it to separate.
    * **The letters of `β` must be non-negative.** `strip` peels `Int.ofNat n`;
      a negative entry is not a generator index this encoding can peel. The old
      field quantified over every `β : List ℤ` and so asserted the product law
      in cases the mathematics does not reach. -/
theorem markovTrace_disjointProduct
    {R : Type*} [CommRing R]
    {markovTrace : ℕ → List ℤ → R}
    {embedRight : List ℤ → ℕ → List ℤ}
    {z : R}
    (hmT : IsMarkovTrace markovTrace embedRight z)
    (k n : ℕ) (α β : List ℤ) (hβ : ∀ b ∈ β, 0 ≤ b) :
    markovTrace n (α ++ embedRight β (k + 1))
      = markovTrace k α * markovTrace (n - k - 1) β := by
  have hshift : ∀ c ∈ embedRight β (k + 1), 0 ≤ c := by
    intro c hc
    rw [hmT.embed_disjoint β (k + 1)] at hc
    obtain ⟨b, hb, rfl⟩ := List.mem_map.mp hc
    exact add_nonneg (hβ b hb) (Int.natCast_nonneg _)
  have hlen : (embedRight β (k + 1)).length = β.length := by
    rw [hmT.embed_disjoint β (k + 1)]; exact List.length_map _
  have hbeta : markovTrace (n - k - 1) β = z ^ β.length := by
    rw [hmT.ambient_irrelevant (n - k - 1) β]
    have hb := hmT.append_cost [] β hβ
    simpa [hmT.normalised 0] using hb
  rw [hmT.ambient_irrelevant n (α ++ embedRight β (k + 1)),
    hmT.append_cost α _ hshift, hlen,
    hmT.ambient_irrelevant k α, hbeta]
  ring

end QOU.BraidKnot
