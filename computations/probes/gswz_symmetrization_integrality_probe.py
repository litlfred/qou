"""GSWZ symmetrization-integrality probe + the module-membership gate demo.

Beans qou-c0aw (U3) + qou-1hlh (U2 gate v1). Scope-(a); no fit; nothing
wired; audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 3).

WHAT THIS CHECKS (exact rational arithmetic, sympy):

1. U3 — the bar-even symmetrization integrality of the 4_1 Kashaev
   asymptotic series, from the printed GSWZ data (arXiv:2412.04241 v2,
   eqns (1)-(2), uploaded at library/arxiv-2412.04241v2/2412.04241v2.pdf). The inner
   series B(h) = 1 + b1 h + b2 h^2 + b3 h^3 + ... has coefficients with
   wild denominators (24*3*sqrt(-3), 1152*(3 sqrt(-3))^2, ...), yet the
   bar-even symmetrization B(h)B(-h):
     - is even in h (odd coefficients cancel EXACTLY),
     - has h^2 coefficient 2*b2 - b1^2 = -1/27 — sqrt(-3)-free and
       3-integral (denominator a pure power of 3),
     - converted to x = q - 1 via h = log(1+x), reproduces the printed
       GSWZ eqn (2) coefficients -1/27 x^2 + 1/27 x^3.
   The nontrivial cancellation (576/15552 = 1/27 from 121 and 697) is
   the arithmetic signature of module membership.

2. U2 gate v1 (executable) — DISCRIMINATING POWER: perturbing b2 by a
   generic rational (the shape of a "fitted" coefficient) breaks the
   3-integrality of the symmetrization, so the gate refutes fitted
   candidates WITHOUT any anchor comparison. This is the first
   executable membership test for fibre-level Habiro-element candidates
   (#1713 / c_k programme); Frobenius-gluing tests across roots of
   unity need multi-fibre candidate data and stay on bean qou-1hlh.

HONESTY: input coefficients are transcribed from the GSWZ paper (their
eqn (1), 4 terms); this probe verifies the symmetrization/integrality
structure exactly at the supported orders (h^2, h^3; x^2, x^3). An
independent recomputation of Phi(h) from formal Gaussian integration
(their eqn (276)) is future work, not claimed here.
"""

import json
import pathlib
import sys
from fractions import Fraction

import sympy as sp

s = sp.sqrt(-3)  # sqrt(-3); (3s)^2 = -27, (3s)^3 = -81 s

# GSWZ eqn (1) inner-series coefficients (prefactor 1/(-3)^(1/4) removed;
# symmetrization squares it to 1/sqrt(-3), also removed here).
b = [
    sp.Integer(1),
    sp.Rational(11, 24) / (3 * s),
    sp.Rational(697, 1152) / (3 * s) ** 2,
    sp.Rational(724351, 414720) / (3 * s) ** 3,
]

h = sp.symbols("h")
N = 3  # supported order from 4 printed terms

B = sum(b[k] * h**k for k in range(N + 1))
F = sp.expand(B * B.subs(h, -h))  # bar-even symmetrization
F_ser = sp.Poly(sp.expand(F), h).all_coeffs()[::-1]  # ascending in h


def denom_primes(r):
    """Prime support of the denominator of a Rational."""
    q = sp.nsimplify(r)
    return set(sp.factorint(sp.Rational(q).q).keys())


checks = {}

# (1) odd cancellation at h^1, h^3
c1 = sp.simplify(F_ser[1]) if len(F_ser) > 1 else 0
c3 = sp.simplify(F_ser[3]) if len(F_ser) > 3 else 0
checks["odd_h_coefficients_vanish"] = bool(c1 == 0 and c3 == 0)

# (2) h^2 coefficient = -1/27, sqrt(-3)-free, 3-integral
c2 = sp.simplify(F_ser[2])
checks["h2_coefficient_is_minus_1_over_27"] = bool(sp.simplify(c2 + sp.Rational(1, 27)) == 0)
checks["h2_coefficient_sqrt_free"] = bool(c2.is_rational)
checks["h2_denominator_support_is_3_only"] = denom_primes(c2) <= {3}

# (3) conversion to x = q-1: F(log(1+x)) to x^3; compare GSWZ eqn (2)
x = sp.symbols("x")
logx = sp.log(1 + x)
Fx = sp.series(F.subs(h, logx), x, 0, 4).removeO()
fx = [sp.simplify(Fx.coeff(x, k)) for k in range(4)]
checks["x2_matches_gswz_eqn2"] = bool(sp.simplify(fx[2] + sp.Rational(1, 27)) == 0)
checks["x3_matches_gswz_eqn2"] = bool(sp.simplify(fx[3] - sp.Rational(1, 27)) == 0)

# (4) THE GATE DEMO: a generic "fitted" perturbation of b2 breaks
# 3-integrality of the symmetrization.
delta = sp.Rational(1, 100)
b_fit = list(b)
b_fit[2] = b[2] + delta
Bf = sum(b_fit[k] * h**k for k in range(N + 1))
Ff = sp.expand(Bf * Bf.subs(h, -h))
c2f = sp.simplify(sp.Poly(Ff, h).all_coeffs()[::-1][2])
checks["gate_rejects_fitted_perturbation"] = not (denom_primes(c2f) <= {3})

print(json.dumps(checks, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_symmetrization_integrality_probe",
    "beans": ["qou-c0aw", "qou-1hlh"],
    "source": "GSWZ arXiv:2412.04241v2 eqns (1)-(2); library/arxiv-2412.04241v2/2412.04241v2.pdf",
    "checks": checks,
    "h2_coefficient": str(c2),
    "gate_demo_perturbation": str(delta),
    "gate_demo_broken_denominator_support": sorted(denom_primes(c2f)),
    "scope": "scope-(a): verifies printed GSWZ data + symmetrization structure at supported orders; independent Phi recomputation not claimed",
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_symmetrization_integrality.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
