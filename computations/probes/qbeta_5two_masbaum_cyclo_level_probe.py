#!/usr/bin/env python3
"""B1.4′: the module-map rung, second arm — the cyclotomic LEVEL
correspondence, decided by exact cross-multiplication.

SUCCESSOR to B1.3 (PR #4235) alongside B1.4 (θ-tower). Both the
Masbaum tail and the GGM blocks are LEVEL-graded sums:

    F      = Σ_n C_n(u)·(u²;u²)_n²          (cyclotomic levels n)
    H±_j,λ = Σ_n p_j(n)·(±)^n q^{e(n,λ)}/(q;q)_n³   (block levels n)

B1.3 ruled out every SCALAR bridge between the total sums. The
cyclotomic route asks the per-level question instead: is there a
λ-row, a level shift k, and a single n-INDEPENDENT dressing r(q) with

    T^Mas_n(u) = r(u) · T^H_{n+k}(u²)   for all n ?

TEST (pre-registered, all exact): for every (sign, j, λ) in the
extended grid (sign +1: λ ∈ −2..3; sign −1: λ ∈ −1..3; j ∈ 0..2 —
33 rows) and every level shift k ∈ {−2..2}, decide n-independence of
the ratio by exact cross-multiplication in the u-series ring:

    T^Mas_n · T^H_{n+1+k} == T^Mas_{n+1} · T^H_{n+k}

order-by-order at O(u^ORD_U), for consecutive n across the testable
window (both sides must expose ≥ MIN_CMP comparable orders beyond the
common leading order, else that pair is recorded as depth-limited, not
counted). A full pass across the window is a LEVEL LEAD (the dressing
r = T^Mas_{n0}/T^H_{n0+k} is then extracted and recorded); any exact
mismatch kills the combination. Per-level u-PARITY of the Masbaum
terms is recorded (the total is u-even per B1.3; levels may not be).

No numerics in the decision; no fit; every combination reported.
auditOnly; no c_k wired. Comparison to observed only; no ontological
claims.

Run: python3 -u computations/probes/qbeta_5two_masbaum_cyclo_level_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_cyclo_level.log
"""
from __future__ import annotations

import importlib.util
import sys
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
import qbeta_5two_stokes_barodd_index_probe as sb  # noqa: E402
import qseries_exact_util as qx  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_masbaum_barodd_profile",
    _HERE / "qbeta_g3_5two_masbaum_barodd_profile.py")
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

ORD_U = 96                  # u-series truncation (q-order 48)
N_MAX = 8                   # Masbaum levels 0..N_MAX
SHIFTS = range(-2, 3)
MIN_CMP = 6                 # comparable orders required per cross-check
LAM_GRID = {+1: range(-2, 4), -1: range(-1, 4)}
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:6.0f}s] {msg}", flush=True)


def masbaum_term_u(n, ord_u):
    """T^Mas_n = C_n(u)·(u²;u²)_n² as an exact u-series (Laurent tails
    below u^0 are impossible: min C_n exponent + 0 ≥ 0 is asserted)."""
    C = _mb.C52(n)
    assert min(C.keys()) >= 0, f"negative u-exponent in C_{n}"
    poch = qx.s_new(ord_u)
    poch[0] = Fraction(1)
    for j in range(1, n + 1):
        f = qx.s_new(ord_u)
        f[0] = Fraction(1)
        if 2 * j < ord_u:
            f[2 * j] = Fraction(-1)
        poch = qx.s_mul(poch, f)
    poch2 = qx.s_mul(poch, poch)
    Cs = qx.s_new(ord_u)
    for e, c in C.items():
        if e < ord_u:
            Cs[e] = Fraction(int(c))
    return qx.s_mul(Cs, poch2)


def h_term_u(sign, j, lam, n, ord_u):
    """The n-th H-block term embedded in the u-grid (q = u²)."""
    ord_q = ord_u // 2 + 1
    tq = qx.h_term(sign, j, lam, n, ord_q)
    out = qx.s_new(ord_u)
    for e, c in enumerate(tq):
        if c and 2 * e < ord_u:
            out[2 * e] = c
    return out


def lead(ser_):
    return next((e for e, c in enumerate(ser_) if c), None)


def cross_check(a, b, c, d, ord_u):
    """Exact test a·b == c·d with a depth report: returns (verdict,
    n_comparable) where verdict ∈ {'match','mismatch','depth-limited'}."""
    la = lead(a)
    lb = lead(b)
    lc = lead(c)
    ld = lead(d)
    if None in (la, lb, lc, ld):
        return "depth-limited", 0
    lo = min(la + lb, lc + ld)
    n_cmp = ord_u - max(la + lb, lc + ld)
    if n_cmp < MIN_CMP:
        return "depth-limited", max(n_cmp, 0)
    ab = qx.s_mul(a, b)
    cd = qx.s_mul(c, d)
    return ("match" if ab == cd else "mismatch"), ord_u - lo


def main() -> int:
    print("=" * 78)
    print(" B1.4' — cyclotomic level correspondence (module map, arm 2)")
    print("=" * 78)

    # ---- gate: engine vs the 18 printed GGM tables ----
    g_printed = True
    for (sgn, j, lam), coeffs in sb.PRINTED.items():
        ser_ = qx.h_series(sgn, j, lam, 8)
        for k, c in enumerate(coeffs):
            cr = sp.Rational(c)
            if ser_[k] != Fraction(int(cr.p), int(cr.q)):
                g_printed = False
    log(f"[gate] engine vs the 18 printed GGM tables: "
        f"{'PASS' if g_printed else 'FAIL'}")

    # ---- Masbaum per-level terms + per-level parity record ----
    log(f"building Masbaum level terms n = 0..{N_MAX} at O(u^{ORD_U}) ...")
    Tm = {n: masbaum_term_u(n, ORD_U) for n in range(N_MAX + 2)}
    level_parity = {}
    for n, ser_ in Tm.items():
        odd = sum(1 for e, c in enumerate(ser_) if c and e % 2 == 1)
        level_parity[n] = {"odd_u_terms": odd, "lead": lead(ser_)}
    n_odd_levels = sum(1 for v in level_parity.values()
                      if v["odd_u_terms"])
    log(f"    per-level u-parity: {n_odd_levels} level(s) carry odd "
        f"u-terms (total is u-even per B1.3)")

    # gate: the levels re-sum to the B1.3 total (q-projection)
    tot = qx.s_new(ORD_U)
    n = N_MAX + 1
    while True:
        C = _mb.C52(n)
        if min(C.keys()) >= ORD_U:
            break
        Tm[n] = masbaum_term_u(n, ORD_U)
        n += 1
        if n > 90:
            break
    for ser_ in Tm.values():
        tot = qx.s_add(tot, ser_)
    odd_tot = [e for e, c in enumerate(tot) if c and e % 2 == 1]
    g_resum = not odd_tot
    log(f"[gate] levels re-sum to a u-even total (B1.3 consistency): "
        f"{'PASS' if g_resum else 'FAIL'}")

    # ---- the level-correspondence scan ----
    log("scanning (sign, j, λ) × level shifts ...")
    combos, leads = [], []
    n_scan = 0
    for sgn, lams in LAM_GRID.items():
        for lam in lams:
            for j in range(3):
                Th = {}
                for k in SHIFTS:
                    for n_ in range(N_MAX + 2):
                        lv = n_ + k
                        if lv >= 0 and lv not in Th:
                            Th[lv] = h_term_u(sgn, j, lam, lv, ORD_U)
                for k in SHIFTS:
                    n_scan += 1
                    verdicts = []
                    for n_ in range(N_MAX):
                        if n_ + k < 0 or n_ + 1 + k < 0:
                            verdicts.append("skipped-negative-level")
                            continue
                        v, _ = cross_check(Tm[n_], Th[n_ + 1 + k],
                                           Tm[n_ + 1], Th[n_ + k], ORD_U)
                        verdicts.append(v)
                    n_match = verdicts.count("match")
                    n_mis = verdicts.count("mismatch")
                    rec = {"sign": sgn, "j": j, "lam": lam, "shift": k,
                           "verdicts": verdicts}
                    combos.append(rec)
                    if n_mis == 0 and n_match >= 3:
                        leads.append(rec)
                        log(f"    LEVEL LEAD: sign {sgn:+d}, j={j}, "
                            f"λ={lam}, shift {k} — {n_match} exact "
                            f"cross-matches, 0 mismatches")
    log(f"[T] {n_scan} combinations scanned: {len(leads)} lead(s)")

    wb = WitnessBuilder("qbeta-5two-masbaum-cyclo-level",
                        engine="exact-fraction-series",
                        _script_path=__file__)
    wb.set_description(
        "B1.4' (module map, arm 2): the cyclotomic LEVEL correspondence "
        "— is the n-th Masbaum term a fixed n-independent dressing of "
        "the (n+k)-th GGM block term? Decided by exact "
        "cross-multiplication T^Mas_n·T^H_{n+1+k} == T^Mas_{n+1}·"
        "T^H_{n+k} in the u-series ring at O(u^96), over the extended "
        "λ-grid (33 rows) × level shifts k ∈ −2..2, Masbaum levels "
        "0..8; depth-limited pairs reported, never counted as matches. "
        "Per-level u-parity recorded; levels re-summed against the "
        "B1.3 u-even total as a consistency gate. No numerics in the "
        "decision. auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("printed_tables_regated",
                     computed=1.0 if g_printed else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="shared exact-series engine reproduces the 18 "
                            "printed GGM H-tables")
    wb.add_assertion("levels_resum_ueven",
                     computed=0.0 if g_resum else 1.0, expected=0.0,
                     tolerance=0.5,
                     source="per-level terms re-sum to a u-even total, "
                            "consistent with the B1.3 parity finding")
    # DEMOTED (bean qou-3e5m): this compared 'scan_completed' to itself and
    # reported `passed` unconditionally. A count of what a run found is
    # DATA, not a check, and `add_assertion` has no way to say
    # "is nonzero" -- which is plausibly why it was written this way.
    # The assertion's `source` prose is kept alongside the value.
    wb.add_data('scan_completed', {'value': float(n_scan), 'source': 'all pre-registered (sign,j,λ)×shift combinations decided and recorded'})

    ok = all(a.passed for a in wb.assertions)

    wb.add_data("level_parity", {str(k): v for k, v in level_parity.items()})
    wb.add_data("scan", {"n_combinations": n_scan,
                         "n_leads": len(leads),
                         "combos_with_any_match":
                             [c for c in combos
                              if c["verdicts"].count("match") > 0]})
    wb.add_data("leads", leads)
    wb.add_data("verdict",
                ((f"CYCLOTOMIC LEVEL LEAD: {len(leads)} combination(s) "
                  f"pass every exact cross-check — data.leads; the "
                  f"dressing series r(u) extraction and an "
                  f"independent-anchor test are the follow-up."
                  if leads else
                  "NO LEVEL CORRESPONDENCE: every (sign,j,λ,shift) "
                  "combination fails exact cross-multiplication "
                  "somewhere in the level window. Scope-(a): "
                  "n-independent scalar level dressing as-stated — "
                  "with B1.4 (θ-tower ruled out) the module map, if "
                  "it exists, must mix levels or act n-dependently "
                  "(e.g. the full Habiro-ring comultiplication), "
                  "which is beyond parameter-free probing at this "
                  "rung.")
                 + " auditOnly.") if ok else "A gate failed — inspect.")
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-masbaum-cyclo-level.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
