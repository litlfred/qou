#!/usr/bin/env python3
"""intro_worked_miniature_h3.py -- every number in the Introduction's proposed
"worked miniature" box, computed exactly.

The box walks one braid word through the five-step chain of
`intro-structure-to-numbers`:

    braid word  ->  normal form in H_3(q)  ->  Markov trace in Q(q)
                ->  Wedderburn split  sum_lambda y_lambda chi_lambda
                ->  number at q_0

Conventions (all fixed by the corpus, none chosen here):

  * Quadratic relation (sigma_i - q)(sigma_i + q^-1) = 0, i.e.
    sigma_i^2 = h sigma_i + 1 with h = q - q^-1
    (`intro-particles-as-knots.md`).
  * Convention D Markov weight z = q^3/(q^2+1) (owner ruling 2026-08-15, R1).
  * Markov trace: tr(1) = 1, tr(x sigma_{n-1} y) = z tr(x y) for x, y in H_{n-1}.
  * q_0 = the experimental (proton) pin `qou_substrate.constants.q_at`
    (owner directive 2026-08-07; rem:epistemic-status-of-calibrations,
    "Which pin the numbers actually use").

Braids treated:
  * V^3 = (sigma_0 sigma_1^-1)^3, the Borromean core.  Its trace is the
    closed form |tr_M(beta_Bor)| = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4) that the
    proton pin itself solves through (constants.q_at docstring).  The script
    re-derives it from the braid word instead of reading it.
  * V^2 = (sigma_0 sigma_1^-1)^2, the figure-eight 4_1.
  * sigma_0 sigma_1 sigma_0, the electron word (Hopf-link closure, owner
    ruling).
  * gamma*gamma for the photon gamma = 1 + p0 s0 + p1 s1 + p01 s0 s1^-1
    (owner ruling 2026-11-20): which of the six basis elements it reaches.

Exact arithmetic: sympy over Q(q, phi).  The only floating evaluation is the
final substitution q = q_0, done in mpmath at 50 digits from the q_0 the
substrate package derives.  No float64 anywhere.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

q = sp.symbols("q", positive=True)
h = q - 1 / q
z = q**3 / (q**2 + 1)

# ---- H_3(q) in the standard basis T_w, w in S_3 ---------------------------
# Words in the generators 0 = sigma_0, 1 = sigma_1; reduced representatives.
BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
IDX = {w: i for i, w in enumerate(BASIS)}
NAMES = ["1", "s0", "s1", "s0 s1", "s1 s0", "s0 s1 s0"]


def _perm(word):
    p = [0, 1, 2]
    for s in word:
        p[s], p[s + 1] = p[s + 1], p[s]
    return tuple(p)


PERM_TO_W = {_perm(w): w for w in BASIS}


def _length(w):
    return len(w)


def left_mult_gen(s, vec):
    """sigma_s * (sum c_w T_w) in the T_w basis."""
    out = [sp.Integer(0)] * 6
    for w, c in zip(BASIS, vec):
        if c == 0:
            continue
        sw = PERM_TO_W[_perm((s,) + w)]
        if len(sw) > len(w):
            out[IDX[sw]] += c
        else:  # sigma_s T_w = h T_w + T_{sw}
            out[IDX[w]] += h * c
            out[IDX[sw]] += c
    return [sp.simplify(x) for x in out]


def elem(word):
    """Normal form of a signed braid word (+s / -(s+1) style is avoided:
    we take a list of (s, sign))."""
    vec = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for s, sign in reversed(word):
        if sign > 0:
            vec = left_mult_gen(s, vec)
        else:  # sigma^-1 = sigma - h
            a = left_mult_gen(s, vec)
            vec = [sp.simplify(x - h * y) for x, y in zip(a, vec)]
    return vec


def mul(a, b):
    """a*b for basis vectors a, b."""
    out = [sp.Integer(0)] * 6
    for w, c in zip(BASIS, a):
        if c == 0:
            continue
        v = list(b)
        for s in reversed(w):
            v = left_mult_gen(s, v)
        out = [o + c * x for o, x in zip(out, v)]
    return [sp.simplify(x) for x in out]


# Markov trace on the basis, from tr(x s1 y) = z tr(xy), x,y in H_2 = <1, s0>.
TR_BASIS = [sp.Integer(1), z, z, z**2, z**2, z * (h * z + 1)]


def tr_M(vec):
    return sp.factor(sp.simplify(sum(c * t for c, t in zip(vec, TR_BASIS))))


# ---- irreducible representations ------------------------------------------
# (3): sigma -> q ; (1,1,1): sigma -> -q^-1 ; (2,1): -q^-1 * reduced Burau at t = q^2.
t = q**2
B0 = sp.Matrix([[-t, 1], [0, 1]]) * (-1 / q)
B1 = sp.Matrix([[1, 0], [t, -t]]) * (-1 / q)
REPS = {
    (3,): (sp.Matrix([[q]]), sp.Matrix([[q]])),
    (2, 1): (B0, B1),
    (1, 1, 1): (sp.Matrix([[-1 / q]]), sp.Matrix([[-1 / q]])),
}


def rep_of_basis(lam, w):
    g = REPS[lam]
    M = sp.eye(g[0].shape[0])
    for s in w:
        M = M * g[s]
    return M


def chi(lam, vec):
    return sp.simplify(sum(c * rep_of_basis(lam, w).trace()
                           for w, c in zip(BASIS, vec)))


def main():
    checks = []

    # relations hold in every representation
    for lam, (g0, g1) in REPS.items():
        n = g0.shape[0]
        quad = all(sp.simplify(g * g - h * g - sp.eye(n)) == sp.zeros(n)
                   for g in (g0, g1))
        braid = sp.simplify(g0 * g1 * g0 - g1 * g0 * g1) == sp.zeros(n)
        checks.append({"name": f"rep_{lam}_satisfies_quadratic_and_braid",
                       "passed": bool(quad and braid)})

    # Wedderburn weights: solve tr_M(T_w) = sum y_lam chi_lam(T_w) on all six T_w
    ys = sp.symbols("y3 y21 y111")
    lams = [(3,), (2, 1), (1, 1, 1)]
    eqs = []
    for i, w in enumerate(BASIS):
        e = [sp.Integer(0)] * 6
        e[i] = sp.Integer(1)
        eqs.append(sp.Eq(TR_BASIS[i],
                         sum(y * chi(l, e) for y, l in zip(ys, lams))))
    sol = sp.solve(eqs, ys, dict=True)
    assert len(sol) == 1, sol
    y = {l: sp.factor(sol[0][yy]) for yy, l in zip(ys, lams)}
    checks.append({"name": "six_trace_equations_have_unique_wedderburn_solution",
                   "passed": True})

    # cross-check against the committed convention-D symbolic witness
    doc = json.loads((REPO / "computations" /
                      "y-lambda-wenzl-bridge-symbolic-witness.json").read_text())
    agree = True
    for row in doc["tables_by_n"]["3"]["weights"]:
        p = row["partition"]
        lam = tuple(json.loads(p) if isinstance(p, str) else p)
        ref = sp.sympify(row["y_lambda_symbolic"], locals={"q": q})
        agree &= sp.simplify(ref - y[lam]) == 0
    checks.append({"name": "y_lambda_matches_committed_convention_D_witness_n3",
                   "passed": bool(agree)})

    words = {
        "borromean_V3": [(0, 1), (1, -1)] * 3,
        "figure_eight_V2": [(0, 1), (1, -1)] * 2,
        "electron_s0s1s0": [(0, 1), (1, 1), (0, 1)],
    }
    braids = {}
    for name, w in words.items():
        v = elem(w)
        tr = tr_M(v)
        wed = sp.simplify(sum(y[l] * chi(l, v) for l in lams))
        braids[name] = {
            "normal_form": {NAMES[i]: str(sp.factor(c)) for i, c in enumerate(v) if c != 0},
            "tr_M": str(tr),
            "tr_M_in_h": None,
            "chi": {str(l): str(sp.factor(chi(l, v))) for l in lams},
        }
        checks.append({"name": f"{name}_wedderburn_sum_equals_tr_M",
                       "passed": sp.simplify(wed - tr) == 0})
        braids[name]["_tr"] = tr

    # Borromean: compare with the closed form the proton pin solves through
    closed = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)
    trB = braids["borromean_V3"]["_tr"]
    sign = None
    for sgn in (1, -1):
        if sp.simplify(trB - sgn * closed) == 0:
            sign = sgn
    checks.append({"name": "borromean_tr_M_equals_pm_constants_q_at_closed_form",
                   "passed": sign is not None})

    # photon squared
    p0, p1, p01 = sp.symbols("phi0 phi1 phi01")
    gamma = [sp.Integer(0)] * 6
    for coeff, w in ((1, []), (p0, [(0, 1)]), (p1, [(1, 1)]),
                     (p01, [(0, 1), (1, -1)])):
        v = elem(w) if w else [sp.Integer(1)] + [sp.Integer(0)] * 5
        gamma = [g + coeff * x for g, x in zip(gamma, v)]
    g2 = mul(gamma, gamma)
    reached = [NAMES[i] for i, c in enumerate(g2) if sp.expand(c) != 0]
    checks.append({"name": "gamma_squared_reaches_all_six_basis_elements",
                   "passed": len(reached) == 6})

    # numbers at q_0 (proton pin), 50 digits
    import mpmath as mp
    from qou_substrate import constants as C
    mp.mp.dps = 60
    q0 = C.q_at(50)
    vals = {}
    for name, b in braids.items():
        f = sp.lambdify(q, b.pop("_tr"), modules="mpmath")
        vals[name] = mp.nstr(f(q0), 30)
    yv = {str(l): mp.nstr(sp.lambdify(q, y[l], modules="mpmath")(q0), 30) for l in lams}

    out = {
        "computation": "intro-worked-miniature-h3",
        "description": "Exact H_3(q) worked miniature for the Introduction: "
                       "braid word -> normal form -> tr_M in Q(q) -> Wedderburn "
                       "split -> value at the proton-pinned q_0.",
        "scriptFile": "intro/intro_worked_miniature_h3.py",
        "q0Anchor": "proton",
        "q0AnchorReason": "Numerical evaluation only; production default per "
                          "owner directive 2026-08-07. Every symbolic result is "
                          "q-independent of the pin.",
        "q0": mp.nstr(q0, 40),
        "conventions": {"quadratic": "s^2 = h s + 1, h = q - 1/q",
                        "z": "q^3/(q^2+1)"},
        "y_lambda": {str(l): str(y[l]) for l in lams},
        "y_lambda_at_q0": yv,
        "braids": braids,
        "braids_tr_M_at_q0": vals,
        "borromean_sign_vs_closed_form": sign,
        "gamma_squared_terms": {NAMES[i]: str(sp.factor(sp.expand(c)))
                                for i, c in enumerate(g2)},
        "assertions": checks,
    }
    out["allPassed"] = all(c["passed"] for c in checks)
    print(json.dumps(out, indent=2))
    dest = REPO / "computations" / "intro-worked-miniature-h3.witness.json"
    dest.write_text(json.dumps(out, indent=2) + "\n")
    return 0 if out["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
