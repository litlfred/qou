#!/usr/bin/env python3
"""h2_torus_electron_probe.py — electron from a single crossing: sigma0^m sigma1^t (T(2,m) stabilised).

Owner 2026-11-15: "b, then a as fall back". Bean qou-a1hh, PR #7741.
Recipe: preregistration.md here (committed 0823f764c57 before this file).
Reuses h2_gg_atom / h2_one_rule unchanged (mpmath 40 dps, convention D, proton pin).
Trace ratios reported, never used to select. Nothing fitted, selected against data, or wired.

-- Ref: [manuscript] prop:ilp-covalent-bond; bean qou-a1hh; bean qou-ales
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)  # the h2_one_rule base works at 40 dps; stated here so this
                                # probe does not rely on an import side effect two modules away

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
sys.path.insert(0, str(HERE.parent / "h2_one_rule"))
import h2_gg_atom_probe as gg  # noqa: E402

base, kct = gg.base, gg.kct
ONE, ZERO, TOL, N, y, log = base.ONE, base.ZERO, base.TOL, base.N, base.y, base.log
H = base.H
from qou_substrate.witness import WitnessBuilder  # noqa: E402

NUCLEONS = {"V3": base.V(0) * 3, "V6": base.V(0) * 6}
MS = [m for m in range(-9, 10) if m % 2]


def letter(g, sign):
    return (ONE, ZERO, g) if sign > 0 else (ONE, -H, g)


def electron(m, t):
    return [letter(0, m)] * abs(m) + [letter(1, t)]


def chars(word, n, lo=1):
    return gg.level_chars(base.diag_of(word, n), n, lo)


def fails(lc):
    return sorted({k for (k, mu), v in lc.items() if v < -TOL})


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}: {src}")

    # K0: trefoil m=3,t=+1 reproduces chi_(2,1) = -1 (h2_gg_atom/level6_trefoil_derivation.py)
    lt = chars(electron(3, 1), 3)
    check("K0_trefoil_chi21_minus_one", abs(lt[(3, (2, 1))] + 1) < TOL, f"chi_(2,1) = {mp.nstr(lt[(3, (2, 1))], 15)}")

    c21p = {n: chars(w, 3)[(3, (2, 1))] for n, w in NUCLEONS.items()}
    log(f"nucleon chi_(2,1): {{{', '.join(f'{n}: {mp.nstr(v, 12)}' for n, v in c21p.items())}}}")

    rows, atoms_ok, p1_ok = {}, [], True
    for m in MS:
        for t in (1, -1):
            e = electron(m, t)
            lc3 = chars(e, 3)
            f3 = fails(lc3)
            c3, c21 = lc3[(3, (3,))], lc3[(3, (2, 1))]
            r = {"T1_pass": not f3, "T1_fails": f3, "chi3_e": mp.nstr(c3, 20), "chi21_e": mp.nstr(c21, 20),
                 "chars_e": {f"{k}:{mu}": mp.nstr(v, 20) for (k, mu), v in sorted(lc3.items())}, "atoms": {}}
            for pn, P in NUCLEONS.items():
                atom = P + [(c, d, g + 3) for c, d, g in e]
                lc6 = chars(atom, 6)
                f6 = fails(lc6)
                pred = (c3 + c21p[pn] * c21) >= -TOL
                got = lc6[(6, (3, 3))] >= -TOL
                p1_ok &= (pred == got)
                r["atoms"][pn] = {"fails": f6, "atom_33": mp.nstr(lc6[(6, (3, 3))], 20), "P1_pred_pass": bool(pred)}
                if not f6:
                    atoms_ok.append((m, t, pn))
                log(f"m={m:+d},t={t:+d},{pn}: T1 {'pass' if not f3 else f'fail {f3}'}; atom fails {f6}; "
                    f"chi3 {mp.nstr(c3, 8)} chi21 {mp.nstr(c21, 8)} (3,3) {mp.nstr(lc6[(6, (3, 3))], 8)}")
            rows[f"m={m},t={t}"] = r
    check("P1_level6_sign_matches_closed_form", p1_ok, "sign of chi3(e)+chi21(p)chi21(e) vs computed (3,3)")

    chiral = {}
    for m in MS:
        for t in (1, -1):
            a, b = rows[f"m={m},t={t}"]["chars_e"], rows[f"m={-m},t={-t}"]["chars_e"]
            chiral[f"m={m},t={t}"] = any(abs(mp.mpf(a[x]) - mp.mpf(b[x])) > TOL for x in a)

    stage2 = {}
    # T3 runs on every atom passing levels 1-6, as pre-registered; T1 (electron alone) is NOT a gate.
    for m, t, pn in atoms_ok:
        P, e = NUCLEONS[pn], electron(m, t)
        w1 = P + [(c, d, g + 3) for c, d, g in e]
        for atom2 in ("pe", "ep"):
            w2 = w1 if atom2 == "pe" else e + [(c, d, g + 3) for c, d, g in P]
            x = w1 + kct.shift(w2, 6)
            prefix = {}
            for lam in base.two_row(N):
                dim = kct.cols(list(lam))[1]
                I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
                prefix[lam] = kct.right_apply(I, x, list(lam))
            dx = {lam: [prefix[lam][i][i] for i in range(len(prefix[lam]))] for lam in prefix}
            trx = mp.fsum(y(l) * mp.fsum(dx[l]) for l in base.two_row(N))
            out = []
            for kk in (0, 1, 2, 3):
                for s in ((None,) if kk == 0 else (4, 5)):
                    d = dx if kk == 0 else base.diag_of(base.V(s) * kk, N, prefix)
                    lc = gg.level_chars(d, N, 1)
                    tr = mp.fsum(y(l) * lc[(N, l)] for l in base.two_row(N))
                    f = fails(lc)
                    out.append({"K": "none" if kk == 0 else f"V^{kk}", "site": s, "every_level": not f,
                                "fails": f, "ratio": mp.nstr(tr / trx, 20)})
                    log(f"T3 m={m:+d},t={t:+d},{pn} atom2={atom2} K={out[-1]['K']}@{s}: every-level={not f} fails {f}")
            stage2[f"m={m},t={t},{pn},atom2={atom2}"] = out

    full = [(tg, o["K"], o["site"]) for tg, v in stage2.items() for o in v if o["every_level"]]
    outcome = "iii" if not atoms_ok else ("i" if full else "ii")
    log(f"OUTCOME ({outcome}): atoms passing {atoms_ok}; H2 cells passing {full}")

    wb = WitnessBuilder("h2-torus-electron", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)",
        "description": "PROBE (bean qou-a1hh, owner 'b, then a as fall back'): electron = sigma0^m sigma1^t, m odd in "
                       "[-9,9], t=+-1 (T(2,m) stabilised); nucleons V^3, V^6; reading 3 every level, convention D. "
                       "Pre-registered. Nothing fitted or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "outcome": outcome, "nucleon_chi21": {n: mp.nstr(v, 20) for n, v in c21p.items()},
        "electrons": rows, "mirror_differs": chiral, "h2": stage2,
        "atoms_passing": [list(map(str, a)) for a in atoms_ok], "h2_passing": [list(map(str, f)) for f in full],
    })
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
