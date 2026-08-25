"""Three-strand (3,k) torus tower: hyperbolic winding + rigid color winding
(T2b of the toroidal channel-interpolation follow-on, PR #3445; GAP-A-3).

T2 established that the two-strand (2,2k) torus-link tower is the forced
mu = 1/2 toroidal family at eta = 2 ln q. This probe extends to THREE
strands — the closures of (sigma_1 sigma_2)^k in B_3 are the (3,k) torus
links, and three strands is the Borromean/nucleon carrier arity — and asks
whether the tower picks a different toroidal family.

Answer: it picks the SAME forced mu = 1/2 elementary family, but on BOTH
loci of the channel-rotation table at once, adding one new COMPACT winding:

(1) EIGEN-FACTS (sympy exact, Hoefsmit seminormal): on the 2-dim (2,1)
    block, rho(sigma_1 sigma_2) has trace -1 and det 1 — eigenvalues are
    the primitive cube roots of unity omega^{+-1} — and
    (sigma_1 sigma_2)^3 = Id EXACTLY, INDEPENDENT OF q. The 1-dim channels
    give q^2 (trivial) and q^{-2} (sign). So the three-strand tower is
        x_k = W_+ q^{2k} + W_- q^{-2k} + W_0 * 2 cos(2 pi k / 3):
    the hyperbolic winding pair (carrying the substrate modulus) plus a
    q-RIGID compact winding of period 3 — a topological zeta_3 (color /
    triality) phase that does not flow with q.

(2) FACTORED ANNIHILATOR (sympy exact): the tower is annihilated by the
    order-4 product of the two degree flows,
        (E^2 + E + 1) o (E^2 - (q^2 + q^{-2}) E + 1),
    i.e. a 2 cosh(eta) flow at eta = 2 ln q times a 2 cos(theta) flow at
    theta = 2 pi / 3 (the E^2+E+1 factor is the theta = 2pi/3 Chebyshev
    flow since 2 cos(2pi/3) = -1).

(3) COMPACT-LOCUS ELEMENTARY FAMILY (mpmath, 50 dps, constants included):
    on the cut (Ferrers functions, type=2),
        P^{1/2}_{nu-1/2}(cos theta)  = sqrt(2/(pi sin theta)) * cos(nu theta)
        P^{-1/2}_{nu-1/2}(cos theta) = sqrt(2/(pi sin theta)) * sin(nu theta)/nu
    — the SAME mu = 1/2 family verified on cosh eta in T2, now on the
    compact locus x = cos theta (the bar-even/meson locus of the Askey
    channel table). The compact winding of (1) rides this family at
    theta = 2 pi / 3.

LEVEL-SELECTION READING ((a)-scoped, GAP-A-3): the three-strand level
family is indexed by the winding pair (k, k mod 3) — a hyperbolic winding
on the substrate torus (argument cosh eta, eta = 2 ln q, carries the
modulus) and a compact color winding on the zeta_3 circle (argument
cos theta, theta = 2pi/3, q-rigid / topological). Both ride the P1-forced
mu = 1/2 elementary Legendre family, one per locus row of the
channel-rotation table. Structural only: selects the level lattice for the
three-strand (Borromean/nucleon) carrier, produces no binding number,
nothing wired (Delta_lambda gate respected).
"""
import json
import os

import mpmath as mp
import sympy as sp

# ------------------------------------------------------ (1) eigen-facts
q = sp.symbols("q", positive=True)
h = q - 1 / q
a2 = h / (1 - q**(-4))
am2 = h / (1 - q**4)
b = sp.sqrt(a2 * am2 + 1)
s1 = sp.diag(q, -1 / q)
s2 = sp.Matrix([[am2, b], [b, a2]])
P = s1 * s2

trace_is_minus_one = sp.simplify(sp.radsimp(P.trace())) == -1
det_is_one = sp.simplify(P.det()) == 1
cube_is_id = sp.simplify(P**3) == sp.eye(2)
one_dim_channels_ok = (
    sp.simplify((q) * (q) - q**2) == 0
    and sp.simplify((-1 / q) * (-1 / q) - q**(-2)) == 0
)

# --------------------------------------------- (2) factored annihilator
j = sp.symbols("j", integer=True, positive=True)
Wp, Wm, W0 = sp.symbols("W_p W_m W_0", positive=True)
u = q**2


def x(m):
    return (Wp * u**m + Wm * u**(-m)
            + W0 * 2 * sp.cos(2 * sp.pi * m / sp.Integer(3)))


def L_hyp(f, m):
    """E^2 - (u + 1/u) E + 1 applied at m."""
    return f(m + 2) - (u + 1 / u) * f(m + 1) + f(m)


def L_cpt_of_seq(g, m):
    """E^2 + E + 1 applied at m (2 cos(2pi/3) = -1)."""
    return g(m + 2) + g(m + 1) + g(m)


annihilator_ok = sp.simplify(sp.expand_trig(
    L_cpt_of_seq(lambda m: L_hyp(x, m), j))) == 0
cos_flow_id = sp.simplify(2 * sp.cos(2 * sp.pi / 3) + 1) == 0

# ------------------------------------- (3) compact-locus elementary family
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
half = mp.mpf(1) / 2
tol = mp.mpf("1e-40")
CPTS = [(mp.mpf("1"), mp.mpf("0.9")), (mp.mpf("2.4"), mp.mpf("2.0944")),
        (mp.mpf("4"), mp.mpf("0.5"))]
cpt_plus_ok = all(
    abs(mp.legenp(nu - half, half, mp.cos(t), type=2)
        - mp.sqrt(2 / (mp.pi * mp.sin(t))) * mp.cos(nu * t)) < tol
    for nu, t in CPTS)
cpt_minus_ok = all(
    abs(mp.legenp(nu - half, -half, mp.cos(t), type=2)
        - mp.sqrt(2 / (mp.pi * mp.sin(t))) * mp.sin(nu * t) / nu) < tol
    for nu, t in CPTS)

assertions = {
    "block21_trace_minus_one": bool(trace_is_minus_one),
    "block21_det_one": bool(det_is_one),
    "block21_cube_identity_q_independent": bool(cube_is_id),
    "one_dim_channels_q2_qm2": bool(one_dim_channels_ok),
    "tower_annihilated_by_factored_order4": bool(annihilator_ok),
    "compact_factor_is_theta_2pi3_flow": bool(cos_flow_id),
    "compact_locus_elementary_plus_half": bool(cpt_plus_ok),
    "compact_locus_elementary_minus_half": bool(cpt_minus_ok),
}

verdict = (
    "THREE STRANDS ADD ONE RIGID COMPACT (COLOR) WINDING, SAME FORCED "
    "FAMILY: on the (2,1) Hoefsmit block rho(sigma_1 sigma_2) has trace -1, "
    "det 1 and cubes to the identity EXACTLY AND q-INDEPENDENTLY, so the "
    "(3,k) torus-link tower is x_k = W+ q^{2k} + W- q^{-2k} + W0 2cos(2pi "
    "k/3): the T2 hyperbolic winding pair (substrate modulus, eta = 2 ln q) "
    "plus a topological zeta_3 winding of period 3 that does not flow with "
    "q. The tower is annihilated by the factored order-4 operator (E^2+E+1)"
    "(E^2-(q^2+q^-2)E+1), and the compact channel rides the SAME forced "
    "mu = 1/2 elementary Legendre family on the compact locus cos theta "
    "(verified with constants at 50 dps) — one family, two locus rows of "
    "the channel-rotation table. LEVEL SELECTION (GAP-A-3 candidate, "
    "(a)-scoped): three-strand (Borromean/nucleon) levels are indexed by "
    "the winding pair (k, k mod 3) — hyperbolic + color/triality. "
    "Structural only; no binding number; nothing wired."
)

witness = {
    "computation": "toroidal_level_selection_three_strand_probe",
    "description": (
        "T2b/GAP-A-3: the (3,k) torus-link tower adds exactly one q-rigid "
        "compact zeta_3 (color) winding to the T2 hyperbolic pair; both ride "
        "the forced mu = 1/2 elementary Legendre family, on the non-compact "
        "(cosh eta) and compact (cos theta) loci respectively."
    ),
    "discipline": "no fit; sympy exact + mpmath 50 dps; (a)-scoped; no observable touched.",
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {
        "block21_sigma1sigma2": "trace -1, det 1, cube = Id (q-independent) -> eigenvalues omega, omega^-1",
        "tower_form": "x_k = W+ q^{2k} + W- q^{-2k} + W0 * 2 cos(2 pi k/3)",
        "winding_lattice": "(k, k mod 3): hyperbolic (modulus-carrying) x compact zeta_3 (q-rigid, color/triality)",
        "torus_link_family": "(3,k): k=1 trefoil-family ground level; three-strand = Borromean/nucleon carrier arity",
        "related": [
            "toroidal-level-selection-hopf-probe.witness.json (two-strand T2)",
            "prop:hoefsmit-toroidal-ladder-locus (forced mu = 1/2)",
        ],
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy+mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__),
                   "toroidal-level-selection-three-strand-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

for kk, v in assertions.items():
    print(f"  {kk}: {'PASS' if v else 'FAIL'}")
print(f"\nallPassed: {witness['allPassed']}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
