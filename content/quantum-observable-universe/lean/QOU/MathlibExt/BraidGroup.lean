import Mathlib.GroupTheory.PresentedGroup

set_option autoImplicit false

/-!
# QOU.MathlibExt.BraidGroup — Artin braid groups (a genuine Mathlib gap)

**Mathlib has no braid groups.** Verified by search: no file matching `*braid*`
anywhere in `Mathlib/`, and `Mathlib/GroupTheory/` carries `Coxeter` but not the
braid group itself. This module supplies the minimum the MFW programme
(`QOU/Knot/MortonFranksWilliams.lean`, bean `qou-dr8m`) actually needs, built on
Mathlib's `PresentedGroup`.

## Indexing convention

`BraidGroup n` is the braid group on **`n + 1` strands**, with `n` Artin
generators indexed by `Fin n`. The offset is deliberate: the alternative
(`Fin (n-1)` for `n` strands) uses truncated ℕ-subtraction, which poisons every
downstream index proof. `strandCount n = n + 1` is provided so callers never
have to remember which convention is in force.

## Artin presentation

    σᵢσⱼ = σⱼσᵢ                    for |i − j| ≥ 2      (far commutation)
    σᵢσᵢ₊₁σᵢ = σᵢ₊₁σᵢσᵢ₊₁                                (braid relation)

## What is proved here

`exponentSum` — the **writhe** homomorphism `BraidGroup n →* Multiplicative ℤ`
sending every generator to `1`. This is the piece MFW needs: the `e` in

    e − n + 1 ≤ mindeg_v P  ≤  maxdeg_v P ≤ e + n − 1

and it is a *theorem*, not a definition-by-fiat: it descends to the quotient
precisely because **every Artin relator has total exponent sum zero** — the far
commutator trivially (it is a commutator, and the target is abelian), and the
braid relator because both sides are words of length three. Both obligations are
discharged below, so `exponentSum` is well-defined on the presented group rather
than only on the free group.

That well-definedness is the whole content: the writhe of a braid *word* is
obvious, the writhe of a braid *group element* is not, and MFW is a statement
about the latter.
-/

namespace QOU.MathlibExt.Braid

open FreeGroup

/-- Number of strands: `BraidGroup n` acts on `n + 1` strands. -/
def strandCount (n : ℕ) : ℕ := n + 1

/-- The Artin relators for `n` generators, as elements of the free group.
Far commutation `σᵢσⱼσᵢ⁻¹σⱼ⁻¹` for `i + 2 ≤ j`, and the braid relation
`σᵢσᵢ₊₁σᵢ(σᵢ₊₁σᵢσᵢ₊₁)⁻¹`. -/
def braidRelators (n : ℕ) : Set (FreeGroup (Fin n)) :=
  {r |
    (∃ i j : Fin n, (i : ℕ) + 2 ≤ (j : ℕ) ∧
        r = of i * of j * (of i)⁻¹ * (of j)⁻¹) ∨
    (∃ (i : Fin n) (h : (i : ℕ) + 1 < n),
        r = of i * of ⟨(i : ℕ) + 1, h⟩ * of i *
            (of ⟨(i : ℕ) + 1, h⟩ * of i * of ⟨(i : ℕ) + 1, h⟩)⁻¹)}

/-- The braid group on `n + 1` strands, as the Artin presentation. -/
def BraidGroup (n : ℕ) := PresentedGroup (braidRelators n)

instance (n : ℕ) : Group (BraidGroup n) := by
  unfold BraidGroup; infer_instance

/-- The `i`-th Artin generator `σᵢ`. -/
def σ {n : ℕ} (i : Fin n) : BraidGroup n := PresentedGroup.of i

/-- Every Artin relator has total exponent sum zero, so the constant map
`generator ↦ 1` kills the relators and descends to the quotient. This is the
well-definedness obligation for `exponentSum`. -/
theorem lift_const_relators (n : ℕ) :
    ∀ r ∈ braidRelators n,
      (FreeGroup.lift fun _ : Fin n => (Multiplicative.ofAdd (1 : ℤ))) r = 1 := by
  rintro r (⟨i, j, _, rfl⟩ | ⟨i, h, rfl⟩) <;>
    simp [FreeGroup.lift] <;> rfl

/-- **The writhe.** `exponentSum β` is the total exponent sum of any word
representing `β` — well defined on the group, not merely on words, by
`lift_const_relators`. This is the `e` of the Morton–Franks–Williams pair. -/
def exponentSum (n : ℕ) : BraidGroup n →* Multiplicative ℤ :=
  PresentedGroup.toGroup (lift_const_relators n)

@[simp] theorem exponentSum_σ {n : ℕ} (i : Fin n) :
    exponentSum n (σ i) = Multiplicative.ofAdd (1 : ℤ) :=
  PresentedGroup.toGroup.of _

end QOU.MathlibExt.Braid
