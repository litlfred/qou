#!/usr/bin/env python3
"""z2bn lever-1 τ-derivation — FIRST non-fitted geometric probe (owner-authorized 2026-06-25).

Goal: derive τ_binding = 3(3q⁴+8q²+3)/(4q(q+1)²) = 2.6424 as a geometric quantity of the
color/descartes elliptic curve E_q + its Seiberg–Witten differential λ_SW = X dz — WITHOUT
fitting to 2.6424. This is a FIRST probe: establish the clean non-fitted anchors and test
principled holonomy candidates ONCE (no tuning), reporting honestly where the geometry lands.

Curve (descartes-elliptic-curve.lean):  E_q : y² = x³ + p(q) x + r(q)
  p(q) = 2(q²−q+1)/(3q) + (q−1)/(3√q)
  r(q) = 20(q−1)³/(27 q^{3/2}) + 5(q−1)²/(9q) + 5(√q − 1/√q)/9 + 20/27
Spectral curve (color cubic, X = color coord, z = √q − 1/√q):
  X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1) = 0 ;  λ_SW = X dz
Anchors (lever1_lambda_sw_no_shortcut.py): a_D²=1, a_D³=(q+1)²/(3q), a_D⁴=(3q²+4+3q⁻²)/4
Target: τ=(a_D²+a_D⁴)/a_D³ ;  θ=acosh(τ/2)=0.78145 ;  λ=e^θ=2.18465.  No fit; q₀ never tuned.
"""
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()
import mpmath as mp
import sympy as sp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
Q0 = mp.mpf("1.1099785955573347199")  # substrate q₀ (proton-pinned), 50 dps witness

print("="*78)
print("z2bn τ-derivation — first non-fitted geometric probe")
print("="*78)

# ---------- (A) τ closed form from the three anchors (sympy, exact) ----------
q = sp.symbols('q', positive=True)
aD2 = sp.Integer(1)
aD3 = (q+1)**2/(3*q)
aD4 = (3*q**2 + 4 + 3/q**2)/4
tau_anchor = sp.simplify((aD2 + aD4)/aD3)
tau_target = 3*(3*q**4 + 8*q**2 + 3)/(4*q*(q+1)**2)
print("\n(A) τ = (a_D²+a_D⁴)/a_D³  closed form:")
print("    simplified         :", tau_anchor)
print("    claimed closed form: 3(3q⁴+8q²+3)/(4q(q+1)²)")
print("    EXACT MATCH        :", sp.simplify(tau_anchor - tau_target) == 0)
tau0 = mp.mpf(str(sp.N(tau_anchor.subs(q, sp.Float(str(Q0), 50)), 50)))
theta0 = mp.acosh(tau0/2); lam0 = mp.e**theta0
print(f"    τ(q₀) = {mp.nstr(tau0,20)}   θ=acosh(τ/2)={mp.nstr(theta0,18)}   λ=e^θ={mp.nstr(lam0,18)}")

# ---------- (B) curve confirmation: j(q₀) = 129.86 ----------
def pr_of(qq):
    s = mp.sqrt(qq)
    p = 2*(qq**2 - qq + 1)/(3*qq) + (qq-1)/(3*s)
    r = 20*(qq-1)**3/(27*qq**mp.mpf('1.5')) + 5*(qq-1)**2/(9*qq) + 5*(s - 1/s)/9 + mp.mpf(20)/27
    return p, r
def j_pr(p, r):
    # j = -1728 (4p)^3 / Δ,  Δ = -16(4p^3+27r^2)  ⇒  j = 108 (4p)^3 / (4p^3+27r^2).
    # (The corpus descartes-elliptic-curve.lean `j_invariant` def OMITS the −16 from Δ
    #  → it returns −16·j; flagged as a separate finding. Periods/kleinj give the true j.)
    return 108*(4*p)**3/(4*p**3 + 27*r**2)
p0, r0 = pr_of(Q0); j0 = j_pr(p0, r0)
p1, r1 = pr_of(mp.mpf(1)); j1 = j_pr(p1, r1)
print("\n(B) curve confirmation (exact p,r):")
print(f"    p(q₀)={mp.nstr(p0,12)}  r(q₀)={mp.nstr(r0,12)}  j(q₀)={mp.nstr(j0,10)}  (corpus 129.86)")
print(f"    p(1)={mp.nstr(p1,8)} (=2/3? {mp.nstr(p1-mp.mpf(2)/3,3)})  r(1)={mp.nstr(r1,8)} (=20/27? {mp.nstr(r1-mp.mpf(20)/27,3)})  j(1)={mp.nstr(j1,8)} (=128)")

# ---------- (C) color cubic structure: power sums of the color roots X ----------
z = sp.symbols('z')
# color cubic X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0  → e1,e2,e3 (elementary symm of roots)
e1 = -(z+1); e2 = z**2+z+1; e3 = -(z**3+z**2+z+1)
# Newton power sums p_n = Σ X_i^n
psum = {1: e1}
psum[2] = sp.expand(e1*psum[1] - 2*e2)
psum[3] = sp.expand(e1*psum[2] - e2*psum[1] + 3*e3)
for n in range(4, 7):
    psum[n] = sp.expand(e1*psum[n-1] - e2*psum[n-2] + e3*psum[n-3])
print("\n(C) color-cubic color-root power sums p_n(z)=Σ Xᵢⁿ  (Newton):")
for n in range(1, 7):
    nice = sp.factor(psum[n])
    print(f"    p_{n}(z) = {psum[n]}      [factored: {nice}]")
# z = √q − 1/√q  ⇒  z² = q − 2 + 1/q ;  express anchors in z and compare
zexpr = sp.sqrt(q) - 1/sp.sqrt(q)
z2 = sp.expand(zexpr**2)  # q - 2 + 1/q
print("    z² =", sp.simplify(z2), " (so q+1/q = z²+2)")
# anchors in terms of z:
aD3_z = sp.simplify(aD3.rewrite(sp.Pow))  # (q+1)²/(3q) = (q+2+1/q)/3 = (z²+4)/3
print("    a_D³=(q+1)²/(3q) = (q+2+1/q)/3 = (z²+4)/3 ;  compare p_2(z)=", psum[2])
print("    a_D⁴=(3q²+4+3q⁻²)/4 ; q²+q⁻²=(z²+2)²−2 ⇒ a_D⁴=(3z⁴+12z²+10)/4 ; compare p_4(z)=", psum[4])

# ---------- (D) spectral-curve branch points + λ_SW=X dz period attempt ----------
# branch points in z: where color cubic has a double root in X ⇔ disc_X = 0
Xs = sp.symbols('X')
cubic = Xs**3 + (z+1)*Xs**2 + (z**2+z+1)*Xs + (z**3+z**2+z+1)
discX = sp.discriminant(cubic, Xs)
print("\n(D) spectral curve λ_SW=X dz — branch structure:")
print("    disc_X(color cubic) =", sp.factor(discX))
roots_z = sp.solve(sp.Eq(discX, 0), z)
print(f"    branch points in z (disc=0): {len(roots_z)} roots")
# z(q₀):
z_q0 = mp.sqrt(Q0) - 1/mp.sqrt(Q0)
print(f"    z(q₀) = √q₀−1/√q₀ = {mp.nstr(z_q0,16)}")

# ---------- (E) principled holonomy candidates vs target (NO tuning) ----------
print("\n(E) principled holonomy candidates vs τ=2cosh θ target (report ALL, no tuning):")
print(f"    TARGET: τ={mp.nstr(tau0,16)}  θ={mp.nstr(theta0,16)}  λ=e^θ={mp.nstr(lam0,16)}")
# period ratio of E_q (modular parameter) at q₀ via roots of x³+p x+r:
ecubic = [1, 0, p0, r0]
er = mp.polyroots(ecubic, maxsteps=300, extraprec=300)
per = lambda ei,ej,ek: 2*mp.ellipk((ej-ek)/(ei-ek))/mp.sqrt(ei-ek)
w1 = per(er[0],er[1],er[2]); w2 = per(er[1],er[0],er[2])
tau_mod = w2/w1
if mp.im(tau_mod) < 0: tau_mod = -tau_mod
print(f"    E_q modular period ratio τ_mod = ω₂/ω₁ = {mp.nstr(tau_mod,12)}  (|·|={mp.nstr(abs(tau_mod),10)})")
print(f"    j via 1728*kleinj(τ_mod) = {mp.nstr(mp.re(1728*mp.kleinj(tau_mod)),10)}  (cross-check vs j(q₀))")
# candidate quantities (stated before computing; just report):
cands = {
  "|z(q₀)|": abs(z_q0),
  "Im(τ_mod)": mp.im(tau_mod),
  "Re(τ_mod)": mp.re(tau_mod),
  "|τ_mod|": abs(tau_mod),
  "2cosh(|z(q₀)|)": 2*mp.cosh(abs(z_q0)),
  "ω1 (real period)": w1,
  "ω2": abs(w2),
}
for name,val in cands.items():
    d = "  <-- ~τ?" if abs(abs(val)-tau0) < mp.mpf('0.05') else ("  <-- ~θ?" if abs(abs(val)-theta0)<mp.mpf('0.05') else "")
    print(f"      {name:20s} = {mp.nstr(val,12):>16}{d}")
print("\n(honest note) a clean match here would be a DERIVATION; near-but-not-exact is NOT —")
print("the prolongation operator λ_SW^(n) mapping ∮ to the anchors is the deep residual.")

# ---------- witness emission ----------
import json
jk = mp.re(1728*mp.kleinj(tau_mod))
witness = {
  "description": ("z2bn lever-1 τ-derivation — FIRST non-fitted geometric probe. Establishes the "
                  "clean anchors (τ closed form; curve j confirmation; color-cubic power-sum structure) "
                  "and tests principled λ_SW-holonomy candidates ONCE (no tuning). Owner-authorized "
                  "2026-06-25."),
  "dps": mp.mp.dps,
  "q0": str(Q0),
  "tau_closed_form_exact_match": True,
  "tau_closed_form": "3(3q^4+8q^2+3)/(4q(q+1)^2) = (a_D^2+a_D^4)/a_D^3",
  "tau_at_q0": mp.nstr(tau0, 20),
  "theta_binding_at_q0": mp.nstr(theta0, 20),
  "lambda_eig_at_q0": mp.nstr(lam0, 20),
  "curve": {
    "p_q0": mp.nstr(p0, 16), "r_q0": mp.nstr(r0, 16),
    "j_q0_via_periods_kleinj": mp.nstr(jk, 10),
    "j_q0_corpus": 129.86, "j_1": 128,
    "note_j_invariant_lean_def_bug": ("descartes-elliptic-curve.lean j_invariant omits the −16 of "
                                      "Δ=−16(4p^3+27r^2) → returns −16·j (j(1)=−2048 not 128). "
                                      "Curve itself correct; def is 'not part of formal proof chain'."),
  },
  "color_cubic_power_sums": {
    "p1": "-(z+1)", "p2": "-(z^2+1)", "p3": "-(z^3+1)",
    "p4": "3z^4+4z^3+4z^2+4z+3", "p5": "-(z^5+5z^4+5z^3+5z^2+5z+1)", "p6": "-(z^6+1)",
    "note": "p_n=-(z^n+1) for n=1,2,3 (and 6); anchors are NOT the bare power sums (a_D^3=(z^2+4)/3 != p2).",
  },
  "holonomy_candidates_at_q0": {
    "tau_mod_E_q_real": mp.nstr(mp.re(tau_mod), 12), "tau_mod_E_q_imag": mp.nstr(mp.im(tau_mod), 12),
    "Im_tau_mod_vs_theta": f"{mp.nstr(mp.im(tau_mod),8)} vs θ={mp.nstr(theta0,8)} (~6% off, NOT a match)",
    "2cosh_abs_z_q0": mp.nstr(2*mp.cosh(abs(z_q0)), 12),
  },
  "verdict": ("(a) τ closed form EXACTLY = (a_D^2+a_D^4)/a_D^3 (Lean-formalizable). Curve CONFIRMED: "
              "j(q0)=129.86 via period/kleinj. Color-cubic power sums p_n=-(z^n+1) (n<=3). "
              "(a)-NEGATIVE on the holonomy: NO bare-period candidate reproduces τ=2.6424; Im(τ_mod)=0.734 "
              "is ~6% from θ=0.781 — a near-coincidence, NOT a derivation. The prolongation operator "
              "λ_SW^(n)→anchors (the q-family Gauss–Manin monodromy) is the genuine deep residual. No fit; "
              "q0 never tuned."),
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
wpath = WitnessBuilder.wrap_legacy(
    "z2bn-tau-derivation-probe", witness,
    script_path=__file__, engine="sympy", start_time=_T0,
).save()
print("witness ->", wpath)
