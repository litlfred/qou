#!/usr/bin/env python3
"""h2_weak_vertex_electron_probe.py — gamma-gamma electron with one crossing replaced by the weak vertex.

Owner 2026-11-15: "b, then a as fall back". Bean qou-a1hh, PR #7741.
Recipe: preregistration.md here (committed b5b044aa3ac before this file).
W = sigma P_R + sigma^-1 P_L = q^-1 (2 sigma - h)/[2]  (weakVertex_eq_split); mirror W' = sigma P_L + sigma^-1 P_R.
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
q = base.Q
h = q - 1 / q
b2 = q + 1 / q
from qou_substrate.witness import WitnessBuilder  # noqa: E402

P = base.V(0) * 3
W_TOK = (2 / (q * b2), -h / (q * b2))            # W  = c sigma + d
WP_TOK = (1 + h / b2, -h + h / (q * b2))          # W' = c sigma + d
C21_V3 = -(q**4 - q**2 + 1) * (q**8 - 2 * q**6 - 2 * q**2 + 1) / q**6


def dressed(k, j, tok, s=0):
    w = base.V(s) * k
    c, d, g = w[j]
    w[j] = (tok[0], tok[1], g)
    return w


def chars(word, n, lo=1):
    return gg.level_chars(base.diag_of(word, n), n, lo)


def every_level(lc):
    return sorted({m for (m, mu), v in lc.items() if v < -TOL})


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}: {src}")

    # K1: W eigenvalues on the 2-strand irreps: W on (2) = q^-1, on (1,1) = -q^-1 (so W^2 = q^-2)
    w2 = chars([(W_TOK[0], W_TOK[1], 0)], 2)
    check("K1_W_eigenvalues", abs(w2[(2, (2,))] - 1 / q) < TOL, f"chi_(2)(W) = {mp.nstr(w2[(2, (2,))], 15)}")

    rows = {}
    p1_ok = True
    for k in range(1, 7):
        for j in range(2 * k):
            for vname, tok in (("W", W_TOK), ("Wp", WP_TOK)):
                e = dressed(k, j, tok)
                lc3 = chars(e, 3)
                f3 = every_level(lc3)
                atom = P + [(c, d, g + 3) for c, d, g in e]
                lc6 = chars(atom, 6)
                f6 = every_level(lc6)
                c3, c21 = lc3[(3, (3,))], lc3[(3, (2, 1))]
                # P1: level-6 (3,3) of the hydrogen atom in closed form; chi_(2,1) is a trace over a 2-dim block,
                # and level_chars normalises (3,3) by y; compare SIGN and the ratio to the (6) block.
                pred_sign = (c3 + C21_V3 * c21 * mp.mpf(1)) >= -TOL
                got_sign = lc6[(6, (3, 3))] >= -TOL
                p1_ok &= (pred_sign == got_sign)
                tag = f"k={k},j={j},{vname}"
                rows[tag] = {"T1_pass": not f3, "T1_fails": f3, "atom_fails": f6,
                             "chi3_e": mp.nstr(c3, 20), "chi21_e": mp.nstr(c21, 20),
                             "atom_33": mp.nstr(lc6[(6, (3, 3))], 20), "P1_pred_pass": bool(pred_sign),
                             "chars_e": {f"{m}:{mu}": mp.nstr(v, 20) for (m, mu), v in sorted(lc3.items())}}
                log(f"{tag}: T1 {'pass' if not f3 else f'fail {f3}'}; atom fails {f6}; "
                    f"chi3 {mp.nstr(c3, 8)} chi21 {mp.nstr(c21, 8)}")
    check("P1_level6_sign_matches_closed_form", p1_ok, "sign of chi3(e)+chi21(V3)chi21(e) vs computed (3,3)")

    # chirality report: W vs W' characters differ?
    chiral = {}
    for k in range(1, 7):
        for j in range(2 * k):
            a, bb = rows[f"k={k},j={j},W"]["chars_e"], rows[f"k={k},j={j},Wp"]["chars_e"]
            chiral[f"k={k},j={j}"] = any(abs(mp.mpf(a[x]) - mp.mpf(bb[x])) > TOL for x in a)

    # T3: full H2 for atoms whose electron passes T1 and whose atom passes levels 1..6
    stage2 = {}
    for tag, r in rows.items():
        if not (r["T1_pass"] and not r["atom_fails"]):
            continue
        k, j, vname = tag.split(",")
        k, j = int(k[2:]), int(j[2:])
        tok = W_TOK if vname == "W" else WP_TOK
        e = dressed(k, j, tok)
        for atom2 in ("pe", "ep"):
            w1 = P + [(c, d, g + 3) for c, d, g in e]
            w2 = w1 if atom2 == "pe" else e + [(c, d, g + 3) for c, d, g in P]
            x = w1 + kct.shift(w2, 6)
            prefix = {}
            for lam in base.two_row(N):
                dim = kct.cols(list(lam))[1]
                I = [[ONE if i == jj else ZERO for jj in range(dim)] for i in range(dim)]
                prefix[lam] = kct.right_apply(I, x, list(lam))
            dx = {lam: [prefix[lam][i][i] for i in range(len(prefix[lam]))] for lam in prefix}
            trx = mp.fsum(y(l) * mp.fsum(dx[l]) for l in base.two_row(N))
            out = []
            for kk in (0, 1, 2, 3):
                for s in ((None,) if kk == 0 else (4, 5)):
                    d = dx if kk == 0 else base.diag_of(base.V(s) * kk, N, prefix)
                    lc = gg.level_chars(d, N, 1)
                    tr = mp.fsum(y(l) * lc[(N, l)] for l in base.two_row(N))
                    f = every_level(lc)
                    out.append({"K": "none" if kk == 0 else f"V^{kk}", "site": s, "every_level": not f,
                                "fails": f, "ratio": mp.nstr(tr / trx, 20)})
                    log(f"T3 {tag} atom2={atom2} K={out[-1]['K']}@{s}: every-level={not f} fails {f}")
            stage2[f"{tag},atom2={atom2}"] = out

    t1 = [t for t, r in rows.items() if r["T1_pass"]]
    atoms = [t for t, r in rows.items() if r["T1_pass"] and not r["atom_fails"]]
    full = [(t, o["K"], o["site"]) for t, v in stage2.items() for o in v if o["every_level"]]
    outcome = "iii" if not t1 else ("i" if full else "ii")
    log(f"OUTCOME ({outcome}): T1 pass {len(t1)}/{len(rows)}; atoms pass {atoms}; H2 cells passing {full}")

    wb = WitnessBuilder("h2-weak-vertex-electron", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)",
        "description": "PROBE (bean qou-a1hh, owner 'b, then a as fall back'): electron = V^k (k<=6) with one letter "
                       "replaced by the weak vertex W (or mirror W'); nucleon V^3; reading 3 every level, convention D. "
                       "Pre-registered. Nothing fitted or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "outcome": outcome, "electrons": rows, "chirality_W_vs_Wp_differs": chiral, "h2": stage2,
        "t1_passing": t1, "atoms_passing": atoms, "h2_passing": [list(map(str, f)) for f in full],
    })
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
