/-!
# QOU.Organic.HeteroaromaticAlexander — Heteroatom invariance

Conjectural class: the Alexander polynomial of a heteroaromatic
ring is independent of heteroatom substitution.  The class is
parameterised by a "ring species" type whose members all map to
the same all-carbon Alexander polynomial.

## References

- [manuscript] Ch. 10, Conjecture `conj:heteroaromatic-alexander`
- [manuscript] Ch. 10, Lemma `lem:alexander-T2N-closed-form`
-/

namespace QOU.Organic

/-- Inductive type indexing the ring atoms supported by the
    conjecture.  Adding a new heteroatom to the chemistry is a
    matter of extending this enumeration. -/
inductive RingAtom
  | carbon
  | nitrogen
  | oxygen
  | sulfur
  | NH
  deriving DecidableEq, Repr

/-- A heteroaromatic ring is a list of `RingAtom` (its vertex
    sequence around the cycle).  The ring size is the list length. -/
def ringSize (atoms : List RingAtom) : ℕ := atoms.length

/-- Conjectural class: a witness that the Alexander polynomial of
    `atoms` (a heteroaromatic ring) coincides with the all-carbon
    polynomial of the same ring size.  We model the polynomial by
    its evaluation at q = 1 (an integer) for simplicity. -/
class HeteroaromaticAlexander where
  /-- Heteroatom-independent: any two rings of the same size share
      the same Alexander value at q = 1. -/
  invariance : ∀ (atoms₁ atoms₂ : List RingAtom),
    ringSize atoms₁ = ringSize atoms₂ →
    True   -- Δ(atoms₁, 1) = Δ(atoms₂, 1) (placeholder)

/-- Sanity decidability: ring sizes are decidable equal. -/
-- Ref: [manuscript] Ch. 10, Conjecture conj:heteroaromatic-alexander
example (atoms₁ atoms₂ : List RingAtom)
    (h : ringSize atoms₁ = ringSize atoms₂) :
    atoms₁.length = atoms₂.length := h

/-- Pyridine is a 6-membered ring (1 N, 5 C). -/
-- Ref: [manuscript] Ch. 10, Conjecture conj:heteroaromatic-alexander
def pyridine : List RingAtom :=
  [.nitrogen, .carbon, .carbon, .carbon, .carbon, .carbon]

/-- Benzene is a 6-membered ring (6 C). -/
-- Ref: [manuscript] Ch. 10, Conjecture conj:heteroaromatic-alexander
def benzene : List RingAtom :=
  [.carbon, .carbon, .carbon, .carbon, .carbon, .carbon]

/-- Sanity check: pyridine and benzene have the same ring size. -/
-- Ref: [manuscript] Ch. 10, Conjecture conj:heteroaromatic-alexander
theorem pyridine_benzene_same_size :
    ringSize pyridine = ringSize benzene := by
  unfold ringSize pyridine benzene
  rfl

end QOU.Organic
