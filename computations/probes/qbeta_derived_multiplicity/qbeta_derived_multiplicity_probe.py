#!/usr/bin/env python3
"""qbeta_derived_multiplicity_probe — route 1 of issue #8833 (owner choice 2026-11-21).

The closed candidate list is PREREGISTRATION.md in this directory (commits 7dd448828c,
4659deea22), fixed before this file was written. Every candidate is reported; none is
selected, wired or scored. CODATA appears in a comparison column only.

Exact sympy over Q(q) on (C^2)^{x3} (the matrices of NucleonWeightSpaceTraces.lean, imported
from the flavour-split probe, not re-typed). Numbers: mpmath, 70 dps, proton q0,
E0 = qbeta_e0.canonical.

Checks
  P1  the two photon orders give the same element: gamma(0,0,qh) gamma(0,0,-h/q)
      = gamma(0,0,-h/q) gamma(0,0,qh) = V^3 on all of (C^2)^{x3}  (M1 counts 2 ordered pairs).
  P2  eps_flavour of V^-3, mirror^3, mirror^-3 equals eps_flavour(V^3) exactly, so the orbit
      members add rather than cancel (M3, M4).
  P3  the base reproduces the scored cell |eps_flavour(V^3)| E0 = 0.3254339287 MeV.
  P4  table Q(m) = m * Q_base for every registered m; no candidate is chosen.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qbeta_e0  # noqa: E402
from codata_2022_source import Q_BETA_MEV_AME  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 70
mp.mp.dps = DPS

_FS = _ROOT / "computations/probes/qbeta_flavour_weight_split/qbeta_flavour_weight_split_probe.py"
_spec = importlib.util.spec_from_file_location("_flavour_split", _FS)
fs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fs)
q, h, D2 = fs.q, fs.h, fs.D2

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


Q0 = sp.Rational(Q_50_DIGIT_STR)


def mpv(e) -> mp.mpf:
    return mp.mpf(str(sp.N(sp.sympify(e).subs(q, Q0), DPS + 5)))


def eps_of(Mp, Mn):
    """eps_flavour = q^-1 tr_{W_n} - q tr_{W_p}, over [2]^3 (ruled normalisation D1)."""
    return sp.simplify(((1 / q) * Mn.trace() - q * Mp.trace()) / D2 ** 3)


def main() -> int:
    # weight-space restrictions of sigma_0, sigma_1 (W_p: A1, A2; W_n: B1, B2)
    A1, A2, B1, B2 = fs.A1, fs.A2, fs.B1, fs.B2
    words = {
        "V^3": (A1 * A2.inv(), B1 * B2.inv(), 3),
        "V^-3": (A1 * A2.inv(), B1 * B2.inv(), -3),
        "mirror^3": (A1.inv() * A2, B1.inv() * B2, 3),
        "mirror^-3": (A1.inv() * A2, B1.inv() * B2, -3),
    }
    eps = {}
    for nm, (Mp, Mn, k) in words.items():
        eps[nm] = sp.factor(eps_of(Mp ** k, Mn ** k))
    base = eps["V^3"]

    # P1: photon order
    g1 = fs.photon8(0, 0, q * h)
    g2 = fs.photon8(0, 0, -h / q)
    V3 = fs.V8 ** 3
    p1 = all(sp.simplify(x) == 0 for x in (g1 * g2 - V3)) and \
        all(sp.simplify(x) == 0 for x in (g2 * g1 - V3))
    check("P1_both_photon_orders_give_V3", p1,
          "gamma(0,0,qh) gamma(0,0,-h/q) and the reversed order are both V^3 exactly on "
          "(C^2)^{x3}. They are the same element, so M1 counts two ordered factorisations "
          "of one element, not two elements.")

    p2 = all(sp.simplify(eps[nm] - base) == 0 for nm in eps)
    check("P2_orbit_members_have_equal_eps_flavour", p2,
          "eps_flavour of V^-3, mirror^3 and mirror^-3 equals eps_flavour(V^3) exactly, so "
          "summing over the orbit multiplies (does not cancel). Base: "
          f"{base}.")

    E0 = mp.mpf(qbeta_e0.canonical())
    Qbase = abs(mpv(base)) * E0
    import json
    wit = json.loads((_FS.parent / "qbeta-flavour-weight-split.witness.json").read_text())

    def _find(node):
        if isinstance(node, dict):
            if node.get("element") == "V^3" and "Q_beta_MeV" in node:
                return node
            node = list(node.values())
        if isinstance(node, list):
            for x in node:
                hit = _find(x)
                if hit is not None:
                    return hit
        return None
    committed = _find(wit)
    p3 = committed is not None and \
        abs(Qbase - mp.mpf(committed["Q_beta_MeV"])) < mp.mpf(10) ** -25
    check("P3_base_is_the_scored_cell", p3,
          f"|eps_flavour(V^3)| E0 = {mp.nstr(Qbase, 20)} MeV (matches the committed scored cell in qbeta-flavour-weight-split.witness.json).")

    two = mpv(D2)
    three = mpv(q ** 2 + 1 + q ** -2)
    cands = [
        ("M1", "2", mp.mpf(2), "ordered photon pairs giving V^3", "gamma-gamma"),
        ("M3", "2", mp.mpf(2), "{V^3, V^-3}", "NOT gamma-gamma under the 2026-11-20 photon"),
        ("M4", "4", mp.mpf(4), "{V^3, V^-3, mirror^3, mirror^-3}",
         "NOT gamma-gamma under the 2026-11-20 photon"),
        ("M5", "3", mp.mpf(3), "quark strands (colour labels)", "strand count"),
        ("M6", "1", mp.mpf(1), "colour-singlet multiplicity", "strand count"),
        ("M7", "[2]_q", two, "q-dimension of the doublet", "U_q(sl2)"),
        ("M8", "[3]_q", three, "q-dimension of spin 1", "U_q(sl2)"),
    ]
    QB = mp.mpf(str(Q_BETA_MEV_AME))
    rows = []
    print("  id   m        value          Q_beta (MeV)      vs CODATA")
    for cid, lab, m, what, flag in cands:
        Qm = m * Qbase
        pct = (Qm / QB - 1) * 100
        rows.append({"id": cid, "m": lab, "m_value": mp.nstr(m, 25), "counts": what,
                     "flag": flag, "Q_beta_MeV": mp.nstr(Qm, 20),
                     "vs_codata_pct": mp.nstr(pct, 8)})
        print(f"  {cid}  {lab:<7} {mp.nstr(m, 10):>12}  {mp.nstr(Qm, 12):>14}   {mp.nstr(pct, 6):>9} %")
    print()
    need = QB / Qbase
    p4 = all(abs(mp.mpf(r["m_value"]) - need) > mp.mpf("0.1") for r in rows)
    check("P4_no_registered_multiplicity_equals_the_needed_factor", p4,
          f"needed factor = {mp.nstr(need, 12)}; registered values are 1, 2, 3, 4, "
          f"[2]_q = {mp.nstr(two, 8)}, [3]_q = {mp.nstr(three, 8)}. Every one is more than "
          "0.1 away. Integer counts bracket it (2 gives -16.8 %, 3 gives +24.8 %); neither is "
          "selected. Scope (a): this list, nothing beyond it.")

    allp = all(ok for _, ok, _ in RESULTS)
    print(f"  {sum(ok for _, ok, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-derived-multiplicity", engine="mpmath")
    for nm, ok, det in RESULTS:
        wb.add_assertion(nm, computed="PASS" if ok else "FAIL", expected="PASS",
                         tolerance="exact", source=det)
    wb.save({
        "description": ("Route 1 of issue #8833: multiply the scored Q_beta cell by every "
                        "pre-registered corpus-fixed multiplicity. Reported, none selected."),
        "beans": ["qou-cds1", "qou-pdix", "qou-99qc"],
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "E0_canonical_MeV": mp.nstr(E0, 30),
        "eps_flavour_V3": str(base),
        "Q_beta_base_MeV": mp.nstr(Qbase, 30),
        "needed_factor": mp.nstr(need, 20),
        "candidates": rows,
        "scope": "(a): the closed list in PREREGISTRATION.md; nothing is excluded beyond it.",
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
