---
# qou-qrkf
title: 'NEGATIVE: the a_D / Family-A production-wiring is correctly labelled — no laundering at this site'
status: completed
type: task
priority: normal
created_at: 2026-09-06T14:10:12Z
updated_at: 2026-09-06T14:10:49Z
---

## What was suspected

A corpus-grep aside flagged, without verifying it, that
`computations/substrate/z2bn_prolongation_qdifference_constraint.py:12-16`
claims the anchors `a_D^(2)=1`, `a_D^(3)=(q+1)^2/(3q)`, `a_D^(4)=Family-A` are
"PRODUCTION-WIRED Wedderburn-H_4 selection-rule inputs" *while* the corpus flags
`∮λ_SW^(n) = a_D^(n)` as the OPEN keystone, and `a_D^(4)=Family-A` is itself a
CODATA-implied near-match. If true that is an open conjecture and a fit reaching
production — the §"Axiomatization is NOT a Proof" case.

## Measured: it does not hold. Every layer is labelled.

**The Lean half is honest AND unwired.**
`QOU.Mass.SelectionRuleQuantumIntegerForm` (3 decls, 0 sorry) states in its own
docstring: "This does **not** touch the open keystone (the geometric↔categorical
identity `a_D^(n) = ∮ λ_SW^(n) = lw(n−1)`); it formalises the categorical half";
"The `τ` assembled here reproduces the anchors `a_D^(2..4)`, **to which `τ` is
fit**"; and "must **not** be extrapolated as the geometric period recurrence".
Both theorems are pure field algebra (`field_simp; ring`). **Zero importers** —
nothing in `content/`, `computations/` or `docs/` references it but itself.

**The Python half IS production-wired, and says so, and is deprecated.**
`_li_2_q_util.linking_weight_family_a` is "single source of truth for the
production multiplier" with live consumers (`mass_vol_density`,
`skein_proton_canonical`, `gamma_gamma_pair_production_decomposition`,
`mass_per_knot_density`). Its own docstring records that "at the substrate
anchor q₀ the value ≈ 2.533 is a CODATA-implied" near-match, and
`skein_proton_canonical.py` opens with "⚠ That absolute-mass form is DEPRECATED
(owner ruling 2026-06-24)", names the canonical muon-anchored route, and even
records that the λ_A tower "lands m_p_pred ≈ 966 MeV" — i.e. it carries its own
~3 % miss in the source.

Note the value `(3q²+4+3q⁻²)/4` is *exactly* the LHS of
`selection_rule_c3_quantum_integer`, so the Lean does formalise the
production-wired quantity — it simply formalises it honestly and is consumed by
nothing.

## Verdict

**Scope-(a) negative: no laundering at this site.** The anti-fit labelling
discipline is holding everywhere I probed. Recorded so the next agent reading
that docstring does not re-walk it.

**What this does NOT establish.** I checked the labelling and the wiring, not
whether the deprecated λ_A path should still have live consumers at all given
the 2026-08-11 absolute-mass excision (`qou-exam`). That is a separate question
and I did not measure it.
