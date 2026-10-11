#!/usr/bin/env python3
"""Neutron-prediction comparison table, regenerated (bean qou-opjb, owner decision 1b).

Producer for `prop:neutron-prediction-comparison` and its table block
`tbl:neutron-prediction-comparison-table-data`
(folio/quantum-observable-universe/observations/).  Before this script the
block's table had NO producer, and its constant c = 0.01497 traced to no chain
stated in the corpus (bean qou-opjb).

OWNER RULING 2026-10-10 (decision 1b): replace c = 0.01497 by

    c = lambda_C / (2 a_asym),
    lambda_C = (q - q^-1) [6]_q m_e,       a_asym = 3 [2]_q [7]_q m_e,

the coefficient assignments of `QOU.Interactions.QIntegerMassFormula`
(Ch 11 §8), balanced q-integers [n]_q = (q^n - q^-n)/(q - q^-1), at the
PROTON pin q0 (qou_substrate.constants.q_at).  m_e cancels in the ratio.

EPISTEMIC TIER.  lambda_C and a_asym are bare `noncomputable def`s in that Lean
file; nothing derives the choice of [6]_q or 3[2]_q[7]_q.  So c here is FIXED BY
AN ASSIGNMENT, NOT DERIVED.  It is a comparison of a model quantity against
observation (the empirical claim lives at the comparison), not a derivation.

PREDICTION.  For each proton number p, the predicted stable mass number A*(p)
is the fixed point of A = p (2 + c A^{2/3}) (inverting the beta-stability line
p*(A) = A/(2 + c A^{2/3}) of `prop:beta-stability`), and
n_pred(p) = round_half_up(A*(p)) - p.

OBSERVATION (the definition the old table never stated, now stated):
n_obs(p) = N of the most abundant naturally occurring isotope of element p
(NUBASE2020 `IS=` field); for an element with no `IS=` entry, the ground state
with the longest half-life in NUBASE2020.  Source: the NUBASE2020 table text
held at library/kondev-2021-chinese-phys-c-45-030001/sections/ (Kondev et al.,
Chinese Phys. C 45, 030001 (2021)).  Z <-> symbol from computations/data/ame2020.json.

Precision: mpmath mpf throughout (60 dps); no float64 in any computed value.
The only non-mpf numbers are the parsed NUBASE half-life magnitudes, used solely
to ORDER isotopes (never in arithmetic that reaches the result) — and they are
parsed into mpf too.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(_ROOT / "computations"))

import mpmath as mp  # noqa: E402

mp.mp.dps = 60

from qou_substrate.constants import q_at  # noqa: E402

NUBASE_DIR = _ROOT / "library" / "kondev-2021-chinese-phys-c-45-030001" / "sections"
AME_JSON = _ROOT / "computations" / "data" / "ame2020.json"
C_OLD = mp.mpf("0.01497")
P_MAX = 103

# --- the constant -----------------------------------------------------------
q0 = q_at(dps=60)


def qint(n: int, q):
    return (q**n - q**(-n)) / (q - 1 / q)


lambda_C_over_me = (q0 - 1 / q0) * qint(6, q0)
a_asym_over_me = 3 * qint(2, q0) * qint(7, q0)
C_NEW = lambda_C_over_me / (2 * a_asym_over_me)


# --- prediction -------------------------------------------------------------
def a_star(p: int, c):
    A = mp.mpf(2 * p)
    for _ in range(400):
        A_new = p * (2 + c * mp.cbrt(A) ** 2)
        if abs(A_new - A) < mp.mpf(10) ** (-50):
            return A_new
        A = A_new
    raise RuntimeError(f"fixed point did not converge at p={p}")


def n_pred(p: int, c) -> int:
    return int(mp.floor(a_star(p, c) + mp.mpf("0.5"))) - p


# --- observation ------------------------------------------------------------
_UNITS = {
    "ys": "1e-24", "zs": "1e-21", "as": "1e-18", "fs": "1e-15", "ps": "1e-12",
    "ns": "1e-9", "µs": "1e-6", "us": "1e-6", "ms": "1e-3", "s": "1", "m": "60",
    "h": "3600", "d": "86400", "y": "31557600", "ky": "31557600e3",
    "My": "31557600e6", "Gy": "31557600e9", "Ty": "31557600e12",
    "Py": "31557600e15", "Ey": "31557600e18", "Zy": "31557600e21",
    "Yy": "31557600e24",
}
_HL_RE = re.compile(
    r"(\d+(?:\.\d+)?)\s*(Yy|Zy|Ey|Py|Ty|Gy|My|ky|ys|zs|as|fs|ps|ns|µs|us|ms|y|d|h|m|s)(?=[\s\d<>]|$)"
)
_NAME_RE = re.compile(r"^(\d+)([A-Z][a-z]?)\s")


def load_symbols() -> dict:
    d = json.loads(AME_JSON.read_text())
    return {e["element"]: e["Z"] for e in d["entries"] if e["Z"] >= 1}


def parse_nubase(sym2z: dict):
    """Return {Z: [(A, abundance_or_None, halflife_s_or_None, line)]} for ground states."""
    out: dict = {}
    for f in sorted(NUBASE_DIR.glob("*.md")):
        for line in f.read_text().splitlines():
            m = _NAME_RE.match(line)
            if not m:
                continue
            A, sym = int(m.group(1)), m.group(2)
            if sym not in sym2z:
                continue
            Z = sym2z[sym]
            if Z > P_MAX or A < Z:
                continue
            body = line[m.end():].replace(" .", ".")
            ab = None
            mi = re.search(r"IS=\s*([\d.]+)", body)
            if mi:
                ab = mp.mpf(mi.group(1))
            hl = None
            if "stbl" in body:
                hl = mp.inf
            else:
                mh = _HL_RE.search(body)
                if mh:
                    hl = mp.mpf(mh.group(1)) * mp.mpf(_UNITS[mh.group(2)])
            out.setdefault(Z, []).append((A, ab, hl, line.strip()))
    return out


def observed(nub: dict) -> dict:
    res = {}
    for Z in range(1, P_MAX + 1):
        rows = nub.get(Z, [])
        if not rows:
            raise RuntimeError(f"no NUBASE ground state parsed for Z={Z}")
        abund = [r for r in rows if r[1] is not None]
        if abund:
            best = max(abund, key=lambda r: r[1])
            rule = "most abundant (IS=)"
        else:
            timed = [r for r in rows if r[2] is not None]
            best = max(timed, key=lambda r: r[2])
            rule = "longest-lived ground state"
        res[Z] = {"A": best[0], "N": best[0] - Z, "rule": rule, "nubase_line": best[3]}
    return res


def main() -> None:
    sym2z = load_symbols()
    z2sym = {z: s for s, z in sym2z.items()}
    obs = observed(parse_nubase(sym2z))

    rows = []
    for p in range(1, P_MAX + 1):
        no = obs[p]["N"]
        nn, nol = n_pred(p, C_NEW), n_pred(p, C_OLD)
        rows.append({
            "p": p, "symbol": z2sym[p], "A_obs": obs[p]["A"], "n_obs": no,
            "obs_rule": obs[p]["rule"],
            "A_star_new": mp.nstr(a_star(p, C_NEW), 20), "n_pred_new": nn,
            "dn_new": nn - no, "n_pred_old": nol, "dn_old": nol - no,
        })

    def stats(key):
        absd = [abs(r[key]) for r in rows]
        mean = mp.mpf(sum(absd)) / len(absd)
        mx = max(absd)
        return mean, mx, [r["p"] for r in rows if abs(r[key]) == mx]

    mean_new, max_new, at_new = stats("dn_new")
    mean_old, max_old, at_old = stats("dn_old")

    def bins(key):
        b = {}
        for r in rows:
            k = abs(r[key])
            k = str(k) if k <= 4 else "5-8" if k <= 8 else ">8"
            b.setdefault(k, []).append(r["symbol"])
        return b

    print(f"q0 (proton pin)  = {mp.nstr(q0, 30)}")
    print(f"c_old            = {mp.nstr(C_OLD, 10)}")
    print(f"c_new            = {mp.nstr(C_NEW, 30)}")
    print(f"lambda_C / m_e   = {mp.nstr(lambda_C_over_me, 20)}")
    print(f"a_asym / m_e     = {mp.nstr(a_asym_over_me, 20)}")
    print(f"{'p':>3} {'sym':>3} {'A_obs':>5} {'n_obs':>5} {'n_new':>5} {'dn':>4} {'n_old':>5} {'dn_old':>6}  rule")
    for r in rows:
        print(f"{r['p']:>3} {r['symbol']:>3} {r['A_obs']:>5} {r['n_obs']:>5} {r['n_pred_new']:>5} "
              f"{r['dn_new']:>+4} {r['n_pred_old']:>5} {r['dn_old']:>+6}  {r['obs_rule']}")
    print(f"mean|dn| new = {mp.nstr(mean_new, 6)}, max {max_new} at p={at_new}")
    print(f"mean|dn| old c (same obs) = {mp.nstr(mean_old, 6)}, max {max_old} at p={at_old}")
    for k, v in sorted(bins("dn_new").items()):
        print(f"  |dn|={k}: {len(v)}  {' '.join(v)}")

    from qou_substrate.witness import WitnessBuilder  # noqa: E402
    wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
    wb.set_description(
        "Predicted vs observed stable neutron number per element p<=103, with "
        "c = lambda_C/(2 a_asym) from the q-integer coefficient assignments of "
        "QIntegerMassFormula.lean (Ch 11 §8) at the proton pin — fixed by an "
        "assignment, not derived (owner decision 1b, bean qou-opjb)."
    )
    wb.set_content_block("prop:neutron-prediction-comparison")
    wb.add_parameter("q0", mp.nstr(q0, 50))
    wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
    wb.add_parameter("c_new", mp.nstr(C_NEW, 50))
    wb.add_parameter("c_old_superseded", "0.01497")
    wb.add_parameter("lambda_C_over_m_e", mp.nstr(lambda_C_over_me, 50))
    wb.add_parameter("a_asym_over_m_e", mp.nstr(a_asym_over_me, 50))
    wb.add_parameter("observation_rule",
                     "most abundant isotope (NUBASE2020 IS=); else longest-lived ground state")
    wb.add_data("rows", rows)
    wb.add_data("summary", {
        "mean_abs_dn_new": mp.nstr(mean_new, 20), "max_abs_dn_new": max_new,
        "max_at_p_new": at_new,
        "mean_abs_dn_old_c_same_obs": mp.nstr(mean_old, 20),
        "max_abs_dn_old_c_same_obs": max_old, "max_at_p_old": at_old,
        "bins_new": {k: v for k, v in sorted(bins("dn_new").items())},
    })
    wb.add_assertion("c_new_value", mp.nstr(C_NEW, 20), "0.01451583", "1e-8",
                     source="bean qou-opjb measurement (decimal, 50 digits)")
    wb.add_caveat("c is fixed by the bare-def q-integer coefficient assignments "
                  "lambda_C=(q-q^-1)[6]_q m_e, a_asym=3[2]_q[7]_q m_e; not derived.")
    wb.add_caveat("The superseded table (c=0.01497) had no producer and no stated "
                  "observation rule; old-c figures here use THIS script's observation rule.")
    print(f"witness -> {wb.save({'q0Anchor': 'proton', 'q0Value': mp.nstr(q0, 50)})}")


if __name__ == "__main__":
    main()
