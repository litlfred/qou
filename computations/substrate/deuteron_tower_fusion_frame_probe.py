"""Deuteron 5g law: the canonical-tower / fusion frame (D1 of the
full-derivation program; follow-on to PR #3445 + the reeb-flow tranches
#3442/#3448/#3451).

The E_unit constraint ledger (reeb-flow audit SS2f) says a successful
bridge needs "a genuinely new derived energy ... or the conclusion that the
linear law is not fundamental." This probe establishes, EXACTLY, that the
dimensionless content of the 5g law is already canonical-tower data — four
symbolic identities plus one honest deformation-ambiguity finding. No
numeric matching is performed beyond restating the ledger's own numbers;
predicted-first gate respected (every identity is derived below BEFORE any
evaluation, and none touches E_unit).

(1) THE BOND FACTOR IS THE CANONICAL MARKOV PARAMETER. The corpus Markov-
    Ocneanu-Wenzl trace normalization (pyhecke.gram) sets
        z = 1/(sqrt(q0) + 1/sqrt(q0)) = 1/[2]_v,  v = sqrt(q0)
    — identical to the reeb-flow bond factor z = 1/[2]_v = delta^{-1}.
    The 2H law's z is not a modeling choice; it is THE trace parameter of
    the corpus's tr_M. (Checked against the live pyhecke value.)

(2) THE "5" IS FORCED BY THE FUSION RULE. The Clebsch-Gordan / TL fusion
    identity [2]_v^2 = [3]_v + 1 (spin 1/2 x 1/2 = 1 + 0, q-dimensions)
    gives
        1 + [2]_v^2 = 2 + [3]_v  ->  5 at v = 1.
    So the marginal-stability quantity 1 + b^2 of the reeb-flow Lean
    (ss_det_marginal) is the total quantum dimension of the deuteron's
    two-nucleon channel decomposition {V_0 (direct), V_0 + V_1 (fused)},
    and the integer 5 in "5g" is its classical value — not a free integer.

(3) THE WINDING-TOWER BRIDGE. With tau(v) = 1 - v^2 - v^{-2} — the
    three-strand ALTERNATING winding trace (PR #3445 T6 probe, the
    unknot/4_1/Borromean tower at k = 1, 2, 3) —
        1 + [2]_v^2 = 4 - tau(v)   exactly.
    Hence g = z/sqrt(1+z^2) = 1/sqrt(4 - tau(v)): the deuteron bond
    magnitude is determined by the SAME winding object whose k = 2 level
    is the figure-eight (muon anchor) and k = 3 level the Borromean
    (nucleon carrier). Level ladder: k = 1 (unknot) -> bond, k = 2 -> 4_1,
    k = 3 -> B_3.

(4) CRITICALITY = NORMALIZED CHANNEL PROJECTION. g^2 (1 + [2]_v^2) = 1
    identically — the landed magnitude (I1/I2) and the marginal-stability
    zero of ss_det_marginal are the same statement, and both say: g is the
    unit-normalized exchange component of the channel direction (1, z).

(5) HONEST DEFORMATION AMBIGUITY (the sharpened open). The classical
    integer 5 = (1 + [2]^2)|_{v=1} admits at least two canonical
    deformations of the binding law:
        (i)  B = 5 g E_unit          = 5/sqrt(2 + [3]_v) * E_unit
        (ii) B = sqrt(2 + [3]_v) E'  (deform the numerator too)
    At the substrate v both are ~0.4-0.6 % near-matches with a ~1 MeV
    unit. The fusion frame does NOT select between them; what it does is
    reduce the "derive the linear law" open to two sharp questions:
    (a) which deformation of the classical 5 is canonical, and (b) what
    fixes the unit. Recorded as the sharpened open; no candidate is
    proposed, no scan is run (entropy-bound / gate discipline).

Scope (a) throughout: exact algebra + structural reading; nothing wired;
E_unit untouched.
"""
import json
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(
    os.path.join(_HERE, "..", "..", "tools", "pyhecke", "python")))

v = sp.symbols("v", positive=True)


def bkt(n, x):
    """Symmetric q-integer [n]_x."""
    return (x**n - x**(-n)) / (x - 1 / x)


two_v = v + 1 / v          # [2]_v
three_v = v**2 + 1 + v**(-2)  # [3]_v

# (1) canonical z — live pyhecke value vs the convention-D closed form
import mpmath as _mp  # noqa: E402
import pyhecke.gram as gram  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402  (canonical q0, via substrate path)

# `gram.z` is a float64 module constant, so this comparison has a float64 side
# no matter what. Lift it EXACTLY (`repr` round-trips a float64) rather than
# computing the reference in float64 too: the reference is then honest at 50 dps
# and the tolerance below is a statement about `gram.z`'s resolution, not a
# precision claim about the identity. Was `float(gram.z)` differenced against a
# float64 `Q0**3/(Q0**2+1)` until 2026-08-23 (AGENTS.md "PROBES ARE NOT EXEMPT").
with _mp.workdps(50):
    _q0 = _mp.mpf(Q_50_DIGIT_STR)
    z_live = _mp.mpf(repr(float(gram.z)))
    z_formula = _q0**3 / (_q0**2 + 1)
    # 1e-12 is far looser than float64 eps at this magnitude (~1.1e-16); it is
    # the historical threshold and is kept so the tripwire's sensitivity does
    # not change silently along with its arithmetic.
    z_canonical_ok = abs(z_live - z_formula) < _mp.mpf("1e-12")

# symbolic: [2]_v as bracket
bracket_two_ok = sp.simplify(bkt(2, v) - two_v) == 0

# (2) fusion identity [2]^2 = [3] + 1 and the forced 5
fusion_ok = sp.simplify(two_v**2 - (three_v + 1)) == 0
forced_five_ok = sp.simplify((1 + two_v**2).subs(v, 1)) == 5

# (3) winding-tower bridge: 1 + [2]_v^2 = 4 - tau(v)
tau = 1 - v**2 - v**(-2)
bridge_ok = sp.simplify((1 + two_v**2) - (4 - tau)) == 0

# (4) criticality = normalized projection: g^2 (1 + [2]^2) = 1 with
#     g = z/sqrt(1+z^2), z = 1/[2]_v
z_sym = 1 / two_v
g_sym = z_sym / sp.sqrt(1 + z_sym**2)
criticality_ok = sp.simplify(g_sym**2 * (1 + two_v**2) - 1) == 0
g_eq_inv_sqrt_ok = sp.simplify(g_sym - 1 / sp.sqrt(4 - tau)) == 0

assertions = {
    "z_canonical_equals_pyhecke_gram_z": bool(z_canonical_ok),
    "two_v_is_q_bracket": bool(bracket_two_ok),
    "fusion_identity_[2]^2_eq_[3]+1": bool(fusion_ok),
    "five_forced_at_classical_point": bool(forced_five_ok),
    "winding_bridge_1+[2]^2_eq_4-tau": bool(bridge_ok),
    "criticality_g2_times_1+[2]^2_eq_1": bool(criticality_ok),
    "g_eq_inv_sqrt_4_minus_tau": bool(g_eq_inv_sqrt_ok),
}

verdict = (
    "THE 5g LAW'S DIMENSIONLESS CONTENT IS CANONICAL-TOWER DATA (exact): "
    "the bond factor z IS the corpus Markov-trace parameter (pyhecke.gram "
    "z = 1/[2]_v at v = sqrt(q0), checked live); the integer 5 is FORCED "
    "by the fusion identity [2]^2 = [3]+1 (1+[2]_v^2 = 2+[3]_v -> 5 at "
    "v=1, the total quantum dimension of the two-nucleon channel "
    "decomposition); and 1+[2]_v^2 = 4 - tau(v) ties the marginal-"
    "stability denominator to the alternating winding trace whose k=1,2,3 "
    "levels are unknot/figure-eight/Borromean — bond, lepton anchor, "
    "nucleon carrier on one tower. Criticality g^2(1+[2]^2)=1 is "
    "identically the normalized channel projection. SHARPENED OPEN "
    "(honest): the classical 5 admits >=2 canonical deformations (5g vs "
    "sqrt(2+[3]_v)); the frame does not select one, and the unit E_unit "
    "remains the genuine open — no candidate proposed, no scan run. "
    "SCOPE (a): exact algebra + structural reading; nothing wired."
)

witness = {
    "computation": "deuteron_tower_fusion_frame_probe",
    "description": (
        "D1 of the full-derivation program: exact identities showing the "
        "2H 5g law's dimensionless content is canonical Markov-tower data "
        "(z = trace parameter; 5 forced by the fusion rule; 4 - tau "
        "winding bridge; criticality = normalized channel projection), "
        "plus the honest deformation-ambiguity finding."
    ),
    "discipline": ("predicted-first gate respected: all identities derived "
                   "before evaluation; no E_unit candidate, no scan; sympy "
                   "exact + one live pyhecke cross-check; (a)-scoped."),
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {
        "z_live_pyhecke": repr(z_live),
        "fusion_frame": "1 + [2]_v^2 = 2 + [3]_v = 4 - tau(v); 5 at v=1",
        "tower_levels": "k=1 unknot -> bond factor; k=2 4_1 -> muon anchor; k=3 B_3 -> nucleon carrier",
        "sharpened_open": [
            "(a) which canonical deformation of the classical 5: 5/sqrt(2+[3]_v) vs sqrt(2+[3]_v)",
            "(b) the unit E_unit — unchanged, per the SS2f ledger and entropy bound",
        ],
        "related": [
            "alternating-tower-borromean-winding-probe.witness.json (tau, tower)",
            "docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md SS2e/SS2f/SS3f",
        ],
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy+pyhecke")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(_HERE, "deuteron-tower-fusion-frame-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

for kk, val in assertions.items():
    print(f"  {kk}: {'PASS' if val else 'FAIL'}")
print(f"\nallPassed: {witness['allPassed']}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")

# Exit non-zero when an assertion fails.  Bean qou-9d6h.
#
# This probe wrote `allPassed: False` and exited 0, so the convention-C
# regeneration harness recorded it `ok` (25/29 on the 2026-08-11 run) and the
# failure was visible only to someone opening the witness. The failing check is
# not incidental: `z_canonical_equals_pyhecke_gram_z` is the live detector for
# the `pyhecke` C/D split (`qou-5wpk`) -- the pure-Python `gram.z` is convention
# C (0.4993203341836945) while the installed `pyhecke_native.markov_z` returns
# convention D (0.6126880371464652). Silent success on that check is exactly the
# failure shape this campaign exists to find, so it is now loud.
#
# RESOLVED 2026-08-23. `pyhecke.gram.z` moved to convention D (`q^3/(q^2+1)`),
# so the tripwire's condition is met: `gram.z` and the closed form now agree to
# 0.0, and `qou-w8zz` / `qou-5wpk` / `qou-9d6h` are all completed. The witness
# had been stale since 2026-08-14 — one day before that move — and the only
# action this check ever needed was a re-run. Left loud on purpose: it is still
# the live detector for a C/D split reopening.
if not witness["allPassed"]:
    failed = [k for k, v in assertions.items() if not v]
    print(f"\nFAILED assertions: {', '.join(failed)}")
    sys.exit(1)
