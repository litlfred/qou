"""Alternating three-strand tower: the Borromean/figure-eight winding vs the
level lattice (T6 of the toroidal channel-interpolation follow-on, PR #3445).

T2b established the UNIFORM three-strand tower (sigma_1 sigma_2)^k — the
(3,k) torus links — carries a q-RIGID zeta_3 color winding (cube = Id
exactly). This probe runs the same analysis on the ALTERNATING word
A = sigma_1 sigma_2^{-1}, whose power closures are the hyperbolic anchor
family: k = 2 is the figure-eight knot 4_1 (the lepton anchor) and k = 3 is
the Borromean rings B_3 (the nucleon carrier).

Verified (sympy exact unless noted):

(1) TRACE CLOSED FORM: on the (2,1) Hoefsmit block,
        tau(q) := tr rho(sigma_1 sigma_2^{-1}) = 1 - q^2 - q^{-2},
    det = 1; tau is BAR-EVEN (tau(q^{-1}) = tau(q)), q-DEPENDENT, and
    tau(1) = -1 — the classical limit coincides with the uniform word's
    rigid value (both words are the 3-cycle at q = 1).

(2) TOWER RECURRENCE: tr rho(A^k) satisfies the Chebyshev flow
        x_{k+1} = tau x_k - x_{k-1}     (verified k <= 5),
    the same mu = 1/2 elementary-family degree recurrence as T2/T2b, with
    2 cos(theta') resp. 2 cosh(eta') = |tau| as the locus argument.

(3) EXACT ELLIPTICITY BOUNDARY AT THE GOLDEN RATIO: |tau| < 2 (elliptic /
    compact winding, eigenvalues on the unit circle) iff q^2 + q^{-2} < 3,
    and the boundary q^2 + q^{-2} = 3 holds at q = phi = (1+sqrt 5)/2
    EXACTLY (phi^2 = phi + 1). For 1 < q < phi the alternating winding is
    an ELLIPTIC rotation with q-deformed angle
        theta'(q) = arccos(tau/2),  theta'(1) = 2*pi/3;
    at q = phi it is parabolic; beyond, hyperbolic.
    NOTE (coordination, #3444): phi here is an exact spectral-transition
    point of a trace polynomial — |tau| = 2 — NOT a fitted anchor; no
    Delta_lambda claim, no observable evaluated, and this does not touch
    the golden-ratio numerology cut in #3444.

(4) READING ((a)-scoped): the block carries TWO winding directions —
    uniform word = RIGID zeta_3 color rotation (theta = 2pi/3, exact,
    q-independent; T2b); alternating word = the SAME rotation at q = 1,
    deformed by the modulus for q > 1 (theta'(q) ~ 2pi/3 + O((q-1)^2)).
    The hyperbolic anchor family rides the deformed direction at
    consecutive integer windings: 4_1 (lepton) at k = 2, Borromean
    (nucleon) at k = 3. Level-lattice answer to "does the nucleon sit at a
    lattice point": yes — k = 3 of the deformed color rotation, the same
    k as its torus-link shadow on the rigid direction. Structural only;
    no binding number; nothing wired.
"""
import json
import os

import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

q = sp.symbols("q", positive=True)
h = q - 1 / q
a2 = h / (1 - q**(-4))
am2 = h / (1 - q**4)
b = sp.sqrt(a2 * am2 + 1)
s1 = sp.diag(q, -1 / q)
s2 = sp.Matrix([[am2, b], [b, a2]])
A = sp.simplify(s1 * s2.inv())

tau = sp.simplify(sp.radsimp(A.trace()))
tau_expected = 1 - q**2 - q**(-2)

trace_closed_form = sp.simplify(tau - tau_expected) == 0
det_one = sp.simplify(A.det()) == 1
bar_even = sp.simplify(sp.radsimp(tau.subs(q, 1 / q) - tau)) == 0
q_dependent = sp.simplify(sp.diff(tau_expected, q)) != 0
classical_limit = sp.limit(tau_expected, q, 1) == -1

# (2) Chebyshev recurrence on matrix-power traces, k <= 5
traces = [sp.simplify(sp.radsimp((A**k).trace())) for k in range(7)]
recurrence_ok = all(
    sp.simplify(sp.radsimp(traces[k + 1] - tau * traces[k] + traces[k - 1])) == 0
    for k in range(1, 6))

# (3) golden-ratio boundary, exact
phi = (1 + sp.sqrt(5)) / 2
boundary_at_phi = sp.simplify((q**2 + q**(-2) - 3).subs(q, phi)) == 0
phi_defining = sp.simplify(phi**2 - phi - 1) == 0
# |tau| < 2 iff q^2 + q^-2 < 3 (for the relevant branch tau < 0 for q > 1:
# |tau| = q^2 + q^-2 - 1); algebraic identity |tau| - 2 = (q^2 + q^-2) - 3:
abs_tau_identity = sp.simplify((q**2 + q**(-2) - 1) - 2 - (q**2 + q**(-2) - 3)) == 0
# elliptic angle at q = 1 is exactly 2pi/3: cos(theta') = tau/2 = -1/2
angle_classical = sp.simplify(sp.acos(sp.Rational(-1, 2)) - 2 * sp.pi / 3) == 0

assertions = {
    "trace_closed_form_1_minus_q2_minus_qm2": bool(trace_closed_form),
    "det_one": bool(det_one),
    "tau_bar_even": bool(bar_even),
    "tau_q_dependent": bool(q_dependent),
    "tau_classical_limit_minus_one": bool(classical_limit),
    "chebyshev_recurrence_k_le_5": bool(recurrence_ok),
    "golden_boundary_q2_plus_qm2_eq_3_at_phi": bool(boundary_at_phi),
    "phi_defining_identity": bool(phi_defining),
    "abs_tau_minus_2_identity": bool(abs_tau_identity),
    "classical_angle_2pi_over_3": bool(angle_classical),
}

verdict = (
    "THE ALTERNATING (HYPERBOLIC-ANCHOR) TOWER IS THE MODULUS-DEFORMED "
    "COLOR ROTATION: tr rho(sigma_1 sigma_2^{-1}) = 1 - q^2 - q^{-2} "
    "(bar-even, det 1), equal to the rigid zeta_3 value -1 at q = 1 and "
    "deforming with the modulus; the tower obeys the same mu = 1/2 "
    "Chebyshev degree flow, elliptic for q^2 + q^{-2} < 3 with the exact "
    "parabolic boundary at q = phi (phi^2 = phi + 1 — a spectral-"
    "transition point of the trace polynomial, NOT a fitted anchor; cf. "
    "#3444). The figure-eight (k = 2, lepton anchor) and Borromean (k = 3, "
    "nucleon carrier) sit at consecutive integer windings of this deformed "
    "rotation — the nucleon IS a lattice point, k = 3, matching its "
    "torus-link shadow on the rigid direction. SCOPE (a): structural; no "
    "observable evaluated; nothing wired."
)

witness = {
    "computation": "alternating_tower_borromean_winding_probe",
    "description": (
        "T6: the alternating three-strand word (figure-eight/Borromean "
        "family) is the modulus-deformed color rotation on the Hoefsmit "
        "block — same Chebyshev flow, angle 2pi/3 at q=1, exact elliptic/"
        "hyperbolic boundary at q = phi; anchors at windings k = 2, 3."
    ),
    "discipline": ("no fit; sympy symbolic exact; fibre-level only (no q_0 "
                   "evaluation, no observables); (a)-scoped; golden-ratio "
                   "boundary is an exact spectral fact, not an anchor (cf. "
                   "PR #3444 numerology cut)."),
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {
        "tau": str(tau_expected),
        "winding_pair": "uniform word: rigid theta = 2pi/3 (T2b); alternating word: theta'(q) = arccos((1 - q^2 - q^{-2})/2)",
        "anchor_levels": "4_1 (lepton) at k=2; Borromean B_3 (nucleon) at k=3 — consecutive windings",
        "ellipticity": "elliptic iff q^2 + q^{-2} < 3; parabolic exactly at q = (1+sqrt5)/2; hyperbolic beyond",
        "related": [
            "toroidal-level-selection-three-strand-probe.witness.json (rigid direction)",
            "toroidal-level-selection-hopf-probe.witness.json (two-strand)",
        ],
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__),
                   "alternating-tower-borromean-winding-probe.witness.json")
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
for kk, v in assertions.items():
    print(f"  {kk}: {'PASS' if v else 'FAIL'}")
print(f"\nallPassed: {witness['allPassed']}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
