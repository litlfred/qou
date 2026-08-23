---
# qou-i2ir
title: 'Route C (f-map): Φ_b amplitude expansion → c_k ladder, BAR-EVEN channel — the sole open f-map frontier'
status: in-progress
type: task
priority: normal
created_at: 2026-08-21T21:28:47Z
updated_at: 2026-08-21T21:41:36Z
---

PARENT: qou-cds1. The ONLY untested f-map route after A/B/redirect were fenced (PR #5415: c3 NOT forceable from the D two-row trace, parity+genericity). Distinct from the A_omega Route C (qou-q9ih, DT/CoHA) — this is the c_k f-map AMPLITUDE leg.

OBJECT: Faddeev Phi_b / Andersen-Kashaev state integral for 4_1; semiclassical Z(4_1;h) ~ exp(Vol/h)*delta^{-1/2}*(1+k1 h+k2 h^2+...), Ohtsuki tower k1=11 sqrt3 pi/108, k2=2 pi^2/27 (closed forms). TARGET: c_k in Q_beta=Q_base*Prod(1+c_k u^k), u=b*hbar_q^2.

KEY CONSTRAINT (PR #5415): c3=-2 is a BAR-EVEN q=1 shadow. The amplitude route MUST target the bar-EVEN part (torsion delta^{-1/2} x even-order k's), not the odd tower.

PRIOR REFUTATIONS — route around, DO NOT re-run: C16 (not a formal Habiro element -> use the ANALYTIC integral); C17 (raw qZeilberger operator -> c_k O(1) residuals); C18 (PSLQ recognition -> ENTROPY-BLOCKED). Attack must be STRUCTURAL (closed-form k_n, forced combos), NEVER numerical PSLQ.

HOW (4 steps):
1. Extend the Ohtsuki recursion to k3,k4 as EXACT closed forms (pi, sqrt3, zeta-values) — sidesteps the C18 entropy wall.
2. Map h <-> u=b*hbar_q^2 at q0 (h_F=-ln q0, per the route-C probe). Exact conversion.
3. Form the BAR-EVEN amplitude combination; test if its u-coefficients are c2=-1, c3=-2 as FORCED (parameter-free) values.
4. STRUCTURAL prize: the 1-loop Reidemeister torsion delta(4_1) is the bar-even prefactor; test whether it / a forced amplitude ratio yields c3=J_Hopf(1)=-2 structurally — connects to the KC21 Phi_b-saddle result (|S|~0.0094~vol-deficit, qou-uoo0).

FIRST STEP: exact k3,k4 + bar-even amplitude combo vs c2/c3, symbolic. FORCED -> derivation; fitted/entropy-blocked -> honest negative. Anti-fit fence STRICT: closed-form only, no PSLQ, report negatives.

── EXECUTED step 1 (2026-08-21): Route C REFUTED scope-(a), structural ──
Used exact 4₁ Ohtsuki tower κ_n=(p/q)√3^{[n odd]}π^n (κ1..7 certified) + torsion δ(4₁)=1/√3 (jones_1loop_c0_calibration_fig8). Log-cumulants λ2=455π²/7776, λ3=270463√3π³/6298560.
ONE-SCALE/TWO-TARGET GATE: single σ forces c2=−1 AND c3=−2 iff 4λ2³+λ3²=0. It is 6.088 ≠ 0 — a SUM OF POSITIVES, structurally impossible. Plus √3-parity mismatch: odd cumulants carry √3, targets are √3-free rationals; no single scale reconciles. So the forced map fails; any working map = a fit (fence-forbidden). NOT entropy-blocked (unlike C18) — structural.
Probe: fmap_c3_routeC_amplitude_exclusion.py (6/6). Audit updated.
NET: all 4 f-map routes fenced (A/B/redirect trace-weights + C amplitude). c3=J_Hopf(1)=−2 is a genuine near-match, not forceable from any tried route. A derivation, if any, is outside all of these (the A_ω CoHA/BPS Route C qou-q9ih, a separate programme).
