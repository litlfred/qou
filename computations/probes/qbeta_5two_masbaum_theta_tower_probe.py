#!/usr/bin/env python3
"""B1.4: the module-map rung, first arm — the Euler-descendant tower
and the extended λ-grid, decided by exact linear algebra.

SUCCESSOR to B1.3 (PR #4235): the Masbaum tail lies OUTSIDE the 18-dim
H±_{j,λ} block span for every scalar dressing (q;q)_∞^p·q^s. The named
successors were the MODULE MAP routes. This probe tests the first: the
Habiro-module operators that act on the block basis without leaving
exact q-series land —

  * the Euler operator θ = q·d/dq (the derivative tower), applied as
    θ^m, m ∈ {0,1,2}, to every basis series;
  * the λ-grid extension: λ beyond {−1,0,1} to the full domain where
    the series exponents stay non-negative (sign +1: λ ∈ −2..3;
    sign −1: λ ∈ −1..3), j ∈ {0,1,2} — 33 base series, ×3 θ-levels
    = 99 columns.

TARGETS (pre-registered): θ^t F for t ∈ {0,1,2} — the tail may itself
be a derivative image — each dressed by (q;q)_∞^p·q^s, p ∈ −3..3,
s ∈ 0..2: 63 exact membership decisions at O(q^128) (margin gate:
row-count minus basis rank ≥ 20, so a "solution" is genuinely
overdetermined).

DECISION DISCIPLINE (all exact): basis rank is certified by modular
rank (a 61-bit prime) — full column rank mod p forces full rank over
ℚ; each candidate is first tested mod p (rank_p(aug) > rank_ℚ(M)
certifies OUTSIDE exactly, since rank_ℚ(aug) ≥ rank_p(aug)); only a
mod-p in-span candidate escalates to the exact rational solve. No
numerics anywhere in the decision.

Gates: (1) the shared exact-series engine re-gated against the 18
printed GGM H-tables; (2) series-prefix self-consistency (the O(q^40)
generation is a prefix of the O(q^128) one); (3) the margin gate;
(4) decision completeness.

auditOnly; no c_k wired; no fit. Comparison to observed only; no
ontological claims.

Run: python3 -u computations/probes/qbeta_5two_masbaum_theta_tower_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_theta_tower.log
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

ORD_Q = 128                 # rows of the decision matrix
MARGIN_MIN = 20             # required overdetermination beyond the rank
PRIME = (1 << 61) - 1       # Mersenne prime for the modular fast path
LAM_GRID = {+1: range(-2, 4), -1: range(-1, 4)}
THETA_LEVELS = (0, 1, 2)
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:6.0f}s] {msg}", flush=True)


def masbaum_q_series(ord_q):
    """The Masbaum tail as an exact q-series (B1.3 established u-parity
    EVEN, re-checked here)."""
    ord_u = 2 * ord_q
    out = {}
    n = 0
    while True:
        C = _mb.C52(n)
        if min(C.keys()) >= ord_u and n > 0:
            break
        poch = {0: 1}
        for j in range(1, n + 1):
            new = {}
            for e, c in poch.items():
                new[e] = new.get(e, 0) + c
                e2 = e + 2 * j
                if e2 < ord_u:
                    new[e2] = new.get(e2, 0) - c
            poch = new
        poch2 = {}
        for e1, c1 in poch.items():
            for e2, c2 in poch.items():
                e = e1 + e2
                if e < ord_u:
                    poch2[e] = poch2.get(e, 0) + c1 * c2
        for e1, c1 in C.items():
            if e1 >= ord_u:
                continue
            for e2, c2 in poch2.items():
                e = e1 + e2
                if e < ord_u:
                    out[e] = out.get(e, 0) + int(c1) * c2
        n += 1
        if n > 90:
            break
    odd = [e for e, c in out.items() if e % 2 == 1 and c != 0]
    assert not odd, f"odd u-powers appeared: {odd[:5]}"
    F = qx.s_new(ord_q)
    for e, c in out.items():
        if c != 0 and e // 2 < ord_q:
            F[e // 2] = Fraction(c)
    return F


def frac_mod(x, p):
    num = x.numerator % p
    den = x.denominator % p
    if den == 0:
        raise ZeroDivisionError("denominator divisible by the prime")
    return num * pow(den, p - 2, p) % p


def rank_mod(rows, p):
    """Gaussian elimination over GF(p); rows = list of int lists (mod p)."""
    rows = [r[:] for r in rows]
    ncols = len(rows[0]) if rows else 0
    rank = 0
    for col in range(ncols):
        piv = next((r for r in range(rank, len(rows)) if rows[r][col]), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], p - 2, p)
        rows[rank] = [(v * inv) % p for v in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col]:
                f = rows[r][col]
                rows[r] = [(a - f * b) % p
                           for a, b in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def main() -> int:
    print("=" * 78)
    print(" B1.4 — the Euler-descendant tower + extended λ-grid "
          "(module map, arm 1)")
    print("=" * 78)

    # ---- gate 1: engine re-gate vs the 18 printed GGM tables ----
    g_printed = True
    for (sgn, j, lam), coeffs in sb.PRINTED.items():
        ser_ = qx.h_series(sgn, j, lam, 8)
        for k, c in enumerate(coeffs):
            cr = sp.Rational(c)
            if ser_[k] != Fraction(int(cr.p), int(cr.q)):
                g_printed = False
    log(f"[gate] engine vs the 18 printed GGM tables: "
        f"{'PASS' if g_printed else 'FAIL'}")

    # ---- the basis: 33 base series × 3 θ-levels at O(q^ORD_Q) ----
    log(f"generating the extended basis at O(q^{ORD_Q}) "
        f"(33 base series) ...")
    base = {}
    for sgn, lams in LAM_GRID.items():
        for lam in lams:
            for j in range(3):
                base[(sgn, j, lam)] = qx.h_series(sgn, j, lam, ORD_Q)
        log(f"    sign {sgn:+d} done ({len(base)} series so far)")

    # gate 2: prefix self-consistency at O(q^40) on 3 spot series
    g_prefix = True
    for key in [(+1, 0, -1), (-1, 2, 1), (+1, 2, 3)]:
        short = qx.h_series(*key, 40)
        if short != base[key][:40]:
            g_prefix = False
    log(f"[gate] O(q^40) prefix self-consistency (3 spot series): "
        f"{'PASS' if g_prefix else 'FAIL'}")

    cols = {}
    for key, ser_ in base.items():
        cur = ser_
        for m in THETA_LEVELS:
            cols[key + (m,)] = cur
            cur = qx.s_theta(cur)
    keys = sorted(cols.keys())
    log(f"basis columns with θ-tower: {len(keys)}")

    # ---- rank certification ----
    Mp = [[frac_mod(cols[k][o], PRIME) for k in keys]
          for o in range(ORD_Q)]
    rank_p = rank_mod(Mp, PRIME)
    full_col = rank_p == len(keys)
    # full column rank mod p ⇒ rank over ℚ = column count (exact).
    if full_col:
        rank_Q = len(keys)
        log(f"basis rank mod p = {rank_p} = column count ⇒ "
            f"rank over ℚ = {rank_Q} (certified)")
    else:
        log(f"basis rank mod p = {rank_p} < {len(keys)} — "
            f"computing the exact rational rank ...")
        M = sp.Matrix([[sp.Rational(cols[k][o].numerator,
                                    cols[k][o].denominator)
                        for k in keys] for o in range(ORD_Q)])
        rank_Q = M.rank()
        log(f"exact rank over ℚ = {rank_Q}")
    margin = ORD_Q - rank_Q
    g_margin = margin >= MARGIN_MIN
    log(f"[gate] overdetermination margin {margin} ≥ {MARGIN_MIN}: "
        f"{'PASS' if g_margin else 'FAIL'}")

    # ---- targets: θ^t F dressed by (q;q)_∞^p·q^s ----
    log("building the Masbaum tail + dressings ...")
    F = masbaum_q_series(ORD_Q)
    E_ser = qx.qpoch_inf_ser(ORD_Q)
    E_inv = qx.s_inv(E_ser)

    def dress(p):
        s_ = qx.s_const(1, ORD_Q)
        b_ = E_ser if p > 0 else E_inv
        for _ in range(abs(p)):
            s_ = qx.s_mul(s_, b_)
        return s_

    thF = {0: F, 1: qx.s_theta(F), 2: qx.s_theta(qx.s_theta(F))}
    results, solved = [], []
    n_exact_escal = 0
    M_cache = []

    def exact_M():
        if not M_cache:
            M_cache.append(sp.Matrix(
                [[sp.Rational(cols[k][o].numerator, cols[k][o].denominator)
                  for k in keys] for o in range(ORD_Q)]))
        return M_cache[0]
    for t in (0, 1, 2):
        for p in range(-3, 4):
            Fd = qx.s_mul(thF[t], dress(p))
            for s in range(0, 3):
                tser = qx.s_shift(Fd, s)
                tcol = [frac_mod(x, PRIME) for x in tser]
                aug_p = [row + [tcol[i]] for i, row in enumerate(Mp)]
                r_aug_p = rank_mod(aug_p, PRIME)
                if r_aug_p > rank_Q:
                    in_span = False       # certified: rank_ℚ(aug) ≥ r_aug_p
                else:
                    # potential hit — escalate to the exact rational solve
                    n_exact_escal += 1
                    M = exact_M()
                    tvec = sp.Matrix([sp.Rational(x.numerator,
                                                  x.denominator)
                                      for x in tser])
                    in_span = M.row_join(tvec).rank() == rank_Q
                    if in_span:
                        sol, params = M.gauss_jordan_solve(tvec)
                        if params:
                            sol = sol.subs({pp: 0 for pp in params})
                        solved.append(
                            {"theta": t, "p": p, "shift": s,
                             "coeffs": {str(k): str(sol[i])
                                        for i, k in enumerate(keys)
                                        if sol[i] != 0}})
                        log(f"    IN SPAN: θ^{t}·(q;q)_∞^{p}·q^{s}·F")
                results.append({"theta": t, "p": p, "shift": s,
                                "in_span": bool(in_span)})
    n_solved = len(solved)
    log(f"[T] {len(results)} exact decisions: {n_solved} in-span, "
        f"{len(results) - n_solved} outside "
        f"({n_exact_escal} escalated to the exact rational path)")

    wb = WitnessBuilder("qbeta-5two-masbaum-theta-tower",
                        engine="exact-fraction-series+sympy",
                        _script_path=__file__)
    wb.set_description(
        "B1.4 (module map, arm 1): the Euler-descendant tower θ^m "
        "(m ∈ 0..2) over the extended λ-grid (sign +1: λ ∈ −2..3; "
        "sign −1: λ ∈ −1..3; j ∈ 0..2 — 99 columns) confronted with "
        "θ^t F (t ∈ 0..2) dressed by (q;q)_∞^p·q^s (p ∈ −3..3, "
        "s ∈ 0..2): 63 exact membership decisions at O(q^128), "
        "overdetermination margin gated. Decisions are exact: modular "
        "rank certifies OUTSIDE (rank_p(aug) > rank_Q(M) forces "
        "rank_Q(aug) > rank_Q(M)); mod-p in-span candidates escalate "
        "to the exact rational solve. Engine re-gated against the 18 "
        "printed GGM tables. auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("printed_tables_regated",
                     computed=1.0 if g_printed else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="shared exact-series engine reproduces the 18 "
                            "printed GGM H-tables")
    wb.add_assertion("prefix_self_consistency",
                     computed=1.0 if g_prefix else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="O(q^40) generation is a prefix of the O(q^128) "
                            "generation (3 spot series)")
    wb.add_assertion("overdetermination_margin",
                     computed=float(margin), expected=float(ORD_Q),
                     tolerance=float(ORD_Q - MARGIN_MIN),
                     source=f"rows − rank ≥ {MARGIN_MIN} so membership is "
                            "genuinely overdetermined")
    wb.add_assertion("decision_family_completed",
                     computed=float(len(results)), expected=63.0,
                     tolerance=0.5,
                     source="all 63 pre-registered decisions completed")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("basis", {"columns": len(keys), "rank": int(rank_Q),
                          "rank_certification":
                              "modular (full column rank mod 2^61-1)"
                              if full_col else "exact sympy rational",
                          "order": ORD_Q, "margin": int(margin)})
    wb.add_data("decisions", results)
    wb.add_data("solutions", solved)
    wb.add_data("verdict",
                ((f"MODULE-MAP HIT (θ-tower): {n_solved} decision(s) "
                  f"in-span — coefficient vectors in data.solutions; "
                  f"independent-anchor confirmation is the follow-up."
                  if n_solved else
                  "THE θ-TOWER DOES NOT BRIDGE: θ^t F lies outside the "
                  "99-dim descendant span for every pre-registered "
                  "dressing (63 exact decisions). Scope-(a): this "
                  "operator family as-stated — the Euler tower and the "
                  "λ-grid extension are ruled out as the module map; "
                  "the cyclotomic level structure (B1.4') is the "
                  "remaining named route.")
                 + " auditOnly.") if ok else "A gate failed — inspect.")
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-masbaum-theta-tower.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
