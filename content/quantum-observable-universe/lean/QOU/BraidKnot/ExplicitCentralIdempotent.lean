import Mathlib.Algebra.Star.Basic
import Mathlib.RingTheory.Idempotents

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

    The four Murphy–Lagrange cross-checks (sum-to-identity,
    orthogonality, self-adjointness, bar-pairing) follow from Lagrange
    interpolation in the commuting Jucys–Murphy elements
    `J_1, …, J_n`.

    The field states the one of the four that downstream Lean actually
    consumes — idempotency of `e_λ` at every partition of every `n`.
    It is quantified over `lam` and `n`, so it is a claim about the
    whole Murphy–Lagrange construction and not about one partition. -/
class ExplicitCentralIdempotentConjecture {R : Type*} [CommRing R] (q : R) : Prop where
  /-- The explicit idempotency holds. -/
  idempotent : ∀ {n : ℕ} (lam : List ℕ) (_h : lam.sum = n),
    centralIdempotent lam q * centralIdempotent lam q = centralIdempotent lam q

end QOU.BraidKnot.ExplicitCentralIdempotent
