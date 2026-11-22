#!/usr/bin/env python3
"""
manybody_term_admissible_window_probe — the admissible window for a many-body
binding term, per isotope. It RETRACTS #6402's "switch-off constraint" (my own
claim, merged one turn earlier), excludes two candidate shapes, and shows no
many-body term of any shape can address the deuteron.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.

## The method — parameter-free, and it tests shapes without fitting one

#6402 bracketed each isotope between the two extreme pairwise bond sets. Turn
that into a constraint on an ADDITIVE many-body term `T`: a pairwise bond set
plus `T` can reach `B_AME` exactly when

    B_AME - B_allpairs  <=  T  <=  B_AME - B_chain

because the pairwise part is free to range over `[B_chain, B_allpairs]`. That
window is computed from `q0` and AME with nothing fitted, and a candidate SHAPE
`T = c * k(A)` is admissible iff a single `c` lies in every isotope's window
simultaneously.

## The windows

    iso   A |      T_min       T_max     width | C(A,4)  floor(A/4)
    2H    2 |  -0.6085964  -0.6085964       0.0 |      0          0
    3H    3 |  -0.4914354    2.341727   2.83316 |      0          0
    3He   3 |  -0.4898700    2.343293   2.83316 |      0          0
    4He   4 |  11.1145200   19.614010   8.49949 |      1          1
    6Li   6 | -11.0499500   17.463840   28.5138 |     15          1
    7Li   7 | -22.2190700   21.408030   43.6271 |     35          1

## Three findings, and the first is a retraction of my own

**(1) RETRACTED — #6402's "switch-off constraint".** That PR claimed: *"a term
calibrated at 4He and applied uniformly would push 6Li and 7Li FURTHER out...
whatever the term is, it must switch off or be absorbed once the alpha is
embedded"*, and called it free, from the bracket. **It is wrong.** A single
constant per complete alpha, firing EQUALLY at 4He, 6Li and 7Li, is admissible
with

    c in [11.1145, 17.4638] MeV      -- NON-EMPTY

so the term does **not** have to switch off. My error was specific and worth
naming: I tested the term against the ALL-PAIRS value only (`43.04 + 11.11 =
54.16` against `B_AME(6Li) = 31.99`, hence "pushed further out"), when the
correct test is whether SOME pairwise set plus `T` reaches AME. With a smaller
bond set it does. **I checked one endpoint of the bracket instead of the
bracket.**

**(2) EXCLUDED — `T = c * C(A,4)`**, the 4-subset-counting shape: the window is
`[11.1145, 0.6117]`, empty. 4He needs `c >= 11.11` while 7Li (35 four-subsets)
caps it at `0.61`. Also excluded: **`T = c` constant in A** (window
`[11.1145, 2.3417]`, empty) -- so the term cannot be A-independent either; it
must grow with the alpha count but far more slowly than `C(A,4)`.

**(3) NO many-body term can address the deuteron, and this is forced.** At `A=2`
the chain and complete graph coincide (one bond), so the window has ZERO WIDTH:
`T(2H) = -0.6086` exactly. Any genuine `>=3`-body term must VANISH at `A = 2` --
there are not enough nucleons -- so no such term can supply `-0.6086`. The
deuteron defect is therefore located in the PAIRWISE sector, specifically the
single p-n bond being 27 % too strong. That confirms #6402's three-regime split
and pins the deuteron leg exactly.

## Scope

Scope **(a)**. No many-body term is proposed, derived or fitted -- what is
computed is the window a term would have to live in, plus two shape exclusions.
`c in [11.11, 17.46]` is a CONSTRAINT, not a value: choosing a `c` inside it
against AME would be a fit and is not done here.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin, exact `math.comb`.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import json  # noqa: E402
from math import comb  # noqa: E402  # float64-ok: exact int, never float

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 50

ISO = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
       ("6Li", 3, 3), ("7Li", 3, 4)]


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    from codata_constants import M_E_MEV as _me
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h = q0 - 1 / q0
    z = q0**3 / (q0**2 + 1)
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    al = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    dlt = flavor_split_leading(q0)
    wr = mp.log(1 - h)

    def L(d, e):
        return -mp.log(z + d) - (e / 2) * wr

    Lpp = L(mp.mpf(0), mp.mpf(1))
    Lnn = L(-h, mp.mpf(-1))
    Lpn = L(-h * (mp.mpf(1) / 2 - dlt / 4), 2 * (mp.mpf(1) / 2 - dlt / 4) - 1)

    p = _Path(__file__).resolve().parent / "data" / "ame2020.json"
    raw = json.loads(p.read_text())
    ent = raw["entries"] if isinstance(raw, dict) and "entries" in raw else raw
    rows = ent.values() if isinstance(ent, dict) else ent
    B = {(r["Z"], r["A"]): mp.mpf(str(r["binding_energy_total_keV"])) / 1000
         for r in rows if r.get("binding_energy_total_keV") is not None}

    print("manybody_term_admissible_window_probe")
    print("=" * 78)
    print("METHOD.  A pairwise bond set plus an additive many-body term T can")
    print("reach B_AME exactly when")
    print("    B_AME - B_allpairs  <=  T  <=  B_AME - B_chain")
    print("since the pairwise part ranges freely over [B_chain, B_allpairs].")
    print("Computed from q0 and AME with nothing fitted.")
    print()
    print(f"{'iso':>5} {'A':>2} {'T_min':>12} {'T_max':>12} {'width':>10} "
          f"{'C(A,4)':>7} {'floor(A/4)':>11}")
    W = {}
    for nm, Z, N in ISO:
        A = Z + N
        ch = al * ((Z - 1) * Lpp + Lpn + (N - 1) * Lnn)
        ap = al * (comb(Z, 2) * Lpp + Z * N * Lpn + comb(N, 2) * Lnn)
        lo, hi = B[(Z, A)] - ap, B[(Z, A)] - ch
        W[nm] = (lo, hi, A)
        print(f"{nm:>5} {A:>2} {fmt(lo, 7):>12} {fmt(hi, 7):>12} "
              f"{fmt(hi - lo, 6):>10} {comb(A, 4):>7} {A // 4:>11}")
    print()

    # ---- (3) first, because it is forced and it scopes the rest -----------
    lo2, hi2, _ = W["2H"]
    print("NO MANY-BODY TERM CAN ADDRESS THE DEUTERON — and this is forced")
    print("-" * 78)
    print(f"  At A = 2 chain and complete graph COINCIDE (one bond), so the")
    print(f"  window has ZERO WIDTH: T(2H) = {fmt(lo2, 8)} exactly.")
    assert abs(hi2 - lo2) < mp.mpf(10) ** -30, "the A=2 window must be a point"
    print("  Any genuine >=3-body term VANISHES at A = 2 -- not enough nucleons")
    print("  -- so no such term can supply that value.  The deuteron defect is")
    print("  in the PAIRWISE sector: the single p-n bond is 27 % too strong.")
    print("  This confirms #6402's three-regime split and pins the deuteron leg.")
    print()

    # ---- shape tests, excluding 2H as a pairwise defect --------------------
    print("SHAPE TESTS (excluding 2H, a pairwise defect, per the above)")
    print("-" * 78)
    W3 = {k: v for k, v in W.items() if k != "2H"}
    print(f"{'shape':>30} {'admissible c':>28} {'verdict':>18}")
    results = {}
    for name, f in (("c * C(A,4)", lambda A: mp.mpf(comb(A, 4))),
                    ("c * floor(A/4)  [per alpha]", lambda A: mp.mpf(A // 4)),
                    ("c  (constant in A)", lambda A: mp.mpf(1))):
        los, his, bad = [], [], None
        for nm, (lo, hi, A) in W3.items():
            k = f(A)
            if k == 0:
                if not (lo <= 0 <= hi):
                    bad = nm
                    break
                continue
            los.append(lo / k)
            his.append(hi / k)
        if bad:
            results[name] = None
            print(f"{name:>30} {'--':>28} {'EXCLUDED by ' + bad:>18}")
            continue
        cmin, cmax = max(los), min(his)
        ok = cmin <= cmax
        results[name] = (cmin, cmax) if ok else None
        print(f"{name:>30} {'[' + fmt(cmin, 6) + ', ' + fmt(cmax, 6) + ']':>28} "
              f"{('ADMISSIBLE' if ok else 'EXCLUDED (empty)'):>18}")
    print()
    assert results["c * C(A,4)"] is None, "C(A,4) must be excluded"
    assert results["c  (constant in A)"] is None, "A-independent must be excluded"
    assert results["c * floor(A/4)  [per alpha]"] is not None, \
        "per-alpha must be admissible"
    print("  C(A,4) is excluded because 4He needs c >= 11.11 while 7Li, with 35")
    print("  four-subsets, caps it at 0.61.  A constant in A is excluded because")
    print("  the A=3 window tops out at 2.34.  So the term must grow with the")
    print("  alpha count, but FAR more slowly than C(A,4).")
    print()

    # ---- (1) the retraction ------------------------------------------------
    cmin, cmax = results["c * floor(A/4)  [per alpha]"]
    print("RETRACTION — #6402's 'switch-off constraint' is WRONG")
    print("-" * 78)
    print("  #6402 (mine, merged one turn earlier) claimed: 'a term calibrated at")
    print("  4He and applied uniformly would push 6Li and 7Li FURTHER out ...")
    print("  whatever the term is, it must switch off or be absorbed once the")
    print("  alpha is embedded', and called it free, from the bracket.")
    print()
    print(f"  It is wrong.  A single constant per complete alpha, firing EQUALLY")
    print(f"  at 4He, 6Li and 7Li, is admissible with c in "
          f"[{fmt(cmin, 7)}, {fmt(cmax, 7)}] MeV.")
    print("  The term does NOT have to switch off.")
    print()
    print("  MY ERROR, named precisely: I tested the term against the ALL-PAIRS")
    _lo6, _hi6, _ = W["6Li"]
    ap6 = B[(3, 6)] - _lo6
    print(f"  value ONLY -- {fmt(ap6, 6)} + 11.11 = {fmt(ap6 + cmin, 6)} against")
    print(f"  B_AME(6Li) = {fmt(B[(3, 6)], 6)}, hence 'pushed further out'.  But")
    print("  the correct test is whether SOME pairwise set plus T reaches AME,")
    print("  and with a smaller bond set it does.  I CHECKED ONE ENDPOINT OF THE")
    print("  BRACKET INSTEAD OF THE BRACKET.")
    print()

    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * c in [11.11, 17.46] is a CONSTRAINT, not a value.  Choosing a c")
    print("    inside it against AME would be a fit and is not done here.")
    print("  * NOT that a per-alpha term is right -- only that the bracket does")
    print("    not exclude it, where it does exclude C(A,4) and A-independence.")
    print("  * Admissibility is necessary, not sufficient: it says a pairwise")
    print("    bond set EXISTS that would work, not that the framework derives")
    print("    that particular set.  Which graph remains open.")
    print("  * Only six isotopes.  A wider table would narrow these windows and")
    print("    could exclude the per-alpha shape too.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
