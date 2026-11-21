---
# qou-n2dp
title: Five content blocks cite computation scripts that are not in the tree
status: todo
type: task
priority: normal
created_at: 2026-11-21T00:00:00Z
updated_at: 2026-11-21T00:00:00Z
---

Found during epic N2 (Lean foundations), session https://claude.ai/code/session_01Qmmkt6y3aQRP3f1SXsiZqC, on main 313bff6.

Each block's `computation.script` names a file that does not exist under
`computations/` or `fsh-guts/` (checked with `find`). The deletion commit is
not in this container's shallow history, so when and why they went is not
established here.

| block | missing script |
|---|---|
| stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation | computations/probe_q_beta_high_precision_ck.py |
| stochastic-mechanics/F3-eps6-leading-eq-neg-2b-cubed | computations/probe_q_beta_cat_per_factor_decomposition.py |
| mass-theory/multi-link-jones-q1-extension | computations/probe_q_beta_c5_c6_multilink.py |
| mass-theory/tau-M-asymptotic-rep-theory | computations/probe_q_beta_operator_valued_N2.py |
| mass-endomorphism/chi-per-irrep-cyclotomic-closed-forms | computations/probe_per_wedderburn_block_ck.py |

(`braids-and-knots/chi-sym-alt-closed-form` was checked too; its script exists.)

## Check against owner rulings before acting

Four of the five are Q_β `c_k`-ladder probes. The ladder is convention-C-frame
and its Form A base is the retired z = 1 cell; Q_β is now derived from γγ
(ruling 2026-11-20) and every β-decay route uses the two-term trace
(2026-11-21). So do NOT re-create these probes on the old basis. For each
block decide: point it at a live producer on the current basis, or mark the
block's numbers as historical / superseded with this evidence.

Owner decision needed for any block whose kind or claims change.
