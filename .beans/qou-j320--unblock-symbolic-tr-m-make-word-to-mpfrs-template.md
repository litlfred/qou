---
# qou-j320
title: 'Unblock symbolic tr_M: make word_to_mpfr''s template match structural, not float-based'
status: todo
type: task
priority: normal
created_at: 2026-08-19T19:46:57Z
updated_at: 2026-08-19T19:47:45Z
---

From qou-e58e. chi_monotone_transfer.word_to_mpfr calls float(h) and float(d) to CLASSIFY each letter against the sigma / sigma-inverse / averaged / color-weighted templates. This is NOT a precision defect -- it rebuilds d at full dps from q afterwards, so the numerics are clean. But the float refuses a sympy symbol, so chi_all_lambda_reduced_block and hence tr_M cannot be evaluated symbolically, even though mass_at_3A_proper.atom_braid_word_3A IS fully symbolic (verified: it returns letters like (1, -q/2 + 1/(2q), 0) and the interface (1, (-q+1/q)*(-(1-1/q^4)(q-1)^2/12 + 1/2), 2)).

Fix: match on the letter TEMPLATE structurally (carry a tag, or compare sympy expressions) rather than on a float value. Payoff: opens the symbolic derivation of delta(q) (qou-kgsx) instead of identifying it from a numeric sample, which would be a fit. Also opens exact rational-function work on tr_M generally.
