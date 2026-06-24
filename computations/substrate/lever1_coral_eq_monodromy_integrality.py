"""Option 2: the coral elliptic E_q + the integer-trace obstruction on tr B.

Probe only — no fit, no production wiring. Two findings:

1. The coral elliptic curve E_z (brings-surface/coral-elliptic.md) IS the descartes
   elliptic curve E_q (brings-surface/descartes-elliptic-curve.md): j(q0) = 129.86
   (descartes records 129.9) and the classical limit j(1) = 128, p(1)=2/3, r(1)=20/27
   match exactly. So the rank-2 W-plane = H^1(coral E_q) is the SAME curve direction B
   names (numerically confirmed; closes the curve-identification half of direction B).

2. INTEGER-TRACE OBSTRUCTION (decisive reframing of direction A / option 2). The
   topological Gauss-Manin monodromy of an elliptic-curve family acts on H^1(E,Z) = Z^2
   preserving the intersection form, hence lands in SL2(Z) -> every monodromy element has
   INTEGER trace. But tr B = tau_binding = 3(3q^4+8q^2+3)/(4q(q+1)^2) = 2.6424 at q0 is
   NOT an integer. Therefore B is NOT a topological SL2(Z) monodromy element of E_q. B is
   the holonomy of the ABELIANISED lambda_SW Cartan sub-connection (M-workplan 2026-06-06:
   prop:mi-sw-abelianisation) -- a real/hyperbolic flat-connection holonomy, tau = 2cosh
   theta, theta = 0.7815 -- NOT the integral pi_1-monodromy. The substrate torus
   tau_torus = 2cosh(2 eta0) = 2.0437 is ALSO non-integer, confirming the same
   connection-holonomy (not topological-monodromy) nature for both sectors.

(b)-exclusion invariant cited: integrality of SL2(Z) traces (the topological monodromy of
an elliptic family preserves H^1(E,Z), so its trace is an integer). This does NOT exclude
the coral E_q as the rank-2 W (the curve is confirmed); it identifies WHICH object B is
(abelianised connection holonomy, real trace) vs is NOT (integral topological monodromy).
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools", "qou-substrate", "python"))
import mpmath as mp
import sympy as sp
from qou_substrate import constants as C

mp.mp.dps = 40

# ---- symbolic coral/descartes E_q Weierstrass data: y^2 = x^3 + p x + r ----
qs = sp.Symbol("q", positive=True)
ss = sp.sqrt(qs)
zc = ss - 1/ss
p_sym = 2*(qs**2 - qs + 1)/(3*qs) + (qs - 1)/(3*ss)
r_sym = (20*(qs - 1)**3/(27*qs**sp.Rational(3, 2)) + 5*(qs - 1)**2/(9*qs)
         + 5*(ss - 1/ss)/9 + sp.Rational(20, 27))
Delta_sym = -16*(4*p_sym**3 + 27*r_sym**2)
j_sym = -1728*(4*p_sym)**3 / Delta_sym

q0s = sp.nsimplify(mp.nstr(mp.mpf(C.Q_MP) if hasattr(C, "Q_MP") else mp.mpf(str(C.Q)), 18), rational=False)
def ev(e, n=12):
    return float(sp.N(e.subs(qs, q0s), n))

j_q0 = ev(j_sym)
j_q1 = float(sp.nsimplify(sp.limit(j_sym, qs, 1)))
p_q1 = sp.nsimplify(sp.limit(p_sym, qs, 1))
r_q1 = sp.nsimplify(sp.limit(r_sym, qs, 1))

# ---- tau_binding + integer-trace test ----
q = mp.mpf(C.Q_MP) if hasattr(C, "Q_MP") else mp.mpf(str(C.Q))
eta = mp.log(q)
tau_binding = 3*(3*q**4 + 8*q**2 + 3)/(4*q*(q + 1)**2)
tau_torus = 2*mp.cosh(2*eta)
theta_b = mp.acosh(tau_binding/2)

def is_int(x, tol=mp.mpf("1e-9")):
    return abs(x - mp.nint(x)) < tol

results = {
    "j_coral_at_q0": j_q0,
    "j_descartes_recorded": 129.9,
    "j_match": abs(j_q0 - 129.9) < 0.1,
    "j_classical_limit_q1": j_q1,
    "p_q1": str(p_q1), "r_q1": str(r_q1),
    "tau_binding": mp.nstr(tau_binding, 16),
    "tau_binding_is_integer": is_int(tau_binding),
    "tau_torus": mp.nstr(tau_torus, 16),
    "tau_torus_is_integer": is_int(tau_torus),
    "theta_binding": mp.nstr(theta_b, 16),
    "nearest_int_to_tau_binding": int(mp.nint(tau_binding)),
}

assertions = {
    "coral_eq_is_descartes_curve_j_match": bool(abs(j_q0 - 129.9) < 0.1),
    "classical_limit_j_128": bool(abs(j_q1 - 128) < 1e-6),
    "classical_limit_p_2_3": bool(p_q1 == sp.Rational(2, 3)),
    "classical_limit_r_20_27": bool(r_q1 == sp.Rational(20, 27)),
    "tau_binding_NOT_integer": bool(not is_int(tau_binding)),
    "tau_torus_NOT_integer": bool(not is_int(tau_torus)),
    "B_excluded_from_topological_SL2Z": bool(not is_int(tau_binding)),
}
all_passed = all(assertions.values())

witness = {
    "computation": "lever1_coral_eq_monodromy_integrality",
    "description": (
        "Coral elliptic E_q = descartes E_q (j(q0)=129.86 ~ 129.9; classical j(1)=128, "
        "p(1)=2/3, r(1)=20/27 exact) confirms the direction-B curve. Decisive: tr B = "
        "tau_binding = 2.6424 is NOT an integer, but the topological Gauss-Manin monodromy "
        "of an elliptic family is in SL2(Z) (preserves H^1(E,Z)) with integer trace -> B is "
        "NOT a topological monodromy element. B is the abelianised lambda_SW Cartan-connection "
        "holonomy (real/hyperbolic, tau=2cosh theta). tau_torus=2.0437 also non-integer -> "
        "same connection-holonomy nature for both sectors."
    ),
    "discipline": (
        "no fit; sympy symbolic Weierstrass + mpmath 40dps; (b)-exclusion cites integrality "
        "of SL2(Z) traces (topological monodromy preserves H^1(E,Z)); does NOT exclude the "
        "coral E_q as the rank-2 W (curve confirmed) -- identifies which object B is."
    ),
    "auditOnly": "docs/audits/2026-06-24-lever1-coral-eq-monodromy-integrality.md",
    "results": results,
    "assertions": assertions,
    "allPassed": all_passed,
    "verdict": (
        "CORAL E_q CONFIRMED (j(q0)=129.86~129.9), but tr B = 2.6424 is NON-INTEGER so B is "
        "NOT the integral topological Gauss-Manin monodromy of E_q (which is SL2(Z), integer "
        "trace). B is the abelianised lambda_SW Cartan-connection holonomy (real/hyperbolic, "
        "tau=2cosh theta_binding, theta=0.7815). This REFRAMES option 2: a genus-1 Picard-Fuchs "
        "topological-monodromy computation would yield the WRONG (integer-trace) object. The "
        "decisive open step is the holonomy of the abelianised lambda_SW connection at q0, not "
        "the topological monodromy -- consistent with the M-workplan abelianisation (Cartan "
        "reduction) and the keystone non-compact (real-holonomy, q0 not a root of unity) arena. "
        "Curve identified; the explicit abelianised-connection holonomy = theta_binding stays "
        "the open keystone step. No fit; nothing wired."
    ),
}

out = os.path.join(os.path.dirname(__file__), "lever1-coral-eq-monodromy-integrality.witness.json")
with open(out, "w") as f:
    json.dump(witness, f, indent=2)

for k, v in results.items():
    print(f"  {k:32s} = {v}")
print()
for k, v in assertions.items():
    print(f"  [{'PASS' if v else 'FAIL'}] {k}")
print(f"\nallPassed = {all_passed}\nwitness -> {out}")
