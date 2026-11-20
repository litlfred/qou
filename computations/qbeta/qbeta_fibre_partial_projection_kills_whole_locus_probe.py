#!/usr/bin/env python3
"""qbeta_fibre_partial_projection_kills_whole_locus_probe.py — under the PARTIAL
projection the reality condition excludes the WHOLE fibre locus, not merely its
root-of-unity sublocus.

🛑 THIS PROBE'S HEADLINE IS WITHDRAWN — OWNER RULING 2026-09-06:
   "Does not need to be real in fiber."

   The title claim is FALSE under the ruling. The whole locus is excluded only
   IF Q_beta must be real on the fibre, and it need not be. Reality is an
   ARCHIMEDEAN constraint on the evaluation at q_0, not a fibre condition, so
   there is no reality condition on |q| = 1 and the locus is NOT excluded.

   The arithmetic is untouched and all five assertions still hold as stated:
   the condition (WHEN imposed) is one on every point of the circle, its
   solution set is exactly {0, pi/3, pi, 5pi/3}, the dense scan finds no fifth
   zero, and all four are degenerate. The probe's own closing paragraph named
   this assumption as load-bearing and flagged that the fibre-vs-observable
   banner puts Im(q) unconstrained at fibre level. The ruling resolves that
   flag AGAINST the premise.

   Net: route 5's fibre locus |q| = 1 is INTACT, minus 4 degenerate points.
   Nothing selects N there. #6755's 1/111 is neither selected nor excluded.
   See the audit doc's RETRACTION section.

Bean `qou-cds1` / `qou-pdix` route 5.  Scope-(a), conditional on the reality
assumption route 5's N-selection already rests on (stated at the bottom).

## 🛑 This STRENGTHENS my own #6889, whose scope line was too weak

#6889 established that on `|q| = 1` the block's partial projection makes
`Q_beta` real iff

    Im[q^2 - q]  =  sin(2 phi) - sin(phi)  =  sin(phi) (2 cos(phi) - 1)  =  0

and that the three non-pole solutions `{pi/3, pi, 5pi/3}` are each degenerate.
It then wrote, as the scope caveat:

    "This does not close route 5.  |q| = 1 is a great deal more than its roots
     of unity"

**That sentence is true about the LOCUS and irrelevant to the ARGUMENT.**  The
displayed equation is a condition on every point of `|q| = 1`, not a condition
imposed only at roots of unity.  Its solution set on `[0, 2pi)` is exactly

    {0, pi/3, pi, 5pi/3}

— four points, all of which happen to be roots of unity.  So the "great deal
more" is already excluded, by reality, before degeneracy is mentioned.  The
non-rational phases were never open under the partial projection; I described
them as open.

## What that gives — a dichotomy, and neither branch predicts anything

    PARTIAL projection  ->  reality leaves 4 points, ALL degenerate
                            ==> the entire fibre locus is excluded
    FULL projection     ->  |Delta(net) * E_0| is real for every q
                            ==> no condition at all, nothing selected

So route 5's N-selection mechanism yields **no prediction under either reading**
of the projection.  That is a scope-(a) negative on the MECHANISM.  It is not a
refutation of route 5's underlying idea (a fibre-level Habiro element evaluated
archimedeanly), which this says nothing about.

The fourth point `phi = 0` is `q = 1`, degenerate twice over: `h = q - 1/q = 0`
kills `Delta(net)`, and `E_0 = m_e/(q(q-1))` has a pole there.  #6889 dismissed
it in one word as "the pole"; both facts are checked here.

## Precision

sympy exact for the solve and the factorisation; mpmath at 50 dps for the dense
scan and the degeneracy evaluations.  `q_0` from `q_at` (proton pin).  No
float64: no `float(`, no `statistics`, no `math.`.
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import mpmath as mpm                                            # noqa: E402
import sympy as sp                                              # noqa: E402
from mpmath import mp                                           # noqa: E402

from q_parameter import q_at                                    # noqa: E402

mp.dps = 50

RESULTS: list[dict] = []


def record(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


# ---------------------------------------------------------------- symbolic ---
phi = sp.symbols("phi", real=True)
q_s = sp.exp(sp.I * phi)

# The block: Q_beta = |Delta(net)| * E_0, Delta(net) = h(h-2)/2, h = q - 1/q,
# E_0 = m_e/(q(q-1)).  |Delta(net)| is real by construction, so the partial
# projection is real iff 1/(q(q-1)) is, iff Im[q(q-1)] = Im[q^2 - q] = 0.
im_expr = sp.simplify(sp.im(sp.expand_complex(q_s**2 - q_s)))
factored = sp.factor(sp.simplify(sp.expand_trig(im_expr)))

# ---------------------------------------------------------- 1. solution set ---
sols = sp.solveset(im_expr, phi, sp.Interval.Ropen(0, 2 * sp.pi))
sols_set = set(sp.simplify(s) for s in sols)
expected = {sp.Integer(0), sp.pi / 3, sp.pi, 5 * sp.pi / 3}
record(
    "reality_is_a_condition_on_the_WHOLE_locus_with_exactly_four_solutions",
    sols_set == expected,
    f"Im[q^2-q] factors as {factored}; solveset on [0,2pi) gives "
    f"{sorted(sols_set, key=lambda z: float(sp.N(z)))} — exactly the four "
    f"expected {sorted(expected, key=lambda z: float(sp.N(z)))}. This is a "
    f"condition at EVERY point of |q|=1, not one imposed only at roots of "
    f"unity, so the non-rational phases are excluded by reality itself.",
)

# ------------------------------------------------- 2. dense numerical scan ---
# Independent of sympy: scan the circle and confirm no fifth zero hides between
# the four. Sample densely and check the sign pattern / minima locations.
def im_num(p):
    return mpm.sin(2 * p) - mpm.sin(p)


N_SCAN = 20000
two_pi = 2 * mp.pi


def circ_dist(a, b):
    """Distance on the circle. phi = 0 and phi = 2*pi are the SAME point; a
    linear |a-b| calls them 2*pi apart and reports a spurious fifth zero."""
    d = abs(mpm.fmod(a - b, two_pi))
    return min(d, two_pi - d)


zeros_found = []
prev_p = mp.mpf(0)
prev_v = im_num(prev_p)
for i in range(1, N_SCAN + 1):
    p = two_pi * i / N_SCAN
    v = im_num(p)
    if prev_v == 0 or (prev_v < 0) != (v < 0):
        # bracket -> refine
        try:
            root = mpm.findroot(im_num, (prev_p, p), solver="bisect", tol=mp.mpf(10) ** (-45))
        except Exception:
            root = prev_p
        if all(circ_dist(root, z) > mp.mpf(10) ** (-20) for z in zeros_found):
            zeros_found.append(root)
    prev_p, prev_v = p, v

exp_num = [mp.mpf(0), mp.pi / 3, mp.pi, 5 * mp.pi / 3]
matched = len(zeros_found) == len(exp_num) and all(
    min(circ_dist(z, e) for e in exp_num) < mp.mpf(10) ** (-15) for z in zeros_found
)
record(
    "dense_scan_finds_no_fifth_zero",
    matched,
    f"scanned {N_SCAN} points on [0,2pi) with sign-change bracketing; found "
    f"{len(zeros_found)} zero(s), each within 1e-15 of one of "
    f"{{0, pi/3, pi, 5pi/3}}. An independent check that sympy's solveset is "
    f"complete — a missed branch would show as an unmatched bracket here.",
)

# ------------------------------------------------------- 3. all four die -----
def hoefsmit_b2(qv):
    return (qv**4 + qv**2 + 1) / (qv**2 + 1) ** 2


def h_of(qv):
    return qv - 1 / qv


deg = {}
# phi = 0  ->  q = 1
q1 = mp.mpf(1)
deg["0"] = {
    "h": mpm.nstr(h_of(q1), 8),
    "E_0 denominator q(q-1)": mpm.nstr(q1 * (q1 - 1), 8),
    "verdict": "h = 0 kills Delta(net) AND q(q-1) = 0 is a pole of E_0 — degenerate twice",
}
# phi = pi -> q = -1
qm = mp.mpf(-1)
deg["pi"] = {
    "h": mpm.nstr(h_of(qm), 8),
    "verdict": "h = q - 1/q = 0 — the substrate degenerates",
}
# phi = pi/3, 5pi/3 -> primitive 6th roots
for nm, p in (("pi/3", mp.pi / 3), ("5pi/3", 5 * mp.pi / 3)):
    qv = mpm.exp(1j * p)
    b2 = hoefsmit_b2(qv)
    deg[nm] = {
        "|b^2|": mpm.nstr(abs(b2), 8),
        "|q^2+1| (denominator)": mpm.nstr(abs(qv**2 + 1), 8),
        "verdict": "primitive 6th root: q^6-1 = (q^2-1)(q^4+q^2+1) forces "
        "q^4+q^2+1 = 0, so Hoefsmit b^2 = 0 and V_(2,1) decouples",
    }

all_degenerate = (
    abs(h_of(q1)) < mp.mpf(10) ** (-40)
    and abs(h_of(qm)) < mp.mpf(10) ** (-40)
    and abs(hoefsmit_b2(mpm.exp(1j * mp.pi / 3))) < mp.mpf(10) ** (-35)
    and abs(hoefsmit_b2(mpm.exp(1j * 5 * mp.pi / 3))) < mp.mpf(10) ** (-35)
)
record(
    "all_four_reality_solutions_are_degenerate",
    all_degenerate,
    "phi=0: h = 0 and E_0 has a pole (degenerate twice — #6889 called it "
    "'the pole' and checked only the second); phi=pi: h = 0; phi=pi/3 and "
    "5pi/3: |b^2| < 1e-35, the V_(2,1) coupling vanishes identically at a "
    "primitive 6th root. Sixth-root denominators |q^2+1| are non-zero, so the "
    "vanishing is the numerator's, not an indeterminate form.",
)

# --------------------------------------- 4. the strengthened conclusion ------
record(
    "partial_projection_excludes_the_ENTIRE_fibre_locus",
    sols_set == expected and all_degenerate,
    "reality cuts |q| = 1 to four points and non-degeneracy removes all four, "
    "so under the block's partial projection NO point of the fibre locus "
    "survives — not merely no root of unity. This strengthens #6889, whose "
    "scope line ('|q| = 1 is a great deal more than its roots of unity') "
    "described the non-rational phases as still open when reality had already "
    "excluded them.",
)

# ---------------------------------------------- 5. the dichotomy, restated ---
# Full projection: |Delta(net) * E_0| is a modulus, real for every q.
q0 = q_at(50)
probe_pts = [mpm.exp(1j * mp.mpf(1) / 7), mpm.exp(1j * mp.mpf(2)), mpm.mpf(q0)]
full_all_real = True
for qv in probe_pts:
    hv = h_of(qv)
    val = abs(hv * (hv - 2) / 2 * (_qbeta_e0.order_zero_scaled(1, qv)))
    if abs(mpm.im(mpm.mpmathify(val))) > mp.mpf(10) ** (-40):
        full_all_real = False
record(
    "full_projection_imposes_nothing_so_route5_predicts_nothing_either_way",
    full_all_real,
    "|Delta(net) * E_0| evaluated at q = e^(i/7), e^(2i) and the proton q_0 is "
    "real in every case (it is a modulus), so a full projection imposes no "
    "condition and selects no N. Combined with the assertion above: PARTIAL "
    "kills the whole locus, FULL selects nothing — route 5's N-selection "
    "mechanism yields no prediction under either reading. Scope-(a) on the "
    "MECHANISM; it says nothing about route 5's underlying fibre-Habiro idea.",
)

# ------------------------------------------------------------------ witness --
out = {
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "strengthens": "my own #6889 — its scope line described the non-rational "
    "phases as open when the reality condition had already excluded them",
    "question": "does the partial projection exclude only the root-of-unity "
    "sublocus, or the whole fibre locus?",
    "answer": "the whole fibre locus. Reality is a condition at every point of "
    "|q| = 1 and has exactly four solutions {0, pi/3, pi, 5pi/3}, all "
    "degenerate. With the full projection imposing nothing, route 5's "
    "N-selection mechanism predicts nothing under either reading.",
    "scope": "(a), conditional on the reality assumption route 5's N-selection "
    "already rests on (that Q_beta must be real AT the fibre evaluation point, "
    "not merely after the archimedean functor). Not a refutation of route 5's "
    "underlying fibre-Habiro idea.",
    "reality_solution_set": "{0, pi/3, pi, 5pi/3}",
    "im_factored": str(factored),
    "scan_points": N_SCAN,
    "zeros_found": len(zeros_found),
    "degeneracy": deg,
    "q0": mpm.nstr(q0, 20),
    "q0_pin": "proton (q_at)", "q0Anchor": "proton",
    "dps": mp.dps,
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
wpath = _HERE.parent / "qbeta-fibre-partial-projection-kills-whole-locus.witness.json"
wpath.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wpath}")
print(f"allPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
