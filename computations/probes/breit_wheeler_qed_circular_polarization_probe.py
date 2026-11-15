#!/usr/bin/env python3
"""Tree-level QED with CIRCULAR polarizations: is either helicity configuration zero?

Bean qou-ccst / qou-qs2u, PR #7825 (owner F1(b)). In the (2,1) block of H_3 the letter
sigma_i is diagonal in its own eigenline pair (the q / -q^-1 lines that the BW block calls
left / right circular), and sigma_i sigma_i = h sigma_i + 1 stays diagonal in that pair.
So the reading "sigma_i sigma_i = same-letter helicity content" assigns sigma_i sigma_i to
photon pairs of definite helicity in one circular basis. This script asks whether QED
pair production vanishes for either helicity configuration.

Photon 1 moves along +z, photon 2 along -z. Polarization VECTORS e_pm = (0, 1, +-i, 0)/sqrt2.
Same vector (e+, e+) is J_z = +2 (opposite helicities); (e+, e-) is J_z = 0 (equal
helicities). Exact sympy, rational kinematics as in the linear-polarization probe; the
assertions are the gate.
"""
import importlib.util
import pathlib
import sympy as sp

here = pathlib.Path(__file__).with_name("breit_wheeler_qed_linear_polarization_probe.py")
spec = importlib.util.spec_from_file_location("lin", here)
lin = importlib.util.module_from_spec(spec)
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(lin)

r = 1 / sp.sqrt(2)
e_plus = [0, r, sp.I * r, 0]
e_minus = [0, r, -sp.I * r, 0]
res = {}
for E, P, label in [(sp.Rational(5, 4), sp.Rational(3, 4), "beta=3/5"),
                    (sp.Rational(13, 12), sp.Rational(5, 12), "beta=5/13")]:
    lin.E, lin.P = E, P
    lin.k1 = [E, 0, 0, E]
    lin.k2 = [E, 0, 0, -E]
    for dname, n in [("along x-z (3/5,0,4/5)", (sp.Rational(3, 5), 0, sp.Rational(4, 5))),
                     ("transverse (1,0,0)", (1, 0, 0))]:
        p1 = [E] + [P * x for x in n]
        jz2 = sp.nsimplify(sp.simplify(lin.msq(p1, e_plus, e_plus)))
        jz0 = sp.nsimplify(sp.simplify(lin.msq(p1, e_plus, e_minus)))
        res[(label, dname)] = (jz0, jz2)
        print(f"{label:10s} {dname:24s} |M|^2  J_z=0: {jz0}   J_z=2: {jz2}")
assert all(a > 0 for a, _ in res.values()), "J_z = 0 vanishes somewhere"
assert any(b > 0 for _, b in res.values()), "J_z = 2 vanishes everywhere tested"
print("VERDICT: both helicity configurations give nonzero pair production at the points tested.")
