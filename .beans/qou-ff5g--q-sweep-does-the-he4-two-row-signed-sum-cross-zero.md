---
# qou-ff5g
title: 'q-sweep: does the He4 two-row signed sum cross zero at some q != q0?'
status: todo
type: task
priority: normal
created_at: 2026-08-07T10:01:51Z
updated_at: 2026-08-07T10:01:52Z
---

DISCRIMINATOR for qou-8mmq (the 29,000x He4 two-row suppression). At q0 the He4 two-row stratum has l1 = 8.4532 but signed sum = -2.918e-4, ratio 3.45e-5, versus an ordinary 0.31-0.42 at D/T/3He. With 50-dps inputs an EXACT identity would leave a residual near 1e-50, so at q0 this is strong suppression, NOT exact.\n\nTEST: recompute sum_{l(lambda)<=2} y_lambda(q) chi^lambda_q(beta_4He) Delta_lambda across a range of q and look for a ZERO CROSSING.\n- If it crosses zero cleanly at some q* != q0, the suppression is a REAL IDENTITY and q0 merely sits near it -- that is a structural finding and q* itself is then an object worth identifying.\n- If it never crosses and just happens to be small at q0, it is a coincidence of the averaged-crossing convention and should be recorded as such (scope-(a) negative), NOT as a selection rule.\n\nBLOCKER: needs chi^lambda_q(beta_4He) as a FUNCTION of q, not the q0-pinned cache. The committed chi-helium-4-h12-at-q0-50dps.witness.json is evaluated AT q0 only, so this probe cannot reuse it -- it needs the Hoefsmit character machinery (chi_at_q0_via_hoefsmit_mpfr.py / pyhecke) re-run per q. In a fresh container pyhecke/pyhecke_native/mpmath are all absent (cf. bean qou-dgkf: pyhecke_native has no wheel), so this needs an environment with the compute stack, or a from-scratch Hoefsmit implementation.\n\nAlso check the SAME sweep at the other three isotopes as a control -- if they ALL dip near q0 the effect is conventional, not special to the doubly-magic 4He.
