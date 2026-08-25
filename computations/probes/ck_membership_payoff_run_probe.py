"""The corpus c_k payoff run — named fibre-level candidates through the membership gate stack, twisted p = 5 leg included.

Beans qou-9p9y (the queued "twisted test" of the membership program)
+ qou-1hlh follow-on (U2 payoff). Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 19).

CANDIDATES (the corpus's actual named fibre-level c_k objects):

- J_Hopf(q) = -(q + 1/q) = -[2]_q — the c_3 fibre candidate
  (c3_hopf_habiro_analysis.py; the SETTLED near-match verdict is a
  VALUE-level statement about Taylor-exactness at q_0 and is not
  re-litigated here — this run tests the ELEMENT's arithmetic).
- -2 - hbar_q^2 * q with hbar_q = 1 - 1/q — the corpus's other c_3
  q-form; verified EXACTLY EQUAL to J_Hopf(q) as a Laurent element
  (transcription anchor, falsifiable).
- [2]_q = q + 1/q — the alpha_EM element's q-factor (PR #1511
  pattern [2]_q * (1 - h^2 alpha); the h-deformation factor is an
  archimedean dressing, out of scope for ring membership).
- D(4) = the n = 4 binding Habiro tail (known member; control from
  habiro_tail_membership_gate_probe.py, q^2 D(4) = (q-1)^2 Phi_3).

FAIL CONTROLS (the refutation-grade promise of U2 — "a c_3 candidate
can FAIL without any anchor inversion"):

- SWING-FIT: J_Hopf * (1 + 149/5000) — a fitted-shape perturbation of
  the size of the measured 2.98% cross-anchor swing, written as an
  exact rational (denominator 2^3 * 5^4). Must FAIL the global gate
  AND the p = 2 and p = 5 Frobenius gates (denominator meets both
  primes), while PASSING the 3-integrality gate — the failure is
  per-prime, not generic.
- DENOM-7: [2]_q / 7. Must FAIL the global gate but PASS all three
  local gates (7 is invertible at p = 2, 3, 5) — demonstrating that
  the local gates genuinely encode "integrality away from a prime
  set" (GSWZ integrality away from Delta), i.e. G4 is NOT the global
  gate restated.

GATES (exact sympy cyclotomic arithmetic throughout):

  G1 global: integer Laurent coefficients (classical Habiro ring).
  G2 bar/3:  bar-even symmetrization (F(q) + F(1/q))/2 has
             3-integral coefficients (the GSWZ symmetrization gate
             pattern, gswz_symmetrization_integrality_probe.py).
  G3 p = 2:  F(zeta_8)^2 == F(zeta_4) mod 2 Z[zeta_8] — the Frobenius
             endomorphism congruence g^2 == Frob(g) mod 2 with
             Frob(zeta_8) = zeta_4; the zeta_4 -> zeta_8 edge of U4
             in exact form.
  G4 p = 5:  F(zeta_5)^5 == F(1) mod 5 Z[zeta_5] — the TWISTED leg
             queued on qou-9p9y: the same Frobenius congruence one
             prime up, computed in Z[zeta_5] (minimal polynomial
             1 + q + q^2 + q^3 + q^4), where the 5_2/GSWZ machinery
             of this program lives.

HONESTY: membership of Z[q,1/q] elements in the classical Habiro ring
is automatic — the content is (a) the twisted gates exercised exactly
on the NAMED corpus candidates, (b) the per-prime failure signature
separating fitted shapes from structural elements, (c) the exact
identity of the two corpus c_3 q-forms. Every gate can fail (the two
controls fail exactly where predicted, and a wrong Frobenius or a
wrong reduction would break the member rows).
"""

import json
import pathlib
import sys
from fractions import Fraction

import sympy as sp

q = sp.symbols("q")

checks = {}
detail = {}

# ---------------- candidates (exact Laurent in q) ---------------------
hbar = 1 - 1 / q
J_hopf = -(q + 1 / q)
c3_form2 = -2 - hbar**2 * q
two_q = q + 1 / q

# corpus D(4): q^2 D(4) = (q-1)^2 Phi_3(q)  (anchor from the classical
# gate run) => D(4) = (q-1)^2 (1 + q + q^2) / q^2
D4 = sp.expand((q - 1) ** 2 * (1 + q + q**2) / q**2)

swing_fit = sp.nsimplify(J_hopf * (1 + sp.Rational(149, 5000)))
denom7 = two_q / 7

# transcription anchor: the two corpus c_3 q-forms are the SAME element
checks["c3_two_forms_identical"] = sp.simplify(c3_form2 - J_hopf) == 0


def laurent_coeffs(f):
    """Exact Laurent coefficients of f as {exp: Fraction}."""
    f = sp.cancel(sp.together(sp.expand(f)))
    num, den = sp.fraction(f)
    pn = sp.Poly(num, q)
    pd = sp.Poly(den, q)
    # denominator must be a monomial c*q^k for a Laurent polynomial
    if len(pd.monoms()) != 1:
        return None
    k = pd.monoms()[0][0]
    c = pd.coeffs()[0]
    out = {}
    for (e,), co in zip(pn.monoms(), pn.coeffs()):
        out[e - k] = Fraction(int(sp.fraction(co)[0]), int(sp.fraction(co)[1])) / Fraction(
            int(sp.fraction(c)[0]), int(sp.fraction(c)[1])
        )
    return out


def g1_integer(f):
    lc = laurent_coeffs(f)
    return lc is not None and all(c.denominator == 1 for c in lc.values())


def g2_bar3(f):
    sym = sp.together((f + f.subs(q, 1 / q)) / 2)
    lc = laurent_coeffs(sp.expand(sym))
    return lc is not None and all(c.denominator % 3 != 0 for c in lc.values())


# ---- exact cyclotomic reduction helpers ------------------------------
def eval_at_zeta(f, order, minpoly_coeffs, deg):
    """f(zeta_order) in the power basis of Z[zeta]/(minpoly), exact
    Fractions. minpoly monic: zeta^deg = -sum m_i zeta^i."""
    lc = laurent_coeffs(f)
    if lc is None:
        return None
    pows = {}
    vec = [Fraction(0)] * deg
    vec[0] = Fraction(1)
    for e in range(order):
        pows[e] = vec[:]
        out = [Fraction(0)] * (deg + 1)
        for i, c in enumerate(vec):
            out[i + 1] += c
        top = out[deg]
        if top:
            for i in range(deg):
                out[i] -= top * minpoly_coeffs[i]
        vec = out[:deg]
    res = [Fraction(0)] * deg
    for e, c in lc.items():
        pv = pows[e % order]
        for i in range(deg):
            res[i] += c * pv[i]
    return res


def cyc_mul(a, b, minpoly_coeffs, deg):
    out = [Fraction(0)] * (2 * deg - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    for k in range(2 * deg - 2, deg - 1, -1):
        top = out[k]
        if top:
            for i in range(deg):
                out[k - deg + i] -= top * minpoly_coeffs[i]
    return out[:deg]


def frob_congruence(f, p, order, minpoly_coeffs, deg, target_order):
    """Gate: f(zeta_order)^p == f(zeta_target) mod p, exactly.
    Returns True/False, or False if any denominator meets p."""
    v = eval_at_zeta(f, order, minpoly_coeffs, deg)
    w = eval_at_zeta(f, target_order, minpoly_coeffs, deg)
    if v is None or w is None:
        return False
    if any(c.denominator % p == 0 for c in v + w):
        return False
    vp = [Fraction(1)] + [Fraction(0)] * (deg - 1)
    for _ in range(p):
        vp = cyc_mul(vp, v, minpoly_coeffs, deg)
    diff = [a - b for a, b in zip(vp, w)]
    # reduce mod p: all coefficients (denominators prime to p) must
    # have numerator * inv(denominator) == 0 mod p
    for c in diff:
        if (c.numerator * pow(c.denominator, -1, p)) % p != 0:
            return False
    return True


# Z[zeta_8]: minpoly q^4 + 1, zeta_8^4 = -1; zeta_4 = zeta_8^2.
MP8 = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]  # zeta^4 = -(1)
# gate G3: f(zeta_8)^2 == f(zeta_4) mod 2, both inside Z[zeta_8]
def g3_p2(f):
    v8 = eval_at_zeta(f, 8, MP8, 4)
    if v8 is None or any(c.denominator % 2 == 0 for c in v8):
        return False
    # f(zeta_4): substitute q -> zeta_8^2 == evaluate with order-8
    # powers at doubled exponents — reuse eval by mapping f(q)->f(q^2)
    f4 = sp.expand(f.subs(q, q**2))
    v4 = eval_at_zeta(f4, 8, MP8, 4)
    if v4 is None or any(c.denominator % 2 == 0 for c in v4):
        return False
    v8sq = cyc_mul(v8, v8, MP8, 4)
    for a, b in zip(v8sq, v4):
        c = a - b
        if (c.numerator * pow(c.denominator, -1, 2)) % 2 != 0:
            return False
    return True


# Z[zeta_5]: minpoly 1 + q + q^2 + q^3 + q^4, zeta^4 = -(1+z+z^2+z^3)
MP5 = [Fraction(1), Fraction(1), Fraction(1), Fraction(1)]
def g4_p5(f):
    return frob_congruence(f, 5, 5, MP5, 4, target_order=1)


CANDIDATES = {
    "J_hopf_c3_candidate": (J_hopf, dict(g1=True, g2=True, g3=True, g4=True)),
    "two_q_alphaEM_factor": (two_q, dict(g1=True, g2=True, g3=True, g4=True)),
    "binding_tail_D4": (D4, dict(g1=True, g2=True, g3=True, g4=True)),
    "FAIL_swing_fit_2p98pct": (swing_fit, dict(g1=False, g2=True, g3=False, g4=False)),
    "FAIL_denom7": (denom7, dict(g1=False, g2=True, g3=True, g4=True)),
}

table = {}
for name, (f, expect) in CANDIDATES.items():
    got = dict(
        g1=g1_integer(f),
        g2=g2_bar3(f),
        g3=g3_p2(f),
        g4=g4_p5(f),
    )
    table[name] = got
    checks[f"{name}_signature_as_predicted"] = got == expect

# D4 bar-evenness sanity (the classical gate's H2, via this harness)
checks["D4_bar_even"] = sp.simplify(D4 - D4.subs(q, 1 / q)) == 0

print(json.dumps(checks, indent=1))
print(json.dumps(table, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

import subprocess

_sha = subprocess.run(
    ["git", "rev-parse", "HEAD"], capture_output=True, text=True
).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "ck_membership_payoff_run_probe",
    "engine": "python3-sympy-exact",
    "scriptFile": "ck_membership_payoff_run_probe.py",
    "commitSha": _sha,
    "beans": ["qou-9p9y", "qou-1hlh"],
    "source": (
        "corpus c_3 candidates (computations/c3_hopf_habiro_analysis.py; "
        "docs/coordination/1ppq-qbeta.md); alpha_EM element PR #1511; "
        "binding tails (habiro_tail_membership_gate_probe.py); GSWZ "
        "gates (library/arxiv-2412.04241v2/2412.04241v2.pdf); CGZ (library/arxiv-1712.04887v3/1712.04887v3.pdf)"
    ),
    "checks": checks,
    "gate_table": table,
    "gates": {
        "g1": "integer Laurent (global classical membership)",
        "g2": "bar-even symmetrization 3-integral (GSWZ pattern)",
        "g3": "F(zeta_8)^2 == F(zeta_4) mod 2 in Z[zeta_8] (p=2 Frobenius edge)",
        "g4": "F(zeta_5)^5 == F(1) mod 5 in Z[zeta_5] (TWISTED p=5 leg)",
    },
    "scope": (
        "scope-(a): the named corpus fibre-level c_k candidates pass all "
        "four gates; the fitted-shape controls fail with the predicted "
        "PER-PRIME signature (swing-fit fails g1/g3/g4, passes g2; "
        "denom-7 fails only g1) — the gates encode integrality away "
        "from a prime set, the refutation-grade structure U2 promised. "
        "VALUE-level c_3 verdicts (near-match, cross-anchor swing) are "
        "untouched: this is element-level arithmetic only."
    ),
}
with open(pathlib.Path(__file__).resolve().parent / "ck_membership_payoff_run.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
