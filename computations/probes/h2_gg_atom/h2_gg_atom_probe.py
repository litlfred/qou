#!/usr/bin/env python3
"""h2_gg_atom_probe.py — H2 with a γγ-built nucleon block V^m (owner decision C, "try γγ first").

Bean `qou-a1hh`, PR #7741. Recipe: `preregistration.md` here (committed 97dacc709d3 before this file).
Reuses `../h2_one_rule/h2_one_rule_probe.py` unchanged (mpmath 40 dps, convention D, proton pin); only the
nucleon block changes: production `V^3·TAIL_p·σ0σ0` -> V^m, m in {3..7}. Levels are read from m = 1 here
(the H2 one-rule probe read from 3; calibration K0 compares levels 3..12 only).
Trace ratio reported, never used to select (ruling B). Nothing fitted, selected against data, or wired.

-- Ref: [manuscript] prop:ilp-covalent-bond; bean qou-a1hh; bean qou-ales
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)  # the h2_one_rule base works at 40 dps; stated here so this
                                # probe does not rely on an import side effect two modules away

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_one_rule"))
import h2_one_rule_probe as base  # noqa: E402

kct, mjw, cf = base.kct, base.mjw, base.cf
ONE, ZERO, TOL, N, y, log = base.ONE, base.ZERO, base.TOL, base.N, base.y, base.log
from qou_substrate.witness import WitnessBuilder  # noqa: E402

PRODUCTION_BLOCK = kct.proton_block


def two_row(n):
    return base.two_row(n)


def level_chars(diag, n, lo=1):
    out = {}
    for m in range(lo, n + 1):
        for mu in two_row(m):
            acc = ZERO
            for lam, d in diag.items():
                rows = base.tableau_rows(lam)
                s = mp.fsum(v for v, r in zip(d, rows) if base.restricted(r, m) == mu)
                acc += y(lam) / y(mu) * s
            out[(m, mu)] = acc
    return out


def h2_rows(block_fn, lo):
    kct.proton_block = block_fn
    results = {}
    for ename in kct.ELECTRONS:
        kct.ELECTRON = ename
        for atom2 in ("pe", "ep"):
            tag = f"electron={ename},atom2={atom2}"
            w1, _ = kct.atom("pe", False)
            w2, _ = kct.atom(atom2, False)
            x = w1 + kct.shift(w2, 6)
            prefix = {}
            for lam in two_row(N):
                dim = kct.cols(list(lam))[1]
                I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
                prefix[lam] = kct.right_apply(I, x, list(lam))
            dx = {lam: [prefix[lam][i][i] for i in range(len(prefix[lam]))] for lam in prefix}
            trx = mp.fsum(y(l) * mp.fsum(dx[l]) for l in two_row(N))
            rows = []
            for k in (0, 1, 2, 3):
                for s in ((None,) if k == 0 else (4, 5)):
                    d = dx if k == 0 else base.diag_of(base.V(s) * k, N, prefix)
                    lc = level_chars(d, N, lo)
                    tr = mp.fsum(y(l) * lc[(N, l)] for l in two_row(N))
                    fails = sorted({m for (m, mu), v in lc.items() if v < -TOL})
                    rows.append({"K": "none" if k == 0 else f"V^{k}", "site": s, "ratio": mp.nstr(tr / trx, 20),
                                 "trace_decreases": bool(tr < trx - TOL),
                                 "reading3_every_level": not fails, "failing_levels": fails,
                                 "negative": [f"{m}:{mu}={mp.nstr(v, 8)}" for (m, mu), v in sorted(lc.items()) if v < -TOL],
                                 "chars": {f"{m}:{mu}": mp.nstr(v, 20) for (m, mu), v in sorted(lc.items())}})
                    r = rows[-1]
                    log(f"  {tag} K={r['K']}@{s}: ratio {r['ratio'][:10]} every-level={r['reading3_every_level']} "
                        f"fails {fails} {r['negative'][:4]}")
            results[tag] = {"tr_x": mp.nstr(trx, 30), "rows": rows}
    kct.proton_block = PRODUCTION_BLOCK
    return results


def vm(m):
    return lambda: base.V(0) * m


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}")

    # K0: production block reproduces the committed h2-one-rule witness (levels 3..12)
    old = json.loads((HERE.parent / "h2_one_rule" / "h2-one-rule.witness.json").read_text())["results"]
    log("K0: recomputing production-block rows")
    new = h2_rows(PRODUCTION_BLOCK, 3)
    worst = mp.mpf(0)
    for tag, res in old.items():
        for ro, rn in zip(res["rows"], new[tag]["rows"]):
            for key, v in ro["chars"].items():
                worst = max(worst, abs(mp.mpf(v) - mp.mpf(rn["chars"][key])))
    check("K0_production_block_reproduces_h2_one_rule", worst < mp.mpf("1e-18"), f"max diff {mp.nstr(worst, 5)}")

    # K5: chi_(3)(V^m) = 1 and the H3 levels of the bare nucleon
    h3 = {}
    ok5 = True
    for m in range(3, 8):
        w = base.V(0) * m
        lc = level_chars(base.diag_of(w, 3), 3, 1)
        ok5 &= abs(lc[(3, (3,))] - 1) < TOL and abs(lc[(3, (3,))] - mjw.chi([3], w)) < TOL
        fails = sorted({k for (k, mu), v in lc.items() if v < -TOL})
        h3[f"V^{m}"] = {"reading3_every_level": not fails, "failing_levels": fails,
                        "chars": {f"{k}:{mu}": mp.nstr(v, 20) for (k, mu), v in sorted(lc.items())}}
        log(f"H3 V^{m}: every-level={not fails} " + ", ".join(f"{k}:{mu}={mp.nstr(v, 10)}" for (k, mu), v in sorted(lc.items())))
    check("K5_chi3_Vm_is_1", ok5, "trivial rep: sigma -> q, sigma^-1 -> q^-1")

    results = {}
    for m in range(3, 8):
        log(f"H2 with nucleon block V^{m}")
        results[f"V^{m}"] = h2_rows(vm(m), 1)

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("h2-gg-atom", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)",
        "description": "PROBE (bean qou-a1hh, owner decision C 'try gamma-gamma first'): H2 with nucleon block V^m, "
                       "m in 3..7, electron fixed (Tw0 or trefoil), no p-e or junction letter, bond K in {none,V,V^2,V^3} "
                       "at s=4,5; reading 3 at every level 1..12, convention D. Pre-registered. Nothing fitted or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "h3_nucleon": h3,
        "results": results,
    })
    log(f"witness: {out}")
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
