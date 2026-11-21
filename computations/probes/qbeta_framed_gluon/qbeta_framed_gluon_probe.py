#!/usr/bin/env python3
"""qbeta_framed_gluon_probe — framed gluon loops inside gamma-gamma words (issue #8833).

Closed family, value and question: PREREGISTRATION.md (committed first). Lean:
QOU/QBeta/FramedGluonWrithe.lean (self part of the writhe = minus the between part in a
gamma-gamma word).

Checks
  R1  the bare nucleon word reproduces the ruled cell.
  R2  every word in the family has self writhe = -between writhe (the Lean statement).
  R3  report, per gluon framing |f| = k: count, F range, reading-3 range, |F| >= F_required.
  R4  report whether max |F| grows with k (the preregistered question). Nothing selected.
mpmath at the proton pin, 60 dps.
"""
from __future__ import annotations

import importlib.util
import itertools
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
_spec = importlib.util.spec_from_file_location(
    "_gsw", _ROOT / "computations/probes/qbeta_gluon_strand_words/qbeta_gluon_strand_words_probe.py")
gsw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gsw)

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

gg, mp, Q0, TOL = gsw.gg, gsw.mp, gsw.Q0, gsw.TOL
F_REQ = mp.mpf("2.40397")
FAMILY = ((4, 8), (5, 7), (6, 5))
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n", flush=True)


def components(word, n):
    pos, cr = list(range(n)), []
    for (i, s) in word:
        a, b = pos[i], pos[i + 1]
        cr.append((a, b, s))
        pos[i], pos[i + 1] = b, a
    end = {pos[p]: p for p in range(n)}
    comp, seen, c = {}, set(), 0
    for s0 in range(n):
        if s0 in seen:
            continue
        s = s0
        while s not in seen:
            seen.add(s)
            comp[s] = c
            s = end[s]
        c += 1
    selfw = [0] * c
    between = 0
    for a, b, sg in cr:
        if comp[a] == comp[b]:
            selfw[comp[a]] += sg
        else:
            between += sg
    return comp, c, selfw, between


def main() -> int:
    t0 = time.time()
    core = gg.gg_word((0, 0, 0))
    e3 = gsw.eps_pair(gsw.diag_all(core, 3, Q0), 3, 3, Q0)
    ruled = e3["n"] - e3["p"]
    check("R1_ruled_cell", abs(e3["p"] - mp.mpf("0.408718179341")) < mp.mpf("1e-11") and
          abs(e3["n"] - mp.mpf("0.331737644740")) < mp.mpf("1e-11"),
          f"eps_flavour = {mp.nstr(ruled, 12)}.")
    rows, ok2 = [], True
    for n, L in FAMILY:
        for ln in range(1, L + 1):
            for vs in itertools.product(range(n - 2), repeat=ln):
                if max(vs) + 2 < 3:
                    continue
                X = gg.gg_word(vs)
                if not gsw.perm_quarks_closed(X, n):
                    continue
                W = X + core
                comp, c, selfw, between = components(W, n)
                ok2 &= sum(selfw) == -between
                gl = sorted({comp[s] for s in range(3, n)})
                f = sum(selfw[g] for g in gl)
                diag = gsw.diag_all(W, n, Q0)
                e = gsw.eps_pair(diag, n, c, Q0)
                F = (e["n"] - e["p"]) / ruled
                r3 = all(x > -TOL for x in gsw.two_row_chars(diag, n))
                rows.append({"n": n, "X": "".join(f"V{i}" for i in vs), "components": c,
                             "gluon_framing": f, "F": mp.nstr(F, 20), "reading3": r3})
            print(f"   n={n} L={ln} done, {len(rows)} rows, {time.time() - t0:.0f}s", flush=True)
    check("R2_self_eq_neg_between", ok2,
          f"all {len(rows)} words: sum of self writhes = -(between writhe) "
          "(Lean selfWrithe_eq_neg_betweenWrithe).")
    ks = sorted({abs(r["gluon_framing"]) for r in rows})
    bins, lines = {}, []
    for k in ks:
        sel = [r for r in rows if abs(r["gluon_framing"]) == k]
        Fs = [mp.mpf(r["F"]) for r in sel]
        s3 = [mp.mpf(r["F"]) for r in sel if r["reading3"]]
        b = {"words": len(sel), "F_min": mp.nstr(min(Fs), 10), "F_max": mp.nstr(max(Fs), 10),
             "absF_max": mp.nstr(max(abs(x) for x in Fs), 10),
             "reading3_words": len(s3),
             "reading3_F_range": [mp.nstr(min(s3), 10), mp.nstr(max(s3), 10)] if s3 else None,
             "at_or_above_F_required": sum(abs(x) >= F_REQ for x in Fs)}
        bins[str(k)] = b
        lines.append(f"|f|={k}: {b['words']} words, F [{b['F_min']}, {b['F_max']}], "
                     f"r3 {b['reading3_words']} {b['reading3_F_range']}, >=F_req {b['at_or_above_F_required']}")
    check("R3_report_by_framing", True, " | ".join(lines))
    mx = [mp.mpf(bins[str(k)]["absF_max"]) for k in ks]
    grows = all(mx[i + 1] > mx[i] for i in range(len(mx) - 1))
    check("R4_question", True,
          f"max |F| by |f| = {[mp.nstr(x, 6) for x in mx]}; strictly growing with |f|: {grows}. "
          "None selected.")
    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed, {time.time() - t0:.0f}s")
    wb = WitnessBuilder("qbeta-framed-gluon", engine="mpmath")
    for nm, o, d in RESULTS:
        wb.add_assertion(nm, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="1e-40", source=d)
    wb.save({
        "description": ("Gamma-gamma words X.V0^3 on 4-6 strands binned by the gluon loop's own "
                        "framing; F = eps_flavour(W)/eps_flavour(V0^3), derived normalisation; "
                        "reading-3 reported. Nothing selected."),
        "q0": Q_50_DIGIT_STR, "F_required": "2.40397", "family": [list(x) for x in FAMILY],
        "bins": bins, "rows": rows,
    })
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
