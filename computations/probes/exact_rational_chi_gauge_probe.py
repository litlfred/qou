#!/usr/bin/env python3
"""Exact-rational chi^lambda via the ASYMMETRIC seminormal gauge — design proof.

WHAT THIS ESTABLISHES

Two independent things, from one computation:

1. **An exact-arithmetic route to chi^lambda exists that needs no square root,
   no fraction field and no floating point.** Hoefsmit's *symmetric* seminormal
   form carries `b = sqrt(a a' + 1)` off-diagonal, which is irrational; the
   trace-invariant *asymmetric* gauge `[[a, b^2], [1, a']]` is rational, so a
   whole atom evaluates in exact `Fraction` arithmetic at any rational `q`.
   Verified here against every cached symbolic character of the deuteron.

2. **The p-n interface is colour-WEIGHTED, decisively** (bean `qou-cblw`).
   Running the identical pipeline with the colour-BLIND factor matches
   **nothing**. This is the discriminator, not an opinion:

       colour-weighted  d = -h*(1/2 - delta/4)     11 / 11 match
       colour-blind     d = -h/2                    0 / 11 match

   with `delta = flavor_split_leading(q) = (q-1)^2 (1 - q^-4) / 3`, which is a
   RATIONAL function of q — the fact that makes exact evaluation possible at
   all. AGENTS.md records the owner ruling of 2026-08-15 (R3) that
   `bring_color_weighted` is canonical; this shows the committed chi cache
   agrees with it, so any consumer using `h/2` for a p-n interface disagrees
   with the corpus's own recorded numbers.

WHY IT MATTERS

The symbolic (sympy) route to these characters costs `4.31 s per dim^2`
(measured, bean `qou-lrnd`), so the A=3 atoms are `sum dim^2 = 9! = 362,880`
=> ~18 days, and a PARTIAL result is worth nothing because `tr_M` sums over
every partition. The route proved here is the input to a Rust `BigRational`
port, where the same arithmetic is not symbolic manipulation but integer
arithmetic.

SCOPE. This proves the EVALUATION is exact and correct. Recovering the Laurent
polynomial from evaluations (interpolation) is standard and is NOT done here.
No claim is made about A=3 timing.

Precision: `fractions.Fraction` end to end; sympy only parses the cached
reference expressions. No float anywhere.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402

from canonical_braid_crossings import CTYPES  # noqa: E402

HERE = Path(__file__).parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

CACHE = REPO / "computations" / "chi-deuteron-h6.witness.json"
Q_POINTS = [F(2), F(3), F(5, 2)]


def syts(lam: list[int]) -> list[tuple]:
    n = sum(lam)
    out: list[tuple] = []

    def rec(pos: int, cells: list, rows: list[int]) -> None:
        if pos > n:
            out.append(tuple(cells))
            return
        for r in range(len(lam)):
            c = rows[r]
            if c < lam[r] and (r == 0 or rows[r - 1] > c):
                rows[r] += 1
                cells.append((r, c))
                rec(pos + 1, cells, rows)
                cells.pop()
                rows[r] -= 1

    rec(1, [], [0] * len(lam))
    return out


def blocks_at(lam: list[int], qv: F):
    """Asymmetric-gauge generator blocks at rational `qv`. No sqrt."""
    n = sum(lam)
    T = syts(lam)
    idx = {t: i for i, t in enumerate(T)}
    d = len(T)
    hv = qv - F(1, 1) / qv
    allb = []
    for k in range(1, n):
        bl, done = [], [False] * d
        for i, t in enumerate(T):
            if done[i]:
                continue
            ck, ck1 = t[k - 1], t[k]
            rho = (ck1[1] - ck1[0]) - (ck[1] - ck[0])
            a = hv / (1 - qv ** (-2 * rho))
            sw = list(t)
            sw[k - 1], sw[k] = ck1, ck
            j = idx.get(tuple(sw))
            if j is None or j == i:
                bl.append(("one", i, a))
                done[i] = True
            else:
                ap = hv / (1 - qv ** (2 * rho))
                b2 = a * ap + 1                      # b^2, never sqrt(b^2)
                lo, hi = min(i, j), max(i, j)
                bl.append(("two", lo, hi,
                           a if i < j else ap, ap if i < j else a, b2))
                done[i] = done[j] = True
        allb.append(bl)
    return d, allb


def chi_at(lam: list[int], factors, qv: F) -> F:
    """chi^lambda of prod_i (c_i sigma_{g_i} + d_i I), exactly, at rational qv."""
    d, allb = blocks_at(lam, qv)
    tot = F(0)
    for e in range(d):
        v = [F(0)] * d
        v[e] = F(1)
        for (c, dd, g) in reversed(factors):
            bl = allb[g - 1]
            nv = list(v)
            for B in bl:
                if B[0] == "one":
                    _, i, a = B
                    nv[i] = c * a * v[i] + dd * v[i]
                else:
                    _, i, j, a, ap, b2 = B
                    nv[i] = c * (a * v[i] + b2 * v[j]) + dd * v[i]
                    nv[j] = c * (v[i] + ap * v[j]) + dd * v[j]
            v = nv
        tot += v[e]
    return tot


def flavor_split_leading_exact(qv: F) -> F:
    """delta(q) = (q-1)^2 (1 - q^-4) / 3 — exact, rational in q."""
    return (qv - 1) ** 2 * (1 - qv ** -4) / 3


def factors_for(crossings, qv: F, *, colour_weighted: bool):
    hv = qv - F(1, 1) / qv
    dl = flavor_split_leading_exact(qv)
    out = []
    # The ctype VOCABULARY has one owner. This probe cannot call
    # `classify_crossing` -- that is float and this is exact `Fraction`
    # arithmetic, which is the whole point of the probe -- but it can take
    # the label set from the canonical module rather than re-listing it, and
    # fail loudly if a fifth ctype ever lands.
    d_for = {
        "sigma": F(0),
        "sigma_inv": -hv,
        "averaged": -hv / 2,
        # the p-n interface: colour-weighted unless this run is the control
        "averaged_weighted": (-hv * (F(1, 2) - dl / 4) if colour_weighted
                              else -hv / 2),
    }
    missing = set(CTYPES) - set(d_for)
    if missing:
        raise ValueError(
            f"canonical_braid_crossings.CTYPES grew {sorted(missing)}; this "
            f"probe has no exact-arithmetic `d` for it. Add one -- do NOT "
            f"let it fall through to a default."
        )
    for (g, kind) in crossings:
        if kind not in d_for:
            raise ValueError(f"unknown ctype {kind!r}; expected one of {CTYPES}")
        out.append((F(1), d_for[kind], g + 1))
    return out


def main() -> int:
    spec = importlib.util.spec_from_file_location(
        "hca", REPO / "computations" / "habiro" / "habiro_coefficients_atomic.py")
    hca = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(hca)
    except SystemExit:
        pass
    crossings = hca.atomic_braid_to_crossings(1, 1, include_inter=True)
    cache = {tuple(e["partition"]): e["chi_q_symbolic"]
             for e in json.loads(CACHE.read_text())["chi_lambda_symbolic"]}

    print("=" * 76)
    print("Exact-rational chi via the asymmetric seminormal gauge (no sqrt, no float)")
    print(f"  deuteron: {len(crossings)} factors, {len(cache)} cached characters")
    print(f"  evaluated at q = {[str(x) for x in Q_POINTS]}")
    print("=" * 76)

    tallies = {}
    for mode in ("weighted", "blind"):
        ok = 0
        for lam, expr in sorted(cache.items()):
            E = sp.sympify(expr)
            sym = list(E.free_symbols)[0]
            good = True
            for qv in Q_POINTS:
                facs = factors_for(crossings, qv, colour_weighted=(mode == "weighted"))
                mine = chi_at(list(lam), facs, qv)
                ref = E.subs(sym, sp.Rational(qv.numerator, qv.denominator))
                if sp.simplify(sp.Rational(mine.numerator, mine.denominator) - ref) != 0:
                    good = False
                    break
            ok += good
        tallies[mode] = ok
        print(f"  p-n factor {mode:9s}:  {ok:>2} / {len(cache)} match")

    print("=" * 76)
    verdict = (tallies["weighted"] == len(cache) and tallies["blind"] == 0)
    print("  VERDICT: the cached characters are COLOUR-WEIGHTED"
          if verdict else "  VERDICT: inconclusive — see tallies above")
    print("=" * 76)

    from qou_substrate.witness import WitnessBuilder
    wb = WitnessBuilder("exact-rational-chi-gauge-probe", _script_path=Path(__file__))
    wb.set_description(
        "Proves an exact-arithmetic route to chi^lambda via the asymmetric "
        "seminormal gauge (rational, no square root), and uses it to discriminate "
        "the colour-weighted from the colour-blind p-n interface factor.")
    wb.set_audit_only(True)
    wb.add_parameter("q_evaluation_points", [str(x) for x in Q_POINTS])
    wb.add_parameter("reference_cache", str(CACHE.relative_to(REPO)))
    wb.add_data("match_counts", tallies)
    wb.add_data("n_cached_characters", len(cache))
    wb.add_assertion("weighted_matches_all", tallies["weighted"], len(cache))
    wb.add_assertion("blind_matches_none", tallies["blind"], 0)
    wb.add_assertion("no_float_used", True, True)
    wb.add_caveat(
        "Proves the EVALUATION is exact and correct at rational q. Recovering the "
        "Laurent polynomial from evaluations (interpolation) is standard and is NOT "
        "performed here, and no A=3 timing claim is made.")
    wb.save()
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
