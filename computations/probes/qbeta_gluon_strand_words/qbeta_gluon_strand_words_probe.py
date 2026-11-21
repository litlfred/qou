#!/usr/bin/env python3
"""qbeta_gluon_strand_words_probe — gluon strands that change the nucleon word (issue #8833).

Closed family, value and reporting rules: PREREGISTRATION.md (committed first). Lean:
QOU/QBeta/GluonLoopParity.lean (gluon-loop parity from the gamma-gamma parity theorem).

Checks
  W1  the bare nucleon word on 3 strands reproduces the ruled cell (eps_p, eps_n).
  W2  an untouched gluon strand leaves eps unchanged under the derived normalisation.
  W3  every admissible word has the gluon-loop count the Lean parity predicts
      (4 strands: 1 loop; 5 strands with 3 quark components: 2 loops).
  W4  report F for every word, reading-3 survivors, none selected.
mpmath at the proton pin, 60 dps.
"""
from __future__ import annotations

import importlib.util
import itertools
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "_gg", _ROOT / "computations/probes/qbeta_gg_lepton_pair/qbeta_gg_lepton_pair_probe.py")
gg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gg)

mp.mp.dps = 60
Q0 = mp.mpf(Q_50_DIGIT_STR)
D2 = Q0 + 1 / Q0
F_REQ = mp.mpf("2.40397")
TOL = mp.mpf("1e-40")
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def diag_all(word, n, q):
    """<b| rho(word) |b> for every basis b."""
    out = {}
    for b in range(2 ** n):
        v = {b: mp.mpf(1)}
        for (i, s) in reversed(word):
            v = gg.apply_crossing(v, n, i, s, q)
        out[b] = v.get(b, mp.mpf(0))
    return out


def quark_downs(b, n):
    return bin(b >> (n - 3)).count("1")


def eps_pair(diag, n, c, q):
    res = {}
    for nd, key in ((1, "p"), (2, "n")):
        tot = mp.mpf(0)
        for b, d in diag.items():
            if quark_downs(b, n) == nd and d:
                tot += q ** (n - 2 * bin(b).count("1")) * d
        res[key] = tot / D2 ** c
    return res


def two_row_chars(diag, n):
    tr = [mp.mpf(0)] * (n + 1)
    for b, d in diag.items():
        tr[bin(b).count("1")] += d
    return [tr[d] - (tr[d - 1] if d else 0) for d in range(n // 2 + 1)]


def perm_quarks_closed(word, n):
    pos = list(range(n))
    for (i, _s) in word:
        pos[i], pos[i + 1] = pos[i + 1], pos[i]
    return set(pos[:3]) == {0, 1, 2}


def main() -> int:
    core = gg.gg_word((0, 0, 0))
    d3 = diag_all(core, 3, Q0)
    e3 = eps_pair(d3, 3, 3, Q0)
    ok1 = abs(e3["p"] - mp.mpf("0.408718179341")) < mp.mpf("1e-11") and \
        abs(e3["n"] - mp.mpf("0.331737644740")) < mp.mpf("1e-11")
    ruled = e3["n"] - e3["p"]
    check("W1_ruled_cell", ok1, f"eps_p = {mp.nstr(e3['p'], 12)}, eps_n = {mp.nstr(e3['n'], 12)}, "
          f"eps_flavour = {mp.nstr(ruled, 12)}.")
    d4 = diag_all(core, 4, Q0)
    e4 = eps_pair(d4, 4, 4, Q0)
    check("W2_untouched_gluon_strand", abs(e4["p"] - e3["p"]) < TOL and abs(e4["n"] - e3["n"]) < TOL,
          "V0^3 (x) idle strand, gluon strand summed, / [2]^4: eps unchanged (premise N2).")

    rows, ok3 = [], True
    for n, L in ((4, 6), (5, 5)):
        verts = range(n - 2)
        for ln in range(1, L + 1):
            for vs in itertools.product(verts, repeat=ln):
                if max(vs) + 2 < 3:          # must touch a gluon strand (index >= 3)
                    continue
                X = gg.gg_word(vs)
                if not perm_quarks_closed(X, n):
                    continue
                W = X + core
                k, _lk, _sc = gg.strand_data(W, n)
                # quark components: cycles of the permutation restricted to {0,1,2}
                pos = list(range(n))
                for (i, _s) in W:
                    pos[i], pos[i + 1] = pos[i + 1], pos[i]
                end = {pos[p]: p for p in range(n)}
                seen, qc = set(), 0
                for s0 in range(3):
                    if s0 in seen:
                        continue
                    qc += 1
                    s = s0
                    while s not in seen:
                        seen.add(s)
                        s = end[s]
                g = k - qc
                if qc == 3:
                    ok3 &= (g == 1) if n == 4 else (g == 2)
                diag = diag_all(W, n, Q0)
                e = eps_pair(diag, n, k, Q0)
                F = (e["n"] - e["p"]) / ruled
                chars = two_row_chars(diag, n)
                r3 = all(x > -TOL for x in chars)
                rows.append({"n": n, "X": "".join(f"V{i}" for i in vs), "vertices": ln,
                             "components": k, "quark_components": qc, "gluon_loops": g,
                             "eps_p": mp.nstr(e["p"], 20), "eps_n": mp.nstr(e["n"], 20),
                             "F": mp.nstr(F, 20), "two_row_chars": [mp.nstr(x, 12) for x in chars],
                             "reading3": r3})
    check("W3_gluon_loop_parity", ok3,
          "every admissible word with 3 quark components has 1 gluon loop on 4 strands and 2 on "
          "5 strands (Lean four_strands_one_gluon_loop, five_strands_two_gluon_loops).")

    def rng(sel):
        v = [mp.mpf(r["F"]) for r in rows if sel(r)]
        return (f"[{mp.nstr(min(v), 8)}, {mp.nstr(max(v), 8)}] ({len(v)} words)") if v else "none"
    surv = [r for r in rows if r["reading3"]]
    det = (f"{len(rows)} admissible words. F all: n=4 {rng(lambda r: r['n']==4)}, n=5 "
           f"{rng(lambda r: r['n']==5)}. Reading-3 survivors: n=4 {rng(lambda r: r['n']==4 and r['reading3'])}, "
           f"n=5 {rng(lambda r: r['n']==5 and r['reading3'])}. |F| >= F_required: "
           f"{sum(abs(mp.mpf(r['F'])) >= F_REQ for r in rows)} words, of which reading-3 survivors "
           f"{sum(abs(mp.mpf(r['F'])) >= F_REQ for r in surv)}. None selected.")
    check("W4_report", True, det)
    big = sorted(rows, key=lambda r: -abs(mp.mpf(r["F"])))[:10]
    for r in big:
        print("   ", r["n"], r["X"], "F =", r["F"][:12], "c =", r["components"], "r3 =", r["reading3"])

    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-gluon-strand-words", engine="mpmath")
    for nm, o, d in RESULTS:
        wb.add_assertion(nm, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="1e-40", source=d)
    wb.save({
        "description": ("Nucleon word V0^3 with gamma-gamma-attached gluon strands on 4 and 5 "
                        "strands; F = eps_flavour(W)/eps_flavour(V0^3) under the derived "
                        "normalisation; reading-3 filter. Nothing selected."),
        "q0": Q_50_DIGIT_STR, "F_required": "2.40397", "rows": rows,
    })
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
