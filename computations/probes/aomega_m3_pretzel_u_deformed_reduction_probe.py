"""aomega_m3_pretzel_u_deformed_reduction_probe.py

Route C, M3, Part 12a (bean qou-x3iv): the u-DEFORMED one-dimensional reduction —
the meridian-holonomy deformation of the state integral, which is what the
holomorphic blocks and the rotated index are functions of.

Held input beyond Part 11: DG arxiv-1202.6268v2 (C.21)/(C.23): at meridian
parameter u (u_vec = (0,...,0,u), m = e^u the meridian eigenvalue) the exponent of
the state integral acquires  -(2/hbar) Z.B^-1 u_vec  (plus u-only constants that
need the completion (C,D) and are NOT derived here: they are overall factors).
GGM 2012.00062 (125)/(322): 4_1 = Z_{1,2} with shifts (u,0) and w = -2u, i.e.
  int Phi_b(v+u) Phi_b(v) e^{-pi i v^2 - 4 pi i u v} dv;  (240)/(323): 5_2 = Z_{2,3}
with shifts (0,u,-u), w = 0.

Derivation: Part 11 with P_i = c v_i W - (i pi + hbar/2) w_i - 2 u beta_i, beta = B^-1 e_N.
Each tetrahedron becomes Phi_b(v_i x + (1 - w_i) c_b - 2 beta_i ubar), ubar = u/(2 pi b),
and the cross terms P_i^2 add a u-linear term in x.  Everything exact in sympy.

Gates (one dictionary must serve both):  u_G := -2 ubar  (x_G = e^{2 pi b u_G} = m^{-2})
  G1  4_1 : shifts (u_G, 0) after centring, linear coefficient -2 u_G  == GGM (125) exactly
  G2  5_2 : shifts (u_G, 0, -u_G), linear 0                            == GGM (240) exactly
Test
  T1  m016: A = 2, shifts (+u_G/2, -u_G/2, 0) after centring, linear 0, i.e.
        int Phi_b(x + u_G/2) Phi_b(x - u_G/2) Phi_b(2x - c_b) e^{-2 pi i x^2} dx
      — the deformation sits on the two UNIT factors at HALF the meridian variable
      (x_G^{1/2} = m^{-1}); the doubled factor is undeformed.  Second level-2 signature.
Orientation: SnapPy's throughout (Part 11).  No q0, no float.
"""
from __future__ import annotations

import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))
sys.path.insert(0, HERE)
from aomega_m3_pretzel_one_dim_reduction_probe import nz_datum, rows_of, rank_one_factor  # noqa: E402

KNOTS = [("m004", "4_1", (0, 0)), ("m015", "5_2", (2, 2, 2)), ("m016", "(-2,3,7) = K12n242", (0, 2, 1))]


def deformed_reduction(c, v, w, beta):
    """Exact exponent bookkeeping.  Returns A, the u-dependent shift of each factor after
    centring the Gaussian, the linear coefficient, all as sympy expressions in ubar."""
    b, x, ub = sp.symbols("b x ubar")
    hbar = 2 * sp.pi * sp.I * b**2
    cb = sp.I * (b + 1 / b) / 2
    lam = 2 * sp.pi * b * cb                     # i pi + hbar/2
    u = 2 * sp.pi * b * ub
    n = len(v)
    W = 2 * sp.pi * b * x / c                    # t = -cW, t = -2 pi b x
    P = [c * v[i] * W - lam * w[i] - 2 * u * beta[i] for i in range(n)]
    E = sp.expand(-c * W**2 / (2 * hbar) + sum((P[i] ** 2 + 2 * lam * P[i]) / (2 * hbar) for i in range(n)))
    Ex = sp.Poly(E, x)
    A = sp.nsimplify(sp.simplify(Ex.coeff_monomial(x**2) / (-sp.pi * sp.I)))
    lin = sp.simplify(Ex.coeff_monomial(x) / (2 * sp.pi * sp.I))          # exponent = -pi i A x^2 + 2 pi i lin x + ...
    shifts = [sp.expand((1 - w[i]) * cb - 2 * beta[i] * ub) for i in range(n)]     # Phi_b(v_i x + shift_i)
    # centre: x -> x + lin/A  removes the linear term (Gaussian -pi i A (x - lin/A)^2 + const)
    x0 = sp.simplify(lin / A)
    shifts_c = [sp.expand(shifts[i] + v[i] * x0) for i in range(n)]
    lin_c = sp.simplify(sp.expand(-2 * sp.pi * sp.I * A * (-x0) + 2 * sp.pi * sp.I * lin) / (2 * sp.pi * sp.I))  # = 0 by construction
    return {"A": A, "lin_before": sp.factor(lin), "shifts_before": shifts, "x0": x0, "shifts_centred": shifts_c,
            "lin_after": sp.simplify(lin_c), "cb": cb, "ub": ub}


def main():
    t0 = time.time()
    import snappy
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    ub = sp.Symbol("ubar")
    uG = -2 * ub                                       # the dictionary
    res = {}
    for name, label, quad in KNOTS:
        M = snappy.Manifold(name)
        n = M.num_tetrahedra()
        Gm = sp.Matrix(rows_of(M.gluing_equations()))
        A_, B_, nu = nz_datum(Gm, n, quad)
        c, v = rank_one_factor(B_.inv() * A_)
        w = B_.inv() * nu
        beta = B_.inv()[:, n - 1]
        d = deformed_reduction(c, [sp.nsimplify(t) for t in v], [sp.nsimplify(t) for t in w], [sp.nsimplify(t) for t in beta])
        # express every shift EXACTLY as a*c_b + beta*u_G (a, beta rational): a = s(ubar=0)/c_b, beta = -(1/2) ds/dubar
        def canon(s):
            a = sp.nsimplify(sp.simplify(s.subs(ub, 0) / d["cb"]))
            be = sp.nsimplify(sp.simplify(sp.diff(s, ub) * sp.Rational(-1, 2)))
            assert sp.simplify(s - (a * d["cb"] + be * (-2 * ub))) == 0
            return a * sp.Symbol("c_b") + be * sp.Symbol("u_G")
        sh_uG = [canon(s) for s in d["shifts_centred"]]
        sh_before = [canon(s) for s in d["shifts_before"]]
        lin_uG = canon(d["lin_before"]) if d["lin_before"] != 0 else sp.Integer(0)
        # linear term expressed AFTER centring relative to the u-shift (for 4_1 GGM keeps a linear term and shift (u,0));
        # so also report the form with the smallest shift set to 0 (translate x by the last unit factor's shift)
        print(f"\n== {name} = {label}: c = {c}, v = {list(v)}, w = {list(w)}, beta = B^-1 e_N = {list(beta)}")
        print(f"   A = {d['A']};  before centring: linear coeff (of 2 pi i x) = {lin_uG},  shifts = {sh_before}")
        print(f"   centred (no linear term): shifts = {sh_uG}")
        res[name] = {"label": label, "c": str(c), "v": [int(t) for t in v], "beta": [str(t) for t in beta],
                     "A": str(d["A"]), "linear_coeff_before_centring_in_u_G": str(lin_uG),
                     "shifts_before_centring_in_u_G": [str(t) for t in sh_before],
                     "shifts_centred_in_u_G": [str(s) for s in sh_uG],
                     "dictionary": "u_G = -2 ubar, ubar = u_DG/(2 pi b); x_G = e^{2 pi b u_G} = m^{-2}, m = e^{u_DG} the DG meridian eigenvalue"}

    # G1: 4_1 vs GGM (125): Phi_b(v+u)Phi_b(v) e^{-pi i v^2 - 4 pi i u v}: translate so the second factor is unshifted
    r4 = res["m004"]
    b4 = [sp.sympify(s) for s in r4["shifts_before_centring_in_u_G"]]
    uGs = sp.Symbol("u_G")
    # translate x -> x - b4[1] (so factor 2 is Phi_b(x)): shifts become (b4[0]-b4[1], 0); linear coeff becomes lin - 2*A*(-b4[1])... exponent -pi i A (x - s)^2 + 2 pi i lin (x - s) => linear coeff lin + A s with s = -b4[1]
    # translate x -> x - s with s = b4[1]:  -pi i A (x - s)^2 + 2 pi i lin (x - s)  =>  linear coefficient  lin + A s
    lin4 = sp.simplify(sp.sympify(r4["linear_coeff_before_centring_in_u_G"]) + sp.sympify(r4["A"]) * b4[1])
    sh4 = [sp.simplify(b4[0] - b4[1]), 0]
    print(f"\n 4_1 in GGM's frame (second factor unshifted): shifts {sh4}, linear coefficient {lin4}  [GGM (125): (u,0), -2u]")
    check("G1-4_1 u-deformation == GGM (125)/(322): shifts (u_G, 0) and linear term -2 u_G, with u_G = -2 ubar",
          sh4 == [uGs, 0] and lin4 == -2 * uGs, shifts=[str(s) for s in sh4], linear=str(lin4))
    r5 = res["m015"]
    check("G2-5_2 u-deformation == GGM (240)/(323): shifts {u_G, 0, -u_G} and no linear term, SAME dictionary",
          sorted(res["m015"]["shifts_centred_in_u_G"]) == sorted(["u_G", "0", "-u_G"]) and r5["linear_coeff_before_centring_in_u_G"] == "0",
          shifts=r5["shifts_centred_in_u_G"])
    rp = res["m016"]
    check("T1-m016: A = 2, centred shifts (u_G/2, -u_G/2, 0) up to order — deformation on the UNIT factors at HALF the "
          "meridian variable, doubled factor undeformed; no linear term",
          rp["A"] == "2" and set(rp["shifts_centred_in_u_G"]) == {"u_G/2", "-u_G/2", "-c_b"} and rp["linear_coeff_before_centring_in_u_G"] in ("-c_b",),
          shifts=rp["shifts_centred_in_u_G"])

    verdict = ("DERIVED: the u-deformed one-dimensional integrals. One dictionary u_G = -2 ubar (x_G = m^{-2}) makes the "
               "4_1 reduction reproduce GGM (125) exactly INCLUDING its u-dependence (shifts (u_G,0), linear -2u_G) and the "
               "5_2 reduction reproduce (240) (shifts (u_G,0,-u_G), no linear term). The pretzel (SnapPy orientation) is "
               "int Phi_b(x + u_G/2) Phi_b(x - u_G/2) Phi_b(2x - c_b) e^{-2 pi i x^2} dx: the deformation sits on the two "
               "unit factors at HALF the meridian variable (x_G^{1/2} = m^{-1}) and the doubled factor is undeformed — a "
               "second level-2 signature, this time in x. Next (Part 12b): residues at the union of the three pole families "
               "(unit factors: c_b -/+ u_G/2 + ibm + ib^-1 n; doubled: c_b + (ibm + ib^-1 n)/2), blocks, sigma1-sigma1.")
    print(f"\n verdict: {verdict}")
    from qou_substrate.witness import WitnessBuilder as _WB
    wit = {"name": "aomega-m3-pretzel-u-deformed-reduction",
           "description": "u-deformed (meridian holonomy) one-dimensional reduction of the DG state integral for 4_1, 5_2 and the "
                          "(-2,3,7) pretzel; gates against GGM (125) and (240); the pretzel's deformation is at half the meridian variable.",
           "computation": "aomega-m3-pretzel-u-deformed-reduction", "engine": "python+sympy+snappy",
           "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
           "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
           "parameters": {"snappy_version": snappy.__version__, "u_term": "DG (C.21)/(C.23): -(2/hbar) Z.B^-1 u_vec, u_vec = u e_N",
                          "dropped": "u-only constants 2u.DB^-1u + (2 pi i + hbar) f.B^-1 u (overall factors; need the completion (C,D))",
                          "orientation": "SnapPy's (Part 11)"},
           "data": res, "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(wit, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pretzel-u-deformed-reduction.witness.json")
    with open(out, "w") as fh:
        json.dump(wit, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
