---
# qou-uyb4
title: 'q-deformed Schur-Weyl: the K-weighted permutation character over the tensor power (the TRACE-WEIGHT half of q!=1)'
status: completed
type: task
priority: normal
created_at: 2026-09-05T07:40:22Z
updated_at: 2026-09-05T07:46:28Z
---

DONE 2026-09-05, sorry-free, lean-direct exit 0 (2.9 s), zero warnings, #print axioms
clean on all five public results.

    sum_{f invariant} prod_i w(f i)  =  prod_{orbits O} sum_k w(k)^|O|

THE DEFORMATION LIVES ENTIRELY IN THE ORBIT SIZES, which the q=1 count discards. That
is the whole content and it explains why the undeformed statement could get away with
COUNTING orbits rather than MEASURING them.

Three checks, and the middle one is the one that matters:
 * sum_orbitSize -- orbit sizes sum to card alpha (they really do partition).
 * weighted_permutation_character_one -- at w == 1 the product collapses to
   (card kappa)^orbitCount sigma, THE CHARACTER PROVED IN OrbitQuotientCount. So the
   deformation is not a new object; it is the same character with sizes retained. If
   this had failed, orbitSize or the equiv was wrong and the rest was decoration.
 * weighted_character_two -- at kappa = Fin 2 with K = diag(1, q^2) (the weight the
   corpus's own Schur-Weyl normalisation uses) the character is
   prod_O (1 + q^(2|O|)), one q-binomial per orbit. At q=1 each factor is 2.

CORROBORATION from the corpus, not designed for: derived_chi_catalogue_matrix_m_*.py
carry norm_scalar = (1+q^2)(1+q^2+q^4). Those are exactly [2]_{q^2} and [3]_{q^2},
i.e. the size-1 orbit factors for |kappa| = 2 and 3 -- the shape this theorem predicts.

🛑 WHICH q != 1 THIS IS. 'Quantum Schur-Weyl' is TWO independent deformations:
  (a) the TRACE WEIGHT -- flat trace -> K-weighted trace, K = diag(1,q^2)^{tensor n}.
      PROVED HERE.
  (b) the BRAIDING -- permutation P_sigma -> R-matrix Rcheck(q), S_n -> H_n(q).
      NOT HERE, NOT STARTED.
The double centralizer needs both. qou-mpq5's multi-week assessment STANDS.

MEASURED 2026-09-05: Mathlib has ZERO files matching QuantumGroup, HeckeAlgebra,
BraidGroup, RMatrix, YangBaxter, TemperleyLieb -- only Coxeter groups. So (b) is a
from-scratch development, not a gap closable by finding the right lemma. Do NOT cite
WeightedPermutationCharacter.lean as quantum Schur-Weyl.
