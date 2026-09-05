"""Membership gate, first in-corpus run — the binding Habiro tail D(n), n = 4..9.

Bean qou-1ddd (T2 of the Habiro attack plan). Scope-(a); no fit;
nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 6).

TARGET. The binding q-deformation Habiro tail
D(n) = S(n) - S(n-1) - [n-1]_q S(n-2), with S(n) = sum_{lambda |- n}
dim_q(lambda) the na-Stokes period (q-hook-length formula), from
docs/audits/2026-07-12-lever1-habiro-tail-closed-form.md — the corpus's
own exact Habiro-flavoured series family, and the first REAL target for
the GSWZ membership gate stack.

WHAT THIS CHECKS (exact sympy rational arithmetic):

1. Convention anchors (falsifiable transcription guards): D(2) = D(3) = 0
   and q^2 D(4) = (q-1)^2 Phi_3(q) — the audit table's printed seed and
   n = 4 row.
2. Gate: INTEGER Laurent coefficients for every n = 4..9 — membership
   in the CLASSICAL Habiro ring Z[q, q^{-1}] (trivial gluing), i.e. the
   tails pass the integrality gate outright, unlike a generic fitted
   series.
3. Gate: bar-evenness D(1/q) = D(q) for every n (the audit's H2,
   re-verified through the gate harness).
4. Gate: the (q-1)^2 double root for every n >= 4 (the audit's H1 —
   order >= 2 vanishing at the zeta_1 fibre).
5. NEW fibre data: exact zeta_4 and zeta_8 evaluations of D(n) for
   n = 4..9 — the binding tail's values at the monodromy point and at
   the Q_beta witness point, recorded in the witness for the
   zeta-indexed picture. Bar-evenness forces D(zeta_4) real
   (bar = conjugation on the unit circle); the probe verifies this
   reality as a cross-check of H2 at the fibre level.

HONESTY: D(n) in Z[q,1/q] makes classical-Habiro membership automatic —
the content of this run is (a) the gate harness exercised end-to-end on
real corpus series, (b) the H1/H2 invariants re-verified through it,
(c) the new exact fibre values. No number-field twist is involved for
these tails; the twisted test remains for genuinely non-polynomial
candidates (bean qou-9p9y).
"""

import json
import sys

import sympy as sp
from sympy.utilities.iterables import partitions

from pathlib import Path as _PathW  # noqa: E402 — witness output root
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)
_HERE_W = _PathW(__file__).resolve().parent

q = sp.symbols("q")


def q_int(n):
    """Balanced q-integer [n]_q = (q^n - q^{-n})/(q - q^{-1}) — the
    corpus convention (lever1_habiro_tail_closed_form.py), which is
    bar-invariant and the source of the tails' bar-evenness."""
    if n == 0:
        return sp.Integer(0)
    return sp.cancel((q**n - q**(-n)) / (q - 1 / q))


def q_fact(n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= q_int(k)
    return r


def hooks(lam):
    """Hook lengths of partition lam (list of parts, descending)."""
    conj = []
    for i in range(lam[0]):
        conj.append(sum(1 for p in lam if p > i))
    hs = []
    for i, p in enumerate(lam):
        for j in range(p):
            hs.append((p - j) + (conj[j] - i) - 1)
    return hs


def dim_q(lam, n):
    num = q_fact(n)
    den = sp.Integer(1)
    for h in hooks(lam):
        den *= q_int(h)
    return sp.cancel(num / den)


def S(n):
    if n == 0:
        return sp.Integer(1)
    total = sp.Integer(0)
    for pdict in partitions(n):
        lam = []
        for part, mult in sorted(pdict.items(), reverse=True):
            lam.extend([part] * mult)
        total += dim_q(lam, n)
    return sp.cancel(total)


Svals = {n: S(n) for n in range(0, 10)}
Dvals = {}
for n in range(2, 10):
    Dvals[n] = sp.cancel(Svals[n] - Svals[n - 1] - q_int(n - 1) * Svals[n - 2])

checks = {}

# (1) convention anchors
checks["anchor_D2_D3_zero"] = bool(
    sp.simplify(Dvals[2]) == 0 and sp.simplify(Dvals[3]) == 0
)
phi3 = q**2 + q + 1
checks["anchor_q2_D4_eq_qm1sq_Phi3"] = bool(
    sp.simplify(sp.expand(q**2 * Dvals[4]) - sp.expand((q - 1) ** 2 * phi3)) == 0
)


def laurent_coeffs(expr):
    """Coefficients of a Laurent polynomial in q as a dict deg -> Rational."""
    e = sp.cancel(expr)
    num, den = sp.fraction(sp.together(e))
    pnum = sp.Poly(sp.expand(num), q)
    pden = sp.Poly(sp.expand(den), q)
    # den must be a monomial c*q^k for a Laurent polynomial
    assert len(pden.terms()) == 1, "denominator not a monomial"
    (dmono, dcoef), = pden.terms()
    out = {}
    for (m,), c in pnum.terms():
        out[m - dmono[0]] = sp.Rational(c, dcoef)
    return out


all_integer = True
all_bareven = True
all_droot = True
fibres = {}
I = sp.I
zeta8 = sp.exp(sp.I * sp.pi / 4)
for n in range(4, 10):
    Dn = Dvals[n]
    cs = laurent_coeffs(Dn)
    if not all(c.q == 1 for c in cs.values()):
        all_integer = False
    if sp.simplify(Dn.subs(q, 1 / q) - Dn) != 0:
        all_bareven = False
    if sp.simplify(Dn.subs(q, 1)) != 0 or sp.simplify(sp.diff(Dn, q).subs(q, 1)) != 0:
        all_droot = False
    z4 = sp.simplify(sp.expand_complex(Dn.subs(q, I)))
    z8 = sp.nsimplify(
        sp.simplify(sp.expand_complex(Dn.subs(q, zeta8))), [sp.sqrt(2)]
    )
    fibres[n] = {"zeta4": str(z4), "zeta8": str(z8)}

checks["gate_integer_laurent_all_n"] = all_integer
checks["gate_bareven_all_n"] = all_bareven
checks["gate_qm1_sq_double_root_all_n"] = all_droot
# bar-even => real at zeta4
checks["zeta4_values_real"] = all(
    sp.im(sp.sympify(fibres[n]["zeta4"])) == 0 for n in range(4, 10)
)

print(json.dumps(checks, indent=1))
print(json.dumps(fibres, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

witness = {
    "schema": "probe-witness/v1",
    "probe": "habiro_tail_membership_gate_probe",
    "beans": ["qou-1ddd"],
    "source": "docs/audits/2026-07-12-lever1-habiro-tail-closed-form.md; GSWZ gate stack (this PR)",
    "checks": checks,
    "zeta_fibre_values": fibres,
    "scope": "scope-(a): gate exercised on the corpus binding Habiro tails; classical-ring membership automatic for Z[q,1/q]; twisted test queued (qou-9p9y)",
}
# Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
# opening for write TRUNCATES immediately, so an import that raises inside the
# `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
# is not importable from a bare producer context, which is how 22 witnesses were
# emptied by a single `producer_importability_audit` run.
import os as _os  # noqa: E402 -- provenance stamp
from qou_substrate.witness import WitnessBuilder as _WB
# Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
# `os.replace` it into position. `open(..., "w")` TRUNCATES before the
# dump runs, so any exception in between leaves the committed witness
# empty or partial -- the shape that emptied 22 witnesses to zero bytes
# in one `producer_importability_audit` run. `os.replace` is atomic on
# POSIX within a filesystem, hence a SIBLING temp file.
_wpath_sidu = _HERE_W / "habiro_tail_membership_gate.witness.json"
_wtmp_sidu = str(_wpath_sidu) + ".tmp"
with open(_wtmp_sidu, "w") as f:
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    json.dump(witness, f, indent=1)

_os_sidu.replace(_wtmp_sidu, _wpath_sidu)
sys.exit(0 if npass == len(checks) else 1)
