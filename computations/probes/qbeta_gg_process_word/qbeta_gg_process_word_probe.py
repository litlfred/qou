#!/usr/bin/env python3
"""qbeta_gg_process_word_probe — x = ε(p e⁻ ν̄) on linked 9-strand process words (issue #8833).

Closed family, value and reporting rules: PREREGISTRATION.md (committed first). Owner ruling
2026-11-21: the γγ lepton pair is e⁻ + ν̄ + an extra unknot on 6 strands.

x(W) = Tr(K^{⊗9} P ρ(W)) / [2]⁹ with P = (nucleon strands 0-2 at weight q) ⊗ (lepton strands
3-8 at weight q⁻²). Jimbo R; mpmath at the proton pin. Family enumeration is exact (q = 2, 3
Fractions, via the 5-strand probe's routines). Nothing is selected or scored.

Checks
  P1  ε_p(β_Bor) at q₀ reproduces the scored 0.40872 (nucleon rule on 3 strands).
  P2  for X = 1 every x factorises as ε_p · f_L (f_L on the 6 lepton strands).
  P3  the lepton family: 60 e⁻ν̄ + 60 mirror words (<= 5 vertices), as in the enumeration.
  P4  report: x for every word, window hits, none selected.
"""
from __future__ import annotations

import importlib.util
import itertools
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_GG = _ROOT / "computations/probes/qbeta_gg_lepton_pair/qbeta_gg_lepton_pair_probe.py"
_spec = importlib.util.spec_from_file_location("_gg", _GG)
gg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gg)

mp.mp.dps = 60
Q0 = mp.mpf(Q_50_DIGIT_STR)
D2 = Q0 + 1 / Q0
WINDOW = (mp.mpf("0.33174"), mp.mpf("0.40872"))
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def shift(word, k):
    return [(i + k, s) for (i, s) in word]


def downs(b, n, strands):
    return sum((b >> (n - 1 - p)) & 1 for p in strands)


def sector_trace(word, n, basis, q):
    tot = mp.mpf(0)
    for b in basis:
        v = {b: mp.mpf(1)}
        for (i, s) in reversed(word):
            v = gg.apply_crossing(v, n, i, s, q)
        if v.get(b):
            kw = q ** (n - 2 * bin(b).count("1"))
            tot += kw * v[b]
    return tot


def perm_identity(word, n):
    pos = list(range(n))
    for (i, _s) in word:
        pos[i], pos[i + 1] = pos[i + 1], pos[i]
    return pos == list(range(n))


def main() -> int:
    beta = gg.gg_word((0, 0, 0))
    b3 = [b for b in range(8) if bin(b).count("1") == 1]
    eps_p = sector_trace(beta, 3, b3, Q0) / D2 ** 3
    check("P1_eps_p_reproduced", abs(eps_p - mp.mpf("0.40872")) < mp.mpf("1e-5"),
          f"eps_p = q tr_(W_p)(beta_Bor)/[2]^3 at q0 = {mp.nstr(eps_p, 15)}.")

    # lepton family on 6 strands (exact identification at q = 2, 3)
    QS = (Fr(2), Fr(3))
    ref = {q: gg.inv([(0, 1), (1, 1), (0, 1)], 5, q) for q in QS}
    refm = {q: gg.inv([(0, -1), (1, -1), (0, -1)], 5, q) for q in QS}
    leps = []
    for L in range(1, 6):
        for vs in itertools.product(range(4), repeat=L):
            w = gg.gg_word(vs)
            k, lk2, _sc = gg.strand_data(w, 6)
            if k != 4:
                continue
            lks = sorted(abs(lk2[a][c]) // 2 for a in range(4) for c in range(a + 1, 4))
            if lks != [0, 0, 0, 0, 0, 1]:
                continue
            val = {q: gg.inv(w, 6, q) for q in QS}
            m = "e-nubar" if val == ref else ("mirror" if val == refm else None)
            if m:
                leps.append((vs, m))
    ne = sum(1 for _, m in leps if m == "e-nubar")
    nm = len(leps) - ne
    check("P3_lepton_family", ne == 60 and nm == 60,
          f"{ne} e-nubar + {nm} mirror 6-strand gamma-gamma words (<= 5 vertices).")

    # junction family: products of V1, V2 (0..6 vertices) with identity permutation
    juncs = []
    for L in range(0, 7):
        for vs in itertools.product((1, 2), repeat=L):
            if perm_identity(gg.gg_word(vs), 9):
                juncs.append(vs)
    print(f"  junction words with identity permutation: {len(juncs)}")

    n = 9
    P = [b for b in range(2 ** n)
         if downs(b, n, range(3)) == 1 and downs(b, n, range(3, 9)) == 4]
    b6 = [b for b in range(64) if bin(b).count("1") == 4]
    rows = []
    fac_ok = True
    for lv, m in leps:
        lw = gg.gg_word(lv)
        f_L = sector_trace(lw, 6, b6, Q0) / D2 ** 6
        for X in juncs:
            W = gg.gg_word(X) + beta + shift(lw, 3)
            x = sector_trace(W, n, P, Q0) / D2 ** n
            if not X:
                fac_ok &= abs(x - eps_p * f_L) < mp.mpf("1e-40")
            rows.append({"lepton": "".join(f"V{i+3}" for i in lv), "lepton_kind": m,
                         "junction": "".join(f"V{i}" for i in X), "junction_vertices": len(X),
                         "x": mp.nstr(x, 20), "f_L": mp.nstr(f_L, 20),
                         "in_window": bool(WINDOW[0] < x < WINDOW[1])})
    check("P2_unlinked_words_factorise", fac_ok,
          "for X = 1 every x equals eps_p * f_L to 1e-40 (the product case of #8868).")
    xs = [mp.mpf(r["x"]) for r in rows]
    hits = [r for r in rows if r["in_window"]]
    linked = [mp.mpf(r["x"]) for r in rows if r["junction_vertices"]]
    unl = [mp.mpf(r["x"]) for r in rows if not r["junction_vertices"]]
    det = (f"{len(rows)} words ({len(leps)} lepton x {len(juncs)} junction). x range all "
           f"[{mp.nstr(min(xs), 8)}, {mp.nstr(max(xs), 8)}]; unlinked "
           f"[{mp.nstr(min(unl), 8)}, {mp.nstr(max(unl), 8)}]; linked "
           f"[{mp.nstr(min(linked), 8)}, {mp.nstr(max(linked), 8)}]. In window "
           f"(0.33174, 0.40872): {len(hits)} (e-nubar {sum(r['lepton_kind']=='e-nubar' for r in hits)}, "
           f"mirror {sum(r['lepton_kind']=='mirror' for r in hits)}). None selected.")
    check("P4_report", True, det)
    for r in hits[:20]:
        print("   ", r)

    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-gg-process-word", engine="mpmath")
    for nm_, o, d in RESULTS:
        wb.add_assertion(nm_, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="exact" if nm_ != "P1_eps_p_reproduced" else "1e-5", source=d)
    wb.save({
        "description": ("x = Tr(K^9 P rho(W))/[2]^9 on linked 9-strand words W = X beta_Bor L "
                        "(owner option 3: e- + nu-bar + loop on 6 strands). Nothing selected."),
        "q0": Q_50_DIGIT_STR, "eps_p": mp.nstr(eps_p, 30),
        "window": ["0.33174", "0.40872"], "junctions": ["".join(f"V{i}" for i in X) for X in juncs],
        "rows": rows,
        "caveats": ["x is a restricted-sector trace, not a link invariant.",
                    "the window cannot separate e-nubar from e+nu."],
    })
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
