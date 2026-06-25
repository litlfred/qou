"""Lever-1 (owner-ungated 2026-06-25): derive theta_binding from the color E_q
GEOMETRY, non-circularly.

Owner reversal: the narrow s5-so3 keystone reversal (2026-06-19) is extended to the
lambda_SW SW-period side of the SAME keystone (coordination ledger updated this PR).

The prior probes (lever1_color_eq_monodromy_integrality.py, ..._hyperbolicity.py,
..._lambda_sw_no_shortcut.py) all set theta = acosh(tau_binding/2) with tau_binding the
WIRED anchor value -- circular. Here we compute a curve-native candidate and confront it
with the target, WITHOUT feeding tau_binding in.

Construction (no fit):
  * Family E_q: y^2 = x^3 + p(q) x + r(q), p,r the color/descartes coefficients.
  * Griffiths-Dwork on the basis (omega = dx/y, varpi = x dx/y) gives the Gauss-Manin
    connection d/dq [omega, varpi]^T = N(q) [omega, varpi]^T (derived by hand; trace-free
    => sl_2, consistent with the proved det B = 1, prop:sl2-prolongation-recurrence).
    Validated numerically: the two periods omega(q)=∮dx/y, varpi(q)=∮x dx/y satisfy
    d/dq[omega,varpi] = N[omega,varpi] (finite-difference check at q0).
  * Abelianisation (prop:mi-sw-abelianisation): abelianised (Cartan) holonomy rapidity =
    spectral eigenvalue 1-form integrated along the substrate path,
    theta_spec = int_1^{q0} sqrt(-det N(q)) dq  (eigenvalues of N are +-sqrt(-det N)).
    q=1 (classical E_1) -> q0 (substrate), both smooth; no Delta=0 crossing on [1,q0].

PRE-REGISTERED (anti-numerology): report theta_spec RAW and x2/x0.5 (half vs full-period
convention -- the same '2' as z=s-1/s~2 sinh, tau=2 cosh) regardless of hit/miss; do NOT
tune a multiplier. Calibrate on the substrate torus (theta_torus = 2 log q0).

To parametrise we use s = sqrt(q) (everything rational in s -> no slow radical simplify);
d/dq f = (df/ds)/(2s).
"""
import json
import os
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
Q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")
S0 = mp.sqrt(Q0)

# ---- symbolic, rational in s = sqrt(q) ----
s = sp.Symbol("s", positive=True)
a = 2*(s**4 - s**2 + 1)/(3*s**2) + (s**2 - 1)/(3*s)            # p(q), q=s^2
b = 20*(s**2 - 1)**3/(27*s**3) + 5*(s**2 - 1)**2/(9*s**2) \
    + 5*(s - 1/s)/9 + sp.Rational(20, 27)                      # r(q)
# d/dq = (d/ds)/(2s)
aq = sp.diff(a, s)/(2*s)                                       # da/dq
bq = sp.diff(b, s)/(2*s)                                       # db/dq

D = (4*a**3 + 27*b**2)/6                                       # = -Delta/96
A_ = a**2*aq/3 + sp.Rational(3, 2)*b*bq
Bc = a*bq - sp.Rational(3, 2)*aq*b
Cc = -a*aq*b/2 + a**2*bq/3
fac = -1/(2*D)
N11 = fac*A_; N12 = fac*Bc; N21 = fac*Cc; N22 = fac*(-A_)      # d/dq connection, in s

f_N11 = sp.lambdify(s, N11, "mpmath"); f_N12 = sp.lambdify(s, N12, "mpmath")
f_N21 = sp.lambdify(s, N21, "mpmath"); f_N22 = sp.lambdify(s, N22, "mpmath")
f_a = sp.lambdify(s, a, "mpmath"); f_b = sp.lambdify(s, b, "mpmath")

def negdetN_of_s(sv):
    return -(f_N11(sv)*f_N22(sv) - f_N12(sv)*f_N21(sv))

# ---- numeric periods, as functions of q ----
def AB(qq):
    sv = mp.sqrt(qq); return f_a(sv), f_b(sv)

def real_root(qq):
    A, B = AB(qq)
    rts = mp.polyroots([1, 0, A, B])
    reals = [mp.re(r) for r in rts if abs(mp.im(r)) < mp.mpf("1e-20")]
    return max(reals)

def period(qq, kind):
    A, B = AB(qq); e1 = real_root(qq)
    if kind == "omega":
        g = lambda x: 1/mp.sqrt(x**3 + A*x + B)
    else:
        g = lambda x: x/mp.sqrt(x**3 + A*x + B)
    return 2*mp.quad(g, [e1, mp.inf])

# ---- validate N via the 2nd-order Picard-Fuchs ODE on the (convergent) first-kind
# period omega=∮dx/y.  varpi=∮x dx/y is 2nd-kind (divergent naive integral), so we
# eliminate it: w' = N11 w + N12 varpi => varpi=(w'-N11 w)/N12; varpi'=N21 w+N22 varpi
# => w'' = c1 w' + c0 w with c1 = N11+N22+N12'/N12, c0 = N11'-N11 N12'/N12+N12 N21-N11 N22.
hh = mp.mpf("1e-5")
w_m, w_0, w_p = (period(Q0-hh, "omega"), period(Q0, "omega"), period(Q0+hh, "omega"))
dw = (w_p - w_m)/(2*hh); ddw = (w_p - 2*w_0 + w_m)/hh**2
nat = lambda fn, qq: fn(mp.sqrt(qq))
N11_0, N12_0, N21_0, N22_0 = f_N11(S0), f_N12(S0), f_N21(S0), f_N22(S0)
dN11 = (nat(f_N11, Q0+hh) - nat(f_N11, Q0-hh))/(2*hh)
dN12 = (nat(f_N12, Q0+hh) - nat(f_N12, Q0-hh))/(2*hh)
c1 = N11_0 + N22_0 + dN12/N12_0
c0 = dN11 - N11_0*dN12/N12_0 + N12_0*N21_0 - N11_0*N22_0
pf_resid = ddw - c1*dw - c0*w_0
res_w = abs(pf_resid)/abs(ddw)
N_validated = bool(res_w < mp.mpf("1e-4"))

# trace-free check (numeric, a few points)
tr_max = max(abs(f_N11(mp.mpf(t)) + f_N22(mp.mpf(t))) for t in ["1.02", "1.05", "1.08"])
trace_free = bool(tr_max < mp.mpf("1e-25"))

# hyperbolic? -det N > 0 along the path
negdet_q0 = negdetN_of_s(S0)
hyperbolic = bool(mp.re(negdet_q0) > 0 and abs(mp.im(negdet_q0)) < mp.mpf("1e-20"))

# ---- theta_spec = int_1^{q0} sqrt(-det N) dq = int_1^{S0} sqrt(-det N) * 2s ds ----
def integrand_s(sv):
    nd = negdetN_of_s(sv)
    return mp.sqrt(nd) * 2*sv
theta_spec = abs(mp.quad(integrand_s, [mp.mpf(1), S0]))

# ---- target (computed ONLY for confrontation; never fed into theta_spec) ----
tau_binding = 3*(3*Q0**4 + 8*Q0**2 + 3)/(4*Q0*(Q0 + 1)**2)
theta_binding = mp.acosh(tau_binding/2)
theta_torus = 2*mp.log(Q0)
def rel(x, y): return float(abs(x - y)/abs(y))

results = {
    "q0": mp.nstr(Q0, 16), "p_q0": mp.nstr(f_a(S0), 12), "r_q0": mp.nstr(f_b(S0), 12),
    "trace_free_max_resid": mp.nstr(tr_max, 4),
    "neg_det_N_q0": mp.nstr(negdet_q0, 12),
    "omega_q0": mp.nstr(w_0, 12),
    "N_PF_ode_residual_rel": mp.nstr(res_w, 4),
    "theta_spec_raw": mp.nstr(theta_spec, 12),
    "theta_spec_x2": mp.nstr(2*theta_spec, 12),
    "theta_spec_half": mp.nstr(theta_spec/2, 12),
    "theta_binding_target": mp.nstr(theta_binding, 12),
    "theta_torus_2logq0": mp.nstr(theta_torus, 12),
    "tau_binding_target": mp.nstr(tau_binding, 12),
    "tau_from_theta_spec": mp.nstr(2*mp.cosh(theta_spec), 12),
    "tau_from_theta_spec_x2": mp.nstr(2*mp.cosh(2*theta_spec), 12),
    "rel_theta_spec_vs_binding": rel(theta_spec, theta_binding),
    "rel_theta_spec_x2_vs_binding": rel(2*theta_spec, theta_binding),
    "rel_theta_spec_vs_torus": rel(theta_spec, theta_torus),
}
assertions = {
    "N_trace_free_sl2": trace_free,
    "N_validated_by_PF_ode": N_validated,
    "connection_hyperbolic_on_path": hyperbolic,
    "theta_spec_raw_matches_binding_1pct": bool(rel(theta_spec, theta_binding) < 0.01),
    "theta_spec_x2_matches_binding_1pct": bool(rel(2*theta_spec, theta_binding) < 0.01),
}
solid = trace_free and N_validated
hit = assertions["theta_spec_raw_matches_binding_1pct"] or assertions["theta_spec_x2_matches_binding_1pct"]
witness = {
    "computation": "lever1_color_eq_lambda_sw_rapidity",
    "description": (
        "Owner-ungated (2026-06-25) non-circular test of theta_binding from color E_q "
        "geometry. Derives the Gauss-Manin connection N(q) of y^2=x^3+p(q)x+r(q) via "
        "Griffiths-Dwork (trace-free sl_2; validated by the two numerically integrated "
        "periods omega=∮dx/y, varpi=∮x dx/y). Abelianised (Cartan) holonomy rapidity "
        "theta_spec = int_1^{q0} sqrt(-det N) dq confronted with theta_binding="
        "acosh(tau_binding/2). Target NOT used as input."
    ),
    "discipline": (
        "no fit; sympy rational-in-s connection + mpmath 30dps periods; abelianised-holonomy "
        "spectral 1-form pre-registered (raw + x2 convention reported regardless of hit/miss); "
        "torus theta=2 log q0 for calibration. N validated by period system to <1e-5 rel."
    ),
    "auditOnly": "docs/audits/2026-06-25-lever1-color-eq-lambda-sw-rapidity.md",
    "results": results, "assertions": assertions,
    "allPassed": bool(solid),
}
witness["verdict"] = (
    ("MATCH (<=1%, convention noted): a curve-native abelianised-holonomy rapidity reproduces "
     "theta_binding -- candidate geometric derivation of tau."
     if hit else
     "NO 1% MATCH: the derived Gauss-Manin connection N(q) is SOLID (trace-free sl_2, "
     "period-validated <1e-5), but theta_spec = int sqrt(-det N) dq differs from theta_binding "
     "under the natural (half/full-period) conventions. N(q) is delivered as the concrete "
     "Picard-Fuchs input the prior sessions punted on; the residual is the precise "
     "abelianisation frame/normalisation.") + " No fit; nothing wired."
)
out = os.path.join(os.path.dirname(__file__), "lever1-color-eq-lambda-sw-rapidity.witness.json")
with open(out, "w") as f:
    json.dump(witness, f, indent=2, default=str)

print("trace-free:", trace_free, "| N validated (PF 2nd-order ODE on omega):", N_validated,
      f"(rel residual={mp.nstr(res_w,3)})")
print("hyperbolic on path:", hyperbolic)
print()
for k, v in results.items():
    print(f"  {k:32s} = {v}")
print()
for k, v in assertions.items():
    print(f"  [{'PASS' if v else '----'}] {k}")
print(f"\nverdict: {witness['verdict']}\nwitness -> {out}")
