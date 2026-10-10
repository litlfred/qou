---
# qou-j320
title: 'Unblock symbolic tr_M: make word_to_mpfr''s template match structural, not float-based'
status: completed
type: task
priority: normal
created_at: 2026-08-19T19:46:57Z
updated_at: 2026-08-19T20:12:14Z
---

From qou-e58e. chi_monotone_transfer.word_to_mpfr calls float(h) and float(d) to CLASSIFY each letter against the sigma / sigma-inverse / averaged / color-weighted templates. This is NOT a precision defect -- it rebuilds d at full dps from q afterwards, so the numerics are clean. But the float refuses a sympy symbol, so chi_all_lambda_reduced_block and hence tr_M cannot be evaluated symbolically, even though mass_at_3A_proper.atom_braid_word_3A IS fully symbolic (verified: it returns letters like (1, -q/2 + 1/(2q), 0) and the interface (1, (-q+1/q)*(-(1-1/q^4)(q-1)^2/12 + 1/2), 2)).

Fix: match on the letter TEMPLATE structurally (carry a tag, or compare sympy expressions) rather than on a float value. Payoff: opens the symbolic derivation of delta(q) (qou-kgsx) instead of identifying it from a numeric sample, which would be a fit. Also opens exact rational-function work on tr_M generally.

DONE 2026-08-19. Two edits, both minimal and both verified behaviour-preserving on the numeric path:

1. chi_monotone_transfer.word_to_mpfr -- a SYMBOLIC word already carries its d exactly at the requested q, so there is nothing to re-identify and nothing to re-lift: pass through. Numeric branch untouched; tr_M at q0 and 1/q0 is BIT-IDENTICAL before and after (30 digits).
2. wedderburn_jones_markov.y_lambda_at -- a symbolic q_val fell through to the numeric branch and died inside mpmath ("invalid literal for int() with base 10: q"), even though the exact convention-D solver was already wired for q_val=None. Symbolic q_val now reaches it, with THAT symbol. Numeric branch unchanged; the two agree at q0.

Both also replaced mp.mpf(0)/mp.mpf(1) seeds with exact Python ints -- identical for any numeric q, but an mpf seed drags sympy into Float contagion (the trap flavor_split_leading documents).

Independent check on the plumbing: symbolic weights come out as convention D exactly -- y(3)=(q^4+1)/(q^2+1)^2, y(2,1)=q^2/(q^2+1)^2, y(1,1,1)=0.

PAYOFF, IMMEDIATE: the closed form for delta fell out the same session. See qou-e58e / qou-kgsx.
