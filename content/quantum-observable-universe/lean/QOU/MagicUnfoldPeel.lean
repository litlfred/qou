/-
# Magic-unfold Markov peel

Formal statement + proof of `prop:magic-unfold-peel`:

    tr_M(A · σ^m · B)  =  z^m · tr_M(A) · tr_M(B)

when A and B far-commute and σ is the Markov-stab generator
between them.  This is the **abstract** Markov-peel identity; the
physical claim that the atom braid admits such a factorization is
a separate question (see `magic-unfold-peel.md` for the
computational falsification of the reordering hypothesis for the
standard `atom_braid_word_3A`).

The proof is an iterated application of the Markov axiom
    tr_M(x · σ_{top}) = z · tr_M(x)       for x in H_{n-1}
plus the Markov-trace factorization theorem for tensor products
of commuting sub-algebras.

Ref: [jones1985] https://doi.org/10.2307/1971403
Ref: [wenzl1988] https://doi.org/10.1007/BF01393746
Ref: [leitner2026] https://github.com/litlfred/qou
-/

import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.BigOperators.Basic

namespace QOU.MassEndomorphism

/-!
## Abstract Hecke / Markov structure

We model the minimal structure needed for the peel: a ring `H`
with a distinguished element `σ` and a linear functional `tr_M`
with the Markov property and factorization over a commuting
tensor split.
-/

/-- Abstract Markov trace on a (non-commutative) ring with a
distinguished Markov generator `σ` and parameter `z`.  Encodes
the two identities used in the proof:

  1. Markov axiom:
       ∀ x, tr_M (x * σ) = z * tr_M x
     (equivalently for σ⁻¹; here we take the positive case).
  2. Factorization over commuting subrings:
       ∀ a ∈ subring_A, b ∈ subring_B with [a, b] = 0,
       tr_M (a * b) = tr_M a * tr_M b.
-/
class MarkovTrace (H : Type*) [Ring H] where
  /-- The Markov-stab generator `σ` at the top of the current level. -/
  σ      : H
  /-- The Markov parameter `z`. -/
  z      : H
  /-- Trace functional. -/
  tr_M   : H →+ H
  /-- Markov axiom: peeling one σ gives a factor of z. -/
  markov : ∀ x : H, tr_M (x * σ) = z * tr_M x
  /-- Factorization for commuting products. -/
  factor : ∀ a b : H, a * b = b * a → tr_M (a * b) = tr_M a * tr_M b

/-- **Magic-unfold peel (abstract).**  For commuting elements `A`,
`B`, and the Markov-stab element `σ` that far-commutes with both,
the trace of `A · σ^m · B` factorises as `z^m · tr_M(A) · tr_M(B)`.

This is the abstract statement captured in
`prop:magic-unfold-peel`.  The proof is an induction on `m` using
the Markov axiom, combined with the factorization lemma applied to
the commuting pair `(A, B)`.

The physical claim — that the atom braid word admits this
factorization at shell closure — is SEPARATE and currently refuted
empirically for the standard `atom_braid_word_3A` (see the
companion `.md` for the computational negative result on T and
³He).  The abstract peel theorem stands on its own as the Hecke-
algebra identity that WOULD give the reduction if the atom word
were correctly structured.

Ref: [leitner2026] https://github.com/litlfred/qou
Ref: [jones1985] https://doi.org/10.2307/1971403
-/
theorem magic_unfold_peel
    {H : Type*} [Ring H] [MarkovTrace H]
    (A B : H) (m : ℕ)
    (hAB : A * B = B * A)
    (hAσ : A * MarkovTrace.σ = MarkovTrace.σ * A)
    (hBσ : B * MarkovTrace.σ = MarkovTrace.σ * B) :
    MarkovTrace.tr_M (A * MarkovTrace.σ ^ m * B)
      = MarkovTrace.z ^ m * MarkovTrace.tr_M A * MarkovTrace.tr_M B := by
  -- Step 1: commute σ^m past B (σ far-commutes with B)
  have hBσm : B * MarkovTrace.σ ^ m = MarkovTrace.σ ^ m * B := by
    induction m with
    | zero => simp
    | succ k ih =>
      calc B * MarkovTrace.σ ^ (k + 1)
          = B * (MarkovTrace.σ ^ k * MarkovTrace.σ)  := by rw [pow_succ]
        _ = (B * MarkovTrace.σ ^ k) * MarkovTrace.σ  := by ring
        _ = (MarkovTrace.σ ^ k * B) * MarkovTrace.σ  := by rw [ih]
        _ = MarkovTrace.σ ^ k * (B * MarkovTrace.σ)  := by ring
        _ = MarkovTrace.σ ^ k * (MarkovTrace.σ * B)  := by rw [hBσ]
        _ = MarkovTrace.σ ^ (k + 1) * B              := by rw [pow_succ]; ring
  -- Step 2: rewrite A · σ^m · B = (A · B) · σ^m using commutativity
  have hrewrite : A * MarkovTrace.σ ^ m * B = (A * B) * MarkovTrace.σ ^ m := by
    calc A * MarkovTrace.σ ^ m * B
        = A * (MarkovTrace.σ ^ m * B)   := by ring
      _ = A * (B * MarkovTrace.σ ^ m)   := by rw [hBσm]
      _ = (A * B) * MarkovTrace.σ ^ m   := by ring
  rw [hrewrite]
  -- Step 3: iterate Markov axiom m times to peel σ^m off the right
  have hpeel : ∀ (k : ℕ) (x : H),
      MarkovTrace.tr_M (x * MarkovTrace.σ ^ k) = MarkovTrace.z ^ k * MarkovTrace.tr_M x := by
    intro k
    induction k with
    | zero =>
      intro x
      simp
    | succ j ih =>
      intro x
      calc MarkovTrace.tr_M (x * MarkovTrace.σ ^ (j + 1))
          = MarkovTrace.tr_M (x * (MarkovTrace.σ ^ j * MarkovTrace.σ)) := by rw [pow_succ]
        _ = MarkovTrace.tr_M ((x * MarkovTrace.σ ^ j) * MarkovTrace.σ) := by ring_nf
        _ = MarkovTrace.z * MarkovTrace.tr_M (x * MarkovTrace.σ ^ j)   := MarkovTrace.markov _
        _ = MarkovTrace.z * (MarkovTrace.z ^ j * MarkovTrace.tr_M x)   := by rw [ih]
        _ = MarkovTrace.z ^ (j + 1) * MarkovTrace.tr_M x               := by ring
  rw [hpeel]
  -- Step 4: factorize tr_M(A·B) = tr_M A · tr_M B (commutativity hAB)
  rw [MarkovTrace.factor A B hAB]
  ring

/-- **Corollary** — magic-unfold applied to an atom with a magic
shell core.  If the atom braid word `W_atom` can be written as
`W_core · σ_{3C−1}^m · W_valence` with commuting W_core /
W_valence / σ (all three far-commuting pairwise), then:

  tr_M(W_atom) = z^m · tr_M(W_core) · tr_M(W_valence).

The HYPOTHESIS of braid-relation equivalence between the standard
`atom_braid_word_3A` and the core-first reordering is NOT proved;
computational check (`magic_unfold.py::validate_against_full`) on
T and ³He falsifies it for the inter-nucleon-coupled case.  So
this corollary is a CONDITIONAL statement on a specific braid-
word structure, not on the standard atom word.

Ref: [leitner2026] https://github.com/litlfred/qou
-/
theorem magic_unfold_peel_atom_corollary
    {H : Type*} [Ring H] [MarkovTrace H]
    (W_core W_valence : H) (m : ℕ)
    (W_atom : H)
    (h_decomp : W_atom = W_core * MarkovTrace.σ ^ m * W_valence)
    (h_cv     : W_core * W_valence = W_valence * W_core)
    (h_cσ     : W_core * MarkovTrace.σ = MarkovTrace.σ * W_core)
    (h_vσ     : W_valence * MarkovTrace.σ = MarkovTrace.σ * W_valence) :
    MarkovTrace.tr_M W_atom
      = MarkovTrace.z ^ m * MarkovTrace.tr_M W_core * MarkovTrace.tr_M W_valence := by
  rw [h_decomp]
  exact magic_unfold_peel W_core W_valence m h_cv h_cσ h_vσ

end QOU.MassEndomorphism
