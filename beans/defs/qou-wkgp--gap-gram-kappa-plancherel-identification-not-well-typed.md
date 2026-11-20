---
# qou-wkgp
title: 'GAP: conj:gram-determinant-plancherel-ratio has no well-typed statement — Plancherel product vs det G_cl/det G_q'
status: todo
type: task
priority: normal
tags:
    - gap
    - lean
    - alpha-em
created_at: 2026-11-20T16:00:00Z
updated_at: 2026-11-20T16:00:00Z
parent: qou-3l2l
---

Found 2026-11-20 (PR #8562, branch claude/alpha-em-witten-kappa-2026-11-20).

The sorry in mass-theory/gram-determinant-plancherel-ratio.lean
(gram_kappa_numerical_value) stated a FALSE proposition: its torus-pair
predicate was a universally quantified parameter, so fun _ _ => True is a legal
instance and the statement is the universal closure over CharacterDecomposition
data. Replaced by the sorry-free gram_kappa_numerical_value_refuted (empty data:
gramKappa = 1, |1 - 1.722| = 0.722). lean -DautoImplicit=false -s 65536 exit 0;
axioms propext, Classical.choice, Quot.sound.

The 1.722 is det G_cl / det G_q (kappa_gram(q0) = 1.7216142017088 at the
one-term proton pin, 70 dps), which never uses gramKappa.

OPEN (not queued as a sorry, deliberately): a WELL-TYPED statement of the
identification. Obstacles already recorded in
docs/audits/2026-11-15-sidecar-review-mass-theory/route-other.md row 16:
T(2,9) lives in H_2 and T(3,5) in H_3 (no common n); exponents chi_s*chi_w are
not integers; T(3,5) is not central so beta = sum chi_l e_l fails. A statement
must first fix a common algebra and an exponent convention. Until then a sorry
here would be a trap.

Does NOT affect any scored row: m_K/m_pi's alpha uses det G_cl/det G_q directly.
