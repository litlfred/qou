import Mathlib.Algebra.Exact
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.Tactic

/-!
# QOU.Mathlib.LongExactSequence — the LES, and the three things it is used for

Bean `qou-fngs`. Until now the corpus had **no** long exact sequence: an audit
on 2026-08-24 found the phrase in exactly two prose lines and zero
declarations, while `rem:self-dual-ses` states a short exact sequence in
Markdown with nothing formal behind it.

That was not for want of Mathlib. `Function.Exact` and `LinearMap.exact_iff`
are there, and this file does not re-derive them. What is missing upstream is
the **packaged ℤ-indexed sequence** and, more to the point, the three
consequences an obstruction argument actually reaches for. Those are the
content here.

## Exactness is a computation rule, not a decoration

An LES is worth having because it converts *vanishing* into *isomorphism*.
Each theorem below is one direction of that trade:

* `surjective_iff_next_eq_zero` — `f_n` is onto **exactly** when `f_{n+1} = 0`.
  Surjectivity is not evidence about `f_n`; it is evidence about its successor.
* `injective_iff_prev_eq_zero` — dually, injectivity of `f_{n+1}` is a fact
  about `f_n`.
* `equivOfNeighboursZero` — both neighbours vanish ⟹ the middle map is an
  isomorphism. This is the one that closes a computation: an unknown module is
  pinned to a known one by two vanishing statements, neither of which mentions
  it.

`map_eq_zero_of_subsingleton` then feeds the machine: a term that is zero
makes both maps touching it zero, so a single vanishing *group* propagates
outward as injectivity and surjectivity of its neighbours. That is how a
long exact sequence is used to compute, and it is why the vanishing results
this corpus keeps assuming are worth proving rather than positing.

## Relation to the spectral-sequence files

`PagedSpectralSequence.turn` is `E_{r+1} ≅ ker d ⧸ im d` — a subquotient. An
LES is the degenerate case where the subquotient vanishes, so exactness holds
on the nose. The two are the same bookkeeping at different resolution, and
`Collapses` is what makes a spectral sequence behave like this file.

## Base ring

`Ring R`, generic. Nothing here is archimedean and nothing needs a field: the
statements are about kernels and ranges, which exist over any ring — including
`R_q = ℤ[q, q⁻¹]`, where the corpus actually works.

-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes
-/

namespace QOU.Mathlib.LongExactSequence

universe u v

variable {R : Type u} [Ring R]

/-- **A long exact sequence**: a `ℤ`-indexed family of modules with maps
    `f_n : M n → M (n+1)`, exact at every spot.

    Indexed by `ℤ` rather than `ℕ` because the sequences this corpus produces
    are two-sided — a connecting map runs *down* in degree — and truncating at
    zero would put a spurious boundary where the mathematics has none. A
    bounded sequence is expressed by making the outlying terms subsingletons,
    which `map_eq_zero_of_subsingleton` turns into exactly the vanishing
    hypotheses the theorems below want. -/
structure LES (R : Type u) [Ring R] (M : ℤ → Type v)
    [∀ n, AddCommGroup (M n)] [∀ n, Module R (M n)] where
  /-- The map out of degree `n`. -/
  map : ∀ n, M n →ₗ[R] M (n + 1)
  /-- Exact at every degree: `ker f_{n+1} = range f_n`. -/
  exact : ∀ n, Function.Exact (map n) (map (n + 1))

variable {M : ℤ → Type v} [∀ n, AddCommGroup (M n)] [∀ n, Module R (M n)]

/-- `ker f_{n+1} = range f_n`, in submodule form. -/
theorem ker_eq_range (L : LES R M) (n : ℤ) :
    LinearMap.ker (L.map (n + 1)) = LinearMap.range (L.map n) :=
  LinearMap.exact_iff.mp (L.exact n)

/-- Consecutive maps compose to zero — the half of exactness that always
    holds, recorded because it is what most calculations touch first. -/
theorem comp_eq_zero (L : LES R M) (n : ℤ) :
    (L.map (n + 1)).comp (L.map n) = 0 := by
  ext x
  have : L.map n x ∈ LinearMap.ker (L.map (n + 1)) := by
    rw [ker_eq_range]
    exact ⟨x, rfl⟩
  simpa using this

/-- **Surjectivity is a statement about the next map.**

    `f_n` is onto exactly when `f_{n+1}` is zero. Read right to left this is
    the workhorse: prove something vanishes one step along, and you have
    surjectivity here for free. -/
theorem surjective_iff_next_eq_zero (L : LES R M) (n : ℤ) :
    Function.Surjective (L.map n) ↔ L.map (n + 1) = 0 := by
  rw [← LinearMap.range_eq_top, ← ker_eq_range L n, LinearMap.ker_eq_top]

/-- **Injectivity is a statement about the previous map.** Dual to the above,
    and the reason a vanishing term propagates in both directions. -/
theorem injective_iff_prev_eq_zero (L : LES R M) (n : ℤ) :
    Function.Injective (L.map (n + 1)) ↔ L.map n = 0 := by
  rw [← LinearMap.ker_eq_bot, ker_eq_range L n, LinearMap.range_eq_bot]

/-- A zero module has only the zero map out of it. Trivial, and it is the
    input the theorems above are shaped for: it converts "this group vanishes"
    — the form vanishing results are always stated in — into the "this map
    vanishes" form exactness consumes. -/
theorem map_eq_zero_of_subsingleton (L : LES R M) (n : ℤ) [Subsingleton (M n)] :
    L.map n = 0 := by
  ext x
  simp [Subsingleton.elim x 0]

/-- A map **into** a zero module is zero. The companion to the above: a
    vanishing term kills the map arriving at it as well as the one leaving. -/
theorem map_eq_zero_of_subsingleton_target (L : LES R M) (n : ℤ)
    [Subsingleton (M (n + 1))] : L.map n = 0 := by
  ext x
  exact Subsingleton.elim _ _

/-- A vanishing term makes the map **out of its successor position** injective. -/
theorem injective_of_subsingleton (L : LES R M) (n : ℤ) [Subsingleton (M n)] :
    Function.Injective (L.map (n + 1)) :=
  (injective_iff_prev_eq_zero L n).mpr (map_eq_zero_of_subsingleton L n)

/-- A vanishing term two steps along makes `f_n` surjective.

    The target, not the source: `f_n` is onto when `f_{n+1}` is zero
    (`surjective_iff_next_eq_zero`), and what makes `f_{n+1}` zero without
    also collapsing `f_n`'s own target is `M_{n+2}` vanishing. Deriving it
    from `Subsingleton (M (n+1))` instead would be true and useless — that
    hypothesis makes `f_n`'s codomain trivial, so surjectivity says nothing. -/
theorem surjective_of_subsingleton_target (L : LES R M) {n p : ℤ}
    (hp : n + 1 + 1 = p) [Subsingleton (M p)] :
    Function.Surjective (L.map n) := by
  subst hp
  exact (surjective_iff_next_eq_zero L n).mpr (map_eq_zero_of_subsingleton_target L (n + 1))

/-- **The theorem that closes a computation.**

    If the maps on both sides vanish, `f_n` is an isomorphism — so an unknown
    module is pinned to a known one by two vanishing statements, neither of
    which mentions it. This is what an LES is *for*, and it is the shape every
    "the obstruction vanishes, therefore the two agree" argument in the corpus
    wants underneath it.

    The predecessor index is carried as an equation rather than written `n-1`,
    because `n - 1 + 1` is only propositionally `n` in `ℤ` and the difference
    is a type mismatch on `M`. `subst` then discharges the transport. -/
theorem bijective_of_neighbours_zero (L : LES R M) {m n : ℤ} (hmn : m + 1 = n)
    (hprev : L.map m = 0) (hnext : L.map (n + 1) = 0) :
    Function.Bijective (L.map n) := by
  subst hmn
  exact ⟨(injective_iff_prev_eq_zero L m).mpr hprev,
    (surjective_iff_next_eq_zero L (m + 1)).mpr hnext⟩

/-- The isomorphism `bijective_of_neighbours_zero` provides. -/
noncomputable def equivOfNeighboursZero (L : LES R M) {m n : ℤ} (hmn : m + 1 = n)
    (hprev : L.map m = 0) (hnext : L.map (n + 1) = 0) :
    M n ≃ₗ[R] M (n + 1) :=
  LinearEquiv.ofBijective (L.map n) (bijective_of_neighbours_zero L hmn hprev hnext)

/-- **The classic pattern**, from vanishing *terms* rather than vanishing maps:

        ⋯ → 0 → M n → M (n+1) → 0 → ⋯

    flanked by zeros on both sides, the middle map is an isomorphism. This is
    the form a computation actually presents — vanishing results are statements
    about groups, not about maps. -/
noncomputable def equivOfFlankingTermsZero (L : LES R M) {m n p : ℤ}
    (hmn : m + 1 = n) (hp : n + 1 + 1 = p)
    [Subsingleton (M m)] [Subsingleton (M p)] :
    M n ≃ₗ[R] M (n + 1) :=
  equivOfNeighboursZero L hmn (map_eq_zero_of_subsingleton L m)
    (by subst hp; exact map_eq_zero_of_subsingleton_target L (n + 1))

/-- **The quotient description.** Where `f_{n+1}` is onto, its target is the
    middle modulo the previous image — `M_{n+2} ≅ M_{n+1} ⧸ im f_n`.

    Stated because vanishing is not always available: when the sequence does
    not degenerate, this is what an exact spot still gives you. -/
noncomputable def quotEquivOfSurjective (L : LES R M) (n : ℤ)
    (hsurj : Function.Surjective (L.map (n + 1))) :
    (M (n + 1) ⧸ LinearMap.range (L.map n)) ≃ₗ[R] M (n + 1 + 1) :=
  Function.Exact.linearEquivOfSurjective (L.exact n) hsurj

end QOU.Mathlib.LongExactSequence
