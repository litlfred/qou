"""Gauss linking rate of a slope-z torus pair = the reeb-flow g (D3 of the
full-derivation program; discharges the chain's residual postulate down to
a units convention).

The reeb-flow derivation chain (audit 2026-07-06-reeb-flow SS2d/SS2e) has
ONE residual postulate: "the Reeb linking amplitude of the pn bond is the
CWF (unit-tangent, arc-length) functional evaluated on the channel-space
direction (1, z)". This probe derives that functional's value as plain
linking geometry:

(1) SYMBOLIC (exact). On a flat torus with cycle circumferences
    (2*pi*R direct, 2*pi*r exchange), the (1, n) geodesic has metric slope
    z = n r / R and period arc length L = 2*pi*R*sqrt(1 + z^2). Its
    parallel push-off links it Lk = n times (surface framing of a (1,n)
    torus curve: Lk = 1*n). Therefore the LINKING RATE PER UNIT ARC
    LENGTH, measured in exchange-cycle units (2*pi*r),
        Lk * (2*pi*r) / L = n r / (R*sqrt(1+z^2)) = z / sqrt(1+z^2) = g,
    EXACTLY and INDEPENDENTLY of (R, r): the normalized exchange component
    sin(theta) is not a postulated functional — it IS the linking number
    per exchange-normalized arc length of a slope-z curve pair.

(2) NUMERIC (Gauss integral). The topological input Lk((1,n) cable pair)
    = n is verified by direct evaluation of the Gauss double integral for
    radially-offset (1, n) cables on an embedded torus in R^3 (n = 1, 2, 3;
    R = 3, r = 1, offset 0.15), periodic Riemann sum (spectrally
    convergent for smooth periodic integrands).

CONSEQUENCE (recorded, (a)-scoped). Composed with the sibling results
(tangent = Markov weight, SS2d; z = canonical Markov parameter, D1), the
g = sin(theta) magnitude is now DERIVED as: canonical Markov parameter ->
channel slope -> linking rate. The one remaining assumption shrinks from a
functional identification to a UNITS CONVENTION: the bond's arc length is
measured in exchange-cycle units. The 2H law's remaining opens are then
exactly (i) that convention, (ii) the deformation choice (D1), and
(iii) E_unit. Nothing wired; no observable evaluated.
"""
import json
import os

import numpy as np
import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

# ------------------------------------------------------- (1) symbolic
R_, r_, n_ = sp.symbols("R r n", positive=True)
z_ = n_ * r_ / R_
L_ = 2 * sp.pi * R_ * sp.sqrt(1 + z_**2)
rate = n_ * (2 * sp.pi * r_) / L_
g_ = z_ / sp.sqrt(1 + z_**2)
rate_eq_g = sp.simplify(rate - g_) == 0
# geometry-independence: the rate depends on (R, r, n) only through z
zz = sp.symbols("zz", positive=True)
rate_in_z = sp.simplify(rate.subs(n_, zz * R_ / r_))
geom_independent = sp.simplify(rate_in_z - zz / sp.sqrt(1 + zz**2)) == 0

# ------------------------------------------------------- (2) numeric Gauss
def torus_curve(t, R, r, n):
    x = (R + r * np.cos(n * t)) * np.cos(t)
    y = (R + r * np.cos(n * t)) * np.sin(t)
    z = r * np.sin(n * t)
    return np.stack([x, y, z], axis=-1)


def torus_curve_deriv(t, R, r, n):
    c, s = np.cos(t), np.sin(t)
    cn, sn = np.cos(n * t), np.sin(n * t)
    rho = R + r * cn
    drho = -r * n * sn
    dx = drho * c - rho * s
    dy = drho * s + rho * c
    dz = r * n * cn
    return np.stack([dx, dy, dz], axis=-1)


def gauss_linking(R, r1, r2, n, N=600):
    t = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    g1, d1 = torus_curve(t, R, r1, n), torus_curve_deriv(t, R, r1, n)
    g2, d2 = torus_curve(t, R, r2, n), torus_curve_deriv(t, R, r2, n)
    diff = g1[:, None, :] - g2[None, :, :]
    dist3 = np.linalg.norm(diff, axis=-1) ** 3
    cross = np.cross(d1[:, None, :], d2[None, :, :])
    integrand = np.einsum("ijk,ijk->ij", diff, cross) / dist3
    return integrand.sum() * (2 * np.pi / N) ** 2 / (4 * np.pi)


R0, r1, r2 = 3.0, 1.0, 1.15
# Orientation convention: with the parametrization above (meridian phase
# +n*t against the right-handed longitude), the signed Gauss integral of
# the co-oriented cable pair is -n; the magnitude |Lk| = n is the
# topological input used by the rate identity (which is orientation-blind:
# the physical rate is |Lk| per unit length).
numeric = {}
numeric_ok = True
for n in (1, 2, 3):
    lk = gauss_linking(R0, r1, r2, n)
    ok = abs(abs(lk) - n) < 1e-3
    numeric_ok = numeric_ok and ok
    numeric[f"Lk_(1,{n})_cable_pair"] = {"gauss_integral_signed": f"{lk:.8f}",
                                         "expected_abs": n, "ok": bool(ok)}

assertions = {
    "linking_rate_equals_g_exact": bool(rate_eq_g),
    "rate_geometry_independent_in_z": bool(geom_independent),
    "gauss_integral_abs_lk_eq_n_n123": bool(numeric_ok),
}

verdict = (
    "THE g = sin(theta) MAGNITUDE IS LINKING GEOMETRY (derived): for a "
    "slope-z curve pair on a torus, linking number per unit arc length in "
    "exchange-cycle units equals z/sqrt(1+z^2) = g EXACTLY, independent of "
    "the torus geometry (symbolic), with the topological input Lk = n "
    "verified by direct Gauss integration (n = 1,2,3 to <1e-3). Composed "
    "with SS2d (tangent = Markov weight) and D1 (z = canonical Markov "
    "parameter), the reeb-flow chain's residual CWF postulate REDUCES TO A "
    "UNITS CONVENTION (arc length in exchange-cycle units). Remaining 2H "
    "opens: that convention, the D1 deformation choice, and E_unit. "
    "SCOPE (a): structural; nothing wired; no observable evaluated."
)

witness = {
    "computation": "gauss_linking_channel_slope_probe",
    "description": (
        "D3: the CWF channel postulate discharged to a units convention — "
        "linking rate of a slope-z torus pair equals g = z/sqrt(1+z^2) "
        "exactly (symbolic, geometry-independent), Gauss-integral "
        "verification of the Lk = n input."
    ),
    "discipline": ("no fit; sympy exact + numpy Gauss quadrature (periodic "
                   "Riemann, spectral); (a)-scoped; no q_0, no observables."),
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {
        "symbolic_identity": "Lk*(2*pi*r)/L = z/sqrt(1+z^2) = g, any (R, r)",
        "numeric_gauss": numeric,
        "postulate_reduction": (
            "linking amplitude = CWF functional on (1, z)  ==>  arc length "
            "measured in exchange-cycle units (normalization convention)"
        ),
        "related": [
            "docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md SS2d/SS2e",
            "deuteron-tower-fusion-frame-probe.witness.json (D1: z canonical)",
        ],
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy+numpy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "gauss-linking-channel-slope-probe.witness.json")
# Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
# `os.replace` it into position. `open(..., "w")` TRUNCATES before the
# dump runs, so any exception in between leaves the committed witness
# empty or partial -- the shape that emptied 22 witnesses to zero bytes
# in one `producer_importability_audit` run. `os.replace` is atomic on
# POSIX within a filesystem, hence a SIBLING temp file.
_wpath_sidu = out
_wtmp_sidu = str(_wpath_sidu) + ".tmp"
with open(_wtmp_sidu, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

_os_sidu.replace(_wtmp_sidu, _wpath_sidu)
for kk, val in assertions.items():
    print(f"  {kk}: {'PASS' if val else 'FAIL'}")
for k2, v2 in numeric.items():
    print(f"    {k2}: {v2['gauss_integral_signed']} (expect |Lk| = {v2['expected_abs']})")
print(f"\nallPassed: {witness['allPassed']}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
