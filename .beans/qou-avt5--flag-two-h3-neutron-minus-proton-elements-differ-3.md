---
# qou-avt5
title: 'FLAG: two H_3 "neutron minus proton" elements differ 39% at the substrate, with no disambiguation row'
status: todo
type: task
priority: high
created_at: 2026-08-26T04:30:52Z
updated_at: 2026-08-26T04:30:52Z
---

Parent: `qou-avtq`. Surfaced while checking `qou-avt2`'s premise (are the
hand-derived per-block characters right?) before building a general-n tool.

NOT A BUG REPORT. This MEASURES a discrepancy and does NOT determine which object
is intended. Do not cite it as showing either one wrong.

## The two objects

(A) `Delta = NF(n) - NF(p)` -- the GROBNER-SHIRSHOV NORMAL FORM difference.
    `nuclear-interactions/qbeta-counit-closed-form.md` derives
    `eps(Delta) = h^2/2 - h`, `tr_M(Delta) = h^2/2 - h*z`, and qou-cds1
    verified `eps(Delta)*E_0` reproduces the committed Q_A closed form exactly.
    This is what the ladder phase is built from (`eps - tr_M = h(z-1) = 2*alpha`).

(B) `Delta_T_beta` -- whose per-block characters are the hand-derived closed
    forms in `qbeta_utils.py` and Lean `QBetaPerBlockChiClosedForms`
    (`-- Ref: [hoefsmit1974]`). Their source witness
    `qbeta-per-block-paper-closed-forms` calls them `chi_lambda(beta_n - beta_p)`
    -- the RAW BRAID difference, not the normal form.

## The test and the measurement

The counit is the 1-dim rep `sigma_i -> q`, i.e. exactly the `lambda = (n)`
block, so for ONE AND THE SAME element `chi_(3)(X) = eps(X)` identically.

    q            chi_(3)(Delta_T_beta) / eps(Delta)
    1+1e-2       1.030454535251763
    1+1e-4       1.000300045004500
    1+1e-8       1.000000030000000
    q -> 1       1                    (exact limit)
    q0           1.39090616920312     <- 39% at the substrate

They AGREE CLASSICALLY and DIVERGE AT THE SUBSTRATE. Both are linear in hbar_q at
leading order (each -> -2*hbar_q), which is why a leading-order check missed it.

Downstream: `Delta_tau_M = sum y_lambda chi_lambda(Delta_T_beta)` is NOT
`tr_M(Delta)` in either weighting (-0.18443 dim-weighted / -0.15802
un-dim-weighted vs -0.10624), so the two feed different consumers with no note.

## Why this is a flag and not a shrug

Agreeing at q=1 and differing at q0 is exactly what TWO DIFFERENT
q-DEFORMATIONS OF ONE CLASSICAL OBJECT look like -- real, common, and not
automatically an error. What IS a defect is that the corpus carries NO registry
section-2 disambiguation row for these two and nothing in docs/, content/ or
computations/ states that they differ. AGENTS.md names this exact class
("distinct objects sharing a glyph is a recurring root cause") and registry
section 2 exists for it.

## What would settle it (NOT attempted here)

Exhibit the two WORDS.
* If `NF(n)-NF(p)` and `beta_n - beta_p` are genuinely distinct elements of
  H_3(q): add the disambiguation row and move on.
* If they are meant to be the SAME element: one of the two closed forms is wrong
  at O(hbar_q^2), and either the ladder (via eps/tr_M) or the per-block c_k
  extraction inherits the error. That would be consequential -- the ladder's
  whole phase is eps - tr_M.

Probe: computations/qbeta/qbeta_delta_vs_deltaTbeta_discrepancy_probe.py (5/5)
