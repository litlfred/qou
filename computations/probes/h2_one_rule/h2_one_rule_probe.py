#!/usr/bin/env python3
"""h2_one_rule_probe.py — H2 under the one rule: γγ bonds, reading 3 at every level.

Bean `qou-a1hh`, PR #7741. Recipe: `preregistration.md` in this directory (committed 4ff6d8d594d before this file).

Cell: no p–e letter, no junction letter (neither is a γγ word). Bond K ∈ {none, V, V², V³}, V = σ_sσ_{s+1}⁻¹, s = 4, 5;
knot requirement dropped. Reading 3 is checked at every level m = 3..12 by closing strands from the top with the
convention-D Markov trace:

    χ_μ(E_{n→m} W) = Σ_λ (y_λ / y_μ) Σ_{T : T|₁..ₘ has shape μ} W_TT,     y_λ = [λ₁−λ₂+1]_q / [2]_qⁿ.

Trace drop tr(xK) < tr(x) is reported as a column, not used to select (owner decision B pending).
mpmath 40 dps throughout; no float. Nothing fitted, selected against data, or wired.

-- Ref: [manuscript] prop:ilp-covalent-bond; bean qou-a1hh; bean qou-ales; computations/probes/gg_ntower
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
import knot_convoluted_tensor_h2_probe as kct  # noqa: E402
cf, mjw = kct.cf, kct.mjw
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
Q, H, ZD = cf.Q, cf.H, cf.Z_D
ONE, ZERO = mp.mpf(1), mp.mpf(0)
TOL = mp.mpf("1e-25")
N = 12
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def qint(m):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def y(lam):
    lam = tuple(lam) + (0,) * (2 - len(lam))
    return qint(lam[0] - lam[1] + 1) / qint(2) ** (lam[0] + lam[1])


def two_row(n):
    return [tuple(l) for l in mjw.two_row(n)]


_ROWS: dict = {}


def tableau_rows(shape):
    """For each SYT (same order as cf.sigmas), the row (0/1) of entries 1..n."""
    key = tuple(shape)
    if key not in _ROWS:
        syts, _ = cf.standard_young_tableaux(list(shape))
        cells = cf.young_cells(list(shape))
        n = sum(shape)
        _ROWS[key] = [[cells[t[e]][0] for e in range(1, n + 1)] for t in syts]
    return _ROWS[key]


def restricted(rows, m):
    r1 = sum(rows[:m])
    return (m - r1, r1) if r1 else (m,)


def level_chars(diag, n):
    """diag[λ] = list of W_TT over SYT of λ (λ two-row ⊢ n). Returns {(m, μ): χ_μ(E_{n→m} W)}."""
    out = {}
    for m in range(3, n + 1):
        for mu in two_row(m):
            acc = ZERO
            for lam, d in diag.items():
                rows = tableau_rows(lam)
                s = mp.fsum(v for v, r in zip(d, rows) if restricted(r, m) == mu)
                acc += y(lam) / y(mu) * s
            out[(m, mu)] = acc
    return out


def diag_of(word, n, prefix=None):
    out = {}
    for lam in two_row(n):
        dim = kct.cols(list(lam))[1]
        if prefix is None:
            I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
            M = kct.right_apply(I, word, list(lam))
            out[lam] = [M[i][i] for i in range(dim)]
        else:
            Kc = kct.sparse_word(word, list(lam))
            P = prefix[lam]
            out[lam] = [mp.fsum(P[T][j] * w for j, w in Kc[T].items()) for T in range(dim)]
    return out


def V(s):
    return [(ONE, ZERO, s), (ONE, -H, s + 1)]


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}")

    # K1 y formula vs committed witness
    ok = True
    for n in (3, 12):
        yw = cf.load_y(n)
        for lam in two_row(n):
            if abs(y(lam) - yw[lam]) > TOL:
                ok = False
    check("K1_y_formula_matches_witness_n3_n12", ok, "y-lambda-at-q0.witness.json")

    # K2/K3/K4 on an n=6 test word
    w6 = kct.electron(0)[:2] + [(ONE, -H, 2), (ONE, ZERO, 3), (ONE, ZERO, 4), (ONE, -H, 1), (ONE, ZERO, 0)]
    d6 = diag_of(w6, 6)
    lc6 = level_chars(d6, 6)
    check("K2_top_level_is_chi", all(abs(lc6[(6, l)] - mjw.chi(list(l), w6)) < TOL for l in two_row(6)), "mjw.chi")
    tr6 = mp.fsum(y(l) * lc6[(6, l)] for l in two_row(6))
    check("K3_closing_preserves_trace", all(abs(mp.fsum(y(mu) * lc6[(m, mu)] for mu in two_row(m)) - tr6) < TOL
                                             for m in range(3, 7)), "sum_mu y_mu chi_mu")
    a = [(ONE, ZERO, 0), (ONE, -H, 2), (ONE, ZERO, 3)]
    b = [(ONE, ZERO, 1), (ONE, ZERO, 3), (ONE, -H, 0)]
    lc = level_chars(diag_of(a + [(ONE, ZERO, 4)] + b, 6), 6)
    check("K4_E_of_a_sigma_b_is_z_ab", all(abs(lc[(5, mu)] - ZD * mjw.chi(list(mu), a + b)) < TOL for mu in two_row(5)),
          "Markov property, top closing")

    results = {}
    for ename in kct.ELECTRONS:
        kct.ELECTRON = ename
        for atom2 in ("pe", "ep"):
            tag = f"electron={ename},atom2={atom2}"
            w1, lab1 = kct.atom("pe", False)
            w2, lab2 = kct.atom(atom2, False)
            x = w1 + kct.shift(w2, 6)
            prefix = {}
            for lam in two_row(N):
                dim = kct.cols(list(lam))[1]
                I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
                prefix[lam] = kct.right_apply(I, x, list(lam))
            dx = {lam: [prefix[lam][i][i] for i in range(len(prefix[lam]))] for lam in prefix}
            trx = mp.fsum(y(l) * mp.fsum(dx[l]) for l in two_row(N))
            log(f"{tag}: prefix built, junction {(lab1[-1], lab2[0])}")
            rows = []
            for k in (0, 1, 2, 3):
                for s in ((None,) if k == 0 else (4, 5)):
                    word = V(s) * k if k else []
                    d = dx if k == 0 else diag_of(word, N, prefix)
                    lc = level_chars(d, N)
                    tr = mp.fsum(y(l) * lc[(N, l)] for l in two_row(N))
                    fails = sorted({m for (m, mu), v in lc.items() if v < -TOL})
                    neg = [f"{m}:{mu}={mp.nstr(v, 8)}" for (m, mu), v in sorted(lc.items()) if v < -TOL]
                    row = {"K": "none" if k == 0 else f"V^{k}", "site": s, "ratio": mp.nstr(tr / trx, 20),
                           "trace_decreases": bool(tr < trx - TOL), "reading3_top_only": all(lc[(N, l)] >= -TOL for l in two_row(N)),
                           "reading3_every_level": not fails, "failing_levels": fails, "negative": neg,
                           "chars": {f"{m}:{mu}": mp.nstr(v, 20) for (m, mu), v in sorted(lc.items())}}
                    rows.append(row)
                    log(f"{tag} K={row['K']}@{s}: ratio {row['ratio'][:10]} top-only={row['reading3_top_only']} "
                        f"every-level={row['reading3_every_level']} failing levels {fails} {neg[:6]}")
            results[tag] = {"junction_pair": [lab1[-1], lab2[0]], "tr_x": mp.nstr(trx, 30), "rows": rows}

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("h2-one-rule", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through the committed y-lambda-at-q0 witness (proton pin) via cf.Q",
        "description": "PROBE (bean qou-a1hh): H2 under the one rule (owner 2026-11-15). No p-e letter, no junction "
                       "letter; bond K in {none, V, V^2, V^3}, V = sigma_s sigma_{s+1}^-1, s = 4, 5; reading 3 at "
                       "every level m = 3..12 by convention-D top closing. Pre-registered. Nothing fitted or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "constants": {"q0": mp.nstr(Q, 40), "h": mp.nstr(H, 40), "z_D": mp.nstr(ZD, 40)},
        "results": results,
    })
    log(f"witness: {out}")
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
