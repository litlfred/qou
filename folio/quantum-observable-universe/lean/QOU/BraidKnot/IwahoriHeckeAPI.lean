import Mathlib.Data.Nat.Dist
import Mathlib.Algebra.Star.Basic
import Mathlib.Algebra.Module.Basic
import Mathlib.GroupTheory.GroupAction.Basic

/-!
# Iwahori--Hecke algebra API (scaffolding for QOU's graded-Mikusiński framework)

This file provides a Mathlib-style API for the Iwahori–Hecke algebra
`H_n(q)` over a commutative ring `R`, structured to support QOU's
graded-Mikusiński / Goncharov-period framework
(`conj:gb-depth-period-correspondence`).

The core `IwahoriHeckeAlgebra` structure is defined as a class with
the standard relations + a bar involution + Markov trace. Specific
results — Wedderburn decomposition at generic `q`, central
idempotent formulas via Jucys–Murphy elements — are stated as
theorems with `sorry` references to upstream sources (Kassel 1995,
Hoefsmit, Murphy, Dipper–James), pending Mathlib's eventual
formalisation.

This scaffolding lets QOU's content blocks
(`hecke-baer-star-generic.lean`, `explicit-central-idempotent.lean`,
`gb-depth-period-correspondence.lean`, etc.) cite a concrete Lean
API rather than `True` placeholders. When Mathlib upstreams an
`IwahoriHeckeAlgebra`, these files migrate by re-binding the
opaque definitions to Mathlib's official ones.
-/

namespace QOU.BraidKnot.IwahoriHeckeAPI

/-! ## Core algebra structure -/

/-- The **Iwahori–Hecke algebra** `H_n(q)` of type `A_{n-1}` over a
    commutative ring `R` with invertible element `q ∈ R^×`. The
    algebra has braid generators `σ_i` (`i = 1, …, n - 1`) satisfying:

    1. *Quadratic relation* `(σ_i - q)(σ_i + q⁻¹) = 0`;
    2. *Braid relation* `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`;
    3. *Far commutativity* `σ_i σ_j = σ_j σ_i` for `|i - j| ≥ 2`.

    The bar involution `* : H_n(q) → H_n(q)` is the antilinear
    extension of `σ_i ↦ σ_i⁻¹`, `q ↦ q⁻¹`. The Markov trace is the
    unique linear functional `tr_M : H_n(q) → R` invariant under
    Markov moves (stabilisation + conjugation).

    This is a placeholder structure pending Mathlib's eventual
    formalisation. The opaque type carries enough hypotheses to
    state and prove the structural results we need, but concrete
    construction is deferred. -/
structure IwahoriHeckeAlgebra (n : ℕ) (R : Type*) [CommRing R]
    (q : R) (h_unit : IsUnit q) where
  /-- The underlying carrier type. -/
  carrier : Type
  /-- Algebra structure on the carrier. -/
  ring : Ring carrier
  /-- Star (bar involution) structure. -/
  star_ring : StarRing carrier
  /-- The braid generators `σ_i` for `i ∈ Fin (n - 1)`. Defined
      only when `n ≥ 1`; trivial otherwise. -/
  sigma : Fin (n - 1) → carrier
  /-- Markov trace as an `R`-linear map `carrier → R`.  Linearity,
      Markov-trace cyclicity, and the stabilisation property are
      placed as separate axioms below. -/
  markov_trace : carrier → R

namespace IwahoriHeckeAlgebra

variable {n : ℕ} {R : Type*} [CommRing R] {q : R} {h_unit : IsUnit q}

/-- `H.carrier` is nonempty: it carries a `Ring` (the `ring` field), hence
    has `0`.  Registered so `opaque`/placeholder constants valued in
    `H.carrier` (`jucysMurphy`, `centralIdempotent`) elaborate (an `opaque`
    constant of type `T` requires `Nonempty T`). -/
instance instNonemptyCarrier (H : IwahoriHeckeAlgebra n R q h_unit) :
    Nonempty H.carrier :=
  letI : Ring H.carrier := H.ring
  ⟨0⟩

/-! ## Hecke relations (axioms)

Note: These relation classes assume an `Algebra R H.carrier`
instance providing the scalar action `R → H.carrier`. The inverse
`q⁻¹` is taken via the substrate unit witness `h_unit : IsUnit q`
— i.e. `↑(h_unit.unit)⁻¹ : R` — so the whole API stays over a generic
`[CommRing R]` (per AGENTS.md §7c base-ring convention); no `[Field R]`
specialisation is needed, which also removes the `CommRing`/`Field`
instance diamond on `R`.

Per Copilot PR #634 review: the previous formulation used
`Ring.inverse q` (incorrect — that's the standard `Ring` partial
inverse, not the Hecke-algebra-natural inverse via `IsUnit`) and
`(q : R) • (1 : H.carrier)` without an `SMul R H.carrier` instance.
This rewrite uses the `IsUnit`-natural inverse and an algebra-style
embedding `R → H.carrier` for the scalar action. -/

/-- Algebra hom from `R` to the Hecke-algebra carrier — provides
    the scalar embedding required to write `(q : R) ↪ H.carrier`. -/
class HeckeRingHom (H : IwahoriHeckeAlgebra n R q h_unit) where
  scalarOf : R → H.carrier
  scalarOf_one :
    letI : Ring H.carrier := H.ring
    scalarOf 1 = (1 : H.carrier)

/-- The quadratic Hecke relation: `(σ_i - q)(σ_i + q⁻¹) = 0`, with `q⁻¹`
    the `IsUnit`-natural inverse `↑(h_unit.unit)⁻¹`. -/
class HeckeQuadratic
    (H : IwahoriHeckeAlgebra n R q h_unit) [HeckeRingHom H] : Prop where
  quadratic :
    ∀ i : Fin (n - 1),
      letI : Ring H.carrier := H.ring
      (H.sigma i - HeckeRingHom.scalarOf (R := R) q) *
        (H.sigma i + HeckeRingHom.scalarOf (R := R) (((h_unit.unit)⁻¹ : Rˣ) : R)) = 0

/-- The braid relation: `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`. -/
class HeckeBraid (H : IwahoriHeckeAlgebra n R q h_unit) : Prop where
  braid :
    ∀ i : Fin (n - 2),
      letI : Ring H.carrier := H.ring
      H.sigma ⟨i.val, by omega⟩ * H.sigma ⟨i.val + 1, by omega⟩ *
          H.sigma ⟨i.val, by omega⟩
        = H.sigma ⟨i.val + 1, by omega⟩ * H.sigma ⟨i.val, by omega⟩ *
          H.sigma ⟨i.val + 1, by omega⟩

/-- Far commutativity: `σ_i σ_j = σ_j σ_i` for `|i - j| ≥ 2`. -/
class HeckeFarCommute (H : IwahoriHeckeAlgebra n R q h_unit) : Prop where
  far_commute :
    ∀ i j : Fin (n - 1), Nat.dist i.val j.val ≥ 2 →
      letI : Ring H.carrier := H.ring
      H.sigma i * H.sigma j = H.sigma j * H.sigma i

/-! ## Bar involution -/

/-- The bar involution `* : σ_i ↦ σ_i⁻¹` is the standard antipode
    structure on `H_n(q)`. -/
class HeckeBar (H : IwahoriHeckeAlgebra n R q h_unit) : Prop where
  bar_sigma :
    ∀ i : Fin (n - 1),
      letI : Ring H.carrier := H.ring
      letI : StarRing H.carrier := H.star_ring
      star (H.sigma i) * H.sigma i = 1
  bar_q :
    letI : Ring R := inferInstance
    -- bar lifts q ↦ q⁻¹ on the coefficient ring (placeholder;
    -- requires R to carry a star structure).
    True

/-! ## Markov trace axioms -/

/-- Markov trace cyclicity: `tr_M(a · b) = tr_M(b · a)`. -/
class MarkovTraceCyclic (H : IwahoriHeckeAlgebra n R q h_unit) : Prop where
  cyclic :
    ∀ a b : H.carrier,
      letI : Ring H.carrier := H.ring
      H.markov_trace (a * b) = H.markov_trace (b * a)

/-- **Tower inclusion** `H_n ↪ H_{n+1}`: the unital ring hom that sends each
    braid generator `σ_i` of `H_n` to the same-indexed generator of `H_{n+1}`,
    realising `H_n` as the subalgebra of `H_{n+1}` on the first `n-1` strands.
    The Markov stabilisation move is stated against this map. -/
class HeckeInclusion
    (H : IwahoriHeckeAlgebra n R q h_unit)
    (H_succ : IwahoriHeckeAlgebra (n + 1) R q h_unit) where
  /-- The underlying inclusion of carriers. -/
  incl : H.carrier → H_succ.carrier
  /-- The inclusion is unital. -/
  map_one :
    letI : Ring H.carrier := H.ring
    letI : Ring H_succ.carrier := H_succ.ring
    incl 1 = 1
  /-- The inclusion is multiplicative (a ring hom). -/
  map_mul :
    letI : Ring H.carrier := H.ring
    letI : Ring H_succ.carrier := H_succ.ring
    ∀ a b, incl (a * b) = incl a * incl b
  /-- The inclusion preserves generators: `σ_i ↦ σ_i`. -/
  map_sigma :
    ∀ i : Fin (n - 1), incl (H.sigma i) = H_succ.sigma ⟨i.val, by omega⟩

/-- Markov trace stabilisation: with the tower inclusion `incl : H_n ↪ H_{n+1}`
    (`HeckeInclusion`) and the new top generator `σ_n` of `H_{n+1}` (index `n-1`
    of its `Fin n` generators), the Markov trace satisfies

    `tr_{M, n+1}(incl a · σ_n) = z · tr_{M, n}(a)`

    for the Markov parameter `z : R` (concretely `z = 1 / (q^{1/2} + q^{-1/2})`,
    carried here as an abstract `R`-parameter since `q^{1/2}` need not lie in a
    generic `R`).  Together with `MarkovTraceCyclic` this is the defining pair of
    Markov moves characterising `tr_M` (Jones 1987 §3).  `hn : 0 < n` makes the
    `σ_n` index `⟨n-1, _⟩ : Fin n` well-formed (stabilisation adds `σ_n` to
    `H_n`, which requires `n ≥ 1`). -/
class MarkovTraceStabilisation
    (H : IwahoriHeckeAlgebra n R q h_unit)
    (H_succ : IwahoriHeckeAlgebra (n + 1) R q h_unit)
    [HeckeInclusion H H_succ] (z : R) (hn : 0 < n) : Prop where
  stabilisation :
    ∀ a : H.carrier,
      letI : Ring H_succ.carrier := H_succ.ring
      H_succ.markov_trace (HeckeInclusion.incl a * H_succ.sigma ⟨n - 1, by omega⟩)
        = z * H.markov_trace a
  -- Ref: [jones1987] Jones, Hecke algebra representations of braid groups
  -- and link polynomials — §3 uniqueness of Markov trace on H_∞(q).

/-- **Consumer (the two Markov moves compose).**  Cyclicity of `tr_{M, n+1}`
    lets the stabilisation move be read in either order: the Markov trace of the
    new generator times an included element equals `z · tr_{M, n}` regardless of
    side.  A genuine derivation from the two axioms — `MarkovTraceStabilisation`
    is not decorative. -/
theorem markovTrace_stab_comm
    {H : IwahoriHeckeAlgebra n R q h_unit}
    {H_succ : IwahoriHeckeAlgebra (n + 1) R q h_unit}
    [HeckeInclusion H H_succ] {z : R} {hn : 0 < n}
    [MarkovTraceCyclic H_succ]
    [MarkovTraceStabilisation H H_succ z hn]
    (a : H.carrier) :
    letI : Ring H_succ.carrier := H_succ.ring
    H_succ.markov_trace (H_succ.sigma ⟨n - 1, by omega⟩ * HeckeInclusion.incl a)
      = z * H.markov_trace a := by
  letI : Ring H_succ.carrier := H_succ.ring
  rw [MarkovTraceCyclic.cyclic (H_succ.sigma ⟨n - 1, by omega⟩) (HeckeInclusion.incl a)]
  exact MarkovTraceStabilisation.stabilisation a

/-! ## Wedderburn decomposition (axiomatic, generic q) -/

/-- The "generic" condition on `q`: `q^{2k} ≠ 1` for `k ∈ {2, …, n}`.
    This is the precise locus on which `H_n(q)` is semisimple
    (`prop:hecke-baer-star-generic` failure-locus characterisation). -/
def IsGeneric (n : ℕ) (q : R) : Prop :=
  ∀ k : ℕ, 2 ≤ k → k ≤ n → q ^ (2 * k) ≠ 1

/-- **Wedderburn decomposition at generic q** (named conditional conjecture,
    §3b).  When `q` is generic, `H_n(q)` is finite-dimensional semisimple over
    `R` and decomposes as a direct sum of matrix algebras indexed by the
    partitions `λ ⊢ n` (here ranged over by the supplied list `parts`).

    Honest disposition: the decomposition is *named* as a `Prop` over the
    opaque carrier — it asserts the existence of a complete family of pairwise
    orthogonal central idempotents `{e_λ}` that sum to `1` (the Wedderburn unit
    resolution).  This is the structural content of semisimplicity; the proof
    needs Mathlib's matrix-algebra / seminormal-form infrastructure and is the
    open part (`prop:wedderburn-weight-canonical`, `prop:hoefsmit-seminormal-form`).
    Replaces the previous `: True := trivial` (vacuous) projection. -/
-- Ref: [kassel1995] §V.5 — Iwahori–Hecke algebra structure theorem at generic q.
-- Ref: [leitner2026] §prop:wedderburn-weight-canonical
-- Ref: [leitner2026] §prop:hoefsmit-seminormal-form
def wedderburn_decomposition_generic
    (H : IwahoriHeckeAlgebra n R q h_unit)
    (_h_gen : IsGeneric n q) (parts : List (List ℕ)) : Prop :=
  letI : Ring H.carrier := H.ring
  ∃ e : List ℕ → H.carrier,
    -- each block is idempotent
    (∀ lam ∈ parts, e lam * e lam = e lam) ∧
    -- blocks are pairwise orthogonal
    (∀ lam ∈ parts, ∀ mu ∈ parts, lam ≠ mu → e lam * e mu = 0) ∧
    -- blocks are central
    (∀ lam ∈ parts, ∀ x : H.carrier, e lam * x = x * e lam) ∧
    -- the idempotents resolve the unit (complete decomposition)
    (parts.map e).sum = 1

/-! ## Central primitive idempotents and JM elements -/

/-! ### 🛑 `jucysMurphy` and `centralIdempotent` must stay `opaque`

Both were `noncomputable def … := Classical.ofNonempty` with their index
argument named `_k` / `_lam`, i.e. **discarded**.  A `def` that discards its
index is *definitionally constant* in it, so `centralIdempotent H [1]` and
`centralIdempotent H [2]` were the same term — and combined with
`centralIdempotent_orthogonal_axiom` that PROVES every central idempotent is
zero:

    e * e = e            (λ = μ)
    e * e = 0            (λ ≠ μ, same term)
    ⟹ e = 0

Machine-checked before the fix: the derivation compiled, depending on exactly
`[propext, Classical.choice, centralIdempotent_orthogonal_axiom]`.  With every
`e_λ = 0` the other two axioms became trivially true (`0` commutes;
`star 0 = 0`), so the whole idempotent API asserted nothing.

It was **not** an inconsistency: `wedderburn_decomposition_generic` quantifies
existentially over a *fresh* `e` and never plugs in `centralIdempotent`, so no
`0 = 1` is derivable.  And nothing outside this file consumed it —
`ExplicitCentralIdempotent.lean` defines its own, separate `centralIdempotent`.

`opaque` removes the collapse: after the change the derivation fails with
*"`H.centralIdempotent a` is not definitionally equal to `H.centralIdempotent b`"*.
**Do not revert either declaration to `def`** without re-checking that.
Bean `qou-i6cn`. -/

/-- The **Jucys–Murphy element** `J_k` of `H_n(q)`. Definition uses
    the formula `J_k = q^{1-k} Σ_{i < k} σ_{i, k}` from
    `prop:jucys-murphy-central-elements-qou`.  Opaque, not a placeholder
    `def` — see the note above. -/
noncomputable opaque jucysMurphy
    (H : IwahoriHeckeAlgebra n R q h_unit) (k : Fin n) : H.carrier

/-- The **central primitive idempotent** `e_λ` for partition
    `λ ⊢ n`. Constructed via Lagrange interpolation in JM elements
    per `prop:explicit-central-idempotent`.  Opaque, not a placeholder
    `def` — see the note above. -/
noncomputable opaque centralIdempotent
    (H : IwahoriHeckeAlgebra n R q h_unit) (lam : List ℕ) : H.carrier

/-- **External axiom (Murphy 1981; Dipper–James 1986):**

    Central idempotents are central via the Lagrange-interpolation
    construction in commuting JM elements.  Recorded as an axiom
    (§3b-cond pattern) since concrete proof requires constructing
    JM elements + interpolation polynomial, both of which depend on
    a full IwahoriHeckeAlgebra implementation. -/
-- Ref: [murphy1981] Murphy, "A new construction of Young's seminormal representation of the symmetric groups," J. Algebra 69 (1981)
-- Ref: [dipper-james1986] Hecke-algebra extension.
axiom centralIdempotent_central_axiom :
    ∀ {n : ℕ} {R : Type*} [CommRing R] {q : R} {h_unit : IsUnit q}
      (H : IwahoriHeckeAlgebra n R q h_unit) (lam : List ℕ)
      (x : H.carrier),
        letI : Ring H.carrier := H.ring
        centralIdempotent H lam * x = x * centralIdempotent H lam

/-- Central idempotents are central: `e_λ · x = x · e_λ` for all
    `x ∈ H_n(q)`. -/
theorem central_idempotent_central
    (H : IwahoriHeckeAlgebra n R q h_unit) (lam : List ℕ)
    (x : H.carrier) :
    letI : Ring H.carrier := H.ring
    centralIdempotent H lam * x = x * centralIdempotent H lam :=
  centralIdempotent_central_axiom H lam x

/-- **External axiom**: orthogonality of central idempotents follows
    from Lagrange interpolation in commuting variables (the JM
    elements pairwise commute by [murphy1981]). -/
-- Ref: [murphy1981] Murphy, "A new construction of Young's seminormal representation of the symmetric groups," J. Algebra 69 (1981)
axiom centralIdempotent_orthogonal_axiom :
    ∀ {n : ℕ} {R : Type*} [CommRing R] {q : R} {h_unit : IsUnit q}
      (H : IwahoriHeckeAlgebra n R q h_unit) (lam mu : List ℕ),
        letI : Ring H.carrier := H.ring
        centralIdempotent H lam * centralIdempotent H mu =
          if lam = mu then centralIdempotent H lam else 0

/-- Central idempotents are orthogonal idempotents:
    `e_λ · e_μ = δ_{λμ} · e_λ`. -/
theorem central_idempotent_orthogonal
    (H : IwahoriHeckeAlgebra n R q h_unit) (lam mu : List ℕ) :
    letI : Ring H.carrier := H.ring
    centralIdempotent H lam * centralIdempotent H mu =
      if lam = mu then centralIdempotent H lam else 0 :=
  centralIdempotent_orthogonal_axiom H lam mu

/-- Transpose of a partition (Young-diagram conjugate).  For each
    column index `j` (0-indexed up to the row length of the first
    row), the transposed partition's `j`-th entry is the number of
    original rows with at least `j + 1` boxes.  Examples:

      `transpose [3, 1] = [2, 1, 1]`  (Young diagram with 3 + 1 = 4 boxes)
      `transpose [2, 2] = [2, 2]`     (self-conjugate)
      `transpose [4]    = [1, 1, 1, 1]`

    Per Gemini PR #634 review: replaces the previous incorrect
    `List.reverse` placeholder.  Reversal does NOT yield the
    transpose (e.g. `[3, 1].reverse = [1, 3]` which is not even a
    valid partition; the correct transpose is `[2, 1, 1]`). -/
def partitionTranspose : List ℕ → List ℕ
  | [] => []
  | h :: t =>
    (List.range h).map fun j =>
      ((h :: t).filter (· > j)).length

/-- **External axiom** (manuscript §prop:explicit-central-idempotent
    "Cross-checks" §3-4): the bar involution `q ↦ q⁻¹` acts on
    central idempotents by partition transpose. -/
-- Ref: [murphy1981] Murphy, "A new construction of Young's seminormal representation of the symmetric groups," J. Algebra 69 (1981)
axiom bar_centralIdempotent_transpose_axiom :
    ∀ {n : ℕ} {R : Type*} [CommRing R] {q : R} {h_unit : IsUnit q}
      (H : IwahoriHeckeAlgebra n R q h_unit) [HeckeBar H]
      (lam : List ℕ),
        letI : Ring H.carrier := H.ring
        letI : StarRing H.carrier := H.star_ring
        star (centralIdempotent H lam) =
          centralIdempotent H (partitionTranspose lam)

/-- Bar involution acts on central idempotents by partition
    transpose: `star (e_λ) = e_{λ'}`. -/
theorem bar_central_idempotent_transpose
    (H : IwahoriHeckeAlgebra n R q h_unit) [HeckeBar H]
    (lam : List ℕ) :
    letI : Ring H.carrier := H.ring
    letI : StarRing H.carrier := H.star_ring
    star (centralIdempotent H lam) =
      centralIdempotent H (partitionTranspose lam) :=
  bar_centralIdempotent_transpose_axiom H lam

/-! ## Failure locus characterisation -/

/-- The **exact failure locus** of generic-q Wedderburn / Baer-*:
    `{q : ∃ k ∈ [2, n], q^{2k} = 1}`. At each such `q`, the
    quantum integer `[k]_q := (q^k - q^{-k}) / (q - q^{-1})`
    vanishes for some `k ≤ n`, the Hoefsmit projector becomes
    singular, and the Jacobson radical is non-trivial.

    Co-located with the Volume Conjecture asymptotic regime
    (`rem:vc-as-depth-2-instance`). -/
def failureLocus (n : ℕ) (R : Type*) [CommRing R] : Set R :=
  { q : R | ∃ k : ℕ, 2 ≤ k ∧ k ≤ n ∧ q ^ (2 * k) = 1 }

/-- A `q` outside the failure locus is generic. -/
theorem not_in_failure_locus_iff_generic
    (q : R) :
    q ∉ failureLocus n R ↔ IsGeneric n q := by
  -- Direct definitional unfolding: both sides reduce to the same
  -- `∀ k, 2 ≤ k → k ≤ n → q ^ (2 * k) ≠ 1` after pushing negation
  -- through the set-membership existential (HPow over the single
  -- `[CommRing R]` instance — no Field/CommRing diamond).
  unfold failureLocus IsGeneric
  simp only [Set.mem_setOf_eq, not_exists, not_and]

/-! ## Summary: API surface ready for downstream blocks -/

/-! This file provides a Mathlib-style API for `H_n(q)`:

    - `IwahoriHeckeAlgebra n R q h_unit` — the abstract structure
    - `HeckeQuadratic`, `HeckeBraid`, `HeckeFarCommute`, `HeckeBar`,
      `MarkovTraceCyclic`, `MarkovTraceStabilisation` — axiom classes
    - `wedderburn_decomposition_generic` — Wedderburn theorem
      (axiomatic)
    - `jucysMurphy`, `centralIdempotent` — JM elements + central
      idempotents (opaque)
    - `central_idempotent_central`, `central_idempotent_orthogonal`,
      `bar_central_idempotent_transpose` — structural theorems
    - `failureLocus`, `IsGeneric`, `not_in_failure_locus_iff_generic`
      — exact failure-locus characterisation

    Downstream content blocks (`hecke-baer-star-generic.lean`,
    `explicit-central-idempotent.lean`, etc.) cite this API.

    Migration path to Mathlib: when Mathlib formalises
    `IwahoriHeckeAlgebra`, replace the opaque `IwahoriHeckeAlgebra`
    structure here with a re-export of the Mathlib version, and
    fill in the `sorry`-proofs using Mathlib's Wedderburn /
    seminormal-form / Markov-trace infrastructure. The QOU
    content blocks remain unchanged.
-/

end IwahoriHeckeAlgebra
end QOU.BraidKnot.IwahoriHeckeAPI
