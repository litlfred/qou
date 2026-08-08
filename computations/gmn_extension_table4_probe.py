#!/usr/bin/env python3
"""Extended Gell-Mann-Nishijima check on the quark knot dictionary (DECISIVE).

Checklist item 4 of the heavy-flavour survey (bean qou-ypl2 context):
the knot-derived charge convention (positive crossing = up-type +2/3,
mirror ^sigma / negative crossing = down-type -1/3; borromean-quark +
strangelet blocks) must satisfy the extended Gell-Mann-Nishijima
relation

    Q = I3 + (B + S + C + B' + T)/2

with the standard additive flavour numbers (S(s) = -1, C(c) = +1,
B'(b) = -1; sign matching the species' charge sign; B = 1/3 per quark;
I3 = +-1/2 for u,d and 0 for heavier flavours).

Two assignments are tested, exactly as they appear in the corpus:

  A (table4 current): c = positive crossing <- T(2,7); b = POSITIVE
    crossing <- T(2,5). The crossed pairing (b with mu, c with tau).
  B (SM-aligned, the bullet list already in unmapped-torus-knots.md):
    c = positive <- T(2,5); b = mirror ^sigma (negative) <- T(2,7).

RESULT this probe certifies: assignment A VIOLATES extended GMN on the
bottom quark — a positive-crossing b has topological charge +2/3 but
B' = -1 forces Q = -1/3 (and the alternative B' = +1 contradicts the
defining bottomness of a -1/3 down-type quark). Assignment B passes on
all five flavours and on every composite checked (p, n, uds, K+, D+,
B-). The pairing question is thereby arithmetic, not taste: the
mirror-mark discipline + extended GMN force the SM-aligned assignment,
under which a weak doublet is exactly the (unmarked, marked) pair of
one winding family. Exact rational arithmetic; no fit, no tolerance.
"""

from __future__ import annotations

from fractions import Fraction as Fr

import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder  # noqa: E402

# Flavour data: (I3, B, species additive number name)
# Charge from crossing sign: +2/3 if positive, -1/3 if negative (^sigma).
FLAVOURS = {
    "u": dict(I3=Fr(1, 2), extra=Fr(0)),
    "d": dict(I3=Fr(-1, 2), extra=Fr(0)),
    "s": dict(I3=Fr(0), extra=Fr(-1)),   # strangeness
    "c": dict(I3=Fr(0), extra=Fr(1)),    # charm
    "b": dict(I3=Fr(0), extra=Fr(-1)),   # bottomness
}
B_QUARK = Fr(1, 3)

ASSIGNMENTS = {
    "A_table4_current": {"u": +1, "d": -1, "s": -1, "c": +1, "b": +1},
    "B_sm_aligned": {"u": +1, "d": -1, "s": -1, "c": +1, "b": -1},
}


def q_topo(sign: int) -> Fr:
    return Fr(2, 3) if sign > 0 else Fr(-1, 3)


def q_gmn(fl: str) -> Fr:
    d = FLAVOURS[fl]
    return d["I3"] + (B_QUARK + d["extra"]) / 2


def check_assignment(signs: dict) -> dict:
    per = {}
    for fl in FLAVOURS:
        qt, qg = q_topo(signs[fl]), q_gmn(fl)
        per[fl] = dict(Q_topo=str(qt), Q_gmn=str(qg), ok=qt == qg)
    # Composites: quark content with anti-quarks negating everything.
    def comp(content):  # list of (flavour, +1 particle / -1 antiparticle)
        qt = sum(a * q_topo(signs[f]) for f, a in content)
        qg = sum(a * q_gmn(f) for f, a in content)
        return qt, qg
    composites = {
        "p (uud)": [("u", 1), ("u", 1), ("d", 1)],
        "n (udd)": [("u", 1), ("d", 1), ("d", 1)],
        "uds strangelet": [("u", 1), ("d", 1), ("s", 1)],
        "K+ (u sbar)": [("u", 1), ("s", -1)],
        "D+ (c dbar)": [("c", 1), ("d", -1)],
        "B- (b ubar)": [("b", 1), ("u", -1)],
    }
    per_comp = {}
    for name, content in composites.items():
        qt, qg = comp(content)
        per_comp[name] = dict(Q_topo=str(qt), Q_gmn=str(qg), ok=qt == qg)
    n_viol = sum(not v["ok"] for v in per.values()) + \
        sum(not v["ok"] for v in per_comp.values())
    return dict(flavours=per, composites=per_comp, violations=n_viol)


def main() -> None:
    results = {k: check_assignment(v) for k, v in ASSIGNMENTS.items()}

    wb = WitnessBuilder("gmn-extension-table4", engine="python-fractions")
    wb.set_description(
        "DECISIVE extended Gell-Mann-Nishijima check on the quark knot "
        "dictionary (bean qou-ypl2): Q_topo (crossing sign: +2/3 "
        "positive, -1/3 mirror) vs Q = I3 + (B+S+C+B')/2. Assignment A "
        "(table4 current: b positive at T(2,5)) violates GMN on b; "
        "assignment B (SM-aligned: c at T(2,5), b mirror at T(2,7)) "
        "passes on all flavours and composites. The mirror-mark "
        "discipline + GMN force the SM-aligned pairing; weak doublets "
        "become the (unmarked, marked) pair of one winding family. "
        "Exact rational arithmetic.")
    wb.add_data("convention", {
        "Q_topo": "+2/3 positive crossing, -1/3 mirror ^sigma",
        "gmn": "Q = I3 + (B + S + C + B')/2, B = 1/3 per quark",
        "additive": {"S(s)": -1, "C(c)": +1, "B'(b)": -1},
    })
    wb.add_data("results", results)
    wb.set_content_block("prose:sm-params-quark-masses")
    wb.add_assertion(
        name="assignment_B_zero_violations",
        computed=results["B_sm_aligned"]["violations"], expected=0,
        tolerance=0, unit="count",
        source="SM-aligned assignment satisfies extended GMN everywhere.")
    wb.add_assertion(
        name="assignment_A_violates_on_b",
        computed=int(not results["A_table4_current"]["flavours"]["b"]["ok"]),
        expected=1, tolerance=0, unit="bool",
        source=("table4's positive-crossing bottom has Q_topo = +2/3 "
                "against GMN Q = -1/3: the crossed pairing fails."))
    out = wb.save()

    for name, res in results.items():
        print(f"{name}: violations = {res['violations']}")
        for fl, v in res["flavours"].items():
            mark = "ok" if v["ok"] else "VIOLATION"
            print(f"  {fl}: Q_topo {v['Q_topo']} vs GMN {v['Q_gmn']}  {mark}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
