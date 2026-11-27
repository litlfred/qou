#!/usr/bin/env python3
"""Orientation of the two CAL-1 charts: the framing / bar-parity split (probe, 2026-11-27).

Thread "Unify the log and mass-formula energy scales", decision A ("derive the orientation
first"). Lean: QOU/Observations/EnergyScaleOrientation.lean. Audit:
docs/audits/2026-11-27-energy-scale-bridge.md section 7.

Claim checked: the electron trace factors as tau_e = q^3 * y3 with y3 = (q^4+1)/(q^2+1)^2
bar-invariant (y3(1/q) = y3(q)). So with beta = ln q,
    L_e = l_e + 3 beta,   w_e = omega_e + 3,
l_e = log y3 bar-even, omega_e = q d_q log y3 bar-odd. The log-chart unit sign is set by
l_e (bar-even part dominates), the mass-chart unit sign by the writhe 3 (framing dominates).
At q = 1: l_e = -ln 2 < 0 and w_e = 3 > 0, so the split is present in the classical
limit and is not a q0 accident. Exact arithmetic (mpmath, 50 dps). No measured value.
"""
import mpmath as mp

mp.mp.dps = 50
Q0 = mp.mpf("1.1099785827513808")  # proton pin (constants.Q); model evaluation point only

def y3(q): return (q**4 + 1) / (q**2 + 1) ** 2
def tau_e(q): return q**3 * y3(q)
def delta(F, q): return q * mp.diff(F, q)
def omega(q): return 4 * q**2 * (q**2 - 1) / ((q**4 + 1) * (q**2 + 1))

ok = True
def check(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

tol = mp.mpf(10) ** -30
for q in (Q0, mp.mpf(2), mp.mpf("0.7")):
    check(f"y3 bar-invariant at q={mp.nstr(q,6)}", abs(y3(1 / q) - y3(q)) < tol)
    check(f"omega = q d_q log y3 at q={mp.nstr(q,6)}", abs(delta(lambda t: mp.log(y3(t)), q) - omega(q)) < tol)
    check(f"omega bar-odd at q={mp.nstr(q,6)}", abs(omega(1 / q) + omega(q)) < tol)

b = mp.log(Q0)
le, om = mp.log(y3(Q0)), omega(Q0)
Le, we = mp.log(tau_e(Q0)), delta(lambda t: mp.log(tau_e(t)), Q0)
print("q0: l_e", mp.nstr(le, 12), " 3beta", mp.nstr(3 * b, 12), " L_e", mp.nstr(Le, 12))
print("q0: omega_e", mp.nstr(om, 12), " writhe 3", " w_e", mp.nstr(we, 12))
check("L_e = l_e + 3 beta", abs(Le - (le + 3 * b)) < tol)
check("w_e = omega_e + 3", abs(we - (om + 3)) < tol)
check("log chart: bar-even part dominates (l_e < -3 beta)", le < -3 * b)
check("mass chart: framing dominates (omega_e > -3)", om > -3)
check("q=1: l_e = -ln 2, omega_e = 0", abs(mp.log(y3(mp.mpf(1))) + mp.log(2)) < tol and omega(mp.mpf(1)) == 0)
# threshold: the log-chart unit changes sign where l_e + 3 beta = 0
qs = mp.findroot(lambda t: mp.log(tau_e(t)), mp.mpf(1.3))
print("log-chart unit sign change at q* =", mp.nstr(qs, 15), "(tau_e = 1)")
check("q0 lies below the log-chart sign change", Q0 < qs)
print("ALL PASS" if ok else "SOME FAIL")
raise SystemExit(0 if ok else 1)
