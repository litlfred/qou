/-
# The block factorisation, both halves joined

`QOU.Knot.BodyOrderExpansion` supplies the abstract half: a generating function
over a product index set, with additive degree and multiplicative coefficients,
factorises (`gf_pi`, and `gf_pow` for identical factors).

`QOU.Knot.BlockLengthAdditive` supplies the concrete half: Coxeter length is
additive across an order-separated block split (`length_blockProd`, and
`length_blockProd_of_supportedIn` for the two-sided support condition a nucleon
block satisfies).

Neither alone says anything about the atomic braid. The abstract half needs a
degree function that is *already* a sum over blocks; the concrete half produces
exactly such a sum but says nothing about generating functions. This file is the
join, and it is short because both halves were done properly.

## What the join actually delivers

`gf_blocks` states: for a family of nucleon blocks, each supported on its own
strand interval, the grade generating function of the assembled `A`-nucleon
word -- graded by the Coxeter length of the *assembled* permutation, which is
what the Gröbner–Shirshov normal form of `H_{3A}` is filtered by -- equals the
product of the per-nucleon generating functions.

The degree function on the left is `ℓ(blockProd f A)`, not `Σᵢ ℓ(fᵢ)`. That
distinction is the whole content: the left-hand side is a statement about one
word in one algebra, the right-hand side is a product over `A` independent
objects, and only the parabolic length formula makes them the same number.

## What it does NOT deliver

It does not say that the normal forms of `H_{3A}` are *exhausted* by such
block products -- a general `w ∈ S_{3A}` is a block product times a minimal
coset representative, and the coset factor is precisely where inter-nucleon
bonds live. That factor is `gf_bonds`'s `∏ (X + C d)` in the measured
composition law `G_A(x) = [∏_bonds (x + d)] · G_1(x)^A`, and it is a separate
object. This file proves the `G_1(x)^A` factor is what it is claimed to be; it
does not prove the decomposition into the two factors.

## References

- [leitner2026] §mass-theory/bond-order-eq-jet-degree
-/
import QOU.Knot.BodyOrderExpansion
import QOU.Knot.BlockLengthAdditive

namespace QOU.Knot.BlockGeneratingFunction

open Polynomial
open QOU.Knot.GradedGeneratingFunction
open QOU.Knot.BodyOrderExpansion
open QOU.Knot.JetGradePromotion
open QOU.Knot.BlockLengthAdditive

variable {R : Type*} [CommSemiring R] {m : ℕ}

/-- Extend an `A`-indexed family of blocks to all of `ℕ` by the identity, so it
can be fed to `blockProd`. Blocks past `A` contribute nothing. -/
def ofFin {A : ℕ} (f : Fin A → Equiv.Perm (Fin m)) : ℕ → Equiv.Perm (Fin m) :=
  fun n => if h : n < A then f ⟨n, h⟩ else 1

theorem ofFin_lt {A : ℕ} (f : Fin A → Equiv.Perm (Fin m)) {n : ℕ} (h : n < A) :
    ofFin f n = f ⟨n, h⟩ := dif_pos h

theorem ofFin_ge {A : ℕ} (f : Fin A → Equiv.Perm (Fin m)) {n : ℕ} (h : ¬ n < A) :
    ofFin f n = 1 := dif_neg h

/-- **The Coxeter length of the assembled word is the sum of the blocks'
lengths.** This is `length_blockProd_of_supportedIn` transported to a `Fin A`
family: the extension by the identity is supported everywhere vacuously, so the
hypothesis is only a condition on the `A` real blocks. -/
theorem length_ofFin {b : ℕ → ℕ} (hb : Monotone b) {A : ℕ}
    (f : Fin A → Equiv.Perm (Fin m))
    (hf : ∀ i : Fin A, SupportedIn (b i) (b ((i : ℕ) + 1)) (f i)) :
    length (blockProd (ofFin f) A) = ∑ i : Fin A, length (f i) := by
  have hs : ∀ n, SupportedIn (b n) (b (n + 1)) (ofFin f n) := by
    intro n
    by_cases h : n < A
    · rw [ofFin_lt f h]; exact hf ⟨n, h⟩
    · rw [ofFin_ge f h]; exact supportedIn_one
  rw [length_blockProd_of_supportedIn hb hs A,
    ← Fin.sum_univ_eq_sum_range (fun n => length (ofFin f n)) A]
  exact Finset.sum_congr rfl fun i _ => by rw [ofFin_lt f i.isLt]

/-- **The block factorisation.** Grading by the Coxeter length of the assembled
`A`-nucleon word, the generating function is the product of the per-nucleon
generating functions.

The left-hand degree is `ℓ` of a single permutation in `S_m`; the right-hand
side is a product over `A` independent blocks. They agree because length is
additive across an order-separated split, which is the parabolic length formula
of `BlockLengthAdditive`. -/
theorem gf_blocks {b : ℕ → ℕ} (hb : Monotone b) {A : ℕ}
    (S : Fin A → Finset (Equiv.Perm (Fin m)))
    (hS : ∀ (i : Fin A), ∀ w ∈ S i, SupportedIn (b i) (b ((i : ℕ) + 1)) w)
    (c : Fin A → Equiv.Perm (Fin m) → R) :
    gf (Fintype.piFinset S) (fun f => ∏ i, c i (f i))
       (fun f => length (blockProd (ofFin f) A))
      = ∏ i, gf (S i) (c i) length := by
  rw [← gf_pi S c (fun _ => length)]
  refine gf_congr _ _ fun f hf => ?_
  exact length_ofFin hb f fun i => hS i (f i) (Fintype.mem_piFinset.mp hf i)

/-- The identical-block corollary: `A` copies of one block give `G_1(x)^A`,
now with the degree being the length of the assembled word rather than an
assumed sum. -/
theorem gf_blocks_pow {b : ℕ → ℕ} (hb : Monotone b) {A : ℕ}
    (S : Finset (Equiv.Perm (Fin m)))
    (hS : ∀ (i : Fin A), ∀ w ∈ S, SupportedIn (b i) (b ((i : ℕ) + 1)) w)
    (c : Equiv.Perm (Fin m) → R) :
    gf (Fintype.piFinset fun _ : Fin A => S) (fun f => ∏ i, c (f i))
       (fun f => length (blockProd (ofFin f) A))
      = (gf S c length) ^ A := by
  rw [gf_blocks hb (fun _ => S) hS (fun _ => c), Finset.prod_const, Finset.card_univ,
    Fintype.card_fin]

end QOU.Knot.BlockGeneratingFunction
