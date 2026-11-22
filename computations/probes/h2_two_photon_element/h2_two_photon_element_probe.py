#!/usr/bin/env python3
"""h2_two_photon_element_probe.py — the H2 bond as a two-photon ELEMENT, not a monomial.

Issue #8879, route 4. Recipe: PREREGISTRATION.md here (committed before this file).

An absorbed photon is gamma_s(phi) = 1 + phi0 sigma_s + phi1 sigma_{s+1} + phi01 V_s,
V_s = sigma_s sigma_{s+1}^-1 (owner ruling 2026-11-20). Only the coefficients the corpus fixes are
used: phi0 = phi1 = 0, phi01 in {q h, -q^-1 h}, h = q - q^-1, from the proved factorisation
V^3 = gamma(0,0,qh) gamma(0,0,-q^-1 h) (borromeanV3A/B_eq_switched_photon_product).

Elements per cell (10): one photon gamma_s^a (4); two photons one window (2, = V_s^3, check C1);
two photons two windows gamma_s^a gamma_s'^b, (a,b) in {(qh,-q^-1h),(-q^-1h,qh)}, both orders (4).
Element diagonals are linear combinations of monomial diagonals, so each is exact to the engine's
precision. Reuses ../h2_ruled_electron (and through it h2_gg_atom, h2_one_rule) unchanged:
mpmath 40 dps, convention D, proton pin, reading 3 at every level 1..12. Trace ratio reported,
never used to select. Nothing fitted or wired.

-- Ref: [leitner2026] prop:ilp-covalent-bond; def:photon; issue #8879
"""
from __future__ import annotations

import json
import sys
from multiprocessing import Pool
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_ruled_electron"))
import h2_ruled_electron_probe as re_  # noqa: E402

ga, base, kct, log, TOL, N = re_.ga, re_.base, re_.kct, re_.log, re_.TOL, re_.N
ONE, ZERO, H, Q, y = re_.ONE, re_.ZERO, re_.H, re_.Q, re_.y
from qou_substrate.witness import WitnessBuilder  # noqa: E402

h = Q - 1 / Q
A_PLUS, A_MINUS = Q * h, -h / Q          # the two photons of the factorisation
V = re_.V

MONOMIALS = {
    "1": [],
    "V4": V(4), "V5": V(5),
    "V4.V5": V(4) + V(5), "V5.V4": V(5) + V(4),
    "V4.V4.V4": V(4) * 3, "V5.V5.V5": V(5) * 3,
}


def elements():
    """name -> {monomial: coefficient}."""
    out = {}
    for s in (4, 5):
        for tag, a in (("+", A_PLUS), ("-", A_MINUS)):
            out[f"g{s}{tag}"] = {"1": ONE, f"V{s}": a}
        out[f"g{s}+.g{s}-"] = {"1": ONE, f"V{s}": A_PLUS + A_MINUS,
                               f"V{s}.V{s}": A_PLUS * A_MINUS}
    for s, t in ((4, 5), (5, 4)):
        for (ta, a), (tb, b) in ((("+", A_PLUS), ("-", A_MINUS)), (("-", A_MINUS), ("+", A_PLUS))):
            out[f"g{s}{ta}.g{t}{tb}"] = {"1": ONE, f"V{s}": a, f"V{t}": b, f"V{s}.V{t}": a * b}
    return out


def cell(args):
    m, atom2 = args
    kct.proton_block = ga.vm(m)
    kct.ELECTRON = re_.ELECTRON
    w1, _ = kct.atom("pe", False)
    w2, _ = kct.atom(atom2, False)
    x = w1 + kct.shift(w2, 6)
    prefix = {}
    for lam in ga.two_row(N):
        dim = kct.cols(list(lam))[1]
        I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
        prefix[lam] = kct.right_apply(I, x, list(lam))
    mons = dict(MONOMIALS)
    mons["V4.V4"] = V(4) * 2
    mons["V5.V5"] = V(5) * 2
    diag = {}
    for name, word in mons.items():
        if not word:
            diag[name] = {lam: [prefix[lam][i][i] for i in range(len(prefix[lam]))] for lam in prefix}
        else:
            diag[name] = base.diag_of(word, N, prefix)
    lc = {name: ga.level_chars(d, N, 1) for name, d in diag.items()}
    trx = mp.fsum(y(l) * lc["1"][(N, l)] for l in ga.two_row(N))
    rows = []
    for name, comb in elements().items():
        d = {lam: [mp.fsum(c * diag[mon][lam][i] for mon, c in comb.items())
                   for i in range(len(diag["1"][lam]))] for lam in diag["1"]}
        lce = ga.level_chars(d, N, 1)
        tr = mp.fsum(y(l) * lce[(N, l)] for l in ga.two_row(N))
        fails = sorted({k for (k, mu), v in lce.items() if v < -TOL})
        rows.append({"element": name, "expansion": {k: mp.nstr(v, 25) for k, v in comb.items()},
                     "reading3_every_level": not fails, "failing_levels": fails,
                     "negative": [f"{k}:{mu}={mp.nstr(v, 8)}" for (k, mu), v in sorted(lce.items()) if v < -TOL][:6],
                     "ratio": mp.nstr(tr / trx, 20),
                     "_lc": lce})
    # C1: one-window two-photon element vs V_s^3; C2 values for the witness comparison
    c1 = mp.mpf(0)
    for s in (4, 5):
        e = next(r for r in rows if r["element"] == f"g{s}+.g{s}-")["_lc"]
        v3 = lc[f"V{s}.V{s}.V{s}"]
        scale = max(abs(v) for v in v3.values())
        c1 = max(c1, max(abs(e[k] - v3[k]) for k in v3) / scale)
    v3chars = {s: {f"{k}:{mu}": mp.nstr(v, 20) for (k, mu), v in sorted(lc[f"V{s}.V{s}.V{s}"].items())}
               for s in (4, 5)}
    for r in rows:
        r["chars"] = {f"{k}:{mu}": mp.nstr(v, 20) for (k, mu), v in sorted(r.pop("_lc").items())}
    npass = sum(r["reading3_every_level"] for r in rows)
    log(f"done V^{m} atom2={atom2}: {npass}/{len(rows)} elements pass; C1 rel diff {mp.nstr(c1, 5)}")
    return {"m": m, "atom2": atom2, "tr_x": mp.nstr(trx, 30), "c1_rel_diff": mp.nstr(c1, 5),
            "v3_chars": v3chars, "rows": rows}


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name} — {src}")

    jobs = [(m, a) for m in (3, 6) for a in ("pe", "ep")]
    with Pool(len(jobs)) as pool:
        res = pool.map(cell, jobs)
    results = {f"nucleon=V^{r['m']},atom2={r['atom2']}": r for r in res}

    worst = max(mp.mpf(r["c1_rel_diff"]) for r in res)
    check("C1_one_window_element_equals_V3", worst < mp.mpf("1e-30"), f"max rel diff {mp.nstr(worst, 5)}")

    old = json.loads((HERE.parent / "h2_ruled_electron" / "h2-ruled-electron.witness.json").read_text())["results"]
    w2, n2 = mp.mpf(0), 0
    for tag, r in results.items():
        orows = {row["K"]: row for row in old[tag]["rows"]}
        for s in (4, 5):
            for key, v in r["v3_chars"][s].items():
                w2 = max(w2, abs(mp.mpf(v) - mp.mpf(orows[f"V{s}.V{s}.V{s}"]["chars"][key])))
                n2 += 1
    check("C2_V3_rows_match_h2_ruled_electron", w2 < mp.mpf("1e-18"), f"{n2} characters, max diff {mp.nstr(w2, 5)}")

    summary = {tag: {"passing": [row["element"] for row in r["rows"] if row["reading3_every_level"]]}
               for tag, r in results.items()}
    for tag, s in summary.items():
        log(f"{tag}: {s}")

    wb = WitnessBuilder("h2-two-photon-element", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)",
        "description": "PROBE (issue #8879, route 4): H2 bond as an element of photons gamma_s(0,0,a), "
                       "a in {qh, -q^-1 h} fixed by the proved factorisation of V^3; one photon, two photons one "
                       "window, two photons two windows; nucleon V^m (m=3,6), electron sigma0 sigma1 sigma0, "
                       "reading 3 at every level 1..12, convention D, proton pin. Pre-registered. Nothing fitted.",
        "weight_family": "markov_y_lambda_convention_D",
        "photon_coefficients": {"a_plus_qh": mp.nstr(A_PLUS, 30), "a_minus_neg_qinv_h": mp.nstr(A_MINUS, 30)},
        "summary": summary,
        "results": {tag: {k: v for k, v in r.items() if k != "v3_chars"} for tag, r in results.items()},
    })
    log(f"witness: {out}")
    log(f"{sum(ok for _, ok, _ in checks)}/{len(checks)} checks pass")
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
