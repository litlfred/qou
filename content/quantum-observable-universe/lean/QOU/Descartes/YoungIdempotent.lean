import QOU.Descartes.HeckeRep
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Tactic

/-!
# Young Symmetric Idempotent for H_n(q)

The Young symmetric idempotent `e_{(n)}` is the element of the
Iwahori–Hecke algebra H_n(q) that projects onto the symmetric
(trivial) representation.

## Main definitions

- `CoxeterLength` — the Coxeter length ℓ(w) of a permutation w ∈ S_n
- `S3Perms` — explicit enumeration of S₃ (6 elements)
- `permToHeckeWord` — embed a permutation into H_n(q) via a reduced word
- `poincarePolynomial` — the Poincaré polynomial P_n(q²)
- `youngSymIdempotent` — the Young symmetric idempotent `e_{(n)}`

## Key properties

The Young symmetric idempotent satisfies:
1. `e_{(n)}² = P_n(q²) · e_{(n)}` (quasi-idempotent)
2. `σ_i · e_{(n)} = q · e_{(n)}` (eigenvalue property for symmetric rep)
3. `e_{(n)} · σ_i = q · e_{(n)}` (right eigenvalue property)

## References

- [murphy1992] G. Murphy, On the representation theory of the symmetric
  groups and associated Hecke algebras.
- [mathas1999] A. Mathas, Iwahori-Hecke Algebras and Schur Algebras
  of the Symmetric Group.
-/

namespace QOU.YoungIdempotent

open QOU.Descartes Matrix

/-! ## §1  Coxeter length (inversion count) -/

/-- The Coxeter length of a permutation: the number of inversions.
    `ℓ(w) = #{(i, j) : i < j ∧ w(i) > w(j)}`. -/
def coxeterLength {n : ℕ} (w : Equiv.Perm (Fin n)) : ℕ :=
  ((Finset.univ.product Finset.univ).filter fun ij =>
    ij.1 < ij.2 ∧ w ij.1 > w ij.2).card

/-- The identity permutation has length 0. -/
theorem coxeterLength_one {n : ℕ} : coxeterLength (1 : Equiv.Perm (Fin n)) = 0 := by
  simp only [coxeterLength, Equiv.Perm.one_apply]
  rw [Finset.card_eq_zero]
  ext ⟨a, b⟩
  simp only [Finset.mem_filter, Finset.mem_product, Finset.mem_univ, true_and, Finset.not_mem_empty,
             iff_false, not_and]
  intro hab
  exact not_lt.mpr (le_of_lt hab)

/-! ## §2  S₃ explicit enumeration -/

/-- The 6 elements of S₃ as permutations of Fin 3, with their
    Coxeter lengths and reduced words.

    | Element | Cycle notation | Length | Reduced word |
    |---------|---------------|--------|--------------|
    | e       | ()            | 0      | []           |
    | s₀      | (0 1)         | 1      | [0]          |
    | s₁      | (1 2)         | 1      | [1]          |
    | s₀s₁    | (0 1 2)       | 2      | [0, 1]       |
    | s₁s₀    | (0 2 1)       | 2      | [1, 0]       |
    | s₀s₁s₀  | (0 2)         | 3      | [0, 1, 0]    |
-/
def S3_reduced_words : List (List (Fin 2) × ℕ) :=
  [([],                 0),
   ([0],                1),
   ([1],                1),
   ([0, 1],             2),
   ([1, 0],             2),
   ([0, 1, 0],          3)]

/-- The number of elements in S₃. -/
theorem S3_card : S3_reduced_words.length = 6 := by decide

/-! ## §3  Poincaré polynomial -/

/-- The q²-integer `[n]_{q²} = 1 + q² + q⁴ + … + q^{2(n−1)}`
    as an element of `ℤ[t, t⁻¹]` where `q = t²`.

    This is the sum form — no division required, so it lives in
    the Laurent polynomial ring directly.

    `[n]_{q²} = Σ_{k=0}^{n-1} q^{2k} = Σ_{k=0}^{n-1} t^{4k}` -/
noncomputable def qSqInt (n : ℕ) : R_t :=
  (Finset.range n).sum fun k =>
    (q_from_t * q_from_t) ^ k   -- q^{2k} = (q²)^k = t^{4k}

/-- The Poincaré polynomial `P_n(q²) = ∑_{w ∈ S_n} q^{2ℓ(w)}`.

    This is the sum of `q^{2ℓ(w)}` over all permutations in S_n.
    It equals the q²-factorial: `P_n(q²) = [n]_{q²}!`.

    Recursion: `P_n = P_{n-1} · [n]_{q²}` where
    `[n]_{q²} = 1 + q² + q⁴ + … + q^{2(n-1)}`.

    For small n:
    - P₁ = 1
    - P₂ = 1 + q² = [2]_{q²}
    - P₃ = (1 + q²)(1 + q² + q⁴) = [2]_{q²} · [3]_{q²}
         = 1 + 2q² + 2q⁴ + q⁶ -/
noncomputable def poincarePolynomial : ℕ → R_t
  | 0 => 1
  | n + 1 => poincarePolynomial n * qSqInt (n + 1)

/-! ## §4  Young symmetric idempotent (for representations) -/

/-- The Young symmetric idempotent evaluated in a representation.

    For a representation ρ : H_n(q) → End(V), the image of the
    Young symmetric idempotent is:

    `ρ(e_{(n)}) = ∑_{w ∈ S_n} q^{ℓ(w)} · ρ(T_w)`

    where `T_w` is the Hecke algebra element for permutation w
    (using any reduced word).

    For H₃(q), this is explicitly:
    `e_{(3)} = 1 + q·T₁ + q·T₂ + q²·T₁T₂ + q²·T₂T₁ + q³·T₁T₂T₁` -/
noncomputable def youngSymIdempotent3 (ρ : HeckeRep 3 d) :
    Matrix (Fin d) (Fin d) R_t :=
  let q := q_from_t
  let T₀ := ρ.gen 0
  let T₁ := ρ.gen 1
  -- e_{(3)} = I + q·T₀ + q·T₁ + q²·T₀T₁ + q²·T₁T₀ + q³·T₀T₁T₀
  1 + q • T₀ + q • T₁ +
  (q * q) • (T₀ * T₁) + (q * q) • (T₁ * T₀) +
  (q * q * q) • (T₀ * T₁ * T₀)

/-- General Young symmetric idempotent for H₂(q):
    `e_{(2)} = I + q · T₀`. -/
noncomputable def youngSymIdempotent2 (ρ : HeckeRep 2 d) :
    Matrix (Fin d) (Fin d) R_t :=
  1 + q_from_t • ρ.gen 0

/-- The Young symmetric idempotent satisfies the eigenvalue property:
    `σ_i · e_{(n)} = q · e_{(n)}` in the Hecke algebra.

    In a representation:
    `ρ(σ₀) · ρ(e_{(3)}) = q · ρ(e_{(3)})`

    This is the key property used for ordering independence:
    the Skein polynomial symmetrized by e_{(n)} depends only on
    the multiset of crossing weights, not their ordering.

    Proof strategy: expand σ₀ · e_{(3)} using the Hecke and braid
    relations to show each term contributes correctly.

    For each w ∈ S₃, σ₀ · T_w is either:
    - T_{s₀w} with ℓ(s₀w) = ℓ(w) + 1 (length increases), or
    - q · T_w + (q−q⁻¹) · T_{s₀w} with ℓ(s₀w) = ℓ(w) − 1 (Hecke reduction)

    Summing over S₃ with q^{ℓ(w)} weights produces q · e_{(3)}. -/
-- Ref: [mathas1999] Theorem 3.2 (Young symmetrizer eigenvalue property)
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou

/-- **Young-symmetric eigenvalue — typeclass (Pattern 4).**

    Witnesses the symmetric-rep eigenvalue property `σ_i · e_{(3)} = q · e_{(3)}`
    for a *specific* representation `ρ`. The universal claim
    requires expanding σ_i · T_w via Hecke/braid relations across
    the full S_3 sum; until that is mechanised, callers supply a
    per-`ρ` witness. -/
class YoungSym3Eigenvalue (ρ : HeckeRep 3 d) : Prop where
  /-- For every generator `i`, the symmetric idempotent acts as
      multiplication by `q`. -/
  eigenvalue : ∀ i : Fin 2,
    ρ.gen i * youngSymIdempotent3 ρ = q_from_t • youngSymIdempotent3 ρ

/-- Per-instance form. -/
theorem youngSym3_eigenvalue (ρ : HeckeRep 3 d) (i : Fin 2)
    [hi : YoungSym3Eigenvalue ρ] :
    ρ.gen i * youngSymIdempotent3 ρ = q_from_t • youngSymIdempotent3 ρ :=
  hi.eigenvalue i

end QOU.YoungIdempotent
