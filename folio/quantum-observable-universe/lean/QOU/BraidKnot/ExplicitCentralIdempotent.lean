import Mathlib.Algebra.Star.Basic
import Mathlib.RingTheory.Idempotents
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# Central primitive idempotents `e_λ` — carrier and open conjecture

The vocabulary shared by `prop:explicit-central-idempotent` and
`conj:explicit-central-idempotent`: the standard-Young-tableau type, the
q-content of a box, the idempotent element itself, and the **open**
conjecture asserting that the four Murphy–Lagrange cross-checks hold.

## Why this is a library module and not a content-block sibling

`ExplicitCentralIdempotentConjecture` is stated by one block (the
`conj:`) and *consumed* as an instance hypothesis by another (the
`prop:`). A content-block sibling `.lean` cannot import another
sibling, so keeping the class in a sibling would force the two blocks
to declare it **twice**, independently — the divergence shape recorded
in `docs/audits/2026-09-03-sibling-lean-compile-sweep.md` §"A cost of
this sweep", where two declarations sharing a name drift apart and the
`lean.ref` (which resolves sibling-first, by file) silently picks the
stale one. Declaring it once here is what makes both blocks able to
name the same object.

## §3b-tax status

`ExplicitCentralIdempotentConjecture` is a **primary** conjecture: its
signature binds no other conjecture class. Per §3b-tax an unproved
primary is a content-bearing class with **no instance**, and there is
deliberately none — supplying one would assert the conjecture rather
than prove it (§"Axiomatization is NOT a Proof").
-/

namespace QOU.BraidKnot.ExplicitCentralIdempotent

variable {R : Type*} [CommRing R]

/-- A standard Young tableau of shape `λ`: a filling of the Young
    diagram of `λ` with `1, ..., n` such that rows and columns
    increase. Placeholder for Mathlib's eventual SYT API. -/
opaque SYT (lam : List ℕ) : Type

/-- The q-content of a box at position `(i, j)` in a Young diagram:
    `c(i, j; q) = q^(2(j - i))`.

    This is the integer (signed) power, so for boxes below the main
    diagonal (`j < i`) the content is `q⁻²ᵏ` for some `k > 0`, i.e.
    `q ^ (n : ℤ)` must be total.

    §7c: that is supplied by carrying `q` as a **unit** `q : Rˣ` of a bare
    `CommRing R` — `Rˣ` is a group, so `zpow` is total there — rather than by
    strengthening the base ring to a `GroupWithZero`/`Field`. The generic
    Hecke ground ring `ℤ[q, q⁻¹]` is exactly this situation: `q` is a unit and
    the ring is not a field.

    Per Gemini PR #634 review: previous `(2 * (j - i)).toNat` was
    mathematically incorrect — it forced `q^0 = 1` for all boxes
    below the diagonal, which contradicts the standard q-content
    definition (Hoefsmit, prop:hoefsmit-seminormal-form). -/
def qContent {R : Type*} [CommRing R] (i j : ℤ) (q : Rˣ) : R :=
  ((q ^ (2 * (j - i)) : Rˣ) : R)

/-- Murphy–Lagrange formula for the central primitive idempotent
    `e_λ ∈ Z(H_n(q))`. Placeholder element-of-the-algebra constant.

    Per Gemini PR #634 review: previous `: Type` signature was a
    type-mismatch — `centralIdempotent` is an *element* of the
    algebra carrier, not a type. The full Lean formalisation
    binds it to `H.carrier` for an `IwahoriHeckeAlgebra` `H`; this
    placeholder fixes the signature to return a value in the
    underlying ring `R`, allowing element-level identities
    (orthogonality, self-adjointness, bar-pairing) to typecheck. -/
noncomputable opaque centralIdempotent {R : Type*} [CommRing R]
    (lam : List ℕ) (q : R) : R

/-- **CONJECTURE (OPEN)** — `conj:explicit-central-idempotent`.

    The Murphy–Lagrange element `e_λ` decomposes as a sum, over the standard
    Young tableaux of shape `λ`, of **pairwise-orthogonal idempotents** — the
    per-tableau Lagrange projectors

        π_T = ∏_k ∏_{□ ≠ T(k)} (J_k - c(□;q)) / (c(T(k);q) - c(□;q))

    onto the joint `(c(T(1);q), …, c(T(n);q))`-eigenspace of the commuting
    Jucys–Murphy elements.

    **This is the interpolation-theoretic INPUT, not the conclusion.** Earlier
    this class had a single field whose type was
    `centralIdempotent lam q * centralIdempotent lam q = centralIdempotent lam q`
    — the downstream theorem's conclusion verbatim — and that theorem
    discharged it by `exact hi.idempotent lam h`, a bare projection. AGENTS.md
    §3b-cond **item 5** forbids exactly that: a class must axiomatise the
    hypotheses and the theorem must *derive* its conclusion from them. Caught
    2026-09-04 by the `--item5` mode of
    `scripts/conditional-on-class-hypothesis-audit.ts`.

    The three fields below are what Lagrange interpolation in commuting
    variables actually supplies, and idempotency, orthogonality and
    sum-to-identity are all consequences of them rather than restatements.
    `explicit_central_idempotent_via_murphy` now composes them. -/
class ExplicitCentralIdempotentConjecture {R : Type*} [CommRing R] (q : R) where
  /-- The standard Young tableaux of shape `λ`, as an index type. -/
  Tab : List ℕ → Type
  /-- Finitely many of them, so the decomposition is a finite sum. -/
  [fintypeTab : ∀ lam, Fintype (Tab lam)]
  /-- The Lagrange projector attached to one tableau. -/
  proj : ∀ lam, Tab lam → R
  /-- Each projector is idempotent — Lagrange interpolation at a simple
      joint eigenvalue. -/
  proj_idem : ∀ lam (T : Tab lam), proj lam T * proj lam T = proj lam T
  /-- Distinct tableaux carry distinct joint eigenvalue tuples, so their
      projectors are orthogonal. -/
  proj_orth : ∀ lam (T T' : Tab lam), T ≠ T' → proj lam T * proj lam T' = 0
  /-- `e_λ` is the sum of the per-tableau projectors. -/
  centralIdempotent_eq_sum : ∀ lam,
    centralIdempotent lam q = ∑ T : Tab lam, proj lam T

attribute [instance] ExplicitCentralIdempotentConjecture.fintypeTab

/-- **Main-diagonal unity and transpose inversion of `qContent` (`qou-2150`).**
For any unit `q : Rˣ` in a commutative ring `R`, `qContent i i q = 1` on the main diagonal,
and `qContent i j q * qContent j i q = 1` under cell transposition `(i, j) ↔ (j, i)`. -/
theorem qContent_diag_and_transpose_mul_eq_one (i j : ℤ) (q : Rˣ) :
    qContent i i q = 1 ∧ qContent i j q * qContent j i q = 1 := by
  unfold qContent
  refine ⟨by simp, ?_⟩
  rw [← Units.val_mul, ← zpow_add]
  have hexp : 2 * (j - i) + 2 * (i - j) = 0 := by ring
  rw [hexp, zpow_zero, Units.val_one]

end QOU.BraidKnot.ExplicitCentralIdempotent
