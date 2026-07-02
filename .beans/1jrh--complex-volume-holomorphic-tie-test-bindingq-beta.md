---
# 1jrh
title: 'Complex-volume holomorphic tie: test (binding,Q_beta) satisfy one Askey-Wilson 3-term recurrence (recurrence_invol_descent)'
status: completed
type: task
priority: normal
created_at: 2026-06-30T20:35:58Z
updated_at: 2026-07-02T16:20:00Z
---


## 2026-07-02 — formalize-first prune: test GATED on c₃^even (no scan run)
DOF count: AW has 4 params (a,b,c,d; q₀ fixed); measured rungs give at most 2
recurrence constraints (odd: c₂=−1 proved, c₃≈−2 near-match, c₄ CAL-anchored;
even: c₂≈−8 ONLY — one rung cannot constrain a recurrence). Under-determined ⇒
any AW identification now = fit (Δ_λ-gate forbidden). Prior art transferred:
constant depth-2 kernel already REFUTED (PR #1900, c₄=1−c₃² over-determination);
AW = the surviving non-constant case, so 1jrh is well-posed but blocked.
DECISIVE GATED TEST (parameter-free Casoratian sign test, one line once
c₃^even exists): W₂ ≈ 16 + c₃^even (numeric part from near-match rungs); AW positivity ⇒ W₃/W₂ > 0; violation
refutes one-recurrence outright. Blocking measurement: extend Hoefsmit Stage-B
net-route one order deeper in u (the c₂^even≈−8 machinery).
Full analysis: ../docs/audits/2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md

## 2026-07-02 — mechanism-level confirmation at H₂/Hopf (complementary, does NOT lift the gate)
The recurrence_invol_descent MECHANISM is compute-confirmed at the 2-strand
Hopf (deuteron-bond) tower, where no identification problem exists (the AW
multiplier c = q²+q⁻² is FORCED by the crossing eigenvalues, not fitted):
tower + both parity channels (binding bar-even, Q_β bar-odd) ride ONE
Chebyshev/q-ultraspherical (AW special-case) recurrence, exact + <1e-65 at
muon-q₀; bar-even hypothesis proved NECESSARY (bar-odd multiplier
cross-couples channels exactly: E_{m+1} = c·O_m + E_{m−1}). Probe:
computations/substrate/frakV_askey_wilson_recurrence_tie_probe.py (11/11,
PR #3216). The PHYSICAL c_k-ladder identification above remains GATED on
c₃^even — this note is the structural half only; status stays per the prune.

## 2026-07-02 — c₃^even MEASURED (exact-rational s-series); W₂ > 0; W₃ gated w/ indicative lean
Executed the gated measurement: exact sympy s-series of the net-route ladder
(qbeta_c3even_exact_sseries_probe.py, 132s). GATE PASS: exact c₂^even =
−8.00641 reproduces the prior robust rung. NEW RUNG: c₃^even = +86.66116
(exact expr in witness). Prior 10⁴ odd-order "blowup" was mp.taylor NOISE —
true bar-odd remainder is exact + modest, closed forms in ℚ[√3]
([s³]=−33/8+√3/8, …). Casoratian W₂ ≈ +102.67 > 0 (shadow rungs). W₃ stays
GATED: with the two UNTRUSTED c₄ inputs it comes out < 0 (would violate AW
positivity) — indicative scope-(a) lean AGAINST one-recurrence, decision needs
genuine c₄ rungs (H₄ Hoefsmit build for c₄^even; c₄^odd beyond CAL-anchor).
Bonus constraint: even rungs grow ×11,×21 ⇒ even-side u-ladder asymptotic;
disfavors a common AW recurrence IN u (kernel R(q,ξ) search constraint).
Audit: ../docs/audits/2026-07-02-1jrh-c3even-exact-measurement.md
>>>>>>> b686eb22 (compute(1jrh): measure c3^even = +86.661 via exact-rational s-series)
>>>>>>> 6f1bf4bb (compute(1jrh): measure c3^even = +86.661 via exact-rational s-series)
